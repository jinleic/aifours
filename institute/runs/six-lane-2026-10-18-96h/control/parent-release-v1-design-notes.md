# Parent release v1 — immutable self-HOLD source

Actual `/bin/date` before this write: `2026-10-19T13:40:09-0700`.
Source: `parent_release_v1.py`, SHA256 `6bc92891779feb3e50b3d9948a5d7fc0711a451665794d7fd32738807ad60127` (1386 lines, 63068 bytes). No execution/import/compile/tests occurred.

## Governing design and status

Frozen base contract: `parent-release-transaction-contract-v1.json`, `4d12287257f8bf74d9057a796a0c6f7a391387c411b95d5dcda1131aa4692d3e`. Checkpoint 001 (`0fe334f0…`) freezes every field schema, cause order and initial design before code; checkpoint 002 (`4e3eaa41…`) corrects deadline/BaseException/registry/identity boundaries before code. Read those exact immutable records for the complete v1 interface. This note does not supersede their authority.

V1 is **SELF_REPORTED_SOURCE_HOLD_NOT_QUALIFIED**, not a complete release implementation. Parent accepted the reported defects as ground truth and authorized a **new v2**, scope `parent-release-transaction-v2-repair-scope-v1.json`, `2fdf13b45e946df4f07881b0e6e2b5bc5452ea33d1df022afe896dded698b407`. V1 remains unchanged; no v1 caller should be admitted.

Known blocking deltas:

1. `_Txn.read:246-261` and `_take_census:812-837` check the original deadline after a successful callback, but not after its `Exception`. A later callback can therefore start before that failure completion is deadline-checked. Required v2: primary callback failure retained, then original-deadline check on **every** completion, secondary failure retained, stop on crossing.
2. `_signature:883-885` / `_signature_key:888-889` / `_scan:892-911` compare metadata only. A content change preserving the signature escapes part 5. V2 must hash every regular file with stable identity/metadata and bounded anchored chunked reads.
3. Fresh late accounting has free bytes only; it does not record distinct-inode logical and allocated `st_blocks*512` totals including roots/directories. Unknown accounting must be HELD, never zero.
4. `_parts:116-121` normalizes absolute paths but does not constrain commit_dir / registry mutation paths to aifours. V2 must enforce that scope.

## Exact entry points and semantics

`decide_and_commit(spec, read_bytes, census, owned_date, commit_dir, deadline_check) -> dict` and `build_late_baseline(roots, deadline_check) -> dict`. Definitions only at import; no launcher, scheduler, signal or clock read. All callbacks are trusted parent interfaces, not self-authenticating observations.

`spec` exact keys: `item, go, allocation, gate, launch, exit, captures, publication, artifacts, oracle, identities, late_audit, reservation, exit_table`. `exit_table` is the contract-required explicit list of `{actual_exit:int,state:str}`; no defaults. Oracle adds a pinned parent `wait_record` so actual exit0 is not inferred from its verdict. GO/launch generic documents use the exact fields frozen in checkpoint001; existing heterogeneous raw lane records are **not** parsed by this module. A separately reviewed raw adapter and parent-authenticated expectation construction remain required.

Main rules: part1 binds pinned current GO/launch/gate/RUNNING registry allocation/reservation; part2 joins parent raw wait status, both complete outer capture bytes, publication hash/explicit exit mapping and actual job-directory identities/digests; part3 requires distinct admitted oracle GO, parent wait exit0, complete captures and pinned PASS verdict bound to exactly declared artifact digests; part4 independently calls census and tests supplied incarnations, owned groups and current parent links; part5 compares supplied roots against baseline, checks free floor and obtains an owned bounded date. Independent causes accumulate in frozen `CAUSES` order, evidence capped at 16×512 chars/cause. Shape-invalid dependencies mark the dependent part BLOCKED; release requires all five PASS and no causes.

Counts/exit codes/inode fields use exact `type(...) is int` (bool is not int); hashes lowercase hex64; JSON duplicate keys/nonfinite numbers reject. Read cap16MiB; JSON documents1MiB; spec4MiB (embedded <=256KiB); decision strictly <1MiB; job entries4096; late entries200000/depth64. Artifacts >16MiB are deliberately HELD pending a separately reviewed streaming interface, not silently skipped.

A disposition is created once with `O_EXCL|O_NOFOLLOW`, mode0444, bounded write, file fsync, own-inode readback, close, directory fsync; ACK re-reads via `read_bytes` and checks bytes/hash plus original dev/ino/link/size. EEXIST/partial writes/ACK failures never overwrite or remove. Registry append follows **only ACK_OK** and validates the observed prefix/current suffix first; one append-only line, fsync and descriptor close, then the original deadline check. No registry creation/rewrite.

