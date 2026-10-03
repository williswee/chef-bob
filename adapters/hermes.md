# Chef Bob with Hermes Agent

This adapter is experimental. Its setup follows Hermes documentation; v0.1 has not been tested in a live Hermes bot session.

## Give Hermes this message

```text
Set up Chef Bob from https://github.com/williswee/chef-bob in my current
Hermes profile. Read START_HERE.md and SKILL.md first.
Locate this profile's skills directory and put the complete Chef Bob
repository in its chef-bob folder. Preserve an existing installation.
Keep my personality, memory, other skills and credentials unchanged.
Use ~/.chef-bob for personal data unless CHEF_BOB_DATA_DIR is set,
and confirm that the data directory is outside the skill source.
Load the skill, guide me to one small meal plan and keep reminders off.
```

Hermes stores local skills under the active profile's skills directory, normally `~/.hermes/skills/`. Keep the entire Chef Bob folder there, with `SKILL.md` at `chef-bob/SKILL.md`. Profile overrides may change the base directory. [Hermes skill documentation](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills/)

If the assistant cannot download files, extract the repository ZIP into that folder. Do not copy only `SKILL.md`; the recipe collection, templates and helper are part of the package. Ask Hermes to verify discovery before continuing. Do not bypass an installation warning or replace an existing folder without reviewing it.

## Invoke Chef Bob

Hermes documents installed skills as chat commands using their skill name. Where this is available, pass the Chef Bob action as input:

```text
/chef-bob /help
/chef-bob /plan Three dinners next week.
/chef-bob /preferences Cook for 2 and avoid pork.
/chef-bob /recipe-add Save the recipe below for me.
```

The wrapper reaches the same four Chef Bob actions. A host command such as `/help` may belong to Hermes, and messaging platforms can impose different command-name rules. If needed, send `Chef Bob: /help` as ordinary text and verify that Hermes loaded the skill. [Hermes skill invocation](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills/)

Telegram command menus cannot contain a hyphen. Use `/recipe_add` only as a configured alias for the logical `/recipe-add` action; do not assume a menu or alias was installed. The plain-text prefix also avoids a conflict with platform help. [Telegram command names](https://core.telegram.org/bots/api#botcommand)

## Confirm your setup

Check skill discovery, private storage, a saved preference and a small accepted plan. Reopen the private files to confirm persistence. Test link fetching and photo reading separately if you want to use them. Report unavailable tools instead of marking the whole setup successful.

Hermes schedules tasks through its gateway. A working chat alone does not establish that scheduled delivery is available. Keep notifications off until the user requests them and the assistant verifies the gateway, timezone, destination and job details. [Hermes scheduled tasks](https://hermes-agent.nousresearch.com/docs/user-guide/features/cron/)

When scheduling is enabled, attach the Chef Bob skill or otherwise provide its complete instructions to the scheduled session, and make its personal data directory explicit. Store the returned job identifier privately. Updating the skill must not create duplicate jobs or reset notification preferences.
