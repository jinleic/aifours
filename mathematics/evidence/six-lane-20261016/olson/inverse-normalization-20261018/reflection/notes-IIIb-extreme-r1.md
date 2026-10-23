# Notes: an exact reformulation of the extreme IIIb family (kappa = (p + 1)/2, R = p, all-ones)

Owner OlsonReflectionRigidity.  Written after host clock 2026-10-18T12:35:31-0700.  Status: route notes [W].  The derivation in Sec. 1
is exact (H0 windows); nothing here is a theorem about avoiders.

## 0. The family

- B = 0, all blocks odd, kappa = (p + 1)/2 (so H = (p - 3)/2), R = p, k = 2p - R + 2 kappa = 2p + 1.
- P0 gives n_E <= 2 kappa = p + 1 and N_+ <= R = p, so n_E = p + 1, N_+ = p, and every nonempty run is a single rho_1.
- Delta = kappa - 1 and mu = Delta - kappa + 1 = 0.
- This is the IIIb cell with the most runs.  For p = 7 it is (kappa, k) = (4, 15).  There E15b found 54,927 2-avoiders, and E15c
  found that all are killed by 3-interval patterns (finite aid).

## 1. The z-formulation (exact)

Put v_t = u_t - r_t and z_t := 2 v_t in Z_p.  For a pattern P let z_P = sum_P z_t, and let E_P be the number of ones in P.
- Then sum_t z_t = 0, and z_t != 0 at every empty run (genuineness).
- By H0 (B0S-r4 Imports), an m-interval pattern P kills iff z_P lies in F(m, E_P), a set of ODD integers taken mod p:
  * middle range 2m - 3 <= E <= p + 3 - 2m:  F = odd integers in [-(2m - 3), 2m - 3];
  * E < 2m - 3:  F = odd integers in [1 - E, 2m - 3] for E even, and in [-E, 2m - 3] for E odd;
  * E > p + 3 - 2m:  the mirror image, F(m, E) = -F(m, p - E), since the complement pattern has the same m and mass p - E;
  * this ignores the cap p - m, which binds only when m > p - floor(E/2).
Derivation.
- In the middle range, g_m(E) = E + m - kappa - 1 and g_m(p - E) = p - E + m - kappa - 1.
- So the v-window is [(3 - p)/2 - m, m - (p + 3)/2].  Doubling and adding p gives the odd integers from 3 - 2m to 2m - 3.
- For E < 2m - 3 the complement side is in its floor branch, g_m(p - E) = floor((p - E)/2), and the same computation gives the
  stated ranges.
Consequences.
- m = 1: F is empty for all E.  Intervals impose nothing beyond z_t != 0 at empty runs.
- m = 2: F = {+-1} for 1 <= E <= p - 1, F = {1} for E = 0, F = {-1} for E = p.
- m = 3: F = {+-1, +-3} for 3 <= E <= p - 3; for E = 0 it is {1, 3}; for E = 1, 2 it is {-1, 1, 3}.
So two separated runs, at least one of them a one, must have z-sum different from +-1, and two separated empty runs must have
z-sum different from 1.

## 2. Structure from the pair condition

On Z_p join x and y when x + y is +-1.  Every vertex has the two neighbours 1 - x and -1 - x.  There are loops exactly at
x = +-1/2, and the remaining edges form the single Hamiltonian path 1/2, -3/2, 5/2, -7/2, ..., -1/2.  So a set of residues that
occur on pairwise separated runs (with at least one one among each pair, or with the stronger sum-1 rule for empty-empty pairs)
is essentially an independent set of that path: at most (p + 1)/2 distinct values.  Combined with the m = 3 condition, and with
sum z = 0 over 2p + 1 runs, this should force a kill, but no proof has been written.

## 3. Why it matters

The family is the extreme case of gap (d).  The windows of every pattern are explicit sets of odd residues, so the problem is a
clean additive one: a zero-sum cyclic sequence must avoid prescribed small odd sums on unions of separated arcs.
