# Plan E16: p = 11, B = 0, regime III, random run data with an exhaustive residue search per datum (pre-registered before running; file mtime authoritative)

Owner OlsonReflectionRigidity.  This is a finite aid and not a premise.  It follows plan-E15c.md.
Question.  At p = 7 every tested regime-III cell had no survivors once intervals plus 2- and 3-interval patterns were imposed;
in IIIa there were at most 2 survivors after intervals and 2-patterns.  Is the same seen at p = 11?
Cells (kappa, k, R), B = 0, k >= p + 1, Delta <= kappa - 1, regime III:
- deep IIIa (2 kappa < R <= 4 kappa - 5): (4, 19, 11), (5, 19, 13), (6, 19, 15), (7, 19, 17);
- IIIb (R <= 2 kappa): (6, 22, 12), (7, 21, 15).
Data.  Per cell, 40 run data are drawn uniformly (seeded) from the P0-valid sequences (e_R <= 2 kappa).  The draw is by
rejection from random compositions; data are not deduplicated up to rotation.
Search.  code/e16_p11_sample.py.  For each datum, the DFS of code/e15c_census.py (search3: every interval, every 2-pattern,
every 3-pattern ending before the last run) runs exhaustively over u in Z_11^k.
- Every leaf is tested with killed_by for m = 2, 3, 4.
- A leaf not killed by m <= 4 is recorded as "unkilled at m <= 4".  That is NOT an avoider claim: a full 2^k check is
  infeasible at k ~ 20 in this budget.
- At most 400 s of CPU per cell; the DFS node count is recorded.
Recorded per cell: the number of data done, the nodes, the leaves after pruning, the histogram of minimal m (2..4 or ">4"),
and examples.
One process, run after the current E15c chunk ends.
