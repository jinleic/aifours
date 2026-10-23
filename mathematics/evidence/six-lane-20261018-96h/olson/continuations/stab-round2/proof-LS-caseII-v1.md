# LS at its threshold: the dominant-value case (II) is impossible (inductive, written), v1

Owner OlsonSTABSuccessor (Slice A).  Written after /bin/date 2026-10-19T05:01:22-0700.  Status: CANDIDATE, written proof [W], UNREVIEWED.
Depends on: proof-CF-XT-v1.md (aa602d45e154a7787ac3f0270a3c26deb5e8c6a70736cf4a82c700f5368c191f) Lemma CF; proof-ROW-v1.md (a7b73415a83a6d898589c820d311e5ad084e864521adf937f1eee05d69fc4b2d)
Lemmas RS, DGM-p, ROW and the LS-threshold dichotomy; parent-accepted Lemma S1-sharp (verdict review/olson-s1sharp-parent-
verdict-v1.md) and accepted Corollary RED of proof-SLZ-EXT-v2.md + erratum 1 (verdict review/olson-KPS-SLZ-parent-verdict-v1.md);
Cauchy-Davenport (classical).  LS itself is assumed ONLY at smaller kappa (hypothesis H'), as an induction.  No computation.

## 0. Setting
p >= 7 prime, kappa0 := floor(2p/3) < kappa <= p - 2, e := p - kappa (2 <= e, 3e <= p - 1), thr := p + 2kappa + 1.
H'(kappa): LS(p, kappa') holds for every kappa0 < kappa' < kappa.  A LS-counterexample of length thr is a sequence Y of odd
elements, |Y| = thr, with (ZP_kappa) and a long zero-sum; by accepted RED, LS(p, kappa) fails iff one exists.  For such Y,
g := g0 of DGM-p, CF data (delta0, U): delta0 <= 2e - 3, r = |U| = p - 2e + 1 + delta0 <= p - 2, K := r - delta0 = p - 2e + 1.
Case (II): some value mu1 of U has multiplicity v1 >= K + 1; R' := the other terms of U, s := |R'|; then s <= e - 2 and
s = r - v1 <= delta0 - 1.

## 1. Lemma SH (short zero-sums meet long ones; re-derived, not imported from the unreviewed partials)
Assume H'(kappa) and let Y be a LS-counterexample of length thr.  (a) Every zero-sum Z of Y with 2 <= |Z| <= 2e meets every
long zero-sum.  (b) No long zero-sum T contains a zero-sum Z with 2 <= |Z| <= 2e.
Proof.  (a) Let Z (|Z| = z) be disjoint from a long T.  For a zero-sum W of Y - Z, W and WZ are zero-sums of Y, so (ZP_kappa)
excludes |W| in [2kappa + 2, 2p] and |W| in [2kappa + 2 - z, 2p - z]; as z <= 2e, 2p - z >= 2kappa, so Y - Z has (ZP_kappa') with
kappa' := kappa - z/2 >= 0, and T <= Y - Z has length >= 2p + 2 > 2kappa' + 2.  |Y - Z| = p + 2kappa' + 1.  If kappa' <= kappa0 this
contradicts S1-sharp; otherwise kappa0 < kappa' < kappa and it contradicts LS(p, kappa').  (b) T - Z is a zero-sum of length
>= 2p + 2 - 2e = 2kappa + 2, hence (by (ZP_kappa)) long, and disjoint from Z: contradicts (a).  []

## 2. Lemma AP (an arithmetic progression in a short arc)
Let n >= 1, 3n < p, x in Z_p nonzero, a in Z_p.  If {a + rho x : 0 <= rho <= n} lies in a cyclic interval (arc) I of size
<= 2n, then x = 1 or x = -1.
Proof.  The n points a + rho x (1 <= rho <= n) are distinct and lie in I and in I + x, so |I n (I + x)| >= n.  For an arc of size
l <= 2n and the signed representative |x| <= (p - 1)/2, |I n (I + x)| = max(0, l - |x|) + max(0, l - p + |x|).  If |x| >= 2n the
first term is 0 and the second is <= 2n - (p + 1)/2 < n; if p - 2n < |x| < 2n the sum is <= 4n - p < n; so |x| <= p - 2n,
|x| < 2n, and l - |x| >= n gives |x| <= n.  Lift I to an integer interval [alpha, alpha + l - 1].  From a point y of it, y + x
lies in [alpha - n, alpha + 3n - 1], which meets no translate of the lift other than itself (p > 3n - 1); so the lifted points
are y_0 + rho x (integers) inside an interval of length l - 1 <= 2n - 1, and n|x| <= 2n - 1 gives |x| <= 1.  []

