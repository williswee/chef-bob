# Changelog

## Unreleased

- Onboarding starts with Bob's introduction, an optional nickname, and a short invitation to introduce yourself.
- Questions use the host's real choice controls when available, with optional free text and a stated fallback for text-only hosts. The new flow is unscored and supersedes the original v06 entry.
- Interactive `/demo` with a trial plan, conversational edits, and a handoff to real use.
- `/demo` replaces the dedicated help command. Type "help" for the menu; the four commands remain `/demo`, `/plan`, `/preferences`, and `/recipe-add`.
- Demo changes stay in the conversation and do not update personal files or notification jobs.
- README and adapter examples explain how to start the demo before setup.
- Ten earlier demo versions tested with GPT-6.1 Sol at ultra reasoning as the adversarial judge, with an aggregate scorecard and explicit tie handling. Version 6 was the selected default before the onboarding changes.

## 0.1.0 - 3 October 2026

- First public Chef Bob package with fresh repository history.
- Four conversational commands: help, planning, preferences, and recipe additions.
- AI-guided onboarding, configurable meal preferences, and private local data storage.
- A formatted collection of 104 imported recipe entries and six original starter recipes.
- OpenClaw, Hermes, and generic-chat setup guides with explicit capability limits.
- Local helper checks for profiles, recipe additions, and weekly plan history.

Imported recipes retain unresolved source details. The initial release does not claim that every recipe is kitchen-tested or that automated messaging has been tested on every host.
