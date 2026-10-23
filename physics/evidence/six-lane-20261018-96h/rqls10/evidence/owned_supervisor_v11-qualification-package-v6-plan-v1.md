# Restored v11 qualification successor, package v6 — SOURCE REVIEW ONLY

Recorded 2026-10-19T08:46:20-0700 after /bin/date. Author ContinueRQLS10b. No runtime authority, no source acceptance,
no invocation requested by this document. V10 and its package remain immutable/unexecuted. Parent correction
RUN/review/rqls10-supervisor-v10-scope-parent-correction-v1.json,
`fabe57ab4aeacc416f22bdf334c2cc3bbd5fda1d0e777d7279187ae0564155a2`, WITHDRAWS the earlier e441d858 scope decision.
This successor RESTORES /bin/date helpers and owned/unproved/mixed-UID evidence; it does not relabel away obligations.

## Source pins and dependencies
- Supervisor `code/owned_supervisor_v11.py`
  `f43c7addf232cfe5e40de7e5622577fb7d883415ee0ad3e701887b376f97d90c` (frozen, queued to parent Codex review;
  RUN/review/rqls10-owned-supervisor-v11-source-review-freeze-v1.json c501a664...043d).
- Test child `code/guard_qual_child_v8.py`
  `002925444403fd9cecd6d0d724b207fb08eaa6bc51351f67604db3e94e69ba9b`.
- Config/layout writer `code/guard_qual_configs_v7.py`
  `69dd256ead0d8a26478a57114f60b2b4000dddee701c81bdf1244f0295870532`.
- Independent artifact-reading checker `code/guard_qual_check_v7.py`
  `9932d2984b3b38b694d65c1619ec060e2d3b826d1a3bfe4800a3570c8ba252b9`.
- Unchanged gate source: lane `code/stability_gate_v2.py`
  `1f62874aff9b22657a90f180b81c678117fd703afe2345f7576454e0faae008a`; parent observer source
  `RUN/control/resource_observer_v3.py`
  `fe311f28d122310da004d0968272ae294a99757756b4898f0d9db4cb13f04196`.
  Dependency execution envelopes stay parent-owned. Do not infer approval from their old filenames. Gate reads the
  parent's pinned observer stream and writes one exclusive RUN/stability.json, projected20971520 bytes. V11 does not
  supervise the outer gate; the exact parent invocation still needs its existing separately audited approval.

All new sources were AST-parsed, not imported/executed. Writer/checker config_for ASTs match. One implementation is
not independent process/runtime verification. Science target remains OPEN / UNKNOWN.

## Mandatory fail-closed boundary and known integration blockers
Source-reviewed nonforking science children are a narrower admission interface ONLY, not an ownership exemption.
Every unknown post-baseline identity, every unproved census, mixed-UID unreadability and every unresolved helper
blocks a positive outcome. Ordinary launchd churn and persistent elevated login processes can make qualification
unavailable on this host. That availability risk is separate from correctness and gives NO permission to exclude
those processes, replace unknown RSS with zero, omit incomplete samples or accept extra failure codes.

Static package integration disclosed to Main, no source changed:
1. A fast clean child can clear before observe writes its first sample. Checker intentionally requires nonempty samples
   and FAILs such a bundle; absence of observations is not accepted as a qualified positive control.
2. Every helper/retry now enforces resource limits, but retained helper proof omits RSS/busy/retry observations while
   maxima include them. Exact maxima reconciliation can FAIL; do not weaken the checker to hide missing evidence.
3. go_unlisted has no admitted authorization; final end-date attempt can add HELPER_CALL_FAILED. Checker preserves the
   isolated GO-negative requirement and FAILs that contamination rather than accepting arbitrary extra failures.
These require explicit parent source disposition or a NEW source/package version before any affected control GO.
This plan is a complete proposed acceptance contract for REVIEW, not a claim that v11 currently passes it.

