# U-GAS Multi-Agent Collaboration

Use this policy when multiple agents, sessions, or executors may touch overlapping project or repository work, or when returned work must be reconciled. Do not invoke a heavy collaboration protocol for a simple single-agent task with no overlapping-work risk.

## Operational procedure

1. Treat the current repository and durable project files as the shared coordination surface. Model memory and executor/agent reports are evidence and context, not authority.
2. Before work, inspect the current branch, status, relevant files, and existing intentional work. Verify whether the requested work already exists, identify overlapping files or surfaces, and preserve unique local or other-agent work.
3. During work, make the smallest bounded change. Do not silently revert another agent or duplicate an implementation merely because the current conversation did not witness it. Preserve provenance when reconciling approaches; disagreement with intentional architecture requires evidence before replacement.
4. When work returns from another agent or executor, reconcile its prose and claimed result against the actual current repository and durable state. A clean textual merge does not prove semantic integration; inspect resulting behavior and invariants and run the required tests.
5. If ownership, intent, or current authority cannot be reconciled safely, fail closed: stop and report the exact conflict or boundary rather than choosing arbitrarily or overwriting.

## Required outcome

Leave one coherent authoritative result with unique work preserved, duplicate or conflicting changes resolved explicitly, provenance and evidence visible, remaining risk stated, and the next action plus any human/device/manual boundary clear. This policy does not introduce locking, orchestration, task boards, daemons, coordination servers, or fleet infrastructure.
