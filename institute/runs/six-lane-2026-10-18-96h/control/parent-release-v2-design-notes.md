# Parent release transaction v2 — source-review candidate, NOEXEC

Actual `/bin/date` before this write: `2026-10-19T13:49:32-0700`.

Source `RUN/control/parent_release_v2.py`: SHA256 `addcdf4c75c08bd4cd1e6d13c833886d058851b9b1927557008bb41bf93992a1`, 1596 lines, 73848 bytes. Base contract `4d12287257f8bf74d9057a796a0c6f7a391387c411b95d5dcda1131aa4692d3e`; repair scope `2fdf13b45e946df4f07881b0e6e2b5bc5452ea33d1df022afe896dded698b407`; checkpoints001–003 freeze design before source. V1 `6bc92891…` remains immutable/self-HOLD. This is neither source acceptance nor empirical qualification. **No import, compile, AST, tests, helper, fixture, driver, checker, solver or model CLI was run.** Only source reading/authoring, hashes, byte/line metadata and the requested source-text diff occurred.

## Authority boundaries (not solved by v2)

1. The caller authenticates authority and actual observations: exact parent GO/current revocation/allocation, actual argv/cwd/environment/interpreter/source/input execution binding, parent wait/captures, actual oracle invocation and checker semantics. Matching typed JSON and SHA256 authenticate selected bytes, not their origin. Raw supervisor parsing and the RQLS10 eight consumer obligations remain a separate qualified adapter.
2. A parent-enforced **exclusive immutable publication freeze** covers all evidence paths, ancestors/namespaces, aliases and relevant writers for the call. NOFOLLOW, stable fstat brackets and hashes do not create an atomic OS snapshot. No cache in this module; reads are fresh, but that alone cannot prove immutability between acquisitions.
3. CP2: parent/raw adapter must bind `identities` to the **complete historical union** of all applicable incarnations: driver/main/helpers/descendants/unproved/unknown/oracle and every reparented or escaped incarnation. Current pid/ppid/group checks cannot prove an omitted historical identity does not exist. Disposition says `identity_union_completeness:EXTERNAL_PREREQUISITE_NOT_VERIFIED`; no invented completeness guarantee.
4. Part5 requires exact whole `RUN_ROOT` in roots. The parent also authenticates coverage of **all applicable lane roots**, temporary resources, outer captures and aliases; source cannot derive that scope from a current process list. No narrowing roots to obtain release.
5. CP1: effective release requires the parent caller to **observe the complete returned RELEASED outcome**, ACK_OK, completed append/fsync/close and final original-deadline check. A RELEASED registry line can survive a later failure. Its syntax, `remaining_output_reservation_bytes:0`, or an on-disk RELEASED disposition alone is not authority. A parent-owned exclusive caller receipt binding item/disposition/registry line/result digest is proposed in checkpoint002 but **not implemented**. Downstream reservation accounting must not act on line syntax before CP1 integration.
6. No new launch, clock, signal, scheduler, next-item admission, science authority, publication authority, overwrite, removal or outside-aifours mutation. Source-only results never waive global HOLD.

## Entry points and callback interfaces

```text
decide_and_commit(spec:dict, read_bytes:callable, census:callable,
                  owned_date:callable, commit_dir:str, deadline_check:callable)->dict
build_late_baseline(roots:list[str], deadline_check:callable)->dict
```

Definitions/constants/stdlib imports only at import. Neither entry runs at import. Baseline helper is observation-only, separately admitted, writes nothing and starts no processes. No v1 import/alias/shim. Baseline, disposition, registry and result schemas are **v2 only**; native parent wait-record schema remains `parent-release-wait-v1` (unchanged evidence schema, not a v1 implementation shim).

