# Lemma S1-sharp: (ZP) implies (S1) for every kappa <= floor(2p/3); uniform INV* and ordered Olson under 3 o_F <= 2p+1, v1

Owner ContinueOlson (math-2 lane, 96-hour continuation).  Written after /bin/date 2026-10-19T00:11:26-0700.  Status: CANDIDATE, written
proof [W], UNREVIEWED.  No computation is a premise.  No novelty or priority claim; no Lean.  This is NOT unrestricted
INV*(p), not ordered Olson for D_2p in general, and not the all-groups target.

## 0. Statements

Notation.  p is a prime, p >= 5.  Z_2p is additive; its odd elements are the elements (1, x) of C_2 x C_p.  A zero-sum
subsequence has sum 0; zero-sums of odd elements have even length.  For an integer kappa >= 0:
  (ZP_kappa)  Y has no zero-sum subsequence whose length lies in [2kappa + 2, 2p];
  (S1_kappa)  every zero-sum subsequence of Y has length <= 2kappa.

**Lemma S1-sharp.**  Let p >= 5 be prime and kappa an integer with 0 <= kappa <= floor(2p/3).  Every sequence Y of odd
elements of Z_2p satisfying (ZP_kappa) satisfies (S1_kappa).

Equivalently, with delta := 2kappa - p (odd): the conclusion holds for kappa <= (p+1)/2 (accepted S1+), and for every odd
delta >= 3 with p >= 3delta - 1 (note 3kappa <= 2p <=> p >= 3delta - 1 because 6kappa is even).

**Sharpness (two families; arithmetic remark, not used below).**  For kappa = floor(2p/3) + 1 the implication fails.
(F1) parent-checked family g^(p+3) (3g)^(p-1) (R/olson-s1g-parent-verdict-v1.md, sharpness remark, p = 7, 11, 13, 17,
19, 31); (F2) for p = 1 (mod 3), g^(2p-1) (c g)^3 with c = (2p+1)/3 (found by the lane probe, see Sec. 4; for F2 the
only zero-sums are g^(2p-c) (cg) (length 2p-c+1 = (4p+2)/3), g^(2p-2c)(cg)^2 (length 2p-2c+2 = (2p+4)/3) and the whole
sequence (length 2p+2), so (ZP) holds exactly for kappa >= (2p+1)/3 and (S1) fails there).  Sec. 3 locates the exact step
of the proof that each family breaks.

**Corollary S1-sharp-INV/OLSON.**  For every prime p >= 5:
- (a) every avoider of length 4p-2 over D_2p with 3 o_F <= 2p + 1 satisfies INV* (it lies in RGR_(4p-2)(p));
- (b) every word of length 4p-1 over D_2p with 3 o_F <= 2p + 1 has an identity 2p-subword in increasing index order.
Here o_F is the number of odd maximal cyclic constant reflection blocks, as in the accepted ZX and S1(g) verdicts.

## 1. Imports (accepted scopes only)

- S1+ : (ZP_kappa) => (S1_kappa) for every integer 0 <= kappa <= (p+1)/2, every prime p >= 5 (accepted; listed in
  R/olson-s1g-parent-verdict-v1.md, statement 2, sha256 cc9e27fbabdd14e8cc35e9d6d1477ea1ca90742a985629d8a362c89505b3605e).
- Index-one theorem (Savchev-Chen / Yuan), exactly as recorded in R/olson-index-one-primary-statement-parent-v1.md
  (e461514461d23287beeecf04fa26334efd91d3de51caa33312f6c5b10b4d35c6): every minimal zero-sum sequence over C_n, n >= 3,
  of length >= floor(n/2) + 2 has a 1-element basis {a}: every term is x(t) a with a positive least coefficient and
  sum_t x(t) = ord(a).  Used once, with n = 2p, on a sequence of length p + delta >= p + 3.
