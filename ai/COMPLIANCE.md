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

`scripts/check_u_gas.py` checks only what it implements and must not infer product scope, rewrite files, install dependencies, call GitHub, or claim evidence beyond local checks. Fleet registries, managed blocks, organization sync, and consumer rewrites are intentionally outside U-GAS.
