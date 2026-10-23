# Receipts: wh10_exact_v1 (EXACT) and wh10_design_check_v1 (deterministic float design check)

Recorded 2026-10-19T04:11:41-0700 (from /bin/date). Owner ContinueRQLS10b. Note: evidence/wh10-reduction-v1.md
(7e77051c33431921c6d50ddcd8bd2f1c1ba961a0956cb2678f529d0290c0cac8). Both runs: cwd lane, wrapper /bin/bash -c 'echo START ...
PID $$ PGID ...; exec /usr/bin/env -i TMPDIR=<lane>/tmp /opt/homebrew/bin/python3.14 -I -B <source> <output>' (PID printed
before compute), single process, lane tmp/ empty afterwards, outputs frozen 0444. One implementation each.

## 1. wh10_exact_v1 (decisions in integer cyclotomic arithmetic: zero test = remainder modulo Phi_N)
Source code/wh10_exact_v1.py 9a06f84f211d0150af041cfabe9aea8e32d64c9da08995ceb0d38053eb379b62; launch record
evidence/wh10_exact_v1.launch.json 8b3d4187570a49dc15642ac9cc45a9730c52798d52ab0c4df72f8c6851173159. START 2026-10-19T04:02:03-0700,
PID 73507 = PGID 73507, EXIT 0, END 04:02:05 (1.9 s in-run), tool timeout 0. Output evidence/wh10_exact_v1.result.json
a341595414d7c1cbb14fded92c2cd2147201b2ceef10b9137dc3acd3e0506bdf.
Results (exact):
- C (CRT, d = 10 and 6): Z/X identities true; f_k satisfy the U = XZ^-1 eigen-equation; sigma_y and Gauss factor
  eigenvectors correct (d = 10: X_5 Z_5^2 with a = 1; d = 6: X_3 Z_3 with a = 2); every f_k equals a product g_j (x) h_b,
  k -> (j, b) a bijection (d = 10: 0->(0,0), 1->(1,2), 2->(0,4), 3->(1,1), 4->(0,3), 5->(1,0), 6->(0,2), 7->(1,4), 8->(0,1), 9->(1,3)).
- A (anchors): all 22 odd-d Gauss anchors (d = 5: a in {1,3,4}; 7: {1,2,4,5,6}; 9: {2,5,8}; b in {0,1}) have all 3d lines
  orthogonal and exactly d distinct rays; every mutation keeps rows (phase change) and breaks columns and classes.
  d = 10 relaxed anchors: Chu zeta_20^(t^2) rows+columns (classes fail), constant rows+classes (columns fail), e_0
  columns+classes (rows fail); CRT Bloch components of M^*M vanish exactly on the paired axes (z rows, x columns,
  y classes) and not on the free axis - the W9 prediction.
- E (exhaustive CAZAC enumeration, h_0 = 1): length 10 over mu_20: 160,000 b_0 (107,005 rejected by modulus, 0 with a
  DFT zero among the rest; zero-class pairs 105 x 2,100 give 0 candidates), 40 candidates, all exact; closure under all
  100 maps D_w exact; exactly 40 CAZACs = the 40 Chu sequences zeta_20^(a t^2) omega^(bt) (gcd(a, 20) = 1); 0 non-Chu;
  0 satisfy the WH condition (iii) (class flatness); twisted control zeta_20^(2t^2): 30 pass (test non-vacuous);
  Re <b_0, b_1> = 0 for all (W9). Length 6 over mu_12: 12 CAZACs, all Chu, identical to an independent brute force over
  all 248,832 sequences; 0 satisfy (iii); twisted control 6 pass.
- Exact restricted consequence: no WH_10 single-orbit 1-RQLS(10) has sqrt10 x with all entries in mu_20 (scoped: a
  finite phase lattice; the general case is the numerical assay's target). Consistent with Corollary W5 (all Chu
  sequences are CRT products).

## 2. wh10_design_check_v1 (deterministic float; no search; design evidence for the numpy gates)
Source code/wh10_design_check_v1.py e829d45e6d5658c2794844e710eed7bdaf67ceeb3a233f2a5c4c3de79464425c; launch record
evidence/wh10_design_check_v1.launch.json 441477843dfa5dbbfe255a12918132d519ced3a140e496c9965da643b422990d. START
2026-10-19T04:09:40-0700, PID 74896 = PGID 74896, EXIT 0 (0.05 s), tool timeout 280. Output
evidence/wh10_design_check_v1.result.json 4ee856d16b7ddd3e069b85cfc4251c1e6bc8908ddbadbc73ddd332d0404f0182.
Results: basis self-tests <= 6.0e-15 (d = 2, 5, 6, 7, 9, 10); every stage-A gate of the assay passes when recomputed
in pure Python (anchor residual <= 3.0e-14, rays = d, mutation residual >= 0.129, mutation Gram deviation >= 0.150;
relaxed d = 10 anchors: used-family residual <= 1.3e-15, full residual 0.316 / 0.949 / 0.949, paired-axis Bloch
<= 8.2e-16, free axis 1.0). Jacobian at the KP anchors (a = smallest valid, b = 0): d = 5 and 7 kernel = phase only
(next singular values 0.976 and 0.673); d = 9: 3-dimensional kernel (phase + 2; next 0.322) - so the KP gate of the
assay requires all amp <= 1e-2 runs to verify only at d = 5, 7 and records d = 9.
