# Plan E9 (frozen before running; host clock 2026-10-18T04:39:44-0700)

Question (exploration aid for B = 0, k >= p + 1; no claim): for B = 0 all-odd G-words with k >= p + 1, kappa >= 2, >= 1 genuine
empty run, (a) how often does the B0S Step 1 bound x_t >= -L^t fail on interval-feasible lift data, and for which (alpha, r_t)
branch pattern; (b) which patterns kill interval-feasible data (m, inside/outside the defect set Z, size), to guide a written
argument.  Data: seeded random run data (P0: n_E + #even nonempty runs <= 2 kappa; k - n_E <= R) at p in {7, 11, 13}, values
drawn through the Step 0 gaps (as E8b) and kept only if every cyclic interval avoids its window (interval-feasible); then all
2^k - 2 patterns are tested with the Lemma H0 windows (k <= 16 only).  Caps: in-process eval, <= 3000 interval-feasible words,
<= 2^16 patterns each, no DP (H0 = DP equivalence is accepted GRX), output only summary statistics in this session (no file
unless a statistic is quoted later, in which case a script + JSON are written first).
