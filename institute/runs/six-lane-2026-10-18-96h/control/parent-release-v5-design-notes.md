# Parent release transaction v5 — scoped repair, NOEXEC

Actual `/bin/date` before this write: `2026-10-19T18:37:17-0700`.

Source `RUN/control/parent_release_v5.py`: SHA256 `82feb74cd1cc7b0c69d5e4e1b3ca447250609735485a901240e0247566acd8cd`, 1838 lines, 86795 bytes. Exact `/usr/bin/diff -u -L control/parent_release_v4.py -L control/parent_release_v5.py` stream and file `RUN/review/parent_release_v4_to_v5.diff`: `35dd41531f5fa9dcc779e5e151b43ad61ace805de49ba79e496090c889197b27`, 747 lines, 35183 bytes.

Governing: base `4d122872…`; scopes v2 `2fdf13b4…`, v3 `1f9befdb…`, v4 `32d161b0…`; v5 `control/parent-release-v5-repair-scope-v1.json` `ef0ab41a6e6e5ec2357f2f5022a611e99f1e4d4a05ab2001699572232e6fb2f3`; v4 Codex HOLD 0 FATAL/3 MAJOR/2 MINOR `b38745818f96a032106eea3da675a40adf640d19c483c83dac64691f7228a8e8`. Plan frozen before source in checkpoint010 `16fefc3719404595d6aa13d1fe586224de31b1aaeb5382fcaca308305905166f`, amended by checkpoint011 `ae1306a14e8d7ec4374c0ca91e8c856a3316bacd3b847e4415efea17c829313b` (helper retention).

**SOURCE ONLY, UNTESTED.** No execution, import, compile, AST, fixture, test, lint, runtime or model CLI. V1–v4 remain immutable HOLD. No source-readiness, runtime, reservation-release or scientific authority. Global HOLD remains.

## Supersessions and interfaces

V2 notes `9e02abce…`, amended by v3 `7a9fcdca…` and v4 `e29e719a…`, govern only as amended here. This document wins on conflict. V4's claims that its shaping rule covered caught field errors, its cleanup retained every exception, and `_absorb` never raised were rejected by the v4 review; they are not accepted facts.

- Result `parent-release-result-v5`; disposition `parent-release-disposition-v5`, module `parent_release_v5.py`, file `prt-v5-<slug>-<sha256>.json`; registry `parent-release-registry-v5`, owner `parent_release_v5.py`. `_held_for` accepts only v5 HELD rows for the same allocation. No prior version ran, so no compatibility branch.
- Disposition `repair_scope_sha256s` = `[2fdf13b4…, 1f9befdb…, 32d161b0…, ef0ab41a6e6e5ec2357f2f5022a611e99f1e4d4a05ab2001699572232e6fb2f3]`.
- No result (22 keys), disposition, registry or resources **key-set** change from v4. No ack/status/final_deadline_check vocabulary change. Spec, wait-v1 and late-baseline-v2 unchanged. No old-version import, alias or shim.
- `parent_release_result` stays pure JSON: dict/list/str/int/bool/None (no exception object). Retained objects exist only in the transaction's private list and the separate `parent_release_prior_exceptions` tuple, not evidence/events/resources/result/disposition/registry.
- **CP1 must not repin until Main accepts a source.** Effective release requires caller-observed returned `state:'RELEASED'` AND `final_deadline_check:'PASSED'`, ACK_OK, APPENDED/RELEASED/fsync/clean closes and no live/unresolved resource. No disk syntax is authority.

## Finding map and mechanisms

