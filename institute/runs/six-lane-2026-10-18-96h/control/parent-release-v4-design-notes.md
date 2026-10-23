# Parent release transaction v4 — minimal repair candidate, NOEXEC

Actual `/bin/date` before this write: `2026-10-19T17:23:31-0700`.

Source `RUN/control/parent_release_v4.py`: SHA256 `4c4a84f07047fa7499d4cc4bdc8ea29230614f760b2f7cf6fc42e85b16963b59`, 1755 lines, 83137 bytes. Exact source-text diff `RUN/review/parent_release_v3_to_v4.diff`: SHA256 `925dc38e9fe8495b5d48f182e8d6b05132e15becb94738e967f6072689580114` (274 lines, 14084 bytes; equals a regenerated `/usr/bin/diff -u` stream).

Governing inputs:
- base contract `4d122872…`;
- v2 scope `2fdf13b4…` and v3 scope `1f9befdb…`;
- v4 authorization `RUN/control/written-slot-transitions-olson-beta-prt-20261019-1708-v1.json` key `prt_v4`, SHA256 `32d161b0408bc297f0e95516980142d741eb219dc882e40bd93df9c79cd59f12`;
- v3 Codex HOLD (0 FATAL / 3 MAJOR / 2 MINOR) `bf110a0785589ee182a8d348b98ca345ca84dd214fbf16a906f076c38d3e2777`;
- scope freeze checkpoint007 `014b88f324a7b9290f5882f21e0922b854ff9c1e6b88767bded8ed0ffd7dc0fc`.

**SOURCE ONLY, UNTESTED.** No import, compile, AST, test, fixture, helper, runtime or model CLI was run. V1, v2 and v3 stay immutable HOLD. Nothing here grants source readiness, runtime, reservation-release or scientific authority. Global HOLD is unchanged.

## Relationship to earlier notes

The base is `parent-release-v2-design-notes.md` (`9e02abce…`) as amended by `parent-release-v3-design-notes.md` (`7a9fcdca…`). It governs v4 only as amended here; this document wins on conflict.

The v3 disposition errata (`1f654266…`) and the checkpoint006 anchor correction are restated in the control section below and govern.

Every v3 statement naming `-v3` formats, the `prt-v3-` prefix or `parent_release_v3.py` reads as the v4 name.

## Supersessions, exact

1. **Formats and names.**
   - Result: `parent-release-result-v4`.
   - Disposition: `parent-release-disposition-v4`, module `parent_release_v4.py`.
     - `repair_scope_sha256s:[2fdf13b4…, 1f9befdb…, 32d161b0…]`.
     - File: `commit_dir/prt-v4-<slug>-<sha256>.json`.
   - Registry row: `parent-release-registry-v4`, owner `parent_release_v4.py`.
   - `_held_for` (`815-817`) accepts **only** v4 HELD rows for the same allocation. No v3 rows exist, because v3 never ran; there is no compatibility branch.
   - Spec, `parent-release-wait-v1` and `parent-release-late-baseline-v2` are unchanged.
2. **Vocabulary.**
   - `ack` adds `ACK_ATTEMPTED`. It is latched before the ACK readback callback (`_ack:1451`) and promoted only on completion to `ACK_OK` (`1479`). Otherwise it is replaced by `ACK_FAILED` or `ACK_UNPROVED_DEADLINE` as before.
   - Registry `status` adds `ATTEMPTED`. It is latched immediately before registry I/O (`_append_registry:1550`) and promoted to `APPENDED` (`1564`) only after write, fsync and the size check. Otherwise it becomes `DEADLINE_CROSSED` or `FAILED` as before.
   - Both ATTEMPTED values can survive **only** on BaseException-attached results (see T121).
   - `_commit` no longer rewrites `ack` in its Exception branch (`1506-1510`), so it cannot erase a latch.
   - Effective release still needs:
     - `ACK_OK` and `APPENDED`/RELEASED with fsync and clean closes;
     - `live:0` and `unresolved_total:0`;
     - `final_deadline_check:'PASSED'`;
     - CP1.
3. **Exception attachment.**
   - Every raised exception carries, best-effort, `parent_release_result` (an in-memory HELD report) and the **new** `parent_release_prior_exceptions`: a tuple of every other retained BaseException, oldest first (`_attach_and_raise:1661-1668`).
   - **Selection rule:** the newest BaseException propagates, as Python does for an exception raised while handling another.
   - Earlier ones are linked as `__context__` only when that slot is empty and the link is provably acyclic (`_link:1626-1637`, a bounded 64-step walk; otherwise there is no link). They are always kept in the attached tuple and as `Pn_BASE_EXCEPTION` evidence strings.
   - `_absorb` (`1640-1654`) never raises.
