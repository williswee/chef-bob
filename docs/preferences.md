# Preferences and saved plans

Tell Chef Bob what to change in normal language. For example, `/preferences plan for four servings, avoid pork, and stop daily reminders`. The AI edits one private profile and validates it. You do not need to edit JSON yourself.

## Where your data lives

The default data directory is `~/.chef-bob`. Set `CHEF_BOB_DATA_DIR` to another directory outside the repository if needed. The Python helper resolves this location and rejects a data directory inside the project. Keep the directory private and backed up using your own chosen method.

| File | Contents |
| --- | --- |
| `preferences.json` | Current household settings and temporary meal exceptions |
| `state.json` | Saved plans keyed by Monday date |
| `recipes.md` | Recipes you add, including sources and review notes |
| `recipe-index.json` | Derived lookup of private recipe titles and stable IDs |

Initialization copies the public [preference template](../templates/preferences.json) and [empty state](../templates/state.json) only when needed. It must not reset existing data. The public files contain defaults, not a real household's profile.

After an authorized manual correction to a private recipe, run `python3 scripts/chef_bob.py check-data --rebuild-index` to validate the book and refresh its derived index. The same action can repair an index mismatch after an interrupted import. It does not replace the recipe book or reset plans.

## Profile fields

| Field | Meaning |
| --- | --- |
| `schema_version` | `1` for this format |
| `household.adults`, `household.children` | Household counts, stored separately from serving size |
| `household.servings` | Positive number of recipe servings to prepare by default |
| `timezone` | An IANA timezone such as `Europe/London`; the template uses `UTC` until you choose |
| `diet.allergies` | Allergens requiring ingredient and substitution checks; never inferred from dislikes |
| `diet.dislikes` | Taste preferences; ask before overriding one |
| `diet.excluded_ingredients` | Ingredients the user has explicitly ruled out for other reasons |
| `diet.preferred_proteins` | Proteins to favor when selecting dishes; preferences do not override exclusions |
| `meal_schedule` | List of weekday and meal-slot pairs, such as Monday dinner |
| `planning.max_active_minutes` | Desired maximum hands-on time per planned meal; flag longer total elapsed time separately |
| `planning.repeat_gap_weeks` | `1` avoids the immediately previous calendar week's dishes; `0` permits repeats |
| `carb_cycle` | Optional rice/noodle pattern, described below |
| `shopping.region` | Optional place or shopping context, such as a country; `null` means unspecified |
| `shopping.units` | `metric` or `imperial`; original recipe units must remain clear |
| `shopping.group_by` | `meal` or `category` for grocery grouping |
| `notifications` | Verified notification setup; defaults off and does not itself run a scheduler |
| `temporary_overrides` | Date-specific meal changes; do not replace the lasting profile |

The default meal schedule is Monday, Wednesday, and Friday dinner for two servings. The adult and child counts help explain the household; they do not calculate portions automatically. A person may need more or less than one recipe serving.

The helper's structural checks cannot detect every alias for an allergen, verify product labels, or establish nutritional suitability. Those remain part of recipe review and the user's decisions.

## Carb pattern

`R` means rice. `N` means noodles, pasta, or macaroni. It never means "no carbs". The optional pattern defaults to `RRNRRN`, with four rice meals and two noodle meals per six consumed positions.

| Setting | Default and behavior |
| --- | --- |
| `enabled` | `false`; no cycle is imposed until selected |
| `pattern` | `RRNRRN`; a nonempty sequence of `R` and `N` |
| `start_index` | `0`; the initial position in the sequence, not a mutable progress counter |
| `days` | Monday through Friday; meals on other days do not consume positions |
| `skip_behavior` | `do_not_advance`; omitted or skipped meals consume no position |
| `continue_across_weeks` | `true`; the next eligible saved meal uses the next position, including across Monday boundaries |

Only `do_not_advance` is supported in v0.1. Do not silently interpret a requested alternative. Setting `continue_across_weeks` to `false` restarts at `start_index` each Monday.

With three planned dinners a week and weekdays eligible, `RRNRRN` produces `R, R, N` in the first week and `R, R, N` in the next. Unscheduled Tuesday and Thursday meals do not advance it. If weekend meals are added to `days`, their planned meals consume positions too.

Saved meals are ordered by date, then breakfast, lunch, and dinner. Custom slot names follow those three, in alphabetical order. Use that order when assigning carb labels to several eligible meals on one day. Rerunning the same saved week does not advance the sequence. Changing a week can affect already saved later weeks; report conflicts and revise the affected plans explicitly.

Changing the pattern affects new planning. Earlier saved meals still count toward continuity, but their original carb labels remain historical facts. The helper checks the candidate week and any later saved plans against the current pattern, so a change may require revising future plans.

## Temporary exceptions

Each override identifies a date and meal slot. It may change `servings`, set `skip`, or add `excluded_ingredients` for that meal. It cannot remove a household allergy or exclusion.

```json
{
  "date": "2027-01-08",
  "slot": "dinner",
  "servings": 4,
  "excluded_ingredients": ["pork"]
}
```

Add that object to `temporary_overrides` for an extra-guest dinner without changing the normal serving count. A skipped meal uses `"skip": true` and is omitted from the plan. Keep expired exceptions out of future planning.

## Notifications

The default is `enabled: false`, `channel: null`, and an empty `schedules` list. Ask the AI for a destination and timing only if you want notifications and the host supports them.

A schedule record contains `name`, a `time` in `HH:MM` format, and lowercase weekday names in `days`. Store the host's schedule identifier as `host_schedule_id` when available. Schedule times use the profile's timezone.

Changing the JSON does not create or cancel a host schedule. Enable notifications only after the requested host setup succeeds. When turning them off, disable or remove the actual schedule and verify it. If host access is unavailable, report that the existing schedule remains active or unverified; do not say reminders are off just because the profile changed.

## Saved plan format

The helper accepts a `week_start` Monday date and a `meals` list. Each meal records its `date`, `slot`, `recipe_id`, `servings`, and `ingredients`. Each ingredient has a `name`, numeric `quantity`, and `unit`. Use `null` for an unknown quantity or unit; do not supply a guessed value. A `carb` label is required for eligible meals when the cycle is enabled. A top-level `notes` list is optional.

```json
{
  "week_start": "2027-01-04",
  "meals": [
    {
      "date": "2027-01-04",
      "slot": "dinner",
      "recipe_id": "starter-tomato-chickpea-rice",
      "servings": 2,
      "carb": "R",
      "ingredients": [
        { "name": "White rice, dry", "quantity": 150, "unit": "g" }
      ]
    }
  ],
  "notes": ["Schema illustration only. A real meal must include every ingredient."]
}
```

`state.json` starts with `{"schema_version": 1, "weeks": {}}`. The helper stores each entry under `weeks[week_start]` as `{ "revision": 1, "plan": ... }`. Saving identical content is idempotent. A changed plan replaces that week's content and increases its revision; it does not add a second week.

The helper checks the declared data. It cannot establish that an ingredient list is complete, that quantities match the source recipe, or that a proposed substitution works. The AI must compare the plan to its recipes before saving.
