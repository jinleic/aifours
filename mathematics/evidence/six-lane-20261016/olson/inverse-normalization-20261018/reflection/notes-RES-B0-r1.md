# RES_<(p) with B = 0, k <= p, R <= 2p - 2: a G-version of Proposition S1' -- Steps 0-1 proved, Step 2 fails (exact obstruction)

Owner OlsonReflectionRigidity.  Written after host clock 2026-10-18T03:42:41-0700.  Status: Sec. 1 written proof [W], unreviewed;
Sec. 2 exact description of where the RGR argument breaks; Sec. 3 finite aid.  Notation of proof-K0star-r2.md / proof-RED-r2.md.
Setting S: an all-odd G-avoider of length 4p - 2 with all rotations rho_1 (B = 0), g >= 1 empty runs, kappa >= 1, k <= p and
R = 2p - k + 2 kappa <= 2p - 2 (so k >= 2 kappa + 2, p >= 2 kappa + 3, R >= p + 2 kappa).  RGR model: Proposition S1' of
inverse-parity/proof-PAR-Kplus-partial-r2.md L164-206 (accepted chain).

## 1. Steps 0-1 survive empty runs and giant runs

g_m(E) := min(p - m, E + m - kappa - 1, floor(E/2)); a pattern with m intervals and R_Q = E has window [-g_m(R - E), g_m(E)]
(Lemma H0, beta = 0, B = 0).  For a proper interval E <= R <= 2p - 2 (E = R is now possible: the complement may consist of empty
runs only), so g_1(E) = min(E - kappa, floor(E/2)).
Step 0.  Every interval window is nonempty and not full: for E = 0, g_1(0) + g_1(R) = floor(R/2) - kappa >= (p - 1)/2 > 0; in
general the RGR computation (sum >= min(2p - k, (2p - k - 1)/2) > 0 when a truncation term occurs, >= R/2 - 1 otherwise) is
unchanged; fullness needs R = 2p - 2 and is then a certificate.  So the prefix lifts V_j (representative of u_((0,j]) in
[g_1(rho_j) + 1, p - g_1(R - rho_j) - 1]), V_0 = 0, V_k = p, x_t = V_t - V_(t-1), bh_t = 2 x_t - r_t are defined;
sum bh_t = 2p - R = k - 2 kappa; for an empty run bh_t = 2 x_t with x_t != 0.
Step 1 (claim x_t >= -L^t, L^t := g_1(R - r_t), for every run t).  For t = 1, k as in the RGR proof.  For 2 <= t <= k - 1,
x_t >= g_1(rho_t) + g_1(R - rho_(t-1)) + 2 - p, so it suffices that S := g_1(rho_t) + g_1(R - rho_(t-1)) + L^t >= p - 2.  Write
alpha = rho_(t-1) and use g_1(E) >= min(E - kappa, (E - 1)/2).  All eight choices of minima (RGR assumed L^t untruncated, which
FAILS for a run with R - r_t <= 2 kappa - 2 -- possible here when g is large):
 (F,F,F) S >= R - 3/2;  (T,F,F) S >= (alpha + r_t)/2 + R - kappa - 1;  (F,T,F) S >= R - kappa - 1 + (R - alpha)/2;
 (T,T,F) S >= 2p - k + (R + r_t - 1)/2;  (F,F,T) S >= R - 1 - kappa;  (T,F,T) and (F,T,T) S >= 3R/2 - 2 kappa - 1/2;
 (T,T,T) S = 2R - 3 kappa;
and each is >= p - 2 because R - kappa >= p + kappa, R - 2 kappa = 2p - k >= p, R >= p + 2 kappa.  Hence x_t >= -L^t.  A defect
(bh_t <= 0, i.e. x_t <= r_t/2 < p - L^t as R < 2p) therefore has x_t >= U^t + 1, U^t = g_1(r_t) = r_t - kappa, so
delta_t := -bh_t <= 2 kappa - 2 - r_t, exactly as (9.2); an EMPTY defect has x_t in [1 - kappa, -1] (genuineness excludes 0) and
delta_t in [2, 2 kappa - 2].  Every defect has r_t + delta_t >= 2.  []

## 2. Where Step 2 breaks (exact)

RGR Step 2 needs Phi(Z) := rho_Z + 2 m_Z + delta_Z >= 2 kappa + 2 for the defect set Z, from delta_Z >= 2 kappa - |Z| and
rho_Z >= |Z|.  Here delta_Z >= 2 kappa - |Z| + g_Y (empty non-defects have bh >= 2) but rho_Z >= |Z| - g_Z, so only
Phi(Z) >= 2 kappa + 2 m_Z + g_Y - g_Z (and Phi(Z) >= 2|Z| + 2 m_Z).  Equality analysis: Phi(Z) < 2 kappa + 2 forces, e.g. for
kappa = 3, Z = two consecutive empty defects with x = -1, all nonempty runs odd with bh = 1, g_Y = 0; in general it forces lift
data with every non-defect bh_t = 1 and empty defects of small depth (the extreme family: all nonempty runs bh = 1, all empty runs
x_t = -1, 3g = 2 kappa).  For such data no subset P of Z satisfies (K1).  Exact open sub-lemma (S1'-G): in setting S, the lift data
of Sec. 1 with Phi(Z) < 2 kappa + 2 never belong to an avoider.  A repair route suggested by the data below: kill with
P = Z u Y' where Y' consists of non-defects with bh = 1 and r >= 3 (each adds r - 1 >= 2 to Phi and costs 1 of delta); the kill
conditions (K1) Phi(P) >= 2 kappa + 2 and (K2) delta_P >= [rho_P odd] must then be balanced.  Not proved here.

## 3. Finite aid (plan-E7.md frozen 03:38:01; code/e7_failing_lifts.py; out/e7_failing_lifts.json)

1,200 words of the extreme family (p = 11, 13, 17, 19; (kappa, g) = (3, 2), (6, 4); all admissible k; empty runs adjacent or
separated): every one is solvable by raw DP (0 candidates); 216 of them realise the intended prefix lifts exactly.  For realising
words at p = 11 an eval exploration (03:4x, not a pinned script) found hundreds of killing patterns each, always including
cyclic intervals that contain the empty defects together with adjacent bh = 1 runs (e.g. r = (1,1,5,5,1,1,0,0,1,1,1), empty runs
6, 7: the interval {3,...,7} has rho = 7, delta = 1, Phi = 10 >= 8 and is hit at x = 3) -- the repair route of Sec. 2.
