# Chef Bob

Turn your recipes into a meal plan and shopping list with the AI assistant you already use.

Plan dinners, swap a protein, or save a recipe from text, a link or a photo. Chef Bob uses your household size, food preferences and meal schedule. Your AI handles the files.

This is an open-source skill with a small local helper. You bring the AI tool and model. There is no Chef Bob account or hosted backend.

## Try the demo first

Once the latest Chef Bob is loaded, send `/demo`. In OpenClaw, use `/skill chef-bob /demo`. If your app intercepts slash commands, type `Chef Bob: /demo`.

For a new chat, copy this message:

```text
Try Chef Bob from https://github.com/williswee/chef-bob.
Read SKILL.md, COMMANDS.md and docs/demo.md, then run /demo.
Guide me through a small meal plan and let me change it.
Keep this a trial in this chat. Do not save a personal profile or plan,
add recipes to my real collection, or enable reminders.
If you cannot read the repository, tell me which files to attach.
```

The demo lets you try planning, preference changes and recipe additions before setup. Tell Bob what matters in normal language. Type "help" for the menu, "start over" for a fresh trial, or "use this for real" when ready. Chef Bob keeps the trial in the conversation; your AI provider's usual chat-history settings still apply.

If the link cannot be opened, download the repository ZIP and attach `SKILL.md`, `COMMANDS.md`, `docs/demo.md` and `recipes/STARTER_RECIPES.md`. No local installation is needed for the chat preview.

## Set up when you are ready

Copy this into your AI assistant:

```text
Help me set up Chef Bob from https://github.com/williswee/chef-bob.
Read START_HERE.md and follow it. Guide me one step at a time, ask only
what you need for my first meal plan, and show me a preview.
Keep my preferences and recipes private, and leave notifications off.
If you cannot read the repository or save files, explain the attachment
or manual option instead of saying setup is complete.
```

Can't open the link? Select **Code → Download ZIP**, then attach the extracted `START_HERE.md`, `SKILL.md` and `recipes/STARTER_RECIPES.md`. Add `RECIPES.md` for the larger collection. Without attachments, paste the instructions and selected recipes. [Manual setup](adapters/generic-chat.md)

## Four things to remember

| Command | What it does | Example |
| --- | --- | --- |
| `/demo` | Tries a plan and changes in this chat before setup. | `/demo` |
| `/plan` | Creates or revises a meal plan with a shopping list and preparation notes. | `/plan Three dinners next week. Use the broccoli first.` |
| `/preferences` | Shows or changes your household, food, planning and notification settings. | `/preferences Cook for 3 people, replace pork with chicken, and keep reminders off.` |
| `/recipe-add` | Saves a recipe draft to your personal collection for review. | `/recipe-add Save the recipe below and flag any missing quantities.` |

For a link, send `/recipe-add Save this recipe: <recipe URL>`. For a photo, attach it with `/recipe-add Save this photo as a recipe draft and flag anything unreadable.` These need browsing or image support. Ask for a preview if you want to see it without saving.

Type "help" for the menu. Browse in ordinary language: "Show me quick tofu recipes" or "What soups do I have?" `/demo` replaces the earlier help command so the menu still has four commands. While the demo is active, the other commands make trial changes too.

Some tools reserve slash commands. If that happens, prefix your message with `Chef Bob:`, for example `Chef Bob: /demo`. A configured Telegram menu alias uses `/recipe_add` for `/recipe-add`. These reach the same four actions. See your adapter below.

## Make it yours

Change preferences in chat, without editing configuration files:

```text
/preferences Plan weekday dinners for 2 adults. No shellfish.
Use RRNRRN: R means rice, N means noodles or pasta. Continue the cycle
across weeks. I prefer chicken and tofu. Keep active cooking under
30 minutes and notifications off.
```

The cycle is optional. Change its pattern and eligible days in chat. Skipped meals do not advance it in v0.1. Specify when a preference change applies to just one day or week.

Reminders start off. Use `/preferences` to request a timezone, schedule and destination. Your AI tool must support and verify scheduling and delivery before Bob calls them active.

## Recipes included

- [Six original starter recipes](recipes/STARTER_RECIPES.md) give you a small first-plan collection. They have not been kitchen-tested.
- [104 imported recipes](RECIPES.md) cover drinks, soups, vegetables, fish, eggs, meat and one-pot meals. They are untested drafts with source links and review notes for missing quantities, methods or temperature units.
- Your additions go into your private `recipes.md`. `/recipe-add` does not publish them or push them to GitHub.

Ask Bob to review a recipe's gaps before using it. Missing instructions should stay visible until resolved.

## Choose your AI tool

| Tool | v0.1 path |
| --- | --- |
| [OpenClaw](adapters/openclaw.md) | Recommended setup. Skill discovery checked on 2026.9.7; live chat and delivery not tested. |
| [Hermes Agent](adapters/hermes.md) | Experimental adapter based on its documented skill system. |
| [Other chats and bots](adapters/generic-chat.md) | Paste or attach the instructions. Persistence, links, photos and scheduling depend on your tool. |

Dot, Instinct and Grok users can try the manual path if their product accepts instructions or attachments. Native integrations are not verified. Each adapter explains the checks to run on your own bot.

The local helper passed 16 tests, including saved-plan revisions, recipe imports and quantity checks across two example weeks. See [what was tested](docs/verification.md) and the remaining host checks.

For the demo, GPT-6.1 Sol with ultra reasoning judged ten versions across 50 generated replies. The selected version scored 9.00/10, tied with three alternatives. The [ranked comparison](docs/demo-evaluation/README.md) covers delightful UX, ease of use, context capturing, and clarity. These are AI judgments from a fixed scenario, not human usability results or live bot tests.

## Privacy, costs and updates

With file access, personal data lives outside the repository in `~/.chef-bob`, or a directory selected through `CHEF_BOB_DATA_DIR`. The optional Python 3.9+ helper has no third-party dependencies and makes no AI calls, messages or scheduled jobs.

Your chosen AI receives the prompts, preferences, recipes and images you share or let it read. Enabled notifications also pass through your messaging service. Local storage does not hide a cloud conversation from its provider. Keep credentials in your tool's settings.

Chef Bob has no subscription fee. Your AI subscription, model/API usage, hosting and optional services may cost money. Check your providers' prices.

To update, ask your AI to back up your personal directory and update only Chef Bob's source. Preserve saved preferences, recipes and reminder settings. [Update procedure](START_HERE.md#update-without-losing-personal-data)

## Contribute

Contribute recipe corrections, clearer instructions or reports from your bot setup. Include a recipe ID or tool/version and remove personal data before posting. [Contribution guide](CONTRIBUTING.md)

Report security problems through the [private reporting process](SECURITY.md).

Original code, documentation and starter recipes use the [MIT license](LICENSE). See [sources and attribution](NOTICE.md) for imported recipes and external materials.
