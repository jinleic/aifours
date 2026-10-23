# Supervisor v15 — qualification package v8, written review snapshot

Recorded after actual `/bin/date`: 2026-10-19T10:26:58-0700.

**NOEXEC.** This document grants no preparation, helper, control, fixture, Q1 or science execution; no reservation release. The maximal-cardinality 1-RQLS(10) target remains OPEN / UNKNOWN. No numerical solver or assay has been changed by this package.

## 1. Immutable source set and authority

| Role | Lane-relative source | SHA-256 |
|---|---|---|
| Supervisor | `code/owned_supervisor_v15.py` | `0a22bbc56a929bf674a579314ef0eeefd7f8e71ed5b3e39cb44db7921f5f34f9` |
| Child | `code/guard_qual_child_v11.py` | `56841a0464be0f1e38965d86305fe7dbf0dcc4abaecaddf3fce7a411febb4b45` |
| Preparation writer | `code/guard_qual_configs_v11.py` | `720335c15531190c41ea12a1ff723829ca9d3a5abcbe73d60aea5276fd8e2447` |
| Checker | `code/guard_qual_check_v10.py` | `de6766d63c8e7ca8605e97ef18c1010405b52feb21ff9bf4056d3e3863ad2e04` |

All are 0444. Fresh qualification root is exactly `<LANE>/qual-pkg-v8-v15`; each scenario directory is exclusively created once. No existing run, fixture or prior evidence may be reused, mutated, overwritten, moved or deleted.

The parent reports source v15 `SOURCE_READY_FOR_GUARD_QUALIFICATION` (0 FATAL / 0 MAJOR / 0 MINOR), review SHA `a8ae9326ef03f56fa25ebe4ccd60b26fc9d47e3bd06c411d7703543f38f4b1e6`. Parent readiness RUN `review/rqls10-supervisor-v15-source-readiness-parent-v1.json`, SHA `9821c9750c7f369d6f63a532bf2882b27776a81844de88ced4e24f223a706940`, is **SOURCE_READY_RUNTIME_HOLD, NOT GO**. It does not accept these new child/writer/checker sources.

Binding correction `fabe57ab4aeacc416f22bdf334c2cc3bbd5fda1d0e777d7279187ae0564155a2` remains: actual owned bounded `/bin/date`; all post-baseline unproved identities block regardless of UID/path; mixed real/effective UID unreadability is failed coverage; SIGTERM only, no escalation/tool timeout/ulimit/deletion; no speculative birth-ancestry exemption. Parent alone serializes exact one-item allocations, gates, admissions and releases. No broad GO or automatic chain is supplied.

## 2. Preparation, exact individual authority, and creation identity

Preparation itself needs the parent's individually authorized owned envelope; the writer is not permission to invoke it. The writer spawns nothing, imports no package source, writes no GO/stability/approval, and invents no clock/resource observations. It accepts only fixed scenario metadata and the actual realpath `.../Resources/Python.app/Contents/MacOS/Python`, not the framework launcher.

Before creation it checks fixed paths and actual four-source/interpreter digests. A fresh run/out/tmp is anchored using no-follow descriptors. For `mutate_pin`, the original inode, size, one-link count and bytes are captured with fstat/readback on the **CREATED exclusive descriptor before close**. Preparation is written before config; it contains no config or GO digest, avoiding circularity.

Preparation has exactly:
`kind, scenario, run, output_root, fixture, source_pins, python, allocation, negative_control`.
Kind is `qualification-creation-preparation-v1`; run/out are `{path,inode:[dev,ino]}`; fixture is null except the original pin `{path,inode,sha256,bytes,nlink:1}`. Four source pins are exactly `{path,sha256}` at the listed fixed paths. Allocation is `{bytes,cpu_slots,outstanding_reservations_bytes,lane_outstanding_reservations_bytes}`. Negative control is true except `ok`/`rc_nonzero`. The checker independently hashes the actual preparation/config/GO/stability/source/interpreter bytes and semantically reconstructs the complete preparation/config.

