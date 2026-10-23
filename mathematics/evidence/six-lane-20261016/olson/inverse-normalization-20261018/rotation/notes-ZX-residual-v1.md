# The residual of the ZX route inside 3k <= 2p + 1: exact obstruction, two small lemmas, and what is missing (notes, v1)

Owner OlsonRotationRigidity.  Written after host clock 2026-10-18T12:26:59-07:00.  Status [W], UNREVIEWED notes.
This file changes no file.  It reads proof-ROT-ZX-v1.md (ad2460b2...815b) and proof-ROT-ZX-addendum-S1c-v1.md
(7ce7102c...b0b6) through the parent overlay in R/olson-zx-s1c-parent-verdict-v1.md (2f8d376b...e6af).  It contains:
- Corollary TII and Lemma RED, both with proofs;
- the structure that any failure of (S1) must have in the residual range, with proofs;
- the one ingredient this route lacks.
No new ROT, INV* or ordered-Olson coverage is claimed here.  No novelty claim.  "Not covered" means not covered by this
route; no failure is claimed anywhere.

Notation is that of the ZX files.  All kappa are integers.  For odd y = (1, x) in Z_2 x Z_p, "x-sum" is the sum of
the second coordinates.  A "half-sum" is a subsequence of odd length with x-sum 0, i.e. with group sum (1, 0).
delta := 2kappa - p.

## 1. Where the residual is

The terminal criterion (verdict item 3) covers 3k <= 2p + 1 with (S1) at kappa^, in particular kappa^ <= (p + 1)/2.

Inside 3k <= 2p + 1, a normal form fails the criterion only if all of the following hold:
- kappa^ >= (p + 3)/2;
- its rotation sequence violates (S1);
- since kappa^ <= k - 1 <= (2p - 2)/3, also 6kappa^ <= 4p - 4 and 3 <= delta <= (p - 4)/3, so p >= 13.
Terminal pairs (k, kappa^) for p <= 23:
- p = 13: (9, 8).
- p = 17: (11, 10).
- p = 19: (12, 11), (13, 11), (13, 12).
- p = 23: (14, 13), (15, 13), (15, 14).
In general k - 1 - kappa^ <= (p - 13)/6, so these pairs lie close to the Davenport-tight line kappa^ = k - 1.  For
p <= 17 they lie exactly on it.
Uniform shadow: a word with 3o <= 2p + 1 is outside the accepted uniform class exactly when o > (p + 3)/2 and
F < o + p - 3.  Even then it is covered if SOME admissible normal form meets the terminal criterion (overlay 2).

## 2. Corollary TII (Davenport-tight sequences under (S1))

