DISPOSITION: ACCEPT-WITH-FIXES

1. **MAJOR — The validator can apply bytes it never hash-checked.** [k4_orbit_r2.py:54](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/moqls8-k4-orbit-parent-inputs-v2/code/k4_orbit_r2.py:54) hashes the files, then [line 74](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/moqls8-k4-orbit-parent-inputs-v2/code/k4_orbit_r2.py:74) reopens the arrays. Receipts likewise undergo separate hash and parse reads.

   I reproduced this entirely in memory: the first `g1` read returned pinned bytes; the second returned those bytes with entries 57/106 exchanged. Validation accepted **`c022 ← c037 via g1` with no problems**. Both pinned generators fix variables 57 and 106, so no pinned word maps these cubes. The substituted map is demonstrably not an automorphism: base clause `(-1625, -57)` maps to `(-3193, -106)`, absent from F4.

   **Fix:** read each artifact once, hash that buffer, and deserialize that same buffer. Add a replacement-between-reads regression.

2. **MINOR — The 14 controls omit the central r2 regressions.** [k4_orbit_controls.py:65](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/moqls8-k4-orbit-parent-inputs-v2/code/k4_orbit_controls.py:65) supplies five positive and nine negative controls. It does not test full-path versus incremental literals, strict-source unit/hash mismatches, literal bounds, truthy nonboolean verdicts, refined-source partitions, or combined refinement/orbit cycles. M7 changes the expected pin before loading; it misses finding 1.

   My additional in-memory probes correctly rejected those malformed cases. Preserve these probes in the control suite and reissue its receipt.

3. **MINOR — The frozen package lacks replay dependencies.** [k4_orbit_r2.py:210](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/moqls8-k4-orbit-parent-inputs-v2/code/k4_orbit_r2.py:210) imports missing `code/k4_cover.py`; direct invocation raises `FileNotFoundError`. The controls need that adapter plus ledger/pilot inputs absent from the manifest. Include or explicitly pin these dependencies. To replay the 14 controls, I used the pinned `k5_cover.py`, applied the K4 constants in memory, and read the external ledger/pilot receipts.

All 12 manifest hashes and sizes match. Independent streaming verification confirmed the base hash, strict DIMACS parsing, and **exact clause-multiset equality for both generators across all 5,833,793 clauses**; peak RSS was **0.78 GiB**. Both arrays are total positive bijections, fix 0, preserve literal polarity, and satisfy the S3 relations with closure size six. Both checker implementations perform genuine exact multiset comparisons.

With stable artifact reads, the full-path, strict-receipt, partition, settledness, acyclicity, evidence, and terminal-leaf checks passed inspection and targeted probes. The r2 DRAT qualification is correct, and the false depth restriction is withdrawn; its depth-four example checks exactly.