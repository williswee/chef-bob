# Chef Bob in another chat or bot

Use this path when your assistant can read instructions but has no verified Chef Bob adapter. It also applies to Dot, Instinct and Grok where the particular product accepts pasted text or attachments. This guide does not claim native integration, file persistence or scheduled notifications for those products.

## Start in chat

Download the repository ZIP and attach `START_HERE.md`, `SKILL.md` and `recipes/STARTER_RECIPES.md`. Attach `RECIPES.md` if you want to use the larger imported collection. If file upload is unavailable, paste the instructions and the recipes you want to use.

Then send:

```text
Use the supplied Chef Bob instructions for meal planning in this chat.
Tell me whether you can save private files, read recipe links, read
photos and schedule notifications. Do not assume those features exist.
Guide me one step at a time to a first plan. Keep reminders off.
If you cannot save files, give me a personal record I can save and
bring back next time. Do not claim you will remember it automatically.
```

If the assistant has confirmed local file access, it can follow the normal private-storage steps in `START_HERE.md`. Otherwise, use manual mode below.

## Use the same four actions

```text
Chef Bob: /help
Chef Bob: /plan Three dinners next week, using my saved preferences.
Chef Bob: /preferences Use tofu instead of pork from now on.
Chef Bob: /recipe-add Save the recipe below for my next plan.
```

The prefix makes these ordinary chat messages when your tool reserves slash commands. For recipe additions, paste text after the message, provide a link if browsing works, or attach a photo if image reading works. A request to add authorizes a private draft save when storage is available. The assistant should show the saved recipe and flag missing details. Ask for a preview if you want to see it without saving.

For browsing, just ask "Which of my recipes use mushrooms?" or "Show me that recipe." No extra command is needed.

## Keep a personal record

Without file access, the assistant can prepare a plan but cannot store it on your device. At the end of a session, ask it for a compact record containing:

- Household servings, allergies, food preferences and normal meal schedule.
- Any rice/noodle cycle, its next position and eligible days. Skipped meals do not advance it in v0.1.
- The accepted plan, dated exceptions and recent meals to avoid repeating.
- Personal recipes, source links and unresolved recipe details.
- Notification preference, which stays off when scheduling is unavailable.

Save the record in your own notes or private file. Paste or attach it when starting a new chat. Review it before sharing, especially in a group. A provider's chat history or memory may have its own retention rules; Chef Bob cannot guarantee persistence or privacy beyond the tool you choose.

The assistant should label a plan "ready to save" until you save it yourself. Editing a preference in chat should update the personal record, not a public repository. Adding a recipe must not trigger a public post or GitHub push.

## Understand the limits

If a link cannot be opened, paste the recipe text. If a photo cannot be read, transcribe its ingredients and steps. If the assistant loses context, provide the personal record again. If it cannot schedule or send messages, reminders remain manual.

Your selected AI service receives the material you send. Use its own settings for model access and credentials; never paste API keys or bot tokens into a recipe. Chef Bob has no separate backend and does not add a subscription, though your AI service and optional tools may charge for use.
