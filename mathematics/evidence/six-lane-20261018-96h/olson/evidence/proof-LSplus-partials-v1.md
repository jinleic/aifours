# LS+ partial results: extremal two-value structure (Lemma TV), inductive structure (Lemmas RED+, SHIFT), v1

Owner ContinueOlson (math-2 lane, 96-hour continuation).  Written after /bin/date 2026-10-19T03:39:13-0700.  Status: CANDIDATE PARTIALS,
written proofs [W], UNREVIEWED.  Scope frozen first: evidence/LSplus-scope-v1.md 7dc04949c1152907eef9938c4680248eeb24d5830ab751f67f1355ba6e0e2cbc.  LS+ itself is NOT
proved and not assumed (Lemmas RED+ and SHIFT are conditional on LS+ at smaller kappa, stated explicitly).  No computation
is a premise.  No novelty claim; no Lean.

## 0. Notation
p >= 5 prime, kappa0 := floor(2p/3), e := p - kappa.  Odd elements of Z_(2p); (ZP_kappa), (S1_kappa), LONG (length
>= 2kappa + 2; under (ZP_kappa) >= 2p + 2) as in evidence/proof-SLZ3-v1.md (0cfe637f919bdaab937f8292fa527d7fbd54e3af7d55bb07ddf137c0ad263c1c).  LS+(p, kappa): every (ZP_kappa)
sequence failing (S1_kappa) has length <= 3kappa + 1.  H(kappa): LS+(p, kappa') for every kappa0 < kappa' < kappa.
Fact S (S1-sharp): for kappa' <= kappa0, (ZP_kappa') implies (S1_kappa'), so a (ZP_kappa') sequence has no long zero-sum.

## 1. Lemma TV (two values {h, 3h}; exact extremal structure)
Let kappa0 + 1 <= kappa <= p - 1 and Y = h^a (3h)^b (h odd, a, b >= 0).  If Y satisfies (ZP_kappa) and fails (S1_kappa),
then a + b <= 3kappa + 1, with equality exactly for
    E2: (a, b) = (3kappa - p + 2, p - 1)    and    E3: (a, b) = (3kappa - 2p + 2, 2p - 1),
both of which satisfy (ZP_kappa) and fail (S1_kappa) for every generator h.
Proof.  If h = p (the involution), Y = p^(a+b) and (ZP_kappa) forces a + b <= 2kappa + 1 < 2p + 2, so no long zero-sum: so h
is a generator.  Zero-sums are h^i (3h)^j with i <= a, j <= b, i + 3j = 2pk (k >= 1), of length 2pk - 2j.  (ZP_kappa)
excludes h^(2p) and (3h)^(2p), so a, b <= 2p - 1 and a + 3b <= 8p - 4: k <= 3.  For level k let
J_k := [max(0, ceil((2pk - a)/3)), min(b, floor(2pk/3))] (an integer interval of feasible j).  A length lies in
[2kappa + 2, 2p] iff j in [p(k-1), pk - kappa - 1]; it is long iff j <= p(k-1) - 1.  Let k* be the least level with a long
zero-sum (j0 in J_(k*), j0 <= p(k* - 1) - 1); k* in {2, 3}.
- k* = 2.  If b >= p, then p in J_2 (ceil((4p - a)/3) <= j0 < p <= floor(4p/3)), a zero-sum of length 2p: so b <= p - 1.
  J_1 is nonempty (a <= 2p - 1 gives ceil((2p - a)/3) >= 1, and (2p - a)/3 < (4p - a)/3 <= j0 <= b, (2p - a)/3 <= 2p/3), so
  its least element must be >= p - kappa (else a length in [2kappa + 2, 2p]): ceil((2p - a)/3) >= p - kappa, i.e.
  a <= 3kappa - p + 2.  Hence a + b <= 3kappa + 1, with equality only at E2.
- k* = 3.  If b >= 2p then 2p in J_3: excluded, so b <= 2p - 1.  J_2 is nonempty ((4p - a)/3 <= (3j0 - 2p)/3 < b, as
  6p - 3j0 <= a) and, by minimality of k* and (ZP_kappa), J_2 meets neither [0, p - 1] nor [p, 2p - kappa - 1]:
  ceil((4p - a)/3) >= 2p - kappa, i.e. a <= 3kappa - 2p + 2.  Hence a + b <= 3kappa + 1, with equality only at E3.