## Confined fixture layout
QROOT = `<lane>/qual-pkg-v6-v11`. Writer opens component-by-component through retained O_DIRECTORY|O_NOFOLLOW fds,
checks source/interpreter pins and arguments before creation, creates/binds package-root.json once and refuses an
existing scenario directory. No arbitrary BASE/output/mutation path accepted. Per scenario RUN contains config.json,
preparation.json, tmp/, out/ and mutate_pin's new pinned-scratch.txt. Parent approval/GO/stability/captures/check/audit/
release files live in RUN OUTSIDE out/. The supervisor alone creates its evidence in out/. Child mutations are EXACTLY
RUN/pinned-scratch.txt or RUN/out/launch.json, opened without create/no-follow, bounded regular and one link, original
fixture bytes checked; append exactly b'x'. Neither parent nor worker modifies earlier run files.

Use the real `.../Resources/Python.app/Contents/MacOS/Python` executable with pinned digest, never Homebrew's bin
launcher (read-only binary inspection showed a startup re-exec). V11 uses protected os.posix_spawn with explicitly empty
child mask and inherited cwd; the exact invoking cwd MUST equal the lane. No unsafe preexec/global cwd mutation.

## Exact serialized invocation and release transaction
No broad GO, automatic next item, file-existence release, timeout, SIGKILL, ulimit or deletion. Every control has its OWN
parent GO and current allocation; process-ownership negatives must be labelled as such, never accepted science.

1. **Allocate/prepare/authorize.** Parent reserves20971520 bytes plus ONE CPU slot, except busy2 reserves TWO slots
   (trip threshold1; global lane ceiling2 remains unchanged; no busy3). Metadata-only writer, only if authorized:
   `PYTHON_APP -I -B code/guard_qual_configs_v7.py SCENARIO PYTHON_APP OUTSTANDING_BYTES LANE_OUTSTANDING_BYTES`.
   Run fresh parent-approved stability gate. Parent exclusively writes /bin/date-stamped go.json with decision GO,
   exact item, raw not_after_epoch, stability_receipt_sha256 and exactly one config digest->printed GO entry. For
   go_unlisted ONLY, configs={}. Its raw expiry must cover the proposed launch/GO/ACK; no supervisor timestamp
   extrapolation substitutes for a fresh parent decision. Parent then exclusively writes parent-authorization.json
   and retains its SHA externally. Schema kind=`v11-qualification-invocation-v1`, scenario, config_sha256, go_sha256,
   stability_receipt_sha256, preparation_sha256, sources={supervisor,child,writer,checker} each {path,sha256},
   python={path,sha256}, allocation={bytes:20971520,cpu_slots:1 or2,outstanding_reservations_bytes,
   lane_outstanding_reservations_bytes}; ownership_negative=true for busy2/all ownership_* and zombie_hold.
2. **Execute only after all source/package/item gates.** Fresh approved gate && exact supervisor invocation
   `PYTHON_APP -I -B code/owned_supervisor_v11.py RUN/config.json`, cwd lane, tool timeout0. Parent captures the single
   stdout JSON line exclusively in supervisor-summary.txt and retains the ACTUAL exit separately. Independently
   re-hash receipt and settlement, prove .staged same inode/two links, and verify post_publish_mono after publication,
   readbacks and all root directory fsyncs. Printed acknowledgment alone never releases anything.
3. **Check independently read artifacts.**
   `PYTHON_APP -I -B code/guard_qual_check_v7.py SCENARIO PARENT_APPROVAL_SHA256 ACTUAL_EXIT` -> exclusive RUN/check.json.
   Trusted approval digest and actual exit are external inputs, not fields trusted from the receipt. Checker hashes
   actual four source files/interpreter/config/GO/stability/preparation/evidence, reconstructs config and exact
   scenario outcome, checks full identities/owned roots, mandatory helper settlement, whole strict JSON sample
   sequence (no partial/trailing garbage), exact manifests, intended child-PID resource cause, exact payload charge
   and held reservation arithmetic. Exit0 only PASS,1 FAIL,2 infrastructure error. A PASS is one observed control,
   not science admission, universal latency or independent supervisor implementation verification.
4. **Verify every owned AND unproved identity ended.** Parent performs independent read-only PID+uniqueid+version
   checks for main child, all /bin/date helpers, all retained descendants, all reported negative-workload PIDs, and
   all unresolved post-baseline identities. No speculative signal or PID-only join. Helper leader reaped is NOT
   closure: require recorded initial identity, known wait status, complete group/descendant/unproved census and actual
   stdout EOF/close; unresolved proofs retain the block. For injected group/EOF uncertainty, later independent physical
   end proof is recorded separately without rewriting the original UNSETTLED result. Any still-live process after its
   own deadline or unaccounted identity HOLDs the sequence; reservations stay held.
