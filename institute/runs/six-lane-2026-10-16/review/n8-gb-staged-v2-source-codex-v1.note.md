**CONTROL SOURCE: GO-WITH-FIXES — BLOCKING.** SOURCE02 `89db9635…2844` is not cleared for native controls.

**SCIENCE: HOLD.**

All 19 supplied hashes and byte counts match. Review used snapshot reads and hashes only.

Three **MAJOR** defects remain:

1. **F3 — descriptors can escape before `acquire()` receives them.** At **SOURCE02:1964, 1967, 2027**, `(os.open(...),)` allocates a tuple **after** opening the FD. If that allocation raises `MemoryError`, `got` remains `None` at **1649**, so **1656–1660** cannot close the descriptor. The feeder’s nested finalizer is repaired.  
   **Repair:** use a single-FD acquisition helper that stores the scalar FD inside its cleanup scope before allocating any wrapper. Add fault injection between open and registration; SOURCE07:723–739 tests registration failure only.

2. **F4 — signals during commit publication can leave authoritative qualification true.** **SOURCE02:2695** samples the signal before constructing and writing the commit at **2697–2704**. SIGINT/SIGTERM after that sample, including during commit serialization, leaves `qualified: true`; **2718** merely stops further work. Admission at **1247–1265** accepts that commit. SOURCE07’s H5 injects before the sample, missing this window.  
   **Repair:** prepare the commit before the final signal decision, then use a protected publication step with an explicit linearization point and latched/pending-signal handling. Cover both signals during commit preparation/publication.

3. **F4 — “receipt durable” is not established.** [SOURCE02:445](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/n8-gb-staged-v2-source-review-v1/snapshot/02-runtime-gb_staged_v2.py:445) closes and re-hashes the JSON file; it performs no file or directory durability operation. Consequently **2694–2704** can publish qualification before the receipt is durable.  
   **Repair:** flush and sync the receipt and its directory before commit publication; make durability failures fail closed, and define durable commit publication too.

The previous findings otherwise resolve as follows:

| Finding | Source judgment |
|---|---|
| **F1 closed** | Independent self-exit/signal, TIMEOUT, outcome and fatal-diagnostic vetoes at SOURCE02:2300–2327; science independently requires no timeout/fatal diagnostic at 2208–2210. `may_fail` cannot bypass these. |
| **F2 closed** | Preallocated ownership slots; reaped flag and `returncode` set before diagnostics, SOURCE02:1718–1721, 1757–1771. Subsequent signal/wait paths exclude reaped children. No PGID signaling/reuse exposure found. |
| **F3 partial** | Registration rollback and feeder closure improved; acquisition gap above remains. |
| **F4 partial** | Both native spawn boundaries, SIGINT/SIGTERM latching, evaluation downgrade and commit-required admission exist. Publication defects above remain. |
| **F5 closed** | Named GB/GA desk/evidence exclusions, orphan and GB-parent checks, scanner-owned exclusion latch and completion/evaluation vetoes: SOURCE02:588–749, 928–940, 1818–1826, 2112–2116, 2230–2236. |
| **F6 closed** | In-flight `busy + 1 <= 4`, both launch thresholds, 12e9 floor, 6 GiB pipeline/11 GiB lane accounting, and frozen monitor window are implemented: SOURCE02:787–847, 1854–1873, 1898–1924. |

The seven controls are consistent with the supplied C parser and current evaluator:

| Control | Static conclusion |
|---|---|
| UNSAT | VERIFIED/0 and exactly one formula-phase duplicate normalization are feasible. |
| SAT-checker | NOT VERIFIED/1 is feasible; complete equal transport remains required. |
| Short CNF | Removing the final LF can preserve VERIFIED/0; measured incomplete delivery rejects it. |
| Truncated proof | VERIFIED/0 or NOT VERIFIED/1 remains possible. `N ∈ {D,D+1}` matches EOF handling; only the preregistered `no conflict` diagnostic is permitted. |
| Suffix | Parsing continues beyond the empty clause; `N = D = R+5` is feasible. Changed transport rejects it. |
| Altered digest | `N = D = R` can coexist with VERIFIED and a changed digest. Equality rejects it. |
| Early close | Header error exits 0 before proof parsing; releasing the feeder after reap produces the intended zero-byte EPIPE. |

These conclusions follow from **SOURCE11:845–875, 983–994, 1052–1185, 1265–1267, 1466–1500** and **SOURCE02:2250–2362**. I found no source-proven impossible preregistration or remaining F1 native-failure acceptance path. Actual Kissat proof layout and native outcomes remain unestablished.

Independently audited: the exact 12+6 allowlist; RAM regeneration/composition and GBBINDING SHA/bytes/header/piece comparisons; both CNF feeds; staging and settlement; actual collector EOF; collector/buffer/feeder digest and count equality plus checker-consumed count; singleton statuses after CR removal; self-exits 20/0; exact duplicate-warning filtering; direct runtime file writes, retained FIFOs, SIGTERM-only cleanup and overlap guards.

Imported: unavailable binder/encoder implementations, historical binding measurements, binary/build identities and prior mathematical conclusions.

**Science evidence blocker:** [SOURCE08:22](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/n8-gb-staged-v2-source-review-v1/snapshot/08-SELFCHECK-gbs2-v2.json:22) identifies stubs. After repairs and renewed source clearance, science still requires all seven real control receipts and qualified commits independently checked, followed by explicit per-item parent GO. No n8 correctness or novelty claim.