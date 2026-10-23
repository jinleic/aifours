# Addendum to proof-ROT-ZX-v1.md: Lemma S1 (e) - (ZP) implies (S1) at kappa = (p+5)/2 for p >= 19; extended ranges, v1

Owner OlsonRotationRigidity.  Written after host clock 2026-10-18T12:55:10-07:00.  Status [W], UNREVIEWED.

This addendum changes no file.
- It adds one sequence lemma, Lemma S1 (e), with a self-contained proof given its imports.  The proof follows the
  pattern of Lemma S1 (d) (proof-ROT-ZX-addendum-S1d-v1.md, aefcfc58...c61b, under review).
- It states the consequences through the parent-accepted terminal criterion of R/olson-zx-s1c-parent-verdict-v1.md
  (2f8d376b...e6af) item 3, read through that verdict's overlay.
- Combined with S1+ (accepted) and S1 (d) (under review), it gives: (ZP) implies (S1) for every integer
  kappa <= (p + 5)/2 when p >= 19.  The consequence statements in Sec. 2 depend on S1 (d) being accepted.
No novelty claim.  Not ROT(p), INV*(p) or ordered Olson in general.

Imports (as in the S1 (d) addendum):
- (D);
- the Erdos-Ginzburg-Ziv theorem for Z_p;
- Davenport for Z_p (proved inline in proof-ROT-ZX-addendum-S1c-v1.md, 7ce7102c...b0b6);
- the EXPLICIT classical Savchev-Chen / Yuan index theorem, with the sources listed in the S1 (d) addendum.  It is used
  once, in Step (6), on a minimal zero-sum sequence over C_p of length p - 1 or p - 3.  Both are >= floor(p/2) + 2 for
  p >= 9.
Notation as in the S1 (d) addendum:
- x(y) is the second coordinate of an odd y = (1, x).  For a subsequence U, x(U) is the sum of the x(y) over U.
- A half-sum is an odd-length U with x(U) = 0.  Two disjoint half-sums form a zero-sum.
- After Step (6), every x-value is written c h with c in [0, p - 1], the "coefficient".

## 1. Lemma S1 (e)

**Lemma S1 (e).**  Let p >= 19 be prime and kappa = (p + 5)/2, so 2kappa = p + 5.  Let Y be a sequence of odd elements
of Z_(2p) with
  (ZP) no zero-sum subsequence of length in [p + 7, 2p].
Then every zero-sum subsequence of Y has length <= p + 5.

Proof.  Suppose not.  Let T be a zero-sum subsequence with |T| >= p + 7 and |T| least, and N := |T|.

(1) Lengths.
- N >= 2p + 2 by (ZP).  T has nonempty proper zero-sums by (D).
- For a nonempty proper zero-sum T' of T, both T' and T - T' are nonempty zero-sums shorter than T.  By minimality and
  parity, each has length <= p + 5.
- Hence every nonempty proper zero-sum of T has length in [N - p - 5, p + 5], and N <= 2p + 10.

(2) Half-sums.  EGZ gives a half-sum T_1 <= T with |T_1| = p.  Put M := T - T_1, so mu := |M| = N - p >= p + 2, and M
is a half-sum.
- Claim A.  Let V <= M with x(V) = 0 and 1 <= |V| <= p.
  - If |V| is even, V is a proper zero-sum of T, so |V| >= N - p - 5.
  - If |V| is odd, T_1 V is a proper zero-sum of length p + |V|, so |V| <= 5.
- Claim B.  M has no two disjoint odd V's as in Claim A.
  - Otherwise their union is a nonempty proper zero-sum of length <= 10.
  - By (1) its length would be >= N - p - 5 >= p - 3 >= 16.

(3) N is 2p + 2 or 2p + 4.  Suppose N >= 2p + 6.
- Then even V's in Claim A would need length >= p + 1 > p.
- So Davenport (on p terms of M) gives an odd V_1.  M - V_1 has >= p + 1 terms, so Davenport gives an odd V_2
  disjoint from V_1, contrary to Claim B.
Put l := N - p - 5, so l is p - 3 or p - 1.  Every nonempty proper zero-sum of T has length >= l.

(4) T has no term (1, 0).  Suppose u = (1, 0) is a term.
- Take T_1 by EGZ avoiding u.  Then u lies in M.  M - {u} has >= p + 1 terms, so Davenport gives V <= M - {u} with
  x(V) = 0 and 1 <= |V| <= p.