Parent approval, trusted by an external SHA passed to the checker, has kind `v15-qualification-invocation-v1`; it pins scenario, config/GO/stability/preparation hashes, all four actual sources, interpreter and current allocation. Explicit flags are:
- Every `busy2`, `ownership_*`, `zombie_hold`: `ownership_negative=true`, plus GO `qualification_negative={scenario,kind:"ownership",creation_channel:false}`.
- The four helper injections: `helper_injection=true`, GO kind `helper_injection`, false creation channel.
- Both mutations: `mutation_negative=true`, GO kind `mutation`, literal boolean true creation channel.
- Other controls omit the negative GO object; their exact config SHA/purpose/scenario still needs its own individual authority.

Each GO binds exactly one config digest and the v15 BOUND_KEYS, including `creation_channel`; only deliberate `go_unlisted` has an empty config map under its own negative authority. Busy2 reserves **both CPU slots**, threshold1, unchanged global ceiling2. No busy3 exists.

Ordinary/science/certificate consumers keep exact bytes `GO\n` then EOF, with `creation_channel={}`. Only the two declared mutations receive the one fixed canonical compact JSON line, at most4096 bytes, then EOF. Exact schema, source binding and terminal/accounting contract are frozen in `review/rqls10-v15-qualification-interface-v1.md`, SHA `bc18425509159d362b4392e88eb54c4d8fa6fb165cd4a635bddc619e5d5ab290`. No command/target selection is added. The child verifies approved run/out anchors and original target descriptor inode/hash/size/one-link **before append**, then verifies the same descriptor/name again. An older renamed same-content inode is refused before mutation. The launch target uses its original supervisor publication inode/digest. The checker joins exact received-line digest, preparation facts, original and after facts, and before/append/fsync/after monotonic ordering.

## 3. Retained original22 controls — exact required outcomes, NOT results

`G` = `GRACE_EXPIRED_AFTER_CHILD_EXIT`; `S` = `STREAMS_OR_THREADS_NOT_CLOSED`. An ownership blocker code is derived only from the single full intended incarnation's actual final classification; no unrelated failure is excused.

| Control | Receipt / actual exit | Child rc; exact cause and required stimulus |
|---|---|---|
| date_fault | NOT_LAUNCHED / 14 | no child; exactly HELPER_FAULT_INJECTED; no helper PID, null clock, exact STABILITY_AGE_UNVERIFIABLE ACK refusal |
| helper_overrun | NOT_LAUNCHED / 14 | no child; exactly HELPER_CALL_FAILED; measured injection start < actual call deadline < injection end; complete bounded helper cleanup |
| helper_group | UNSETTLED / 14 | no child; exactly HELPER_CALL_FAILED + HELPER_OWNERSHIP_UNSETTLED; reaped integer-status leader, group proof deliberately withheld |
| helper_eof | UNSETTLED / 14 | no child; same exact failures; actual stdout closed, EOF proof deliberately withheld |
| go_unlisted | NOT_LAUNCHED / 14 | no failures/helpers; exactly missing-config reason and machine cause GO_DOES_NOT_NAME_THIS_CONFIG; no clock invented |
| ok | SETTLED / 0 | rc0; EXITED; no trips/failures/signals; exact three stdout lines |
| rc_nonzero | SETTLED / 0 | rc3; EXITED; no trips/failures/signals; nonzero child rc grants no science acceptance |
| missing_output | UNSETTLED / 11 | rc0; EXITED; exactly REQUIRED_OUTPUT_MISSING; main already reaped, no sent TERM |
| mutate_pin | UNSETTLED / 11 | rc0; EXITED; exactly PIN_CHANGED_OR_UNREADABLE; original fresh approved fixture plus one byte |
| mutate_evidence | UNSETTLED / 11 | rc0; EXITED; exactly EVIDENCE_MUTATED; original published launch inode plus one byte |
| stray_file | UNSETTLED / 11 | rc0; EXITED; exactly UNDECLARED_ENTRIES; exact new stray file name/content |
| deadline | SETTLED / 0 | rc-15; EXITED; DEADLINE only; actual wall/order/once-only TERM and post-publication latency proved |
| flood | SETTLED / 0 | rc-15; EXITED; STREAM_CAP only; nonblocking bounded flood, actual overflow and exact retained counters/bytes |
| busy2 | SETTLED / 0 | rc-15; EXITED; BUSY only; both full intended incarnations measured busy at first threshold1 excess, two reserved slots, no global excess |
| rss | SETTLED / 0 | rc-15; EXITED; RSS only; intended child allocation/touch/task brackets and its measured RSS alone > threshold, exact first partial-prefix trip |
| zombie_hold | SETTLED / 0 | rc0; EXITED; no trips/failures; full intended status5 identity retained while held, rooted ownership and bounded WNOHANG joins |
| ownership_group | UNSETTLED / 11 | rc0; grace-child-exit; exactly G+OWNED_LIVE+S; sole full intended known same-group descendant/root |
| ownership_slow | UNSETTLED / 11 | rc0; grace-child-exit; exactly G+OWNED_LIVE+S; sole full intended known current-parent descendant/root, never unproved alternative |
| ownership_fast | UNSETTLED / 11 | rc0; grace-child-exit; exactly G+intended actual OWNED_LIVE or UNPROVED_LIVE+S; no other blocker/identity |
| ownership_double | UNSETTLED / 11 | rc0; grace-child-exit; exactly G+intended actual OWNED_LIVE or UNPROVED_LIVE; streams closed, complete intermediate join and stable post-exec/post-reparent incarnation |
| ignore | UNSETTLED / 11 | rc null; grace-stop; DEADLINE only; exactly GRACE_EXPIRED_AFTER_STOP_REQUEST+CHILD_NOT_REAPED+OWNED_LIVE+S; TERM actually sent and ignored |
| identity | UNSETTLED / 11 | rc null; grace-stop; same plus IDENTITY_UNVERIFIED; explicitly unsent injected TERM, no escalation |

