# Plan E11 (frozen before running; host clock 2026-10-18T05:43:34-0700)

Question (aid for LEMMA SIGMA, proof-B0SP-r1.md Sec. 4; no claim): for B = 0, all-odd G-run data with k >= p + 1, do there exist
value assignments that are interval-feasible (every proper cyclic interval avoids its Lemma H0 window mod p, genuine empty runs)
but whose singleton representatives w_t (in [U^t + 1, p - L^t - 1]) have sum w_t != p?  Generator: E9's run-data generator
(P0, k - n_E <= R); values drawn by choosing w_t in the singleton gaps (uniform, and a biased mode pushing w_t of light runs to
the gap ends) subject to sum w_t = 2p or 0; u_t := w_t mod p; then the full interval check.  For each SIGMA-violating
interval-feasible datum found: record it, test all 2-interval patterns (and all patterns if k <= 14) for a kill, and decide it
by raw DP (dp1 = dp2) when p <= 11.  p in {7, 11, 13}; caps: one process, ulimit -t 1200, <= 2,000,000 assignments per p,
output out/e11_sigma_search.json (x).  A found datum that no pattern kills is a candidate counterexample: parent notified.
