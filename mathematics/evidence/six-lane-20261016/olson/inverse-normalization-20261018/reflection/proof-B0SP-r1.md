# Theorem B0S+: the B0S argument beyond k <= p (B = 0, k <= p + kappa + 1, R >= 4 kappa + 1, 2 kappa <= p - 1)

Owner OlsonReflectionRigidity.  Written after host clock 2026-10-18T05:37:06-0700.  Status: written proof [W], UNREVIEWED.
Base: proof-B0S-r4.md (d76a179d...b89c; the r2/r3 mathematics is parent-accepted, R/olson-reflection-smallk-parent-verdict-v1.md
b71fcaf4...13b8).  This file changes only the numerical facts that B0S derived from k <= p; every step of B0S-r4 Secs. 2-5 is
reused with the inequality it needs re-checked below.  Scope: B = 0 only; no statement about rotation values, INV*(p), REFL(p)
or ordered Olson.

## 0. Statement

**Theorem B0S+.**  Let p >= 5 be prime and w a word of length 4p - 2 over D_(2p) whose rotation letters all equal one rho_x,
x != 0 (normalised rho_1, B = 0), with F, R >= 1, all maximal constant reflection blocks of odd length, kappa = p - 1 - H >= 1, and
any number of (genuine) empty runs.  Suppose
   (H1) k <= p + kappa + 1,   (H2) R >= 4 kappa + 1,   (H3) 2 kappa <= p - 1.
Then w has an identity 2p-subword.
For k <= p the hypotheses hold automatically (R = 2p - k + 2 kappa >= p + 2 kappa and p >= 2 kappa + 1 by B0S-r4 Sec. 1), so B0S+
contains Theorem B0S.  New range: p + 1 <= k <= min(p + kappa + 1, 2p - 2 kappa - 1) with kappa <= (p - 1)/2 (H2 reads
k <= 2p - 2 kappa - 1 because R = 2p - k + 2 kappa).
**Corollary.**  RES_<(p) has no avoider with B = 0 and (H1)-(H3).
Imports: exactly those of proof-B0S-r4.md (the H0 instance, B = 0, beta = 0, every m >= 1, derived there from GRX).

## 1. The facts replacing B0S-r4 Sec. 1

R = 2p - k + 2 kappa (all blocks odd).  If R >= 2p, rho_1^(2p) is an identity, so R <= 2p - 1 and k >= 2 kappa + 1.  From (H1):
   (F1) R - kappa - 1 = 2p - k + kappa - 1 >= p - 2,   and R >= p + kappa - 1 >= p.
From (H2): k <= 2p - 2 kappa - 1, so (F2) 2p - k = R - 2 kappa >= 2 kappa + 1 >= 3.  (H3) is used only in Sec. 3.

## 2. Lifts and the defect bound (B0S-r4 Sec. 2, re-checked)

Step 0 (interval windows nonempty).  If one term uses the truncation branch, by the symmetry E <-> R - E let it be g_1(E) = E - kappa;
then g_1(E) + g_1(R - E) >= min(R - 2 kappa, (E + R - 1)/2 - kappa) >= min(2p - k, (R - 1)/2 - kappa) >= 1 by (F2) and (H2)
((R - 1)/2 - kappa >= kappa).  Otherwise both are floors and the sum is >= R/2 - 1 > 0.  The prefix lifts V_j, x_t, bh_t are
defined as in B0S-r4 Step 0 (any chain); sum x_t = p and sum bh_t = 2p - R = k - 2 kappa >= 1.
Step 1 (x_t >= -L^t).  As in B0S-r4 it suffices that S := g_1(rho_t) + g_1(R - rho_(t-1)) + g_1(R - r_t) >= p - 2 for
2 <= t <= k - 1.  For an argument E >= 2 kappa + 1 the floor branch is strictly smaller than E - kappa (ceil(E/2) >= kappa + 1), so a
truncation branch can be the minimum only at arguments <= 2 kappa.  At most one of the three arguments rho_t, R - alpha
(alpha := rho_(t-1)), R - r_t is <= 2 kappa: rho_t + (R - alpha) = R + r_t >= R, rho_t + (R - r_t) >= R and
(R - alpha) + (R - r_t) = 2R - rho_t >= R, while any two arguments <= 2 kappa would give R <= 4 kappa, contrary to (H2).  Hence
only the cases FFF, TFF, FTF, FFT of B0S-r4 occur, with S >= R - 3/2, R - kappa - 1 + rho_t/2, (3R - alpha)/2 - kappa - 1,
(3R - r_t)/2 - kappa - 1 respectively (exact values recorded by the Claude review of B0S-r2), each >= R - kappa - 1 >= p - 2 by (F1).
Defects: verbatim (x_t <= r_t/2 < p - L^t because R < 2p), so (2.1) delta_t <= 2 kappa - 2 - r_t, r_t + delta_t even and >= 2,
empty defects in [1 - kappa, -1].

