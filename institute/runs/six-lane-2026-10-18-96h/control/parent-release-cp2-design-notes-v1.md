# Parent release CP2 — historical identity union + fresh census, source v1 — NOEXEC

Actual `/bin/date` before this write: `2026-10-19T16:51:13-0700`.

Source `RUN/control/parent_release_identity_v1.py`: SHA-256 `d07548e2dbff4ef6b64a3a902d3b59ed7c4abbf8dc2115e8b08ed37ee2ec14d5`, 1548 lines, 81805 bytes, ASCII. Design frozen before code: `RUN/control/parent-release-cp2-design-freeze-v1.json` `3d6f48ced0d07293a81f44936c3559571e4d4f98919c024a257f32761a7af027`. Authority: CP2 scope `RUN/control/parent-release-cp1-cp2-implementation-scope-v1.json` `1f717bf944e6d5a524aa0a65776d39726cd251bcd006971ba322f328de6bd314`; obligations from PRT v2 notes lines 11/27/51 (`9e02abce…b7b`) and review line 88 (`935b74fb…5ad`).

**Status: NOEXEC source candidate.** Not source-accepted, not qualified, not complete CP2, no runtime/release/signal/scheduling/science authority. **No import, compile, AST parse, test, helper, fixture, census, model CLI or other execution occurred.** Evidence is source reading, hashes, byte/line metadata and a static grep audit of this file (no `os.kill`/`killpg`/`posix_spawn`/`subprocess`/fork/`waitpid`/`open`/write call; `ctypes.CDLL` only inside `_bind_libproc`; clocks only `time.monotonic`/`time.sleep` inside the census callback; import time = constants, definitions, `frozenset`, `object()`).

Self-review finding **SR-1 (MAJOR, unrepaired in v1)**: pid-only unknown incarnations are closed by H7 instead of HELD (see §9). A narrow successor was requested from the parent; v1 is immutable.

## 1. Reused supervisor19 semantics (no second convention)

Pinned producer `RQ/code/owned_supervisor_v19.py` `cb828a78367dc2023bfc6e330696745f186f186811752361472747e5fe547e93` (SOURCE_READY_RUNTIME_HOLD, readiness `558f9ba3…6ce96`; interface v17 `089ae87c…`, v18 `ceeca0a9…`, v19 `75ee7c21…`). CP2 re-implements the identical native table in-module rather than importing the subject (an import would execute `CDLL` loading and module-global PID capture and bind a subject):

| CP2 | sv19 lines | Exact semantics |
|---|---|---|
| `_bind_libproc` | 169-173 | `/usr/lib/libproc.dylib`, `proc_pidinfo(int,int,uint64,void*,int)->int`, `proc_listallpids(void*,int)->int`; bound lazily per `make_census`, never at import |
| `_pidinfo` | 202-208 | zombies flag 1 where sv19 uses it; return must equal the requested size else `_NativeError(OSError)` |
| `_unique` | 211-213 | flavor 17, 56 bytes: `uniqueid '=Q'@16`, `idversion '=i'@32` |
| `_short_info` | 216-222 | flavor 13, 64 bytes: `pid,ppid,pgid,status '=IIII'@0`, `comm[16:32]` utf-8 replace, `flags,uid '=II'@32` (`euid`=pbsi_uid), `ruid '=I'@44`, `traced=flags&2` |
| `_identify` | 234-242 | unique, short, unique, short, unique; uniqueid/idversion stable and sv19 fingerprint `(pid,uniqueid,idversion,euid,ruid,ppid,pgid,traced)` equal else failure |
| `_all_pids` | 292-310 | sizing call; cap=`count*2+1024`, 4 doublings; negative/duplicate => malformed; pid 0 dropped; original deadline after every native list call |
| attempts | 1367-1383 | up to 3 fresh full attempts per call, 0.05 s pause, no stitching |

## 2. One start-fingerprint convention

`start_fingerprint = 'sv19-incarnation-v1:%d:%d:%d' % (pid, uniqueid, idversion)` — exact sv19 integers (u32, u64, i32), canonical decimal (parser rejects signs except idversion `-`, leading zeros, non-ASCII digits, non-canonical text). It names one exec-image incarnation (XNU changes idversion on exec). ppid/pgid/euid/ruid/traced/comm are mutable **variant history**, not start identity.