`state:RELEASED` returned to the caller is effective only with all part checks, ACK_OK, complete RELEASED append/fsync/clean close, final original deadline and trusted-parent prerequisites. A written RELEASED line can survive later failure: its syntax alone is **not** authority. CP1 caller receipt is proposed, not implemented. Other results/exceptions mean HELD.

Detected deadline crossing: no new callback/I/O; only cleanup of already-owned FDs. In-memory HELD only if crossing occurred before commit. Crossing after write leaves an unacknowledged immutable disposition; crossing after ACK forbids registry append; crossing after append leaves possibly visible RELEASED bytes but returned HELD. Kernel calls can stall; byte caps are not a time bound.

Non-Exception BaseException in evaluation may attempt HELD only while original deadline/reader/date remain safe; the original exception is re-raised with `parent_release_result` when possible. BaseException from read/deadline/date makes that path unsafe: immediate re-raise, no commit. BaseException during commit propagates immediately, with the earlier exception chained when appropriate. No refreshed cleanup allowance.

## What v1 cannot establish

No independent OS provenance of supplied wait/capture/identity/authentication claims, interpreter/source actually executed, atomic immutable namespace, complete historical union (including reparented/unproved/unknown incarnations), freshness of a malicious/cached census, or raw supervisor result semantics. Current pid/ppid/group checks supplement a **complete authenticated union**, not prove its completeness. CP2 union-record binding is still a parent/raw-adapter prerequisite. Root coverage must encompass the whole RUN and all applicable lane roots; a caller cannot narrow it to obtain release. V1's missing content conservation and accounting are additional source defects, not waived prerequisites. No scientific or runtime authority follows.

## Finite controls for a separately admitted successor run

No control was run. Use isolated exclusive parent-frozen fixtures; synthetic callbacks must be labelled synthetic, never OS evidence. Repair v2 first, then freeze its exact full matrix (not v1) with these required outcomes:

| Family | Isolated alteration | Required outcome |
|---|---|---|
| Positive | All five valid, empty pin maps allowed | RELEASED, causes=[], all PASS, ACK_OK, one durable RELEASED line; caller must observe return |
| P1 | Bad GO hash; later same-item terminal registry line; bad gate chronology | HELD, respectively P1_GO_INVALID / P1_ALLOCATION_NOT_CURRENT / P1_GATE_NOT_BEFORE_LAUNCH; independent checks still run |
| P2 | Bad wait status; stdout byte/hash fault; extra artifact; publication exit mapping fault | HELD, respectively P2_EXIT_INVALID / P2_CAPTURE_STDOUT_INVALID / P2_ARTIFACT_SET_MISMATCH / P2_PUBLICATION_EXIT_INCONSISTENT |
| P3 | Oracle exit!=0; capture fault; verdict!=PASS; digest map mismatch | HELD, respectively P3_ORACLE_EXIT / P3_ORACLE_CAPTURE_INVALID / P3_ORACLE_VERDICT / P3_ORACLE_BINDING |
| P4 | Incomplete census; live identity; reused pid; nonempty owned group | HELD; P4_CENSUS_INCOMPLETE; live identity also P4_IDENTITY_ALIVE (+P4_OWNED_GROUP_NONEMPTY if same group); reused pid P4_PID_REUSE_AMBIGUOUS |
| P5 | Undeclared new/changed/removed file; low free; unsettled/bad date | HELD, matching P5_LATE_UNDECLARED_* / P5_FREE_BYTES_LOW / P5_OWNED_DATE_FAILED |
| Callback Exception | Reader/census/date raises | Owning cause; post-completion original deadline check REQUIRED (v1 reader/census defect); no exception becomes PASS |
| Deadline | Initial, any callback success/failure, assembly, post-write/ACK/append crossing | HELD; no new I/O after detection; partial artifacts preserved; written RELEASED bytes not authority |
| ACK | Wrong bytes/type/hash/inode or readback Exception | ACK_FAILED (deadline crossing ACK_UNPROVED_DEADLINE); no registry line |
| Registry | Open/write/fsync/close failure | HELD, P5_REGISTRY_APPEND_FAILED; preserve partial/visible line; no syntax-only release |
| BaseException | Evaluation vs reader/deadline/date vs commit | Safe original-deadline HELD attempt then re-raise vs immediate re-raise/no unsafe I/O; no second disposition attempt |
| New v2 obligations | Signature-preserving content mutation; unknown st_blocks; outside-aifours write targets | HELD; v1 does not satisfy these controls |

Independent source review then separately admitted finite controls remain required. No execution authority or acceptance is claimed by this document.
