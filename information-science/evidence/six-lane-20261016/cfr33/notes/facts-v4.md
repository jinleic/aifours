# Written facts v4 (adds R1, R2) -- written 2026-10-17 15:35:19 PDT

## R1 (operations preserving "f extends to a CFR(r,n) normal form") [written proof]
Let D be a normalised DM (rows 0, id, f_1..f_{r-1} as functions of the column t). For distinct rows p, q the
renormalisation R_{p,q}(D): rows (D_i - D_p) o (D_q - D_p)^-1 is again a normalised DM (pairwise differences are
compositions of bijections with a fixed bijection), with D_p -> 0 and D_q -> id.
* (p,q) = (id, 0): D_q - D_p = -x, so every f-row f_j becomes t -> f_j(-t) + t; for odd f_j this is id - f_j.
* (p,q) = (0, f_1): every row is composed with f_1^-1; the old id row becomes f_1^-1, which is an f-row of the new
  normal form.
* Conjugation by mu in Z_n^*: f -> mu f(mu^-1 x) applied to all rows maps normal forms to normal forms (id fixed).
All three preserve oddness and K-equivariance for abelian K <= Z_n^*. Hence for any odd f: f is an f-row of some
odd CFR(r,n) normal form  <=>  the same holds for id - f, for f^-1, and for every conjugate of f. Searching one
representative per orbit of the generated group is therefore complete for "some f-row lies in a given invariant set".

## R2 (random-f_1 calibration facts; empirical, not proofs)
n = 25: random odd f_1 has |L2| about 1100 with about 12 orthogonal pairs inside L2; an odd CFR(5,25) was found after 72
random f_1 (21.9 s, seed 1, controls/odd-search-smoke-v6); the found solution has only the trivial symmetry {+-1}
(f_3 alone is <7>-equivariant). n = 27: |L2| about 4060, about 50 pairs inside L2, about 1.9 s per f_1.