- `read_bytes(path:str,cap:int)->bytes`: pinned beta reader `1fc8f00c08cd9f78885c9a38fa0797ce5b01aba8e8ad39a6d19d7b6ce3370ec6` semantics: normalized absolute anchored NOFOLLOW parents and regular one-link leaf, NONBLOCK, bounded cap+1 read, post-read identity/size/link/time/close/deadline checks. Parent retains the original reader and its resource report on **every** exception; unresolved reader resources remain parent HOLD. Do not pass an unlabelled synthetic reader as kernel evidence.
- `census()->{complete:bool,processes:[{pid:int,ppid:int,pgid:int,uid:int,start_fingerprint:str}],observed_at_mono:float}`. Exact keys, nonnegative exact ints, unique pids, <=200000 rows, finite exact float. Must be a new independent full snapshot, not cached or filtered to waive UIDs/unproved identities. Observing parent PID must be present as a positive coverage check. No module clock is read; the finite float is syntax, not independent freshness proof. Freshness/provenance is a callback contract.
- `owned_date()->{settled:bool,text:str|None,child:{pid:int,pgid:int,start_fingerprint:str},reaped:bool,group_empty:bool,stdout_eof:bool,term_sent:int}`. Exact keys; four flags true, pid/pgid positive and equal, fingerprint nonempty, term_sent exact int0, text valid 24-char `/bin/date +%Y-%m-%dT%H:%M:%S%z` (no LF). Term1 or unsettled/unparsable => P5_OWNED_DATE_FAILED, null date. Callback itself owns pre-spawn original deadline, bounded capture/cleanup, full identity/group/descendant/EOF/close proof and at most one checked SIGTERM; module never launches it or invents time.
- `deadline_check()->None` or raise, always the **original** nonrenewing deadline. Non-None return is failure. Synchronous open/read/fsync/close may stall beyond it: byte limits do not bound latency. Late success is HELD, never a new allowance.
- `commit_dir`: normalized absolute, equal to or strictly below `/Users/jinleic/repos/aifours`, anchored NOFOLLOW; not exactly the artifact job directory. Registry mutation target has the same aifours-only check. No other mutation target.

## Exact spec and selected document schemas

All containers/scalars use exact Python types; bool never int. JSON duplicate keys/NaN/Infinity reject. Counts nonnegative; hashes lowercase64hex. A `ref` is exact `{path,sha256}` with normalized absolute path. Spec is detached through bounded JSON preflight/serialization before callbacks; arbitrary objects, cycles, oversized nodes/strings/ints reject.

`spec` exact keys (14):

