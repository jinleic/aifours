**DISPOSITION: HOLD — one blocking MAJOR and three MINOR findings.**

All 26 files match the supplied SHA-256 hashes and byte counts. Review used only static reads and hashes within the snapshot.

1. **MAJOR — The new control can hang before exercising the race.**  
   [SOURCE13:156–160](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/pa19-full-k1-v6-source-review-v1/snapshot/13-src-check_m2_ms09_k1_v6.py:156) globally replaces `threading.Event`. This also replaces the events used internally by `Thread._started`.

   In CPython bootstrap, that event is signalled before the new thread enters the active-thread registry. Calling `current_thread()` inside the replacement’s `set()` can therefore construct a `_DummyThread`; its own started event invokes the same override recursively. The original started event never gets signalled, leaving the first `sf.start()` at `SOURCE05:295` blocked before solver launch. The required control then depends on supervisor intervention instead of exercising delayed failure publication.

   **Repair:** avoid replacing global threading primitives. Instrument only the pipeline’s stop event. At minimum, capture the main thread’s identifier beforehand and compare `threading.get_ident()` inside `set()`, avoiding thread-object lookup during bootstrap.

2. **MINOR — The control remains dependent on scheduling after that repair.**  
   `SOURCE13:110` keeps the solver alive for one second; `SOURCE13:167` delays publication for 0.2 seconds. A delayed worker can miss the intended bounded exit. Conversely, a removed-join regression can escape detection if the main thread pauses long enough after releasing publication.

   **Repair:** use explicit acknowledgments for solver lifetime and final-join entry. Hold publication until the settlement join begins, and require a removed-join mutant to fail. Use bounded waits solely to detect broken handshakes.

3. **MINOR — A prohibited subprocess timeout was added.**  
   [SOURCE13:185](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/pa19-full-k1-v6-source-review-v1/snapshot/13-src-check_m2_ms09_k1_v6.py:185) calls `Popen.wait(timeout=10)` through its positional argument, contrary to the explicit no-subprocess-timeout constraint.

   **Repair:** poll against a monotonic deadline, fail the control if the child remains alive, and call parameterless `wait()` after observing exit. Preserve supervisor ownership throughout.

4. **MINOR — Exceptional reasons still are not compared exactly.**  
   [SOURCE13:226](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/pa19-full-k1-v6-source-review-v1/snapshot/13-src-check_m2_ms09_k1_v6.py:226) checks substring membership; `SOURCE13:858` checks a generic prefix. Injection markers, the intended trip, and definite-versus-uncertain cleanup now establish substantially better attribution, but the advertised exact-reason assertion remains incomplete.

   **Repair:** compare the complete expected `unknown_reason` and `lifecycle_error` against the corresponding injected `RuntimeError` representation.

The **v5 production publication race is repaired on the reviewed Python return/exception paths**: [SOURCE05:340–358](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/pa19-full-k1-v6-source-review-v1/snapshot/05-src-m2_native_staged_v6.py:340) sets stop, joins registered feeders before copying records, and records unsettled feeders as lifecycle failures ahead of cap/bounded fallback. The added settlement waits are bounded to 30 seconds each. Write-error provenance and independent close-error precedence remain intact (`SOURCE05:77–116,220–245`).

Termination signals can bypass Python cleanup; owner/supervisor handling still prevents ordinary acceptance and persists a safety/integrity hold (`SOURCE06:50–74,137–157`). Thus signal safety remains fail-closed, without guaranteeing feeder receipts after termination.

The UNSAT/QUALIFIED acceptance predicate is unchanged apart from version identities (`SOURCE07:64–127`; `SOURCE11:97–113`). Both frozen contracts bind the supplied v6 source hashes. The supplied diffs show no unrelated substantive changes. Active production paths retain exclusive publication, SIGTERM-only cleanup, explicit ownership settlement, no automatic retry, and no setuid helpers.

Controls remain **NOT_RUN**, with no observed receipt (`SOURCE03:4,148`).