# Parent release CP1 caller v3 — source-only integration plan v2 (PLAN ONLY, NOEXEC)

Actual `/bin/date` before this write: `2026-10-19T17:54:17-0700`.

This plan **supersedes plan v1** (`RUN/control/parent-release-cp1-v3-integration-plan-v1.md` `e38d047e39a4d794756b10fa8cb0b93ce87ae07463ccc5e8d024f5f82c33ebcb`), which stays immutable. It covers exactly ONE caller successor, `RUN/control/parent_release_caller_v3.py`. **No successor source has been written.** CP1 v2 `9f3d158bd80a31d6ce2d964e216244d5095eb9422782bc448dc3a671d81e4cb4` and v1 `4072c50ef5be021a22e72a43571550c1338ab8a4d243752d88e3b7cc71a75cae` stay immutable.

Two things are new since v1:
- ParentIdentityCP2 sent the CP2 v4 interface by IRC at ~17:50.
- The Codex review of PRT v4 completed with **HOLD 0 FATAL / 3 MAJOR / 2 MINOR**. Two of its MAJORs concern exactly the exception-handling rules CP1 v3 was going to copy.

**No import, compile, AST, exec, test, probe or model CLI** was used; only reading, `shasum`/`wc`, IRC and this exclusive write. Global HOLD is unchanged.

## Inputs (hashes read 17:50:59–17:54:17)

| Object | SHA256 | Status / use |
|---|---|---|
| `control/parent_release_v4.py` | `4c4a84f07047fa7499d4cc4bdc8ea29230614f760b2f7cf6fc42e85b16963b59` (83137 B, 1755 lines) | Codex HOLD; parent verdict pending; a PRT successor is expected |
| `review/parent-release-v4-codex-v1.prompt.stdout.txt` | `b38745818f96a032106eea3da675a40adf640d19c483c83dac64691f7228a8e8` (6486 B; receipt written 17:51) | HOLD 0F/3M/2m; M2 and M3 apply to CP1 (§4) |
| `review/parent_release_v3_to_v4.diff` | `925dc38e9fe8495b5d48f182e8d6b05132e15becb94738e967f6072689580114` | Read in full (plan v1) |
| `control/parent_release_identity_v4.py` | `39c51017a6f01fad779d40c22ad0912cde2d0384e4ed7e7baad2206bc8e93d7c` (105992 B, 1919 lines) | CP2 v4, source-only, unreviewed |
| `control/parent-release-cp2-design-freeze-v4.json` | `72eb4720f5d21d77195aac9fe939f4c427656ad55a8815dc76d22dd5671b2805` | Read in full; equals `DESIGN_FREEZE_SHA256` reported by v4 |
| `control/parent-release-cp2-v4-repair-scope-v1.json` | `18fe620f22dae58ccd1c5007f9084a13ba19e77a2057ab689e2c7b0adb388175` | CP2 v4 parent scope |
| `review/parent_release_identity_v3_to_v4.diff` | `a9c01e1247c21474bf7a8976566eb466b6ae16b3b0a3e7c498ca0142a73745f1` (1019 lines) | NOT read in full. CP1-relevant v4 source read directly: 618–692, 762–829, 1699–1708, 1777–1781, 1815–1919 |

## 0. Status

- **CP1 v1/v2:** still must not be invoked or receive attestations, because they pin PRT v3 (HOLD).
- **PRT v4:** Codex HOLD, so CP1 v3 cannot pin PRT yet.
- **CP2 v4:** the interface is frozen and known; its review is pending.

The interface deltas below are exact. **Pin values for PRT, and possibly CP2, will still change after review**, which confirms plan v1's advice not to write the source yet.

## 1. Sequencing (to avoid pin churn)

- **G1:** the PRT successor of v4 is frozen and its review is not HOLD (parent verdict).
- **G2:** CP2 v4, or its successor, is frozen and not HOLD. A CP2 repair changes at least the CP2 source sha and the design-freeze value CP1 pins.
- **G3:** a parent authorization naming the CP1 v3 write scope and answering D1–D7.

Then:
1. Freeze an exact-once replacement list against CP1 v2 bytes `9f3d158b…` in a CP1 checkpoint.
2. Create, all mode `x`: `parent_release_caller_v3.py`, the v2→v3 diff, notes v3, disposition v3 and a final checkpoint.
3. Park.

A pin change after step 1 means a new list in a new checkpoint; a frozen list is never edited. If the parent prefers to write before G1/G2 and accept churn, the version-neutral naming (D6) keeps each later re-pin value-only.