Used identically by: CP2 census rows; CP2 PRT identity rows; **required** of the parent launch record `driver` and the parent wait records (`parent-release-wait-v1`); recommended for PRT `owned_date.child.start_fingerprint`. A parent producer obtains it by taking a separate `make_census()` snapshot after `posix_spawn` returns and before its first `waitpid`, and copying the row for the child pid (never reusing that factory/log for release). The same pid with a different fingerprint is **ambiguous, never endedness proof** (scope hard limit).

## 3. API and exact contracts

- `start_fingerprint(pid, uniqueid, idversion) -> str` (pure).
- `build_identity_union(request, read_bytes, deadline_check) -> dict` format `parent-release-identity-union-v1`. Never raises `Exception` (HELD report); `BaseException` propagates with `exc.parent_release_identity_partial`. No clock, write, process, signal or descriptor; all bytes via parent `read_bytes`.
- `make_census(deadline_check) -> (census, log)`. `census()` returns PRT-exact `{complete:bool, processes:[{pid,ppid,pgid,uid,start_fingerprint}], observed_at_mono:float}` (`uid`=euid). Raises on deadline, listing failure, non-finite clock, process cap or log cap; identification gaps give `complete:false`. `log` is `CensusLog`: `served_count()` (exact int), `served` (records with full raw identities, `served_sha256` of the exact returned dict), `attempts`, `refusals`, `summary()`.
- `evaluate_endedness(union, log, deadline_check) -> dict` format `parent-release-identity-endedness-v1`, keys used by CP1: `format`, `state` (`ENDED_CONDITIONAL`|`HELD`), `causes` (ordered, `[]` iff ENDED), `union_sha256` (echo or null), `endedness_sha256` (canonical digest without itself). Never raises `Exception`.
- `spec_identities_match(union, identities) -> bool`.
- `deadline_check` is always the caller's ORIGINAL nonrenewing predicate: union start, before and after every `read_bytes` (success or Exception), after result assembly (rebuild as HELD, no I/O); census start, observer bracket, after pid sizing/list, after every identification success or failure, around the retry pause, before return; endedness start and after assembly. Non-None return = crossed. Late success is never accepted.

Request (exact keys, bounded detach ≤4096 nodes/depth 8/64 KiB, JSON scalars only, no floats):
`{format:'parent-release-identity-request-v1', item:str1..512, histories:[1..16 × {family:'main'|'oracle', producer:ref, wait_record:ref, launch_record:ref|null, stdout:capture, receipt:ref|null, settlement:ref|null}]}`; `ref={path,sha256}`; `capture` = PRT capture shape with `eof:true, overflow:false, error:null, seen==stored<=16MiB`. Exactly one `main` (launch_record required), ≥1 `oracle` (launch_record null in v1). ACK line ⇒ receipt+settlement required; refusal line ⇒ both null.

**CP1 join** (ParentCallerCP1 `RUN/control/parent_release_caller_v1.py` `4072c50ef5be021a22e72a43571550c1338ab8a4d243752d88e3b7cc71a75cae` uses exactly these names): union `state=='CLOSED_CONDITIONAL'`, `prt_identities` typed-equal spec.identities, the PRT census argument is this `census`, `served_count()` +1 across the PRT call, then `evaluate_endedness(detached union, log, deadline)` ENDED with `causes==[]` and echoed `union_sha256`. Use a fresh `make_census()` per transaction: endedness evaluates **every** served snapshot in the log. The union's canonical bytes must fit CP1 SPEC_CAP 4 MiB (larger unions are HELD by CP1, fail-closed).

## 4. Origin boundary (what bytes are bound to what)

