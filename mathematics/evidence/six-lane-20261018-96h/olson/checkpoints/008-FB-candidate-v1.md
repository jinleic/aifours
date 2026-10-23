# Checkpoint 008: Lemma FB (candidate) closes the t = kappa^ question; residual moved to (S1)-failure and S(p)

Owner ContinueOlson.  Written after /bin/date 2026-10-19T02:03:28-0700.  Continues checkpoint 007 (a6d46c67...01ea).

## Actual result
- Disposition of the accepted ROT-ZB/BAL-full verdict: evidence/disposition-BALfull-ROTZB-v1.md 55138906...16c4.
- T-MAX scope frozen first: evidence/TMAX-scope-v1.md 858d9a3e...568f.
- CANDIDATE (unreviewed; parent launched both reviews): evidence/proof-FB-v1.md 339dcadcd914a9f036ea71a5ec2b5d3f0678cc100e22aca9de2d75751373cc6b.
  Lemma FB: in (S'), S(N) <= 2p - 1 - W for every longest Z and every index-<1 g (balance + room, no L-vs-t hypothesis).
  Theorem ROT-FB: terminal 2 <= k <= p - 1, kappa^ >= 1, (S1) at kappa^ (automatic for kappa^ <= floor(2p/3)) => rotation
  rigidity; also k = p when every zero-sum has length <= 2kappa^ - 2 (then L >= p + 2, so SC0/REALIZE/ZSTRUCT apply).
  Corollary: INV* and ordered Olson for o_F <= p - 1 and F - o_F >= 2(p - 1 - floor(2p/3)), p >= 7.
  ROUTE-ALL(T) holds: no option-(ii) obstruction exists.
- Aids: evidence/probe-v10/RECEIPT-v9-v10-v1.md a5d3da6ae896f2f34ebaff66d564ad69b9c27dd64706e09e686438d7039aa134 (0 counterexamples; positive control 100%).

## Exact blocker (rotation half, terminal k <= p)
(i) kappa^ >= floor(2p/3) + 1 with (S1) FAILING: the rotation sequence has a zero-sum of length >= 2p + 2; the longest
zero-sum's complement then has length <= 2kappa^ - k - 2 <= k - 4, so SC0 does not apply (S1-sharp's F1/F2 show (ZP) alone
does not exclude this).  (ii) k = p with a zero-sum of length exactly 2kappa^ (complement of length p; S(p) open).

## Next bounded action
Written work on (i): structure of (ZP)-sequences failing (S1) for kappa > floor(2p/3) (inverse form of S1-sharp) and a
word-level (GRX arc) attack on the resulting families; respond to FB reviews.