## 2. PRT deltas (exact against v4; values are re-taken from the PRT pin that passes G1)

| CP1 v2 site | v2 | v3 (v4 values) |
|---|---|---|
| PRT path / sha / bytes (l.42–44) | v3 file, `161ae04c…`, 81235 | `…/parent_release_v4.py`, `4c4a84f0…`, 83137 → replaced by the G1 successor's values |
| `FORBIDDEN_PRT_SHA256` (l.45–47) | {v1, v2} | add v3 `161ae04c…` and v4 `4c4a84f0…` once a successor is pinned |
| `PRT_MODULE` (l.48); `REGISTRY_FORMAT` owner | `parent_release_v3.py` | `parent_release_v4.py` (or successor) |
| `PRT_REPAIR_SCOPES` (l.50–51) | 2 entries | v4: append `32d161b0408bc297f0e95516980142d741eb219dc882e40bd93df9c79cd59f12`; successor: its full list |
| `RESULT_FORMAT` / `DISPOSITION_FORMAT` / `REGISTRY_FORMAT` / `DISPOSITION_PREFIX` (l.57–60) | `-v3`, `prt-v3-` | `-v4`, `prt-v4-` (or successor) |
| `ACK_STATES` (l.87) | 4 values | add `ACK_ATTEMPTED` |

- **Vocabulary.** Read from the v4 source and confirmed by the PRT owner: ack ∈ {`ACK_NOT_ATTEMPTED`, `ACK_ATTEMPTED`, `ACK_FAILED`, `ACK_UNPROVED_DEADLINE`, `ACK_OK`}; registry status ∈ {`NOT_ATTEMPTED`, `ATTEMPTED`, `APPENDED`, `DEADLINE_CROSSED`, `FAILED`}. The two `*ATTEMPTED` values occur only on exception-attached results.
- **No closed-set status check.** CP1 never checks registry status against a closed set: shape check l.80–82, copy l.815, `== 'APPENDED'` only on returned results l.839. If v3 ever adds such a check, it uses the full lists above.
- **Unchanged:** key sets, `final_deadline_check` values and the release predicate.
- **Exception objects.** CP1 re-raises PRT's identical exception object, so PRT's `parent_release_result` and `parent_release_prior_exceptions` survive whatever PRT's successor changes in its own exception repairs.

## 3. CP2 v4 deltas (exact against `39c51017…`, read in source)

| CP1 v2 site | v2 | v3 |
|---|---|---|
| `identity` keys (`_check_callbacks` l.644–647) | {union, census_log, evaluate_endedness} | {union, **request**, census_log, evaluate_endedness} |
| `CP2_UNION_VERSION` (l.52–56) | module `parent_release_identity_v3.py`, freeze `033cb30d…` | module `parent_release_identity_v4.py`, freeze `72eb4720f5d21d77195aac9fe939f4c427656ad55a8815dc76d22dd5671b2805`; scheme and producer unchanged |
| New pre-invocation request step (in `_union`, S3b) | — | Detach `identity['request']` with CP1 bounds; require `format == 'parent-release-identity-request-v1'` plus D1/D3/D7 |
| `evaluate_endedness` call (l.859–860) | `(union, census_log, deadline_check)` | `(request copy, call.reader.read_bytes, census_log, fresh detached copy of spec.identities, original deadline_check)`, still through `_Call.observe` |
| Endedness acceptance (l.861–866) | format, `ENDED_CONDITIONAL`, `causes []`, hex `endedness_sha256`, `union_sha256` echo == pre-invocation union digest | Same. The echo is now the **rebuilt** union digest. Add the consistency checks implied by ENDED: `identities_match is True`, `union_state == 'CLOSED_CONDITIONAL'`, `union_causes == []`, `deadline_crossed is False`, plus D2 |
| `served_count()` (l.698–702, 867–869) | +1 across PRT | Unchanged. In v4 one factory serves one call and evaluation seals the log, so `served_before == 0` (D3) and `served_after == 1` |
| Receipt identity block | union/endedness digests and served counts | Adds `request_sha256` and `request_bytes` (CP1 canonical) and, with D2, `endedness_module`. Hence `RECEIPT_FORMAT` → `parent-release-caller-receipt-v2` and `RECEIPT_PREFIX` → `prt-caller-v2-` |

