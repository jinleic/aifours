# Generic-construction analysis v1 (CFR(6,21) = (Z_21,7;1)-DM) — ContinueCFR21, frozen 2026-10-19T00:05:23-0700

Purpose: decide where a CFR(6,21) could still come from, using the CRT representation (alpha = mod 3, beta = mod 7,
fibre orthogonality). Proved statements are marked [PROVED]; measured ones [MEASURED probe]; heuristics [HEURISTIC].

## 1. Exact lift accounting [PROVED]
Given the mod-7 image beta of k rows (row 0 = 0), alpha is a solution of the F3 system E(beta): for every row pair and
each of its 7 fibres (3 columns) the three values of alpha_i - alpha_j sum to 0; a genuine lift additionally needs every
fibre RAINBOW (three distinct values) — "nowhere-zero". Gauge-fixed unknowns 20(k-1); equations 7*C(k,2); the
C(k-1,2) constant circulations of K_k are always dependencies; the k-1 constant solutions bound rank(E) <= 21(k-1)-(k-1).
Excess E(k) = 7C(k,2) - C(k-1,2) - 20(k-1): E(4) = -21, E(5) = -16, E(6) = -5, E(7) = +12.
Hence every 6-row beta has a pseudo-lift space L(beta) of dim >= 5, while for 7 rows L(beta) = 0 unless rank E <= 119.
CFR(6,21) exists  <=>  some (Z7,7;3)-DM beta has a nowhere-zero element of L(beta).

## 2. Measurements
* [MEASURED p3] all 96 P21 DM6: dim L = 7 (2 above the forced 5), exactly one nowhere-zero element up to sign (the DM).
* [MEASURED p6, seed 20261019, 40+40 samples, stdout f68dbe63…] seven-row three-affine-block betas
  beta_i(t,c) = a_t(i)c + b_t(i): dim L = 6 in all 40 random-slope samples and in all common-slope samples with <= 4
  affine triples; one common-slope sample with 5 affine triples and a 4-point collinear row set had dim L = 18
  (excluded anyway by Lemma B3). No nowhere-zero lift in any sample with dim L <= 14.
* [PROVED, block lemma] If the 21 columns split into three blocks each carrying a (Z7,7;1)-DM mod 7, then every
  block-constant alpha (alpha_i(t,c) = h_i(t) with sum_t h_i(t) = 0) lies in L(beta): a 6-dim space after gauge
  (6 rows x 2 - constants). None of it is nowhere-zero: rainbow on all fibres would make (h_i(t)) a (Z3,7;1)-DM with 3
  columns. So block structure supplies only useless pseudo-lifts; this explains the old CRT families' kernels.

## 3. Where the improbability sits [HEURISTIC, calibrated]
Random 7-row beta: P(rank E <= 119) ~ 3^-13 (13 extra dependencies over the forced 27-dim left kernel), then
P(one kernel vector rainbow on all 147 fibres) ~ (2/3)^147 ~ 1e-26. Expected CFR(6,21) classes ~ 1e-18.6.
Same model: DM6 ~ 0.02-0.06 asymmetric classes (real DM6 exist only with Z5 symmetry, P21); Z15: DM5 ~ 2.7e5
labelled, DM6 ~ 0.013 (true omega(Z15) = 3, consistent); Z9: predicts ~218 labelled DM4 but none exist (9 | n:
outside Theorem A/L3 hypotheses; another obstruction). The nowhere-zero (rainbow) condition, not the linear algebra,
is the dominant barrier; structure that only adds pseudo-lifts (blocks, low rank) does not help.

## 4. Mechanism inventory for beating ~1e-18
* Symmetry divides the number of independent fibre conditions by |G|: all untwisted groups of order >= 3 and 36 twist
  classes are exhausted (old lane, one program), g16 (order 2, mu 13) exhausted, g15 DRAT; OPEN: order-2 models
  g00 = (1,(12)(34)(56)) and g10 = (8,(12)(34)(56)). [HEURISTIC] g00 expectation ~ 6e-5 solutions over all 188,181 h.
* Algebraic degeneracy: Theorem A (mod-3 affine rank 5 or 6), Lemma B (mod-7 image a set, no 4 collinear rows), block
  lemma (blocks give only useless pseudo-lifts). Old common-slope/offset CRT families sit here and failed.
* Generic rigid stratum: no mechanism; heuristic count ~1e-18.6.

## 5. Decision consequence
A witness, if any, is (i) one of the two open order-2 symmetric models, or (ii) a rigid DM with full-rank-type
projections (mod-3 rank 5/6 under Theorem A's shapes, mod-7 image a set with no 4 collinear rows, no block structure
helping). Closing (i) with a fast exact engine is the only remaining bounded search with a structural meaning
("every CFR(6,21) is rigid", relative to the old one-program symmetric exclusions). (ii) is equivalent in difficulty
to computing omega(Z21) exactly [INFERENCE: ~1e8 orthomorphism classes x 0.1-1 s each].
