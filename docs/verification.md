# Verification

## Demo study

This study predates the current personality file, introduction, optional assistant nickname, and selectable onboarding questions. Those changes are unscored; the results below apply only to the original v06 instructions.

On 3 October 2026, GPT-6.1 Sol with ultra reasoning evaluated ten demo candidates. Each received the same four-turn conversation and one distinct adversarial follow-up, for 50 generated replies. The baseline scores were frozen before each follow-up. See the [ranked summary and methodology](demo-evaluation/README.md).

The selected guide is version 6, with an equally weighted score of 9.00/10. Versions 7, 9, and 10 tied on all four criteria and unnecessary-question count; the predefined earlier-round tie-break selected version 6. Each version received one different adversarial follow-up, so the selected version was not tested against all ten attacks.

This was a fixed-scenario AI conversation study with one sample per version. It did not test human usability, live bot delivery, or real storage and scheduling through the demo. The local helper checks below are separate. The historical guide at commit `69f7b7e` matches the selected candidate; the current guide has since changed.

## v0.1 local checks

Checked on 3 October 2026. These results describe the shipped files and local workflows; each AI host still needs its own setup check.

| Check | Result |
| --- | --- |
| Local helper tests | All 16 passed on Python 3.9.6 and 3.13. |
| Recipe and documentation checks | Unique recipe IDs, required sections, local links, public-package boundaries, and the four-command limit passed. |
| Skill format | The skill validator accepted `SKILL.md`. |
| OpenClaw discovery | OpenClaw 2026.9.7 loaded the skill from an isolated workspace as eligible, model-visible, user-invocable, and command-visible. |
| Two-week trial | An independent agent followed the instructions, saved six distinct dinners with `RRNRRN`, and reopened the private files successfully. |
| Revisions | Changing one dinner from two to three servings updated its ingredient quantities and shopping totals. Saving it again left the stored state unchanged. |
| Recipe additions | A supplied recipe retained its quantities and attribution. A duplicate was rejected without changing private files. |
| Reinitialization | Existing preferences, plans, and personal recipes survived unchanged. |

The trial used fictional preferences and temporary private storage. It left notifications disabled and made no messaging or scheduling calls. The public source files used during the trial stayed unchanged.

The tests compare all six starter recipes with the two [example weeks](../examples/example-plan.md), including scaled quantities and grocery totals. Other tests cover invalid data, symlink paths, interrupted index writes, skipped meals, and changes that conflict with later plans.

## Run the local checks

From the source folder, with Python 3.9 or later:

```sh
python3 -m unittest discover -s tests -v
python3 scripts/check_release.py
```

These checks ran locally for this release. GitHub Actions is not active because the publishing credential lacked workflow permission. A ready-to-use [workflow template](../scripts/github-actions-check.yml) and [activation steps](../CONTRIBUTING.md#automatic-checks) are included.

Before publication, the release files were also checked with Gitleaks 8.30.1 and a targeted personal-data review. No findings were detected. A passing scan is not a guarantee that every possible secret or identifying detail can be recognized.

## Still needs testing in a configured host

Live OpenClaw conversations, Hermes sessions, photo imports, external recipe-page imports, and scheduled channel delivery were not tested for this release. Dot, Instinct, and Grok have a manual instruction path; no native integration is claimed.

The helper does not assess dietary suitability or cooking safety. The six original starter recipes have not been kitchen-tested, and the 104 imported entries retain their review notes and source gaps.
