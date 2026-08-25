# U-GAS GitHub Workflow

Use this sequence for GitHub-backed work:

1. Inspect the canonical local clone, branch, status, remotes, and local-only history.
2. Fetch the authoritative remote branch before treating local state as current.
3. Resolve repository purpose and branch from current metadata and local rules.
4. Read relevant PICA and repository instructions.
5. Make a targeted, non-destructive change.
6. Verify the diff and relevant tests.
7. Commit on the permitted branch when the work is durable.
8. Push only to the known intended repository and branch.
9. Fetch again and verify the remote commit/content.

Do not use a stale clone as authority. Do not probe permissions with a mutation. If remote authority cannot be established, report the blocker and do not claim a remote-current PASS.
