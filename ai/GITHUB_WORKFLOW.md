# U-GAS GitHub Workflow

## Pending acceptance evidence — durable handoff before final report

When an accepted task has a material `UNKNOWN`, `FAIL`, `SKIPPED`, or `BLOCKED` acceptance condition that a successor must resolve, **do not present partial test success as complete acceptance**. Complete the independent safe checks still available; before the final report, save the exact target branch/commit, observed evidence, missing proof, and next capable executor/action in the **existing** issue/PR or canonical project continuity surface. Verify the saved checkpoint by remote read-back when available. If persistence fails, report `HANDOFF NOT SAVED / PARTIAL`; do not claim durable handoff. Avoid a new tracker or noisy checkpoint for a transient issue that does not affect future work.

For a local checkout collision or `.git` metadata write denial, use the on-demand ownership check in `ai/MULTI_AGENT_COLLABORATION.md` before any cleanup or forced synchronization. Continue independent authorized work; do not equate clean status with no unpublished commits.

## Task-scoped execution capability and continuation

At task entry, identify the acceptance condition and discover **only** the tools needed to implement and verify it. Prefer authorized direct repository operations when they suffice; use the existing terminal, CI, or capable executor when actual test execution is needed. A tool name alone is not evidence of successful access. If the preferred route fails, try one materially different authorized route and continue independent work. Do not require a local checkout when a verified remote read/write route suffices.

**Acceptance conditions, not commits, determine completion.** After **every** successful edit, commit, remote verification, or test checkpoint:

1. Re-read authoritative branch/HEAD and reconcile concurrent work; verify exact-commit test/CI results as PASS, FAIL, PENDING, SKIPPED, or NOT RUN.
2. Compare all remaining acceptance conditions with evidence. A green subtest or one successful commit is a checkpoint, not a final result while other conditions remain.
3. If any safe, authorized, concrete next step remains, **execute it** without routine owner reauthorization. Prefer independent work while CI runs; commit and verify justified changes, then repeat.
4. Stop only when acceptance is met, a genuine owner decision/permission is needed, an evidenced technical capability blocker remains after a meaningful fallback, or an actual execution/time limit prevents further calls. `PARTIAL`, pending CI, and a successful commit are **not** themselves stop conditions.
5. Bound CI polling; never wait indefinitely. If execution must end, use the existing live-state/handoff authority to record branch, HEAD, CI run ID/URL, unresolved acceptance conditions, attempted alternatives, and the **next executable action**. Do not promise automatic resumption without a real scheduler.

**Regression example:** four CI failures are in scope; after fixing one and committing, three remain and CI is pending. Continue resolving independently actionable failures rather than returning a terminal `PARTIAL`. Do not weaken tests or invent evidence just to claim PASS.

## Standard sequence

1. Identify the exact repository and authoritative branch.
2. Inspect clone identity, branch, status, untracked files, stashes, local-only/unpushed history, and remotes.
3. Fetch before treating local state as current.
4. Read relevant PICA and repository rules; determine whether the work already exists.
5. Make the smallest safe mutation.
6. Inspect the bounded diff, account for every changed file against the accepted task contract, and run required checks.
7. Commit and push only when authorized.
8. Fetch again and verify the actual remote commit and content.
9. Record a continuity checkpoint when a material milestone, blocker, pause, or handoff changes what a successor must know.

## Optional repository-health preflight

For a repository with a distinct authoritative working branch and release branch, `scripts/check_repository_health.py` provides a small read-only local preflight. Run it only when branch-role health matters; it is not a mandatory ceremony for every task. Supply the already-established authority branch and optional release branch. `GREEN` allows the ordinary case where the authority branch is ahead; `RED` means the release branch contains unique commits outside authority; missing refs or Git failures are visible as `ERROR`. The sensor reports evidence only: it never fetches, repairs, resets, merges, or rewrites repository state. Establish branch roles from current repository authority first; do not let the checker invent them.

## Mutation side effects and atomic publication

The scope of a remote mutation includes known automatic consequences of publishing it, not only the files in the diff. Before a commit/push/ref update that is known to trigger CI, builds, deployments, notifications, quota/cost consumption, release automation, or other external work, account for those consequences when selecting the mutation mechanism. Do not make the user absorb avoidable failure notifications or automation churn as an implementation detail.

When several interdependent file/state changes form one validity unit and publishing them sequentially would create a **known invalid intermediate remote state**, prefer an available atomic repository mutation: prepare the complete tree/commit first, then publish the ref once and verify the resulting automation. Do not weaken validators, skip required CI, or batch unrelated changes merely to keep runs green. Sequential publication remains correct when intermediate states are independently valid, atomic publication is unavailable/unsafe, or a genuine diagnostic run is required.

## Canonical clone identity

