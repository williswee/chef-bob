"""Regression tests for local privacy, import integrity, and saved-week behaviour."""
import copy
from decimal import Decimal
import importlib.util
import io
import json
import os
from pathlib import Path
import re
import tempfile
import unittest
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("chef_bob", ROOT / "scripts" / "chef_bob.py")
bob = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(bob)


def fixture(name):
    return bob.read_json(ROOT / "examples" / name)


def draft(recipe_id="test-soup", title="Test soup"):
    return f"""### {title}

**ID:** `{recipe_id}`
**Servings:** Not specified.
**Time:** Not specified.
**Review:** Imported draft.

#### Ingredients

- Carrots, quantity not specified

#### Method

Not specified in source.

#### Source

Synthetic test fixture.
"""


class LocalDataTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="chef-bob-test-")
        self.base = Path(self.temporary.name)
        self.data = bob.data_directory(self.base / "private")
        bob.initialize(self.data)

    def tearDown(self):
        self.temporary.cleanup()

    def write_json(self, name, value):
        path = self.base / name
        path.write_text(bob.json_text(value), encoding="utf-8")
        return path

    def set_profile(self, profile):
        bob.validate_profile(profile)
        (self.data / "preferences.json").write_text(bob.json_text(profile), encoding="utf-8")

    def save(self, name, plan):
        return bob.save_plan(self.data, self.write_json(name, plan))

    def snapshot(self):
        return {path.name: path.read_bytes() for path in self.data.iterdir() if path.is_file()}

    def test_rejects_checkout_and_symlink_targets(self):
        for path in (ROOT, ROOT / "private", ROOT / "missing" / "nested"):
            with self.subTest(path=path), self.assertRaises(bob.ValidationError):
                bob.data_directory(path)
        alias = self.base / "checkout-link"
        alias.symlink_to(ROOT, target_is_directory=True)
        with self.assertRaises(bob.ValidationError):
            bob.data_directory(alias / "private")
        with mock.patch.dict(os.environ, {"CHEF_BOB_DATA_DIR": str(alias / "private")}):
            with self.assertRaises(bob.ValidationError):
                bob.data_directory()

    def test_env_directory_and_private_file_symlink(self):
        with mock.patch.dict(os.environ, {"CHEF_BOB_DATA_DIR": str(self.data)}):
            self.assertEqual(bob.data_directory(), self.data)
        preference_path = self.data / "preferences.json"
        preference_path.unlink()
        preference_path.symlink_to(ROOT / "templates" / "preferences.json")
        with self.assertRaisesRegex(bob.ValidationError, "symlink"):
            bob.load_data(self.data)

    def test_init_preserves_custom_profile_recipes_and_history(self):
        self.set_profile(fixture("preferences-example.json"))
        self.save("week.json", fixture("week-one.json"))
        path = self.base / "recipe.md"
        path.write_text(draft(), encoding="utf-8")
        bob.add_recipe(self.data, path)
        before = self.snapshot()
        bob.initialize(self.data)
        self.assertEqual(before, self.snapshot())

    def test_invalid_profile_covers_types_ranges_timezone_and_cycles(self):
        original = fixture("preferences-example.json")
        cases = [
            ("household", "servings", 0),
            ("household", "adults", True),
            ("carb_cycle", "pattern", "RRXN"),
            ("carb_cycle", "start_index", 6),
            ("carb_cycle", "skip_behavior", "advance"),
            ("planning", "max_active_minutes", -1),
            ("diet", "allergies", "peanut"),
            ("notifications", "enabled", "false"),
        ]
        for group, key, value in cases:
            profile = copy.deepcopy(original)
            profile[group][key] = value
            with self.subTest(group=group, key=key), self.assertRaises(bob.ValidationError):
                bob.validate_profile(profile)
        profile = copy.deepcopy(original)
        profile["timezone"] = "Not/A_Timezone"
        with self.assertRaisesRegex(bob.ValidationError, "timezone"):
            bob.validate_profile(profile)
        profile = copy.deepcopy(original)
        profile["notifications"]["schedules"] = [{"name": "daily", "time": "25:00", "days": ["monday"]}]
        with self.assertRaisesRegex(bob.ValidationError, "HH:MM"):
            bob.validate_profile(profile)
        profile = copy.deepcopy(original)
        profile["temporary_overrides"] = [{"date": "2026-01-05", "slot": "dinner", "allergies": []}]
        with self.assertRaisesRegex(bob.ValidationError, "allergies cannot be removed"):
            bob.validate_profile(profile)

    def test_duplicate_imports_preserve_both_original_files(self):
        path = self.base / "recipe.md"
        path.write_text(draft(), encoding="utf-8")
        bob.add_recipe(self.data, path)
        self.assertIn('<a id="test-soup"></a>', (self.data / "recipes.md").read_text())
        before = self.snapshot()
        for content in (draft(), draft("other-id", "TEST   SOUP"), draft("starter-tomato-chickpea-rice", "Other name")):
            path.write_text(content, encoding="utf-8")
            with self.assertRaisesRegex(bob.ValidationError, "Duplicate"):
                bob.add_recipe(self.data, path)
            self.assertEqual(before, self.snapshot())

    def test_incomplete_import_fails_without_mutation(self):
        path = self.base / "recipe.md"
        path.write_text(draft().replace("**Time:** Not specified.\n", ""), encoding="utf-8")
        before = self.snapshot()
        with self.assertRaisesRegex(bob.ValidationError, "Time"):
            bob.add_recipe(self.data, path)
        self.assertEqual(before, self.snapshot())

    def test_interrupted_index_write_can_be_rebuilt(self):
        path = self.base / "recipe.md"
        path.write_text(draft(), encoding="utf-8")
        original_write = bob.atomic_text

        def fail_index(destination, content):
            if destination.name == "recipe-index.json":
                raise OSError("Simulated interrupted index update")
            original_write(destination, content)

        with mock.patch.object(bob, "atomic_text", side_effect=fail_index):
            with self.assertRaises(OSError):
                bob.add_recipe(self.data, path)
        with self.assertRaisesRegex(bob.ValidationError, "rebuild-index"):
            bob.load_data(self.data)
        bob.load_data(self.data, rebuild_index=True)
        self.assertEqual(bob.read_json(self.data / "recipe-index.json")["recipes"], [{"id": "test-soup", "title": "Test soup"}])

    def test_two_weeks_rerun_and_servings_revision(self):
        self.set_profile(fixture("preferences-example.json"))
        week_one = fixture("week-one.json")
        self.assertEqual(self.save("one.json", week_one), (1, True))
        first_state = (self.data / "state.json").read_bytes()
        self.assertEqual(self.save("one.json", week_one), (1, False))
        self.assertEqual(first_state, (self.data / "state.json").read_bytes())
        self.set_profile(fixture("preferences-week-two.json"))
        week_two = fixture("week-two.json")
        self.assertEqual(self.save("two.json", week_two), (1, True))
        revised = copy.deepcopy(week_two)
        revised["notes"].append("Wednesday changed from 3 to 4 servings; slots stay the same.")
        revised["meals"][1]["servings"] = 4
        for ingredient in revised["meals"][1]["ingredients"]:
            ingredient["quantity"] = ingredient["quantity"] * 4 / 3
        changed_profile = fixture("preferences-week-two.json")
        changed_profile["temporary_overrides"].append({"date": "2026-01-14", "slot": "dinner", "servings": 4})
        self.set_profile(changed_profile)
        self.assertEqual(self.save("two.json", revised), (2, True))
        self.assertEqual(self.save("two.json", revised), (2, False))
        profile, state, _, _ = bob.load_data(self.data)
        self.assertEqual(len(state["weeks"]), 2)
        self.assertEqual(sum(len(entry["plan"]["meals"]) for entry in state["weeks"].values()), 6)
        self.assertEqual(profile["household"]["servings"], 3)
        self.assertEqual(state["weeks"]["2026-01-12"]["plan"]["meals"][1]["servings"], 4)
        self.assertEqual(state["weeks"]["2026-01-12"]["plan"]["meals"][2]["servings"], 4)

    def test_multiple_slots_follow_breakfast_lunch_dinner_order(self):
        self.set_profile(fixture("preferences-example.json"))
        plan = fixture("week-one.json")
        for meal, slot in zip(plan["meals"], ("breakfast", "lunch", "dinner")):
            meal["date"] = "2026-01-05"
            meal["slot"] = slot
        plan["meals"].reverse()
        self.save("one.json", plan)
        stored = bob.read_json(self.data / "state.json")["weeks"]["2026-01-05"]["plan"]
        self.assertEqual([meal["slot"] for meal in stored["meals"]], ["breakfast", "lunch", "dinner"])

    def test_continuity_uses_saved_slots_across_weeks(self):
        profile = fixture("preferences-example.json")
        profile["carb_cycle"]["pattern"] = "RRNRN"
        self.set_profile(profile)
        self.save("one.json", fixture("week-one.json"))
        second = fixture("week-two.json")
        for meal, carb in zip(second["meals"], "RNR"):
            meal["carb"] = carb
        self.assertEqual(self.save("two.json", second), (1, True))
        before = (self.data / "state.json").read_bytes()
        self.assertEqual(self.save("one.json", fixture("week-one.json")), (1, False))
        self.assertEqual(before, (self.data / "state.json").read_bytes())

    def test_prior_slot_removal_rejects_inconsistent_later_week(self):
        self.set_profile(fixture("preferences-example.json"))
        first, second = fixture("week-one.json"), fixture("week-two.json")
        self.save("one.json", first)
        self.save("two.json", second)
        before = (self.data / "state.json").read_bytes()
        first["meals"].pop()
        with self.assertRaisesRegex(bob.ValidationError, "later weeks"):
            self.save("one.json", first)
        self.assertEqual(before, (self.data / "state.json").read_bytes())

    def test_new_preferences_preserve_historical_labels(self):
        profile = fixture("preferences-example.json")
        self.set_profile(profile)
        self.save("one.json", fixture("week-one.json"))
        history = bob.read_json(self.data / "state.json")["weeks"]["2026-01-05"]
        profile["carb_cycle"]["pattern"] = "N"
        self.set_profile(profile)
        bob.load_data(self.data)
        second = fixture("week-two.json")
        for meal in second["meals"]:
            meal["carb"] = "N"
        self.save("two.json", second)
        self.assertEqual(history, bob.read_json(self.data / "state.json")["weeks"]["2026-01-05"])

    def test_skipped_slots_do_not_advance_and_weekly_reset(self):
        profile = fixture("preferences-example.json")
        profile["temporary_overrides"] = [{"date": "2026-01-09", "slot": "dinner", "skip": True}]
        self.set_profile(profile)
        first = fixture("week-one.json")
        with self.assertRaisesRegex(bob.ValidationError, "skipped"):
            self.save("one.json", first)
        first["meals"].pop()
        self.save("one.json", first)
        second = fixture("week-two.json")
        for meal, carb in zip(second["meals"], "NRR"):
            meal["carb"] = carb
        self.save("two.json", second)
        profile["carb_cycle"]["continue_across_weeks"] = False
        self.set_profile(profile)
        for meal, carb in zip(second["meals"], "RRN"):
            meal["carb"] = carb
        self.assertEqual(self.save("two.json", second), (2, True))

    def test_bad_plan_rejected_before_state_write(self):
        original = fixture("week-one.json")
        variants = []
        duplicate = copy.deepcopy(original)
        duplicate["meals"].append(copy.deepcopy(duplicate["meals"][0]))
        variants.append(duplicate)
        bad_date = copy.deepcopy(original)
        bad_date["meals"][0]["date"] = "2026-01-12"
        variants.append(bad_date)
        bad_quantity = copy.deepcopy(original)
        bad_quantity["meals"][0]["ingredients"][0]["quantity"] = -1
        variants.append(bad_quantity)
        unknown = copy.deepcopy(original)
        unknown["meals"][0]["recipe_id"] = "does-not-exist"
        variants.append(unknown)
        before = self.snapshot()
        for plan in variants:
            with self.assertRaises(bob.ValidationError):
                self.save("bad.json", plan)
            self.assertEqual(before, self.snapshot())

    def test_json_duplicate_keys_and_nonfinite_numbers_rejected(self):
        for text in ('{"x":1,"x":2}', '{"x":NaN}', '{"x":Infinity}'):
            path = self.base / "bad.json"
            path.write_text(text)
            with self.assertRaises(bob.ValidationError):
                bob.read_json(path)


