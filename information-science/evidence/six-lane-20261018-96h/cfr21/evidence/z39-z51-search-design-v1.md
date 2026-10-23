# Prepared (NOT run) search design: 6 MOLS(n) via a cyclic (Z_n,7;1)-DM, n in {39, 51} — v1 (2026-10-19T00:32:55-0700)

Author ContinueCFR21. Status: written analysis only; no Z39/Z51 search has been run. Any execution waits for the
parent-frozen open-status contract and an item-specific GO. Target bridge: a 7-row DM D over Z_n gives the OA(8,n)
{(c, D_0(c)+g, ..., D_6(c)+g)}, hence 6 MOLS(n) L_t(c,g) = D_t(c) - D_0(c) + g (t = 1..6), and CFR(6,n).
Current table value N(39) >= 5, N(51) >= 5 (Miller-Abel-Valkov-Fraser 2024, Table 1).

## A. Frozen exact checker and controls (prepared, not executed)
* code/check_dm_mols_cfr_v1.py (sha 4e5537e6de0240b46c363a48bdd3d582457d0357c9ab733220ae9bbb85ba4b46): checker A,
  definition-level: (1) DM over Z_n, (2) the six MOLS (Latin + pairwise orthogonal, n^2 pairs), (3) CFR(k-1,n) by a
  re-implementation of the CPro1 circular-Florentine predicate. Exit 0 iff all PASS.
* code/make_dm_controls_v1.py (sha e1432c206cf2b9f5d3e3b1b9b8252b8f83d2d94b6c48b4f04f714f37c96571aa): positives
  (k=7 linear over Z7, Z13; Sage DM_21/33/39/51_6_1 re-implemented from the pinned Sage source
  sources/sage-database-develop.py 761494dd…; pinned P21 DM6 sol 1) and negatives (in-row transpositions of each
  positive, a duplicated row, Z9 {0,x,2x,4x}, Z21 {0,x,2x,5x}, a mutated Z13 k=7). Note: Sage's cyclic_shift is a
  right shift; the generator rotates left, which yields the same column multiset (all 5 rotations), so the DM is the
  same up to column order.
* Execution plan (<= 300 s stdlib, no search): generator into a new directory, then checker on every control;
  acceptance = every expected verdict reproduced. Two further independently authored checkers plus the parent's are
  required for any witness.

## B. Proved necessary conditions available for n = 39, 51 (3 || n)
Theorem A (mod-3 affine rank of a DM7 is 5 or 6; no sum-zero mod-3 relation of support <= 5), L3, Proposition C
(lambda = 13: pairing counts = 2, (4,1) counts = 1 mod 3; lambda = 17: pairing counts = 1, (4,1) counts = 2 mod 3),
Lemma B (q = 13 or 17: the mod-q image is a set; no 4 rows collinear mod q). Symmetry screens (old-lane lemmas, re-derived):
 G2: a pure row permutation (mu = 1) fixing a row has all non-fixed column orbits of length m with m | n-1, and it
     cannot fix two rows (the fixed pair's difference would be constant on an orbit);
 PF: an element fixing two rows pointwise and swapping another pair forces gcd(mu-1,n) = gcd(mu+1,n): impossible for 3 | n;
 CC: a pure 7-cycle fixes only constant columns, of which there is at most one, so it needs n = 0 or 1 (mod 7).

## C. Consequences for the symmetry group G <= Z_n^* x S_7 of a DM7
* n = 51 (Z_51^* = Z_2 x Z_16): no element of order 3 (mu would be 1: G2 needs 3 | 50), 5 (pure 5-cycle fixing 2 rows
  violates G2; a 5-cycle times (56) has an order-2 power fixing 5 rows with a 2-cycle: PF) or 7 (51 = 2 mod 7: CC).
  Hence Aut(DM7) restricted to untwisted elements is a 2-group. Involutions (mu, (12)(34)(56)): fixed columns
  gcd(mu+1,51) = 1, 3, 17, 51 for mu = 1, 35, 16, 50; mu = 50 forces D_2 = -D_1 (constant triple sum: dead by L3).
  Pure multipliers (mu, id): mu = 35 is dead by the P1 argument (every f-row = -x mod 3 off 3Z_51, two such rows are
  not orthogonal); mu = 16 (odd mod 17) and mu = 50 (odd) remain; order-4 elements: mu in {4, 13, 38, 47} with
  pi in {id, (1234)(56) type} need individual screening.
* n = 39 (Z_39^* = Z_2 x Z_12): pure 3-cycles are dead (G2: 3 ∤ 38); order-3 elements need mu in {16, 22}
  (the multiplier of DM_39_6_1); a 7-cycle is dead (39 = 4 mod 7: CC); involutions (mu, (12)(34)(56)) with
  mu in {1, 14, 25, 38} have gcd(mu+1,39) fixed columns (1, 3, 13, 39; mu = 38 dead by L3).
  The natural extension of DM_39_6_1 is G = <(16, (123)(456)), (38, id)> (order 6) with row 0 fixed and the zero
  column; its 6-row restriction must reproduce DM_39_6_1 (positive control for the engine).

## D. Engine and calibration plan (after contract + GO only)
* Engine: exact cover over G-orbits of columns (items = (pair-orbit, difference value) and column-orbit slots),
  equivalent to the old dmorbit_xc design but newly written and independently cross-checked; every hit is
  re-verified by checker A over Z_n. Positive engine controls: 6-row versions of each model must re-find
  DM_39_6_1 (G of order 6) and DM_51_6_1 (G = Z_5 x Z_2, valid for 6 rows) — old-lane reference: the 6-row Z_21
  model with Z_5 found 96 solutions in 2.8 s.
* Cost calibration: first-solution runs capped at 600 s per (n, G, fixed-column mode), 2 processes, then the
  exhaustive runs only for families whose calibrated node rate predicts completion within a 3 h chunk.
* Heuristic priors [HEURISTIC]: asymmetric DM7 classes ~20 (Z_39) and astronomically many (Z_51) under the model
  that fits omega(Z15) = 3; symmetric families trade expected count for search size; for Z_51 only 2-groups remain.
