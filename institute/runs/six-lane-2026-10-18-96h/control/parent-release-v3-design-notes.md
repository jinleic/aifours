# Parent release transaction v3 — minimal repair candidate, NOEXEC

Actual `/bin/date` before this write: `2026-10-19T16:28:00-0700`.

Source `RUN/control/parent_release_v3.py`: SHA256 `161ae04ce4ee98db76bb5b9b983cdfa13c769733b10159ebb5d31b5e377bd23a`, 1727 lines, 81235 bytes. Exact source-text diff `RUN/review/parent_release_v2_to_v3.diff`: SHA256 `5633fcbb88faccbff0af97748e414d740f5e7302c36071dafaac9b0ae7d4b37f` (693 lines, 36306 bytes; equals a regenerated `/usr/bin/diff -u` stream). Governing: base contract `4d122872…`; v2 scope `2fdf13b4…`; v3 scope `1f9befdb4d012800a8e2160c0ce8e822d255e34c88496fd26cb8875aac894030`; v2 Codex HOLD (5 MAJOR/1 MINOR) `935b74fb14bfe4b3e62a583d3fa5c3de8e3946f3edb0e9a7f935317340bbb5ad`; design freeze checkpoint005 `19e4cf6c41eeadd84202574fde14f99ca0e217be1222d32f90b7308bb85866f6`.

**SOURCE ONLY, UNTESTED.** No import, compile, AST, test, fixture, helper, runtime or model CLI was run. V1 and v2 stay immutable HOLD. Nothing here grants source readiness, runtime, reservation-release or scientific authority. Global HOLD unchanged.

## Relationship to the v2 notes

`RUN/control/parent-release-v2-design-notes.md` (SHA256 `9e02abcebb46f58cf384401bca3da0a7fa08ca20019d553b3ed4308a06616b7b`) still describes the interfaces, spec and document schemas, the five part predicates, the baseline-v2 schema, accounting, exclusive/ACK/append protocol and T01–T76. For v3, that text applies **only as amended below**. Where they conflict, this document governs. All v2 external boundaries remain unresolved and are restated at the end.

Supersessions, exact:

1. **Formats/names.** Result `parent-release-result-v3`. Disposition `parent-release-disposition-v3`, module `parent_release_v3.py`, field `repair_scope_sha256s:[2fdf13b4…, 1f9befdb…]` (replaces `repair_scope_sha256`), file `commit_dir/prt-v3-<slug>-<sha256>.json`. Registry row `parent-release-registry-v3`, owner `parent_release_v3.py`. `_held_for` (`810-812`) accepts **only** v3 HELD rows for the same allocation; any later same-item row of another format fires `P1_ALLOCATION_NOT_CURRENT`. No v2 rows exist because v2 never ran; there is no compatibility branch.
2. **Unchanged schemas.** Spec (14 keys), `parent-release-wait-v1`, `parent-release-late-baseline-v2` and its entry/accounting fields are unchanged. The v3 helper `build_late_baseline` (`1704-1727`) produces it; regenerate any baseline with v3. RQLS9 fixture capture records `{path,sha256,bytes,inode:[dev,ino],eof:true}` (original-created descriptor then NOFOLLOW reopen) are **fixture evidence, not the PRT capture API**. The PRT capture schema `{path,sha256,bytes_seen,bytes_stored,eof,overflow,error}` is unchanged and v3 neither accepts nor emulates the fixture schema; a separately reviewed adapter must perform any mapping.
3. **Result keys.** `fds` is replaced by `resources:{acquired:int, closed:int, live:int, unresolved_total:int, unresolved:[{kind:'fd'|'iterator', fd:int|null, path:str, error:str}] (first 64)}`. New `final_deadline_check`: `PASSED | CROSSED | NOT_PERFORMED_ALREADY_CROSSED | BASE_EXCEPTION | NOT_PERFORMED` (the last on exception-attachment paths). The disposition progress record adds `create_attempted:bool`. Registry `status` vocabulary is `NOT_ATTEMPTED | APPENDED | DEADLINE_CROSSED | FAILED`; `DEADLINE_CROSSED` replaces `NOT_APPENDED_DEADLINE` because a crossing can now be detected mid-write. Inspect `bytes_written`, `line_complete` and `fsync`.
4. **Effective release.** `_final` (`1601-1617`) additionally requires `resources.live == 0` and `unresolved_total == 0`. The caller must also see `final_deadline_check == 'PASSED'`. A `PASSED` value implies the returned `state` survived the final check. CP1 caller integration still decides capacity accounting.
5. **Event log.** `callback_events`/`callback_count`/`callback_event_sha256` keep their names but now also record native failures (`NATIVE_EXCEPTION`, `NATIVE_BASE_EXCEPTION`, stage = operation + path) and deadline events. The first 128 rows are kept, plus a rolling digest of all rows. Successful native operations are not logged.
6. **Destination exclusion.** Commit is refused when `commit_dir` equals or lies below `artifacts.job_dir`, or when `job_dir` cannot be independently validated. Previously only exact equality with a fully valid artifact object was refused.
7. **Deadline/BaseException wording.** The v2 statements "No new I/O after detection" and "BaseException … no renewed allowance" still hold. They are now implemented per native operation and per close, as described below.