class ExampleArithmeticTests(unittest.TestCase):
    def test_six_recipes_scaled_and_groceries_reconciled(self):
        source = (ROOT / "recipes" / "STARTER_RECIPES.md").read_text(encoding="utf-8")
        base_recipes = {}
        for chunk in source.split('<a id="')[1:]:
            recipe_id = chunk.split('"', 1)[0]
            table = chunk.split("### Ingredients", 1)[1].split("### Method", 1)[0]
            base_recipes[recipe_id] = {
                (name.strip(), unit.strip()): Decimal(quantity)
                for name, quantity, unit in re.findall(r"^\| ([^|]+) \| ([0-9.]+) \| ([^|]+) \|$", table, re.MULTILINE)
            }
        seen_ids = set()
        for word in ("one", "two"):
            plan = fixture(f"week-{word}.json")
            totals = {}
            for meal in plan["meals"]:
                seen_ids.add(meal["recipe_id"])
                base = base_recipes[meal["recipe_id"]]
                actual = {(item["name"], item["unit"]): Decimal(str(item["quantity"])) for item in meal["ingredients"]}
                self.assertEqual(set(actual), set(base))
                for key, quantity in actual.items():
                    self.assertEqual(quantity, base[key] * Decimal(str(meal["servings"])) / 2)
                    totals[key] = totals.get(key, Decimal(0)) + quantity
            groceries = fixture(f"groceries-week-{word}.json")
            provided = {(item["name"], item["unit"]): Decimal(str(item["quantity"])) for item in groceries}
            self.assertEqual(provided, totals)
        self.assertEqual(seen_ids, set(base_recipes))
        self.assertEqual(len(seen_ids), 6)


if __name__ == "__main__":
    unittest.main()