| Field | Exact shape and checks |
|---|---|
| `item` | str1..512, no NUL/CR/LF |
| `go` | ref; selected document object with `status:PARENT_GO`, `item==spec.item`, nonempty `argv:list[str]`, `pins:dict[str,hex64]` (empty allowed), `reservation:{bytes,cpu_slots}`, `gate:ref`, `exit_table:list`; no key `oracle_for` |
| `allocation` | `{registry_path,line_sha256,record}`; aifours registry path; SHA of line **excluding LF**; exactly one matching line; record typed-equal parsed line; record has state RUNNING, exact item, reservation_bytes, positive driver_pid/driver_pgid, go_sha256, launch_record_sha256, nonempty abs_end. Complete LF-terminated JSON-lines registry required. Bytes==spec.reservation.bytes; GO/launch digests==refs. Current = every later same-item row is `parent-release-registry-v2`, HELD, same allocation line SHA. Any later terminal/release/other allocation row blocks. No old v1 HELD reinterpretation. |
| `gate` | ref; stability_gate_v2 document verdict PASS, reasons exactly[], valid now_date. GO must cite exact gate ref; gate.now_date<=launch.started_at plus GO→launch hash chain establishes declared prelaunch observation. Full original stability algorithm/source provenance remains parent/gate evidence. |
| `launch` | ref; selected object with item, nonempty argv, normalized cwd, env_sha256, pins, reservation, started_at, driver exact `{pid,pgid,start_fingerprint}`, go ref. GO item/argv/pins/reservation typed-equal launch; launch.go==spec.go; driver pid/pgid==allocation and fingerprint==unique driver identity. Env digest syntax bound to selected launch; actual environment execution provenance external. |
| `exit` | exact `{actual_exit:int,observed_by:'parent',wait_record:ref}`; negative signals permitted, never bool. Wait doc exact `{format:'parent-release-wait-v1',item,role:'driver',pid,pgid,start_fingerprint,raw_status:int>=0,actual_exit:int,observed_by:'parent'}`. `os.waitstatus_to_exitcode(raw_status)==actual_exit==spec.exit.actual_exit`; identity matches registry/driver. This consumes actual parent-wait evidence, never calls waitpid. |
| `captures` | exact `{stdout,stderr}`, distinct paths; each exact `{path,sha256,bytes_seen:int,bytes_stored:int,eof:true,overflow:false,error:null}`; seen==stored<=16MiB; actual file length/hash match. Completeness is not result-line/schema correctness; beta X2/X5 remains separate. |
| `publication` | exact `{path,sha256,expected_state}`; selected bytes hash equal, expected_state nonempty str. Does **not** parse raw supervisor state; adapter owns content semantics. |
| `exit_table` | list of exact `{actual_exit:int,state:str}`, unique exits; must typed-equal prelaunch GO exit_table; actual_exit maps to exactly expected_state. Missing mapping fails, no default or waiver. A mapped UNKNOWN outcome can release ended resources if oracle PASS validates the evidence, without scientific acceptance. |
| `artifacts` | exact `{job_dir,declared:{name:{sha256,bytes}}}`; <=4096 plain names; per artifact<=16MiB (larger => HELD, separate part2 streaming interface still required); exact actual directory name set; each actual file regular, nlink1, ino>0, size matches; anchored lstat brackets stable; read_bytes hash/length match. Actual namespace/alias freeze remains external. |
| `oracle` | exact `{go:ref,actual_exit:0,captures:{stdout,stderr},verdict_path:ref,verdict:'PASS',bound_artifact_digests:{name:sha256},wait_record:ref}`. Oracle wait_record is the explicit extension needed for **actual** exit0. GO document status PARENT_GO, oracle_for==item, distinct from main GO. Wait schema above with role oracle, exit0, matching role oracle identity; distinct from driver wait ref. Pinned verdict document verdict PASS, item==spec.item, bound_artifact_digests==spec map==declared artifact map exactly. Parent binds this GO/invocation/wait/captures/verdict, not just their syntax. |
| `identities` | nonempty list of exact `{role,pid,pgid,start_fingerprint,source}`; roles driver/main_child/helper/descendant/unproved/oracle/oracle_child/oracle_helper; positive pid/pgid; unique (pid,fingerprint); exactly one driver, >=1 oracle required by part4. Empty cannot evidence none because driver+oracle necessarily apply. Fingerprints use the same parent definition across launch/wait/census. CP2 complete historical union remains mandatory. |
| `late_audit` | exact `{roots:[paths],baseline_manifest:ref,allowed_new:[paths or plain names]}`; roots unique/nonempty and **exact RUN_ROOT present**, plus parent-authenticated all applicable lane roots. Allowed absolute paths match only that path; plain names match that exact basename wherever it occurs; **no subtree wildcard**. New/changed/removed entries and changed directories each require declaration. |
| `reservation` | exact `{bytes:int>=0,cpu_slots:int>=0}`; typed-equal GO/launch; bytes==registry reservation_bytes. Released only under CP1 complete outcome; no next CPU admission. |

GO/launch/gate/verdict documents may contain extra inert keys; required fields are consumed above. Wait documents and spec records have exact keys. The parent never treats an ignored raw extra field as authority.

## Part5 baseline-v2, content conservation and accounting

Both helper and main checker use **one** walker/schema:

```text
{format:'parent-release-late-baseline-v2',roots:[exact paths],
 entries:{absolute_path:{kind,dev,ino,mode,nlink,bytes,allocated_bytes,mtime_ns,ctime_ns,sha256}},
 accounting:{whole:{entries,distinct_inodes,logical_bytes,allocated_bytes},
             by_root:{root:{entries,distinct_inodes,logical_bytes,allocated_bytes}}}}
```