**Corollary TII.**  Under (G') with kappa = k - 1, let Y (|Y| = 2p + k - 2) satisfy (S1).  Then Y = g^(2p-1) (-g)^(k-1)
for the generator g of Lemma ZX.
Proof.  Let r := #(g in Z), T := the negative part of Z, and sigma := the sum of beta over T.  Lemma ZX gives
cost_g(Y) <= e = k - 1 - 2kappa + |Z| = |Z| - kappa.  By Steps E and G of proof-ROT-ZX-v1.md, cost_g(Y) = e' + r >= r
and sigma = r.  Every beta >= 1, so |T| <= r, and |Z| = r + |T| <= 2r.  Hence:
- |Z|/2 <= r <= cost_g(Y) <= |Z| - kappa, so |Z| >= 2kappa;
- with (S1), |Z| = 2kappa, so r = |T| = kappa, every beta = 1, and e' = 0.
So Z = g^kappa (-g)^kappa and Y - Z = g^L with L = 2p - k, i.e. Y = g^(2p-1) (-g)^kappa.  []
Remark.  At the residual pairs with kappa^ = k - 1 (all residual pairs for p <= 17), any rotation sequence that
satisfies (S1) is therefore type II.  The finite aid of Sec. 5 found no other (ZP) sequence at (13, 9, 8).

## 3. Lemma RED (removing a short zero-sum lowers kappa)

**Lemma RED.**  Let Y satisfy (ZP) at kappa, and let V <= Y be a zero-sum with |V| = 2j, where 1 <= j <= p - kappa - 1.
Then Y - V satisfies (ZP) at kappa - j.
Proof.  Let W <= Y - V be a zero-sum with |W| in [2(kappa - j) + 2, 2p].
- If |W| <= 2p - 2j, then W V is a zero-sum of Y of length |W| + 2j in [2kappa + 2, 2p], contrary to (ZP).
- Otherwise |W| >= 2p - 2j + 1 >= 2kappa + 2, because j <= p - kappa - 1.  So W itself has length in [2kappa + 2, 2p],
  contrary to (ZP).  []

Use and limit.
- Suppose (S1) fails at kappa through a long zero-sum T, and Y has a zero-sum V of length 2j, disjoint from T, with
  kappa - (p + 1)/2 <= j <= p - kappa - 1.  Then Y - V satisfies (ZP) at kappa - j <= (p + 1)/2, so it satisfies (S1)
  by Corollary S1+.  But it contains T, of length >= 2kappa + 2 > 2(kappa - j): a contradiction.
- The window for j is nonempty whenever kappa <= (3p - 1)/4, which includes the residual range.
- The limit: a shortest long zero-sum T has no proper zero-sub-sum shorter than N - 2kappa (Sec. 4).  So every such V
  must meet Y - T, which has at most 2kappa - k - 2 <= k - 4 terms.  RED applies only when such a V exists, and its
  existence is not proved here.

## 4. Structure of any failure of (S1) in the residual range

Let p >= 13 and (p + 3)/2 <= kappa <= (2p - 2)/3, so 3 <= delta <= (p - 4)/3.  Let Y satisfy (ZP) and violate (S1).
Let T be a zero-sum of Y with |T| >= 2kappa + 2 and |T| least, and N := |T|.

(R1) N lies in [2p + 2, 4kappa] = [2p + 2, 2p + 2delta].  T has a nonempty proper zero-sub-sum.  Every nonempty proper
zero-sub-sum T' of T is a MINIMAL zero-sum with N - 2kappa <= |T'| <= 2kappa.
Proof.
- N >= 2p + 2 by (ZP).  By (D), T minus a term contains a nonempty zero-sum.
- T' and T - T' are shorter than T, so both have length <= 2kappa.  Hence N - 2kappa <= |T'| <= 2kappa, and N <= 4kappa.
- If T' were not minimal, it would contain two disjoint nonempty zero-sums.  Both are proper zero-sub-sums of T, so
  each has length >= N - 2kappa, giving 2(N - 2kappa) <= |T'| <= 2kappa, i.e. N <= 3kappa.  But
  N >= 2p + 2 > 3kappa, since 3kappa <= 2p - 2.  []

(R2) EGZ in Z_p gives a half-sum T_1 <= T with |T_1| = p.  Put M := T - T_1, with mu := |M| = N - p >= p + 2.  Then:
 (a) every nonempty x-zero-sum V of M with V != M is either odd with |V| <= delta, or even with |V| >= mu - delta;
 (b) M contains no two disjoint odd ones;
 (c) M = C V with C odd (|C| <= delta, a half-sum) and V even (|V| >= mu - delta), where V has no nonempty proper
     x-zero-sub-sum.  So V is a minimal zero-sum sequence over Z_p, of length beta in [mu - delta, p], and
     beta >= p + 2 - delta >= (2p + 10)/3.
Proof.
- (a) An even V is a proper zero-sub-sum of T, so by (R1) |V| >= N - 2kappa = mu - delta.  For an odd V, T_1 V is a
  proper zero-sub-sum of T (V != M) of length p + |V|, so p + |V| <= 2kappa, i.e. |V| <= delta.
- (b) Two disjoint odd ones would form an even zero-sum of length <= 2delta.  It is proper and nonempty, so
  2delta >= N - 2kappa >= p + 2 - delta.  This contradicts 3delta <= p - 4.
- (c) Davenport in Z_p gives an x-zero-sum V_0 <= M with 1 <= |V_0| <= p < mu.  If V_0 is odd, put C := V_0; otherwise
  C := M - V_0, which is odd and proper, so |C| <= delta.  Put V := M - C.
  - V is an even x-zero-sum, i.e. a nonempty proper zero-sub-sum of T, hence a minimal zero-sum by (R1).  So V has no
    nonempty proper even x-zero-sub-sum.
  - A proper odd x-zero-sub-sum V'' of V would make V'' and V - V'' two odd x-zero-sums of M, each of size <= delta,
    giving |V| <= 2delta < mu - delta.
  - So V has no nonempty proper x-zero-sub-sum, and by Davenport in Z_p, beta <= p.  []

## 5. What this route lacks, and finite aid

Missing ingredient.  To exclude (R2), it would suffice to know the shape of minimal zero-sum sequences V over Z_p of
length beta >= (2p + 10)/3: the index-1 form (a_1 h) ... (a_beta h) with sum a_i = p, Savchev-Chen type.
- This is not among the accepted imports.
- Lemma MULT is the analogous statement for zero-sum-free sequences of odd elements of Z_(2p), but only from length
  (4p - 1)/3 on.  The natural lift (V - v) (1, 0) of such a V is zero-sum-free in Z_(2p) but has length beta <= p, so
  MULT does not apply.
- The earlier slice notes notes-SC-lengthp-v2.md (with addenda) attempted a related Savchev-Chen statement in Z_(2p)
  and left its large-s case open.
Two limits are known:
- The parent's negative control g^13 (5g)^3 at p = 7, kappa = 5 (R/olson-zx-s1c-parent-verdict-v1.md) satisfies (ZP)
  and violates (S1).  That kappa is (p + 3)/2 with 6kappa = 4p + 2, outside the residual range 6kappa <= 4p - 4.  So
  (R1)-(R2) must use kappa <= (2p - 2)/3 (they do: 3kappa <= 2p - 2 and 3delta <= p - 4).
- Inside the range it is not known whether (S1) can fail.

Finite aid, not a premise: zx-check-v1 run1 (in progress at this writing).
- At (13, 9, 8), the only residual item with p <= 13, every (ZP) multiset satisfied (S1) and Steps A-G.  There was
  exactly 1 multiset up to units, type II.
- (17, 11, 10) is the last item of the run and may end UNKNOWN under the self-budget.
- The run disclosed a ulimit deviation (zx-check-v1/DEVIATION-v1.md).

Outside 3k <= 2p + 1 (terminal): not covered by this route.  Proof-ROT-ZX-v1.md Remark (3) lists where 3k <= 2p + 1
enters.
