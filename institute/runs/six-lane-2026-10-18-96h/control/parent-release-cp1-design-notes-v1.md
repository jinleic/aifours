# Parent release CP1 caller integration v1 — source-review candidate, NOEXEC

Actual `/bin/date` before this write: `2026-10-19T16:40:54-0700`.

Source `RUN/control/parent_release_caller_v1.py`: SHA256 `4072c50ef5be021a22e72a43571550c1338ab8a4d243752d88e3b7cc71a75cae`, 1375 lines, 69329 bytes. Scope `RUN/control/parent-release-cp1-cp2-implementation-scope-v1.json` (`1f717bf9…d314`, item CP1). Design frozen before source in `review/parent-release-cp1-checkpoint-001-v1.json` (`565a29ed…291c`) and amended (CP2 join) in `review/parent-release-cp1-checkpoint-002-v1.json` (`7e347d77…84cb`). **No import, compile, AST, test, helper, fixture, probe, driver or model CLI was run.** Only source reading/authoring, hashes and byte/line metadata. This is neither source acceptance nor qualification; the parent owns independent review, finite qualification and all launch/release authority. Global HOLD unchanged.

## Pins

| Object | Pin | Status |
|---|---|---|
| PRT3 `RUN/control/parent_release_v3.py` | `161ae04ce4ee98db76bb5b9b983cdfa13c769733b10159ebb5d31b5e377bd23a`, 81235 bytes | Frozen by ParentReleaseTxn; source-only, untested, pending its own independent review. Executed by CP1 only from the verified in-memory bytes. |
| Forbidden PRT | v1 `6bc92891…0127`, v2 `addcdf4c…a1` | Refused; no fallback, no parent-supplied function object. |
| Reader `RUN/control/beta_parent_reader_v1.py` | `1fc8f00c…0ec6` | Declared source pin, disk bytes hash-checked; live object provenance is prerequisite `callback_provenance`. |
| CP2 design freeze | `3d6f48ce…f027` | CP2 module `parent_release_identity_v1.py` not pinned here; CP2 callables are parent-supplied and their provenance is prerequisite `identity_union_census_cp2`. |
| PRT3 interface | result `parent-release-result-v3` (22 keys), disposition `parent-release-disposition-v3` `prt-v3-<slug>-<sha>.json`, registry row `parent-release-registry-v3` (13 keys, line SHA excludes LF) | Read from the frozen v3 text (`_new_result`, `_final`, `_record`, `_append_registry`, `decide_and_commit`). |

## Public interface

```text
invoke_release(owner:dict, spec:dict, reader, census, owned_date, deadline_check, identity:dict)->CallerOutcome
retain_reader(reader)->int            record_unresolved(source:str, detail:str)->None
resource_report()->dict               CallerOutcome: .state .effective .reader .report()
ReservationAccount(): .hold(item, allocation, reservation)  .release(outcome, receipt_ref)->dict  .report()->dict
```

- `owner` exact keys: `item`, `allocation{registry_path,line_sha256,record}`, `reservation{bytes,cpu_slots}`, `commit_dir`, `receipt_dir`, `sources{caller,reader}` refs, `prerequisites{name:ref}` for exactly the seven names below. Item/allocation/reservation must be typed-equal to the detached spec; `record.item==item`, `record.state=='RUNNING'`, `record.reservation_bytes==reservation.bytes`. Both directories are boundary-checked aifours paths, neither equal to nor below `spec.artifacts.job_dir` (absent/invalid job_dir => refusal).
- `reader`: the ORIGINAL pinned `EvidenceReader` constructed with the identical `deadline_check` (structural `reader._check is deadline_check`). Retained in the process ledger as the first statement, before any validation, and held by every outcome; never replaced or wrapped. Its bound `read_bytes` is passed to PRT3 unchanged.
- `census`, `owned_date`: passed to PRT3 unchanged; CP1 never calls them. `census` must be CP2 `make_census` paired with `identity.census_log`.
- `identity` exact `{union, census_log, evaluate_endedness}` (CP2). `deadline_check`: the ORIGINAL nonrenewing predicate (None or raise). No other deadline is ever accepted, including by the consumer.
- Prerequisite attestation documents (pinned bytes, strict JSON) need `format:'parent-release-cp1-prerequisite-v1'`, `prerequisite:<name>`, `item`, `allocation_line_sha256`, `status:'DISCHARGED_BY_PARENT'`. Names: `authority_execution_provenance`, `callback_provenance`, `identity_union_census_cp2`, `oracle_binding`, `publication_freeze_scope`, `registry_single_writer`, `finite_qualification`. They are recorded as `PARENT_ASSERTED_NOT_SOURCE_AUTHENTICATED`; hash-matching JSON authenticates bytes, never origin.

