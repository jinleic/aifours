# Parent release CP2 — source v2 minimal repair (sticky unknown incarnations) — NOEXEC

Actual `/bin/date` before this write: `2026-10-19T17:01:06-0700`.

| Artifact | Path | SHA-256 |
|---|---|---|
| v2 source | `RUN/control/parent_release_identity_v2.py` (1593 lines, 84818 bytes, ASCII) | `7b2bc4021744aa6fa55677fa4953c9efc1088f53d341fb0ba339621abdddc3ec` |
| exact v1→v2 diff | `RUN/review/parent_release_identity_v1_to_v2.diff` | `ea20bf0283a100f3ef5e98ef1ad44d1a48a177e77344190e4c0e83a7e4dbaf05` |
| v2 delta freeze (before code) | `RUN/control/parent-release-cp2-design-freeze-v2.json` | `7f46b7e5f5581a6e905efa8405381208c9481332b26ba2e2a84f1ace436a1c28` |
| v2 controls matrix | `RUN/review/parent-release-cp2-controls-v2.json` | `3bcbc7476346b25bd7cc975a39a5510543cbc5b87089e3d86045c31988414758` |
| repair scope (parent) | `RUN/control/parent-release-cp2-v2-repair-scope-v1.json` | `afe35832c808cf3d6a482fb6549dc8957d57ae982b7e48e76dba5b5374bcfa98` |
| v1 source (immutable HOLD) | `RUN/control/parent_release_identity_v1.py` | `d07548e2dbff4ef6b64a3a902d3b59ed7c4abbf8dc2115e8b08ed37ee2ec14d5` |
| v1 notes (unchanged sections still apply) | `RUN/control/parent-release-cp2-design-notes-v1.md` | `688871953a2ccb33f9241f95c277ef3eaed75bd79bd5656d6a060777d71a5269` |

**Status: NOEXEC source candidate, unqualified, not self-approved.** No import, compile, AST parse, test, fixture, census or other execution. v2 bytes were produced mechanically from v1 by the nine frozen exact-once text replacements in the v2 freeze (placeholder → freeze digest); the diff above is their complete effect. No old file was mutated.

## Delta (the only behavioral change)

New cause `U_UNKNOWN_INCARNATION`, ordered after `U_SPAWN_CHRONOLOGY`. `_analyze` calls `_sticky(recon, pending)` immediately after reconciliation, completeness and pending-row extraction, **before** the event tape, so tape/baseline/owned/unproved failures cannot hide it. `_sticky` enumerates defensively from the raw reconciliation, independent of every other validation:

- each pending raw acquisition row and history-overflow completed observation (`_pending`);
- **every** `coverage_history` entry (sv19 identification gap pid, including parent-edge and measurement gaps);
- **every** helper report whose `identity` is null;
- `main_wait` present with `main_identity` null.

Each record fires `U_UNKNOWN_INCARNATION` once (≤16 evidence strings, the rest counted in `suppressed`, so the exact count is retained). A coverage/helper structure that cannot be enumerated fires it too ("unknowns cannot be excluded"). Histories with no reconciliation (capture/line/producer failures) already HOLD and expose nothing to enumerate. Unknown rows stay in `unknown_incarnations`, never receive fingerprints, and their history closure is `OPEN_HELD`.

**Non-waiver:** the union becomes HELD, so `evaluate_endedness` fires `E_UNION_HELD` whatever the served census shows; H7 closure, a complete current census, parent ENDED/ENDED_PROVED or CP1 cannot clear a sticky unknown. This matches the beta bridge's sticky-history rule (BetaFiniteControls) without merging its formats.

## Unchanged

Formats (`parent-release-identity-request-v1`, `-union-v1`, `-endedness-v1`), every public name/signature, `CensusLog.served_count()`, union keys `format/state/union_sha256/prt_identities`, endedness keys `format/state/causes/endedness_sha256/union_sha256`, census callback, start-fingerprint scheme, H7 and all other checks, coverage map and boundaries of v1 notes §1-§8 and §10. Report `module` is now `parent_release_identity_v2.py` and `design_freeze_sha256` is the v2 freeze. CP1 caller `parent_release_caller_v1.py` `4072c50e…` needs only the new source pin.

## Findings after v2

- SR-1 MAJOR: **repaired in v2 source** (unexercised).
- SR-4 MINOR (dependent `U_ROW_CONFLICT` when member assembly was blocked) and SR-5 MINOR (no structured request binding in the union report; consumed paths/digests only in the bounded callback log): **unrepaired**, outside the minimal scope.
- SR-2 residual (exact re-serialization assumes no int-keyed sv19 dicts) and SR-3 note (endedness covers every served snapshot; fresh `make_census` per transaction) unchanged.

## Availability consequence (stronger than v1, not weakened)

sv19 records every listed-but-unidentifiable pid (typically a process exiting between listing and identification) as a coverage gap. Under v2 any such gap anywhere in a run's history makes the union HELD, in addition to v1's requirement that the last census show no post-baseline live process on the host. A release-eligible history therefore needs a quiescent host for the whole run. Expected practical outcome on a busy shared host: HELD.

## Controls

`review/parent-release-cp2-controls-v2.json` supersedes v1 expectations for v2: C18 → [U_HISTORY_INCOMPLETE, U_UNKNOWN_INCARNATION]; C34 → [U_UNKNOWN_INCARNATION]; new C45 (one coverage gap) [U_UNKNOWN_INCARNATION]; C46 (ACK, identity-less main spawn) [U_UNKNOWN_INCARNATION]; C47 (tape inconsistent + gap) [U_EVENT_TAPE_INCONSISTENT, U_UNKNOWN_INCARNATION, U_ROW_CONFLICT]; C48 (malformed coverage entry) [U_HISTORY_SCHEMA, U_UNKNOWN_INCARNATION]; E11 (union HELD only by sticky unknown, clean census) [E_UNION_HELD]. Base fixture must contain no gap, identity-less spawn, pending raw or overflow observation. All expectations frozen, none exercised; synthetic fixtures prove predicates only.

## Remaining prerequisites (unchanged from v1 §10)

Parent launch/wait records in `sv19-incarnation-v1`; complete outer stdout capture; oracle under owned_supervisor_v19; continuation history or closing rerun for open histories; sv19 package/finite qualification; parent observation authenticity, direct launch in own groups, publication freeze, non-descendant channel residual; CP1 join; independent parent source review and separate finite qualification.
