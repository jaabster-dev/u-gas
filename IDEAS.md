# Ideas

> Empty shelf, open<br>
> Future thoughts will rest here<br>
> Nothing parked today

Future entries remain unaccepted unless explicitly promoted through a separate scope or product decision.

## 2026-08-28 — arka.norn comparative research (PARKED)

Primary source: https://github.com/arka-squad/arka-norn

This is external comparative research only. It is not U-GAS authority, a dependency, validation, or accepted implementation scope.

- Mechanical evidence: arka.norn separates agent claims from mechanically produced proof/receipts. Research question: for consequential invariants, should AI-reported evidence be labelled more explicitly apart from mechanically verified evidence? Existing U-GAS/GAS principle remains: verify the result, not prose. This does not authorize a new enforcement engine.
- Fail-closed scope and ownership: ambiguous ownership can block execution rather than silently expand scope. This supports smallest-valid-change and validate-target discipline; scope ambiguity must not become broader agent authority.
- Preview, fingerprint, authorization: approval can bind to a specific plan/risk-policy fingerprint and checked state. Research question: if a future action crosses a consequential boundary, should authorization bind to the concrete target/state rather than abstract intent? Do not add fingerprinting for theoretical completeness.
- Dirty or divergent repository: automatic apply can fail closed when the real repository no longer matches the approved preview. Check whether current U-GAS/GAS reconciliation already protects this boundary; if it does, add nothing.
- Unknown remains unknown: unobservable measurements stay unknown rather than being invented. Existing evidence-over-inference governance likely already covers this.
- Architecture boundary: arka.norn is a substantially heavier execution/enforcement/orchestration framework with plans/DAGs, branches/worktrees, execution profiles, brokered tools, container recipes, budgets, risk scoring, and integrator flow. U-GAS remains a lightweight portable continuity/coordination operating model; GAS remains private governance/semantic/repository infrastructure with selective enforcement where justified. arka.norn is a comparator, not the target architecture.

U-GAS complexity rule remains in force: do not add a runtime, orchestrator, broker, DAG, sandbox, budget, or risk subsystem without repeated failure evidence and proof that the simpler existing mechanism is insufficient.

## 2026-08-28 — Additional agent-workflow comparators (PARKED)

This is external comparative research only. It is not U-GAS authority, validation, a dependency, backlog, or accepted implementation scope. Sources were read as public research except Terrarium, which remains owner-supplied showcase evidence and was not independently inspected in this pass.

- Terrarium / Grainwork — [terrarium.watch](https://terrarium.watch/#pricing): owner-supplied evidence describes separation of agent-reported progress, the targeted file/worktree, and mechanically observed disk change after a failure mode where repeated test runs looked like progress while little product work moved. Compare with the existing U-GAS/GAS rule that write/test/report success is not verified completion. Research question: do consequential workflows need a clearer distinction between agent-reported progress and mechanically observed change? Do not infer or adopt a watcher/dashboard from this evidence.
- [Agent OS](https://github.com/andrewgolovanov/agent-os) — a local-first Codex task board/control plane with durable goals, current state, next action, blockers/sources, linked tasks, completion history, private operational state, and an optional native macOS app/runtime. This independently supports the problem that continuity should not live only in chat history. Compare its dedicated operational-state architecture with U-GAS's lighter repository/project-native PICA and `GIVE THIS TO YOUR NEXT AI CHAT.txt`. Research question: does independent U-GAS testing reveal a small human-facing continuity affordance those existing surfaces do not provide? Do not add another state database, native app, runtime, or task board without real failure evidence.
- [Behavior Profiles](https://github.com/Secondmindsystems/Behavior-Profiles) — durable/testable conduct specifications make requested task, authorized scope, no-touch boundaries, authorized actions, done condition, and stop/flag condition explicit. Its public proof boundary distinguishes structural/package checks, synthetic harness controls, bounded observed behavior, and independent external validation; verifier PASS does not prove agent obedience, and instruction-layer profiles are distinct from an experimental enforcement/runtime layer. Research question: are U-GAS scope/done/stop boundaries sufficiently observable and testable in real use without another profile framework? Prefer existing AGENTS/governance/tests; do not add a Behavior Profile subsystem without repeated evidence of a real gap.
- [SessionHarbor](https://github.com/WangPeterXF/session-harbor) — local-first Codex session backup/restore and cross-device continuity with preview/read-only onboarding, verified identity/read-back, explicit dry-run versus apply, and separate backup versus destructive cleanup operations. It is a safety and onboarding comparator. Research question: can U-GAS first contact/bootstrap become clearer while preserving the current human-first/action-first model without teaching internal mechanics? Do not adopt session backup, vault/NAS, cross-device storage, hashing infrastructure, or its architecture merely because the discipline is useful.
- [Remedy](https://github.com/AhmiDarrow/RemedyAI) — a broader local AI partner/runtime with continuity under `~/.remedy`, user-provided cloud/local models, computer/browser capabilities, and human stops around money, passwords, submit/send, and delete. This is another independent signal for local continuity and explicit trust boundaries. Research question: do future U-GAS external failures justify a tighter capability/trust gate than current human-boundary and verification rules? Do not turn U-GAS into a persistent AI runtime, desktop app, model host, computer-use agent, or tool orchestrator.

### Comparative positioning hypothesis (research map, not a uniqueness or market claim)

- Chat/context export tools -> context portability.
- Agent OS -> durable task/outcome continuity.
- Behavior Profiles -> explicit/testable agent conduct and scope.
- Terrarium -> reported progress versus observed worktree/disk change.
- SessionHarbor -> verified session continuity/backup across devices.
- arka.norn -> stronger execution governance/enforcement.
- Remedy -> broader persistent local-agent runtime.
- U-GAS -> currently exploring a lightweight repository/project-native continuity, authority, scope, handoff, and verification layer without requiring a new agent runtime.

The repeated independent appearance of context loss, scope expansion, stale or ambiguous state, weak completion claims, and capability/trust boundaries is evidence that this problem family merits continued research. It is not evidence that U-GAS is unique, superior, independently validated, or should expand scope now.

## 2026-08-28 — Briefboard comparative research (PARKED)

Primary source: https://github.com/shinKatana0/briefboard

This is external comparative research only. It is not U-GAS authority, validation, a dependency, backlog, or accepted product scope.

- Briefboard is a lightweight kanban + CLI that governs a coding-task lifecycle through `backlog -> open -> ready -> in_progress -> review -> done`.
- Markdown backlog/tasks and briefs are authoritative rather than relying on chat structure alone.
- Useful comparator signals: distinguish declared task state from mechanically observed Git/session state; make external or waiting dependencies first-class; use consequence-based human gates rather than confirming every reversible action; and distinguish designed behavior, actually-tested behavior, and independently-validated proof.
- Product boundary: Briefboard governs coding-task lifecycle; U-GAS explores durable project continuity and authority across chats, agents, and execution environments.
- Do not adopt Briefboard's kanban/task board, orchestrator/worker roles, worktree-per-task flow, server/dashboard, or mandatory briefs into U-GAS from this research alone.
