# U-GAS Repository Structure

## Canonical responsibilities

Every active U-GAS-managed project visibly exposes these root controls:

- `PROGRESS.md` — chronological history and evidence;
- `IDEAS.md` — unaccepted possibility space;
- `CURRENT_STATE.md` — compact current state and resume action;
- `AGENTS.md` — agent instructions and routing.

`README.md` is human navigation, not duplicate authority. Missing controls may use truthful templates; substantive existing content must be preserved. Additional documents are optional and responsibility-driven, and referenced optional documents must exist. Do not create a backlog framework, installer, orchestration layer, or new document hierarchy merely to make a project appear complete.

`IDEAS.md` is not accepted scope, a requirement, roadmap, backlog, or authorization. The explicit lifecycle remains `IDEA -> PARKED -> RESEARCHED -> ACCEPTED -> BACKLOG/SCOPE`. During migration, preserve provenance and migrate PICA additively and conservatively; do not concatenate overlapping documents blindly.

Repository name or presence does not establish product purpose. If purpose is unknown, allow only neutral maintenance, ask the smallest owner question, and record a minimal durable purpose after clarification.

## Lightweight change specification

For a non-trivial accepted behavior or product change with interacting requirements, edge cases, ambiguity rules, or important user-visible scenarios, use the smallest sufficient existing canonical specification or decision document. It must state:

- objective and why;
- accepted scope and non-goals;
- requirements;
- representative positive and negative, ambiguous, or unsafe cases;
- invariants;
- verification, acceptance, and evidence criteria.

`PROGRESS.md` is not a specification. `CURRENT_STATE.md` is not history. `README.md` is not the canonical home for every policy. Do not add a framework or folder merely to satisfy this guidance.