## Invocation sequence (each step's failure is HELD; nothing after it runs)

S0 retain reader; S1 callables, reader deadline binding, CP2 identity shape, nonce `os.urandom(32)` (pre/post original check); S2 owner; S3 bounded own preflight (nodes 131072, depth 256, ints 4096 bits, finite floats, no cycles/shared containers, size bound) → canonical bytes (same definition as PRT3 `spec_sha256`) → strict reparse = detached spec; S3b CP2 union (`parent-release-identity-union-v1`, `CLOSED_CONDITIONAL`, hex `union_sha256`, `prt_identities` typed-equal `spec.identities` with CP1's own equality) and served count; S4 PRT3 bytes through the original reader (cap = exact byte count), SHA pin, `compile`/`exec` of those bytes in a fresh namespace, `decide_and_commit` only; S5 declared caller/reader source bytes; S6 seven attestations. Any S1–S6 cause => PRT3 not invoked, nothing written.

S7 original check, invoke PRT3. Exception => `CP1_PRT_EXCEPTION`; non-Exception BaseException => `CP1_PRT_BASE_EXCEPTION`, HELD outcome attached as `exc.parent_release_caller_outcome`, re-raise with no further callback/I/O. S8 detach result (4 MiB bound) then original check; full RELEASED predicate: exact v3 22-key shape, state/decision RELEASED, `release_effective` true, ACK_OK, `final_deadline_check` PASSED, not crossed, `causes==[]`, parts all PASS, uncertainty null, authority flags false, registry APPENDED/RELEASED/fsync/closed/line_complete with exact allocation registry path and no `detail`, disposition create_attempted/created/line_complete/file_fsync/directory_fsync with bytes_written==bytes and positive inode, resources live0/unresolved_total0/unresolved[]. S8b CP2 `evaluate_endedness(detached union, census_log, deadline_check)` through the callback wrapper: `parent-release-identity-endedness-v1`, `ENDED_CONDITIONAL`, `causes==[]`, hex `endedness_sha256`, echoed `union_sha256` equal to the evaluated union digest, served count exactly +1. S9 disposition re-read through the original reader: exact name `commit_dir/prt-v3-<slug>-<sha>.json`, bytes/SHA, reader observation inode == returned identity, v3 format/module/contract/repair scopes, RELEASED, causes[], parts PASS, `spec_sha256`/`spec_bytes` == caller digest, reservation, authority flags, valid owned date. S10 registry re-read: complete LF-terminated strict JSON lines, allocation line unique and typed-equal record, returned line unique and later, v3 RELEASED row bound to disposition path/SHA, allocation, reservation, recorded_at, `remaining_output_reservation_bytes==0`; any other same-item row after the allocation must be an earlier v3 HELD row for the same allocation. S11 global resource join. S12 original check. S13 exclusive receipt. S14 receipt ACK via the original reader and its own inode observation. S15 global join again. S16 complete outcome assembly, final original check, then only O(1) registration as effective and return.

Every reader/CP2 callback goes through `_Call.observe` (pre-check, call, primary event retained, SAME original check on success or Exception, secondary retained separately, BaseException marks unsafe). Every receipt native step goes through `_Call.native` (pre-check, call, ownership retained before the completion check). After a crossing: no new callback or I/O; only one close attempt per already-owned descriptor. `_Call.release` gives every owned descriptor one attempt even after a BaseException and re-raises the first afterwards.

## Global unresolved resources

`_LEDGER` (process lifetime) strongly retains every original reader and every recorded unresolved entry; nothing is removed. `resource_report()` unions each retained reader's `report()['unresolved']` (an unavailable or malformed report counts as unresolved), parent-recorded entries, caller close failures and PRT3 resource uncertainty (returned live/unresolved, malformed result, or an exception without `parent_release_result`). Any unresolved entry blocks every later CP1 release and accounting in that process. This is deliberately conservative. Descriptor and iterator uncertainty is per process and ends when the process exits; the ledger is not persisted, and no claim survives a restart (a restart also loses every outcome, so nothing can be accounted afterwards).

## Receipt and consumer

Receipt `parent-release-caller-receipt-v1` at `receipt_dir/prt-caller-v1-<slug>-<sha256>.json`: anchored NOFOLLOW directory walk from `/`, `O_RDWR|O_CREAT|O_EXCL|O_NOFOLLOW|O_NONBLOCK|O_CLOEXEC` mode 0444, new empty regular one-link inode, bounded writes, file fsync, pread readback, fstat identity, one close, directory fsync, one close per handle. It binds nonce, reader ledger index, item, allocation, reservation, commit_dir, spec SHA/bytes, PRT3 path/SHA/bytes, declared sources, prerequisite refs and origin label, CP2 union/endedness digests and served counts, result format/SHA/bytes, disposition path/SHA/bytes/inode/recorded_at, registry path/observed bytes+SHA/line indices/line SHA and ledger snapshot SHA. It carries no timestamp of its own (it copies the PRT3 disposition's owned-date text, labelled). EEXIST is failure; nothing is overwritten, removed or repaired.

`ReservationAccount.release(outcome, receipt_ref)` accepts only the identical `CallerOutcome` registered as effective in this module instance. It latches the outcome before any check, requires a held entry typed-equal to the outcome, `receipt_ref == {path, sha256}` of the outcome receipt, a fresh receipt re-read through the outcome's retained original reader under the outcome's retained original deadline, reader inode observation equal to the created inode, receipt fields equal to the outcome's bindings and a clean global join. It then makes a final original check; only then are O(1) ledger moves made (held → released). Every refusal leaves the reservation held and the outcome latched. No scheduler, admission or grant follows.

## Finite consumer-visible fault expectations — frozen, NOT exercised

`H(c)` = `invoke_release` returns `state:'HELD'` with exactly the listed CP1 cause(s) in `CAUSES` order, the outcome is not effective, and `ReservationAccount.release` on it returns `AC_OUTCOME_NOT_EFFECTIVE` with the reservation still held. `R` = RELEASED outcome, receipt ACK_OK, and `release` → `RELEASED_ACCOUNTED` moving exactly that reservation once. Unless stated, every other input is the complete positive. Synthetic callbacks/fault injection must be labelled; they prove predicates, not OS provenance.

| ID | Case | Expected |
|---|---|---|
| F01 | Complete genuine positive (authentic prerequisites) | R; receipt bytes exist; registry/disposition untouched by CP1 |
| F02 | `deadline_check` not callable | H(CP1_CALLBACKS_INVALID); no callback, I/O or nonce |
| F03 | Reader not bound to the identical deadline / missing `report`/`last_file` | H(CP1_READER_INVALID); no reader call, PRT3 not loaded |
| F04 | census/owned_date not callable, or identity keys wrong | H(CP1_CALLBACKS_INVALID); PRT3 not invoked |
| F05 | Owner extra/missing key; reservation≠record bytes; record not RUNNING | H(CP1_OWNER_INVALID) |
| F06 | `receipt_dir`/`commit_dir` outside aifours or prefix-confusable `aifours-evil` | H(CP1_OWNER_INVALID); no mutation |
| F07 | Owner allocation/reservation/item not typed-equal spec (one field, bool-for-int) | H(CP1_SPEC_BINDING) |
| F08 | `receipt_dir` equal to/below `spec.artifacts.job_dir`; job_dir absent | H(CP1_SPEC_BINDING) |
| F09 | Spec cycle, NaN, non-JSON type, >131072 nodes, depth>256 | H(CP1_SPEC_BINDING) |
| F10 | CP2 union HELD / wrong format / `prt_identities` ≠ spec identities | H(CP1_IDENTITY_UNION); PRT3 not invoked |
| F11 | PRT3 bytes differ from pin, or file length differs | H(CP1_PRT_SOURCE); nothing executed |
| F12 | Reader raises at PRT3 read, deadline passes | H(CP1_PRT_SOURCE) plus any other independent S5/S6 causes; PRT3 not invoked |
| F13 | Declared caller/reader source bytes differ; reader pin ≠ `1fc8f00c…` | H(CP1_SOURCE_PINS) or H(CP1_OWNER_INVALID) for the pin itself |
| F14 | One attestation missing/digest mismatch/status not DISCHARGED_BY_PARENT/item mismatch | H(CP1_PREREQUISITE_MISSING), evidence names the prerequisite |
| F15 | Deadline crosses during any pre-invoke read/check | H(CP1_DEADLINE_PRE_INVOKE [+owning cause if the callback raised]); no later callback; PRT3 not invoked |
| F16 | PRT3 returns ordinary HELD (any P-cause) | H(CP1_RESULT_NOT_RELEASED); no CP2 evaluation, readback or receipt |
| F17 | PRT3 HELD with registry RELEASED bytes (v2 T67–T69/T69-class) or `final_deadline_check` CROSSED | H(CP1_RESULT_NOT_RELEASED); uncertainty says RELEASED bytes are not authority |
| F18 | Returned RELEASED but synthetic `final_deadline_check:'NOT_PERFORMED'`, `uncertainty` text, `detail` key, or `unresolved_total:1` | H(CP1_RESULT_NOT_RELEASED [+CP1_UNRESOLVED_RESOURCES]); unresolved recorded globally |
| F19 | Returned non-dict / extra key / bool-for-int / non-JSON value | H(CP1_RESULT_INVALID); global record "PRT3 resource state unknown" blocks later releases in-process |
| F20 | PRT3 raises Exception | H(CP1_PRT_EXCEPTION); attached report retained if any, else global unknown-resource record |
| F21 | PRT3 raises KeyboardInterrupt (commit or evaluation) | Re-raised; `parent_release_caller_outcome` HELD with CP1_PRT_BASE_EXCEPTION; no further callback/I/O; reader retained |
| F22 | **Post-result/pre-receipt:** original deadline crosses immediately after PRT3 returns complete RELEASED | H(CP1_DEADLINE_POST_RESULT); no CP2 evaluation, readback or receipt; RELEASED disposition/registry bytes exist and are not authority |
| F23 | Post-result: CP2 endedness HELD / raises / served count +0 or +2 | H(CP1_ENDEDNESS); no receipt |
| F24 | Post-result: disposition re-read raises, bytes/inode differ, `spec_sha256` ≠ caller digest, wrong name | H(CP1_DISPOSITION_READBACK); no receipt |
| F25 | Post-result: registry line missing/duplicated/before allocation, later same-item row, torn tail, malformed unrelated line, remaining≠0 | H(CP1_REGISTRY_READBACK); no receipt |
| F26 | Post-result: another retained reader has an UNKNOWN resource, or any recorded unresolved entry | H(CP1_UNRESOLVED_RESOURCES); no receipt |
| F27 | Post-result: deadline crosses at S11/S12 after all readbacks | H(CP1_DEADLINE_POST_RESULT); no receipt I/O |
| F28 | **Receipt:** directory missing / symlink component / receipt name exists | H(CP1_RECEIPT_WRITE); EEXIST object untouched; `create_attempted` true for EEXIST |
| F29 | Receipt write returns 0 / raises after partial bytes | H(CP1_RECEIPT_WRITE); partial exclusive receipt preserved, not authority |
| F30 | Receipt fsync / pread mismatch / inode change / directory fsync raises | H(CP1_RECEIPT_WRITE); complete bytes may exist |
| F31 | Receipt close raises Exception | H(CP1_RECEIPT_WRITE + later CP1_UNRESOLVED_RESOURCES for every subsequent call); global record permanent in-process |
| F32 | Deadline crosses after any receipt native step | H(CP1_DEADLINE_RECEIPT); only owned-handle closes follow; possible partial/complete receipt preserved |
| F33 | KeyboardInterrupt from a receipt write, then the first close also raises BaseException | Every owned handle still gets one close attempt; first BaseException re-raised with HELD outcome attached |
| F34 | Receipt ACK read raises / bytes differ / observed inode differs | H(CP1_RECEIPT_ACK); complete receipt not authority |
| F35 | ACK returns after deadline | H(CP1_DEADLINE_RECEIPT) |
| F36 | ACK leaves an UNKNOWN reader resource | H(CP1_UNRESOLVED_RESOURCES) at S15 |
| F37 | Deadline crosses during final outcome assembly | H(CP1_DEADLINE_FINAL); `final_deadline_check:'CROSSED'`; receipt exists, outcome not effective |
| F38 | Deadline predicate returns non-None at any stage | That stage's deadline cause; treated exactly as a crossing |
| F39 | Deadline predicate raises BaseException at any stage | Propagates with HELD outcome attached (CP1_BASE_EXCEPTION); no further callback/I/O except owned-handle closes |
| F40 | Spec/owner mutated by another reference after invocation starts | No effect: CP1 and PRT3 use the detached copy only |
| A01 | `release` with dict, `report()` copy, deserialized receipt, foreign object | AC_OUTCOME_NOT_EFFECTIVE; nothing latched or accounted |
| A02 | `release` with a HELD outcome | AC_OUTCOME_NOT_EFFECTIVE |
| A03 | Second `release` of one outcome (same or another account) | AC_OUTCOME_LATCHED |
| A04 | Allocation never held, or held with different reservation | AC_NOT_HELD; outcome latched HELD |
| A05 | `receipt_ref` path/SHA differs | AC_RECEIPT_REF_INVALID; latched |
| A06 | Receipt deleted/replaced/altered, reader raises, inode differs | AC_RECEIPT_READBACK; latched |
| A07 | New unresolved resource since invocation | AC_UNRESOLVED_RESOURCES; latched |
| A08 | Original deadline crossed at start, after readback or at final assembly | AC_DEADLINE; latched; no new deadline accepted |
| A09 | BaseException from reader/deadline in `release` | Propagates with `parent_release_account_record` HELD; latched |
| A10 | Process restart with receipt + RELEASED disposition/registry on disk | Nothing can be accounted: no API accepts disk bytes |

These are source-derived expectations, not observed output. A later runner must freeze isolated fixtures and exact causes, retain native results independently and compare without broadening the expected sets.

## Source-readiness prerequisites (exact, unresolved)

1. PRT3 `161ae04c…d23a` independent hostile review and finite qualification (v3 is source-only/untested). CP1 inherits every PRT3 defect.
2. Independent review of this CP1 source, then a separately admitted finite control run of F01–F40/A01–A10 with labelled synthetic faults.
3. CP2 `parent_release_identity_v1.py` frozen, reviewed and qualified. ParentIdentityCP2 confirmed by IRC (not yet in a frozen CP2 source) the names CP1 uses: `CensusLog.served_count()` (zero-argument method, exact int), union keys `format/state/union_sha256/prt_identities`, endedness keys `format/state/causes/endedness_sha256` with the `union_sha256` echo always present, and `evaluate_endedness` never raising Exception.
4. Parent-authored attestations for all seven named prerequisites, which do not exist. Until they do, every invocation is HELD before PRT3 runs.
5. The parent constructs the original `EvidenceReader` from pinned bytes `1fc8f00c…` with the original deadline predicate, and supplies the qualified owned-date helper and nonrenewing deadline predicate.
6. A parent single-writer registry premise, plus receipt-directory creation and freeze. Receipts are new RUN entries that later late audits must declare.

## Impossible-to-certify boundaries

- Native syscalls and callbacks (reader, CP2, PRT3, deadline predicate) can stall arbitrarily past the deadline. Every check follows completion; there is no hard-real-time proof. A late success is HELD, never a new allowance.
- In-process Python can forge or mutate objects (`_MINT`, `_EFFECTIVE`, `outcome._fields`). Minting prevents accidental use of dicts, copies or reports, not hostile in-process code. Module reload or process restart resets the in-memory ledgers and loses every outcome.
- `exec` of verified bytes trusts the interpreter and the stdlib modules imported by PRT3. Interpreter provenance is external (`callback_provenance`).
- Disk bytes (receipt, disposition, registry, attestations) and matching hashes authenticate only the selected bytes, never their origin or completeness. The structural reader binding (`reader._check is deadline_check`) is not code provenance.
- CP1 cannot detect an omitted historical identity. It relies on CP2's union and endedness, which are themselves conditional (CP2 `conditions_always`).
