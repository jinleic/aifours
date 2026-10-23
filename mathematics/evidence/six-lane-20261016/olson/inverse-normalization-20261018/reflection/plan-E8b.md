# Plan E8b (frozen before running; host clock 2026-10-18T04:1x PDT; after E8 = out/e8_b0s_replay.json)

E8 random inputs were all killed by a prefix interval, so only the plan-E7 family exercised Secs. 4-5 of proof-B0S-r1.md.
E8b samples values THROUGH the lifts: for B = 0 all-odd G-words (k <= p, kappa >= 1, genuine empty runs, 30% giant-run bias),
p in {5, 7, 11, 13, 17, 19, 23, 29}, draw V_j uniformly from the Step 0 gap of every prefix (skip if a prefix window is full),
set u_t = V_t - V_(t-1) mod p (V_k = p), resample when an empty run gets u_t = 0, and run the E8 replay function (copied
verbatim).  Expected: every word reaches Step 1 and is killed by a singleton or by the proof's pattern; 0 failures of
(U1)-(L3)/hit on the proof pattern; Case II frequency recorded; raw DP confirms solvability for p <= 11.  Caps: one process,
ulimit -t 1200, <= 4000 words, output <= 2 MB.  Output out/e8b_lift_sampled.json (exclusive create).