## 3. Kill conditions and Cases I, II (B0S-r4 Secs. 3-5, re-checked)

Sec. 3 of B0S-r4 is generic (Z nonempty and proper uses only sum bh = k - 2 kappa in [1, k - 1]).
Case I (Phi(Z) >= 2 kappa + 2): the greedy P has 2 kappa + 2 <= Phi(P) <= 4 kappa.  (U1), (L1): Phi(P) <= 4 kappa <= 2p by (H3).
(L2): 4 kappa <= 2R - 2 kappa - 2 iff R >= 3 kappa + 1, true by (H2).  (L3): delta_P <= Phi(P) - 2 <= 4 kappa - 2 <= R - 1 by (H2).
Case II (Phi(Z) <= 2 kappa): the identities and bounds delta_Z = 2 kappa - |Z| + s, |Z| <= kappa - m_Z, s <= g_Z - 2 m_Z,
delta_Z - rho_Z >= 4 m_Z, 2 <= d <= g_Z <= kappa - 1 are generic.  |F| >= d/2 needs k >= 2 + 2|Z| - rho_Z: true as
k >= 2 kappa + 1 and |Z| <= kappa - 1.  Properness of P = Z u W (B0S-r4 Sec. 5) is generic.  (U3): delta_P >= kappa + 1 - (kappa - 1)/2 > 0.
(L3): delta_P <= delta_Z <= 2 kappa - 2 <= R - 1.  (U1): <= r_y + 1 <= 2p (W = {y}) and <= 3 kappa - 7 < 2p otherwise.
(L1): <= 4 kappa - 4 < 2p by (H3).  (L2): <= 2 kappa + r_y - 7 (W = {y}) and <= 4 kappa - 4 otherwise; the first is
<= 2R - 2 kappa - 2 iff r_y <= 2R - 4 kappa + 5, true as r_y <= R and R >= 4 kappa - 5; the second iff R >= 3 kappa - 1, true.
So every case ends in a kill: contradiction.  []

## 4. What remains for B = 0 and k >= p + 1

Not covered: (a) k >= p + kappa + 2 (then R = 2p - k + 2 kappa <= p + kappa - 2, n_E >= k - R >= 4, and Step 1's single-truncation
bound R - kappa - 1 can drop below p - 2); (b) R <= 4 kappa (double truncations in Step 1; Case I's (L3) can fail: the finite aid
E9b shows a p = 7, kappa = 3, R = 7 datum where the greedy P = {1, 3} has delta_P = 8 > R - 1, while the pair {1, 7} kills);
(c) kappa >= p/2 ((U1), (L1) of Case I).  In (a)-(c) the B0S framework needs only integer lifts x_t = u_t lying in their singleton
gaps with sum x_t = p (Secs. 3-5 use nothing else); so the open core of B = 0, k >= p + 1 splits into
  LEMMA SIGMA: for an avoider, the singleton representatives w_t (in [U^t + 1, p - L^t - 1]) satisfy sum_t w_t = p, and
  a SELECTION LEMMA: from Z (and isolated bh = 1 fillers) choose P meeting (U1)-(L3) when (H2)/(H3) fail.
Finite aids (not premises): E9 (plan-E9.md da6eb0b3...70b1, code/e9_b0l_probe.py 84c801b3...196f, out/e9_b0l_probe.json):
interval-feasible B = 0, k >= p + 1 data at p = 7 (400) and p = 11 (26): sum w_t = p (Step 1) held in all 426; every datum with
k <= 12 (365) was killed, always with minimal m = 2.  E9b (plan-E9b.md 0b829c0a...baaf; v1 code/e9b_b0l_kills.py 15a5e8f5...
crashed in json.dump after its run, partial out/e9b_b0l_kills.json kept; v2 code/e9b_b0l_kills_v2.py c80856ed...835b,
out/e9b_b0l_kills_v2.json): 590 data (p = 7: 300, p = 11: 290), all in Case I; the Case I greedy killed in all 517 data meeting
2 kappa <= p and R >= 4 kappa - 3 and in 70 of the 73 others; a pair of non-adjacent defects killed in 556/590; some 2-interval
pattern inside Z killed in 581/590.