Kinds file/dir/symlink/fifo/socket/device/other must match mode. All eight numeric metadata fields are exact ints; positive ino/nlink, nonnegative bytes/allocated_bytes (multiple512), times may be negative. For regular files sha256 is lowercase64hex; for every other kind null. Baseline roots must each be actual directories and entries must be within declared roots; recomputed accounting must typed-equal baseline accounting. V1 seven-element signatures are rejected, not upgraded synthetically.

Walk uses anchored directory FDs/NOFOLLOW/NONBLOCK, deterministic names, before/after stable directory fstat. Symlinks/FIFOs/sockets/devices are lstat-only, never followed/opened as files. Cross-device child directory => incomplete HOLD. Each regular file is opened relative to its retained directory; fd fstat must equal selected lstat metadata, SHA256 is streamed in <=65536-byte chunks, exact original st_size plus EOF required, and final fstat must match original dev/ino/mode/link/size/mtime/ctime/st_blocks. Original deadline checks surround each chunk and after file/directory/accounting completion. Per-file cap16GiB, aggregate actual streamed bytes128GiB, entries200000/depth64. Caps are HELD refusal boundaries, never silently truncated successful evidence.

Fresh comparison checks **all entry fields**, including content SHA, identity, metadata and directory sizes/times/blocks. Same-size rewritten regular content is detected even if mtime is restored. A changed directory (including root) must be declared along with the new/removed file. Baseline publication itself, captures, oracle outputs, registry changes and parent review files created after baseline must all be declared explicitly. A directory declaration does not exempt descendants. Baseline helper returns data but does not publish its own file; parent must account for that later publication.

Accounting includes the root itself, every directory and every other entry. `bytes=st_size`, `allocated_bytes=st_blocks*512` from actual native metadata. Missing/invalid st_blocks/st_size/identity metadata causes **P5_ACCOUNTING_UNAVAILABLE**, not0. Whole totals deduplicate `(dev,ino)` across roots and hardlink aliases; per-root totals deduplicate within each root. Same-inode rows with different observations reject (no mixed snapshot). These are logical inode allocation counts, **not physical APFS reclaimable-space claims**: clone/shared extents may be double-counted across distinct inodes. Independent fresh `f_bavail*f_frsize>=12.2e9` is still required per root; unknown free-byte fields cause HELD. Overlapping roots are not double-counted in whole totals.

## Deadline, exceptions and bounded output

`_Txn.observe` is the **only** read_bytes/census/owned_date route, including ACK. On callback success or Exception it retains the primary event **before** the original deadline check. If the callback raised and deadline also raises, both survive (callback event + deadline event/cause); the primary is re-raised to its owning predicate, then `_guard` unwinds immediately on the crossed latch. A secondary BaseException keeps the primary in exception context. No callback failure becomes PASS or `[]`.

Parts execute1→5, independent causes accumulate; invalid dependencies mark BLOCKED, never PASS by default. Release requires all five PASS and no causes. Unexpected Exception => owning/internal cause and HELD. Read/census/date callback Exception checks are not skipped. Deadline_check is itself the original predicate, not recursively checked by itself.

On first detected crossing: **no new callback/I/O**, only close attempts on already-owned FDs. Before commit => in-memory HELD/no disposition. After exclusive file acquisition/write => a partial or complete unacknowledged file may exist, no ACK/append. After ACK => no append. After append/fsync/close => RELEASED bytes may exist but returned HELD. Do not interpret `created:false` or zero retained progress as proof of no side effect: acquisition/check failure may happen before a successful wrapper return. Files are never removed/replaced. Kernel operations may complete late or stall; this source does not claim a hard kernel-latency bound.

Non-Exception BaseException during evaluation records Pn_BASE_EXCEPTION and halts remaining parts. HELD commit is attempted **only** if original deadline, reader and date callbacks are still safe, under their unchanged checks. A read/date/deadline BaseException marks the path unsafe: immediate re-raise, no further I/O. Census BaseException may permit HELD recording while original deadline remains safe. The original exception is re-raised with `parent_release_result` when possible. Any BaseException during commit propagates immediately (prior exception as context where appropriate), no second commit attempt or renewed cleanup allowance.