| Finding | Frozen repair | v5 anchors |
|---|---|---|
| M1 ANY shaping failure still enabled commit | Fresh transaction's `fired` set is a permanent shaping-failure latch. Sole destination assignment occurs only at the last shaping statement, after independent exclusion succeeds, and only if no cause fired. Escaping Exception/BaseException never reaches it. All caught shaping failures fire: callback validity, commit_dir, spec, field validators, capture keys/duplicates, oracle keys and independent exclusion | `_shape:713-769`, sole assignment 769; `_shape_field`, `_shape_captures`; `_commit:1540-1543` |
| M2 cleanup lost objects and propagated oldest | `_Txn.keep` identity-deduplicates original **non-Exception BaseExceptions** in first-encounter order. Every origin/handler retains before description or cleanup. Every finally-owned region has an in-flight catch/keep/re-raise. `release` attempts all closes once, raises newest non-Exception BaseException among close failures, or newest ordinary escaping Exception if none; ordinary cleanup cannot hide a retained interrupt. Phase boundaries and final selection use retained objects rather than an older pending variable | `keep:305-310`; call/tick/observe/failed/native; open/close/release/directory; nine cleanup regions; `_absorb:1710-1720`; `decide_and_commit:1770-1805` |
| M3 overridable context/setattr escaped bookkeeping | Base descriptors `_CONTEXT`, `_EXC_DICT`, `_TYPE_NAME`; real-type `issubclass(type(exc), Exception)` instead of overridable `isinstance`. `_link` is optional, guarded by BaseException, free-slot only, 64-step acyclic walk. `why` retains failures from description, coerces to exact str, never invokes the failed object's code recursively while recording it. Attachment uses the base instance dict and `dict.__setitem__`, no setattr/object.__setattr__ | constants 90-92; `_ordinary:116-117`, `_type_name:120-121`; `why:312-322`; `_link:1690-1707`; `_attach_and_raise:1727-1752` |
| m4 wrong ACK token in T121 | Re-frozen below: ACK_NOT_ATTEMPTED, registry NOT_ATTEMPTED unchanged | `_new_result:1640-1647` |
| m5 helper generated paths its consumer refused | `_parts(full)` runs immediately after path construction, **before** lstat/hash/insertion/descent. The complete walk is refused, never truncated. Same predicate as the baseline consumer | `_scan:1204`; `_baseline:1298`; helper 1808-1838 |

**Retention meaning.** Ordinary Exceptions retain the original failure semantics (owning cause/primary event, not normally propagated). The BaseException-retention promise concerns non-Exception objects such as KeyboardInterrupt, SystemExit and GeneratorExit. Each first retention adds `Pn_BASE_EXCEPTION` evidence `retained at encounter: <type>` using no object-supplied description; boundary absorption adds its bounded stage/description. Causes remain unique/in CAUSES order. Repeated propagation of the identical object does not duplicate it in the ledger. Newest means the last distinct object first encountered; the prior tuple excludes that identity and is oldest-first.

**Cleanup sites.** In-flight objects are retained before finally in `_names`, `_artifacts`, `_hash_file`, `_scan` child, `_walk`, `_free_bytes`, `_write_new`, `_commit`, `_append_registry`, and before cleanup in `open`/`directory`. Destructive close pops the owned record before its one attempt. `unresolved_total` records every unresolved close; a description is not used as a substitute for retaining the actual exception object.