- If |V| is odd, then {u} and V contradict Claim B.
- If |V| is even, then |V| >= l.  The rest M - {u} - V has x-sum 0 and an even number of terms: at least 1 (since
  mu - 1 > p >= |V|), so at least 2, and at most mu - 1 - l = 4.  So it is a zero-sum shorter than l, contrary to (3).

(5) M = C V.  Here C is a half-sum with |C| in {3, 5}, and V is a zero-sum with no nonempty proper subsequence of
x-sum 0.  So the x-values of V form a minimal zero-sum sequence over Z_p, and |V| <= p.
- Davenport gives V_0 <= M with x(V_0) = 0 and 1 <= |V_0| <= p.
  - If |V_0| is odd, put C := V_0; then |C| <= 5 by Claim A.
  - If |V_0| is even, put C := M - V_0, which is odd, proper and nonempty, with |C| <= mu - l = 5.
  - In both cases |C| != 1 by (4).  Put V := M - C.
- An even nonempty proper V'' <= V with x(V'') = 0 would make V'' and V - V'' two zero-sums of length >= l.  Then
  |V| >= 2l >= 2p - 6 > p + 4 >= mu, which is impossible.
- An odd one would make V'' and V - V'' two odd V's as in Claim A, with |V| <= 10 < l, also impossible.
- Sizes:
  - N = 2p + 2 (mu = p + 2): |V| = p - 1 with |C| = 3, or |V| = p - 3 with |C| = 5.
  - N = 2p + 4 (mu = p + 4): |C| = 5, so |V| = p - 1, since |V| = p + 1 > p is impossible.

(6) Index 1.  By the Savchev-Chen / Yuan theorem, there are h in Z_p \ {0} and positive integers summing to p that are
the coefficients of V with respect to h.  Put h^ := (1, h).  So V is one of:
- |V| = p - 1: V = h^^(p-2) y_2;
- |V| = p - 3: V = h^^(p-4) y_4, or V = h^^(p-5) z_3 y_2, or V = h^^(p-6) y_2^3.
Here a subscript is the coefficient of the term.  Let t be the multiplicity of h^ in T; then t >= p - 6.  V contains a
term y of even coefficient e: e = 4 for h^^(p-4) y_4, and e = 2 otherwise.

(7) Classification.  Let z != h^ be a term of T with coefficient c.  By (4), c != 0; and c != 1.
- (7a) c even, c >= 6.  Then h^^(p-c) z (p - c <= p - 6 <= t) has x-sum 0 and even length p - c + 1 <= p - 5 < l, a
  contradiction.  So even c is 2 or 4.
  - If N = 2p + 4, then t >= p - 2 and h^^(p-4) z with c = 4 has length p - 3 < l = p - 1.  So there c = 2.
- (7b) e = 2, c odd, 5 <= c <= p - 2.  Put j := p - 2 - c, so 0 <= j <= p - 7 <= t, and z != y.  Then h^^j y z has
  x-sum 0 and even length p - c <= p - 5 < l, a contradiction.
  - For N = 2p + 4 and c = 3: h^^(p-5) y z has length p - 3 < l = p - 1, also a contradiction.
  - So when e = 2, odd c = 3 only, and only if N = 2p + 2.