## v3 mechanisms (source anchors are function:lines in v3)

**F1 — final assembled result check.** In `decide_and_commit` (`1648-1701`), the complete returned dict is first assembled by `_final` (`1687`). Then `txn.tick('final assembled result completion')` runs at `1690-1692`. On failure, in-memory re-assembly gives HELD (`1698-1699`), and `final_deadline_check` is set to `CROSSED`, or to `NOT_PERFORMED_ALREADY_CROSSED` if the latch was already set (`1700`). No I/O follows the check. A BaseException from the check fires `P5_BASE_EXCEPTION`, re-assembles HELD, records `BASE_EXCEPTION` and re-raises with `parent_release_result` (`1693-1697`). The only work after a passing check is one dict store and `return`. **This is not a hard real-time guarantee:** a late caller observation or a stall after return is outside the module.

**F2 — native completion checks.**
- `_Txn.native` (`371-392`) runs a full original check before the call (`must_tick`), so a crossed latch refuses any new I/O. It then makes one native call.
  - On Exception, it logs the primary event, runs the same check (`failed`, `362-369`; a secondary BaseException keeps the primary as `__context__`) and re-raises the primary.
  - On success, the non-raising `retain` hook stores returned ownership or progress, and then the completion check runs.
  - It never retries.
- `must_tick`/`tick` carry `after_ack`. A deadline BaseException now also latches `crossed` (`tick`, `315-330`).
- Routed through `native`:
  - `os.open` (`_Txn.open`, `417-430`); late completion closes the retained fd once.
  - `os.stat(lstat)` (`_lstat`, `909-910`, used at `_artifacts` `931-975`, `_scan` `1148-1173`, `_ack` `1443-1474`).
  - Every `os.fstat` (`_names`, `_hash_file`, `_scan`, `_walk`, `_write_new`, `_registry_tail`, `_append_registry`).
  - `os.scandir`/`next` (`_names`, `913-928`).
  - `os.read` (`_hash_file`, `1119-1145`, progress via `txn.stream`).
  - `os.write` (`_write_all`, `1385-1398`, per-write progress before the check).
  - `os.pread` (`_pread_exact`, `1407-1415`).
  - `os.fsync` (file/dir/registry, with `_mark` `1401-1404` retaining `file_fsync`/`directory_fsync`/`fsync` before the check).
  - `os.fstatvfs` (`_free_bytes`, `1216-1228`).
- Not routed through `native`:
  - `os.close`/`iterator.close`: cleanup, always permitted for owned handles and then followed by the original check unless already crossed (`_Txn.close`, `432-455`).
  - `os.getpid` (non-blocking identity) and `os.waitstatus_to_exitcode` (pure decode).
- Callback completions are unchanged: `_Txn.observe` (`336-360`).

**F3 — iterators.**
- `_names` (`913-928`) acquires the `os.scandir(fd)` iterator only through `native`, with a pre-check.
- `own` (`397-401`) retains it in the same ledger, keyed `('iterator', id)`, before the completion check.
- It enumerates with `native(next, iterator, None)`, with checks on every entry, and the closing `fstat` is checked too.
- `release` closes the iterator once in `finally`, even after a BaseException.
- Iterator close failures go to `resources.unresolved` (kind `iterator`) and `unresolved_total`, and fire the owning cause (`P2_ARTIFACT_IDENTITY` in part2, `P5_LATE_CENSUS_INCOMPLETE` in part5).
- An enumeration primary stays both as a `NATIVE_EXCEPTION` event and as the owning cause.
- The source relies on CPython's documented fd-based `scandir`: the iterator dup()s the fd and rewinds before closedir. This is source reasoning only.

