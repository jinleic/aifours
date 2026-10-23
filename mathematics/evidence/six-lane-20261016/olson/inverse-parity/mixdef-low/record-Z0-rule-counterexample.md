# [F] Record: the plain defect-set rule fails for MIX_low (p = 13)

Owner OlsonParity.  Frozen at host clock 2026-10-17T11:47:09-07:00.  Finite, exact and
reproducible.  It refutes a proof STEP that was planned, not MIX_low itself: the word
below is solvable.

## Refuted step

Planned Step 2 of the S1' template for MIX_low (README.md here; ../proof-PAR-Kplus-partial-r2.md
Sec. 3' for B = 0) was:

> For every interval-feasible theta of a MIX_low word, the defect set
> Z0 = {t : bh_t <= 0} of the interval-chain lifts satisfies Phi(Z0) >= 2g + 2,
> where Phi(P) = sum_{t in P} (d_t - bh_t) + 2 m(P).

For B = 0 this holds trivially (all d_t >= 1). With anti runs it is false.

## The word (p = 13)

Rotation runs t = 0..12 with d_t = a_t - b_t = (-1, 1, 1, 1, 1, 3, 3, 3, 1, 1, 1, 1, 1):
run 0 is a single rho_{-1}, and every other run consists only of rho_1.  All 13 reflection
runs are odd, with l = (3,3,3,3,3,3,3,3,3,1,1,1,1).  The jumps are
theta_t = 2 x_t mod 13 with x = (-1,0,1,1,1,2,2,2,1,1,1,1,1).  The reflection values are
y = (2,2,0,11,9,5,1,10,8,6,4,2,0), from code/was_verify.word_of with y_12 = 0.

Parameters, as recomputed from the 50 letters: k = o_F = 13 <= p, A = 18, B = 1, R = 19,
F = 31, H = 9, kappa = 3, g = kappa - B = 2, D = 17 = 2p - k + 2g.  So the word is in
MIX_low(13): all reflection runs are odd, k <= p and 1 <= B < kappa <= k - 1.

## What was checked, from the definitions (record_z0_cex.py)

1. Lemma GR (proof-GR.md Sec. 2; code/gr_window.ach and tau, with the word's own y) was
   evaluated on all 2^13 sign vectors.
   * Every one of the 156 proper cyclic interval patterns misses: Ach(z) does not meet
     tau(z) + pZ.  So theta is interval-feasible.
   * 664 sign vectors hit (z and -z are both counted).  The smallest hitting patterns
     have 2 blocks, e.g. {0,5}, {1,3}, {1,4}.  The pattern {1,3}, an aligned defect plus
     an isolated bh = 1 run, hits: m = 2, D = 2, x = 1, and its window is [-8, 1].
2. Raw ordered-product DP (code/was_verify.dp_has) returns True.  A separate DP with
   back-pointers extracts an explicit 26-letter subword.  Multiplying its letters one by
   one in D_26 (left convention) gives the identity.  Its positions and letters are in
   record_z0_cex.json.
3. Each singleton lift x_t is the representative of u_t = theta_t / 2 outside its
   singleton window [lo/2, hi/2] from Ach.  The script asserts that every u_t lies
   outside its window.  The lifts equal the claimed x and sum to 13.  For interval-feasible
   theta in MIX_low these are the chain lifts, by Step 1 and the complement bound.
   Then bh = (-1,-1,1,...,1), Z0 = {0,1} (one block) and Phi(Z0) = 0 + 2 + 2 = 4 < 6 = 2g + 2.
   The pattern Z0 itself misses (GR).

## Hashes

* record_z0_cex.py: 33f5ca94570ac675ffab809c2a0ea5473daca4e97f48ed6402c9b591a1baaafe
* record_z0_cex.json (output): 85a2f98f2ae9a7c0807312a574c697fc8c3d26a38644cb4f9b5509915c1a438c
* imported, unchanged: code/was_verify.py 38ccd5ee...edac, code/gr_window.py
  7d017cc1...9439, code/coverage_all.py f52a419b...6e39

Reproduce with `python3 record_z0_cex.py` in this directory (single process, seconds).

## Consequence for the MIX_low proof

A defect-only selection P inside Z0 cannot meet (Utr) here.  Any proof must allow fillers:
runs with bh_t = 1 that are not adjacent to P.  Each such filler adds d_t + 1 to Phi and
1 to BH(P).  In this example a single filler suffices, within the budget BH(P) <= B.
