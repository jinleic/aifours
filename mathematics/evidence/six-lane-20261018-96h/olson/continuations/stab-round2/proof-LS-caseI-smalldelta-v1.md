# LS at its threshold, case (I) with delta0 <= 2 and a long zero-free part; corollary: LS(p, kappa) for p - kappa in {2, 3, 4}, v1

Owner OlsonSTABSuccessor (Slice A).  Written after /bin/date 2026-10-19T05:17:13-0700.  Status: CANDIDATE, written proof [W], UNREVIEWED.
Depends on: proof-CF-XT-v1.md (aa602d45e154a7787ac3f0270a3c26deb5e8c6a70736cf4a82c700f5368c191f) Lemma CF; proof-ROW-v1.md (a7b73415a83a6d898589c820d311e5ad084e864521adf937f1eee05d69fc4b2d)
DGM-p and the LS-threshold dichotomy; both through erratum-1-CF-XT-ROW-range.md (767fe8f8605019b3b3b7aa1ff6a610f088279ede30b9b3429544d4c8487c1db7);
proof-LS-caseII-v2.md (3df159ff61784cb3345b27a6cf9da873900051df92dbb3be019e846578d73a43) + addendum 1 (Theorem LS-II'); accepted Corollary RED (proof-SLZ-EXT-v2.md + erratum 1,
review/olson-KPS-SLZ-parent-verdict-v1.md); the classical index-one theorem exactly as in the parent import record (run of
2026-10-16, review/olson-index-one-primary-statement-parent-v1.md, e461514461d23287beeecf04fa26334efd91d3de51caa33312f6c5b10b4d35c6), used with n = p prime.  No
induction hypothesis; no computation; LS is not assumed.

## 1. Proposition I-small
Let p >= 7 prime, kappa0 + 1 <= kappa <= p - 2, e := p - kappa, and let Y be a LS-counterexample of length thr = p + 2kappa + 1 in
case (I) (g = g0, delta0 <= e - 2, r = |U| = p - 2e + 1 + delta0).  If delta0 <= 2 and 4e <= p + 1 + 2delta0, contradiction.
Proof.  (A) Every nonempty W <= U has rho(W) not in [0, e - 1]: otherwise |W| + 2rho(W) >= delta0 (if rho >= 1 it is >= 3; if
rho = 0, W is a zero-sum mod p of nonzero terms, so |W| >= 2) and |W| + 2rho(W) <= r + 2e - 2 <= 2p, contradicting CF (F).  In
particular U is zero-sum-free over C_p = Z_p and its nonempty subset sums avoid [0, e - 1].
(B) r >= (p + 1)/2 (this is 4e <= p + 1 + 2delta0).  U (-sigma(U)) is a minimal zero-sum over C_p of length r + 1 >= floor(p/2) + 2
(a proper zero-sum subsequence would give a nonempty zero-sum of U, directly or as a complement), so by the index-one theorem
there are a != 0 and integers x_i >= 1 (one for each term of U) with mu_i = x_i a and S := sum x_i <= p - 1.
(C) Every integer in [0, S] is a subset sum of (x_i).  Sort x_1 <= ... <= x_r.  If x_k > 1 + sum_(i<k) x_i for some k, then x_i >= k + 1
for all i >= k and S >= (k - 1) + (r - k + 1)(k + 1) >= min(3r - 2, 2r) = 2r >= p + 1 (k = 1 gives S >= 2r directly; the middle
expression is concave in k on [2, r]), contradicting S <= p - 1.  So the standard greedy induction gives all of [0, S].
(D) By (A) and (C), a s is not in [0, e - 1] for every s in [1, S]; so rho a^(-1) lies in [S + 1, p - 1] for every rho in [1, e - 1].
This arc has size p - 1 - S <= p - 1 - r = 2e - 2 - delta0 <= 2e - 3 = 2n + 1 with n := e - 2 >= 1 (e >= 3 in case (I)).
Lemma AP' below gives a^(-1) in {1, -1, 2, -2}.  a^(-1) = 1 or 2 puts rho = 1 at 1 or 2 < S + 1; a^(-1) = -2 needs
p - 2(e - 1) >= S + 1, i.e. S <= p - 2e + 1 < r <= S.  So a^(-1) = -1, a = -1, and mu_i = -x_i (mod p).
(E) CF (L) gives W* <= U and j >= 1 with p | sigma(W*) + j and |W*| >= delta0 + 2j.  sigma(W*) = -s* (mod p) with
s* := sum over W* of x_i in [|W*|, S] <= [1, p - 1]; so j = s* (mod p) and j >= 1 force j >= s*.  Then |W*| >= delta0 + 2s* > s* >= |W*|.
Contradiction.  []
Lemma AP'.  Let n >= 1 and 3n + 2 < p.  If an (n + 1)-term progression with difference x != 0 lies in an arc I of size <= 2n + 1
of Z_p, then x is in {1, -1, 2, -2}.
Proof.  As in Lemma AP (proof-LS-caseII-v2.md Sec. 2) with l <= 2n + 1: n <= |I n (I + x)| = max(0, l - |x|) + max(0, l - p + |x|).
|x| >= l gives n <= 2n + 1 - (p + 1)/2, false; p - l < |x| < l gives n <= 2l - p <= 4n + 2 - p, false; so |x| <= p - l and
|x| <= l - n <= n + 1.  Then p - l > n + 1 >= |x| (p > 3n + 2), so the lifted points form an integer progression in an interval of
length <= 2n, and n|x| <= 2n gives |x| <= 2.  []

## 2. Corollary LS-small (unconditional, relative to the listed imports)
LS(p, kappa) holds for: kappa = p - 2 and every prime p >= 7; kappa = p - 3 and every prime p >= 11; kappa = p - 4 and every
prime p >= 13.
Proof.  These kappa satisfy kappa0 + 1 <= kappa <= p - 2 exactly in the stated p-ranges.  By accepted RED it suffices to exclude a
LS-counterexample Y of length thr.  By the dichotomy and Theorem LS-II', Y is in case (I), so delta0 <= e - 2.  e = 2: impossible
(delta0 >= 1).  e = 3: delta0 = 1 and 4e = 12 <= p + 3.  e = 4: delta0 in {1, 2} and 16 <= p + 1 + 2delta0 for p >= 13.
Proposition I-small applies.  []
Scope.  Sequence-level statements only; no INV*/ordered-Olson claim.  For p - kappa >= 5 case (I) remains open (delta0 >= 3
allows zero-sums mod p of size < delta0 in U, and for large e the zero-free part is shorter than (p + 1)/2).
