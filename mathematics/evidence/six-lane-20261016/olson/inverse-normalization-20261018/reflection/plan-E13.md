# Plan E13 (frozen before running; host clock 2026-10-18T06:26:08-0700)

Aid for the open regime (III) R <= 4 kappa of B = 0, k >= p + 1 (proof-B0SPP-r4.md Sec. 4(2)); no claim.  Family p = 7, kappa = 3,
k = 13, R = 7 (forced: six empty runs and seven runs rho_1, P0 tight).  For every run datum up to rotation (positions of the six
empty runs), enumerate interval-feasible value assignments depth-first (every cyclic interval checked against its Lemma H0 window;
genuine empty runs), at most 20,000 DFS nodes per datum; for the first 30 interval-feasible assignments of each datum test all
2^13 - 2 patterns with the H0 windows and record the least number m of intervals of a killing pattern (or "none").  Also record
J = (sum of singleton representatives)/p - 1 for every enumerated assignment.  One process, ulimit -t 1500, output
out/e13_regime3_p7.json (x).  A datum with an assignment that no pattern kills would be a candidate counterexample: raw DP, parent.