**Attachment, exact answers for CP1.** `_EXC_DICT = BaseException.__dict__['__dict__']`; namespace = `_EXC_DICT.__get__(exc)`; writes use `dict.__setitem__`. `parent_release_prior_exceptions` is a plain tuple of the original objects, excluding the propagated identity, oldest first. The selected exception is not wrapped/replaced. `__context__` is only a best-effort extra: existing context is not overwritten, cycles refused, and Python may rewrite context when raising inside an active handler (including a caller's). CP1 reads the same base instance dict, never getattr.

The attachment loop has at most eight rounds. Each round re-finalizes the pure-JSON HELD report, selects the newest retained exception, writes priors then result. A newly raised non-Exception BaseException during linking/attachment is retained, fires its phase's BASE_EXCEPTION and causes reselection. An ordinary bookkeeping Exception fires INTERNAL_ERROR evidence (P5 for attachment). Retry refreshes the report. If all eight rounds fail, the newest retained original still propagates without guaranteed attributes; any reachable report/evidence records the failure, but there is no guaranteed channel if attachment never succeeds. CP1 must permanently block on unknown PRT resource state in that case. No extra I/O or normal return.

Checkpoint011 extends this to `build_late_baseline`: shared cleanup retains objects; on a non-Exception failure the same attachment/selection loop runs with ctx=None/result=None, attaching **priors only**, never a release report. Ordinary failure/deadline refusal behaviour is unchanged when no non-Exception object was retained.

## Control amendments — authored, NOT exercised

Separate GO, isolated exclusive fixture paths, exact pins, labelled synthetic fault injection, no OS-provenance claim. Every row is otherwise positive and pins/baseline/allowed directory metadata repaired to isolate exactly the named defect. H(c) denotes returned/attached HELD with exactly the listed causes in CAUSES order. Never widen sets after seeing output.

**M1 convention overrides old H(c) commits:** any shaping failure means `disposition:null`, `ack:'ACK_NOT_ATTEMPTED'`, registry `NOT_ATTEMPTED`, no disposition/ACK/registry I/O, regardless of an independently valid destination outside job_dir. Evaluation reads still run, and commit-safe owned_date still runs once (unused). Ordinary paths end with `final_deadline_check:'PASSED'` if the original check passes. Do not describe this as no I/O anywhere: it forbids commit I/O, not evaluation reads/native walks/date callback.

| Existing row | Re-frozen v5 expectation |
|---|---|
| T12 | actual_exit bool/float → in-memory H(P2_EXIT_INVALID); no bool0 alias |
| T14 | stdout record shape/completeness invalid → in-memory H(P2_CAPTURE_STDOUT_INVALID) |
| T21 | >16MiB part2 artifact → in-memory H(P2_ARTIFACTS_INVALID); no partial read |
| T23 | oracle actual_exit1/boolFalse → in-memory H(P3_ORACLE_EXIT) |
| T37 | exact RUN_ROOT omitted → in-memory H(P5_LATE_AUDIT_INVALID); part5 blocked |
| T70 | outside-aifours commit_dir → in-memory H(P5_COMMIT_DIR_INVALID); registry_path variant → in-memory H(P1_ALLOCATION_INVALID); neither writes even to an otherwise valid destination |
| T76, T103–T105 | remain in-memory HELD with the previous causes; exclusion still checked independently even after another shape error |
| T112, T113, T120 | Prior tuple retention is unconditional on context availability; their __context__ assertions assume no caller-active exception handler, use the BASE context descriptor, and are best-effort interpreter behaviour, not the retention channel |
| T121 | Every ordinary (non-BaseException) T01–T132 outcome: ack ∈ {ACK_NOT_ATTEMPTED, ACK_OK, ACK_FAILED, ACK_UNPROVED_DEADLINE}; status ∈ {NOT_ATTEMPTED, APPENDED, DEADLINE_CROSSED, FAILED}. ACK_ATTEMPTED/ATTEMPTED survive only on attached BaseException reports. Positives T01/T77 unchanged |

T68, T98-part2/part5, T81/T82, T99–T101 and T109–T120 otherwise stand as re-frozen by v4 notes (with v5 names). In particular T68 is APPENDED/fsync:true/closed:false, H(P5_REGISTRY_APPEND_FAILED), unresolved_total:1, final PASSED; T98-part2 causes exactly [P2_ARTIFACT_SET_MISMATCH,P2_ARTIFACT_IDENTITY], part5 exactly [P5_LATE_CENSUS_INCOMPLETE].

| New ID | Isolated synthetic case | Exact expected outcome |
|---|---|---|
| T122 | Codex M1 example: exit.actual_exit=True; otherwise valid, commit_dir outside job_dir | In-memory H(P2_EXIT_INVALID); disposition null, ACK_NOT_ATTEMPTED, registry NOT_ATTEMPTED; zero module mutation in commit_dir or registry; date once; final PASSED |
| T123 | Valid stdout/stderr records plus an extra captures key (direct fire, no validator exception), commit_dir outside job_dir | In-memory H(P2_CAPTURE_STDOUT_INVALID,P2_CAPTURE_STDERR_INVALID); no commit I/O; final PASSED |
| T124 | Completed registry append/fsync, then registry-fd close raises K=KeyboardInterrupt and directory-fd close raises fresh S=SystemExit | Both attempts exactly once; S propagates; base instance dict has prior==(K,); attached H(P5_BASE_EXCEPTION,P5_REGISTRY_APPEND_FAILED); APPENDED/RELEASED, fsync:true, line_complete:true, closed:false, unresolved_total:2; ACK_OK; final NOT_PERFORMED; RELEASED-bytes uncertainty; both originals retained |
| T125 | Part2 artifact read_bytes raises K; job-dir fd close then raises fresh S | S propagates, prior==(K,); H(P2_ARTIFACT_IDENTITY,P2_BASE_EXCEPTION); reader unsafe, so in-memory only, no date/commit, final NOT_PERFORMED; unresolved_total:1; parts1 PASS,2 FAIL,3–5 NOT_EVALUATED |
| T126 | Native os.read in late hash raises K; file fd close then raises fresh S; every directory close succeeds | S propagates, prior==(K,); H(P5_LATE_CENSUS_INCOMPLETE,P5_BASE_EXCEPTION); unresolved_total:1, all directory fds closed once; native path commit-safe → one HELD commit, ACK_OK, APPENDED HELD; final NOT_PERFORMED |
| T127 | Same K then S during build_late_baseline | No baseline; S identical object propagates; base instance dict prior==(K,); no parent_release_result; no mutation, every directory close once |
| T128 | Census K, then owned_date raises H (non-Exception BaseException) with raising __context__ property/__getattribute__ | H propagates unchanged; no metadata property invoked; base dict prior==(K,), attached H(P4_BASE_EXCEPTION,P5_BASE_EXCEPTION); no commit; base descriptor shows free/acyclic link only |
| T129 | Census raises H with __setattr__ raising fresh SystemExit, plus same-name data descriptors rejecting parent_release_* writes | Direct instance-dict attachment invokes neither override; H propagates, prior==(); base dict contains pure-JSON H(P4_BASE_EXCEPTION); one HELD commit (census safe), ACK_OK/APPENDED HELD; final NOT_PERFORMED |
| T130 | Census raises ordinary E whose __str__ always raises the same pre-created K | Description failure K retained once; evaluation part5 continues; K propagates, prior==(); H(P4_CENSUS_FAILED,P4_BASE_EXCEPTION), one HELD commit ACK_OK/APPENDED HELD; final NOT_PERFORMED; no silent swallow |
| T131 | Census raises non-Exception H whose __class__ property returns RuntimeError | Real-type classification: H is not swallowed as Exception; H identical propagates, prior==(); H(P4_BASE_EXCEPTION), one HELD commit; final NOT_PERFORMED |
| T132 | Synthetic coherent tree within depth/entry/byte caps whose next descendant path exceeds4096 chars; variant: a valid deeper second root then >128 components | _parts refuses before offending lstat/hash/insertion. Helper raises ReleaseRefusal (length: normalized absolute path required; components: path components); no baseline. Transaction H(P5_LATE_CENSUS_INCOMPLETE), fresh_entries:null; safe HELD commit. Each acquired handle closed once; no truncated positive |

All T01–T132 remain unexercised. Exact line-number references above are navigation aids, not execution evidence.

## Preserved limits and external prerequisites

T78 still injects at the final check, not actual assembly expiry. Optional T78b wraps the normal-path `_final` (now at 1791) to flip the synthetic predicate; this proves only detection-at-check, not real-time behaviour. T106 is a count-predicate limit only: 200001st root/child insertion refuses, while a 200000-entry complete baseline cannot fit the 16MiB serialization/read cap. The old v4 T106 anchor `_scan:1164-1165` was wrong (1165-1166); v5 insertion/count are 1210-1211, root count1259, helper cap1829. No huge-baseline positive claimed.

No hard guarantee against MemoryError or an asynchronous exception delivered inside retention/guard/attachment itself or between an origin and its first handler. No adversarial in-process authenticity: subclass descriptors can intercept caller getattr, objects can be mutated in-process, and interpreter/runtime compromise is outside this correctness contract. The base-descriptor behaviour is source-reasoned, unexercised.

Unwaived: CP1 caller receipt/capacity; CP2 COMPLETE historical union; authentic raw/beta adapters and provenance (beta worker owns raw supervisor19; no overlaps here); publication freeze and all lane/TMPDIR/capture/alias scope; baseline provenance; reader-global unresolved report; owned-date lifecycle; >16MiB part2 streaming interface; native stalls (no hard real-time guarantee). Lexical containment/NOFOLLOW walks do not authenticate path origin, aliases or the namespace boundary. The RQLS9 fixture capture schema is not the PRT API.