5. **Late audit + independent release disposition.** Parent audits all RUN files, not just out/, hashes new artifacts,
   verifies previously frozen bytes unchanged and admits only the documented late ignore/identity child-out.json
   (original scenario/PID, born after decision). It writes a NEW exclusive /bin/date-stamped disposition binding
   allocation/approval, actual exit/captured summary, all digests, checker, ended-known/unproved census and late audit.
   ONLY that independently verified disposition releases reservations/CPU slots and allows another GO. Source-level
   unknowns, unexpected failures or contaminated controls need explicit HOLD disposition, not automatic advancement.
   UNSETTLED is immutable; eventual self-exit or repaired observations never turn its receipt into SETTLED/science.

## Restored helper controls (individual negative GOs, all UNRUN)
V11 writes actual /bin/date output or null. Helper budget starts BEFORE pipe creation/spawn; successful late reap is
still failure. Exception cleanup attempts at most one full-identity group TERM and bounded grace. Protected
os.posix_spawn sets an EMPTY child signal mask so the helper can receive SIGTERM; PID/pipe allocation is pre-registered.
Final refresh repeats the SAME full proof and cannot discharge ownership by observing a reap alone.

| Scenario | Intended predicate; exact guard result under otherwise clean host evidence |
|---|---|
| date_fault | Injected before spawn, no fake date, no helper PID, exact HELPER_FAULT_INJECTED; admission DATE_HELPER_UNAVAILABLE; receipt NOT_LAUNCHED/actualexit10, enddate null |
| helper_overrun | Actual /bin/date launched; explicit observer delay0.02s exceeds its0.01s call budget; exact HELPER_CALL_FAILED, date null, cleanup full closure proved within5s, no late-success clock; NOT_LAUNCHED/10 if ownership fully settled |
| helper_group | Actual date helper reaped, group proof explicitly injected as unproved (not an assertion of an actual escaped /bin/date descendant); exact HELPER_CALL_FAILED + HELPER_OWNERSHIP_UNSETTLED, admission DATE_HELPER_UNAVAILABLE; UNSETTLED/11 with leader_reaped=true but settled=false/group_clear=false throughout final refresh |
| helper_eof | Actual date helper reaped and pipe physically closed, EOF proof deliberately withheld; same exact failure set and UNSETTLED/11, settled=false/eof_proved=false after final refresh |

The last three are reviewed injections, NOT empirical proof of real binary failure, real kernel group corruption,
real descriptor failure or arbitrary helper overrun handling. The checker requires complete underlying identity/census
and no unrelated failure. Real helper exceptions/metadata races need separate exact authorized controls. No new helper
after latch/cancel; missing clock stays null. Parent-owned timestamp records still require fresh /bin/date.

## Main-child controls and exact expectations
All have settle20/sample1; module-entry lifetime60s (deadline120s; ownership40s; zombie10s). Interpreter startup is not
falsely claimed inside the module clock; supervisor's pre-spawn clock is independent. GO input and flood are
nonblocking, descendant exceptions exit1, no masking finally-exit0. Every test mode is frozen/reviewed before its own GO.

