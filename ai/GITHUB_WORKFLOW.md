# U-GAS GitHub Workflow

## Standard sequence

1. Identify the exact repository and authoritative branch.
2. Inspect clone identity, branch, status, untracked files, stashes, local-only/unpushed history, and remotes.
3. Fetch before treating local state as current.
4. Read relevant PICA and repository rules; determine whether the work already exists.
5. Make the smallest safe mutation.
6. Inspect the bounded diff and run required checks.
7. Commit and push only when authorized.
8. Fetch again and verify the actual remote commit and content.
9. Record a continuity checkpoint when a material milestone, blocker, pause, or handoff changes what a successor must know.

## Canonical clone identity

Use the configurable identity `<workspace-root>/<repository-owner>/<repository-name>`. The workspace root is a container, not a repository. Verify identity from the remote URL or GitHub metadata, not from a folder name. Reuse an existing canonical clone. Before creating, moving, or deleting a duplicate, inspect unique work, untracked files, stashes, worktrees, and local-only commits.

## Local clone safety

Before editing, inspect branch/status, uncommitted and untracked work, unpushed history, remotes, and authoritative branch. Synchronize through a non-destructive fast-forward/update path when safe. Stop on real divergence or work that would be overwritten. Never reset, clean, force-overwrite, or use a stale clone as authority.

## Capability discovery and fallback

If a capability appears available but a real read/action reports unavailable, inspect capabilities read-only and make one bounded read-only retry where appropriate. Classify a persistent mismatch as connector/runtime failure; do not loop or probe with dummy mutations. Use an authorized repository-native or persistent local execution path. If only a genuine human boundary remains, ask for that one action. Do not make Codex or a particular connector mandatory.

If the current agent cannot execute a known safe operation, discover capability, use an existing repository workflow, then use an authorized persistent coding environment if available. A compact handoff may remain one complete copyable payload when it is short and reliable to transfer directly. When the complete handoff is long or materially structured, exact-payload loss is credible, the material already exists durably, or a direct clipboard/attachment attempt failed, use the repository-backed pending handoff surface described below so the owner does not shuttle routine Git or file contents manually.

Do not use a stale clone as authority. Do not probe permissions with a mutation. If remote authority cannot be established, report the blocker and do not claim a remote-current PASS.

## Procedure discovery and lifecycle detail

Read the target `AGENTS.md`, matching `ai/` policy, and relevant skill before inventing a procedure. Capability checks are non-mutating: never create dummy files, branches, commits, PRs, or permission probes.

If no remote exists, a genuinely new project may start local-first only with safe persistent storage and an explicit later publication step. Exported/downloaded artifacts are not automatically a persistent repository. Reuse `<workspace-root>/<owner>/<repo>` as the canonical clone across sessions/agents and inspect unique work before creating, moving, or deleting duplicates.

Before local work, preserve uncommitted, untracked, stashed, worktree, and local-only history. During work, do not reset, clean, force-overwrite, silently revert another agent, or use a stale clone. After work, push only to the known target/branch, fetch, and verify remote ref/content and workflow result.

A real failed write or stale SHA requires re-fetch and reconciliation, not blind retry. Use one bounded read-only retry for a connector/runtime mismatch, then use an authorized repository-native or persistent coding-agent path. If an execution handoff is necessary, provide one complete copyable payload; the returned report is evidence, not authority, so independently re-read the remote result. Follow target-defined agent/release branch roles without inventing promotion semantics.

### Choosing handoff transport

Use the normal compact one-copy path when the complete payload is short, unstructured enough to transfer reliably, and does not need exact durable preservation. Use a repository-backed pending handoff proactively when the payload is long enough that clipboard/attachment conversion or truncation is a credible risk; contains substantial structured requirements, acceptance criteria, evidence, or exact instructions; already exists as durable structured material; exact preservation matters more than one repository write; or a previous direct transfer failed or became inaccessible. This is a reliability decision, not a character-count ritual: do not create repository handoffs for ordinary short prompts.

The portable repository-local adapter uses `handoffs/pending/<handoff-id>.md`, `status: PENDING`, exact target validation, a read-only checker, and removal only after verified completion. It has no auto-executor, daemon, orchestration, arbitrary remote execution, secret storage, or user-managed file-transfer step.

For small files, obtain a complete current read. For large/truncated/append-only/structured files, route to `ai/LARGE_FILE_PATCHING.md` and its skill. A complete current file plus current identity guard and bounded diff is the minimum safe full-content update property. Routine Git/file/test mechanics are agent-owned; human approval is for credentials/secrets, destructive or irreversible actions, devices, product judgment, and material cost/security/legal/account effects.
