#!/usr/bin/env python3
"""Local storage and structural checks for Chef Bob. No network or AI calls."""
from __future__ import annotations

import argparse
import copy
import datetime as dt
import json
import math
import os
from pathlib import Path
import re
import sys
import tempfile
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

SOURCE_ROOT = Path(__file__).resolve().parent.parent
DAYS = ("monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday")
ID_PATTERN = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z")


class ValidationError(ValueError):
    """A user-editable file or path needs correction."""


def require(condition, message):
    if not condition:
        raise ValidationError(message)


def object_at(value, name):
    require(isinstance(value, dict), f"{name} must be an object")
    return value


def field(obj, key, name):
    require(key in obj, f"{name}.{key} is required")
    return obj[key]


def nonempty(value):
    return isinstance(value, str) and bool(value.strip())


def number(value, name, minimum=0, maximum=10000, integer=False, positive=False):
    require(type(value) in ((int,) if integer else (int, float)), f"{name} must be {'an integer' if integer else 'a number'}")
    require(math.isfinite(value) and minimum <= value <= maximum, f"{name} must be between {minimum} and {maximum}")
    if positive:
        require(value > 0, f"{name} must be greater than zero")


def boolean(value, name):
    require(type(value) is bool, f"{name} must be true or false")


def strings(value, name, allowed=None, nonempty_list=False):
    require(isinstance(value, list), f"{name} must be a list")
    require(all(nonempty(item) for item in value), f"{name} must contain nonempty strings")
    require(len(set(value)) == len(value), f"{name} has duplicate entries")
    if nonempty_list:
        require(bool(value), f"{name} must not be empty")
    if allowed is not None:
        require(all(item in allowed for item in value), f"{name} contains an unsupported value")


def date_value(value, name):
    require(isinstance(value, str) and re.fullmatch(r"\d{4}-\d{2}-\d{2}", value), f"{name} must be YYYY-MM-DD")
    try:
        return dt.date.fromisoformat(value)
    except ValueError as exc:
        raise ValidationError(f"{name} is not a valid date") from exc


def slot_value(value, name):
    require(isinstance(value, str) and re.fullmatch(r"[a-z][a-z0-9_-]*", value), f"{name} must be a lowercase slot name, such as dinner")


def meal_order(meal):
    """Use usual meal order, then custom slots alphabetically on the same date."""
    ranks = {"breakfast": 0, "lunch": 1, "dinner": 2}
    return meal["date"], ranks.get(meal["slot"], 3), meal["slot"]


