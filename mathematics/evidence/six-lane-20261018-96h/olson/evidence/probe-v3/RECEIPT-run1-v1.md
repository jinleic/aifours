# s1sharp_support_probe_v3 run1: receipt (aid only; never a premise)

Written after /bin/date 2026-10-19T00:18:03-0700.  Owner ContinueOlson.  Plan sent to parent before launch (IRC about 00:15).
- Probe code/s1sharp_support_probe_v3.py 10fbff030e91d49119ee7c19838dc0b3e994936237ce6e3f3cd28cca863cb1a3 (= v2 with ITEMS
  replaced only; frozen 00:14:53); launcher code/lane_launcher_v2.py c10c2855...aef4.
- Shell START 2026-10-19T00:15:04-0700, END 00:17:39.  run1.pre.json 16a9c423e64a026570f785a6d9c80ecec025422593209c6dcc5aa4eb45800fb5
  (PID 20473, PGID 20473, abs end bound 00:20:04, written before the gate byte); run1.post.json
  f822339c1ef16508be776601730dad9814eb59e69c9b1c81c9fb8c711342ec80 (returncode 0, wall 154.907 s, reaped); run1.jsonl
  0bb83be9e57213edfe972a3d9d103bc28ee0fe4efecfd7fe7d6ef1e759416fa5; child stdout empty.
- Results (exact; every T with support <= 3 values containing a generator, N even in [2p+2, 4kappa], sum 0), all COMPLETE:
  TARGET kappa = floor(2p/3): p = 37 (24): 0 of 673,288; 41 (27): 0 of 1,112,371; 43 (28): 0 of 1,271,244;
  47 (31): 0 of 1,958,150; 53 (35): 0 of 3,213,595; 59 (39): 0 of 4,993,542; 61 (40): 0 of 5,477,092.
  POS kappa = floor(2p/3)+1: p = 37, 43, 61 (= 1 mod 3): exactly 4 survivors each = F1 and F2 in two unit
  normalisations; p = 41, 47, 53, 59 (= 2 mod 3): 13 survivors each, including F1 (e.g. p = 41: 1^44 3^40) and
  perturbations such as 1^45 3^38 5 (sharpness only; recorded, not analysed further).
- Scope: shortest long zero-sums with support size <= 3 only; independent of Lemma S1-sharp Steps 3-9; not a proof.