- For the Corollary only: the accepted ZX terminal criterion (R/olson-zx-s1c-parent-verdict-v1.md, 2f8d376b...e6af,
  and proof-ROT-ZX-v1.md L204-206): rotations of an avoider lie in one nonzero pair whenever some admissible normal form
  has 3k <= 2p+1 and its rotation sequence satisfies (S1) at kappa^; the normal form facts k <= o_F, k = o_F (mod 2),
  0 <= kappa^ <= k-1 (DAV) for k >= 2, K1 for k = 1; restricted REFL (o_F <= p); the ordered deletion ledger; RGR-LONG
  (R/olson-runs-parent-verdict-v1.md) -- all exactly as used by the S1(g) verdict's consequence derivation.
No other input.  In particular Steps 3-8 of S1(g) are NOT used.

## 2. Proof of Lemma S1-sharp

Induction on kappa for fixed p.  For kappa <= (p+1)/2 use S1+.  Let (p+3)/2 <= kappa <= floor(2p/3), so delta := 2kappa - p
is odd with 3 <= delta and p >= 3delta - 1, and assume the Lemma at kappa - 1.  Put u := 2kappa = p + delta.  Suppose Y
satisfies (ZP_kappa) but not (S1_kappa).

Step 1 (shortest long zero-sum).  Let T be a zero-sum subsequence of Y with |T| >= u + 2 and |T| = N least.  By
(ZP_kappa), N >= 2p + 2.  If T' is a nonempty proper zero-sum subsequence of T, then |T'| <= u (a proper one of length
>= u + 2 would, by (ZP_kappa), have length >= 2p + 2 and contradict the minimality of N), and T - T' is also a nonempty
proper zero-sum, so |T'| >= l := N - u.  Put D := u - l = 2u - N.  Then D is even, and D <= 2u - 2p - 2 = 2delta - 2.
Also l >= 2p + 2 - u = p - delta + 2.

Step 2 (all proper zero-sums are minimal).  If a nonempty proper zero-sum T' of T contained a nonempty proper zero-sum
T'', then T'' and T' - T'' would be nonempty proper zero-sums of T, so 2l <= |T'| <= u, i.e. N <= 3u/2 = 3kappa.  But
3kappa <= 2p < 2p + 2 <= N.  So every nonempty proper zero-sum of T is a minimal zero-sum sequence.

Step 3 (a proper zero-sum of length exactly u).  If every nonempty proper zero-sum of T had length <= u - 2 = 2(kappa-1),
then the sequence T itself would satisfy (ZP_(kappa-1)) (its proper zero-sums are shorter than 2(kappa-1)+2 = u, and
N > 2p) while T is a zero-sum of length N > 2(kappa-1): this contradicts the Lemma at kappa - 1.  So T has a proper
zero-sum Q with |Q| = u; Q' := T - Q is a proper zero-sum with |Q'| = l.  Both are minimal (Step 2).

Step 4 (index one).  |Q| = p + delta >= p + 3 >= floor(2p/2) + 2, so the index-one theorem gives a in Z_2p with every
term of Q equal to x a, x a positive least coefficient, and the coefficients summing to ord(a).  The terms are odd, so
ord(a) is not p (multiples of an element of order p are even) and not 2 (then every term equals p and |Q| = 2); hence a
=: g is an odd generator, every coefficient lies in [1, 2p-1], is odd (x g is odd iff x is odd), and the coefficients of
Q sum to exactly 2p.  From now on every term of T is written c g with c its least positive coefficient, an odd integer
in [1, 2p-1]; for a sub-multiset W write A_W for the sum of the coefficients (an integer) and mass(W) := A_W - |W|.
Write Q = g^m S_Q, where S_Q collects the terms of Q with coefficient >= 3.  mass(S_Q) = 2p - u = p - delta.  Every
coefficient of S_Q is odd and >= 3, so |S_Q| <= (p - delta)/2 and m >= u - (p - delta)/2 = (p + 3delta)/2.  S_Q is
nonempty (otherwise the coefficients of Q would sum to u != 2p).  Let b_min := min S_Q; then b_min - 1 <= mass(S_Q),
i.e. b_min <= p - delta + 1.  Also every element b of S_Q satisfies b <= 2p - m - 3(|S_Q| - 1) = p - delta - 2|S_Q| + 3
(the other terms of Q have coefficients >= 1 and >= 3 respectively).

