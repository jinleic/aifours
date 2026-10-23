## Outcome: REJECT — frozen revision 10

**Overall correctness: incorrect. Confidence: 0.97.** Resource-admission and proof-stream-binding defects require fixes before resumption. **No false mathematical UNSAT acceptance or actual CPU/RSS excursion was demonstrated** by this source-only audit.

### Findings

1. **MAJOR / P1 — Retain tokens and memory locks while descendants survive.**  
   [stream_check10.py:243–245](/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261016/packing-array19/src/stream_check10.py#L243-L245) returns when a solver survives SIGTERM and the bounded wait; the enclosing context then unconditionally releases its token at lines 91–93. The checker-survivor path similarly releases `BigLock` and the token at lines 289–309. A waiting runner can therefore replace a still-running process, exceeding the admitted CPU capacity; two large surviving checkers can also bypass serialization. Preserve/quarantine the occupied capacity until every associated process/helper has exited. **Confidence: 1.00.**

2. **MAJOR / P1 — Account for compression helpers alongside native processes.**  
   [stream_check10.py:204–206](/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261016/packing-array19/src/stream_check10.py#L204-L206) hashes and compresses proof data in the runner while its solver executes; lines 263–271 similarly decompress/hash while the checker executes. Thus one token can cover two CPU-active processes, not one. `rss_watchdog.py:98–99` counts only native solver/checker processes as busy, excluding this work and extension helpers. COUNT4 cannot establish the requested four-busy-process ceiling. The parent’s subsequently mandated COUNT≤2 addresses this admission risk; no excursion was measured here. **Confidence: 0.99.**

3. **MAJOR / P1 — Stop admissions and target memory owners on an RSS trip.**  
   [rss_watchdog.py:63–69](/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261016/packing-array19/src/rss_watchdog.py#L63-L69) selects only native processes with FIFO timestamps. During token-held CNF construction or extension enumeration, excessive memory can reside in runners/helpers and produce no eligible termination target. Admissions remain open while termination is awaited; COUNT is reduced only afterward, never below one. Consequently, an RSS trip need not stop the memory owner or prevent replacement work. This is an after-exceedance sampler, **not an 8-GiB hard bound**; its full sampling loop can also pause for the 60-second termination wait. **Confidence: 1.00.**

4. **MAJOR / P1 — Recheck cancellation and disk space after acquiring a token.**  
   [stream_check10.py:175–178](/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261016/packing-array19/src/stream_check10.py#L175-L178) starts construction immediately after an arbitrarily long token wait. Runner STOP/disk checks occur before that wait (`run_hard10.py:128–140`, `run_m2_10.py:124–135`), so a waiting fifth runner can start after STOP appears or free disk falls below 12,000,000,000 bytes. Extension-helper acquisitions have the same gap. The existing `disk_guard.py` routes only older runner names/STOP files. Revalidate immediately after acquisition, before any construction or helper launch. **Confidence: 1.00.**

5. **MINOR / P2 — Reject replay write failures before asserting stream equality.**  
   [stream_check10.py:270–279](/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261016/packing-array19/src/stream_check10.py#L270-L279) counts/hashes decompressed bytes before writing them and suppresses write/close errors. Failure while writing the final chunk can therefore leave `replay_sha256_matches=True` despite incomplete delivery. That assertion feeds `checked` and `summarize8.py:48–50`. Record feeding failure separately and require successful complete delivery/closure. This undermines the claimed exact-stream binding; it does **not** demonstrate a false mathematical UNSAT result from standard drat-trim. **Confidence: 0.99.**

6. **MINOR / P2 — Recheck the compressed-buffer cap after flushing.**  
   [stream_check10.py:217–220](/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261016/packing-array19/src/stream_check10.py#L217-L220) appends compressor flush output without checking `MAX_ZBUF` again. A proof crossing 500 MiB only during flush can proceed to certification rather than becoming UNKNOWN. Regular-loop checks are also post-allocation chunk checks, not exact allocation ceilings. **Confidence: 1.00.**

### Certification and compatibility assessment

- Both native consumers receive the same regenerated, hashed CNF bytes. M1 direct aggregation additionally requires `cnf_matches_pass1_sha`.
- The normal UNSAT gate requires solver exit20, no detected proof cap, checker self-exit0, exactly `["s VERIFIED"]` after carriage-return stripping, and replay equality. Solver/checker overlap within one pipeline is prevented. Timeout/nonverified records remain uncertified in aggregation; **lrat-check is not consulted**.
- `summarize8.py` explicitly handles revision10. M1 split records carry explicit indices; M2 endpoint ranges are expanded correctly. No newly introduced claim-key/FIFO collision or dispatch drop was found.
- The saved smoke records genuine checks, two verified SAT controls, native-limit UNKNOWNs, raw-cap UNKNOWN, COUNT1 serialization, and forged-empty-clause rejection. It does not cover survivor quarantine, RSS enforcement, post-wait cancellation/disk checks, replay-write failure, or compressed-flush overflow.
- Five-second checker RSS sampling can record zero for short checks; two-second lane samples cannot establish continuous peak compliance.

**Containment:** the parent reports COUNT0, boundary exits of all four holders, and no observed survivor. Those operational observations were not independently inspected. No files were changed, solvers executed, running processes touched, or live logs polled.
