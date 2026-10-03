# Verification

Run the checks from the repository folder with Python 3.9 or newer:

```sh
python3 -m unittest discover -s tests -v
python3 scripts/check_release.py
```

The [GitHub Actions workflow](../.github/workflows/check.yml) runs these checks on Python 3.9 and 3.12 for pushes and pull requests. See the [latest runs](https://github.com/williswee/chef-bob/actions/workflows/check.yml) for the result of a particular commit.

## What the checks cover

The helper tests use synthetic fixtures in temporary directories. They cover:

- Private data paths, symlink protection, and preservation of existing files.
- Recipe imports, duplicate detection, source retention, and index recovery.
- Meal revisions, serving quantities, grocery totals, and cycle continuity.
- Invalid profile values, skipped meals, and conflicting future plans.

The package checker validates recipe IDs and required fields, local documentation links, the four-command menu, and public-file boundaries. A separate secret scanner checks the working tree and reachable Git history before publication. Automated checks do not establish recipe ownership or dietary suitability.

## Host compatibility

OpenClaw 2026.9.7 discovered the skill in an isolated workspace and reported it as eligible. This verifies discovery, not live messaging or delivery. The Hermes adapter follows its documented skill setup but has not been tested in a live host.

Each host still needs checks for private storage, links, photos, question controls, and notification delivery. Do not claim a capability works based on the product name or a successful file read alone.

The starter recipes have not been kitchen-tested. Imported recipes retain unresolved source details in their review notes.
