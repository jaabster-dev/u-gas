# U-GAS Session Continuity

`CURRENT_STATE.md` is compact resume authority. `PROGRESS.md` is chronological history and evidence. `IDEAS.md` is unaccepted possibility space. `README.md` is navigation, not a second state or policy authority.

A live obligation is not safely captured for resume merely because it appears in `PROGRESS.md`. If a newly discovered unresolved issue, blocker, pending verification, accepted follow-up, hardening case, risk or dependency, or open handoff can change what a future agent should do next, keep it represented in `CURRENT_STATE.md` or the repository's current-state/continuity surface until it is resolved, explicitly deferred or paused with its return condition, explicitly dropped or rejected, or otherwise transitioned out of live work. `PROGRESS.md` may preserve discovery, evidence, and decision history, but it must not be the sole location of such unresolved work.

Follow `RESUME ACTION -> RECONCILE -> VERIFY -> PROJECT NEXT`.

Cold/successor/resume work must reconcile durable authority before continuation. Ordinary active-session follow-ups do not mechanically cold-bootstrap when the current conversation already supplies the needed context and no repository fact, mutation, handoff, or evidence depends on a fresh read.

## Resume and reconciliation

On resume, read current repository authority and reconstruct `ACTIVE`, `WAITING/PAUSED`, concrete `PROJECT NEXT`, material `AFTER` ordering, `OPEN HANDOFFS`, `BLOCKER/BOUNDARY`, and any interrupt/return target. `RESUME ACTION` is the immediate safe recovery work; `PROJECT NEXT` is the action after reconciliation and verification. The newest `PROGRESS.md` entry does not silently override intentional current state, and waiting must not manufacture work.

When relative dates could affect reconciliation, establish the actual current local date/time on a cold or successor resume before interpreting today, yesterday, tomorrow, tonight, or next week. Repository/filesystem facts win for repository facts. Newer compatible explicit owner intent remains live until contradicted or durably persisted. If a side task interrupts active work, preserve its return target and unwind nested interruptions when the side task is complete or waiting unless invalidated or reprioritized.

## Current-state lifecycle hygiene

Keep `CURRENT_STATE.md` small enough to be a reliable live resume surface. When resolved material becomes history rather than a live constraint, preserve its evidence in `PROGRESS.md` or an existing archive and remove only the stale resume detail from current state. Cleanup is evidence-triggered, not periodic ceremony: preserve provenance, paused/deferred return conditions, open handoffs, blockers, and accepted constraints. Never reconstruct current state from a partial or truncated history read; use targeted reads/searches and the large-file safety route when history is large.

## Reusable operational knowledge

When a stable capability limitation, disproven route, or verified workaround is likely to recur and is not obvious from current code/configuration, preserve it in the smallest existing target authority/continuity surface with its environment/condition and re-test trigger. A later agent should reuse the known procedure before rediscovering the same dead path. Do not create a separate lessons store when an existing surface owns the fact.

## Machine handoff / execution-continuity gate

Explicit intent to stop on one physical computer and continue on another triggers a stricter check than an ordinary session checkpoint. Repository state alone is not proof that the target machine can perform the next action.

Use four layers when reasoning about readiness: project state, repository state, execution environment, and machine-local/device state. Start from the concrete next action and inspect only known relevant sources such as `CURRENT_STATE.md`, release/checkpoint/manifests, executor output, known candidate paths or hashes, intentional Git exclusions, and required tool/service/device state. Do not perform a blind disk inventory.

Classify each relevant non-conversational dependency as `PORTABLE / REPO-BACKED`, `PORTABLE / CLOUD-SHARED-BACKED`, `LOCAL-ONLY / RECREATABLE`, `LOCAL-ONLY / IMMUTABLE`, `MACHINE-BOUND`, `DEVICE-BOUND`, or `EXTERNAL-SERVICE STATE`. Classification is semantic, not extension-based. Qualified exact release bytes are `LOCAL-ONLY / IMMUTABLE` when rebuilding would create a different candidate.

Keep a minimal live dependency record in the project's existing current-state/continuity surface only while it matters: purpose or stable identifier, authority/hash when known, source location/environment, portability class, action requiring it, target-accessibility verification, and expiry/re-test condition. Do not create a permanent artifact catalog merely for handoff.

Prove readiness as `CURRENT NEXT ACTION -> required execution dependencies -> target-environment accessibility/authority`. `MACHINE HANDOFF: PASS` requires current repository authority to be target-accessible; every relevant non-repo dependency to be accounted for; required immutable authority to be target-accessible with destination identity verified when available; required execution, machine, device, and external-service dependencies to be available or irrelevant; and no known blocker hidden behind words such as saved, checkpointed, or pushed. A known required dependency that is not target-accessible means `PARTIAL` or `BLOCKED`, with the exact pre-switch action stated.

For `LOCAL-ONLY / IMMUTABLE`, copy exact bytes rather than rebuilding and verify the destination hash when a qualified hash exists. Routine non-sensitive copy/checksum work to an already approved target/shared location may be agent-owned. Never invent a shared destination or upload secrets, credentials, private keys, certificates, signing material, or keychain contents to generic cloud storage. If only verified repo/cloud-backed dependencies are required, keep the audit short and do not create a manifest/checklist ritual.

## Durable checkpoint and degraded-session contract

When asked to save where work stopped, conversational summary is not enough. A checkpoint is saved only after the canonical continuity file is actually written and fresh authoritative read-back verifies it. If persistence is unavailable, use safe capability discovery and an authorized execution-capable persistence fallback; do not simulate a save or ask the owner to reconstruct branch/SHA mechanics.

If recent facts are repeatedly lost or current repository authority cannot be established after bounded recovery, stop substantive work, preserve the smallest material stale-session checkpoint, and let a fresh successor bootstrap from current repository authority. The old session is supporting history, not authority; do not claim `SUCCESSOR READY` before safe verified continuity. Any transferable handoff must be one complete copyable payload.