Per history: producer bytes == pinned sv19 digest; wait record exact keys/role/item, `waitstatus_to_exitcode(raw_status)==actual_exit`, canonical fingerprint; main launch `item` and `driver` typed-equal the wait identity; complete stdout capture bytes/length/hash; exactly one LF-terminated ASCII JSON line whose bytes equal the exact sv19 serialization (ACK `sort_keys,(',',':')`; refusal insertion order `(',',':')`); `supervisor=='owned_supervisor_v19'`; ACK keys exact (24), refusal keys within the 7 refuse() site sets; parent exit == line `exit_code`; ACK: receipt/settlement digests and byte counts equal the ACK, both equal exact `bytes_json` serialization, settlement receipt path/digest/config/state agree, receipt `supervisor_sha256==cb828a78`, receipt history fields are typed prefixes (events, censuses, coverage, owned) or order/variant prefixes (identity/unproved history) of the ACK reconciliation, helpers/main_wait/raw/overflow/timing typed-equal. These bind selected bytes across two producer representations (published file vs parent-captured stdout); **they do not authenticate origin** — condition `PARENT_OBSERVATION_AUTHENTICITY`.

## 5. Identity boundary (union)

Members per history = `(identity_history uids \ baseline) ∪ owned uids ∪ {bound driver uid}`; all variants retained (pids, pgids, ppids, idversions, euids, ruids, comms, event refs, first source). Roles: main `driver|main_child|helper|descendant|unproved`, oracle `oracle|oracle_child|oracle_helper|descendant|unproved`; precedence driver > child > helper (owned via helper or helper-report identity) > descendant (owned_group/current_parent) > unproved (all other non-baseline uids, including first-seen-unproved-then-owned, pre-baseline transients and invalid-helper identities). PRT rows: one per (member, distinct idversion), pgid = last_identity pgid for its idversion else last variant with it, `source='sv19:<family>#<i>:<first category>:uid=<u>'`; cross-family dedupe by (pid, fingerprint) with `ROLE_PRIORITY`; driver/oracle collision HELD; exactly one driver, ≥1 oracle, positive pid/pgid, ≤200000. `historical_pgids` = every variant pgid of every member (covers pgids that one-pgid PRT rows cannot carry); `historical_pids` = member pids. Pid-only unknown incarnations (coverage gaps, identity-less helper/main spawns, pending raw, overflow observations) are listed in `unknown_incarnations`, never given fingerprints.

## 6. Endedness boundary

**H7 closure** (per history): the LAST census record L is complete, not aborted, `incomplete_n==0`, and has empty `owned_live/unproved_live/owned_event_refs/unproved_event_refs/group_live/owned_zombies`; ACK `ack_census` typed-equals L; events with interval inside `[L.mono_start, L.mono_complete]` have exactly `L.pids` distinct uids, all baseline and none flagged unproved; no event straddles the window or begins after it; every helper spawn (`mono_spawn`) and the main spawn (receipt `mono_spawn`, or for refusals an earlier main-identity event) precede `L.mono_start`. Soundness: B is a complete scan before any spawn; run-owned processes have non-baseline uniqueids; at L's single-call listing every live process was identified as baseline, so no run-owned process existed then and none can descend afterwards; the supervisor spawns nothing after L. The fresh CP2 census then checks (defense in depth, and PRT part4) that no member uniqueid is alive, no member pid is reused (ambiguous), no historical variant pgid is occupied and no process has a historical pid as ppid, for every served snapshot.

Named residual conditions in every report: `PARENT_OBSERVATION_AUTHENTICITY`, `PARENT_DIRECT_LAUNCH` (direct posix_spawn, own new group, no intermediate process), `SUPERVISOR19_QUALIFICATION` (package v9/original22/finite matrix unexercised), `NON_DESCENDANT_CHANNELS` (launchd/XPC/at/cron), `PUBLICATION_FREEZE`, `CP1_JOIN`. A JSON `complete:true`, a currently empty tree/group (registry rows `census:'empty'`) or a digest alone is never accepted.

## 7. Exact coverage map from producer histories (sv19 → CP2)