4. **Destination.**
   - `ctx.commit_dir` is assigned exactly once, at `_shape:734`. That is the last shaping statement, in the `else` branch after the independent job-dir exclusion succeeded.
   - The validated target is otherwise only the local `candidate` (`683`, `686`).
   - Any interruption or incompleteness before that point leaves `ctx.commit_dir` None. Then `_commit` (`1484-1486`) performs no disposition, ACK or registry I/O.

## Finding map (v3 Codex HOLD `bf110a07…`)

| Finding | v4 change | Anchors (v4 function:lines) | Residual |
|---|---|---|---|
| M1 MAJOR — interrupted shaping bypasses destination exclusion | Local `candidate`; sole `ctx.commit_dir` assignment after exclusion succeeds | `_shape:679-734` (683, 686, 728-734); `_job_dir:650-655`; `_commit:1483-1486` | Lexical containment plus NOFOLLOW walks do not authenticate path origin, aliases or the namespace boundary (parent obligation) |
| M2 MAJOR — second BaseException bypasses the attached HELD report | `_chain` removed; `_absorb` records and returns the newest without raising; priors retained; normal attachment | `_Txn.__init__:288`; `_link:1626-1637`; `_absorb:1640-1654`; `_attach_and_raise:1661-1668`; `decide_and_commit:1690-1723` | Python keeps one `__context__` chain; when its slot is occupied, priors live in the tuple and evidence only |
| M3 MAJOR — BaseException reports say ACK/registry NOT_ATTEMPTED | Conservative latches before I/O; promotion only on completion; no latch rewrite | `_ack:1448-1480` (1451, 1479); `_commit:1506-1510`; `_append_registry:1533-1574` (1550, 1564) | `fsync:false` after an interrupted fsync means "not proven", not "not performed" |
| m4 MINOR — T68 contradicts the source | T68 re-frozen (below) | `_append_registry:1564, 1570-1572` | `APPENDED` is a progress observation only |
| m5 MINOR — T98 lacks distinct part2/part5 sets | T98 split into exact rows (below) | `_names:918-933`; `_Txn.close:435-458`; `_artifacts:936-980`; `_guard:508-517` | — |

Required items of authorization key `prt_v4`: (1)→M1, (2)→M2, (3)→M3, (4)→m4, (5)→m5. The T78/T106 limits are recorded below. No other source behaviour changed. The diff also contains the format/name cutover and docstrings.

## Qualification limits recorded (not solved)

- **T78** injects the crossing *at* the final check: the deadline predicate raises on its last call. It shows that a crossing reported by that check yields in-memory HELD with no I/O afterwards. It does **not** isolate an expiry that happens during actual result assembly, because expiry is observable only when the predicate runs.
  - Optional **T78b** (synthetic): in the isolated control interpreter, wrap `_final` so the deadline state flips to expired inside the single normal-path call at `1712`. Expected: identical to T78.
  - T78b proves detection-at-check of an expiry during assembly. It does not prove real-time behaviour.
  - Native calls may stall; there is no hard real-time guarantee.
- **T106.** "200000 accepted" describes only the entry-count predicate (`_walk:1211`, `_scan:1164-1165`): the 200001st root or child insertion fails with "late tree entry cap".
  - A complete 200000-entry baseline-v2 can be neither produced nor loaded. `build_late_baseline` refuses above 16 MiB of canonical bytes (`1749`, "baseline exceeds16MiB cap"), and `_baseline` reads at most 16 MiB.
  - No successful positive at that size is claimed for the helper or the transaction.
  - Practical baseline capacity is bounded by the 16 MiB serialization: tens of thousands of entries, depending on path length [INFERENCE: about 250–350 canonical bytes per entry].
- **F5 boundary.** `_under`/`_mutation_parts` are lexical checks over normalized absolute strings. Together with anchored NOFOLLOW component walks, they prevent symlink-component escape for the opened path. They do not authenticate the origin of `commit_dir`/`job_dir`, aliases such as hardlinked or bind-like views, or the complete namespace boundary.
- **Owned date on the in-memory paths.** On commit-safe interrupted-shaping paths (T109–T111) `owned_date` is still invoked once, but its reading is unused because no destination exists. Expected callback counts must include it.

## Control amendments — frozen expectations, NOT exercised

Conventions are unchanged from the v2/v3 notes:
- separate GO;
- isolated exclusive fixture destinations;
- exact pins;
- labelled synthetic injection (patching module functions or native calls inside an isolated control interpreter);
- no OS-provenance claim.

**H(c)** means returned or attached HELD with exactly the listed causes, in `CAUSES` order. Unless stated otherwise, the fixture is otherwise positive. "Attached" means the propagated exception's `parent_release_result`. Expected sets must never widen to absorb unrelated failures.