## 3. Theorem LS-II
Assume H'(kappa).  A LS-counterexample of length thr is not in case (II).
Proof.  Step 1 (mu1 = +-1).  For t in [delta0 - s, v1] (note delta0 - s >= 1), W := mu1^t R' has |W| = t + s >= delta0 and
|W| + 2rho(W) <= r + 2e - 2 <= 2p, so by CF (F) t mu1 + sigma(R') is not in [0, e - 1] (mod p).  With x1 := mu1^(-1), the e-term
progression {x1 (rho - sigma(R')) : 0 <= rho <= e - 1} avoids the interval [delta0 - s, v1], of size v1 - delta0 + s + 1 =
K + 1 = p - 2e + 2; so it lies in the complementary arc, of size 2e - 2.  Lemma AP (n = e - 1, 3n < p) gives x1 = +-1.
Step 2 (mu1 != 1).  If mu1 = 1, W := 1^(e-1) (v1 >= K + 1 >= e - 1) has rho = e - 1 and |W| + 2rho = 3e - 3 >= delta0: forbidden.
So mu1 = p - 1, i.e. the dominant non-g element is -g.
Step 3 (shape of R').  For R'' <= R' with |R''| = k and phi := sigma(R'') mod p: the sets W = (-g)^t R'' (0 <= t <= v1) have
sigma(W) = phi - t (mod p) and |W| + 2rho <= r + 2e - 2 <= 2p.  First, R'' = empty and t in [p - e + 1, v1] would give
rho = p - t <= e - 1 and |W| + 2rho = 2p - t >= delta0: so v1 <= p - e.  Then: if phi in [e - 1, v1], take rho = e - 1,
t = phi - e + 1: |W| + 2rho = k + phi + e - 1 >= delta0 (as phi >= e - 1 >= delta0 - e + 1... indeed delta0 <= 2e - 3):
forbidden; if phi in [v1 + 1, v1 + e - 1], take rho = e - 1, t = phi - e + 1 in [v1 - e + 2, v1]: forbidden; if phi <= e - 2,
take t = 0, rho = phi: forbidden unless k + 2phi <= delta0 - 1.  Hence
    (R)  for every R'' <= R':  sigma(R'') mod p  is in [0, (delta0 - 1 - |R''|)/2]  or in [v1 + e, p - 1].
In particular (k = 1) every x in R' is TINY (mu_x <= (delta0 - 2)/2) or NEGATIVE (mu_x in [v1 + e, p - 2]; then
nu := p - mu_x in [2, p - v1 - e] <= [2, e - 2], and x = -c'g with c' = 2nu - 1 in [3, 2e - 5]).
Step 4 (tiny sub-multisets are small).  Let R'' <= R' consist of tiny terms, in any order, with prefix sums S_k (integers,
S_k <= k(delta0 - 2)/2).  If some prefix had S_k > (delta0 - 1 - k)/2, take the first such k: S_k <= (delta0 - k)/2 +
(delta0 - 2)/2 < delta0 < v1 + e and S_k > 0, contradicting (R) for that prefix.  So |R''| + 2sigma(R'') <= delta0 - 1, and
|R''| <= (delta0 - 1)/3.
Step 5 (the long zero-sum).  Let T be a long zero-sum.  g(-g) is a zero-sum of length 2, so by SH(a) T contains all M copies of g
or all v1 copies of -g.  If T contains both g and -g, T - g(-g) is a zero-sum of length |T| - 2: if |T| = 2p + 2 this length is 2p
(excluded by (ZP_kappa)); if |T| >= 2p + 4 it is long and misses a pair g, -g, contradicting SH(a).  A T without g lies in
(-g)^(v1) R', of length <= r <= p - 2: not long.  So T = g^M W' with W' <= R', and |W'| = |T| - M >= 2p + 2 - M = delta0 + 2.
A negative x = -c'g in W' gives the zero-sum g^(c') x <= T of length c' + 1 <= 2e - 4: excluded by SH(b).  So W' is tiny, and
Step 4 gives |W'| <= (delta0 - 1)/3 < delta0 + 2: contradiction.  []

## 4. Consequence and exact remainder for LS
Under H'(kappa), a LS-counterexample of length thr is in case (I): with g = g0, delta0 <= e - 2 (v_g >= p + kappa + 2), every value
of U has multiplicity <= p - 2e + 1, r = p - 2e + 1 + delta0 <= p - e - 1.  Excluding case (I) for every kappa would prove LS by
induction on kappa (base: S1-sharp).  Case (I) is NOT treated here.
