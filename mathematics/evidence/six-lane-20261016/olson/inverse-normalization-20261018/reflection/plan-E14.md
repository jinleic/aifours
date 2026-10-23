# Plan E14 (pre-registered before running): c-function structure in regime (III)

Owner OlsonReflectionRigidity.  Pre-registered 2026-10-18 ~07:20 PDT.  This is a finite aid and not a premise.  It runs in-memory in
this worker's eval kernel: no native launch, no disk output beyond this plan and a short result note.

Question.  For interval-feasible data in regime III, are the following true?
- (a) c(Q) >= 0 for every proper interval Q.
- (b) c(Q) = 0 for every proper interval Q, i.e. the singleton representatives are exactly additive.
- (c) J = 0.
Here "interval-feasible" means that every proper cyclic interval avoids its window, every empty singleton has u != 0, and the
whole cycle sums to 0.  These are the c and J of proof-B0SPP-r5.md Sec. 2, with the same windows.

Data.
- p = 7, kappa = 3, k = 13, R = 7.  The seven nonempty runs are single rho_1, and there are six empty runs.
- Every cyclic arrangement of the six empties among the 13 runs is used, up to rotation.  These are the 132 run data of E13.
- For each datum, a depth-first search over singleton values u_t in Z_7 checks every interval as soon as it is complete.  It stops
  after at most 3000 leaves per datum.
- Second set: p = 11, kappa = 4, k = 19, R = 11 (regime III, Delta = 3).  Eight empties are placed in 20 random arrangements, with
  at most 2000 leaves each.

Recorded.
- The number of leaves.
- min and max of c over all intervals of all leaves.
- The number of leaves with some c(Q) != 0.
- For the first 5 such leaves: the datum, the values, and the offending intervals.
- J.

Decision use.  If (b) holds throughout, try to prove c identically 0 by a local argument.  If c < 0 occurs, record which split fails.
Neither outcome is a premise.