| Controls | Intended exact outcome and cause evidence |
|---|---|
| go_unlisted | Isolated GO_DOES_NOT_NAME_THIS_CONFIG refusal, no other failure. Receipt NOT_LAUNCHED, actualexit14/ACK_REFUSED. Current v11 integration contamination noted above must be disposed before GO. |
| ok / rc_nonzero | SETTLED/exit0 with childrc0/3, EXITED, no trip/failure/signal; real child identity/output, exact stdout; at least one complete sample and all helpers settled |
| missing_output | UNSETTLED/11, childrc0, EXITED, exactly REQUIRED_OUTPUT_MISSING; confirmed absence, exact child stdout and explicit reaped/no-signal stop |
| mutate_pin / mutate_evidence / stray_file | UNSETTLED/11, rc0, EXITED; respectively exactly PIN_CHANGED_OR_UNREADABLE / EVIDENCE_MUTATED / UNDECLARED_ENTRIES. Actual fixture/launch one-byte mutation with inode/size identity, or exact stray name/content. No other failure accepted. |
| deadline / flood / rss | SETTLED/exit0, childrc-15, EXITED, exactly intended DEADLINE / STREAM_CAP / RSS and no failure. One verified group TERM. Match deadline mono_spawn+wall10; actual overflow+retained file bytes/digest; or reported allocating child PID+320MiB touched+sampled threshold crossing. Signal/trip->post_publish_mono<=7s. |
| busy2 | TWO reserved slots, two actual CPU-bound PIDs(parent+ONE child) in sample/trip sets, threshold1 exceeded at count2, no global cap relaxation; BUSY only, rc-15, process SETTLED after all known identities end. Explicitly a forking qualification workload, never a science child. |
| ignore / identity | UNSETTLED/11, childrc null, GRACE_EXPIRED_AFTER_STOP_REQUEST, DEADLINE only; exact GRACE_EXPIRED_AFTER_STOP_REQUEST+CHILD_NOT_REAPED+OWNED_LIVE+STREAMS_OR_THREADS_NOT_CLOSED, plus IDENTITY_UNVERIFIED for injected identity. Sent/ignored vs explicitly unsent injected TERM. Final blocker exactly main child; parent waits/audits late output. |

## Restored process-ownership negative controls
Each has its OWN ownership_negative=true approval and parent GO, never a general science permission. Child reports
intended PIDs through its exclusive output; checker binds them to actual complete owned/unproved census, not an
unrelated launchd process. All reported/retained identities remain in the release obligation, including ended ones.

| Scenario | Workload and exact scoped acceptance |
|---|---|
| ownership_group | Fork one sleeping same-group child, parent stays3s then exits. Known descendant retained; after20s child-exit grace, exact GRACE_EXPIRED_AFTER_CHILD_EXIT+OWNED_LIVE+STREAMS_OR_THREADS_NOT_CLOSED; UNSETTLED/11, original childrc0, no trip, no speculative post-reap signal. Final blocker exactly reported grandchild. |
| ownership_slow | Same3s observation window, descendant setsid. Known ownership follows observed current-parent edge, not group/argv/path; same exact scoped negative result. |
| ownership_fast | Parent exits immediately after fork+setsid. Final intended grandchild must be known owned OR explicitly unproved; never exempted. Exact GRACE_EXPIRED_AFTER_CHILD_EXIT plus OWNED_LIVE and/or UNPROVED_LIVE only when justified by the actual final blocker class, plus STREAMS_OR_THREADS_NOT_CLOSED. Final combined blocker set must be exactly the reported PID. |
| ownership_double | Intermediate forks, reports final PID through bounded pipe, exits; grandchild chdir/, closes streams and execs /bin/sleep for REMAINING lifetime. This is the prior reparent/exec counterexample: it must remain owned or unproved and UNSETTLED; exact GRACE_EXPIRED_AFTER_CHILD_EXIT plus the evidence-justified OWNED_LIVE/UNPROVED_LIVE codes, no unclosed-stream failure (the grandchild closed them). |
| zombie_hold | Holder keeps a reported zombie3s then explicitly reaps it and exits; child reaps holder and reports both. At least one complete sample must show that exact zombie PID and the registry must retain every observed owner. Process SETTLED/0 after everything ends is a guard control only, NOT accepted science for the deliberately forking workload. |

No arbitrary additional blocker/failure is accepted to satisfy these negatives. Broad-unproved host activity can make
them FAIL/HOLD, not grant permission to remove it. Whole samples, all helper proofs, exact bytes/digests, mixed UID and
all incomplete-retry limit latches remain part of acceptance. No busy3. No auto-retry after UNSETTLED or failed controls.

## Explicit limits
No claim of complete atomic global census, OS write sandbox, universal native-call latency, real corrupted-helper
coverage, every cancellation/exec/UID race or every free/lane/publication boundary. Parent source review plus individual
controlled invocations remain necessary. The current three integration blockers are explicit and cannot be solved by
accepting a missing sample, trusting an unexplained maximum or adding an allowance for arbitrary errors. No science or
Q1 execution is authorized; unrestricted fixed-B is still the science route after the guard qualifies.