**F4 — nested cleanup.**
- `_Txn.release` (`457-473`) attempts one close of every owned handle in reverse order and continues after a BaseException. It returns `clean`, and re-raises the **first** BaseException only after all attempts. Later failures stay in the unresolved ledger/event log.
- `_append_registry` (`1528-1568`) owns `[dfd, fd]` and sets `closed` from `release`. It is first set False, so a raising release leaves `closed:false`.
- `_Txn.open` uses `release` for its late-completion fd. `directory()` (`475-487`) already closes the current fd once if an intermediate close raises.
- Commit-phase BaseException (`1682-1686`) fires `P5_BASE_EXCEPTION` and chains any pending evaluation BaseException as context. It propagates with an in-memory HELD `parent_release_result`; there is no further I/O and no second commit.
- Partial dispositions and registry bytes are preserved and never removed.

**F5 — destination exclusion.** `_job_dir` (`647-652`) validates `artifacts.job_dir` independently of the declared map. In `_shape` (`724-729`), `commit_dir` equal to or below it, or an unavailable/invalid `job_dir`, gives `P5_COMMIT_DIR_INVALID` and `commit_dir=None`. That means an in-memory HELD only: no disposition, ACK or registry I/O. Malformed specs consequently lose on-disk HELD evidence; the allocation remains held regardless.

**F6 — root cap.** `_walk` (`1199-1213`) applies `len(entries) <= 200000` right after inserting each root (`1206`). The same check after every child insertion remains in `_scan`.

**Other v3 detail.**
- `_commit` (`1477-1508`) sets `create_attempted` before `O_EXCL`. After any failure or crossing following that attempt, it records uncertainty ("unacknowledged/partial object may exist"); `created:false` alone is never proof of absence.
- `_ack` maps a crossing during the inode check to `ACK_UNPROVED_DEADLINE`, not `ACK_FAILED`.
- `build_late_baseline` raises `ReleaseRefusal('original deadline crossed…')` whenever the latch is set, including when the primary was a native Exception.

## What v3 still cannot establish (all remain explicit prerequisites, not solved)

- **CP1:** a caller receipt and capacity accounting that requires the caller-observed returned `RELEASED`, `final_deadline_check:'PASSED'`, ACK and registry completion. A written RELEASED disposition or registry line alone is never authority.
- **CP2:** a full historical identity-union record binding every driver/main/helper/descendant/unproved/unknown/oracle incarnation, escaped and reparented ones included. Current pid/ppid/group checks are supplements only.
- **Raw adapters and authentic provenance:** GO, revocation, allocation, original deadline, argv/cwd/env/interpreter/source/input, parent wait and complete capture histories, oracle invocation and semantics.
  - The beta worker owns the raw supervisor19 adapter separately; this worker made no overlapping edits.
  - The RQLS10 eight consumer obligations remain in the raw adapter's scope.
- **Exclusive immutable publication freeze; all applicable lane-root/TMPDIR/capture/alias scope; baseline provenance.**
- **The pinned reader's global unresolved-resource report** must be retained and joined by the parent as a release prerequisite. This module's ledger covers only its own descriptors and iterators.
- **Owned-date callback lifecycle settlement:** pre-spawn original deadline, bounded capture, identity, reap, group/descendant closure, EOF/close and at most one checked TERM.
- **Part2 artifacts larger than 16 MiB stay HELD** until a separately reviewed streaming artifact interface binds them to the authentic job and oracle invocation.
- **Native calls can stall.** Checks bound only detection and subsequent new I/O, not syscall latency. Each native op adds about two `deadline_check` calls, so a 200000-entry walk can make millions of calls; the callback must be cheap and nonrenewing.
- The `retain` hooks are assumed non-raising bookkeeping. A MemoryError there could skip one completion check; the result would still be HELD through the internal-error path.

## Finite control expectations — frozen, NOT exercised

The rules from the v2 notes still hold for every case:

- separate GO;
- isolated exclusive fixture destinations;
- exact pins;
- synthetic callbacks labelled as synthetic;
- no OS-provenance claim.

Native faults require **labelled synthetic fault injection at the native boundary in an isolated control interpreter**. Deadline crossings are injected as `deadline_check` raising at an exact, pre-counted call index (counts taken from a frozen deterministic fixture). Observable invariants:

