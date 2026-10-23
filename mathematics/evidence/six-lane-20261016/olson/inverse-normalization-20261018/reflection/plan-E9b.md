# Plan E9b (frozen before running; host clock 2026-10-18T05:03:03-0700)

Follow-up of E9 (out/e9_b0l_probe.json: B = 0, k >= p + 1 interval-feasible data: Step 1 x_t >= -L^t held in 426/426; every
datum with k <= 12 (365) was killed, always with a 2-interval pattern as the minimal m).  E9b classifies the kills to guide a
written argument (aid; no claim): for each interval-feasible datum (same generator and seed family as E9, p in {7, 11, 13},
tries capped) record (k, kappa, R, n_E), Phi(Z) vs 2 kappa + 2, and whether a kill exists among: (A) pairs {a, b} of
non-adjacent DEFECTS; (B) pairs {defect, non-defect}; (C) pairs of non-adjacent runs of any kind; (D) two-interval patterns
inside Z u (adjacent?) -- i.e. P subset of Z with m(P) = 2; (E) the B0S Case-I greedy prefix (if Phi(Z) >= 2 kappa + 2);
(F) any pattern (k <= 12 only).  Caps: one process, ulimit -t 1500, <= 600 data, output out/e9b_b0l_kills.json (x).