def validate_profile(profile):
    p = object_at(profile, "profile")
    require(type(p.get("schema_version")) is int and p["schema_version"] == 1, "profile.schema_version must be 1")
    h = object_at(field(p, "household", "profile"), "household")
    for key in ("adults", "children"):
        number(field(h, key, "household"), f"household.{key}", maximum=1000, integer=True)
    require(h["adults"] + h["children"] > 0, "household needs at least one person")
    number(field(h, "servings", "household"), "household.servings", maximum=1000, positive=True)
    timezone = field(p, "timezone", "profile")
    require(nonempty(timezone), "timezone must be an IANA timezone, such as UTC")
    try:
        ZoneInfo(timezone)
    except (ZoneInfoNotFoundError, ValueError) as exc:
        raise ValidationError(f"Unknown timezone: {timezone}") from exc
    diet = object_at(field(p, "diet", "profile"), "diet")
    for key in ("allergies", "dislikes", "excluded_ingredients", "preferred_proteins"):
        strings(field(diet, key, "diet"), f"diet.{key}")
    schedule = field(p, "meal_schedule", "profile")
    require(isinstance(schedule, list) and bool(schedule), "meal_schedule must be a nonempty list")
    seen = set()
    for item in schedule:
        object_at(item, "meal_schedule entry")
        day, slot = item.get("day"), item.get("slot")
        require(day in DAYS, "meal_schedule day must be a lowercase weekday")
        slot_value(slot, "meal_schedule slot")
        require((day, slot) not in seen, "meal_schedule has a duplicate day and slot")
        seen.add((day, slot))
    planning = object_at(field(p, "planning", "profile"), "planning")
    number(field(planning, "max_active_minutes", "planning"), "planning.max_active_minutes", 1, 1440, integer=True)
    number(field(planning, "repeat_gap_weeks", "planning"), "planning.repeat_gap_weeks", 0, 104, integer=True)
    cycle = object_at(field(p, "carb_cycle", "profile"), "carb_cycle")
    boolean(field(cycle, "enabled", "carb_cycle"), "carb_cycle.enabled")
    pattern = field(cycle, "pattern", "carb_cycle")
    require(isinstance(pattern, str) and re.fullmatch(r"[RN]{1,366}", pattern), "carb_cycle.pattern must contain 1 to 366 R or N characters")
    number(field(cycle, "start_index", "carb_cycle"), "carb_cycle.start_index", 0, len(pattern) - 1, integer=True)
    strings(field(cycle, "days", "carb_cycle"), "carb_cycle.days", DAYS, nonempty_list=True)
    require(cycle.get("skip_behavior") == "do_not_advance", "carb_cycle.skip_behavior must be do_not_advance in this version")
    boolean(field(cycle, "continue_across_weeks", "carb_cycle"), "carb_cycle.continue_across_weeks")
    shopping = object_at(field(p, "shopping", "profile"), "shopping")
    require(shopping.get("region") is None or nonempty(shopping["region"]), "shopping.region must be a string or null")
    require(shopping.get("units") in ("metric", "imperial"), "shopping.units must be metric or imperial")
    require(shopping.get("group_by") in ("meal", "category"), "shopping.group_by must be meal or category")
    notifications = object_at(field(p, "notifications", "profile"), "notifications")
    boolean(field(notifications, "enabled", "notifications"), "notifications.enabled")
    channel = field(notifications, "channel", "notifications")
    require(channel is None or nonempty(channel), "notifications.channel must be a string or null")
    require(not notifications["enabled"] or nonempty(channel), "enabled notifications need a channel")
    schedules = field(notifications, "schedules", "notifications")
    require(isinstance(schedules, list) and all(isinstance(item, dict) for item in schedules), "notifications.schedules must be a list of objects")
    schedule_names = set()
    for schedule in schedules:
        require(nonempty(schedule.get("name")), "notification schedule needs a name")
        require(schedule["name"] not in schedule_names, "notification schedule names must be unique")
        schedule_names.add(schedule["name"])
        require(isinstance(schedule.get("time"), str) and re.fullmatch(r"(?:[01]\d|2[0-3]):[0-5]\d", schedule["time"]), "notification schedule time must be HH:MM in 24-hour time")
        strings(schedule.get("days"), "notification schedule days", DAYS, nonempty_list=True)
        if "host_schedule_id" in schedule:
            require(nonempty(schedule["host_schedule_id"]), "host_schedule_id must be a nonempty string")
    overrides = field(p, "temporary_overrides", "profile")
    require(isinstance(overrides, list), "temporary_overrides must be a list")
    seen = set()
    for override in overrides:
        object_at(override, "temporary override")
        date_value(override.get("date"), "override.date")
        slot_value(override.get("slot"), "override.slot")
        key = (override["date"], override["slot"])
        require(key not in seen, "temporary_overrides has a duplicate date and slot")
        seen.add(key)
        require(set(override) <= {"date", "slot", "skip", "servings", "excluded_ingredients"}, "temporary override has unsupported fields; allergies cannot be removed")
        if "skip" in override:
            boolean(override["skip"], "override.skip")
        if "servings" in override:
            number(override["servings"], "override.servings", maximum=1000, positive=True)
        if "excluded_ingredients" in override:
            strings(override["excluded_ingredients"], "override.excluded_ingredients")
    return p


def data_directory(value=None):
    raw = value or os.environ.get("CHEF_BOB_DATA_DIR") or "~/.chef-bob"
    target = Path(raw).expanduser().resolve()
    require(target != SOURCE_ROOT and SOURCE_ROOT not in target.parents, "Private data must be outside the Chef Bob source checkout, including symlink targets")
    require(not target.exists() or target.is_dir(), "Data directory is an existing file")
    return target


def data_file(directory, name):
    path = directory / name
    require(not path.is_symlink(), f"Private file must not be a symlink: {name}")
    require(not path.exists() or path.is_file(), f"Private path must be a regular file: {name}")
    return path


def read_json(path):
    def invalid_constant(value):
        raise ValidationError(f"Invalid JSON number: {value}")
    def unique_pairs(pairs):
        obj = {}
        for key, value in pairs:
            require(key not in obj, f"Duplicate JSON key: {key}")
            obj[key] = value
        return obj
    try:
        return json.loads(Path(path).read_text(encoding="utf-8"), parse_constant=invalid_constant, object_pairs_hook=unique_pairs)
    except json.JSONDecodeError as exc:
        raise ValidationError(f"Invalid JSON in {Path(path).name}: {exc.msg}") from exc