All main controls require one complete captured stdout summary, complete separately captured supervisor stderr and separately captured actual exit. Helper/admission negatives require their exact ACK_REFUSED interface, not a successful ACK. All launched controls require nonempty complete decoded samples, with exact byte/count reconciliation; an immediate exit cannot qualify through an empty stream. A printed positive ACK followed by actual14, incomplete capture, or any unexpected failure/trip is FAIL/HOLD, not accepted under an expanded code set.

Lifetimes/walls/thresholds remain the retained control definitions: common child life60s, ownership40s, zombie10s, deadline120s; supervisor wall60s except deadline/ignore/identity10s. Cooperative child joins use WNOHANG with absolute earlier deadlines inside the module-entry lifetime and reserved evidence time; unresolved joins record identity/error and fail, never finally-exit0. Sleep exec uses only remaining life. Default helper call/grace5s/5s; overrun call0.01s; group/EOF call0.2s/grace0.5s. Actual measured crossings, not requested flags/delays, determine acceptance.

## 4. Common oracle — including every admission-negative return

The checker has no early admission-negative bypass of common final evidence:
- Complete final census, full main/helper root registry, integer helper wait status, actual source/config/input/approval binding, retained all-UID/mixed-UID history, resource extrema, free minimum, empty test TMP and per-root inventory are mandatory for all22.
- For NOT-LAUNCHED **main only**, it requires the explicit five-path all-null artifact map, empty main expected-digest/stream maps, zero typed sample counters and explicit null main identity/rc/exit/stop/signal fields. It does NOT erase or demand empty observed helper/date/ownership histories.
- Every applicable HELPER/ADMISSION/LAUNCH/GO/ACK commit is required with exact phase/provenance. Canonical/future/nonnegative date-floor checks, actual captured helper purpose/PID/date joins, first-helper-only no-prior-clock exception, nonrenewing monotonic expiry replay, actual post-write/close GO upper age and remaining main runtime are checked. Refusal machine causes are exact, not substrings.
- Receipt/current history prefixes, immutable first observations, monotonic last extensions and variants/counts are checked. Current reconciliation has the complete typed schema. Every sample/helper proof/admission/launch/pre-GO/clear/final/ACK census joins a unique retained observation. All post-publication additions and individual resource measurements are checked; aborted attempts remain explicitly aborted, not completed. Duplicate summary state/rc/failure/blocker/history fields cannot contradict or disappear.
- Intended full incarnations, known ownership roots/edges and lower-bound registry retention are required, not just bare PIDs/upper bounds. Group/slow cannot qualify as unproved; fast/double permit only their defined known-or-unproved alternative. Reported identities are retained for the separate parent ended-identity audit. Zombie, RSS and busy proofs are PID/incarnation-specific. Busy predicates/counters remain evidence from this reviewed implementation, not an independent kernel implementation or proof of numerical backend threading.
- Actual receipt/settlement bytes/digests, original same-inode two-link staged publication, exact distinct-inode charged payload, reservation/output/FREE/LANE arithmetic and actual b/end are mandatory on positive ACK **and ACK_REFUSED**. Precheck a or fresh values cannot substitute. Late artifacts are labelled/excluded only from historical charge reconstruction, never from the later fresh parent audit. No in-flight peak claim is made.

