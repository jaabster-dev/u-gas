# U-GAS Compliance Contract

This is a portable, local, read-only self-check contract. It protects the public U-GAS distribution surface; it is not organization-wide fleet compliance and does not synchronize consumers.

## Invariants

- The four root PICA controls exist.
- Missing controls may use `templates/pica/`; substantive existing controls are not overwritten.
- A project bootstrapped from U-GAS templates has an explicit canonical upstream anchor in its target `AGENTS.md`.
- Referenced local canonical documents and route targets exist.
- `IDEAS.md` has one canonical responsibility and is not casually duplicated.
- README is navigation, not a second state/progress/spec authority.
- U-GAS source self-tests protect this distribution contract.
- Diagnostics are read-only unless an actual authorized repair is separately requested.

There are two bounded check modes:

- distribution mode checks U-GAS's own files, routes, templates, examples, README markers, and public-content hygiene;
- `--project <path>` checks only the target project's readable/non-empty PICA set, exact canonical upstream anchor, and either the canonical minimal `CURRENT_STATE.md` placeholder or its four resume responsibilities.

These checks do not prove product correctness, whether `ACTIVE`/`NEXT` are true, runtime/model compliance, successful GitHub access, branch correctness, repository safety, or independent validation. `scripts/check_u_gas.py` must not infer product scope, rewrite files, install dependencies, call GitHub, or claim evidence beyond local checks. Fleet registries, managed blocks, organization sync, and consumer rewrites are intentionally outside U-GAS.

The optional repository-backed handoff adapter is local and fail-closed: only `PENDING` payloads with valid metadata and non-empty contract sections are executable; consumed or missing payloads cannot be replayed. Compact one-copy prompts remain the default. The adapter does not execute payloads, call GitHub, store secrets, or create orchestration.
