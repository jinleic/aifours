<!-- Parent-commissioned hostile SOURCE review (reviewer subagent PA19K1SourceReview), recorded verbatim by the parent at 2026-10-18T04:31:19-07:00. Inputs: source pack 8825589b46c8c2df711f6b778edf7137fa77a00f086fa7b3b5f583b0fa445bd8, delta 9a664d69c26c3a39f67c52aff1eb1ee4853412349a6b07dd1261c5da2e4b1cc5. Read-only; no execution. -->

# HOLD

**Overall correctness: incorrect.** The new route does not yet enforce the stated production acceptance and admission contract. Exact interval accounting is substantially stronger than the previous runner, but the qualification, invalid-result routing, and exceptional-cleanup gaps below prevent production authorization.

**Confidence: 0.98.** This was a source-only review: no lane code, controls, builds, or native solvers were executed; no files were changed.

## Snapshot verification

All **eight supplied file SHA-256 values matched**: the source pack, delta, and six live sources. I also independently hashed each of the **six decoded source strings embedded in the pack**; each matched both its declared digest and the corresponding live source.

The findings below are anchored in the new runner’s delta. Where implementation resides in unchanged `stream_check15.py`, I distinguish that inherited implementation from the new route’s missing integration safeguards.

## Findings

### 1. BLOCKER / P1 — Retain cleanup ownership until every native child is reaped