E2: level 1 has j >= ceil((2p - a)/3) = p - kappa (lengths <= 2kappa); level 2 has j in [ceil((5p - 3kappa - 2)/3), p - 1],
nonempty as 3kappa >= 2p + 1, lengths >= 2p + 2; a + 3b < 6p.  E3: level 1 has j >= p - kappa; level 2 has
j >= ceil((6p - 3kappa - 2)/3) = 2p - kappa (lengths <= 2kappa); level 3 has j in [ceil((8p - 3kappa - 2)/3), 2p - 1],
nonempty as 3kappa >= 2p + 1, lengths >= 2p + 2; a + 3b = 3kappa + 4p - 1 < 8p.  []
(Probe v12's longest (ZP)-and-not-(S1) multisets are exactly E2 and E3 up to the choice of h, e.g. 1^18 3^10 = E2 and
1^21 15^7 = E3 with h = 15 at p = 11, kappa = 9; aid only.)

## 2. Lemma RED+ (inductive structure; conditional on H(kappa))
Let kappa0 + 1 <= kappa <= p - 2.
(a) If LS+(p, kappa) fails, it fails for a sequence of length exactly 3kappa + 2 (cut a counterexample down around a shortest
    long zero-sum, which has length <= 3kappa + 1 by SLZ3).
(b) Assume H(kappa).  Every (ZP_kappa) sequence V that fails (S1_kappa) and has |V| >= 3kappa - 1 contains a zero-sum of
    length exactly 2kappa.  In particular, in a counterexample Y of length 3kappa + 2, every subsequence of length
    >= 3kappa - 1 containing a long zero-sum contains a 2kappa-zero-sum.
Proof of (b).  Otherwise V satisfies (ZP_(kappa-1)) and still fails (S1_(kappa-1)) (its long zero-sum has length >= 2p + 2),
contradicting Fact S if kappa - 1 = kappa0, and LS+(p, kappa - 1) (|V| >= 3(kappa - 1) + 2) otherwise.  []

## 3. Lemma SHIFT (short zero-sums meet long ones)
Let kappa0 + 1 <= kappa <= p - 2 and let Y satisfy (ZP_kappa).  Let Z be a zero-sum subsequence of Y with
2 <= z := |Z| <= 2e, and suppose Y - Z contains a long zero-sum.  Put kappa' := kappa - z/2.  Then kappa' > kappa0, and if
LS+(p, kappa') holds, |Y| <= 3kappa + 1 - z/2.
Proof.  For every zero-sum W of Y - Z, W u Z is a zero-sum of Y of length |W| + z, so (ZP_kappa) excludes
|W| in [2kappa + 2 - z, 2p - z]; as z <= 2e, 2p - z >= 2kappa, and with (ZP_kappa) for Y - Z (lengths are even) Y - Z has no
zero-sum of length in [2kappa' + 2, 2p]: it satisfies (ZP_kappa').  Its long zero-sum (length >= 2p + 2 >= 2kappa' + 2)
makes it fail (S1_kappa').  Fact S excludes kappa' <= kappa0.  LS+(p, kappa') gives |Y| - z <= 3kappa' + 1.  []
Corollary SHIFT-C (conditional on H(kappa)).  In a counterexample Y to LS+(p, kappa) (|Y| >= 3kappa + 2):
- every zero-sum of length in [2, 2e] meets every long zero-sum (else |Y| <= 3kappa + 1 - z/2 < 3kappa + 2);
- if |Y| = 3kappa + 2 and 5kappa <= 4p + 1, the complement X = Y - T of every long zero-sum T is zero-sum-free
  (|X| <= 3kappa - 2p <= 2e + 1, so a zero-sum in X would have length <= 2e and miss T); in particular sigma(Y) != 0 (else X,
  nonempty by SLZ3, would be a zero-sum).
LS version.  With LS in place of LS+ (H'(kappa): LS(p, kappa') for kappa0 < kappa' < kappa; Fact S covers kappa' <= kappa0):
in a counterexample Y to LS(p, kappa) of length p + 2kappa + 1, every zero-sum of length in [2, 2e] meets every long
zero-sum (Y - Z would be (ZP_kappa') of length exactly p + 2kappa' + 1 with a long zero-sum); and if 4kappa <= 3p + 2, the
complement of every long zero-sum is zero-sum-free (its length is <= 2kappa - p - 1 <= 2e + 1).

## 4. What remains for LS+ (exact)
Under H(kappa): a sequence Y of length 3kappa + 2 with (ZP_kappa), a long zero-sum, a 2kappa-zero-sum in every subsequence of
length >= 3kappa - 1 that contains a long zero-sum, no short zero-sum (length <= 2e) disjoint from a long zero-sum, and (if
5kappa <= 4p + 1) zero-sum-free complements of long zero-sums.  The extremal sequences E2, E3 have no zero-sum of length
<= 2e at all (their shortest zero-sum has length 2p - 2 floor(2p/3) > 2e), so SHIFT is silent near the extremum; a proof
of LS+ must exclude the one-term extensions of E2/E3-like structures by another argument.
