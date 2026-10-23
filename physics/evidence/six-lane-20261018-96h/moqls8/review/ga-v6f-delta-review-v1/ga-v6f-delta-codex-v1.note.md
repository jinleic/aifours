VERDICT: HOLD

| Finding | Status | Evidence |
|---|---|---|
| **03a-1 — bookkeeping and ownership scope** | **REPAIRED** | Ownership state precedes spawn; one scope encloses spawn, subsequent work, waiting and settlement. `snapshot/10-launch_ga_v6f.py:148–162,208–242`. |
| **03a-2 — enforcement wording** | **REPAIRED** | Metadata correctly identifies the driver’s calling thread and pipeline loop. `snapshot/10-launch_ga_v6f.py:180–186`. |
| **03b-1 — GA terminal deadline veto** | **REPAIRED** | Reap records both clocks; late completion sets a safety-stop reason, which vetoes PASS. `snapshot/00-replay_v6f.py:1591–1595,1876–1887,1954–1963`. |
| **03b-2 — launcher interruption** | **REPAIRED** | Non-raising SIGINT/SIGTERM/SIGHUP handlers precede spawn. POSIX exec resets these caught dispositions to default; the mask is inherited unchanged. Python and the driver subsequently install their own handlers. No mask-changing operation appears here. `snapshot/10-launch_ga_v6f.py:51–52,157–162`; `snapshot/00-replay_v6f.py:2430`. |
| **03b-3 — failed registration stops driver** | **PARTIAL** | Writing/announcing failures trigger one owned SIGTERM, waiting and exit 4. Earlier publication-preparation failures bypass that stop. Polling also loses an already-reaped status. NEW 1–2. `snapshot/10-launch_ga_v6f.py:164–214,243–246`. |
| **03b-4 — identical quantized end** | **REPAIRED** | One millisecond value feeds environment and record. Driver validation makes its subsequent `min()` select that same supplied value. NEW 3 concerns admission arithmetic. `snapshot/10-launch_ga_v6f.py:137–147,180`; `snapshot/00-replay_v6f.py:2393–2400`. |

1. **NEW — MAJOR: registration failure handling starts too late.**  
   Console-descriptor closing and construction of `rec` occur before the inner publication handler. An exception there—for example, an I/O error closing the console descriptor or an allocation failure constructing metadata—reaches the outer handler, which only appends an error. `finally` then waits without signalling the driver. A valid driver can therefore pass its admission gate and execute natives while its reserved launch record remains empty. Eventual exit 4 does not repair the missing immediate registration.

   Cover **every** failure between successful spawn and successful publication with the same one-shot owned SIGTERM, followed by reap and settlement. Evidence: [10-launch_ga_v6f.py:164](/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261018-96h/moqls8/review/ga-v6f-delta-review-v1/snapshot/10-launch_ga_v6f.py:164), [10-launch_ga_v6f.py:198](/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261018-96h/moqls8/review/ga-v6f-delta-review-v1/snapshot/10-launch_ga_v6f.py:198), [10-launch_ga_v6f.py:206](/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261018-96h/moqls8/review/ga-v6f-delta-review-v1/snapshot/10-launch_ga_v6f.py:206).

2. **NEW — MINOR: `poll()` can consume the settlement status.**  
   On publication failure, `child.poll()` may reap an already-exited driver and cache its return code. The unconditional raw `os.waitpid()` then raises `ChildProcessError`; `state["status"]` remains `None`, and settlement omits the available exit code or terminating signal. This branch fails closed, but complete exit/signal settlement is **NOT ESTABLISHED**. Preserve the polled return code or consistently use the `Popen` object’s cached waiting mechanism.

   Evidence: [10-launch_ga_v6f.py:203](/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261018-96h/moqls8/review/ga-v6f-delta-review-v1/snapshot/10-launch_ga_v6f.py:203), [10-launch_ga_v6f.py:209](/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261018-96h/moqls8/review/ga-v6f-delta-review-v1/snapshot/10-launch_ga_v6f.py:209), [10-launch_ga_v6f.py:220](/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261018-96h/moqls8/review/ga-v6f-delta-review-v1/snapshot/10-launch_ga_v6f.py:220).

3. **NEW — MINOR: quantization creates spurious launch refusals.**  
   Away from the fixed cutoff, the unrounded runway is exactly `CHILD_END_LIMIT = BACKSTOP + 360 = 10620`. Whenever millisecond rounding rounds downward, `chunk_end - now < 10620`, so the next condition refuses an otherwise fitting launch. For example, fractional time `.0004` loses approximately 0.4 ms. Align the fit calculation with the quantization policy while preserving the deadline bounds.

   Evidence: [10-launch_ga_v6f.py:47](/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261018-96h/moqls8/review/ga-v6f-delta-review-v1/snapshot/10-launch_ga_v6f.py:47), [10-launch_ga_v6f.py:134](/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261018-96h/moqls8/review/ga-v6f-delta-review-v1/snapshot/10-launch_ga_v6f.py:134).

Verified:

- All **16 manifest-listed SHA256 values match**. Only static reading, comparison and hashing were used; no source execution, writes or delegation.
- Paired source-region hashes confirm unchanged **ACCEPTANCE, `evaluate()`, all five controls and their CNFs, base regeneration, strengthened construction/binding after the additional historical pins, measured writers, relay, CR-only parsing, helper supervision and control validation**.
- Formula solver/checker feeds still share the same bound parts (`00-replay_v6f.py:1212–1219`). PASS retains both measured CNF feeds, complete clean relay transport, positive equal producer/delivered counts and hashes, checker-consumed count equality, native verdicts and supervision vetoes (`:1923–1989`). A separately measured consumer SHA256 remains **NOT ESTABLISHED**.
- No new driver false-PASS path or silent native-survivor path was identified in the inspected delta. Late reaps now veto acceptance; unreaped survivors retain explicit reporting (`00-replay_v6f.py:1787–1817,1876–1888`).
- No operative **2026-10-18 deadline** remains. Current driver and launcher cutoff constants use October 22 (`00-replay_v6f.py:256–257`; `10-launch_ga_v6f.py:45–46`).