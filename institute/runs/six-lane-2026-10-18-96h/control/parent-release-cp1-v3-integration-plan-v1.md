# Parent release CP1 caller v3 — source-only integration plan v1 (PLAN ONLY, NOEXEC)

Actual `/bin/date` before this write: `2026-10-19T17:46:26-0700`.

This is a plan for exactly ONE caller successor, `RUN/control/parent_release_caller_v3.py`. **No successor source has been written.** CP1 v2 `9f3d158bd80a31d6ce2d964e216244d5095eb9422782bc448dc3a671d81e4cb4` and v1 `4072c50ef5be021a22e72a43571550c1338ab8a4d243752d88e3b7cc71a75cae` stay immutable. It follows Main's IRC (~17:40): "Keep CP1 v2 immutable; prepare one new caller successor only after BOTH interfaces frozen. No runtime/import/tests. First send a source-only integration plan before writing to avoid pin churn."

**No import, compile, AST, exec, test, probe or model CLI** was used; only reading, `shasum`/`wc`, IRC and this exclusive write. Global HOLD is unchanged.

## Inputs (re-hashed 2026-10-19T17:39:34-0700 unless stated)

| Object | SHA256 | Use |
|---|---|---|
| `control/parent_release_v4.py` | `4c4a84f07047fa7499d4cc4bdc8ea29230614f760b2f7cf6fc42e85b16963b59` (83137 bytes, 1755 lines) | PRT successor; source-only, review pending |
| `review/parent_release_v3_to_v4.diff` | `925dc38e9fe8495b5d48f182e8d6b05132e15becb94738e967f6072689580114` (274 lines) | Read in full; basis of §2 |
| `control/parent-release-v4-design-notes.md` | `e29e719a7e7dba664ae9f63ce1b48c33ca34e55a3c29b31768da14d63325fc87` | Vocabulary and attachment rules; T109–T121 |
| `review/parent-release-checkpoint-008-v1.json` | `e4332ef0fa85f5d3ef9e855b18a687b639bd1f1fa0906d2a5438c08e340d0213` | `interface_changes_for_CP1` |
| `control/written-slot-transitions-olson-beta-prt-20261019-1708-v1.json` | `32d161b0408bc297f0e95516980142d741eb219dc882e40bd93df9c79cd59f12` | PRT v4 repair scope (key `prt_v4`) = third `repair_scope_sha256s` entry |
| `review/parent-release-v3-codex-v2.prompt.stdout.txt` | `bf110a0785589ee182a8d348b98ca345ca84dd214fbf16a906f076c38d3e2777` | Codex HOLD on PRT v3: 0 FATAL / 3 MAJOR / 2 MINOR |
| `control/parent_release_v3.py` | `161ae04ce4ee98db76bb5b9b983cdfa13c769733b10159ebb5d31b5e377bd23a` | Pinned by CP1 v1/v2; now HOLD |
| `control/parent_release_identity_v3.py` | `f21b4296ae52778fe31677f749a871d8982c31c6d5133609dc1d0b0e0fe58b38` | Current CP2 pin in CP1 v2; CP2 v4 pending |
| `review/parent-release-v4-codex-v1.prompt.stdout.txt` | 0 bytes when sized after 17:39:34 | v4 review not yet available |

## 0. Immediate consequence for CP1 v1/v2

CP1 v1 and v2 load only PRT v3 `161ae04c…`, which now has a Codex HOLD. The caller source has no knowledge of review verdicts, so if invoked it would execute those HOLD bytes. **Do not invoke CP1 v1 or v2 for any transaction, and do not issue any of the seven CP1 attestations for one.** In practice this is already fail-closed: none of the attestations exist, so every invocation is HELD before PRT runs.

## 1. Sequencing (to avoid pin churn)

- **G1 PRT:** the CP1 v3 PRT pin is frozen only after the parent's verdict on PRT v4. On HOLD, wait for the successor's freeze; §2 values change, but no logic does.
- **G2 CP2:** CP2 v4 source and interface are frozen and pinned by its owner (§3).
- **G3 Parent:** an authorization naming the CP1 v3 write scope and answering D1–D6 (§5).

