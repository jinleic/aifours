# Written facts v6 (structured f-row families at n = 27) -- written 2026-10-17 16:07:52 PDT

Families of odd orthomorphisms f of Z_27 (as candidate f-rows of an odd CFR(5,27) normal form):
* pres3Z: f(3Z_27) = 3Z_27.  lin3: f(x) = -x (mod 3) for all x (equivalently f respects the cosets of 3Z_27).
* F_h: f respects the cosets of 9Z_27, i.e. f(x) = h(x mod 9) (mod 9) for an odd orthomorphism h of Z_9.
* lin9:c = F_h with h(y) = c y (c in {2,5,8}).  Inclusions: pres3Z > lin3 > union of F_h > lin9.

## S1 (at most one structured f-row per normal form) [written proofs]
(a) two lin3 rows f_i, f_j: f_i - f_j = 0 (mod 3) everywhere, so f_i - f_j is not onto Z_27.
(b) two pres3Z rows: rows 0, id, f_i, f_j restricted to the 9 columns t in 3Z take values in 3Z and their pairwise
    differences must be distinct there, giving a (Z_9, 4; 1)-DM -- impossible ([PC16, Lemma 2.2]; our D1 control).
(c) two 9Z-coset-respecting rows: rows 0, id, f_i, f_j reduced mod 9 are 9-periodic in t, so one period gives a
    (Z_9, 4; 1)-DM -- impossible.  (d) two 10-equivariant rows: E3 restriction to 3Z gives a (Z_9, 4; 1)-DM.
So searching "f_1 in the family" covers every normal form with at least one row in the family.

## S2 (family sizes) [computation, ../code/enum_lin9.py, ../code/enum_Fh.py]
* lin9:2: exactly 81 odd orthomorphisms (3 linear), all of the form 2x + 9 g0(x mod 9); 30 conjugation orbits of
  the 78 non-linear ones.
* 21 odd orthomorphisms h of Z_9; every F_h has 81 members (78 non-linear for the 3 linear h); 27 conjugation orbits
  for non-linear h. Under R1 (conjugation, f -> id - f, f -> f^-1, acting on h as h -> u h(u^-1 .), id - h, h^-1)
  the 21 h form two orbits: the 3 linear h, and the 18 non-linear h.
