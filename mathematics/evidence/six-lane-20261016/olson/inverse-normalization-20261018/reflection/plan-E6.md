# Plan E6 (frozen before running; host clock 2026-10-18T03:30:57-0700)

Context: proof-RED-r1.md reduces REFL(p) to REFL-RES(p) (no avoider in RES_<(p), kappa >= 2).  An exact census of RES_<(7)
for k >= 10 is NOT run: the run-data count alone is ~1.4e8 (eval estimate 03:2x PDT) and an eval prototype at 03:2x showed
hundreds to tens of thousands of interval-feasible value assignments per run datum in the kappa = 6 (H = 0) slices, each needing
a full 2^k-pattern check.  E6 replaces the census by two pre-stated, discriminating questions:
 Q1 (failed-route record): can cyclic-interval patterns (m = 1) plus the zero pattern alone certify RES_< words?  Statistic:
    number of interval-feasible value assignments per sampled run datum (capped).
 Q2 (counterexample probe): is any interval-feasible assignment of a sampled RES_< run datum an avoider?  Every assignment kept
    is decided by the raw DP dp1 (and dp2 for any NO answer); any avoider is a candidate counterexample to REFL(p): explicit word,
    both DPs, hash-pinned JSON, parent notified immediately.  A miss is UNKNOWN, never a proof.
Design: p in {7, 11}; seeded random run data of RES_<(p) (all blocks odd with only H relevant -- all pairs in one block; runs pure or
empty; g >= 1; 0 <= B < kappa; kappa >= 2; A >= B; A <= 2p - 1; (Z0) k >= 2 kappa - B + 1; (P0) g + #even nonempty runs <= 2 kappa),
stratified over (kappa, B, k); interval DFS over values y (y_k = 0) with genuineness at empty runs; per run datum at most C1
assignments decided by DP (random value order).  Positive control: the same DFS + DP pipeline applied to the sharpness run datum
(length 4p - 3: blocks 1 and 2p - 1, runs rho_1^(2p-3) and empty) must find an assignment that the DP confirms AVOIDS.
Caps: one process, ulimit -t 1800, output <= 5 MB, statvfs gate before launch.
Code: code/e6_interval_probe.py; output: out/e6_interval_probe.json (exclusive create).
