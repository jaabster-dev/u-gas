# U-GAS Session Continuity

`CURRENT_STATE.md` is compact resume authority. `PROGRESS.md` is chronological history/evidence. `IDEAS.md` is unaccepted possibility space. The newest history entry does not silently override explicit current state.

Follow `RESUME ACTION -> RECONCILE -> VERIFY -> PROJECT NEXT`.

## Two-layer active state

`CURRENT_STATE.md` should expose `ACTIVE`, `NEXT`, `WAITING/PAUSED`, `BLOCKER/BOUNDARY`, open handoffs, and an interrupt/return point when relevant. `PROGRESS.md` records history; its newest entry is not automatically current priority.

On resume, reconstruct `ACTIVE`, `WAITING/PAUSED`, concrete `PROJECT NEXT`, material `AFTER`, blockers/boundaries, and open handoffs without reading giant history by default.

Recent compatible owner intent may be newer than durable state. Do not discard it merely because Git was read later: repository state wins for repo facts, while newer explicit user decisions remain live until contradicted or persisted.

If a side task interrupts active work, preserve its return target and resume it when the side task is done or waiting unless invalidated or reprioritized.

## Durable checkpoints and degraded sessions

When asked to save where work stopped, conversational summary is not enough. Say saved only after the canonical continuity write completes and a fresh authoritative read verifies it. If writing is unavailable, report save incomplete and use an execution fallback.

If a session repeatedly loses recent facts or cannot establish current repo authority after bounded recovery, stop substantive repo work, preserve the smallest material continuity, and let a fresh successor bootstrap from repository authority. The old conversation is supporting history, not repo authority.

## Active Work State and reconciliation

`RESUME ACTION` is the immediate safe recovery work; `PROJECT NEXT` is the next action after reconciliation and verification. Reconstruct `ACTIVE`, `WAITING/PAUSED`, `PROJECT NEXT`, material `AFTER` ordering, `OPEN HANDOFFS`, `BLOCKER/BOUNDARY`, and any interrupt/return point. Resolve temporal grounding when relative dates matter, then resolve the authoritative branch/current repository state. The newest `PROGRESS.md` entry is not automatically current priority; an intentionally waiting state should not manufacture work.

Recent compatible owner intent may be newer than durable state and must not be discarded merely because Git was read later. Repository state wins for repository facts, while newer explicit owner decisions remain live until contradicted or persisted. Preserve a side-task return target and resume it when done/waiting unless invalidated or reprioritized; unwind nested interruptions where relevant.

## Checkpoint and stale-session contract

When asked to save where work stopped, conversation summary is not saved. Acknowledge a checkpoint only after the canonical write and a fresh authoritative read verify it. If writing is unavailable, use capability discovery and an execution-capable persistence fallback; do not ask the owner to reconstruct branch/SHA mechanics. If recent facts are repeatedly lost or authority cannot be established after bounded recovery, stop substantive work, preserve the smallest stale-session checkpoint, and require a fresh successor to bootstrap from current repository authority. The old session is supporting history, not authority; do not claim `SUCCESSOR READY` before safe verified continuity. A transferable handoff must be one complete copyable payload.