def atomic_text(path, content):
    require(not path.is_symlink(), f"Refusing symlink file: {path.name}")
    fd, temporary = tempfile.mkstemp(prefix=".chef-bob-", dir=str(path.parent))
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


def json_text(value):
    return json.dumps(value, indent=2, ensure_ascii=False, allow_nan=False) + "\n"


def recipes_from_text(text, allow_empty=False):
    # Match recipe metadata first, so a book's index headings are not recipes.
    ids = list(re.finditer(r"^\*\*ID:\*\*[^\n]*", text, re.MULTILINE))
    require(bool(ids) or allow_empty, "Recipe needs an ID field and a level-two or level-three title")
    headings = []
    for identifier in ids:
        preceding = list(re.finditer(r"^(#{2,3}) ([^\n]+)\s*$", text[:identifier.start()], re.MULTILINE))
        require(bool(preceding), "Recipe needs a level-two or level-three title")
        headings.append(preceding[-1])
    recipes = []
    for index, heading in enumerate(headings):
        end = headings[index + 1].start() if index + 1 < len(headings) else len(text)
        block = text[heading.start():end]
        title = heading.group(2).strip()
        section_level = len(heading.group(1)) + 1
        metadata = {}
        for name in ("ID", "Servings", "Time", "Review"):
            matches = re.findall(r"^\*\*" + name + r":\*\*[ \t]*([^\n]+)", block, re.MULTILINE)
            require(len(matches) == 1 and nonempty(matches[0]), f"Recipe {title} needs exactly one {name} field")
            metadata[name] = matches[0].strip()
        recipe_id = metadata["ID"].strip("`")
        require(bool(ID_PATTERN.fullmatch(recipe_id)), "Recipe ID must be a lowercase kebab-case identifier")
        for name in ("Ingredients", "Method", "Source"):
            matches = list(re.finditer(r"^" + "#" * section_level + " " + name + r"\s*$", block, re.MULTILINE))
            require(len(matches) == 1, f"Recipe {recipe_id} needs exactly one {name} section")
            rest = block[matches[0].end():]
            section = re.split(r"^#{1,4} |^<a id=", rest, maxsplit=1, flags=re.MULTILINE)[0].strip()
            require(nonempty(section), f"Recipe {recipe_id} has an empty {name} section; write Not specified. if unknown")
            if name == "Ingredients":
                require(bool(re.search(r"^(?:[-*] \S|\|[^\n]+\|)", section, re.MULTILINE)) or section.startswith("Not specified"), f"Recipe {recipe_id} ingredients must be a bullet list, table, or Not specified.")
            if name == "Method":
                require(bool(re.search(r"^\d+\. \S", section, re.MULTILINE)) or section.startswith("Not specified"), f"Recipe {recipe_id} method must be numbered or Not specified.")
        recipes.append({"id": recipe_id, "title": title})
    seen_ids, seen_titles = set(), set()
    for recipe in recipes:
        title = " ".join(recipe["title"].casefold().split())
        require(recipe["id"] not in seen_ids, f"Duplicate recipe ID: {recipe['id']}")
        require(title not in seen_titles, f"Duplicate recipe title: {recipe['title']}")
        seen_ids.add(recipe["id"])
        seen_titles.add(title)
    return recipes


def public_recipes():
    result = []
    for path in (SOURCE_ROOT / "RECIPES.md", SOURCE_ROOT / "recipes" / "STARTER_RECIPES.md"):
        result.extend(recipes_from_text(path.read_text(encoding="utf-8"), allow_empty=True))
    return result


