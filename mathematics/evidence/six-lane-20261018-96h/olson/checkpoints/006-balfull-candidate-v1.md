# Checkpoint 006: BAL-full proved in written form (candidate); falsification controls run

Owner ContinueOlson.  Written after /bin/date 2026-10-19T01:11:31-0700.  Continues checkpoint 005 (4999be8b...394a).

## Actual result
- CANDIDATE (unreviewed): evidence/proof-BALfull-v2.md sha256 dffbfea8d97730e6c7a7a5f384cb471c64dda17091829fcd289a5c5a9775a3e1
  (scope frozen first: evidence/BALfull-scope-v1.md f2b82c5e...2f315; v1 a82fe520...ad36 never sent).  Lemma BAL-forall:
  in (S'), L >= 2t + 1 (implied by 2kappa + k <= 2p - 1) => every longest Z balanced w.r.t. every index-<1 generator g.
  Theorem ROT-ZB+ and Corollary: INV* and ordered Olson for o_F <= p - 1 with F >= 2o_F - 1, every prime p >= 7.
- Controls: evidence/probe-v6/RECEIPT-v6-v8-v1.md sha256 a011b83cad4df7dd2611ce02cd5edc665ff11191d1922cc068a000477946562d: exhaustive p = 7 (R = 10..17) and random p = 11..19:
  0 counterexamples, 0 ZSTRUCT violations; v7 showed the L < 2t unbalanced items are degenerate (2t > 2p); v8 found no
  unbalanced longest Z inside t < p, p + 1 <= L <= 2t.

## Exact blocker (rotation half, after BAL-full)
High cells 2kappa^ + k >= 2p (k <= p - 1; needs (2p+2)/3 <= k) and k = p (Q1a): in both, the bottleneck is a longest
zero-sum of maximal length t = kappa^ (then L <= 2t; also ROOM needs L >= 2t and SHgen (H) needs n+ <= 2p - 1 - k).  For
t <= kappa^ - 1 the same chain closes k = p when 2 <= kappa^ <= (p+3)/2 (written note to follow, not a claim yet).
Reflection half o_F > p untouched.

## Next bounded action
Respond to ROT-ZB/BAL-full reviews.  Written attempt: (i) BAL for all t < p via minimal-piece reduction (an unbalanced
minimal piece Z_1 is longest in Y' Z_1; index-one theorem when |Z_1| >= p + 2); (ii) the t = kappa^ obstruction.
