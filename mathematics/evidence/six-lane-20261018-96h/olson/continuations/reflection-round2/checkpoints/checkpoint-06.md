# Reflection round 2 (Slice B), checkpoint 06

Written after host clock 2026-10-19T06:24:28-0700.  Written research only; no process owned or launched.

## New since checkpoint 05

- proof-REFLHI-transfer-v2.md (dc1974c8e8c8229002dd02e6bb4ef1e97cd123f7d411479bcd7d8cc9b58729fa), separate from the v5 delta
  set: Lemma INV (RED process: D = A - B constant; B, kappa, g = kappa - B non-increasing; terminal cell (g_T, B_T) in the box
  [1, g_0] x [0, B_0] with k_T = 2p - D_0 + 2 g_T, R_T = D_0 + 2 B_T), Theorem TRANSFER (REFL for an initial word if all box
  cells are excluded), Corollaries T1 (|A - B| <= 1 and o_F >= 3 kappa + 3), T2 (o_F >= 4 kappa + 5 and
  A + floor((A - B)/2) <= p + 1), T3 (box reduction).  Unsent v1 (874a3911...6e28) superseded.
- Corrected size of region (C) (k >= 2p + 1, k <= 3 kappa + 2): it is not thin; it is about p^2/6 cells per prime
  (kappa in [(2p - 1)/3, p - 1]).  By T3, region-(C) cells never occur in the box of an initial word with o_F >= 3 kappa_0 + 3.

## Failed direction (exact count), recorded

Z_(2p)/Kneser arc method for region (A) with base arcs crossing nonempty runs: all windows are floor-type for
m in [kappa + 1, p - floor(R/2)] whatever E+ is, and the kill needs gain 2p - R - 1 = k - 2 kappa - 1.  But every unit of gain
uses a distinct block-to-block step inside one piece (base arc or segment), so total gain <= k - (number of pieces) <=
k - 2(kappa + 1) < k - 2 kappa - 1.  The method misses by at least one in the worst case (two-valued psi along every piece);
it can only succeed through extra value diversity.  Not pursued further.

## Coverage summary (unchanged since checkpoint 05 except the size of (C))

Excluded (CANDIDATE, any B): K2P+, SEG-k, SEG-num, R = p with kappa >= (p + 1)/4 (p >= 11).  Remaining: (A) kappa < (p + 1)/4;
(B) kappa in {(p - 3)/2, (p - 1)/2} with R > p; (C) k >= 2p + 1, k <= 3 kappa + 2 (needs exact m-control or giant-run handling).

## Next

Exact m-control version of K2P+ (TOP technique) to cover (C) cells with m_hi >= m_lo, and a giant-run lemma for the rest of (C).