Use the configurable identity `<workspace-root>/<repository-owner>/<repository-name>`. The workspace root is a container, not a repository. Verify identity from the remote URL or GitHub metadata, not from a folder name. Reuse an existing canonical clone. Before creating, moving, or deleting a duplicate, inspect unique work, untracked files, stashes, worktrees, and local-only commits.

The current working directory alone does not establish that a known repository is unavailable. Before returning `REPOSITORY UNAVAILABLE` / `PARTIAL`, resolve the target identity and authoritative branch from current repository authority, inspect the current workspace, then search only already-known canonical checkout locations from the configured workspace root or an existing authoritative workspace mapping. Accept a candidate only when it is a Git checkout whose configured remote identifies the target; a same-named path or mismatched/ambiguous remote fails closed. Inspect candidate status and local history before reuse, preserving dirty, divergent, or unexpected state under the local-clone rules below. When a safe matching checkout is found elsewhere, report its path briefly and continue there. Do not add a path registry, ask the owner to locate a deterministically discoverable checkout, or automatically clone solely for discovery. Report unavailable only after this bounded discovery fails.

## Local clone safety

Before editing, inspect branch/status, uncommitted and untracked work, unpushed history, remotes, and authoritative branch. Synchronize through a non-destructive fast-forward/update path when safe. Stop on real divergence or work that would be overwritten. Never reset, clean, force-overwrite, or use a stale clone as authority.

## Capability discovery and fallback

If a capability appears available but a real read/action reports unavailable, inspect capabilities read-only and make one bounded read-only retry where appropriate. Classify a persistent mismatch as connector/runtime failure; do not loop or probe with dummy mutations. Use an authorized repository-native or persistent local execution path. If only a genuine human boundary remains, ask for that one action. Do not make Codex or a particular connector mandatory.

Public-source reading is separate from authenticated GitHub connector/API access, local Git networking, and persistent local execution. When a task names a public GitHub HTTPS URL, actually attempt to open/read that URL with an available safe read-only web, browser, or fetch method before reporting the public source inaccessible. If one read method is unavailable, discover or use another available read-only method when the runtime exposes one. Evaluate public-source read, persistent filesystem, and local Git independently: failure of one does not prove failure of the others. Do not use a write or dummy mutation to probe any of them.

If the current agent cannot execute a known safe operation, discover capability, use an existing repository workflow, then use an authorized persistent coding environment if available. A compact handoff may remain one complete copyable payload when it is short and reliable to transfer directly. When the complete handoff is long or materially structured, exact-payload loss is credible, the material already exists durably, or a direct clipboard/attachment attempt failed, use the repository-backed pending handoff surface described below so the owner does not shuttle routine Git or file contents manually.

Do not use a stale clone as authority. Do not probe permissions with a mutation. If remote authority cannot be established, report the blocker and do not claim a remote-current PASS.

During implementation, perform a scope reset when the diff grows beyond the expected bounded change, a new dependency appears, or a useful discovery tempts adjacent work. Restate the objective, accepted scope, non-goals, verification, and boundaries; then continue only the smallest necessary path. Before completion, every changed file must be relevant to the accepted scope. Preserve useful discoveries as parked ideas or explicit follow-ups without silently implementing them.

## Machine-handoff execution

`ai/SESSION_CONTINUITY.md` owns the handoff semantics; this workflow owns safe repository and artifact mechanics. For an explicit physical-machine switch, start from the concrete next action and verify its required repository, artifact, execution, device, and external-service dependencies on the target environment. Routine reversible Git work and non-sensitive artifact copy/checksum work to an already owner-approved destination may be agent-owned when authorized. Do not invent a shared destination, upload sensitive signing/credential material to generic cloud storage, or rebuild a qualified immutable artifact merely to make it portable. When no safe transfer/access path exists, report `MACHINE HANDOFF: PARTIAL` or `BLOCKED` with the exact remaining dependency.

## Procedure discovery and lifecycle detail

Read the target `AGENTS.md`, matching `ai/` policy, and relevant skill before inventing a procedure. Capability checks are non-mutating: never create dummy files, branches, commits, PRs, or permission probes.

If no remote exists, a genuinely new project may start local-first only with safe persistent storage and an explicit later publication step. Exported/downloaded artifacts are not automatically a persistent repository. Reuse `<workspace-root>/<owner>/<repo>` as the canonical clone across sessions/agents and inspect unique work before creating, moving, or deleting duplicates.

Before local work, preserve uncommitted, untracked, stashed, worktree, and local-only history. During work, do not reset, clean, force-overwrite, silently revert another agent, or use a stale clone. After work, push only to the known target/branch, fetch, and verify remote ref/content and workflow result.

