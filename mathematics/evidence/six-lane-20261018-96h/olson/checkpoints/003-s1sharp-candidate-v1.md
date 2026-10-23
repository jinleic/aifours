# Checkpoint 003: Lemma S1-sharp candidate frozen; independent aids; next slice

Owner ContinueOlson.  Written after /bin/date 2026-10-19T00:21:30-0700.  Continues checkpoint 002 (92dd6cc1...e637).

## Actual result
- CANDIDATE (unreviewed): evidence/proof-S1-sharp-v1.md sha256 992ab63f40aa08626560ccf121b0004a08588fdb24805ff4eb30d25a2150cb0c
  (frozen 00:11:26).  Lemma S1-sharp: (ZP_kappa) => (S1_kappa) for every prime p >= 5 and every 0 <= kappa <= floor(2p/3);
  sharp (fails at floor(2p/3)+1: F1 = g^(p+3)(3g)^(p-1); F2 = g^(2p-1)(((2p+1)/3)g)^3 for p = 1 mod 3).  Corollary
  (through the accepted ZX/REFL/ledger/RGR-LONG chain): INV* and ordered Olson for D_2p for every word with
  3 o_F <= 2p+1, every prime p >= 5; residual family Q2 empty.  Parent re-read Steps 1-9 (no gap found yet) and
  launched both hostile reviews of the exact v1 bytes (run review/olson-s1sharp-{codex,claude}-v1.*); no duplicate
  reviews by this lane.
- Aids (never premises): probe v1 (restricted representation; receipt 4351a750...3f8f), probe v2/v3 (support <= 3 exact,
  independent of Steps 3-9; receipts db784ec3...70a5, c4f89301...c9bc): TARGET kappa = floor(2p/3) 0 survivors at
  p = 13, 31, 37, 41, 43, 47, 53, 59, 61; POS kappa+1 survivors at every tested p (F1, F2 and perturbations).
- Process: probe v1 PID recorded only by later ps census (deviation acknowledged by parent); v2/v3 used the stdin-gated
  launcher code/lane_launcher_v2.py (c10c2855...aef4) with exclusive pre-compute records before the gate byte.

## Exact blocker / residual after S1-sharp (if accepted)
Rotation half: Q1a (k = p, kappa^ >= 2) and Q1b ((2p+1)/3 < k <= p-1, kappa^ >= 2, T4 failing).  From T4's K'
(k - 1 + G(kappa^) <= 2p - k - 3) with G(kappa) ~ 2kappa - 4 sqrt(kappa) + 1, Q1b at k = p - j lies roughly at
kappa^ > j + 2 sqrt(j) (or Lambda failing, or kappa^ > (p-1)/2): the residual concentrates at k close to p.  The
binding obstruction there is word-level (SHgen (K) / FLEXa), not sequence-level.  Reflection half: o_F > p.

## Next bounded action
Written: (i) respond to review findings on S1-sharp (new version only if needed); (ii) map the post-S1-sharp residual
precisely (exact Q1b' cells for small p) as a planning note; (iii) explore a word-level mechanism for k close to p
(arc/winding generalisation of ROT-KP Part A with structured rotation multisets).  No launch planned.
