# Contributing to Chef Bob

Open an issue for a bug or a proposed improvement. For an ordinary change, create a branch and submit a pull request describing the problem, the change, and how you checked it. Small documentation corrections can go straight to a pull request.

## Repository map

Start with `README.md` to use Chef Bob. The files below support setup, private storage, recipe planning, or project maintenance. Household data and trial transcripts belong outside the checkout.

### Root files

| File | Purpose |
| --- | --- |
| [README.md](README.md) | Public introduction, setup prompt, and command menu. |
| [START_HERE.md](START_HERE.md) | Step-by-step setup, private storage, first plan, and updates. |
| [SKILL.md](SKILL.md) | Instructions the AI follows for onboarding and everyday use. |
| [COMMANDS.md](COMMANDS.md) | Behavior of the four public commands. |
| [soul.md](soul.md) | Bob's tone, accuracy, and response to mistakes or disagreement. |
| [AGENTS.md](AGENTS.md) | Rules for AI agents working in this repository. |
| [RECIPES.md](RECIPES.md) | The 104 imported recipe entries, their index, sources, and review notes. |
| [CONTRIBUTING.md](CONTRIBUTING.md) | This file map and the process for contributing and checking changes. |
| [CHANGELOG.md](CHANGELOG.md) | Changes grouped by release. |
| [LICENSE](LICENSE) | MIT license for the project's original work. |
| [NOTICE.md](NOTICE.md) | Recipe provenance and third-party attribution limits. |
| [SECURITY.md](SECURITY.md) | Private vulnerability reporting and data boundaries. |
| [.gitignore](.gitignore) | Excludes household data, credentials, trial output, and generated files from Git. |

### Supporting folders

| File or folder | Purpose |
| --- | --- |
| [adapters/generic-chat.md](adapters/generic-chat.md) | Attachment-based setup and a manual record for chats without private file storage. |
| [adapters/openclaw.md](adapters/openclaw.md) | OpenClaw installation, invocation, and capability checks. |
| [adapters/hermes.md](adapters/hermes.md) | Experimental Hermes installation and invocation instructions. |
| [docs/preferences.md](docs/preferences.md) | Private profile fields, saved-plan format, and cycle rules. |
| [docs/verification.md](docs/verification.md) | What the checks cover and which host capabilities remain unverified. |
| [docs/demo.md](docs/demo.md) | Explicitly invoked maintainer UX test with no saved data or reminders. |
| [recipes/README.md](recipes/README.md) | Explains the two public recipe collections and where private additions go. |
| [recipes/STARTER_RECIPES.md](recipes/STARTER_RECIPES.md) | Six illustrative recipes for a first plan and arithmetic checks. |
| [examples/](examples/README.md) | A readable two-week plan and six JSON files used by tests. Its README explains every file. |
| [templates/preferences.json](templates/preferences.json) | Default settings copied only when a private profile does not exist. |
| [templates/state.json](templates/state.json) | Empty history copied only when a private state file does not exist. |
| [scripts/chef_bob.py](scripts/chef_bob.py) | Local storage, recipe imports, data validation, and plan revisions. |
| [scripts/check_release.py](scripts/check_release.py) | Public-package, documentation-link, recipe-metadata, and command-menu checks. |
| [tests/test_chef_bob.py](tests/test_chef_bob.py) | Regression tests for storage, imports, plan history, and example arithmetic. |
| [tests/test_release.py](tests/test_release.py) | Checks that the package rejects accidentally copied trial records. |
| [.github/workflows/check.yml](.github/workflows/check.yml) | Runs tests and package checks on pushes and pull requests. |
| [.github/ISSUE_TEMPLATE/bug.yml](.github/ISSUE_TEMPLATE/bug.yml) | Collects reproducible bug reports without private household data. |
| [.github/ISSUE_TEMPLATE/config.yml](.github/ISSUE_TEMPLATE/config.yml) | Adds a private security-reporting link to the issue chooser. |
| [.github/pull_request_template.md](.github/pull_request_template.md) | Prompts contributors to explain changes, checks, privacy, and recipe permissions. |

When adding a file, identify who uses it and update this map or the examples index. Keep generated output, personal profiles, and trial reports outside the repository.

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

The [GitHub Actions workflow](.github/workflows/check.yml) runs the local checks on Python 3.9 and 3.12 for pushes and pull requests, with read-only repository permissions. Check the [latest runs](https://github.com/williswee/chef-bob/actions/workflows/check.yml) before merging.

## Maintainer UX checks

For an isolated onboarding test, follow [the maintainer guide](docs/demo.md). Test controls are not part of the public help menu. Use fictional data and keep transcripts, generated household files, and evaluation reports outside the checkout. Do not commit them.

## Community

Keep feedback specific and respectful. Explain disagreements about recipes or design without making them personal. Do not post someone's personal information or private conversations. The maintainer may remove abusive or privacy-invasive contributions. Support is best effort; there is no guaranteed response time.

By contributing original work, you agree to distribute it under the project's MIT license. Identify third-party material and its permissions in the pull request.