Notes:
- **Load-bearing check.** CP2 v4 rebuilds the union from the request with its single builder: `_build_union` 1634, which `build_identity_union` 1684–1687 also wraps; the rebuild runs at 1825. CP1's equality check therefore binds the union CP1 checked before invoking PRT to the union CP2 evaluated. That the rebuild reproduces the same digest from unchanged history bytes is the CP2 owner's statement; it is consistent with the single builder and has not been exercised.
- **CP2 v4 refusal limits.** Requests over 64 KiB, 4096 nodes or depth 8, or containing floats, are refused (762–799).
- **Removed CP2 functions.** `spec_identities_match`, `_v_union` and `_union_version` were never called by CP1.
- **New CP2 condition PARENT_CODE_PROVENANCE.** The parent must pass the pinned module's own builder, factory and evaluator. This becomes part of the prerequisite `identity_union_census_cp2`; D4 makes the attestation name the CP2 source sha.
- **Exception attachment.** The CP2 BaseException attachment `parent_release_endedness_partial` survives because CP1 re-raises the identical object.
- **Reader budget.** The rebuild's history reads go through the shared original reader (at most 16 histories), so they count toward its 1024-call cap and the S11 resource join.

## 4. Self-identified CP1 v2 defects to repair in v3

The same classes as the Codex HOLDs on PRT v3 and v4.

- **S1 (class v3-M3).** Receipt and load progress are understated after a late or interrupted completion: `created` 1015, `identity` 1019, `bytes_written`/`complete` 1027–1028, `file_fsync` 1030, `readback` 1043, `directory_fsync` 1047 and `prt.loaded` 747 are set only after the completion check. Fix: retain them through the `retain` hook before the check. False then means "not proven", never "not performed".
- **S2 (classes v3-M2 and v4-M2).** CP1 drops or demotes BaseException objects in two places:
  - `_Call.release` (480–493) re-raises the FIRST close BaseException and drops later ones; its docstring "later ones keep context" is inaccurate.
  - In `_write_receipt` (1048–1049), a primary BaseException from a native step that is replaced by a cleanup BaseException reaches `invoke_release` only as `__context__`.

  Fix, satisfying v4-M2 "retain exceptions when encountered, before cleanup can replace them":
  - Every BaseException object is appended to one per-invocation list at the moment it is caught. The sources are native, observe, tick, close, the PRT call, CP2 callbacks and bookkeeping.
  - Every owned handle still gets exactly one close attempt.
  - After all attempts, the **newest** propagates with `parent_release_caller_outcome` (HELD) and `parent_release_caller_prior_exceptions` (every other retained object, oldest first).
- **S3 (evidence).** On a PRT BaseException, the HELD outcome records the count and class names of `parent_release_prior_exceptions`.
- **S4 (class v4-M3: exception-metadata access can escape).** Sites in CP1 v2:
  - `_why` (154–159): `str(exc)` under `except Exception`;
  - `observe`/`native` secondary linking (403–404, 438–439): unguarded `__context__` read/write on a foreign exception;
  - `_attached` (1088): `getattr` under `except Exception`;
  - `_raise_held` (1241) and `_account` (1371): attribute assignment under `except Exception`.

  Each can let a non-Exception BaseException raised by an overriding `__str__`/`__getattr__`/`__setattr__`/property escape without being retained or reported. Fix:
  - Read and write exception metadata through C-level descriptors: `BaseException.__dict__['__context__']`, and `BaseException.__dict__['__dict__']` for the `parent_release_*` attributes. Never use attribute syntax on foreign exceptions.
  - Evidence for foreign BaseExceptions is the class name only, read via `type.__dict__['__name__']`.
  - Every bookkeeping step is guarded by `except BaseException`. A bookkeeping failure is itself retained and enters the same newest-wins selection, never escaping unretained.
  - Existing occupied-context and cycle protections are kept: link only when the slot is free and the chain is acyclic (bounded walk).
- **Checked and not present: class v3-M1 / v4-M1.** CP1 writes nothing after any refusal or BaseException, and passes `commit_dir` to PRT only after all owner/spec shaping, including the job_dir exclusion, has passed.

## 5. Decisions requested (yes/no; unanswered = no)

