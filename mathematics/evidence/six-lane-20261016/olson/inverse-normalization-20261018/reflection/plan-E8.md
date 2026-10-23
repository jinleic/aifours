# Plan E8 (frozen before running; written at host clock 2026-10-18T04:0x PDT, after proof-B0S-r1.md)

Replay of the proof of Theorem B0S (proof-B0S-r1.md, sha c848d060...4408) as an algorithm on explicit words; aid only.
Inputs: (i) seeded random B = 0 all-odd G-words, k <= p, kappa >= 1, p in {5, 7, 11, 13, 17, 19, 23}, with run lengths drawn to
include giant runs and many empty runs; (ii) the extreme Case II family of plan-E7 (theta_t = r_t + 1 on nonempty runs,
theta_t = -2 on empty runs, 3g = 2 kappa), p in {11, 13, 17, 19}.
For each word: compute the prefix lifts from the Lemma H0 windows; if a prefix window is full or a prefix interval is hit, record
that kill; else check Step 1 (x_t >= -L^t for all t; every defect satisfies (2.1) or its singleton {t} is hit), classify Case I/II,
build the pattern P of Sec. 4 / Sec. 5, and check (a) the six inequalities (U1)-(L3), (b) u_P in I(P) mod p (an actual hit).
Raw DP (dp1, dp2 on NO) confirms solvability for p <= 11.  Mutation control: in Case II replace one item of W by a run adjacent to Z
(when one exists) and record whether the kill survives (expected to fail sometimes).  Expected: every word killed; 0 failures of
(a)/(b) on the proof's own pattern.  Caps: one process, ulimit -t 1200, output <= 2 MB.
Output: out/e8_b0s_replay.json (exclusive create).