A real failed write or stale SHA requires re-fetch and reconciliation, not blind retry. Use one bounded read-only retry for a connector/runtime mismatch, then use an authorized repository-native or persistent coding-agent path. If an execution handoff is necessary, provide one complete copyable payload; the returned report is evidence, not authority, so independently re-read the remote result. Follow target-defined agent/release branch roles without inventing promotion semantics.

### Choosing handoff transport

Use the normal compact one-copy path when the complete payload is short, unstructured enough to transfer reliably, and does not need exact durable preservation. Use a repository-backed pending handoff proactively when the payload is long enough that clipboard/attachment conversion or truncation is a credible risk; contains substantial structured requirements, acceptance criteria, evidence, or exact instructions; already exists as durable structured material; exact preservation matters more than one repository write; or a previous direct transfer failed or became inaccessible. This is a reliability decision, not a character-count ritual: do not create repository handoffs for ordinary short prompts.

The portable repository-local adapter uses `handoffs/pending/<handoff-id>.md`, `status: PENDING`, exact target validation, a read-only checker, and removal only after verified completion. Before issuing a launcher, the originating agent must validate the exact payload against its intended target, commit/push it, fetch/read back authoritative state, and validate that exact read-back payload again with `--handoff-id <handoff-id> --target <owner/repo>`. Only a passing exact check may produce `HANDOFF_READY`; if it fails, fix the payload itself and do not expose a broken launcher or ask the owner to relay errors. The actual execution path must resolve the expected target independently and pass `--target <owner/repo>`; omitting `--target` is reserved for intentionally generic read-only validation. `target_branch` is either an explicit safe branch name or the documented authority-resolution rule. After completion, remove the exact payload, re-fetch authoritative state, and verify the exact path is absent before calling it consumed. The checker cannot prove historical consumption from an already absent file. It has no auto-executor, daemon, orchestration, arbitrary remote execution, secret storage, or user-managed file-transfer step.

For small files, obtain a complete current read. For large/truncated/append-only/structured files, route to `ai/LARGE_FILE_PATCHING.md` and its skill. A complete current file plus current identity guard and bounded diff is the minimum safe full-content update property. Routine Git/file/test mechanics are agent-owned; human approval is for credentials/secrets, destructive or irreversible actions, devices, product judgment, and material cost/security/legal/account effects.

## GitHub Issue as an execution handoff — owner-tested pattern (2026-10-15)

For a multi-phase repository task with existing GitHub Issues, prefer a **specific Issue section** (for example `CODEX EXECUTION HANDOFF / RUN UNTIL HUMAN GATE`) as the durable executor instruction when it is already the project's task surface. A short launcher may point to the exact issue/section rather than repeat the whole plan in chat. A versioned repository document can hold structured tests/evidence and be linked from the Issue. Do not create an Issue merely to route a trivial change; do not duplicate an existing canonical spec, current state, or history. The Issue coordinates a bounded task; `CURRENT_STATE.md` remains live project continuity, `PROGRESS.md` history, and source/commit/test artifacts evidence.

The handoff must identify repository and authoritative branch, approved objective and exclusions, available evidence, commands/acceptance checks, expected durable updates, and actual stop conditions. Explicit `RUN UNTIL HUMAN GATE` means continue through all independently authorized, executable, verifiable phases, fix evidence-backed defects, commit verified work and reconcile Issue/current state; **not** stop after each test phase or request a routine "continue". It never overrides authorization, scope, safety, cost, device/access gates, or a failed prerequisite. If no productive authorized next action remains, report the precise gate and stop without inventing work. Do not loop on already attempted diagnostics unless a material premise changed (see `ai/GOVERNANCE.md`).

The executor's final report should distinguish completed work and commit/remote verification from partial, skipped, unverified, and device-gated checks, and leave one concrete next action. Owner-observed positive example: GridGrabber Issue #171, `dev`, 2026-10-14/15 ResultsRow production slice: Codex reported 92/92 SPS, 611 PASS/22 SKIP, Chrome and iOS simulator evidence, verified commit `383311c7dfcf20ed03b2d2f7e0a03881ed6bd14d`, and correctly retained Phone `PARTIAL / UNFROZEN` pending physical-device and broader parity checks. This is a reported, bounded successful handoff, **not** independent proof of arbitrary unattended execution or all Phone parity. No new executor runtime or issue automation is implied.

## Bidirectional Issue execution ledger (portable contract)

**Ownership/privacy prerequisite:** The Issue and execution reports belong exclusively in the **user's own target-project GitHub repository**, with its existing visibility and access policy; never create user task Issues in `jaabster-dev/u-gas` or any GAS maintainer repository. A public target repository makes its Issues public: check visibility and sensitive content before writing, and fail closed or use private/local versioned handoff when inappropriate. A local-only project or user without GitHub stays local-first; never require GitHub signup, publishing, or a paid tier. Do not create a remote or change repository visibility to enable this transport.



