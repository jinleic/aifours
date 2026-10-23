# Checkpoint 1 — 2026-10-17T15:37:15-07:00 (host clock)

Done:
- Encoders copied byte-identically from the snapshot (code/gram_a.py bf1aada1…d05a, code/gram_a_r3.py 40622a6f…dbb).
- Driver code/bind.py (sha d98924283ba1b151ea76ef033e713a6e442c0987fb262064ba4abdb14b46a7fc) and guard code/guard.py (sha 4042db2b250f7a456c512d23c18cdc072aaea60229d4c4638b22d029868d1efb) written once (mode x).
- Checker sensitivity controls on order-7 builds: 7/7 mutations detected for the intended reason, unmutated clean
  (checker_controls_order7.json + .addendum.json — the addendum corrects a summary-field bug in the first file).
- K5 bind run 15:33:48–15:35:24: regenerated SHA 6ecb77a7…469b = README §8 = map meta = stored lane file (137664569
  bytes); 0 classifier errors; per-family multiset equal to the independent generator; P4: exactly 5 at-least-one
  clauses (squares 1–5 × row 0); 35 lexeq vars (square 1, pairs (i,i+1), i = 2..6); SB2 units = declared 35;
  G2 all 10 pairs × 1568; C12 classical AG(2,8) control: canonical assignment violates only the 5 P4 at-least-one
  clauses and 2 SB2 units of square 1 (|S1| = 3 part); std/strong variants SAT with verified models, mutation UNSAT.
  Peak sampled tree RSS 1.66e9 bytes.
Running: K4 bind (same driver). Next: flag variants (encoder --p4 none, no --sb2) for K5 and K4; K4 §9 split-list
semantics against the regenerated K4 name table; receipt binding-result.json.