After G1–G3:
1. Freeze an exact-once replacement list against CP1 v2 bytes `9f3d158b…` in a new CP1 checkpoint.
2. Create, all mode `x`:
   - `control/parent_release_caller_v3.py`
   - `review/parent-release-cp1-caller-v2-to-v3.diff` (difflib, n=3)
   - `control/parent-release-cp1-design-notes-v3.md`
   - `review/parent-release-cp1-source-disposition-v3.json`
   - a final checkpoint
3. Park.

If a pin changes after step 1, a new list is frozen in a new checkpoint. A frozen list or a written source is never edited.

## 2. PRT v4 deltas (known now; provisional on G1)

| CP1 v2 site | v2 value | v3 value | Basis in v4 |
|---|---|---|---|
| PRT path (`PRT3_PATH`, l.42) | `…/control/parent_release_v3.py` | `…/control/parent_release_v4.py` | — |
| PRT sha (l.43) | `161ae04c…` | `4c4a84f07047fa7499d4cc4bdc8ea29230614f760b2f7cf6fc42e85b16963b59` | shasum |
| PRT bytes (l.44) | 81235 | 83137 | wc |
| `FORBIDDEN_PRT_SHA256` (l.45–47) | {v1 `6bc92891…`, v2 `addcdf4c…`} | add v3 `161ae04c…` (Codex HOLD 3M/2m) | — |
| `PRT_MODULE` (l.48) | `parent_release_v3.py` | `parent_release_v4.py` | l.1354, 1541 |
| `PRT_REPAIR_SCOPES` (l.50–51) | [`2fdf13b4…`, `1f9befdb…`] | append `32d161b0408bc297f0e95516980142d741eb219dc882e40bd93df9c79cd59f12` | l.26, 1356 |
| `RESULT_FORMAT` (l.57) | `parent-release-result-v3` | `parent-release-result-v4` | l.1578 |
| `DISPOSITION_FORMAT` (l.58) | `…-disposition-v3` | `parent-release-disposition-v4` | l.1354 |
| `REGISTRY_FORMAT` (l.59) | `…-registry-v3` | `parent-release-registry-v4` (owner = `PRT_MODULE`) | l.1541 |
| `DISPOSITION_PREFIX` (l.60) | `prt-v3-` | `prt-v4-` | l.1489 |
| `ACK_STATES` (l.87) | 4 values | add `ACK_ATTEMPTED` | l.1451 |

**Why `ACK_STATES` is required.** PRT v4 T115/T116 attach results with `ack:'ACK_ATTEMPTED'`. Without the new value, CP1's shape check (`_result_shape`, l.782) refuses such a result and records "malformed … resource state unknown". The attached v4 report and its resource counts are then lost, and a spurious permanent in-process block is added. Registry status `ATTEMPTED` needs no change: CP1 does not restrict the status vocabulary, and release requires `APPENDED`.

**Unchanged, verified from the diff:**
- the entry signature;
- the 22 result keys, the 10 disposition-result keys, the 7 registry-result keys plus optional `path`/`detail`, and the resources keys;
- the `final_deadline_check` vocabulary;
- the 13 registry-row keys and the line-SHA rule (LF excluded);
- the spec, `parent-release-wait-v1` and `parent-release-late-baseline-v2` schemas;
- effective release = `state:'RELEASED'` and `final_deadline_check:'PASSED'`.

**Exceptions.** v4 attaches `parent_release_result` and the new `parent_release_prior_exceptions` (tuple, oldest first), and propagates the newest BaseException. CP1 already re-raises the identical object, so both attributes survive unchanged. S3 below additionally records the prior tuple in CP1's own HELD outcome.

**Availability notes.**
- v4 `_held_for` counts only v4 HELD rows, so an allocation that ever received a v3 row cannot be released through v4. PRT notes state that no v3 row exists, because v3 never ran.
- The pinned reader allows 1024 `read_bytes`/`directory_names` calls per instance (`beta_parent_reader_v1.py` `MAX_CALLS`). PRT, CP1 and possibly CP2 share that one original reader per transaction. Roughly 13 CP1 reads, about 15 fixed PRT reads, and one read per job artifact must fit, so a job with about 1000 artifacts is HELD.

## 3. CP2 v4 (pending G2)

