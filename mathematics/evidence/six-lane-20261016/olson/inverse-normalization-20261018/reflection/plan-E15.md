# Plan E15: exhaustive search for "2-avoiders" in the p = 7 cell (kappa, k) = (3, 13), and a full avoidance check of survivors (pre-registered before running)

Owner OlsonReflectionRigidity.  Pre-registered 2026-10-18 ~08:25 PDT.  This is a finite aid and not a premise.  Its results are not
a universal statement.
Representation (new since E13).
- B = 0, all blocks odd.  A word is determined, up to block lengths, by its run masses r_t and its run residues u_t in Z_p, with
  u_t != 0 at empty runs and sum u_t = 0.
- Avoidance depends only on (r, u, kappa), through the H0 windows of the B0S-r4 Imports paragraph:
  I(P) = [-g_m(R - E), g_m(E)], g_m(E) = min(p - m, E + m - kappa - 1, floor(E/2)).
- A "2-avoider" is an assignment in which every proper interval and every 2-interval pattern avoids its window.
Cell.  p = 7, kappa = 3, k = 13, R = 7: seven runs rho_1 and six empty runs.  All 132 run data up to rotation are used (as E13).
Search.
- An exhaustive depth-first search over u in Z_7^13 enforces every interval and every 2-interval pattern as soon as it lies
  inside the assigned prefix.
- At a leaf it enforces sum u = 0, and every wrapping interval and 2-pattern through its complement.  A wrapping pattern's
  complement is a linear pattern with the same number of intervals.
- Every surviving 2-avoider is tested against ALL 2^13 patterns.  This decides avoidance exactly, given H0.
Recorded.
- The number of DFS nodes.
- The number of 2-avoiders.
- The number of full avoiders, with each one's (r, u) if any exist.
- For 2-avoiders that are not avoiders: a histogram of the minimal killing m.
Decision use.
- If there are 0 full avoiders, the cell has no RES_<(7) avoider with B = 0.  This is a finite statement and an aid only.
- If there are 0 2-avoiders, it supports a lemma "intervals + 2-patterns suffice" for this regime.
- A full avoider would be reported immediately to Main, as a candidate counterexample to REFL-RES(7), with no claim beyond the
  computation.
Code: code/e15_two_avoiders.py.  Runs under ulimit -t; one process.