- the `deadline_check` call that follows each native completion;
- that no native op or callback happens after a detected crossing (injection counters);
- `resources` counts;
- exact ordered causes.

**R** means:

- returned `state:'RELEASED'` and `release_effective:true`;
- `final_deadline_check:'PASSED'` and `ACK_OK`;
- one `APPENDED` v3 RELEASED row with `fsync` and `closed` true;
- `causes:[]`, all parts PASS;
- `resources.live:0` and `unresolved_total:0`.

**H(c)** means returned HELD with exactly the listed ordered causes.

Amended v2 rows:
- **T01–T03:** the outcome R now includes the final check and the resource predicates above.
- **T56–T59:** they now cover every native completion, not just callbacks. Exception plus crossing gives the owning cause plus `Pn_DEADLINE`, with the primary event retained.
- **T62:** see T83.
- **T66–T68:** statuses `FAILED`, with the progress flags as in v2.
- **T69:** status `APPENDED`, causes `P5_DEADLINE_AFTER_ACK`, `final_deadline_check:'NOT_PERFORMED_ALREADY_CROSSED'`.
- **T73:** see T100/T101.
- Wherever v2 notes say `NOT_APPENDED_DEADLINE`, read `DEADLINE_CROSSED`.

New rows:

| ID | Isolated case | Exact expected outcome |
|---|---|---|
| T77 | Complete positive | R; final check is the last `deadline_check` call; no native op after it |
| T78 | Deadline raises at the final-assembly check only (crossing at call K = last call of T77) | H(`P5_DEADLINE_AFTER_ACK`); `final_deadline_check:'CROSSED'`; ACK_OK; registry APPENDED/RELEASED/fsync/closed true; `uncertainty` says the RELEASED bytes are not authority; no I/O after the check |
| T79 | Final check raises KeyboardInterrupt | KeyboardInterrupt propagates; attached result HELD with `P5_BASE_EXCEPTION`, `final_deadline_check:'BASE_EXCEPTION'` |
| T80 | Commit-dir component `os.open` raises OSError, deadline passes | H(`P5_COMMIT_WRITE_FAILED`); `NATIVE_EXCEPTION` event; one `deadline_check` immediately after the failure; ACK_NOT_ATTEMPTED; no registry I/O |
| T81 | Same failure, then the completion check raises | H(`P5_COMMIT_WRITE_FAILED`,`P5_DEADLINE`); primary event plus deadline event; no further native op or callback |
| T82 | Late successful `os.open` in the part5 walk | fd retained then closed once (`resources.closed` includes it); H(`P5_LATE_CENSUS_INCOMPLETE`?—no: `P5_DEADLINE` only); no further native op; in-memory HELD |
| T83 | `O_EXCL` disposition open returns late | `create_attempted:true`, `created:false`; uncertainty "deadline crossed in exclusive commit…"; H(`P5_DEADLINE`); no write/fsync/pread/ACK/registry; any zero-byte object preserved |
| T84 | First disposition `os.write` returns late with partial count k | `bytes_written:k`, `line_complete` true only if k is the full length; H(`P5_DEADLINE`); no further write/fsync/pread |
| T85 | Disposition `os.write` raises ENOSPC, deadline passes | H(`P5_COMMIT_WRITE_FAILED`); completion check after the failure; no fsync; fd and dfd each closed once |
| T86 | File `fsync` returns late | `file_fsync:true`; H(`P5_DEADLINE`); no pread/fstat/directory fsync |
| T87 | First of several readback `pread`s returns late (disposition >64 KiB) | H(`P5_DEADLINE`); exactly one pread performed |
| T88 | Directory `fsync` returns late | `directory_fsync:true`; H(`P5_DEADLINE`); ACK callback never invoked; no registry I/O |
| T89 | ACK lstat returns late | `ACK_UNPROVED_DEADLINE`; H(`P5_DEADLINE_AFTER_ACK`); no registry I/O |
| T90 | Registry tail `fstat` or `pread` returns late | status `DEADLINE_CROSSED`, `bytes_written:0`; H(`P5_DEADLINE_AFTER_ACK`); fd and dfd closed once each |
| T91 | Registry `write` returns late with partial count k | `DEADLINE_CROSSED`, `bytes_written:k`, `fsync:false`, partial line preserved; H(`P5_DEADLINE_AFTER_ACK`) |
| T92 | Registry `fsync` returns late | `fsync:true`, `DEADLINE_CROSSED`, no fstat; HELD (`P5_DEADLINE_AFTER_ACK`); a fully written RELEASED line may be visible and is not authority |
| T93 | Registry `fsync` raises EIO, deadline passes | status `FAILED`; H(`P5_REGISTRY_APPEND_FAILED`); completion check after the failure; `line_complete:true`, `fsync:false` |
| T94 | Part5 child-directory close completes late | H(`P5_DEADLINE`); the next native op is refused; no disposition (in-memory HELD) |
| T95 | Directory `fstat` before `scandir` returns late | `os.scandir` never called; H(`P5_DEADLINE`) (part5) or H(`P2_DEADLINE`) (part2) |
| T96 | `os.scandir` raises OSError, deadline passes | owning cause (`P5_LATE_CENSUS_INCOMPLETE` in part5; `P2_ARTIFACT_SET_MISMATCH` in part2); `NATIVE_EXCEPTION` event; no iterator owned |
| T97 | `os.scandir` returns late | iterator retained and closed once; `Pn_DEADLINE`; no enumeration |
| T98 | `next` raises OSError, then iterator close raises OSError | both retained: `NATIVE_EXCEPTION` event, `resources.unresolved[kind:'iterator']`, `unresolved_total:1`; owning cause; HELD |
| T99 | `next` raises OSError, iterator close raises KeyboardInterrupt | the directory fd still closes once; evaluation BaseException rule: one HELD commit under the unchanged original deadline when reader/date/deadline are safe; KeyboardInterrupt re-raised with HELD result (`Pn_BASE_EXCEPTION`) |
| T100 | Registry fd close raises KeyboardInterrupt (first of two closes) | dfd still closed once; `closed:false`; `unresolved_total:1`; KeyboardInterrupt propagates with HELD result (`P5_REGISTRY_APPEND_FAILED`,`P5_BASE_EXCEPTION`); line bytes preserved |
| T101 | Completion check after the first registry close raises KeyboardInterrupt | latch set; second close still attempted (its check skipped); KeyboardInterrupt re-raised after both attempts with HELD result |
| T102 | Intermediate `directory()` close raises KeyboardInterrupt | the current fd closes once; propagation; no further acquisition |
| T103 | One artifact > 16 MiB and `commit_dir == job_dir` | H(`P2_ARTIFACTS_INVALID`,`P5_COMMIT_DIR_INVALID`); no disposition/ACK/registry I/O; `final_deadline_check:'PASSED'` |
| T104 | `commit_dir` is a pre-existing subdirectory of `job_dir` | H(`P2_ARTIFACT_SET_MISMATCH`,`P5_COMMIT_DIR_INVALID`); in-memory HELD |
| T105 | `artifacts` key missing (or `job_dir` invalid) | H(`P1_SPEC_INVALID`,`P2_ARTIFACTS_INVALID`,`P5_COMMIT_DIR_INVALID`) for the missing key; (`P2_ARTIFACTS_INVALID`,`P5_COMMIT_DIR_INVALID`) for an invalid `job_dir`; in-memory HELD |
| T106 | First root yields exactly 200000 entries including itself, then a second empty non-overlapping root | H(`P5_LATE_CENSUS_INCOMPLETE`) with evidence "late tree entry cap (root insertion)"; `build_late_baseline` raises `ReleaseRefusal` with the same text; 200000 total entries is accepted |
| T107 | KeyboardInterrupt injected into `os.read` during a late hash | NATIVE_BASE_EXCEPTION event; each level's fd closed once; HELD commit attempted under the unchanged original deadline; KeyboardInterrupt re-raised with HELD result (`P5_BASE_EXCEPTION`) |
| T108 | `build_late_baseline`: native OSError followed by a crossing | `ReleaseRefusal('original deadline crossed; no baseline returned')` chained from the OSError; no baseline returned |

Correction to T82 wording (frozen together with this file): the exact expected causes are **H(`P5_DEADLINE`)** only. The interrupted walk does not reach a later predicate. The inline question mark in that row records that I considered `P5_LATE_CENSUS_INCOMPLETE` and rejected it: `_guard` re-raises `_Crossed` without firing its own cause. It is not an open expectation.

These are source-derived expectations, not observed output. Expected sets must not widen to absorb unrelated failures. All T01–T76 obligations (as amended) plus T77–T108 remain unexercised until independent source review and a separate finite GO.
