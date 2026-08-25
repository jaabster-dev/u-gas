# U-GAS Repository Structure

Every active U-GAS-managed project visibly exposes these root controls:

- `AGENTS.md` — agent instructions;
- `CURRENT_STATE.md` — compact current state and resume action;
- `PROGRESS.md` — chronological history/evidence;
- `IDEAS.md` — unaccepted ideas parking lot.

`README.md` is the short human entry point and should link to, rather than duplicate, the other responsibilities. Additional documents are optional and responsibility-driven. Do not create a backlog, installer, orchestration layer, or new document hierarchy merely to make a project appear complete.

## Lightweight change specification

For a non-trivial accepted behavior or product change with interacting requirements, edge cases, ambiguity rules, or important user-visible scenarios, use the smallest sufficient existing canonical spec/decision document. It should state objective/why, accepted scope, non-goals, requirements, representative positive and negative/unsafe cases, invariants, and acceptance/verification criteria. Do not add a new framework or folder merely to satisfy this guidance.

`IDEAS.md` is not accepted scope. `PROGRESS.md` is not a specification. `CURRENT_STATE.md` is not history. `README.md` is not the canonical home for every policy.