| sv19 field (ACK reconciliation unless noted) | CP2 use | Check | Cause on failure |
|---|---|---|---|
| stdout line (ACK/refusal) | origin of history | exact one-line serialization, keys, version, exit | U_OUTPUT_LINE_INVALID / U_PRODUCER_UNSUPPORTED / U_EXIT_BINDING |
| receipt (`s.rec`), settlement | prefix binding, baseline identities, `supervisor_pid`, `mono_spawn` | digests, bytes_json, prefix/equality | U_RECEIPT_BINDING |
| `timing_failed`, `history_halted`, `history_overflow`, `raw_acquisitions` | completeness | false/false/null/[] | U_HISTORY_INCOMPLETE (+ unknown rows) |
| `identity_events` | raw acquisition tape | 6-tuple types, uid/variant exist, counts | U_EVENT_TAPE_INCONSISTENT |
| `identity_history` | member variants, first source | exact keys, ≤64 distinct forms of one pid/uid, first/last = min/max end events, intervals, status, source ∈ 12 sv19 acquisition sites | U_EVENT_TAPE_INCONSISTENT |
| `baseline_uniqueids` (+ receipt `baseline`) | exclusion set, driver | sorted unique nonempty ⊆ history; receipt identities/refs agree | U_BASELINE_INVALID |
| `owned_identities` | child/helper/descendant roles, escaped/reparented ownership | ref denotes identity; via grammar; roots; current-parent edge proof refs (parent,child,parent) | U_OWNED_REGISTRY_INCONSISTENT |
| `unproved_history` | unproved members | uid non-baseline; first/last = extreme unproved-flagged events; set == flagged uids | U_UNPROVED_INCONSISTENT |
| `census_observations` | live sets, last census L | keys ⊆ allowed, live identities/refs consistent | U_HISTORY_SCHEMA, U_LAST_CENSUS_OPEN, U_LAST_CENSUS_TAPE_MISMATCH |
| `coverage_history` | pid-only unknowns | entry/observation shape | U_HISTORY_SCHEMA (closure: SR-1) |
| `helpers` (helper_reports) | helper roles, identity-less helpers, spawn chronology | exact 44 keys, identity pid/uid/ref | U_HISTORY_SCHEMA, U_CHILD_HELPER_UNBOUND, U_SPAWN_CHRONOLOGY |
| `main_identity`, `main_wait` (+ receipt `child_identity/child_pid`) | main child | own group, owned child registration | U_CHILD_HELPER_UNBOUND |
| parent wait/launch records | driver/oracle binding | baseline self-observation, uid/idversion/pgid, own group | U_WAIT_INVALID / U_LAUNCH_INVALID / U_DRIVER_UNBOUND |
| `main_signal`, `helper_log`, `failures`, `observation_attempts`, resource fields | not consumed (signal identities enter via events) | — | owned by RQLS10 package-v9 consumer obligations |

## 8. Census callback and owned helper lifecycle

In-process libproc only: **no helper process, no signal, no SIGKILL, no timeout wrapper, no cache**. Observer bracket: own pid identified before listing and after the last identification; the row for own pid must exist with the same sv19 fingerprint, else the attempt is incomplete. Every attempt summary (listed, identified, missing sample ≤64, rows digest) and every served snapshot is retained; ≤16 served/≤64 attempts, beyond which the callback refuses instead of discarding evidence. Any future helper-based census must be separately admitted and own its lifecycle like PRT `owned_date`: original pre-spawn deadline, own group, full identity/group/descendant/EOF proof and at most one identity-checked SIGTERM.

## 9. Self-review findings and availability consequences

- **SR-1 MAJOR (unrepaired):** v1 closes pid-only unknown incarnations (coverage-gap pids, identity-less helper or main spawn records) by H7 + spawn chronology, recording `closure:'H7_CLOSED'`, instead of HELD. Scope says gaps/uncertain incarnations ⇒ HELD and the beta bridge treats them as sticky. Narrow successor: fire a new cause (e.g. `U_UNKNOWN_INCARNATION`) for every unknown row. Parent decision requested.
- **SR-2 MINOR:** union/receipt canonical re-serialization assumes no int-keyed dicts in sv19 output (none found by source reading); a genuine positive failing only there is a v1 defect, never a waiver.
- **SR-3 note:** endedness covers all served snapshots of a log (stricter); CP1 must use a fresh factory per transaction.
- **Availability (not weakened):** sv19 makes every post-baseline process unproved, so H7 needs a final census with zero post-baseline live processes anywhere on the host; concurrent lanes or parent tooling started after the baseline make the history open (U_LAST_CENSUS_OPEN). Endedness and PRT part4 HOLD on any reused member pid or occupied historical pgid (e.g. a parent shell group shared by an unproved transient). Expected practical result on a busy shared host is HELD; release needs a quiescent host or a separately reviewed ancestry/containment design.

