# Ideas

## Optional associative-memory layer / memory != authority

Hindsight and [AgentMemory](https://github.com/M-T-D-N/agentmemory-codex-windows) are external examples of persistent or associative memory as a layer separate from U-GAS governance and authority. Hindsight's retain/recall/reflect model and AgentMemory's runtime hooks, provenance, exact-project-scoped writes, and bounded cross-project recall suggest useful ways to find older decisions, lessons learned, preferences, and related history. They do not make recalled memory the project's current truth.

U-GAS should not become its own vector database or graph-memory system merely because these tools exist. A possible future combination would be:

1. U-GAS bootstrap establishes repository identity, branch, and current durable truth.
2. An optional memory layer performs recall.
3. Retrieved memory is reconciled against current Git, PICA, and explicit owner intent.
4. Memory never expands write authority or overwrites newer durable state.
5. U-GAS safe-change and verification rules continue to govern execution.
6. Material current state remains in PICA/Git; memory may additionally retain reusable historical experience.

AgentMemory's exact-project-scoped writes and bounded cross-project recall are an interesting external design signal: recall scope and write scope are not the same thing.

This is not accepted scope. Hindsight, AgentMemory, and other memory integrations must not be implemented until real evidence shows that targeted PICA/Git/history retrieval creates a repeated problem that cannot be solved more simply. Any later evaluation must consider complexity, privacy, portability, maintenance, model/tool lock-in, and owner friction.

**Memory is useful. Memory is not authority.**

## Semantic coherence / make the right action the natural action

U-GAS may benefit from a design quality lens called **semantic coherence**. User intent, repository structure, PICA responsibilities, agent routing, authority, continuity, safe mutation, verification, automation, and human boundaries should carry compatible meanings. The human-visible system and the infrastructure/AI work system should not require two different mental models.

The goal is for the correct path to be inferable from state and meaning: the user states the result they want; the system determines repository, authority, and current state; that state implies the safe workflow; the AI handles routine Git and verification mechanics; and the user enters only at a real product or human boundary. A later agent should reconstruct the same durable meaning without a secret workflow, special command, competing authority file, or treating remembered context, `PROGRESS.md`, an idea, or a local clone as current truth by accident.

Possible evaluation principles:

1. One concept should have one stable meaning.
2. One durable responsibility should have one clear authoritative home where practical.
3. The obvious human action should map naturally to the safe infrastructure action.
4. Structure and naming should carry meaning instead of requiring memorized exceptions.
5. Normal workflows should guide the agent toward the correct procedure, not rely only on prose reminders.
6. Infrastructure detail should remain hidden when it does not require human judgement.
7. Unsafe, ambiguous, stale, or exceptional states should become explicit rather than silently guessed through.
8. The system should reduce procedural knowledge that the owner or agent must keep in working memory.

**The system should make the correct path the natural path.** This is a design/evaluation idea, not accepted governance. For any future rule, file, workflow, script, prompt, or status, ask whether it strengthens shared meaning, reduces translation burden, or adds another procedural layer someone must remember.

## Orchestration vs semantic infrastructure

An external multi-agent orchestrator experiment evolved from a human clipboard between Claude, Codex, and Cursor into dependency-aware planning, dispatch, queues, workers, leases, blockers, approval gates, verification, bounded repair, crash recovery, and audit trails while leaving commit/merge/release/deploy authority with a human. The relevant U-GAS question is not whether to build the same orchestrator.

Research hypothesis: durable authority, explicit current state, a deterministic-ish resume procedure, clear scope, verification, human boundaries, and semantically coherent handoffs may solve some coordination problems before a runtime orchestrator is necessary. An orchestrator automates the courier; U-GAS might reduce the need for a courier by making state and authority reconstructable. Do not pass the whole conversation forward when the required state can be reconstructed from authority.

Future research questions:

- **Duplicate execution / idempotency:** after interruption, how can the next process determine whether a side effect already happened, whether retry is safe, or whether work is complete? Re-read actual authority/state and verify; do not assume success. U-GAS does not currently solve distributed idempotency.
- **Independent verification:** two AI systems can confirm the same wrong solution. Tests, CI, runtime evidence, repository state, and explicit acceptance criteria are stronger evidence than another model saying yes.
- **Bounded repair:** how should retry/repair be bounded, and when must it escalate to human or authority reconciliation? This does not authorize a new retry system.
- **Long-chain context integrity:** how can plan, scope, and invariants survive handoffs without bloating context or silently losing one constraint? The hypothesis is to pass durable authority plus a minimum resume contract, not the whole chat history.

This is comparative research, not authorization to build an orchestrator. U-GAS should not become a “small unreliable Kubernetes for overconfident agents.”

## Parallel-agent semantic isolation / work ownership

Parallel-agent work has at least three different isolation layers:

1. **Source isolation:** Git branches, worktrees, or separate clones.
2. **Runtime isolation:** separate ports, databases, Docker Compose project names, fixtures, seed data, or per-worktree environments.
3. **Semantic/planning isolation:** which agent owns a work intent, module, schema, or domain, and how others discover assumptions already being changed.

A clean Git merge is not evidence of semantically valid integration. Agents can change different files, pass branch-local tests, and merge without textual conflict while making incompatible assumptions about one data model, API, schema, or domain. The serious collisions may occur in planning rather than in code.

Potential lightweight research:

- **Work/intent claiming:** an agent could declare its current work and scope atomically so other agents discover it before overlapping work. First test whether Git, PICA, a specification, or `CURRENT_STATE.md` can provide this more simply; a central task board is not assumed.
- **Semantic ownership boundaries:** where practical, divide parallel work by module, feature, schema, domain, service, or another semantic boundary, not only by file.
- **Integration-level verification:** verification may need evidence after integration, not just branch-local tests and a clean merge.
- **Runtime isolation as separate engineering:** use standard Git, CI, Docker, or devcontainer mechanisms where they already solve runtime isolation. Do not reinvent the wheel; U-GAS value should remain primarily above those mechanisms: authority, intent, continuity, ownership/coordination, safe mutation, verification, and human boundaries.

This is not authorization to create a global task board, worker manager, lock server, lease service, port allocator, Docker orchestrator, or multi-agent dispatcher. Require real U-GAS evidence before adding such machinery.