| ID | Case | Exact expected outcome |
|---|---|---|
| T68 (re-frozen) | Registry fd close raises OSError after a completed append | status `APPENDED`; `fsync:true`; `line_complete:true`; `closed:false`; returned HELD, exactly [`P5_REGISTRY_APPEND_FAILED`]; `unresolved_total:1` (kind fd); `final_deadline_check:'PASSED'`; `uncertainty` = RELEASED-bytes message (the prepared line is RELEASED). APPENDED is never authority |
| T98-part2 (re-frozen) | In `_artifacts`: `next` raises OSError, then the iterator close raises OSError | exactly [`P2_ARTIFACT_SET_MISMATCH`, `P2_ARTIFACT_IDENTITY`]; NATIVE_EXCEPTION event for `scandir next <job_dir>`; `resources.unresolved` has a row of kind `iterator` with `fd:null`; `unresolved_total:1`; then a normal HELD commit (`ACK_OK`, `APPENDED` HELD v4 line); `final_deadline_check:'PASSED'`; no other cause accepted |
| T98-part5 (re-frozen) | Same pair inside the part5 late walk | exactly [`P5_LATE_CENSUS_INCOMPLETE`]; same event, iterator row and `unresolved_total:1`; `late_audit.fresh_entries:null`; normal HELD commit; no other cause accepted |
| T81 (v3 erratum) | Commit-dir component open OSError, then the completion check raises | exactly [`P5_DEADLINE`, `P5_COMMIT_WRITE_FAILED`]; `ack:'ACK_NOT_ATTEMPTED'` (initial, not rewritten) |
| T82 (v3 erratum) | Late successful `os.open` in the part5 walk | exactly [`P5_DEADLINE`]; fd retained and closed once; in-memory HELD |
| T99 (v3 erratum, re-frozen) | `next` OSError, then iterator close raises KeyboardInterrupt | part2: [`P2_ARTIFACT_IDENTITY`, `P2_BASE_EXCEPTION`]; part5: [`P5_LATE_CENSUS_INCOMPLETE`, `P5_BASE_EXCEPTION`]; one HELD commit under the unchanged original deadline (`ACK_OK`, `APPENDED` HELD line); KeyboardInterrupt re-raised with the attached result and `parent_release_prior_exceptions:()` |
| T100 (re-frozen) | Registry fd close raises KeyboardInterrupt (first of two closes) | exactly [`P5_BASE_EXCEPTION`, `P5_REGISTRY_APPEND_FAILED`]; status `APPENDED`; `fsync:true`; `closed:false`; dfd closed once; `unresolved_total:1`; KeyboardInterrupt propagates with the attached HELD; `final_deadline_check:'NOT_PERFORMED'` |
| T101 (re-frozen) | Completion check after the first registry close raises KeyboardInterrupt | exactly [`P5_BASE_EXCEPTION`]; status `APPENDED`; `closed:false`; both closes attempted once (`unresolved_total:0`); `original_deadline_crossed:true`; KeyboardInterrupt with the attached HELD |
| T78 (limit) | Deadline raises at the final-assembly check only | as frozen in v3; isolates detection at the check, not expiry during assembly |
| T78b (synthetic, optional) | Expiry flipped inside the wrapped normal-path `_final` | `final_deadline_check:'CROSSED'`; HELD [`P5_DEADLINE_AFTER_ACK`]; no I/O after the check; registry `APPENDED`/RELEASED bytes are not authority |
| T106 (limit) | 200000 vs 200001 entries | 200001st insertion → H(`P5_LATE_CENSUS_INCOMPLETE`) / helper `ReleaseRefusal` "late tree entry cap…"; at 200000 only the count predicate passes; helper production fails "baseline exceeds16MiB cap"; no positive claimed at that size |
| T109 | Synthetic KeyboardInterrupt in `_preflight`, with `commit_dir == artifacts.job_dir` | KeyboardInterrupt re-raised; attached H(`P1_BASE_EXCEPTION`); parts 1 FAIL, 2–5 NOT_EVALUATED; `disposition:null`; `ack:'ACK_NOT_ATTEMPTED'`; registry `NOT_ATTEMPTED`; no module open/create/write anywhere (job_dir untouched); `owned_date` invoked once; `final_deadline_check:'NOT_PERFORMED'` |
| T110 | Synthetic KeyboardInterrupt in `_job_dir` (exclusion step); valid aifours `commit_dir` outside job_dir | as T109: exactly [`P1_BASE_EXCEPTION`], no disposition (v3 would have committed; v4 must not) |
| T111 | Synthetic KeyboardInterrupt in `_v_identities` (mid-shaping), `commit_dir == job_dir` | as T109 |
| T112 | `census` raises KeyboardInterrupt, then `owned_date` raises a fresh SystemExit | SystemExit propagates; `__context__ is` the KeyboardInterrupt; `parent_release_prior_exceptions == (KeyboardInterrupt,)`; attached H(`P4_BASE_EXCEPTION`, `P5_BASE_EXCEPTION`); parts 1–3 PASS, 4–5 FAIL; `disposition:null` (owned_date unsafe ⇒ no commit I/O); `final_deadline_check:'NOT_PERFORMED'`; `resources.live:0` |
| T113 | As T112 but the SystemExit already has a context X | `__context__` stays X (not overwritten); the KeyboardInterrupt is still in `parent_release_prior_exceptions` and in the `P4_BASE_EXCEPTION` evidence |
| T114 | `census` KeyboardInterrupt, then a synthetic KeyboardInterrupt in `_owned_reading` (all callbacks safe) | second KeyboardInterrupt selected; first in the prior tuple (and linked if free); one HELD commit: disposition `recorded_at:null`, `ACK_OK`, `APPENDED` HELD line; attached H(`P4_BASE_EXCEPTION`, `P5_BASE_EXCEPTION`) |
| T115 | ACK `read_bytes` raises KeyboardInterrupt | `ack:'ACK_ATTEMPTED'` (never NOT_ATTEMPTED); registry `NOT_ATTEMPTED`; disposition `create_attempted`/`created`/`line_complete`/`file_fsync`/`directory_fsync` true with identity; dfd closed once; attached H(`P5_BASE_EXCEPTION`) |
| T116 | ACK original-inode lstat raises KeyboardInterrupt (synthetic native) | `ack:'ACK_ATTEMPTED'`; NATIVE_BASE_EXCEPTION event; attached H(`P5_BASE_EXCEPTION`); no registry I/O |
| T117 | Registry `fsync` raises KeyboardInterrupt after a complete write | status `ATTEMPTED` (never NOT_ATTEMPTED); `bytes_written` = line length; `line_complete:true`; `fsync:false`; `closed:true`; `ack:'ACK_OK'`; attached H(`P5_BASE_EXCEPTION`); RELEASED-bytes `uncertainty` for a RELEASED line; line bytes preserved |
| T118 | Registry leaf open raises KeyboardInterrupt | status `ATTEMPTED`; `bytes_written:0`; `closed:true` (dfd closed once); attached H(`P5_BASE_EXCEPTION`) |
| T119 | Registry tail `pread` raises KeyboardInterrupt | status `ATTEMPTED`; `bytes_written:0`; `closed:true`; attached H(`P5_BASE_EXCEPTION`) |
| T120 | `census` KeyboardInterrupt, then KeyboardInterrupt in the first disposition `os.write` | second KeyboardInterrupt propagates; `__context__ is` the first (free slot); `parent_release_prior_exceptions == (first,)`; attached H(`P4_BASE_EXCEPTION`, `P5_BASE_EXCEPTION`); `create_attempted`/`created` true, `bytes_written:0`, `ack:'ACK_NOT_ATTEMPTED'`, registry `NOT_ATTEMPTED`; partial object preserved |
| T121 (vocabulary regression) | Every non-BaseException outcome in T01–T120 | `ack` ∈ {NOT_ATTEMPTED, ACK_OK, ACK_FAILED, ACK_UNPROVED_DEADLINE}; registry status ∈ {NOT_ATTEMPTED, APPENDED, DEADLINE_CROSSED, FAILED}; ATTEMPTED values appear only on attached BaseException results; positives T01/T77 unchanged (`ACK_OK`, `APPENDED`) |

All other T01–T108 rows stand as amended by the v3 notes and the restatements above. "(v3 erratum)" rows replace the corresponding v3 text. The amended T01–T108 and new T109–T121 remain authored, unexercised expectations until independent source review and a separate finite GO.

## Unchanged external prerequisites (not waived)

- **CP1:** the caller receipt and capacity accounting require the caller-observed returned `RELEASED` with `final_deadline_check:'PASSED'`. No disk line or syntax alone is authority.
- **CP2:** the complete historical identity-union record.
- **Raw/beta adapters and authentic provenance.** The beta worker owns the raw supervisor19 adapter; no overlapping edits were made here. The RQLS10 eight consumer obligations also stay with the adapters. The RQLS9 fixture capture schema is fixture evidence only.
- **Scope:** the publication freeze; complete lane, TMPDIR, capture and alias scope; baseline provenance.
- **Reader:** the reader-global unresolved-resource report.
- **Owned date:** owned-date lifecycle settlement.
- **Large artifacts:** the >16 MiB part2 streaming interface.
- **Stalls:** native stalls; there is no hard real-time guarantee.
