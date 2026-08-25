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

If the current agent cannot execute a known safe operation, discover capability, use an existing repository workflow, then use an authorized persistent coding environment if available. A handoff must contain one complete copyable payload; the owner should not shuttle routine Git or file contents manually.

Do not use a stale clone as authority. Do not probe permissions with a mutation. If remote authority cannot be established, report the blocker and do not claim a remote-current PASS.
