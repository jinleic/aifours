# LS at its threshold: the dominant-value case (II) is impossible (inductive, written), v2

Owner OlsonSTABSuccessor (Slice A).  Written after /bin/date 2026-10-19T05:11:38-0700.  Status: CANDIDATE, written proof [W], UNREVIEWED.
v2 supersedes v1 (proof-LS-caseII-v1.md, never sent): the rho-wording in Steps 1 and 3 is repaired exactly as in
erratum-1-CF-XT-ROW-range.md E3, and one garbled justification in Step 3 is rewritten; no statement changed.
Depends on: proof-CF-XT-v1.md (aa602d45e154a7787ac3f0270a3c26deb5e8c6a70736cf4a82c700f5368c191f) Lemma CF and proof-ROW-v1.md (a7b73415a83a6d898589c820d311e5ad084e864521adf937f1eee05d69fc4b2d)
Lemmas RS, DGM-p, ROW and the LS-threshold dichotomy, both read through erratum-1-CF-XT-ROW-range.md; parent-accepted Lemma
S1-sharp (review/olson-s1sharp-parent-verdict-v1.md) and accepted Corollary RED of proof-SLZ-EXT-v2.md + erratum 1
(review/olson-KPS-SLZ-parent-verdict-v1.md); Cauchy-Davenport (classical).  LS is assumed ONLY at smaller kappa (hypothesis H'),
as an induction.  No computation.

## 0. Setting
p >= 7 prime, kappa0 := floor(2p/3) < kappa <= p - 2, e := p - kappa (2 <= e, 3e <= p - 1), thr := p + 2kappa + 1.
H'(kappa): LS(p, kappa') for every integer kappa0 < kappa' < kappa.  A LS-counterexample of length thr: odd Y, |Y| = thr, (ZP_kappa),
a long zero-sum; by accepted RED, LS(p, kappa) fails iff one exists.  For such Y: g := g0 of DGM-p, CF data (delta0, U),
delta0 <= 2e - 3, r = |U| = p - 2e + 1 + delta0 <= p - 2, K := r - delta0 = p - 2e + 1.  Case (II): some value mu1 of U has
multiplicity v1 >= K + 1; R' := the other terms of U, s := |R'|; then s <= e - 2 and s = r - v1 <= delta0 - 1.
Throughout, every W <= U has |W| <= r, so 'rho(W) in [0, e - 1] and |W| + 2rho(W) >= delta0' already contradicts CF (F)
(as then |W| + 2rho(W) <= r + 2e - 2 <= 2p).  Call such W forbidden.