| ID | Proposal | Recommendation |
|---|---|---|
| D1 | `union.item == owner.item` and `request.item == owner.item`; CP2 confirms `union.item` is a stable copy of the request item (cause `CP1_IDENTITY_UNION`) | YES |
| D2 | `endedness.module == 'parent_release_identity_v4.py'`; CP2 confirms it is stable, consistency only (cause `CP1_ENDEDNESS`) | YES |
| D3 | `served_before == 0` before PRT is invoked. Changed from v1's NO: a used v4 factory refuses PRT's census call, so the PRT run is doomed yet still writes a HELD disposition and registry line; refusing first avoids those writes (cause `CP1_IDENTITY_UNION`) | YES |
| D4 | `identity_union_census_cp2` attestation carries `cp2_source_sha256 ==` the pinned CP2 sha (cause `CP1_PREREQUISITE_MISSING`); also covers PARENT_CODE_PROVENANCE | YES |
| D5 | Option B: CP1 executes the verified CP2 bytes itself, creates the census pair, builds and evaluates. v4 makes this smaller (only the request remains parent data) but changes the interface and runs CP2's native census inside CP1 | NO for v3. This matches Main's ~17:30 clarification, recorded in the CP2 v4 freeze, that trusted builder/reader provenance stays an explicit prerequisite |
| D6 | Version-neutral identifiers (`PRT3_*` → `PRT_*`, PRT3 texts/labels → PRT, neutral exec namespace) so later re-pins are value-only | YES |
| D7 (new) | Request↔spec evidence joins before PRT: the main history's `wait_record` typed-equal `spec.exit.wait_record`; the main `launch_record` typed-equal `spec.launch`; `spec.oracle.wait_record` typed-equal some oracle history's `wait_record`. Binds CP2's histories to the exact parent wait/launch files PRT validates, not merely to records with equal fingerprints (cause `CP1_IDENTITY_UNION`). D7b (main `stdout` typed-equal `spec.captures.stdout`) only if the parent confirms both denote the same supervisor stdout capture | D7 YES; D7b NO unless confirmed |

**Consequences:**
- `OUTCOME_FORMAT` → `parent-release-caller-outcome-v2`.
- Receipt format and prefix move to v2 (§3).
- No new causes.
- The only interface change is the `request` key in `identity`, unless D5 is adopted.
- `ReservationAccount` logic is unchanged; it reads v2-format receipts written by v3.

## 6. Unchanged

- The owner keys and the seven prerequisites;
- the S0–S16 sequence and every original-deadline rule;
- the caller-side union version check, which now runs before PRT side effects;
- the global ledger and resource joins;
- the receipt protocol and the consumer rules;
- caps and boundaries.

## 7. Expectations to freeze with the v3 source (NOT exercised)

| ID | Case | Expected |
|---|---|---|
| W01–W04 | PRT attached `ACK_ATTEMPTED` / registry `ATTEMPTED` / propagated priors / old PRT bytes at the pinned path | As plan v1, with the G1 PRT values |
| W05–W08 | S1 late completions (create, write, fsync, PRT definitions) | Flags reflect the completed step; HELD |
| W09 | Two receipt-cleanup closes raise KeyboardInterrupt, then SystemExit | SystemExit propagates; KeyboardInterrupt in `parent_release_caller_prior_exceptions`; each handle closed once |
| W10 | Receipt write raises KeyboardInterrupt, then a cleanup close raises SystemExit (primary plus cleanup) | SystemExit propagates; the KeyboardInterrupt **object** is in the prior tuple |
| W11 | Foreign BaseException subclass whose `__context__` property raises RuntimeError, whose `__setattr__` raises SystemExit, or whose `__str__` raises KeyboardInterrupt | No unretained escape. The newest retained BaseException propagates; attachment uses C-level dict access; bookkeeping failure is recorded |
| W12 | CP2 rebuilt `union_sha256` ≠ pre-invocation union digest | H(`CP1_ENDEDNESS`); no receipt |
| W13 | Synthetic CP2 result `ENDED_CONDITIONAL` with `identities_match:false` or `union_state` HELD | H(`CP1_ENDEDNESS`) |
| W14 | Used census factory (`served_count() == 1` before PRT) | H(`CP1_IDENTITY_UNION`); PRT loaded, not invoked |
| W15 | Request main wait / launch / oracle wait ref ≠ spec refs | H(`CP1_IDENTITY_UNION`); PRT not invoked |
| W16–W18 | D1 item, D2 module, D4 attestation mismatches | H(`CP1_IDENTITY_UNION`) / H(`CP1_ENDEDNESS`) / H(`CP1_PREREQUISITE_MISSING`) |

## 8. Boundaries (unchanged)

- Native calls and callbacks can stall; there is no hard-real-time guarantee.
- C-level descriptor access reduces, but cannot eliminate, the reach of hostile in-process code; minting and module registries prevent accidents, not adversaries.
- `exec` of verified PRT bytes trusts the interpreter.
- Hashes and self-reported fields authenticate selected bytes or claims, not origin.
- An omitted historical identity is undetectable by CP1, and CP2 results are conditional on its listed conditions.
