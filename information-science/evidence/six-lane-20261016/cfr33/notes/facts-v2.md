# Written facts v2 (supersedes nothing in v1; adds E3b, E5, E6 and corrects a typo) -- written 2026-10-17 15:11:23 PDT

Typo in facts-v1.md (n = 27 bullet of E3): "K in {{1}, <-1>}" should read "K in {1, <-1>}".

## E3b (cycled rows at fixed columns)
Setting of E3 (D a (Z_n,k;1)-DM, column multiset invariant under s = (mu, pi) modulo adding constant vectors),
with |F| >= 2 and pi != id. Then |Fix(mu)|^2 <= n.
Proof. By E3 there are exactly |H| columns c with s(c) = c + g_c 1 (H = Fix(mu)). Fix j in F and i with pi(i) != i.
For such c: s(c)_j = mu c_j = c_j + g_c, so g_c = (mu-1) c_j; s(c)_pi(i) = mu c_i = c_pi(i) + g_c. Hence
c_pi(i) - c_i = (mu-1)(c_i - c_j), an element of (mu-1)Z_n, a subgroup of order n/|H|. The DM property for the
row pair (i, pi(i)) makes these |H| differences distinct, so |H| <= n/|H|. QED.
Consequence at n = 27: mu in {10, 19} (|H| = 9, 81 > 27) is impossible whenever pi != id has >= 2 fixed rows.
So README models M2 (mu = 10, sigma = (2 3 4)) and M3 (M2 + odd) are EMPTY (proved here; SAT/DRAT cross-check
in runs/). With pi = id, E3 already excludes mu in {10, 19} (kmax(Z_9) = 3 < 6).

## E5 (cyclic symmetry types for a (Z_27, 6; 1)-DM; derived from E3/E3b and orbit counting)
s = (mu, pi), pi in S_6 (DM rows 0 = zero row, 1 = id, 2..5 = f_1..f_4), modulo translations.
* mu of order 9 or 18: impossible (some power has mu' of order 3 with pi' = id or with >= 2 fixed rows... pi would
  need order 9, not in S_6).
* mu in {10, 19}: pi must be fixed-point-free of order 3 (two 3-cycles).  [T5]
* mu in {8, 17} (order 6): pi of order 3 or 6 with pi^2 two 3-cycles; pi = two 3-cycles gives the group
  {odd} x {T5}.  [T6]
* mu = -1: pi any involution (H = {0}): pi = id [T1 = M1 odd], or pi = transpositions [T2 = M4a/M4b when pi fixes
  rows 0 and 1], or pi = (0 1)(2 3)(4 5) [T7: f_2 = id - f_1, f_4 = id - f_3].
* mu = 1: at most one fixed row (E3 with H = Z_27 forces every column fixed otherwise): pi = two 3-cycles [T4]
  (no fixed column, 9 orbits of size 3) or three transpositions [T3] (one fixed column, 13 orbits of size 2);
  a 6-cycle is impossible by orbit counting.
* Normal form (rows 0 and 1 normalised) turns s into variable identifications only if pi maps {0,1} onto itself:
  pi fixing 0 and 1 gives f_j(mu x) = mu f_k(x) (k + 1 = pi^-1(j + 1)); pi swapping 0 and 1 gives
  f_j(-mu x) = mu (f_k(x) - x).  T4, T5, T6 need a DM-form encoding (no pi-invariant pair {0,1}).
* Combining T1 with T2 gives (1, transposition): impossible (mu = 1 with >= 2 fixed rows).

## E6 [HEURISTIC, not a proof] expected solution counts (independence model)
Treat each "map is a bijection" event as independent with its random probability. n = 27:
unrestricted (M0) about 10^0.3 ordered normal forms (4-tuples); odd model about 8e5 ordered 4-tuples;
CFR(4,27) odd about 6e11. Same model at n = 25: odd about 2e4, <7>-model about 3.6e6 ordered (Kirtchakov's
enumerated 32795 <7>-orthomorphisms agree with the predicted 4.6e4). The independence model is known to fail
for 3-power orders (n = 9: predicts about 24 orthogonal pairs, true count 0, code/z9_pairs_check.py).