## 1. Lemma SH (re-derived; the unreviewed SHIFT of the partials is not used)
Assume H'(kappa); Y a LS-counterexample of length thr.  (a) Every zero-sum Z of Y with 2 <= |Z| <= 2e meets every long
zero-sum.  (b) No long zero-sum T contains a zero-sum Z with 2 <= |Z| <= 2e.
Proof.  (a) Let Z (|Z| = z) be disjoint from a long T.  For a zero-sum W of Y - Z, W and WZ are zero-sums of Y, so (ZP_kappa)
excludes |W| in [2kappa + 2, 2p] and in [2kappa + 2 - z, 2p - z]; as z <= 2e, 2p - z >= 2kappa, so Y - Z has (ZP_kappa'),
kappa' := kappa - z/2 >= 0, and T <= Y - Z is a zero-sum of length >= 2p + 2 > 2kappa'.  |Y - Z| = p + 2kappa' + 1.  If
kappa' <= kappa0 this contradicts S1-sharp; otherwise kappa0 < kappa' < kappa and it contradicts LS(p, kappa').  (b) T - Z is a
zero-sum of length >= 2p + 2 - 2e = 2kappa + 2, hence long by (ZP_kappa), and disjoint from Z: contradicts (a).  []

## 2. Lemma AP
Let n >= 1, 3n < p, x in Z_p nonzero, a in Z_p.  If {a + rho x : 0 <= rho <= n} lies in an arc I of size <= 2n, then x = +-1.
Proof.  The n points a + rho x (1 <= rho <= n) are distinct and lie in I n (I + x).  For an arc of size l <= 2n and the signed
representative 0 < |x| <= (p - 1)/2, |I n (I + x)| = max(0, l - |x|) + max(0, l - p + |x|).  If |x| >= 2n this is
<= 2n - (p + 1)/2 < n; if p - 2n < |x| < 2n it is <= 4n - p < n; so |x| <= p - 2n, |x| < 2n and l - |x| >= n, i.e. |x| <= n.  Lift
I to [alpha, alpha + l - 1].  For y in the lift, y + x lies in [alpha - n, alpha + 3n - 1], which meets no other translate of the
lift by a multiple of p (p > 3n - 1); so the lifted points are y_0 + rho x (integers) in an interval of length <= 2n - 1, and
n|x| <= 2n - 1 gives |x| = 1.  []

## 3. Theorem LS-II
Assume H'(kappa).  A LS-counterexample of length thr is not in case (II).
Proof.  Step 1 (mu1 = +-1).  For t in [delta0 - s, v1] (delta0 - s >= 1), W := mu1^t R' has |W| = t + s >= delta0, so W is not
forbidden only if rho(W) avoids [0, e - 1]: t mu1 + sigma(R') avoids [0, e - 1] (mod p).  With x1 := mu1^(-1) mod p, the e-term
progression {x1 (rho - sigma(R')) : 0 <= rho <= e - 1} avoids the interval [delta0 - s, v1] of size v1 - delta0 + s + 1 = K + 1 =
p - 2e + 2, so it lies in the complementary arc of size 2e - 2.  Lemma AP (n = e - 1, 3n < p): x1 = +-1, i.e. mu1 = +-1.
Step 2 (mu1 != 1).  If mu1 = 1, W := 1^(e-1) (v1 >= K + 1 >= e - 1) has rho = e - 1 and |W| + 2rho = 3e - 3 >= delta0: forbidden.
So mu1 = p - 1: the dominant non-g element is -g.
Step 3 (shape of R').  First, W = (-g)^t with p - e + 1 <= t <= v1 would have rho = p - t <= e - 1 and |W| + 2rho = 2p - t >= delta0:
forbidden; so v1 <= p - e.  Let R'' <= R', k := |R''|, phi := sigma(R'') mod p, and W := (-g)^t R'' (0 <= t <= v1), so
sigma(W) = phi - t (mod p).
- If e - 1 <= phi <= v1: t := phi - e + 1 in [0, v1] gives rho(W) = e - 1 and |W| + 2rho = k + phi + e - 1 >= 2e - 2 > delta0: forbidden.
- If v1 + 1 <= phi <= v1 + e - 1: t := phi - e + 1 in [v1 - e + 2, v1] (v1 >= e) gives rho(W) = e - 1 and |W| + 2rho >= v1 + e > delta0:
  forbidden.
- If phi <= e - 2: t := 0 gives rho(W) = phi, forbidden unless k + 2phi <= delta0 - 1.
Hence (R): for every R'' <= R', sigma(R'') mod p lies in [0, (delta0 - 1 - |R''|)/2] or in [v1 + e, p - 1].
For k = 1: every x in R' is TINY (mu_x <= (delta0 - 2)/2) or NEGATIVE (mu_x in [v1 + e, p - 2]; then nu := p - mu_x is in
[2, p - v1 - e], p - v1 - e <= e - 2, and x = -c'g with c' = 2nu - 1 in [3, 2e - 5]).
Step 4 (tiny sub-multisets).  Let R'' <= R' consist of tiny terms in any order, prefix sums S_k (integers).  If some prefix had
S_k > (delta0 - 1 - k)/2, the first such k has 0 < S_k <= (delta0 - k)/2 + (delta0 - 2)/2 < delta0 < v1 + e (and < p), contradicting
(R) for that prefix.  So |R''| + 2sigma(R'') <= delta0 - 1; in particular |R''| <= (delta0 - 1)/3.
Step 5 (the long zero-sum).  Let T be a long zero-sum.  g(-g) is a zero-sum of length 2, so by SH(a) T contains all M copies of g or
all v1 copies of -g.  If T contains both g and -g, T - g(-g) is a zero-sum of length |T| - 2: for |T| = 2p + 2 this is 2p, excluded
by (ZP_kappa); for |T| >= 2p + 4 it is long and misses a pair g, -g, contradicting SH(a).  A T without g lies in (-g)^(v1) R', of
length <= r <= p - 2: not long.  So T = g^M W', W' <= R', |W'| = |T| - M >= 2p + 2 - M = delta0 + 2.  A negative x = -c'g in W'
gives the zero-sum g^(c') x <= T of length c' + 1 <= 2e - 4, excluded by SH(b).  So W' is tiny, and Step 4 gives
|W'| <= (delta0 - 1)/3 < delta0 + 2: contradiction.  []

## 4. Consequence and exact remainder for LS
Under H'(kappa), a LS-counterexample of length thr lies in case (I): g = g0 has v_g >= p + kappa + 2 (delta0 <= e - 2), every value
of U has multiplicity <= p - 2e + 1, and r = p - 2e + 1 + delta0 <= p - e - 1.  Excluding case (I) for every kappa in the range
would prove LS by induction on kappa (base: S1-sharp).  Case (I) is NOT treated here.
