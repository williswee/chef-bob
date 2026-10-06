# Chef Bob

Plan meals, adjust portions, and make a shopping list with the AI assistant you already use.

Chef Bob is an open-source skill for your AI tool. It includes recipes and an optional local helper, with no account or backend.

## Get started

Copy this into your AI assistant:

```text
Help me set up Chef Bob from https://github.com/williswee/chef-bob.
Read START_HERE.md, SKILL.md, soul.md and COMMANDS.md.
Guide me through onboarding one question at a time, then show a first
meal plan before saving it. Offer clickable answers when this app
supports them, with optional free text.
Keep my data private and reminders off.
If you cannot read files or save private data, explain the manual option.
```

Bob offers to change his name, then asks about your cooking routine, portions, meals, food restrictions, and time limit.

If the link fails, download the repository ZIP and attach `START_HERE.md`, `SKILL.md`, `soul.md`, `COMMANDS.md`, and `recipes/STARTER_RECIPES.md`. Pasting their contents also works.

Clickable answers depend on the app. Otherwise, Bob offers numbered choices. Free text is always welcome.

## Four commands

| Command | What it does | Example |
| --- | --- | --- |
| `/help` | Shows the menu and next steps. | `/help` |
| `/plan` | Creates or revises meals, groceries, and preparation notes. | `/plan Three dinners next week. Use the broccoli first.` |
| `/preferences` | Shows or changes your settings. | `/preferences Cook for 2 and use tofu instead of pork.` |
| `/recipe-add` | Adds a recipe draft to your private collection. | `/recipe-add Save the recipe below and flag missing quantities.` |

Plain language works too: "Swap Tuesday's dinner." If the app reserves slash commands, use `Chef Bob: /plan`.

Add recipes through text, links, or photos your AI can read. Bob flags missing details and saves private drafts when file access is available. Ask for a preview to avoid saving. See [command details](COMMANDS.md).

## Make it yours

Set portions, preferred proteins, foods to avoid, cooking time, meal days, and notifications in chat. No configuration editing is required.

```text
/preferences Plan weekday dinners for 2 portions. Prefer chicken and tofu.
Use RRNRRN: R means rice, N means noodles or pasta. Keep reminders off.
```

The optional cycle continues across weeks. Skipped meals do not advance it. Say when a preference applies to one meal or week.

[soul.md](soul.md) makes Bob concise and lightly humorous. He checks facts, owns mistakes, and explains decisions. Ask for a different tone. Keep this file inside Chef Bob's folder, separate from your assistant's personality.

## Storage and supported tools

[The setup guide](START_HERE.md) keeps private data outside the source folder, in `~/.chef-bob` or `CHEF_BOB_DATA_DIR`. Without file access, save Bob's handoff record and bring it to your next chat.

| Tool | Setup and limits |
| --- | --- |
| [OpenClaw](adapters/openclaw.md) | Skill discovery checked on 2026.9.7. Live conversations and delivery remain unverified. |
| [Hermes Agent](adapters/hermes.md) | Experimental adapter. No live host test. |
| [Codex, Claude, and other chats](adapters/generic-chat.md) | Read or attach the instructions. Available capabilities depend on the host. |

Dot, Instinct, and Grok have a manual path where they accept instructions or attachments. See [verification notes](docs/verification.md) for integration limits.

Reminders start off. They require your chosen schedule and destination, plus verified host support. The helper does not send messages or create jobs.

## Recipes and privacy

The [six starter recipes](recipes/STARTER_RECIPES.md) are complete but not kitchen-tested. The [104 imported recipes](RECIPES.md) each use a **5-portion base**, with a [scaling guide](RECIPES.md#portions-and-scaling) for other amounts. They retain source links and review notes for missing details. Your additions stay in your private collection. The helper validates file structure and recipe references. The AI must check portion scaling, dietary suitability, and cooking instructions against the recipes.

Your AI provider receives what you share or allow it to read. Keep credentials outside recipes and this repository. Chef Bob has no subscription fee; your AI provider and optional services may charge for use.

## Contribute

The optional helper requires Python 3.9 or newer, with no third-party packages. Run checks from the repository folder:

```sh
python3 -m unittest discover -s tests -v
python3 scripts/check_release.py
```

See the [repository map](CONTRIBUTING.md#repository-map) for what each file does. Read [CONTRIBUTING.md](CONTRIBUTING.md) before submitting changes. [Report bugs](https://github.com/williswee/chef-bob/issues) with reproduction steps and your tool version. Omit personal data. Use [SECURITY.md](SECURITY.md) for private vulnerability reports.

## License

Original code, instructions, documentation, and starter recipes use the [MIT license](LICENSE). [NOTICE.md](NOTICE.md) covers attribution and third-party material.
