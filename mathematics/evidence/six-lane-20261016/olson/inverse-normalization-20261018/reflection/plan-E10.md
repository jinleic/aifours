# Plan E10 (frozen before running; host clock 2026-10-18T04:50:27-0700)

Replay of the proof of Theorem MXG (proof-MXG-r2.md, f2235ed9...ae2f) as an algorithm; aid only, never a premise.
Data: seeded random MXG run data (all blocks odd, runs pure aligned / pure anti / empty, A >= B >= 1, g = kappa - B >= 1,
2g + B <= k - 1, k <= p), p in {7, 11, 13, 17, 19, 23}; lift values x_t drawn from the singleton gaps [U_t + 1, p - L_t - 1],
biased toward small |bh_t| (to reach the residual lemmas), with x_k fixed by sum x = p; kept only if every cyclic interval Q has
x(Q) in its gap (interval-feasible; this is the conclusion of Lemma S, also cross-checked against the chain lifts) and every
empty run has x_t != 0 (genuine).  For each kept datum the elimination order of Sec. 8 (GIANT, MIX-R', W, B1, A', AC', KS', ZP, C,
R4') is run; the lemma that applies builds its set S (or pattern P* for MIX-R') exactly as written; the replay checks the lemma's
hypotheses, the KL hypotheses (proper, phi <= g - 1 on S, c(S) >= g + 1, BH(S) <= B) and that the final KL/Lemma-G' prefix P has
u_P in I(P) (Lemma H0 windows).  A datum where no lemma applies or a check fails is a FAILURE (reported, with the datum).  Words
(y values from theta = 2u) with p <= 11 are decided by raw DP (dp1 = dp2) and must be solvable.  Control: at every SPLIT use, the
plain alternating split without doubling E is also evaluated; the count of uses where it fails is recorded (expected > 0 if
empty defects matter).  Caps: one process, ulimit -t 1800, <= 20000 kept data, output <= 4 MB: out/e10_mxg_replay.json (x).
