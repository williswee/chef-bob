# Chef Bob with OpenClaw

This is the recommended v0.1 setup. The instructions follow OpenClaw's documented skill system.

For v0.1, OpenClaw 2026.9.7 discovered Chef Bob in a temporary, isolated configuration and reported the skill as eligible, model-visible and command-visible. The test did not start a gateway or run a model conversation. Recipe-link access, image reading and message delivery still need testing in your own setup.

## Give OpenClaw this message

```text
Set up Chef Bob from https://github.com/williswee/chef-bob for this
OpenClaw agent. Read START_HERE.md and SKILL.md first.
Find this agent's actual workspace and install the complete repository
as its skills/chef-bob folder, preserving any existing installation.
Do not replace my AGENTS.md, SOUL.md, USER.md, memory or other skills.
Keep personal data outside the source folder, defaulting to ~/.chef-bob.
Check that you can load Chef Bob and guide me to one small meal plan.
Keep notifications off and do not change my existing scheduled jobs.
```

OpenClaw discovers workspace skills under `<workspace>/skills`. Chef Bob's root `SKILL.md` and its supporting files therefore belong together at `<workspace>/skills/chef-bob/`. Identify the selected agent's real workspace; do not assume it is the terminal's current folder. [OpenClaw skill locations](https://docs.openclaw.ai/tools/skills)

If the assistant cannot fetch files, download the repository ZIP, extract the complete folder to that location, and have the assistant read it. If that location already exists, review the existing installation before updating it. Installing this package should not change OpenClaw's model, permissions or global personality.

## Invoke Chef Bob

OpenClaw has a built-in `/help`. Its documented generic skill entrypoint can route a request to Chef Bob explicitly:

```text
/skill chef-bob /help
/skill chef-bob /plan Three dinners next week.
/skill chef-bob /preferences Replace pork with chicken.
/skill chef-bob /recipe-add Save the recipe below for me.
```

These invoke the same four Chef Bob actions. Direct native skill aliases depend on channel configuration and may be renamed after collisions. If you cannot use the wrapper in your channel, send ordinary text such as `Chef Bob: /plan Three dinners next week.` and verify that the assistant loaded the skill. [OpenClaw slash-command behavior](https://docs.openclaw.ai/tools/slash-commands)

Telegram's registered command names allow lowercase letters, digits and underscores, so a menu alias for `/recipe-add` must use `/recipe_add`. Chef Bob does not register or replace your bot's command menu automatically. [Telegram BotCommand format](https://core.telegram.org/bots/api#botcommand)

## Confirm your setup

Have the assistant identify the loaded skill and source folder, show the four actions, and run the private-storage checks from `START_HERE.md`. Make a small plan and reopen it from the personal directory. Test a source link or image only if you want those features and the current tools support them.

If OpenClaw cannot see the new skill, check the workspace, discovery settings and any skill allowlist. Use the reload/session behavior documented for your installed version. Do not overwrite global configuration merely to make the skill appear.

Reminders remain off. If requested later, follow `START_HERE.md` and OpenClaw's current scheduling documentation to verify a schedule and destination before enabling it. The Chef Bob helper itself neither sends messages nor schedules work.

This guide does not claim a live Telegram or other channel-delivery test. Record the OpenClaw version and the checks you actually ran when reporting an integration issue.