## 10. Unfulfilled prerequisites / producer interface gaps

1. Parent launch record `driver` and parent wait records in the `sv19-incarnation-v1` convention (none exist yet).
2. Complete parent outer stdout capture of each supervisor (exact one line).
3. Oracle executed under owned_supervisor_v19 (any other oracle driver ⇒ U_PRODUCER_UNSUPPORTED).
4. For open histories: a governed continuation history in the same convention, or a rerun whose final census closes.
5. sv19 package/finite qualification; parent observation authenticity and publication freeze; CP1 caller join (implemented by CP1, unqualified).

## 11. Finite controls — frozen expectations, NOT exercised

Separately admitted later, isolated fixtures, exact pins; synthetic fixtures (S) prove predicates only; native cases (N) need a parent GO. Unless stated, all other fields are a valid closed fixture. Union causes are exact sets.

| ID | Case | Expected |
|---|---|---|
| C01 N | quiescent host: main + oracle sv19 SETTLED exit0, scheme launch/wait, complete captures | union CLOSED_CONDITIONAL, causes [], 1 driver + ≥1 oracle row; endedness ENDED unless the retained snapshot shows reuse/occupancy, then exactly those E causes (recomputable from log rows) |
| C02 S | refusal PUBLICATION_REFUSED exit12, clean final census, receipt/settlement null | CLOSED_CONDITIONAL |
| C03 N/S | ACK exit11 with unproved_live at ACK census | [U_LAST_CENSUS_OPEN] |
| C04 S | ACK line exit0, parent actual_exit 14 | [U_EXIT_BINDING] |
| C05 S | wait+launch fingerprint idversion differs from self-observation | [U_DRIVER_UNBOUND] |
| C06 S | wait fingerprint with leading zero | [U_WAIT_INVALID] |
| C07 S | launch.driver pgid differs from wait | [U_LAUNCH_INVALID] |
| C08 S | producer ref digest ≠ cb828a78 | [U_PRODUCER_PIN] |
| C09 S | stdout capture eof false | [U_REQUEST_INVALID] |
| C10 S | stdout bytes digest mismatch | [U_CAPTURE_INVALID] |
| C11 S | stdout two lines | [U_OUTPUT_LINE_INVALID] |
| C12 S | ACK line re-serialized with spaces | [U_OUTPUT_LINE_INVALID] |
| C13 S | supervisor 'owned_supervisor_v18' | [U_PRODUCER_UNSUPPORTED] |
| C14 S | receipt digest ≠ ACK receipt_sha256 | [U_RECEIPT_BINDING] |
| C15 S | receipt not bytes_json (indent 2), digests consistent | [U_RECEIPT_BINDING] |
| C16 S | receipt non-baseline event altered (not ACK prefix) | [U_RECEIPT_BINDING] |
| C17 S | refusal with timing_failed true, clean L | [U_HISTORY_INCOMPLETE] |
| C18 S | refusal with one raw pending acquisition | [U_HISTORY_INCOMPLETE], unknown raw_pending_acquisition |
| C19 S | history_halted true | [U_HISTORY_INCOMPLETE] |
| C20 S | one event uid altered | [U_EVENT_TAPE_INCONSISTENT] (dependent checks skipped) |
| C21 S | observations off by one | [U_EVENT_TAPE_INCONSISTENT] |
| C22 S | current_parent edge proof ref to wrong uid | [U_OWNED_REGISTRY_INCONSISTENT] |
| C23 S | owned_group root not child/helper | [U_OWNED_REGISTRY_INCONSISTENT] |
| C24 S | flagged event without unproved_history entry | [U_UNPROVED_INCONSISTENT] |
| C25 S | baseline_uniqueids unsorted | [U_BASELINE_INVALID] |
| C26 S | driver launched in parent group (pgid≠pid) | [U_DRIVER_UNBOUND] |
| C27 S | two history uids with the waited pid | [U_DRIVER_UNBOUND] |
| C28 S | main_identity ≠ owned child registration | [U_CHILD_HELPER_UNBOUND] |
| C29 S | L complete but group_live nonempty | [U_LAST_CENSUS_OPEN] |
| C30 S | L.pids = window distinct uids + 1 | [U_LAST_CENSUS_TAPE_MISMATCH] |
| C31 S | unflagged post-baseline event inside L | [U_LAST_CENSUS_TAPE_MISMATCH] |
| C32 S | event beginning after L | [U_LAST_CENSUS_TAPE_MISMATCH] |
| C33 S | helper mono_spawn ≥ L.mono_start | [U_SPAWN_CHRONOLOGY] |
| C34 S | identity-less helper spawned before clean L | v1: CLOSED_CONDITIONAL with unknown closure H7_CLOSED (SR-1; successor: HELD) |
| C35 S | no oracle history | [U_FAMILY_INVALID, U_ROW_CONFLICT] |
| C36 S | two main histories | [U_FAMILY_INVALID, U_ROW_CONFLICT] |
| C37 S | oracle launch_record non-null | [U_FAMILY_INVALID] |
| C38 S | refusal with receipt ref | [U_RECEIPT_BINDING] |
| C39 S | read_bytes RuntimeError at wait, deadline passes | [U_WAIT_INVALID]; EXCEPTION event retained |
| C40 S | read_bytes RuntimeError then deadline raises | [U_WAIT_INVALID, U_DEADLINE]; no later read |
| C41 S | deadline_check returns non-None at start | [U_DEADLINE]; zero reads |
| C42 S | deadline crosses only at final assembly | report rebuilt HELD [U_DEADLINE] (+ none other) |
| C43 S | read_bytes KeyboardInterrupt | propagates; `parent_release_identity_partial` attached |
| C44 S | request with float / cycle / 4097 nodes | [U_REQUEST_INVALID] |
| K01 N | admitted native census on host | complete true, observer_ok, PRT `_take_census` accepts, canonical fingerprints |
| K02 S | identify ESRCH for one pid in 3 attempts | served complete false, attempts 3 |
| K03 S | attempt1 gap, attempt2 complete | served complete true, attempts 2, both summaries retained |
| K04 S | deadline Exception after pid list | that Exception propagates; refusals +1; served_count unchanged |
| K05 S | deadline returns non-None | CensusRefusal; not served |
| K06 S | deadline BaseException | propagates; refusals records type |
| K07 S | listing never fits (overflow) | `_NativeError` PID_LIST_OVERFLOW raised |
| K08 S | observer fingerprint changes | complete false, observer_ok false |
| K09 S | 17th served call | CensusRefusal |
| E01 S | union HELD | [E_UNION_HELD] |
| E02 S | union mutated after digest | [E_UNION_DIGEST] |
| E03 S | empty log | [E_NO_SERVED_CENSUS] |
| E04 S | served complete false | [E_CENSUS_INCOMPLETE] |
| E05 S | member alive, same pgid | [E_MEMBER_ALIVE, E_GROUP_NONEMPTY] |
| E06 S | member pid reused, other pgid/ppid | [E_PID_REUSE_AMBIGUOUS] |
| E07 S | unrelated process in a variant-only historical pgid (absent from PRT rows) | [E_GROUP_NONEMPTY] — CP2 covers what PRT rows cannot |
| E08 S | unrelated process with ppid = historical pid | [E_PID_CHILD_PRESENT] |
| E09 S | deadline crosses at start / at end | [E_DEADLINE] (+ retained others at end) |
| E10 S | two snapshots, first shows member alive | [E_MEMBER_ALIVE] |
| N01 N | child double-forks setsid escapee outliving ACK | sv19 UNSETTLED; union [U_LAST_CENSUS_OPEN]; endedness E_UNION_HELD + E_MEMBER_ALIVE |
| N02 N | escapee ends before final census | union CLOSED with escapee member variants; endedness per C01 rule |
| N03 N | reparented child (ppid→1) ending before final census | CLOSED; member has two ppid variants |

Also PRT T36 (omitted reparented identity): CP1 typed equality of spec.identities with `prt_identities` refuses; CP2 evaluation still covers the member.
