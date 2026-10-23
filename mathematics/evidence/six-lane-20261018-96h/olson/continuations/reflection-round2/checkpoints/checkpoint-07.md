# Reflection round 2 (Slice B), checkpoint 07

Written after host clock 2026-10-19T06:48:46-0700.  Written research only; no process owned or launched; no model call.

## Since checkpoint 06

- results-round2-v1.md (5bfe5efe63c7c91d09159cab16df111deacdcb165035bd0c8f0fcd62c090b672): package summary.
- proof-REFLHI-arcs-v5-erratum-4.md (32811de59e1b5ca736a3db1a9b6592266dbcbcd8690cff27aa143b678e5907f1): parent question on
  Theorem SEG with Pi_need < 0 (possible since R > 2p can occur with B >= 2).  The printed proof is unsupported there; explicit
  narrowing to Pi+ = max(0, Pi_need) in (H1), (H3) and the proof.  The old raw statement is not claimed false.  All applications
  have Pi_need >= 1 (SEG-p, MID: R = p; SEG-num: R < 2p - 1; SEG-k: R <= 2p - 2; K2P+ does not use SEG).
- Region (B) (parent priority): proof-REFLHI-regionB-v2.md (35948d69955ab44faa6464741a2190c97d528218334101b8fc02674422640af3)
  + erratum-1 (94a018c5dbf63112157c6f6c6564887a24e934a1ce68eb7102c14b4c1f0543e3); unsent v1 (1bf4dd3d...a339) superseded.
  Theorem B: kappa = (p - 1)/2 - eps, R = p + delta, 1 <= delta <= (2p - 29 + 2 eps)/7 excluded (any B).  Corollary B.4: for
  1 <= delta <= (p - 12)/3 a remaining avoider has |AB| <= N_O and 2(R - q) < 7 delta - 2p + 29 - 2 eps.
  Explicit conditions: v5 candidate lemmas with errata 1-4.

## Review state (parent)

v5 + errata 1-3 split into three review snapshots (freeze 30d49594...); erratum-4 is outside those snapshots and will be
disposed by the parent.  SEG-k, TRANSFER and region-B stay separate.

## Remaining

Region (B): p <= 17 (eps = 0) / p <= 13 (eps = 1), and delta > (2p - 29 + 2 eps)/7 (for delta <= (p - 12)/3 only the arc-limit
family of Corollary B.4).  Region (A): kappa < (p + 1)/4 (stated obstruction; no lift claimed).  Region (C): k >= 2p + 1,
k <= 3 kappa + 2 (needs a run with |a - b| >= 2H - 2).