CP1's complete CP2 dependency surface (v2 lines) was sent to ParentIdentityCP2 by IRC at ~17:45:
1. `identity` is exactly `{union, census_log, evaluate_endedness}` (644–647).
2. The union is bounded JSON: at most 4 MiB, 131072 nodes and depth 256, with exact types, finite floats and no shared containers. `module`, `design_freeze_sha256`, `scheme` and `producer_sha256` must be exact strings, checked before any status read (`CP2_UNION_VERSION` 52–56; `_union_version` 705–718; `_union` 720–733). It also needs `format` `parent-release-identity-union-v1`, `state` `CLOSED_CONDITIONAL`, a hex `union_sha256`, and `prt_identities` typed-equal to `spec.identities` (726–731).
3. `census_log.served_count()` is a zero-argument exact int and must rise by exactly +1 across the PRT call (698–702, 867–869).
4. `evaluate_endedness(detached union copy, census_log, deadline_check)` never raises Exception. Its result is bounded JSON with `format` `parent-release-identity-endedness-v1`, `state` `ENDED_CONDITIONAL`, `causes` [], a hex `endedness_sha256` and a `union_sha256` echo (857–873).
5. `census` is passed unchanged to PRT, with PRT's census schema.

**Rule:**
- If the surface is unchanged, the CP2 change is value-only: `CP2_UNION_VERSION` plus the recorded CP2 source sha in docstring and comments.
- Every changed name, signature, format, key or state value becomes an explicit entry in the frozen replacement list.
- Nothing CP2-related is frozen before the owner's v4 pin (source sha, design-freeze sha, module, scheme, producer, API).

## 4. Self-identified CP1 v2 defects to repair in v3 (same classes as the Codex HOLD on PRT v3)

- **S1 (class of Codex M3: progress understated after a late or interrupted completion).**
  - **Where:**
    - `_write_receipt` (1005–1049) sets `created` (1015), `identity` (1019), `bytes_written`/`complete` (1027–1028), `file_fsync` (1030), `readback` (1043) and `directory_fsync` (1047) only after `_Call.native` passes its completion check.
    - `_load_prt` sets `prt.loaded` (747) only after the definitions completion check.
  - **Effect:** a crossing at that check, or a BaseException from it, leaves the flag false or zero although the operation completed. The HELD outcome then under-reports that a receipt was created, written or fsynced.
  - **Fix:** record each through the existing `retain` hook BEFORE the completion check, as PRT v4 does with `_mark` and its progress hooks. False then means "not proven", never "not performed". No schema change. The receipt ACK already latches `ACK_ATTEMPTED` before I/O (1054).
- **S2 (class of Codex M2: a later BaseException object is dropped).**
  - **Where:** `_Call.release` (480–493) re-raises the FIRST close BaseException and drops later ones. Only their evidence strings survive, in events, unresolved and the ledger. Its docstring "later ones keep context" is inaccurate.
  - **Fix:** adopt the PRT v4 rule.
    - Every BaseException object CP1 observes is retained in order.
    - Every owned handle still gets exactly one close attempt.
    - The NEWEST BaseException propagates. It carries `parent_release_caller_outcome` (HELD) and the new `parent_release_caller_prior_exceptions` (tuple, oldest first, excluding the propagating one), attached best-effort.
    - `__context__` is linked only when the slot is free and the link is acyclic (bounded walk).
    - PRT's own `parent_release_prior_exceptions` is never touched.
- **S3 (evidence completeness).** When PRT raises a BaseException, the HELD outcome's `prt` block records the count and **type names only** of `parent_release_prior_exceptions`. Type names only, so no user `__str__` runs.
- **Checked and not present in CP1: the class of Codex M1.** CP1 writes nothing after any BaseException, and passes `commit_dir` to PRT only after the job_dir exclusion (`_spec`) passed.

## 5. Decisions requested (yes/no each; unanswered = no)