**Location:** [run_m2_ms09_k1.py:134–139](/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261016/packing-array19/src/run_m2_ms09_k1.py#L134-L139)  
**Confidence:** 0.99

The new wrapper catches any exception from the staged call and proceeds to publish an UNKNOWN, but it has no ownership-cleanup backstop. The inherited exceptional path is unsafe: `stream_check15._start()` can raise after registering a child—for example, if starting the collector thread fails—and `Token.__exit__()` then calls `quarantine()` without first terminating that child. For checker exceptions, `BigLock.__exit__()` releases the big-memory lock before this cleanup. Worse, `quarantine()` writes its receipt before entering its wait loop; an `OSError` there escapes cleanup. The runner subsequently exits, releasing its token descriptor while the child can remain alive. **Fix:** use a reviewed lifecycle implementation that covers every post-spawn exception, SIGTERMs the owned child, performs the bounded wait, and retains token/big-memory capacity through survivor quarantine and reaping even when quarantine-receipt publication fails. The defensive pattern already exists in `enumeration_helper_guard_v3.py:38–78,196–210`; it is not applied to this proof pipeline.

### 2. BLOCKER / P1 — Require measured completion of both CNF feeds

**Location:** [run_m2_ms09_k1.py:125–132](/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261016/packing-array19/src/run_m2_ms09_k1.py#L125-L132)  
**Confidence:** 0.99

The pre-child pin records the constructor buffer’s hash and length, but neither the solver’s nor checker’s CNF delivery is measured. Inherited `_writer()` (`stream_check15.py:376–381`) swallows write/close errors, and its callers merely perform timed joins (`491`, `551`) without requiring successful completion. The new predicate checks the constructor hash/count (`m2_ms09_evidence.py:60–62`), not delivered CNF bytes. Consequently, a failed or incomplete CNF writer is invisible to qualification; the recorded hash does not establish the required native-input binding. Final formula regeneration reproduces the intended buffer, not its historical delivery. **Fix:** record successful-delivery byte count, SHA-256, completion, and error state separately for both CNF feeds, require writer completion and successful flush/close, and require both measurements to equal the pre-child pin before qualification.

### 3. BLOCKER / P1 — Enforce the complete admission gate before each native spawn

**Location:** [run_m2_ms09_k1.py:79–85](/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261016/packing-array19/src/run_m2_ms09_k1.py#L79-L85)  
**Confidence:** 0.99

The projected-growth and additional-data-cap checks run only during initialization, before subsequent token waits, construction, solving, and possible big-memory-lock waits. The actual solver/checker admissions use inherited `admitted_reason()`, which checks STOP/ABORT and the fixed **12,334,217,728-byte** threshold, plus the budget overlay—not that threshold **plus projected growth**. Thus a later reading equal to the fixed threshold admits a native even when retained growth remains positive. Neither native admission checks lane RSS, and the live token count is not constrained to the contract’s ceiling of two: `token_count()` accepts any nonnegative integer. **Fix:** install a post-lock, immediate-pre-spawn gate for both native types that revalidates current accounting and retained growth, fresh free space, fail-closed RSS/headroom, the token ceiling/ownership, and deadlines. Do not treat the initialization receipt as a reservation. The earlier growth wrapper’s `guarded_spawn()` provides an existing placement pattern.

### 4. MAJOR / P1 — Require the solver’s exact UNSAT status line

**Location:** [run_m2_ms09_k1.py:160–162](/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261016/packing-array19/src/run_m2_ms09_k1.py#L160-L162)  
**Confidence:** 0.99

Qualification never checks for exactly `s UNSATISFIABLE`. `stream_check15.py:484` derives status solely from the return code, and line `489` discards non-SAT solver output; the new predicate at `m2_ms09_evidence.py:42–43` accepts `status=UNSAT`, self-exit, and rc 20 without any parsed solver status lines. Missing, contradictory, or duplicate solver verdicts therefore cannot be rejected by this route, contrary to the frozen solver acceptance rule. **Fix:** retain the completed collector’s parsed solver status lines and require exactly `['s UNSATISFIABLE']` together with rc 20 and self-exit. Make collection failures disqualifying. Existing receipts lacking this evidence need an explicit parent disposition; the missing observation must not be fabricated during rebinding.

### 5. MAJOR / P1 — Propagate invalid proof results as vetoes

**Location:** [run_m2_ms09_k1.py:165–169](/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261016/packing-array19/src/run_m2_ms09_k1.py#L165-L169)  
**Confidence:** 0.98

Every non-SAT qualification failure is converted to UNKNOWN, including an actual invalid proof such as solver rc 20 followed by checker `s NOT VERIFIED`. The loop’s stop condition at `183` does not include these failures, so production continues. This distinction is also lost across the new reader boundary: `E.inspect()` returns `UNQUALIFIED` for predicate failures (`m2_ms09_evidence.py:97–102`), whereas `C.inventory()` adds new-record integrity issues only for `INVALID` (`317–319`), and the resume loop vetoes only `INVALID` or `SAT` (`110–114`). These records are correctly **not counted**, but invalid results do not exercise the required veto. **Fix:** distinguish ordinary bounded UNKNOWN outcomes from invalid verdicts, identity inconsistencies, and corrupted evidence; preserve that classification through publication, inspection, inventory, and resume dispatch. Invalid outcomes must stop further admission and populate the integrity veto.

## Other acceptance areas

| Area | Static assessment |
|---|---|
| **Normal process lifecycle** | Normal solver/checker completion uses `wait()`/`poll()` before token release. Ordinary termination survivors retain the token while waiting. The exceptional paths in finding 1 prevent an unconditional cleanup PASS. No SIGKILL or `Popen.kill()` path was found in the inspected route. |
| **Deadlines and locks** | The existing budget overlay checks allowance after token acquisition and after big-memory-lock waits, and interrupts childless waits. Quarantine intentionally can outlast the chunk deadline; it must remain UNKNOWN and retain capacity. |
| **Checker verdict and DRAT replay** | Checker parsing strips only `\r` and requires exactly `['s VERIFIED']`, rc 0, self-exit, and successful replay. `NOT VERIFIED`, `TIMEOUT`, duplicate status lines, and replay failures do not qualify. Proof replay has measured bytes/hash and completed-frame checks; **CNF feeds do not**. |
| **Exact coverage** | `verify_sources()` reconstructs canonical B100 intervals from the pinned complete denominator, checks exact interval lists and identities, and verifies the frozen phase authority. Inventory counts interval sizes once rather than importing legacy aggregate counters. |
| **Seven reservations** | The exact seven IDs are enforced, excluded from compute order, and checked for forbidden production duplicates. Inventory leaves them reserved without the parent-owned exact-input reuse disposition—including the calibration interval that also has an original baseline receipt. |
| **Receipt-before-count** | Publication writes the pin before native execution, then publishes the commit before the primary record using no-replace hardlinks. `inspect_new()` requires and binds both companions before accepting the primary. Missing or mismatched companions fail closed. |
| **Final reconstruction** | Without `--verify-formulas`, final closed-case counts remain zero and final readiness remains false. Final mode regenerates consumed formulas; readiness additionally requires all 71 component cases resolved, no veto/issues, and dispositions for all seven reservations. B3 remains separately classified as parent mathematics, not DRAT. Findings 2, 4, and 5 weaken the underlying evidence contract. |
| **Disk and resource caps** | I found no direct regular-file CNF/proof write in this route: CNFs use FIFOs, compressed proof chunks remain in memory, and replay goes to checker stdin. The new regular outputs are metadata and possible SAT-model text. Raw/compressed proof caps remain unchanged. However, native RSS sampling only records peaks, and the external watchdog pauses future admissions rather than enforcing an in-flight stop; the stated RSS/free-floor guarantees therefore are not established by this runner. |

## Controls required before production

These are **requirements for the parent, not tests exercised in this review**.

1. **Exceptional lifecycle:** inject failures immediately after solver/checker registration, during thread startup, and during quarantine receipt open/write. Include a SIGTERM-resistant child that later exits. Independently observe that token—and applicable big-memory lock—cannot be acquired until the owned child is reaped; require UNKNOWN and no next native.

2. **Admission boundaries:** separately test solver and checker admissions after token/big-memory waits. Change free space between initialization and spawn; test required threshold minus one and exact threshold, positive projected growth, unknown accounting/RSS, RSS above the ceiling, and COUNT above two. Require zero native starts on refusal. Also exercise expired allowance and an in-flight floor/read failure.

3. **CNF delivery:** independently truncate, fail, or stall each CNF writer while a controlled child emits nominal success statuses. None may qualify. A successful case must show matching measured hashes/counts for **both** feeds.

4. **Native verdicts:** test rc 20 with missing, duplicate, SAT, or contradictory solver status lines. For the checker, test CR-prefixed valid output, `NOT VERIFIED`, `TIMEOUT`, duplicate verdicts, leading-space near-matches, and nonzero rc. Include a tiny satisfiable CNF with an invalid proof as a real negative checker control.

5. **Veto routing:** feed a completed `NOT VERIFIED` outcome through the actual runner → receipt → `inspect_new()` → inventory → resume path. Require a persistent invalid-result veto, zero counted coverage, and no next attempt. Separately confirm ordinary timeout UNKNOWN remains preserved, uncounted, and never automatically retried.

6. **Coverage and publication:** exercise omitted/overlapping/duplicated intervals, final partial B100 intervals, all seven reservations, partial/wrong parent overlays, wrong formula/list hashes, missing pin/commit, publication collisions, and interruption between publication steps. Require no false final closure; retain the exact B3-only empty-cover exception.

7. **Resource/I/O observation:** for the corrected controlled pipeline, inspect actual output file types and retained-byte accounting, including staging hardlinks. Confirm no regular-file CNF/proof retention and record process/RSS observations without presenting sampled peaks as proof of an instantaneous hard cap.

**Disposition:** fix and re-review these source paths before freezing the production contract. The current metadata-control script is useful, but passing it alone would not address the native lifecycle, delivery, or admission gaps above.
