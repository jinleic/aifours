# balance_probe_v5 run1: receipt (aid only; never a premise)

Written after /bin/date 2026-10-19T00:38:55-0700.  Owner ContinueOlson.  Plan sent to parent before launch (IRC about 00:32).
- Probe code/balance_probe_v5.py 1ba1b89849f60df36428be316286ce0c0f013b6f9ff5572f93a7d97b17e951e7 (frozen 00:32:39;
  supersedes code/balance_probe_v4.py b3a8a7dc...a6d3, frozen 00:30:59 and never run).  Launcher v2 c10c2855...aef4.
- Shell START 2026-10-19T00:33:03-0700, END 00:37:34.  run1.pre.json 623803ffb837fcea2a0ab8d0759edb6321a4883d0e922aafa5398e36144e19f8
  (PID 24079 = PGID, written before the gate byte); run1.post.json 1bc2d93ec365fe0a11bd9fea6ea9153c9ab1ffe605f48908f41c72195804e242
  (returncode 0, wall 270.042 s, reaped); run1.jsonl 7d1a7011a895f55bb8857eb9a0880d62baaadc102f6c186ccf0bd740d4a1c329.
- Question: where Lemma LAMBDA's hypotheses fail (8kappa > 4p-3k+5 and 2kappa(2kappa-1) >= 2p), with (2p+1)/3 < k <= p-1
  and 2kappa + k <= 2p-1, can every longest zero-sum Z of a (S1)-sequence Y (|Y| = 2p+2kappa-k) be unbalanced?
- Results (exact over every Y with support <= 3 containing a generator): CONTROL (13,10,2), (13,12,2), (17,14,3)
  (LAMBDA holds): 0 unbalanced, 0 ZSTRUCT violations, 0 missing generators.  TEST items COMPLETE: all 12 at p = 13, all
  29 at p = 17, 20 of the p = 19 items (k = 18, 17, 16 all kappa; k = 15 kappa = 5); (19,15,6) BUDGET_STOP after 64 (S1)
  sequences; remaining p = 19 items and all p = 23 items NOT_STARTED.  In every completed item: some_unbal = 0 (no
  longest Z is unbalanced for any index-<1 generator), all_unbal = 0, zstruct_viol = 0, no_gen = 0.
- Scope: support <= 3 only; small p; aid suggesting that balance may hold beyond LAMBDA's range; not a proof.
