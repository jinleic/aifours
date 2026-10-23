# Plan E7 (frozen before running; written right after host clock 2026-10-18T03:3x PDT)

Context: attempting a G-version of Proposition S1' (B = 0, all blocks odd, k <= p, kappa >= 1, R <= 2p - 2) for RES_<: Step 1
(x_t >= -L^t and the defect bound delta_t <= 2 kappa - 2 - r_t) survives empty runs and giant runs (all eight min-cases checked by
hand), but Step 2 (Phi(Z) >= 2 kappa + 2) can fail.  The failing lift data are forced: every nonempty run has lifted bracket
bh_t = 1 (x_t = (r_t + 1)/2, all r_t odd), every empty run has x_t = -1 (theta_t = -2), and 3g = 2 kappa.  Hypothesis H7: such
words are solvable (a proof would then need a kill outside Step 3's P subset Z).
Test: for p in {11, 13, 17}, kappa with 3g = 2 kappa (g = 2, kappa = 3; g = 4, kappa = 6), k in [2 kappa + 2, p], seeded random
odd run lengths summing to R = 2p - k + 2 kappa, random positions of the g empty runs (adjacent and separated), values from
theta_t = r_t + 1 (nonempty) and theta_t = -2 (empty) -- the unique values with these lifts up to translation; every word decided
by raw DP dp1, any NO re-decided by dp2 and reported as a candidate counterexample (explicit word, JSON, parent notified).  Also
record the lifts check (prefix-lift recomputation from H0 windows) to confirm the words realise the failing lift data.
Caps: one process, ulimit -t 1200, output <= 2 MB.  Code code/e7_failing_lifts.py, output out/e7_failing_lifts.json.
