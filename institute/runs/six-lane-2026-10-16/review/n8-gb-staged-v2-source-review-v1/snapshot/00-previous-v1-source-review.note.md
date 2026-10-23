**CONTROL SOURCE: GO-WITH-FIXES — BLOCKING.** Frozen runtime `b36fbb57…8151` is **not cleared to run the seven native controls**.

**SCIENCE: HOLD.**

All 27 supplied hashes and byte counts match. This audit used snapshot reads and hashes only.

Six **MAJOR** findings require repair:

1. **Negative controls can falsely qualify on native failures.** `truncate`, `suffix`, and `digest-alter` permit failures of the entire checker-verdict group; the evaluator accepts those failures without distinguishing rejection from timeout or abnormal termination. The pinned checker’s timeout prints `s TIMEOUT` and exits **0**. Fatal/error counters are also collected without becoming acceptance vetoes.  
   **Repair:** require an allowed exact status/normal-exit pair, independently veto timeout, signals and fatal diagnostics, and narrowly preregister intended negative-control diagnostics. See **SOURCE00:238–257, 1447–1454, 2036–2053, [2142](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/n8-gb-staged-v1-source-review-v1/snapshot/00-runtime-gb_staged_v1.py:2142)–2151; SOURCE15:905**.

2. **Reaped PIDs can remain eligible for signaling.** After `wait4()` reaps a child, constructing its `done` record can throw. Cleanup tests only membership in `done`, then signals that already-reaped PID, potentially after reuse. Initial `procs[...] = Popen(...)` also depends on allocating a new dictionary entry after spawn.  
   **Repair:** preallocate child ownership slots; mark reaped state before diagnostics; never signal or wait again once reaped. See **[SOURCE00:1599](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/n8-gb-staged-v1-source-review-v1/snapshot/00-runtime-gb_staged_v1.py:1599)–1629, 1823–1825, 1877–1880**.

3. **FD exception safety remains incomplete.** `os.open()`/`os.pipe()` precede allocating registry insertions; failed registration can leave untracked descriptors. The feeder’s finalizer allocates a `range`/iterator and clears chunks **before** closing its claimed FD; failure there bypasses closure.  
   **Repair:** protect newly acquired descriptors until registration commits; put feeder closure in an unconditional nested `finally` before buffer cleanup or diagnostics. See **SOURCE00:1201–1205, [1358](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/n8-gb-staged-v1-source-review-v1/snapshot/00-runtime-gb_staged_v1.py:1358)–1365, 1805–1811, 1866–1870**.

4. **Signal/cutoff checks do not cover actual spawn and publication.** Checker setup and thread launch occur after its last stop/cutoff check. A SIGTERM during evaluation can leave a PASS verdict; one after `stop_latched_after_evaluation` is sampled can leave both receipt latch fields empty during publication.  
   **Repair:** repeat stop/cutoff checks immediately before spawning, downgrade on late signals, and require a signal-aware final publication/commit record for qualification. See **SOURCE00:1861–1880, [2451](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/n8-gb-staged-v1-source-review-v1/snapshot/00-runtime-gb_staged_v1.py:2451)–2467**.

5. **GB exclusion misses orphaned checkers.** A foreign GB `drat-trim` whose driver exited has neither a Kissat name nor a GB-driver argument, so it receives no exclusion. Also, completion can bypass processing the scanner’s newest exclusion reading.  
   **Repair:** identify foreign GB natives through their working directory/ownership and latch exclusions in the scanner through completion. See **[SOURCE00:531](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/n8-gb-staged-v1-source-review-v1/snapshot/00-runtime-gb_staged_v1.py:531)–543, 1666–1687**.

6. **Resource enforcement has gaps.** In-flight busy counts are recorded without enforcing `other_busy + 1 <= 4`. The fresh pre-spawn disk check accepts `FLOOR`—12e9—rather than the launch threshold 12.2e9 plus growth.  
   **Repair:** enforce the busy cap in flight and apply the launch threshold at the final launch boundary. See **SOURCE00:1654–1664, 1715–1732, [1766](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/n8-gb-staged-v1-source-review-v1/snapshot/00-runtime-gb_staged_v1.py:1766)–1777**.

The seven control designs, checked against **SOURCE15:983–994, 1052–1185, 1265–1267, 1480–1500** and **SOURCE00:2074–2151**:

| Control | Static judgment |
|---|---|
| UNSAT | Full PASS and one formula-phase duplicate warning are feasible; diagnostic veto needs repair. |
| SAT-checker | Exact NOT VERIFIED with normal exit 1 is feasible and correctly required. |
| shortCNF | Removing the final LF can still yield VERIFIED/0; measured incomplete delivery correctly rejects it. |
| Truncated proof | Native VERIFIED remains possible; byte equality must reject it. Currently susceptible to finding 1. |
| Suffix | Parser continues beyond the empty clause; `N = D = R + 5` is feasible. Finding 1 applies. |
| Altered digest | Same length and `N = D` can coexist with changed SHA and even VERIFIED. Finding 1 applies. |
| Early close | Missing header exits 0 before proof parsing; held delivery then receives EPIPE. The expected mechanism is feasible. |

I found no source-demonstrated impossible preregistration. Actual native outcomes remain unestablished.

Independently audited: the exact 12+6 allowlist, own GB allocator and RAM composition, GBBINDING/header/piece checks; both measured CNF feeds; collector EOF, buffer/feed SHA and counts, checker `N`; singleton statuses; raw-output hashing and exact duplicate filter; staging, thread handoff, helper/scanner settlement, GO binding, guards and retry prevention. The 6 GiB/11 GiB RSS calculations include driver-held buffers; the frozen monitor-window calculation matches SOURCE25.

Imports remain the historical GBBINDING measurements, unavailable binder inputs, executable/build identities reported by SOURCE14, and prior mathematical/review conclusions—not independently established native evidence.

**BLOCKER for science:** [SOURCE05:22](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/n8-gb-staged-v1-source-review-v1/snapshot/05-SELFCHECK-gbs1-v1b.json:22) explicitly identifies stubs. After repairs and renewed source review, controls need a separate parent GO bound to the new script/PRE-EXEC and ordered seven items. Science remains HOLD until all seven real receipts are independently checked and each science item receives explicit GO. No n8 correctness or novelty claim.