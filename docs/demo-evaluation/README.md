# Demo evaluation summary

Version 6 is the selected [demo guide](../demo.md). It scored 9.00 out of 10, tied with versions 7, 9, and 10. The predefined earlier-round tie-breaker selected version 6. This does not establish a meaningful advantage over the other tied versions.

GPT-6.1 Sol with ultra reasoning acted as the adversarial tester and evaluator. Ten frozen candidates each received the same four-turn conversation, followed by one distinct adversarial challenge. The study recorded 50 generated replies. Each candidate used a fresh responder; the responder model identity was not exposed by the runtime.

## Ranking

Each criterion uses a score from 1 to 10, with equal weight in the mean. Scores cover the shared four-turn conversation and were frozen before the additional challenge. Candidates with observed blockers could not win; none were observed in these tested turns.

| Rank | Version | Delightful UX | Ease of use | Context capturing | Clarity | Mean |
| ---: | --- | ---: | ---: | ---: | ---: | ---: |
| 1 | v06: Complete handoff | 8 | 9 | 9 | 10 | 9.00 |
| 2 | v07: Focused edits | 8 | 9 | 9 | 10 | 9.00 |
| 3 | v09: Shorter entry menu | 8 | 9 | 9 | 10 | 9.00 |
| 4 | v10: Structured combined reply | 8 | 9 | 9 | 10 | 9.00 |
| 5 | v08: Less metadata repetition | 7 | 9 | 9 | 10 | 8.75 |
| 6 | v02: Compact combined reply | 8 | 9 | 9 | 9 | 8.75 |
| 7 | v04: Result-first recipe adding | 8 | 9 | 9 | 9 | 8.75 |
| 8 | v05: Scoped context summary | 7 | 9 | 9 | 8 | 8.25 |
| 9 | v01: Initial demo | 7 | 8 | 9 | 8 | 8.00 |
| 10 | v03: Separate household trials | 6 | 6 | 7 | 8 | 6.75 |

Ties were resolved by context capturing, clarity, fewer unnecessary user turns, then earlier round. The top four tied on every substantive criterion, including zero unnecessary turns. Among the 8.75 candidates, v08 ranks ahead on clarity; v02 and v04 then tie fully, so earlier v02 ranks first. Reply length was not a tie-breaker.

## What changed through testing

The selected version demonstrated recipe adding through a revised plan, reconciled grocery quantities, and included enough source information in its handoff for another chat to continue. It kept household facts, dated exceptions, and trial choices distinct.

Some later versions reduced repeated explanation, but did not improve their overall score. Other changes left a planning conflict unresolved or produced a less varied plan. The selected version's combined reply was still 402 words under the study's whitespace-count method. That remains its main weakness for the human trial.

Rounds 1 and 2 were sequential improvements. The remaining rounds compared independent alternatives in pairs, using completed earlier feedback. They were not ten successive revisions of a single candidate.

## Limits

These are AI judgments from one generated baseline conversation per candidate and one evaluator. The study does not provide statistical confidence or prove that wording alone caused each difference. It did not measure human enjoyment or test live OpenClaw delivery, actual storage, scheduling, or external recipe imports.

Each candidate received only one additional adversarial challenge. The selected version's challenge concerned instructions embedded in recipe text; it was not tested against all ten challenges. Broader user needs and longer histories still need testing. The recipes remain untested cooking examples.

The published guide matches the tested version 6 exactly. Its SHA-256 is `f32db6a6c6f7a15ac44df11cb440cf9194e483ff91a6749877f3c90860381898`.

## Try it

Follow the [README demo instructions](../../README.md#try-the-demo-first), then use your own preferences and corrections. Try a one-night serving change, a recipe addition, and a handoff. The demo should preserve context, update quantities, and keep changes in the trial until you choose to use it for real.
