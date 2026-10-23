# Plan E15b: interval + 2-pattern census of the uncovered p = 7, B = 0 cells of RES_<(7) (pre-registered before running)

Owner OlsonReflectionRigidity.  Pre-registered after host clock 2026-10-18T07:52 PDT (the file mtime is authoritative).  This
extends plan-E15.md (exhaustive search, 0 2-avoiders in the cell (3, 13)).  It is a finite aid and not a premise, and no
universal claim follows from it.

Cells (kappa, k), with R = 14 - k + 2 kappa:
- (4, 9..15), (5, 11..17), (6, 13..19).
- These are the B = 0 cells with k >= p + 1 = 8 not covered by B0S-CJ / B0S-CJ''' (proof-B0SCJ-r2.md, proof-B0SCJx-r4.md).
  This includes the edge cells (4, 9) and (4, 10), i.e. R = 13, 12.
- Cell (3, 13) was done in E15.

Run data.
- All cyclic sequences r in Z_{>=0}^k with sum R and e_R := #{t : r_t even} <= 2 kappa, the P0 bound with e_F = 0, empty runs
  counted as even.
- Taken up to rotation as canonical lexicographically minimal rotations.  About 1.87e6 data in total; per-cell counts were
  computed beforehand in the eval transcript.

Search per datum.  Exactly the DFS of code/e15_two_avoiders.py (ce... see its sha in the result note), generalised to arbitrary
masses:
- every proper interval and every 2-interval pattern against its H0 window;
- genuineness at empty runs;
- sum u = 0.
Each surviving 2-avoider is tested against ALL 2^k proper patterns (exact avoidance, given H0).

Recorded per cell:
- the number of data and of DFS nodes;
- the number of 2-avoiders;
- a histogram of the minimal killing m for 2-avoiders;
- the full avoiders (r, u), if any.

Execution.
- Cells run in increasing order of data count, in one process at a time (code/e15b_census.py), under ulimit -t.
- Each cell writes its own output file out/e15b_<kappa>_<k>.json (exclusive create) when it finishes.
- Chunks are at most 10800 s, and the largest cells may be split.

Decision use.
- If a full avoider is found, it is reported to Main at once, as a candidate counterexample to REFL-RES(7), B = 0.
- If none is found in a cell, the record is "no B = 0 RES_< avoider in that cell (finite aid, given H0)".