- (7c) e = 4 (then N = 2p + 2, |C| = 5, V = h^^(p-4) y_4, t >= p - 4).
  - For odd c with 3 <= c <= p - 4: j := p - 4 - c, so 0 <= j <= p - 7 <= t.  Then h^^j y_4 z has x-sum 0 and even
    length p - 2 - c <= p - 5 < l = p - 3, a contradiction.
  - So odd c = p - 2 only.  Call such a term q.
  - If q is not in C, then h^^2 q (x-sum p, size 3) is a half-sum disjoint from C (its h^'s lie in V).  Then h^^2 q C
    is a zero-sum of length 8 < l, a contradiction.  So q lies in C.
  - Two such q's give h^^4 q q', with x-sum 2p and length 6 < l.  So there is at most one q.

(8) Counting.  Let u_2, u_3, u_4 be the numbers of terms with coefficients 2, 3, 4, and u_q in {0, 1} the number of
q-terms (only when e = 4).  By (7), these are all the terms other than h^.
- S-condition.  Let S be a sub-multiset of the coefficient-2, 3, 4 terms with an odd number of even-coefficient terms
  and sigma := (sum of coefficients over S) with 6 <= sigma <= p.  Then h^^(p - sigma) S (p - sigma <= p - 6 <= t)
  has x-sum 0 and even length p - sigma + |S|.  It is a nonempty proper zero-sum, so p - sigma + |S| >= l >= p - 3,
  i.e. sum over S of (c - 1) <= 3.
- Applying the S-condition, the following sets S are forbidden: {2,2,2,2,2}, {4,2,2}, {4,4,2}, {4,4,4}, {4,3},
  {2,3,3} and {2,2,2,3}.  Each has an odd number of even coefficients, 6 <= sigma <= 12, and sum (c - 1) >= 5.  Hence:
  - u_2 <= 4 and u_4 <= 2;
  - u_4 >= 1 forces u_2 <= 1 and u_3 = 0;
  - u_2 >= 1 forces u_3 <= 1;
  - with u_2 = 0, V = h^^(p-4) y_4, so (7c) gives u_3 = 0.
  So u_3 <= 1 in all cases.
- x-sum of T.  With t = N - u_2 - u_3 - u_4 - u_q:
  x(T) = (t + 2u_2 + 3u_3 + 4u_4 + (p - 2)u_q) h = (N + u_2 + 2u_3 + 3u_4 + (p - 3)u_q) h.
- Since N is 2p + 2 or 2p + 4, x(T) = 0 forces E := N' + u_2 + 2u_3 + 3u_4 - 3u_q = 0 (mod p), with N' = N - 2p in
  {2, 4}.
- By the bounds, -1 <= E <= 4 + 4 + 2 + 6 = 16 < p.  So E = 0, which needs u_q = 1 and N' + u_2 + 2u_3 + 3u_4 = 3.
  - That forces N' = 2, u_2 = 1 and u_3 = u_4 = 0.
  - But u_q = 1 occurs only for V = h^^(p-4) y_4, which has u_4 >= 1.
  A contradiction.  []

Where p >= 19 is used:
- Claim B needs 10 < p - 3, and Step (5) needs 2p - 6 > p + 4 and 10 < l.
- Step (7c) needs 8 < l, and Step (8) needs 16 < p.
- At p = 17, kappa = (p + 5)/2 = 11 exceeds (2p - 2)/3, so it does not occur as a terminal kappa^ with 3k <= 2p + 1.

**Corollary S1+++.**  For every prime p >= 19 and every integer kappa with 0 <= kappa <= (p + 5)/2, (ZP) implies (S1).
This combines S1+ (kappa <= (p + 1)/2, accepted), S1 (d) (kappa = (p + 3)/2, p >= 11, under review) and S1 (e).

## 2. Consequences (conditional on acceptance of S1 (d) and S1 (e))

Through the accepted terminal criterion, as in the S1 (d) addendum, for p >= 19:
- ROT-ZX+++ (terminal): some normal form has k = 1, or has 3k <= 2p + 1 and kappa^ <= (p + 5)/2.  Then all rotations
  lie in one nonzero pair, and INV* holds if moreover o_F(w) <= p.
- INV*-ZX+++ (uniform, length 4p - 2): 3o <= 2p + 1, and o <= (p + 7)/2 or F >= o + p - 7.
- OLSON-ZX+++ (uniform, length 4p - 1): the same condition, with F - o >= p - 7.  The deletion ledger is as before.

|p|unconditional o_F bound (with 3 o_F <= 2p + 1)|with an F condition|
|---:|---|---|
|19|o_F <= 13, i.e. every o_F with 3 o_F <= 2p + 1|-|
|23|o_F <= 15, i.e. every o_F with 3 o_F <= 2p + 1|-|
|29|o_F <= 18|o_F = 19 with F >= 41|
|31|o_F <= 19|o_F in {20, 21} with F >= o_F + 24|

Together with the S1 (d) addendum (p = 13, 17) and the accepted S1 (c) consequences (p = 7, 11):
- For every prime p with 7 <= p <= 23, every avoider of length 4p - 2 with 3 o_F <= 2p + 1 satisfies INV*.
- Every word of length 4p - 1 with 3 o_F <= 2p + 1 has an identity 2p-subword in increasing index order.
- p = 5 stays at the accepted o_F <= 4.

Not covered by this route, inside 3k <= 2p + 1 (terminal): kappa^ >= (p + 7)/2.  This needs p >= 29.
- Terminal pairs (k, kappa^): p = 29: (19, 18).  p = 31: (20, 19), (21, 19), (21, 20).
- Nothing is claimed to fail.