def validate_plan(plan):
    p = object_at(plan, "plan")
    week = date_value(p.get("week_start"), "plan.week_start")
    require(week.weekday() == 0, "plan.week_start must be a Monday")
    meals = p.get("meals")
    require(isinstance(meals, list) and len(meals) <= 1000, "plan.meals must be a list with at most 1000 entries")
    seen = set()
    for meal in meals:
        object_at(meal, "meal")
        day = date_value(meal.get("date"), "meal.date")
        require(0 <= (day - week).days < 7, "Meal date must be within its plan week")
        slot_value(meal.get("slot"), "meal.slot")
        key = (meal["date"], meal["slot"])
        require(key not in seen, "Plan contains a duplicate date and slot")
        seen.add(key)
        require(isinstance(meal.get("recipe_id"), str) and bool(ID_PATTERN.fullmatch(meal["recipe_id"])), "meal.recipe_id must be a stable kebab-case recipe ID")
        number(meal.get("servings"), "meal.servings", maximum=1000, positive=True)
        require("carb" not in meal or meal["carb"] in ("R", "N"), "meal.carb must be R or N when supplied")
        ingredients = meal.get("ingredients")
        require(isinstance(ingredients, list) and bool(ingredients), "meal.ingredients must be a nonempty list")
        names = set()
        for ingredient in ingredients:
            object_at(ingredient, "ingredient")
            require(nonempty(ingredient.get("name")), "ingredient.name must be a nonempty string")
            key = ingredient["name"].strip().casefold()
            require(key not in names, "Meal has duplicate ingredient names; combine quantities first")
            names.add(key)
            quantity = field(ingredient, "quantity", "ingredient")
            if quantity is not None:
                number(quantity, "ingredient.quantity", maximum=1000000, positive=True)
            unit = field(ingredient, "unit", "ingredient")
            require(unit is None or nonempty(unit), "ingredient.unit must be a string or null")
    notes = p.get("notes", [])
    require(isinstance(notes, list) and all(isinstance(note, str) for note in notes), "plan.notes must be a list of strings")
    return p


def validate_state(state):
    s = object_at(state, "state")
    require(type(s.get("schema_version")) is int and s["schema_version"] == 1, "state.schema_version must be 1")
    weeks = object_at(s.get("weeks"), "state.weeks")
    for week, entry in weeks.items():
        object_at(entry, "week entry")
        number(entry.get("revision"), "week.revision", 1, 1000000, integer=True)
        plan = validate_plan(entry.get("plan"))
        require(plan["week_start"] == week, "State week key differs from plan.week_start")
    return s


def validate_weeks(profile, state, recipe_ids, check_from_week=None):
    cycle = profile["carb_cycle"]
    used = 0
    overrides = {(item["date"], item["slot"]): item for item in profile["temporary_overrides"]}
    for week in sorted(state["weeks"]):
        if not cycle["continue_across_weeks"]:
            used = 0
        meals = sorted(state["weeks"][week]["plan"]["meals"], key=meal_order)
        for meal in meals:
            require(meal["recipe_id"] in recipe_ids, f"Unknown recipe ID: {meal['recipe_id']}")
            check_labels = check_from_week is not None and week >= check_from_week
            if check_labels:
                override = overrides.get((meal["date"], meal["slot"]), {})
                require(not override.get("skip", False), f"Plan includes skipped slot {meal['date']} {meal['slot']}")
                if "servings" in override:
                    require(meal["servings"] == override["servings"], f"Plan servings do not match temporary override on {meal['date']}")
            day = DAYS[dt.date.fromisoformat(meal["date"]).weekday()]
            if cycle["enabled"] and day in cycle["days"]:
                expected = cycle["pattern"][(cycle["start_index"] + used) % len(cycle["pattern"])]
                if check_labels:
                    require(meal.get("carb") == expected, f"Carb cycle expects {expected} on {meal['date']} {meal['slot']}; review this and later weeks after changing history or preferences")
                used += 1
    return used


def load_data(directory, rebuild_index=False):
    require(directory.is_dir(), "Data directory does not exist; run init first")
    profile = validate_profile(read_json(data_file(directory, "preferences.json")))
    state = validate_state(read_json(data_file(directory, "state.json")))
    text = data_file(directory, "recipes.md").read_text(encoding="utf-8")
    recipes = recipes_from_text(text, allow_empty=True)
    index_path = data_file(directory, "recipe-index.json")
    expected_index = {"schema_version": 1, "recipes": recipes}
    if not rebuild_index:
        index = read_json(index_path)
        require(index == expected_index, "recipe-index.json does not match private recipes.md; run check-data --rebuild-index to regenerate this derived index")
    public = public_recipes()
    all_ids = [item["id"] for item in public + recipes]
    all_titles = [" ".join(item["title"].casefold().split()) for item in public + recipes]
    require(len(all_ids) == len(set(all_ids)), "Private recipe ID duplicates a public recipe")
    require(len(all_titles) == len(set(all_titles)), "Private recipe title duplicates a public recipe")
    validate_weeks(profile, state, set(all_ids))
    if rebuild_index:
        atomic_text(index_path, json_text(expected_index))
    return profile, state, text, recipes