| ID | Proposal | Effect | Recommendation |
|---|---|---|---|
| D1 | Bind `union.item == owner.item` (cause `CP1_IDENTITY_UNION`) | Closes SF2; CP2 rates it MINOR | YES |
| D2 | Endedness `module` (and any version fields CP2 v4 adds) equal the pinned CP2 values (cause `CP1_ENDEDNESS`) | Closes V14, accidental evaluator mixing | YES |
| D3 | Fresh census pair: `served_before == 0` | Availability and diagnostics only | NO |
| D4 | `identity_union_census_cp2` attestation must carry `cp2_source_sha256 ==` the pinned CP2 sha (cause `CP1_PREREQUISITE_MISSING`) | Guards parent-side version mix-ups; still not an origin proof | YES |
| D5 | Option B: CP1 executes verified CP2 bytes itself, builds the union and a fresh census pair | Binds code identity (closes V13, V14 and the SF1 residual), but changes the owner interface and runs CP2's native libproc census inside CP1 | NO for v3, unless the parent wants code identity now; must be decided before G3 |
| D6 | Version-neutral identifiers: `PRT3_*` → `PRT_*`; `'prt3'` labels and "PRT3" messages → PRT; neutral exec namespace name | One-time diff of about 30 more mechanical lines; later PRT re-pins become value-only | YES |

**Consequences:**
- If S2 or S3 is adopted, `OUTCOME_FORMAT` becomes `parent-release-caller-outcome-v2` (new outcome fields).
- The receipt schema and `RECEIPT_FORMAT` are unchanged. Receipts bind `module`, so the v3 consumer accepts only v3 receipts.
- `ReservationAccount` is unchanged.
- No new causes: D1 uses `CP1_IDENTITY_UNION`, D2 uses `CP1_ENDEDNESS` and D4 uses `CP1_PREREQUISITE_MISSING`.

## 6. Unchanged in v3

Everything not listed above stays as in v2:
- `invoke_release(owner, spec, reader, census, owned_date, deadline_check, identity)`, unless D5;
- owner keys and the seven named prerequisites;
- the S0–S16 sequence and every original-deadline rule;
- the global ledger and resource join;
- the receipt protocol and the consumer;
- caps, causes, and the caller-side union version check.

## 7. Expectations to freeze with the v3 source (NOT exercised)

| ID | Case | Expected |
|---|---|---|
| W01 | PRT T115 (ACK `read_bytes` KeyboardInterrupt; attached `ack:'ACK_ATTEMPTED'`) | The identical KeyboardInterrupt re-raised with a HELD outcome (`CP1_PRT_BASE_EXCEPTION`). The attached v4 report is retained as `result_document`. No "malformed" ledger record |
| W02 | PRT T117 (registry fsync KeyboardInterrupt after a complete RELEASED line; status `ATTEMPTED`) | As W01, plus outcome uncertainty that the RELEASED bytes are not authority |
| W03 | PRT T112 (SystemExit propagates; prior KeyboardInterrupt) | The identical SystemExit re-raised. Its `parent_release_prior_exceptions` is untouched. The outcome records prior count 1 and type `KeyboardInterrupt`; `parent_release_caller_prior_exceptions == ()` |
| W04 | v3 bytes `161ae04c…` at the v4 path | H(`CP1_PRT_SOURCE`); nothing executed |
| W05 | Receipt exclusive create completes, then its completion check crosses | H(`CP1_DEADLINE_RECEIPT`); `created:true`; fd closed once |
| W06 | Full receipt write completes, then its completion check crosses | `bytes_written` = length; `complete:true` |
| W07 | Receipt fsync completes, then its completion check raises KeyboardInterrupt | `file_fsync:true`; KeyboardInterrupt propagates with the HELD outcome |
| W08 | PRT definitions exec completes, then its completion check crosses | `prt.loaded:true`; PRT not invoked |
| W09 | Two receipt-cleanup closes raise KeyboardInterrupt, then SystemExit | SystemExit propagates; earlier BaseExceptions in `parent_release_caller_prior_exceptions`, oldest first; each handle closed once |
| W10–W12 | D1/D2/D4 mismatches, if adopted | H(`CP1_IDENTITY_UNION`) / H(`CP1_ENDEDNESS`) / H(`CP1_PREREQUISITE_MISSING`) |

## 8. Boundaries (unchanged)

- Native calls and callbacks can stall; there is no hard-real-time guarantee.
- In-process forgery, module reload or restart is outside what the source can prevent.
- `exec` of verified PRT bytes trusts the interpreter.
- Hashes and self-reported version fields authenticate selected bytes or claims, never origin.
- An omitted historical identity is undetectable here, and CP2 results are conditional.
