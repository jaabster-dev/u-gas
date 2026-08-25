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
