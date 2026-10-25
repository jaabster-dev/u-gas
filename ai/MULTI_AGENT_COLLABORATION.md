# U-GAS Multi-Agent Collaboration

Use this policy when multiple agents, sessions, or executors may touch overlapping project or repository work, or when returned work must be reconciled. Do not invoke a heavy collaboration protocol for a simple single-agent task with no overlapping-work risk.

## Operational procedure

1. Treat the current repository and durable project files as the shared coordination surface. Model memory and executor/agent reports are evidence and context, not authority.
2. Before work, inspect the current branch, status, relevant files, and existing intentional work. Verify whether the requested work already exists, identify overlapping files or surfaces, and preserve unique local or other-agent work.
3. During work, make the smallest bounded change. Do not silently revert another agent or duplicate an implementation merely because the current conversation did not witness it. Preserve provenance when reconciling approaches; disagreement with intentional architecture requires evidence before replacement.
4. When work returns from another agent or executor, reconcile its prose and claimed result against the actual current repository and durable state. A clean textual merge does not prove semantic integration; inspect resulting behavior and invariants and run the required tests.
5. If ownership, intent, or current authority cannot be reconciled safely, fail closed: stop and report the exact conflict or boundary rather than choosing arbitrarily or overwriting.

## On-demand workspace interruption check

Trigger this **only** when a Git metadata write/lock failure, stale or divergent checkout, another session's changes, potentially unpublished commits, or interrupted handoff materially blocks work or risks unique work. Do not scan every workspace on every task or infer an abandoned agent from an old branch.

1. In the affected environment, identify the exact checkout/worktree path, branch, local HEAD, **verified** remote HEAD, tracked/staged/untracked changes, and local-only commits where accessible. A clean worktree does not establish that all commits were pushed. If a remote-tracking ref is stale, do not use it as proof of publication.
2. Diagnose a `.git` write failure with bounded **read-only** evidence. Distinguish permission/sandbox denial, a lock possibly held by a running process, and unknown cause. Never delete a lock, change permissions, reset, clean, force-checkout, rebase, or overwrite another session's work merely to clear the blocker.
3. Mark ownership `ACTIVE`, `POSSIBLY INTERRUPTED`, or `UNKNOWN` **only as evidence supports**; file age and lock existence alone do not prove liveness. If ownership is unresolved, preserve the affected checkout and continue independent authorized checks via a verified remote or safe isolated environment where appropriate.
4. If the blocker, potential loss of unique work, or owner/executor decision matters for continuation, report compactly: `WORKSPACE / LOCAL HEAD / VERIFIED REMOTE HEAD / DIRTY+UNTRACKED / LOCAL-ONLY COMMITS / OWNERSHIP / BLOCKER / SAFE NEXT`. Use `UNKNOWN` rather than guesses. Persist the unresolved obligation in the existing issue, handoff, or current-state surface **only when needed for successor continuity**, and verify any remote write by read-back. Routine recoverable errors need no new notification service.

This is a portable safety/continuity procedure, **not** a daemon, automatic cleanup mechanism, cross-agent lock manager, or requirement to access local processes from an environment that cannot inspect them.

## Required outcome

Leave one coherent authoritative result with unique work preserved, duplicate or conflicting changes resolved explicitly, provenance and evidence visible, remaining risk stated, and the next action plus any human/device/manual boundary clear. This policy does not introduce locking, orchestration, task boards, daemons, coordination servers, or fleet infrastructure.
