# GO request: rqls_wh10_lm_v1 (WH_10 single-orbit ansatz), ONE bounded numerical run - NOT run

Recorded 2026-10-19T04:12:07-0700 (from /bin/date). Requester ContinueRQLS10b. No numpy computation has been executed for
this item (no smoke). Launch owner: to be named by the parent (this worker launches only if named).

## Written basis (lane-internal, unreviewed, not parent-accepted)
- evidence/wh10-reduction-v1.md 7e77051c33431921c6d50ddcd8bd2f1c1ba961a0956cb2678f529d0290c0cac8: Lemma W1 (row/column/class
  conditions = flatness of x in Z, Fourier and the eigenbasis of X Z^-1), W3 (CRT), Theorem W4 (equivalent C^5 problem:
  a flat plane for the lines (0,1), (1,0), (1,2) of Z_5^2 with three pairwise unbiased flat vectors), Lemma W2 (EVERY
  solution has 100 distinct rays: any WH_10 single-orbit 1-RQLS(10) is maximal), W5 (all Chu/quadratic-phase and CRT
  product sequences excluded), W6 (MUB-pair planes excluded), W7 (exact: no solution for d = 2 and d = 6, no import),
  W8 (odd-d Gauss anchors with exactly d rays), W9 (relaxed-anchor Bloch predictions); the Z_5^2 line triple is not
  Clifford-equivalent to the W8 triple, so the W8 plane numerics do not transfer.
- Exact/design receipts evidence/wh10_exact_v1.receipt.md 9373b4201d18fdd5ae32ff6e10917bc137e53fd6d18873b11325404c3af9f11d:
  CRT identities; 22 Gauss anchors exact with d rays; complete enumeration over mu_20: the 40 CAZACs of length 10 are all
  Chu and none is class-flat (so no solution with phases in mu_20 - exact, scoped); d = 6 cross-checked by brute force;
  deterministic recomputation of every stage-A gate quantity passes; Jacobian kernel at the KP anchors: phase only for
  d = 5, 7, 3-dimensional for d = 9.

## Pins (sha256)
- source code/rqls_wh10_lm_v1.py 39f6067fc481d0746bec370189e9753f20cadce5fc7e5225610075947dec14ab (0444, 502 lines; new file,
  no diff base; LM damping schedule copied from code/rqls_w8_lm_v2.py d336e2e3...a9fd, supervisor protocol identical)
- config evidence/rqls_wh10_lm_v1.supervisor-config-v2.json 40371e8add66a2f05f5f0790d32343399fdd1450f2eddad68d5200f4dd7f489e
- supervisor code/owned_supervisor_v2.py 1fece595258d7ba448875c407e8b221bdbd01966824dc267147c316ef54115aa
- gate code/stability_gate_v2.py 1f62874aff9b22657a90f180b81c678117fd703afe2345f7576454e0faae008a (observer v3 fe311f28...4196)
- tightening 8ac556699352a42f3d97f83861039e21f57db0646da2f38391ee1f11e330aa20; stop registry review/stop-registry-v2.json
  a47bb3ff...acb7 (no relevant stop)

## Run (argv in the config): BUDGET 1600 s, NN 64, NKR 64, NP 128, NW 6000
Model: x in C^d, residual |V^* x|^2 - 1/d over the used bases (exact Jacobian), LM <= 300 iterations; EVERY endpoint
verified on the full d x d configuration (all d rows, d columns, d B-classes; per-family Gram deviation recorded); rays
counted (merge 1 - |<q,q'>|^2 < 1e-7) and, at d = 10, CRT Bloch components. Model defect = reduced residual < 1e-10 with
deviation >= 1e-8, REGARDLESS of LM status (x written); any defect before the target fails a gate.
Gates, all before the target (stop with GATE_FAIL receipt on failure):
 B   basis self-test d in {2, 5, 6, 7, 9, 10} (< 1e-12);
 A   22 odd-d Gauss anchors (residual and deviation < 1e-12, rays = d; mutation >= 0.01) and 3 relaxed d = 10 anchors
     (used families exact, full problem fails, Bloch zero on paired axes, > 0.5 on the free axis);
 N   NEGATIVE d = 2 and d = 6 full problem: >= 1 run each, 0 verified, 0 defects (exact theorem W7);
 KP  near-anchor recovery d = 5, 7, 9, amps 1e-3, 1e-2, 0.1, 0.5 x 4 seeds: all amp <= 1e-2 runs at d = 5, 7 verify; d = 9
     recorded; 0 defects;
 KR  random recovery of KNOWN solution classes, d = 5, 7, 9 x 64: >= 1 run and 0 defects per d; counts/ray histograms
     recorded, not gated (recovery of known classes, NOT target detection power);
 P   relaxed POSITIVES at d = 10 (rows+columns, rows+classes, columns+classes) x 128: >= 1 verified per variant, 0 defects,
     Bloch < 1e-6 on both paired axes for every verified solution.
Target: W = 6000 random full-problem starts at d = 10 (stage time ~890 s; actual started/completed counts recorded,
unstarted ones as SKIPPED_TIME); WS = up to 512 full-problem starts seeded at verified P solutions (+0.05 noise).
Stage clocks: A 30, N 90, KP 60, KR 180, P 180, W rest, WS 150 s inside 1600 s; supervisor max_wall 1700 s, settle 120 s.
Resources: one child; RSS expected < 200 MB (trip 2 GiB); JSONL hard cap 8 MiB in code (expected ~3 MB), output trip
9 MiB; projected reservation 20 MiB. Launch: fresh code/stability_gate_v2.py (projected 20,971,520 B) &&
code/owned_supervisor_v2.py <config>, tool timeout 0.

## Claim limits (consumer)
Target misses are a scoped UNKNOWN for this ansatz (not nonexistence); KR/KP/P recovery rates are not detection power for
d = 10. A verified d = 10 endpoint is automatically a 100-ray maximal candidate (Lemma W2): freeze x, B, seed and config
immediately, notify the parent, no exact claim before independent exact recognition, three independent checkers and a
new GO.
