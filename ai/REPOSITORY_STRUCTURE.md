# U-GAS Repository Structure

Every active U-GAS-managed project visibly exposes these root controls:

- `PROGRESS.md` — chronological history/evidence;
- `IDEAS.md` — unaccepted ideas parking lot;
- `CURRENT_STATE.md` — compact current state and resume action;
- `AGENTS.md` — agent instructions.

`README.md` is the short human entry point and should link to, rather than duplicate, the other responsibilities. Additional documents are optional and responsibility-driven. Do not create a backlog, installer, orchestration layer, or new document hierarchy merely to make a project appear complete.

## Lightweight change specification

For a non-trivial accepted behavior or product change with interacting requirements, edge cases, ambiguity rules, or important user-visible scenarios, use the smallest sufficient existing canonical spec/decision document. It should state objective/why, accepted scope, non-goals, requirements, representative positive and negative/unsafe cases, invariants, and acceptance/verification criteria. Do not add a new framework or folder merely to satisfy this guidance.

`IDEAS.md` is not accepted scope. `PROGRESS.md` is not a specification. `CURRENT_STATE.md` is not history. `README.md` is not the canonical home for every policy.

## Full responsibility boundaries

`AGENTS.md` owns instructions/routing and safe handoff; `CURRENT_STATE.md` owns compact current state; `PROGRESS.md` owns chronological evidence; `IDEAS.md` owns unaccepted possibility space. Missing controls may use templates, but truthful placeholders and substantive existing content must be preserved. IDEAS is not a requirement, roadmap, backlog, or authorization. A useful lifecycle is `IDEA -> PARKED -> RESEARCHED -> ACCEPTED -> BACKLOG/SCOPE`; acceptance is explicit.

Repository name/presence does not establish product purpose. If purpose is unknown, allow neutral maintenance, ask the smallest owner question, and record a minimal durable purpose after clarification. Optional documents are responsibility-driven; if instructions reference one, it must exist. Do not force global filenames or concatenate overlapping documents blindly during migration: preserve provenance and migrate PICA additively/conservatively.

For a non-trivial accepted change, the smallest sufficient spec states objective/why, accepted scope, non-goals, requirements, positive cases, negative/ambiguous/unsafe cases, invariants, and verification criteria. `PROGRESS` is not `CURRENT_STATE` or a spec, and README is navigation rather than the canonical home for everything.
