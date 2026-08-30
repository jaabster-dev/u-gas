# U-GAS Session Continuity

`CURRENT_STATE.md` is compact resume authority. `PROGRESS.md` is chronological history and evidence. `IDEAS.md` is unaccepted possibility space. `README.md` is navigation, not a second state or policy authority.

A live obligation is not safely captured for resume merely because it appears in `PROGRESS.md`. If a newly discovered unresolved issue, blocker, pending verification, accepted follow-up, hardening case, risk or dependency, or open handoff can change what a future agent should do next, keep it represented in `CURRENT_STATE.md` or the repository's current-state/continuity surface until it is resolved, explicitly deferred or paused with its return condition, explicitly dropped or rejected, or otherwise transitioned out of live work. `PROGRESS.md` may preserve discovery, evidence, and decision history, but it must not be the sole location of such unresolved work.

Follow `RESUME ACTION -> RECONCILE -> VERIFY -> PROJECT NEXT`.

## Resume and reconciliation

On resume, read current repository authority and reconstruct `ACTIVE`, `WAITING/PAUSED`, concrete `PROJECT NEXT`, material `AFTER` ordering, `OPEN HANDOFFS`, `BLOCKER/BOUNDARY`, and any interrupt/return target. `RESUME ACTION` is the immediate safe recovery work; `PROJECT NEXT` is the action after reconciliation and verification. The newest `PROGRESS.md` entry does not silently override intentional current state, and waiting must not manufacture work.

When relative dates could affect reconciliation, establish the actual current local date/time on a cold or successor resume before interpreting today, yesterday, tomorrow, tonight, or next week. Repository/filesystem facts win for repository facts. Newer compatible explicit owner intent remains live until contradicted or durably persisted. If a side task interrupts active work, preserve its return target and unwind nested interruptions when the side task is complete or waiting unless invalidated or reprioritized.

## Durable checkpoint and degraded-session contract

When asked to save where work stopped, conversational summary is not enough. A checkpoint is saved only after the canonical continuity file is actually written and fresh authoritative read-back verifies it. If persistence is unavailable, use safe capability discovery and an authorized execution-capable persistence fallback; do not simulate a save or ask the owner to reconstruct branch/SHA mechanics.

If recent facts are repeatedly lost or current repository authority cannot be established after bounded recovery, stop substantive work, preserve the smallest material stale-session checkpoint, and let a fresh successor bootstrap from current repository authority. The old session is supporting history, not authority; do not claim `SUCCESSOR READY` before safe verified continuity. Any transferable handoff must be one complete copyable payload.
