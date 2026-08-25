# U-GAS Multi-Agent Collaboration

- The repository, not model memory, is the shared coordination surface.
- Read current state and verify whether requested work already exists before acting.
- Do not silently revert another agent or duplicate work merely because the current conversation did not witness it.
- When sources disagree, preserve provenance and reconcile against current repository and owner authority.
- Leave a handoff with canonical files correct, evidence clear, temporary artifacts handled, remaining risk explicit, and the next action concrete.
- A clean textual merge does not automatically prove semantic integration correctness; inspect the resulting behavior and invariants.
- Do not add locking, orchestration, task-board, or fleet infrastructure here.