def initialize(directory):
    directory.mkdir(parents=True, exist_ok=True, mode=0o700)
    prefs = data_file(directory, "preferences.json")
    state = data_file(directory, "state.json")
    book = data_file(directory, "recipes.md")
    index = data_file(directory, "recipe-index.json")
    profile = validate_profile(read_json(prefs if prefs.exists() else SOURCE_ROOT / "templates" / "preferences.json"))
    state_value = validate_state(read_json(state if state.exists() else SOURCE_ROOT / "templates" / "state.json"))
    recipe_text = book.read_text(encoding="utf-8") if book.exists() else "# Private recipes\n\nAdd drafts with the local add-recipe helper.\n"
    recipes = recipes_from_text(recipe_text, allow_empty=True)
    index_value = {"schema_version": 1, "recipes": recipes}
    if index.exists():
        require(read_json(index) == index_value, "Existing recipe index does not match the recipe book; init will not overwrite it")
    for path, text in ((prefs, json_text(profile)), (state, json_text(state_value)), (book, recipe_text), (index, json_text(index_value))):
        if not path.exists():
            atomic_text(path, text)
    load_data(directory)


def add_recipe(directory, file):
    _, _, existing_text, existing = load_data(directory)
    draft = Path(file).read_text(encoding="utf-8").strip()
    imported = recipes_from_text(draft)
    require(len(imported) == 1, "Import exactly one recipe draft at a time")
    recipe = imported[0]
    for current in public_recipes() + existing:
        require(recipe["id"] != current["id"], f"Duplicate recipe ID: {recipe['id']}; original files preserved")
        require(" ".join(recipe["title"].casefold().split()) != " ".join(current["title"].casefold().split()), f"Duplicate recipe title: {recipe['title']}; original files preserved")
    anchor = f'<a id="{recipe["id"]}"></a>'
    if anchor not in draft:
        draft = anchor + "\n\n" + draft
    new_text = existing_text.rstrip() + "\n\n" + draft + "\n"
    new_index = {"schema_version": 1, "recipes": recipes_from_text(new_text)}
    atomic_text(data_file(directory, "recipes.md"), new_text)
    atomic_text(data_file(directory, "recipe-index.json"), json_text(new_index))
    return recipe["id"]


def save_plan(directory, file):
    profile, state, _, recipes = load_data(directory)
    plan = validate_plan(read_json(file))
    # A different ordering of the same meals is the same plan.
    plan = copy.deepcopy(plan)
    plan["meals"].sort(key=meal_order)
    plan.setdefault("notes", [])
    current = state["weeks"].get(plan["week_start"])
    revision = current["revision"] + 1 if current else 1
    state["weeks"][plan["week_start"]] = {"revision": revision, "plan": plan}
    ids = {item["id"] for item in public_recipes() + recipes}
    validate_weeks(profile, state, ids, check_from_week=plan["week_start"])
    if current and current["plan"] == plan:
        return current["revision"], False
    atomic_text(data_file(directory, "state.json"), json_text(state))
    return revision, True


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    for name, help_text in (("init", "Create private files without replacing existing data"), ("check-profile", "Validate preference structure"), ("add-recipe", "Import one Markdown draft into private recipes"), ("save-plan", "Save or revise a week without double-advancing rotation"), ("check-data", "Validate private file structure and recipe references")):
        command = commands.add_parser(name, help=help_text)
        command.add_argument("--data-dir", help="Private folder outside this checkout; defaults to CHEF_BOB_DATA_DIR or ~/.chef-bob")
        if name in ("add-recipe", "save-plan"):
            command.add_argument("--file", required=True)
        elif name == "check-profile":
            command.add_argument("--file", help="Validate this profile instead of the private preference file")
        elif name == "check-data":
            command.add_argument("--rebuild-index", action="store_true", help="Regenerate recipe-index.json from validated private recipes; useful after an interrupted import")
    args = parser.parse_args(argv)
    try:
        directory = data_directory(args.data_dir)
        if args.command == "init":
            initialize(directory)
            print(f"Private data ready at {directory}. Existing files preserved.")
        elif args.command == "check-profile":
            validate_profile(read_json(args.file if args.file else data_file(directory, "preferences.json")))
            print("Profile structure is valid. Dietary suitability still needs review.")
        elif args.command == "add-recipe":
            print(f"Added private recipe: {add_recipe(directory, args.file)}")
        elif args.command == "save-plan":
            revision, changed = save_plan(directory, args.file)
            print(f"{'Saved' if changed else 'Unchanged'} week, revision {revision}. Dietary suitability and ingredient scaling still need review.")
        else:
            _, state, _, recipes = load_data(directory, rebuild_index=args.rebuild_index)
            print(f"Data structure is valid: {len(state['weeks'])} weeks, {len(recipes)} private recipes. Dietary suitability and ingredient scaling still need review.")
        return 0
    except (ValidationError, OSError, UnicodeError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