Bounds: reader16MiB/call; selected JSON docs1MiB, registry/baseline/publication16MiB; spec4MiB/131072 nodes/4096-bit integers, no cycles/non-JSON types; spec embedded only<=256KiB; cause evidence<=16 strings×512 chars each; read log first256 plus rolling digest; callback log first128 plus rolling digest; decision strictly<1MiB (oversize => reduced HELD or no commit, not a truncated RELEASED); registry line<=65536; FD opens<=1000000, unresolved close sample<=64; no blind close retry. Parent reader's own call/resource caps may cause conservative HELD.

## Exclusive disposition, ACK and append protocol

One content-addressed `prt-v2-<item slug<=64>-<sha256>.json` per call in aifours-only commit_dir: anchored NOFOLLOW directory walk; O_RDWR|O_CREAT|O_EXCL|NOFOLLOW, mode0444; bounded write; file fsync; original-fd byte readback/fstat; one close; directory fsync; original deadline check. EEXIST is failure (no idempotent overwrite). Byte caps do not make these syscalls timed.

ACK re-reads exact length via parent `read_bytes`, original deadline checked on success/Exception, compares exact bytes and hash, then lstat under retained directory fd must match original dev/ino/size, regular/nlink1; completion deadline checked again. Failure=>ACK_FAILED (successful-but-late read=>ACK_UNPROVED_DEADLINE); **no registry line**. Successful readback does not waive a failed deadline/close.

After ACK_OK only: registry is opened anchored O_RDWR|O_APPEND|NOFOLLOW|NONBLOCK, **no O_CREAT**; must be regular one-link positive inode, <=16MiB. Selected observed prefix length/SHA must persist; new suffix must be complete JSON lines; any same-item suffix must be v2 HELD for same allocation, else refuse. Parent must serialize writers: this is compare-and-append under a **single-writer premise**, not a lock-based multiwriter algorithm. Bounded write of one LF-terminated sorted-key JSON row, fsync, size check, clean FD/directory closes, then final ORIGINAL deadline check.

Row format `parent-release-registry-v2`: item, state RELEASED|HELD, disposition path/SHA, allocation_line_sha256, decision_in_disposition, ordered causes, recorded_at (owned text/null), reservation, remaining_output_reservation_bytes (0 only proposed RELEASED), release_effect warning. On normal HELD with safe ACK/current registry, one HELD line. If no safe selected allocation/registry or deadline is gone, no unsafe append; caller receives HELD/uncertainty. A partial append, fsync/close failure, concurrent growth or final-deadline crossing can leave line bytes visible: caller MUST retain reservation HELD. Never erase/fix a torn line in place.

Result `parent-release-result-v2`: state HELD by default; decision (on-disk proposal), release_effective bool, ack status, disposition path/SHA/bytes/create-progress/fsync/identity, registry status/state/hash/bytes/fsync/closed/progress, ordered causes/evidence/parts, original_deadline_crossed, bounded callback events/digest, FD counts/unresolved, uncertainty and external boundary statements. `decision:RELEASED` is **not** result.state RELEASED. Only complete caller-observed returned state RELEASED is eligible for CP1 release integration.

## Finite control matrix — frozen expectations, NOT exercised

Every case is later separately admitted under its own GO, isolated exclusive fixture destinations, exact source/fixture pins and expected cause assertions. Synthetic callbacks/native fault injection must be explicitly labelled; they prove predicates, not OS provenance. A native positive must use actual anchored reader/census/owned helper, complete parent outer capture, and all CP1/CP2 prerequisites. Fixtures never write science audit directories or trigger a next allocation.