Numeric misses, source review and recovery controls are not nonexistence proofs or maximal-basin evidence. These sources/checker are one implementation with cross-record checks, not an independent runtime verifier or Lean proof.

## 5. Parent-only five-part release transaction

No checker PASS, receipt status, JSON ACK, child rc, supervisor exit or elapsed lifetime alone releases anything. For each exact individual invocation the parent must join all five parts:

1. **Authority/allocation:** serialize current exact item allocation and all other outstanding reservations; fresh stability/gate; exact approved source/config/preparation/GO pins and explicit negative scope. No next invocation without its own current authority.
2. **Execution/publication:** separately capture actual exit and complete stdout AND stderr; verify actual invocation identity, both original publication digests/inodes/link counts/readbacks, post-publish monotonic bound and full successful parent publication acknowledgement. A positive printed ACK with actual14 is rejected.
3. **Oracle:** run only the separately admitted fixed checker with the external trusted approval digest and actual exit; inspect all criteria and exact cause; reject missing/contradictory evidence.
4. **Ended identities:** independently establish endedness for every known main/helper/descendant, reported incarnation and historical unproved identity; retain unresolved coverage. No PID-only or 'missing means gone' shortcut. Wait any authorized surviving workload through its declared life; no escalation, deletion or automatic release.
5. **Late/resources/exclusive commit:** after endedness, independently audit the **entire RUN**, including captures, check output and every late artifact, with fresh bounded descriptor-anchored resource accounting; write a NEW exclusive actual-owned-`/bin/date`-stamped parent disposition joining authority, actual exit, capture/artifact digests, oracle, ended-identity and late-resource evidence. Only successful completion/acknowledgement of that parent transaction releases the allocation. Original UNSETTLED/NOT_LAUNCHED publications stay immutable and are not relabelled.

The parent owns this transaction implementation and every admission/gate/release; this package supplies no competing scheduler or release ledger.

## 6. Separate FULL finite matrix, not science qualification from22

Every obligation in v13 source review `7b042421e9fb410cf3fec99d9953dd69c4a6c5736628a3186b18de3f50db2ddb` lines108–132 and v14 review `1866052f63d8b8c143ece0cee646b277e2f87cbba2f5c58ae4edf5d111fca413` lines30–34 remains required and UNEXERCISED. This base package provides the original22 implementations and oracle, not the additional isolated fault/state fixtures. The full matrix requires an exact separate source/plan/oracle mapping and separately reviewed bounded fixtures where needed, measured actual outcomes/cutoffs, complete actual capture/exit/artifact identities and honest distinction between state-model coverage and native/OS integration. It includes persistent post-ACK stderr failures through shutdown and all four accounting stages with honest nulls. No host-clock mutation or synthetic value presented as actual `/bin/date` output is permitted.

Even successful source review and all22 base controls would not alone qualify the unrestricted fixed-B assay for science. The assay/checker/backend-thread proof remains held, unchanged, until the full required guard qualification and the parent's next separate decisions.

## 7. Authoring provenance and non-results

Only AST parsing, source-byte hashing and written diff/disposition work were performed. No source imports, preparation, helper, control, fixture, numerical/native assay, tests/build/lint/formatter or Q1 occurred. Rejected hashline edits were not applied; exact anchors were re-read. Intermediate child10/writer10/checker9 were already0444/cited when the author found the admission-main manifest omission; they remain immutable UNADMITTED. Corrected child11/writer11/checker10 are ONE coherent packagev8. The correction diff is `review/rqls10-package-v8-authoring-correction-v1.diff`, SHA `bd049916ee0c7fcb9f08245990d351fc0b3951faae01e46a06d773377d1d9f5d`. Supervisor v15 is unchanged.
