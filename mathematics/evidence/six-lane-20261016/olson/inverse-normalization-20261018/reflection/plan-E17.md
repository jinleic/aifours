# Plan E17: interval-level SIGMA in gap-(a) cells (pre-registered before running; file mtime authoritative)

Owner OlsonReflectionRigidity.  This is a finite aid and not a premise.
Question.  In cells with R >= 4 kappa - 4 where Corollary 2 of B0S-CJ''' fails numerically, do interval-feasible data still have
J = 0 and c = 0 on all intervals?  Two all-ones families:
- (p, kappa, R) = (13, 4, 13): k = 21, Delta = 3;
- (p, kappa, R) = (29, 7, 29): k = 43, Delta = 6.
If J != 0 appears there, these cells need multi-interval kills, as regime III does.
Method.
- Random cyclic arrangements of the R ones and 2 kappa empties: 20 for the first cell, 10 for the second (seeded).
- For each, a depth-first search over residues u with interval windows only and genuineness, using the code of
  code/e14_cfunc_regime3.py (run_datum and cvals, imported unchanged) through a new driver code/e17_gap_a_probe.py.
- Caps: at most 200 leaves per datum.  Self-budget: the driver stops starting new data after 300 s per cell.
  There is no ulimit and no tool timeout.
Recorded per cell:
- the number of data, and of leaves;
- the distribution of J;
- the min and max of c;
- whether each arrangement has (2HA), checked combinatorially by brute force over interval pairs.
