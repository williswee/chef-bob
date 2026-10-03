# Reporting a security issue

Use GitHub's private [Report a vulnerability](https://github.com/williswee/chef-bob/security/advisories/new) form for credentials, private-data exposure, unsafe file writes, or other security problems. Do not put exploit details, tokens, household profiles, or meal-history files in a public issue.

Include the Chef Bob version, the AI tool and version, what happened, and a small reproduction using fictional data. Redact credentials and personal details. Reports are handled on a best-effort basis.

For an ordinary setup problem, use a GitHub issue with sanitized error output.

## Data boundaries

Household profiles, personal recipes, and plans belong outside the public checkout. The helper enforces this for its own writes. The AI tool still controls its conversation history, uploads, and connected accounts, so use its settings to review retention and access.

Chef Bob does not run a hosted service or collect telemetry. It does not need access to email, calendar, unrelated files, or a maintainer's accounts. Notification delivery uses the user's chosen AI host and channel only after they enable it.
