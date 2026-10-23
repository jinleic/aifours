# Plan E12 (frozen before running; host clock 2026-10-18T06:17:16-0700)

Reproducible version of an eval-session aid quoted in proof-B0SPP-r1.md Sec. 4(3) (aid only, no claim): for the thin B = 0 datum
p = 13, kappa = 3, k = 19, runs r = (1,0,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,1,1) (empty runs at positions 1, 4, 7, 10, 13, 16), enumerate
value assignments u (genuine at empty runs, u_k fixed by sum u = 0) depth-first with every cyclic interval checked against its
Lemma H0 window, cap 400,000 DFS nodes; for every interval-feasible leaf record J = (sum of singleton representatives)/p - 1.
Also for 20 interval-feasible leaves (the first ones) test all 2^19 - 2 patterns with the H0 windows and record whether some
pattern kills.  One process, ulimit -t 900, output out/e12_thin_dfs.json (x).