Notation: **R** = returned state RELEASED, decision RELEASED, causes=[], parts allPASS, ACK_OK, one APPENDED RELEASED line fsync=true/closed=true and final deadline success. **H(c)** = returned HELD with exact listed cause(s), ACK_OK and one HELD line when original deadline/registry remain safe; no reservation freed. Unless specified, repair pins/baseline/allowed declarations so only the named isolated defect applies. Causes always in `CAUSES` order, not discovery order. Changes to job files may also change directory metadata: explicitly declare those parent-directory changes in controls intended to isolate another cause.

| ID | Finite case | Exact expected outcome |
|---|---|---|
| T01 | Complete genuine positive, empty GO/launch pins maps | R, conditional on authentic external preconditions |
| T02 | Explicit driver exit2 (raw wait512), matching exit-table state UNKNOWN, oracle validates evidence | R; no scientific PASS inferred |
| T03 | Negative signal exit with exact raw wait status and explicit mapped state, all ended/checker PASS | R only if prelaunch table admits exact mapping; no default fallback |
| T04 | GO file digest mismatch, otherwise valid | H(P1_GO_INVALID) |
| T05 | GO argv differs from launch only | H(P1_GO_LAUNCH_MISMATCH) |
| T06 | Gate.now_date after launch, all refs repinned | H(P1_GATE_NOT_BEFORE_LAUNCH) |
| T07 | Allocation line not typed-equal record (one otherwise irrelevant copied field) | H(P1_ALLOCATION_INVALID) |
| T08 | Later same-item RELEASED/terminal/nonmatching-allocation row | H(P1_ALLOCATION_NOT_CURRENT); no interpretation as RUNNING |
| T09 | Spec reservation.bytes differs from GO and allocation; GO/launch still agree | H(P1_RESERVATION_INVALID,P1_ALLOCATION_BINDING) |
| T10 | Registry has unterminated tail or malformed unrelated line | HELD/P1_ALLOCATION_INVALID; no selected safe registry => no append |
| T11 | Main wait raw status inconsistent with exit while spec/table unchanged | H(P2_EXIT_INVALID) |
| T12 | actual_exit bool or float in spec | H(P2_EXIT_INVALID), no bool0 alias |
| T13 | Complete stdout length/hash mismatch (includes prefix byte loss) | H(P2_CAPTURE_STDOUT_INVALID); no invented content/schema cause |
| T14 | Missing/eofFalse/overflowTrue/error/non-int bytes in stdout record | H(P2_CAPTURE_STDOUT_INVALID) |
| T15 | Stderr file/hash mismatch | H(P2_CAPTURE_STDERR_INVALID); complete nonempty stderr alone is not forbidden by generic PRT |
| T16 | Publication file digest mismatch only | H(P2_PUBLICATION_INVALID) |
| T17 | expected_state lacks exact exit-table mapping | H(P2_PUBLICATION_EXIT_INCONSISTENT) |
| T18 | Extra actual job filename, declared as late allowed path to isolate P2 | H(P2_ARTIFACT_SET_MISMATCH) |
| T19 | Same-size artifact content mutation, expected/oracle map unchanged, late path declared | H(P2_ARTIFACT_DIGEST) |
| T20 | Artifact hardlink/nlink2, actual reader refuses, late paths declared | H(P2_ARTIFACT_IDENTITY,P2_ARTIFACT_DIGEST) |
| T21 | Part2 artifact >16MiB | H(P2_ARTIFACTS_INVALID); no partial read/PASS |
| T22 | Oracle GO reused main GO / lacks oracle_for | H(P3_ORACLE_GO_INVALID) |
| T23 | Oracle actual_exit1 or boolFalse | H(P3_ORACLE_EXIT) |
| T24 | Oracle wait raw status!=exit0 | H(P3_ORACLE_EXIT) |
| T25 | Oracle complete capture actual bytes/hash mismatch | H(P3_ORACLE_CAPTURE_INVALID) |
| T26 | Pinned oracle verdict FAIL | H(P3_ORACLE_VERDICT) |
| T27 | Oracle spec+verdict agree on digest map different from declared artifacts | H(P3_ORACLE_BINDING) |
| T28 | Census completeFalse, parent present | H(P4_CENSUS_INCOMPLETE) |
| T29 | Census omits parent pid | H(P4_CENSUS_INCOMPLETE) |
| T30 | Census observed_at_mono int/NaN instead of finite exact float | H(P4_CENSUS_STALE) |
| T31 | Live owned identity same pid/fingerprint/pgid, no owned ppid | H(P4_IDENTITY_ALIVE,P4_OWNED_GROUP_NONEMPTY) |
| T32 | Same pid/different fingerprint, unrelated pgid/ppid | H(P4_PID_REUSE_AMBIGUOUS) |
| T33 | Different pid in owned pgid, unrelated ppid | H(P4_OWNED_GROUP_NONEMPTY) |
| T34 | Escaped current child with ppid ownedpid, different pgid | H(P4_OWNED_DESCENDANT) |
| T35 | Remove all role oracle identities | H(P3_ORACLE_EXIT,P4_ORACLE_IDENTITIES_MISSING) |
| T36 | Deliberately omit a reparented/different-group historical identity | **External CP2 must reject before release**; source cannot detect omission, no in-module guarantee or new cause invented |
| T37 | roots omit exact RUN_ROOT | H(P5_LATE_AUDIT_INVALID); dependent part5 blocked, no narrowed positive |
| T38 | Feed baseline-v1 signature schema | H(P5_LATE_AUDIT_INVALID); no shim |
| T39 | New undeclared regular file (declare changed directories only) | H(P5_LATE_UNDECLARED_NEW) |
| T40 | Same-size regular content rewrite, restore mtime, do not declare file | H(P5_LATE_UNDECLARED_CHANGED), content SHA/ctime retained |
| T41 | Remove file (negative fixture only; no actual run deletion permission) | H(P5_LATE_UNDECLARED_REMOVED), using a pre-frozen synthetic fresh snapshot or isolated authorized fixture |
| T42 | Directory metadata changed but not declared, children changes otherwise declared | H(P5_LATE_UNDECLARED_CHANGED) |
| T43 | Legitimate new/changed entries and all changed dirs explicitly declared | R if all other parts valid; declaration is exact path/name, not subtree |
| T44 | Two hardlink aliases of one actual regular inode in late roots | R if declared; logical/allocated counted once whole and within each root, both names retained |
| T45 | Overlapping roots | R if stable; whole counts each(dev,ino) once, per-root scoped totals exact |
| T46 | st_blocks unavailable/non-int/negative on root/dir/file | H(P5_ACCOUNTING_UNAVAILABLE), fresh_accounting null; never0 |
| T47 | Same inode observed with inconsistent metadata/digest aliases | H(P5_LATE_CENSUS_INCOMPLETE) |
| T48 | File grows/replaces/changes ctime/mtime/blocks during chunk read | H(P5_LATE_CENSUS_INCOMPLETE), no complete content claim |
| T49 | FIFO/symlink in late roots | R if declared and otherwise valid; lstat-only, target/FIFO never opened as regular file |
| T50 | Cross-device child directory / per-file16GiB / total128GiB / depth64 / entry200000 cap exceeded | H(P5_LATE_CENSUS_INCOMPLETE), no truncation success |
| T51 | Unknown/low free bytes after fresh walk | H(P5_FREE_BYTES_LOW) |
| T52 | Owned date unsettled, unreaped, nonempty group, EOF false, term1 or bad text | H(P5_OWNED_DATE_FAILED), recorded_at null, never fabricated |
| T53 | read_bytes Exception at GO, deadline still passes | H(P1_GO_INVALID); callback primary event retained; other independent parts run |
| T54 | census RuntimeError, deadline still passes | H(P4_CENSUS_FAILED); other independent part5 still runs |
| T55 | owned_date RuntimeError, deadline still passes | H(P5_OWNED_DATE_FAILED), null date |
| T56 | Reader GO RuntimeError then original deadline raises | HELD exact P1_GO_INVALID+P1_DEADLINE, primary+secondary events retained; no later callback/I/O, no disposition/registry |
| T57 | Census RuntimeError then original deadline raises | HELD exact P4_CENSUS_FAILED+P4_DEADLINE; no part5/date/commit I/O |
| T58 | Date RuntimeError then original deadline raises | HELD P5_OWNED_DATE_FAILED+P5_DEADLINE; no commit I/O |
| T59 | Successful read/census/date/native chunk returns after deadline | HELD Pn_DEADLINE for its stage; no new I/O after detection; partial evidence preserved |
| T60 | Initial check or after complete decision assembly crosses | HELD P1_DEADLINE / P5_DEADLINE respectively; no disposition/registry |
| T61 | Exclusive O_EXCL file already exists / disposition write/fsync failure | HELD P5_COMMIT_WRITE_FAILED; ACK_NOT_ATTEMPTED, no registry, prior/partial object unchanged |
| T62 | Late exclusive open returns FD then post-open check crosses | HELD P5_DEADLINE; only owned FD cleanup; possible empty exclusive file preserved, created:false is not proof of absence |
| T63 | ACK callback wrong bytes/type/hash or replacement inode | HELD P5_ACK_FAILED, ACK_FAILED, registry NOT_ATTEMPTED |
| T64 | ACK callback Exception then deadline still passes / also crosses | HELD P5_ACK_FAILED / P5_ACK_FAILED+P5_DEADLINE_AFTER_ACK; no registry; primary+secondary events retained |
| T65 | ACK returns after deadline or inode-check completion late | HELD P5_DEADLINE_AFTER_ACK, ACK_UNPROVED_DEADLINE, no append |
| T66 | Registry append open/write failure | HELD P5_REGISTRY_APPEND_FAILED; ACK_OK; zero/partial append preserved, no retry |
| T67 | Registry full line written then fsync fails | HELD P5_REGISTRY_APPEND_FAILED; line_complete true, fsync false; visible RELEASED line not authority |
| T68 | Registry fsync succeeds, close fails | HELD P5_REGISTRY_APPEND_FAILED; fsync true/closed false; visible RELEASED line not authority |
| T69 | Final deadline crosses after registry write/fsync/close | HELD P5_DEADLINE_AFTER_ACK; APPENDED/fsync/closed may true; caller never observed RELEASED |
| T70 | Outside-aifours commit_dir / registry_path (also prefix-confusable aifours-evil) | HELD P5_COMMIT_DIR_INVALID / P1_ALLOCATION_INVALID; forbidden target receives no mutation |
| T71 | Callback BaseException from reader/date/deadline | Original exception propagates, no unsafe HELD commit/new allowance; parent_release_result when available, reservation HELD |
| T72 | Census BaseException with original deadline/reader/date safe | Attempt one original-deadline HELD record/ACK/HELD line, then re-raise original with result attached; remaining parts NOT_EVALUATED |
| T73 | BaseException during exclusive write/ACK/registry | Immediate propagation, no second record attempt; partial objects/line preserved; caller keeps HELD |
| T74 | Primary callback Exception + secondary deadline BaseException | Secondary propagates with primary context and both bounded events; no unsafe I/O |
| T75 | Multiple independent defects GO digest + stdout digest + oracle verdict + incomplete census + undeclared changed file | HELD exact P1_GO_INVALID,P2_CAPTURE_STDOUT_INVALID,P3_ORACLE_VERDICT,P4_CENSUS_INCOMPLETE,P5_LATE_UNDECLARED_CHANGED, unique frozen order |
| T76 | Spec cycles/non-JSON types/too many nodes/oversize representation | HELD/P1_SPEC_INVALID plus owning missing-field causes as source dictates; no successful release from partial typed defaults |

These are source-derived required expectations, **not observed output**. A later runner must freeze exact isolated fixture causes (including deliberate dependency effects), independently retain actual native results and compare them without broadening expected sets to absorb unrelated failures. CP1/CP2, raw supervisor finite matrices, beta X1–X7/X5 integration and genuine N1 cases remain separately admitted work; none are discharged by these proposed controls.