**Purpose:** keep long executor prompts and return reports out of chat without losing a resumable, auditable task record. Use the existing task Issue when it already exists and GitHub read/write access is verified. For substantial new multi-session work, create one Issue only when the repository already uses Issues and the owner authorized tracking; otherwise use the existing versioned repository handoff or one-copy return. This is an optional transport, not a new PICA authority, GitHub dependency, service, or background worker.

### Names and ownership

- **Issue title:** `[Area] Outcome` (e.g. `[Phone] Verify ResultsRow behavior`), not `Codex session 12`. One Issue = one bounded outcome; avoid Issue-per-phase.
- **Issue body sections:** `## OUTCOME & SCOPE`, `## AUTHORITY & GATES`, `## EXECUTION HANDOFF / RUN UNTIL HUMAN GATE`, `## CURRENT CHECKPOINT`. Keep the handoff concise and link existing versioned source/spec/evidence files; do not paste logs. The Issue body is the *current instruction*; do not silently rewrite historical comments.
- **Executor report comment heading:** `## EXECUTION REPORT — YYYY-MM-DD — <short slice>`. Fields: `RESULT` (PASS/PARTIAL/BLOCKED), `BASE → FINAL` (branch, commit IDs, remote verification), `CHANGES` (bounded paths), `CHECKS` (commands, counts, SKIP/UNKNOWN), `EVIDENCE` (permalinks), `GATES` (why stop), `NEXT ACTION` (owner or executor, concrete). Keep it short; place bulky outputs in repository evidence files or CI artifacts. Never include credentials, personal data, or confidential local paths in a public Issue.
- **Chat return:** one short status + Issue URL/comment permalink + commit + real HUMAN GATE if any. Do not paste the full report. If an executor cannot post the report, return `ISSUE WRITE NOT VERIFIED` with a single complete copyable fallback report; never claim it was recorded.

### Exact round-trip

1. **Coordinate:** establish repo, authoritative branch, Issue identity and owner-approved scope. Read the Issue body, latest relevant execution report, `CURRENT_STATE.md`, and actual Git/CI state. Resolve contradictions against current authority before launching; avoid rereading the entire comment history on every pass.
2. **Prepare:** update the Issue's *current* handoff/checkpoint only when needed, with objective, exclusions, required tests, evidence links, branch and stop gates. Verify the published Issue read-back before a short launcher such as `Execute <repo>#<issue> / EXECUTION HANDOFF / RUN UNTIL HUMAN GATE; record report in the same Issue; continue until a real gate`. Do not treat a chat prompt as permission to broaden scope.
3. **Execute:** Codex or another authorized executor works through successive independent phases, checks previous attempts before retries, runs applicable tests, commits approved changes, verifies remote refs, and reconciles project `CURRENT_STATE.md` when live obligations change. Stop for a real HUMAN GATE, failed prerequisite, material authorization/cost boundary, or lack of useful safe work.
4. **Return:** append **one report comment per material execution run or checkpoint**, not per test, commit, or phase. Prefer one final report at the end of a run; if a run is interrupted, post a checkpoint only if durable state actually changed. Verify the comment by fetching it back, and include the verified comment URL in the short chat response. The report must not turn SKIP, simulated evidence, or an unverified push into PASS.
5. **Reconcile:** the coordinating chat reads the report and independently checks material remote claims before acting. Update the Issue's `CURRENT CHECKPOINT` only for a changed next action/gate, and keep `CURRENT_STATE.md` authoritative for project-wide live state. Historical report comments are immutable evidence in ordinary operation; corrections go in a new comment.
6. **Close:** close as `completed` only after acceptance evidence and required owner gates are satisfied; close as `not planned` when cancelled/superseded, linking the replacement. A HUMAN GATE means **open/waiting**, not completed. On close, leave a final short summary and links to commits/evidence, reconcile project state, and verify Issue state. Closed Issues remain searchable history.

### Context budget, rollover, and retention

Do **not** auto-delete Issues after N days, comments, tokens, or runs. GitHub Issue deletion is destructive and unnecessary for context savings. To bound context, read the Issue body + newest relevant report + current project state, following older evidence links only when necessary. When an Issue's scope materially changes, its current instruction becomes unwieldy, or the outcome must split, write a concise verified checkpoint, open a successor Issue **only if genuinely needed**, cross-link both, and close the superseded Issue as `not planned` or completed as appropriate. Never split solely because a timer or arbitrary comment count fired. No scheduler, bot, label automation, retention daemon, or automatic deletion is part of this contract.

**Fallback:** If Issue access, permissions, or comment read-back fails, use the existing repository-backed `handoffs/pending/` transport where appropriate, or a complete one-copy executor return. Do not duplicate the same active instruction across Issue and pending handoff without explicitly identifying one authority. Preserve the exact result and report `PARTIAL` until durable write/read-back succeeds.
