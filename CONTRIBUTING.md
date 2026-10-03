# Contributing to Chef Bob

Open an issue for a bug or a proposed improvement. For an ordinary change, create a branch and submit a pull request describing the problem, the change, and how you checked it. Small documentation corrections can go straight to a pull request.

## Recipes

Personal additions made through `/recipe-add` stay private. To share a recipe, submit a separate pull request containing only the recipe and its index entry.

Use the entry format in [RECIPES.md](RECIPES.md). Include the source, stated servings, measured ingredients, ordered steps, times, and any unresolved details. Keep stable IDs unchanged when editing an existing recipe. Do not turn an imported draft into a reviewed recipe without checking its quantities and method.

Submit text and assets you own or have permission to distribute. Preserve attribution and describe any license requirements. A link to a page is not permission to copy its photos or all of its text. Use fictional examples; omit household names, account IDs, conversations, and private document links.

## Local checks

Python 3.9 or newer is sufficient. No packages are required.

```sh
python3 -m unittest discover -s tests -v
python3 scripts/check_release.py
```

Keep the public menu to four commands. Check any behavior change against [SKILL.md](SKILL.md), [COMMANDS.md](COMMANDS.md), and the relevant platform guide. Report which AI tool and version you used when claiming integration support.

Use a separate temporary data directory for tests. Never point test runs at an actual household's data or messaging channels. A normal update must preserve preferences, recipe additions, and meal history.

## Automatic checks

The [GitHub Actions template](scripts/github-actions-check.yml) runs the local checks on Python 3.9 and 3.12 with read-only repository permissions. It is provided as a template and is not active in v0.1. To enable it, a maintainer can copy it to `.github/workflows/check.yml` and commit it using a GitHub credential permitted to write workflows. Confirm the first run passes before relying on it.

## Community

Keep feedback specific and respectful. Explain disagreements about recipes or design without making them personal. Do not post someone's personal information or private conversations. The maintainer may remove abusive or privacy-invasive contributions. Support is best effort; there is no guaranteed response time.

By contributing original work, you agree to distribute it under the project's MIT license. Identify third-party material and its permissions in the pull request.