Step 5 (main constraint MC).  Let W be a sub-multiset of Q' and Q_1 a sub-multiset of Q with sum of coefficients of Q_1
congruent to A_W modulo 2p, excluding (Q_1, W) = (Q, empty) and (empty, Q').  Then (Q - Q_1) W is a nonempty proper
zero-sum of T (its sum is (2p - (sum of Q_1) + A_W) g = 0), of length u - |Q_1| + |W|.  By Step 1:
    (MC)   |W| <= |Q_1| <= |W| + D.
Write Q' = g^t' Y, where Y collects the terms of Q' with coefficient >= 3 (t' >= 0 copies of g).

Step 6 (no large coefficient in Q').  Every term z of Q' has coefficient c <= D + 1.
Proof.  Suppose c >= D + 2.  Take W = {z} (proper: |Q'| = l >= 2).  We exhibit Q_1 <= Q with coefficient sum c and
|Q_1| >= D + 2, contradicting (MC).  If c <= m, take Q_1 = g^c.  If c > m (note m >= (p+3delta)/2 >= D + 2), let Z_0 be
an inclusion-minimal sub-multiset of S_Q with A_(Z_0) >= c - m (it exists: A_(S_Q) = 2p - m >= c - m), and b_0 := min Z_0.
Minimality gives A_(Z_0) < c - m + b_0, and b_0 <= p - delta - 2|S_Q| + 3 <= p + delta - |S_Q| = m, so A_(Z_0) < c;
hence Q_1 := Z_0 g^(c - A_(Z_0)) is a sub-multiset of Q with coefficient sum c and |Q_1| = c - mass(Z_0).  If
|Q_1| <= D + 1, then mass(Z_0) >= c - D - 1, and mass(Z_0) = A_(Z_0) - |Z_0| < c - m + b_0 - |Z_0| gives
b_0 > m - D - 1 + |Z_0|.
- |Z_0| = 1: b_0 >= m - D + 1 = p + delta - |S_Q| - D + 1 >= p - delta - |S_Q| + 3 (as D <= 2delta - 2), while
  b_0 <= p - delta - 2|S_Q| + 3; so |S_Q| <= 0, impossible.
- |Z_0| >= 2: every element of Z_0 is >= b_0 >= m - D + 2, so mass(Z_0) >= 2(m - D + 1); as mass(Z_0) <= p - delta,
  m <= (p - delta)/2 + D - 1 <= (p + 3delta)/2 - 3 < m, impossible.
So |Q_1| >= D + 2.  []

Step 7 (index of Q' is one).  A_(Q') = 2p.
Proof.  A_(Q') is a positive multiple of 2p.  Suppose A_(Q') >= 4p.  Order Q' arbitrarily and let W be the shortest
prefix with A_W >= 2p.  By Step 6 its last term has coefficient <= D + 1, so r := A_W - 2p lies in [0, D], and W is proper
(A_W < 2p + D + 1 <= 4p).  r != 0, since Q' is minimal.  Q_1 := g^r (r <= D < m) has coefficient sum r = A_W mod 2p, so
(MC) gives |W| <= r, i.e. mass(W) = A_W - |W| >= 2p.  Let W^- be W without its last term, s := 2p - A_(W^-), so
1 <= s <= D + 1 <= m.  Q_1 := Q - g^s has coefficient sum 2p - s = A_(W^-), and (MC) gives |Q_1| <= |W^-| + D, i.e.
u - s <= |W^-| + D, i.e. |W^-| >= l - s.  Hence mass(W^-) = (2p - s) - |W^-| <= 2p - l, and mass(W) <= 2p - l + D (the
last term adds at most D).  So 2p <= 2p - l + D, i.e. l <= D, i.e. u <= 2D <= 4delta - 4, i.e. p <= 3delta - 4,
contrary to p >= 3delta - 1.  []

Step 8 (the coefficient b_min is not a sum of >= 2 terms of Q').  No sub-multiset W of Q' with |W| >= 2 has
A_W = b_min.  Indeed Q_1 := {b_min} has coefficient sum b_min, and (MC) gives |W| <= 1.  Consequences:
- (8a) t' < b_min (else W = g^(b_min) is such a sub-multiset, b_min >= 3).
- (8b) No nonempty sub-multiset Z of Y has A_Z in [b_min - t', b_min - 1] (else W = Z g^(b_min - A_Z), which uses
  between 1 and t' copies of g, is such a sub-multiset).
- (8c) Let Y_low be the terms of Y with coefficient <= t'.  Then A_(Y_low) <= b_min - t' - 1: otherwise, adding the
  terms of Y_low in any order, the first partial sum >= b_min - t' (>= 1 by (8a)) is at most (b_min - t' - 1) + t' and
  so lies in [b_min - t', b_min - 1], contradicting (8b).  As every coefficient of Y is >= 3,
  |Y_low| <= (b_min - t' - 1)/3.

Step 9 (counting).  By Step 7, A_Y = 2p - t' and |Y| = l - t'.  Put base := (3l - 2p)/2 (an integer, l even).  Then
    X := sum over Y of (c - 3)/2 = (A_Y - 3|Y|)/2 = t' - base.
Since D <= 2delta - 2 and l = u - D, base = (p + 3delta - 3D)/2 >= (p - 3delta + 6)/2 >= 5/2, so base >= 3.  Each term of
Y with coefficient >= t' + 1 contributes (c - 3)/2 >= (t' - 2)/2 to X, and every term contributes >= 0; two such terms
would give X >= t' - 2 > t' - base.  So at most one term of Y has coefficient > t', and
    l - t' = |Y| <= |Y_low| + 1 <= (b_min - t' - 1)/3 + 1.
Hence 3l <= b_min + 2t' + 2 <= b_min + 2(b_min - 1) + 2 = 3 b_min (by (8a)), i.e. l <= b_min.  But l >= p - delta + 2 >
p - delta + 1 >= b_min (Steps 1 and 4).  Contradiction.  This proves the Lemma at kappa, and by induction for every
kappa <= floor(2p/3).  []

## 3. Hypothesis map and where the sharp families break

- p >= 3delta - 1 (equivalently kappa <= floor(2p/3)) is used in Step 2 (3kappa <= 2p < N), Step 7 (p > 3delta - 4)
  and Step 9 (base >= 3, i.e. p >= 3delta - 1 since (p - 3delta + 6)/2 > 2 <=> p > 3delta - 2).
- delta >= 3 is used in Step 4 (length >= p + 2); delta = 1 is the accepted base S1+.
- The induction (Step 3) uses the Lemma at kappa - 1 only.
- At kappa = floor(2p/3) + 1 (outside the Lemma) both families satisfy every step up to Step 8 and fail Step 9 exactly:
  - (F1) g^(p+3)(3g)^(p-1), p = 1 (mod 3), kappa = (2p+1)/3: Q = g^(p+1)(3g)^((p-1)/3), Q' = g^2 (3g)^((2p-2)/3),
    t' = 2 < b_min = 3, Y_low empty, every term of Y exceeds t'; base = 2 and X = 0 = t' - base, so the 'at most one
    term above t'' step fails (it needs base >= 3).
  - (F2) g^(2p-1)(cg)^3, c = (2p+1)/3: Q = g^(2p-c)(cg) (length u = (4p+2)/3), Q' = g^(c-1)(cg)^2, t' = c - 1 < b_min =
    c, Y = (cg)^2, base = 2, X = c - 3 = t' - base; again exactly the base >= 3 step fails.
  For p = 2 (mod 3) the first excluded value kappa = (2p+2)/3 is the parent's F1 range; F2 needs p = 1 (mod 3).

## 4. Falsification controls and aids (not premises)

- Parent-checked F1 arithmetic (S1(g) verdict sharpness remark).
- Lane probe evidence/probe-v1 (RECEIPT-run1-v1.md 4351a750cd2f60fa4cd186962649d83cb67e2199c6ef9425fe8a929ee3393f8f;
  run1.jsonl 901a8000772bf6f0b2beec7521e9163ef1687d5e6d1f97622156287081abd253): inside a representation implied by Steps
  3-8 (Q index-one of length u, t' < min S_Q, Y in [3, D+1], A_(Q') = 2p), exact DP found F1 and F2 (and nothing else) at
  the POS controls p = 13, 19, 31, kappa = (2p+1)/3, and no survivor at 15 complete (p, delta) pairs beyond the S1(g)
  range including p = 31, kappa = 20.  Process deviation: PID recorded only by a later ps census.  Aid only.
- Requested independent controls (not yet run): an exact check of the Lemma's statement that does not presuppose Steps
  3-9 (e.g. exhaustive small-support T at p = 31, kappa = 20), and hostile reviews by both model families.

## 5. Proof of the Corollary (re-derivation of the accepted S1(g) consequence chain with the larger kappa range)

(a) Let w be an avoider of length 4p-2 with 3o_F <= 2p+1, o := o_F.  Every admissible normal form w^ has k <= o and
k = o (mod 2).  If k = 1, Proposition K1 gives the rotation conclusion.  If k >= 2, DAV gives 0 <= kappa^ <= k - 1 <=
o - 1 <= (2p+1)/3 - 1, so 3 kappa^ <= 2p - 2 <= 2p, and the rotation sequence of w^ satisfies (ZP) at kappa^ (GRX,
all-plus pattern); Lemma S1-sharp gives (S1) at kappa^, and 3k <= 3o <= 2p + 1, so the ZX terminal criterion puts all
rotation letters of w^ -- the rotation multiset of w -- into one nonzero pair.  Restricted REFL applies to w since
o <= (2p+1)/3 <= p.  So w is RGR.
(b) As in the accepted S1(g)/S1(d) consequence: for a word of length 4p-1 with 3o <= 2p+1, the ordered deletion ledger
(Case 1 uses o <= 2p - 3 and framed equal pairs; Case 2 gives (o-1, F-1); Case 3 gives (o or o-2, F)) keeps 3o <= 2p+1,
so each relevant deletion is an avoider covered by (a), and RGR-LONG completes.  The previous extra alternative
[o <= (p + delta* + 2)/2 or F >= o + p - delta* - 2] is no longer needed because Lemma S1-sharp covers every kappa^ that
can occur under 3k <= 2p+1.

Effect on the residual map (bundle-v5 Sec. 5): family (Q2) is empty for every prime p; in particular the p = 31 pair
(21, 20) is covered.  The rotation-half residual is now (Q1a) k = p, kappa^ >= 2 and (Q1b) (2p+1)/3 < k <= p-1,
kappa^ >= 2 with T4 failing; the reflection half for o_F > p is untouched.

## 6. Scope and limits

- Written proof only, relative to the imports of Sec. 1.  Unreviewed; requires independent parent derivation and both
  model-family hostile reviews before any acceptance.  Source access: the index-one theorem is imported from the
  parent's record (author statement read; 2007 proofs not read).  No literature search was made for Lemma S1-sharp; a
  search miss would not be novelty evidence.
- Not covered: k = p (Q1a); (2p+1)/3 < k <= p-1 with T4 failing (Q1b); reflection rigidity for o_F > p; non-dihedral
  groups.
