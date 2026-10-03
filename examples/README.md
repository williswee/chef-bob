# Example plans

These examples exercise six original starter recipes, the optional `RRNRRN` rotation, and a change in portions. They do not contain household data. They verify arithmetic and storage behaviour, not nutrition, allergy suitability, or cooking results.

These files are developer examples and fixed inputs to [the automated tests](../tests/test_chef_bob.py). Chef Bob does not load them as your preferences or copy them into your plan during onboarding.

## Files in this folder

| File | Purpose |
| --- | --- |
| [README.md](README.md) | Explains the example data and shows both plans and their ingredient totals below. |
| [preferences-example.json](preferences-example.json) | Fictional week-one settings for two servings, with the optional rice/noodle cycle enabled. |
| [preferences-week-two.json](preferences-week-two.json) | Changes the default to three servings and Friday to four. |
| [week-one.json](week-one.json) | First week's three meals, with recipe IDs and ingredient quantities. |
| [week-two.json](week-two.json) | Second week's meals, showing the portion changes and continued cycle. |
| [groceries-week-one.json](groceries-week-one.json) | Expected ingredient totals for week one, checked against its meals. |
| [groceries-week-two.json](groceries-week-two.json) | Expected ingredient totals for week two after scaling portions. |

The helper initializes new private profiles from [templates/](../templates), which leave the cycle disabled. It does not use these example profiles as defaults.

## How the example works

Use `preferences-example.json` for week one. For week two, `preferences-week-two.json` changes the household to 3 servings and Friday to 4. Each starter recipe has a base of 2 servings, so the example multiplies every listed quantity by `desired servings / 2`. Cooking time does not scale with portions.

The example shopping totals preserve recipe ingredient names and units. They represent recipe-use quantities before package rounding. Water is included for arithmetic checking, and does not normally need to be purchased. Some foods are measured cooked and drained.

## Week 1: 2026-01-05

| Date | Meal | Servings | Carb |
| --- | --- | ---: | --- |
| 2026-01-05 | [Tomato chickpea rice](../recipes/STARTER_RECIPES.md#starter-tomato-chickpea-rice) | 2 | R |
| 2026-01-07 | [Lemon white bean rice](../recipes/STARTER_RECIPES.md#starter-lemon-white-bean-rice) | 2 | R |
| 2026-01-09 | [Ginger tofu noodles](../recipes/STARTER_RECIPES.md#starter-ginger-tofu-noodles) | 2 | N |

### Ingredient totals

| Ingredient | Quantity | Unit |
| --- | ---: | --- |
| Broccoli, small florets | 200 | g |
| Carrot, thinly sliced | 100 | g |
| Chickpeas, cooked and drained | 240 | g |
| Chopped canned tomatoes | 400 | g |
| Firm tofu, drained and cubed | 250 | g |
| Garlic, minced | 18 | g |
| Ginger, grated | 10 | g |
| Ground black pepper | 1 | g |
| Lemon juice | 20 | ml |
| Neutral cooking oil | 15 | ml |
| Olive oil | 30 | ml |
| Onion, diced | 100 | g |
| Salt | 4 | g |
| Soy sauce | 30 | ml |
| Spinach, washed | 120 | g |
| Water | 500 | ml |
| Water for boiling noodles | 2000 | ml |
| Water for sauce | 60 | ml |
| Wheat noodles, dry | 180 | g |
| White beans, cooked and drained | 240 | g |
| White rice, dry | 300 | g |

## Week 2: 2026-01-12

| Date | Meal | Servings | Carb |
| --- | --- | ---: | --- |
| 2026-01-12 | [Lentil carrot rice](../recipes/STARTER_RECIPES.md#starter-lentil-carrot-rice) | 3 | R |
| 2026-01-14 | [Egg and pea fried rice](../recipes/STARTER_RECIPES.md#starter-egg-pea-fried-rice) | 3 | R |
| 2026-01-16 | [Tomato lentil pasta](../recipes/STARTER_RECIPES.md#starter-tomato-lentil-pasta) | 4 | N |

### Ingredient totals

| Ingredient | Quantity | Unit |
| --- | ---: | --- |
| Carrot, finely diced | 375 | g |
| Chopped canned tomatoes | 800 | g |
| Dried oregano | 4 | g |
| Eggs | 3 | count |
| Frozen peas | 180 | g |
| Garlic, minced | 12 | g |
| Ground cumin | 3 | g |
| Lentils, cooked and drained | 840 | g |
| Neutral cooking oil | 22.5 | ml |
| Olive oil | 52.5 | ml |
| Onion, diced | 440 | g |
| Salt | 7 | g |
| Soy sauce | 22.5 | ml |
| Tomato passata | 300 | g |
| Water | 450 | ml |
| Water for boiling pasta | 4000 | ml |
| Water for rice | 450 | ml |
| Water for sauce | 150 | ml |
| Wheat pasta, dry | 360 | g |
| White rice, dry | 450 | g |

## What the helper checks

Saving the same JSON twice keeps the same revision. Replacing a week changes that week once. The rotation counts unique saved meal slots in chronological order, so repeating a save does not consume more positions. A change to an earlier week that would make later saved carb labels inconsistent is rejected. Earlier historical labels remain facts when preferences change.

The helper checks file structure and references. It does not generate meals, check allergies, verify that ingredient quantities match recipe servings, or send reminders. The test suite independently checks these example quantities and grocery totals against the starter tables.
