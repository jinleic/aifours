# Lemma ZS and Theorem ROT-HALF: ROT, INV* and ordered Olson for o_F <= (p+1)/2, v1

Owner OlsonRotationRigidity.  Written after host clock 2026-10-18T10:57:16-07:00.  Status [W], UNREVIEWED.
New here: Lemma ZS (Sec. 1-2), a statement about sequences in Z_(2p) with a complete in-file proof.  Sec. 3-4 combine
it with parent-accepted results exactly as the accepted ROT-FEW-E, INV*-FEW (b) and OLSON-FEW (b) do.  Lemma ZS
replaces Steps 1-4 of ROT-FEW (EXTRACT, MULT, WT) and removes the condition (F) 5k <= 2p + 4: the range grows from
(2p+4)/5 to (p+1)/2 odd blocks.  No novelty claim.  This is not ROT(p), INV*(p) or ordered Olson in general.
Paths: R = institute/runs/six-lane-2026-10-16/review/; files without a directory are in this rotation/ directory.
Imports, all parent-accepted at their stated scopes:
- (D) D(Z_(2p)) = 2p, GRX, PM*, Proposition K1: R/olson-rotation-lowodd-parent-verdict-v2.md (0853f4ac...ba29).
- Lemma MULT (i)-(iii): proof-ROT-few-v4.md (abd3973c...b521) L61-81, accepted with ROT-FEW
  (R/olson-fewodd-parent-verdict-v1-addendum-1.md L11); its proof uses SCHERK, GROW, SET and INC (a), (b) of that file.
- Normal form, Lemma DAV / (V) and (ZP) for the normal form: proof-ROT-few-E-v4.md (ac560eb8...ea8f) Sec. 0, L28-43.
  Lemma SHgen-E: same file Sec. 1, L45-71 (addendum-1 L12).
- Theorem SHgen with its setting, (ZP), (V) and weights: proof-SHgen-v3.md (fcbd5a97...eb5e) Sec. 0-1, L20-56
  (addendum-1 L10).
- Corollary REFL-few-odd: reflection/proof-REFL-fewodd-r4.md (1e447754...861d) L21-25 and its Sec. 4 interface
  (R/olson-refl-fewodd-parent-verdict-v1.md L6).
- For Sec. 4 only: RGR-LONG(p) (R/olson-runs-parent-verdict-v1.md L7); the proof of OLSON-FEW in
  proof-OLSON-few-v3.md L28-47; the deletion ledger of proof-FEW-p5-lift-v3.md Sec. 4.1, which does not depend on p
  (R/olson-p5-few-lift-parent-verdict-v1.md, c2d06e14...6d7b).
Notation (as in proof-ROT-few-v4.md L20-23).  Y(x) := (1, x) in Z_2 x Z_p = Z_(2p).  Elements with first coordinate 1
are "odd".  For an odd generator g every odd element is b g with b odd; b is unique mod 2p, and b(y) denotes the
representative in (-p, p].  A sequence is a multiset of terms; T <= Y means a subsequence (a sub-multiset of terms).
Zero-sums of odd elements have even length.

## 1. Lemma ZS

**Lemma ZS.**  Let p >= 5 be prime, let k, kappa be integers with 1 <= k <= (p+1)/2 and 0 <= kappa <= k - 1, and let Y be
a sequence of R = 2p + 2kappa - k odd elements of Z_(2p) such that
  (ZP) Y has no zero-sum subsequence of length in [2kappa + 2, 2p].
Then there is an odd generator g of Z_(2p) such that, with b = b(y) relative to g,
  cost(Y) := sum over y with b > 0 of (b - 1)  +  sum over y with b < 0 of |b|  <=  k - 1.
In particular every term has |b| <= k (so no term is (1,0) = p g), and with E := sum_y (|b| - 1) and N := the number of
terms with b < 0, E <= k - 1 - N.

## 2. Proof of Lemma ZS

Step 1 (every zero-sum is short).  Every zero-sum subsequence T of Y has |T| <= 2kappa.
A minimal zero-sum subsequence has length <= 2p (deleting one term leaves a zero-sum-free sequence, of length <= 2p - 1
by (D)), and its length is even, so by (ZP) it is <= 2kappa.  A zero-sum T is a product T_1 ... T_r of minimal zero-sum
subsequences (take one minimal zero-sum subsequence, then induct on the rest).  If |T| >= 2kappa + 2, let j be least
with |T_1| + ... + |T_j| >= 2kappa + 2.  Then T_1 ... T_j is a zero-sum of length at least 2kappa + 2 and at most
2kappa + 2kappa = 4kappa <= 4k - 4 <= 2p - 2, contrary to (ZP).  []

Step 2 (splitting).  Let Z be a zero-sum subsequence of Y of maximal length (Z may be empty), and Y' the complementary
subsequence.  Y' is zero-sum-free: a nonempty zero-sum V <= Y' would make Z V a longer zero-sum.  By Step 1
|Z| <= 2kappa, so L := |Y'| = R - |Z| >= 2p - k, and e := 2p - 1 - L = k - 1 - 2kappa + |Z| satisfies 0 <= e <= k - 1
(L <= 2p - 1 by (D)).

Step 3 (structure of Y').  Since 3e + 2 <= 3k - 1 <= 2p, Lemma MULT (iii), (ii) applies to Y'.  Let m be the largest
multiplicity in Y', attained by g.  Then g is a generator, and Y' = g^m (d_1 g) ... (d_q g) with odd d_j >= 3 and
e' := sum_j (d_j - 1) <= e.  MULT (i) gives m >= L - e >= 2p - 2k + 1.  Put W' := m + sum_j d_j = L + e'.
**Lemma COMP.**  (a) Every integer t in [0, W'] is the weight w(Q) := #(g in Q) + sum of the d_j of the terms d_j g in Q
of some subsequence Q <= Y'.  (b) W' <= 2p - 1.  (c) Every Q <= Y' has sum w(Q) g and |Q| = w(Q) - (sum of d_j - 1 over
its terms d_j g) >= w(Q) - e'.
Proof.  (a) Every d_j <= e' + 1 <= e + 1 <= m.  The weights of subsequences of g^m are all integers in [0, m].  If all
integers in [0, M] are weights and d <= M + 1, then after adding d g all integers in [0, M + d] are weights (t <= M,
or t - d in [0, M]).  Add d_1, ..., d_q in turn.  (b) If W' >= 2p, some Q has weight 2p by (a), so sum 2p g = 0: a
nonempty zero-sum in Y'.  (c) Clear.  []
Consequences: (C1) every d_j <= e' + 1 <= k <= p - 2 (as k <= (p+1)/2 and p >= 5), so each term of Y' is b g with
b in {1} u [3, k] and b = b(y); (C2) W' >= L >= 2p - k; (C3) e' <= e; (C4) m >= 2p - 2k + 1 >= k - 1, as 3k <= 2p + 2.

Step 4 (zero-sums through Z).  For U <= Z put s(U) := sum over y in U of b(y), an integer, and let tau(U) in
{0, 1, ..., 2p - 1} satisfy tau(U) = -s(U) (mod 2p).  If 1 <= tau(U) <= W', then every Q <= Y' with w(Q) = tau(U) has
|U| + |Q| <= 2kappa.  Hence |U| + tau(U) - e' <= 2kappa (COMP (a), (c)), and if tau(U) <= m also |U| + tau(U) <= 2kappa
(take Q = g^tau(U)).
Proof.  U and Q are disjoint parts of Y, and U Q has sum (s(U) + tau(U)) g = 0.  Apply Step 1.  []

Step 5 (every sub-sum of Z is small).  For every U <= Z, tau(U) lies in {0} u [1, k - 1] u [2p - k + 1, 2p - 1].
Equivalently, the representative of s(U) mod 2p in (-p, p] lies in [-(k-1), k - 1].
Proof.  Suppose k <= tau(U) <= 2p - k, and let U^c be the complement of U in Z.  Z is a zero-sum, so s(Z) g = 0, i.e.
s(Z) = 0 (mod 2p).  Hence tau(U^c) = 2p - tau(U), which also lies in [k, 2p - k].  Both values are <= 2p - k <= W' (C2),
so Step 4 applies twice: |U| + tau(U) - e' <= 2kappa and |U^c| + 2p - tau(U) - e' <= 2kappa.  Adding gives
|Z| + 2p - 2e' <= 4kappa.  With e' <= e = k - 1 - 2kappa + |Z| this becomes 2p - 2k + 2 <= |Z| <= 2kappa <= 2k - 2,
i.e. 4k >= 2p + 4, contrary to k <= (p+1)/2.  []

Step 6 (Z is balanced).  Every term of Z has |b| <= k - 1 (Step 5 with U a single term).  Let Z+ and Z- be the terms of Z
with b > 0 and b < 0, and sigma+ := sum over Z+ of b, sigma- := sum over Z- of |b| (integers).  Then
sigma+ <= k - 1, sigma- <= k - 1 and sigma+ = sigma- =: sigma.
Proof.  List Z+ as y_1, ..., y_r.  The integer partial sums S_j = b(y_1) + ... + b(y_j) increase by at most k - 1 per
step.  If sigma+ = S_r >= k, the least j with S_j >= k has k <= S_j <= 2k - 2 <= p - 1.  Then the representative of
s({y_1, ..., y_j}) is S_j >= k, contrary to Step 5.  The same argument gives sigma- <= k - 1.  Then
s(Z) = sigma+ - sigma- lies in [-(k-1), k - 1] and is 0 mod 2p, so sigma+ = sigma-.  []

Step 7 (room left in Y').  W' <= 2p - 1 - sigma.
Proof.  For sigma = 0 this is COMP (b).  Let sigma >= 1; then tau(Z+) = 2p - sigma lies in [2p - k + 1, 2p - 1].
Suppose 2p - sigma <= W'.  Step 4 gives |Z+| + 2p - sigma - e' <= 2kappa.  With e' <= k - 1 - 2kappa + |Z| this
becomes 2p + 1 <= sigma + k + |Z-|.  Since every |b| >= 1, |Z-| <= sigma- = sigma, so 2p + 1 <= 2sigma + k <= 3k - 2,
contrary to k <= (p+1)/2.  So W' < 2p - sigma.  []

Step 8 (negatives of Z).  |Z-| + sigma <= 2kappa.
Proof.  If sigma = 0, Z- is empty.  Otherwise tau(Z-) = sigma lies in [1, k - 1], and sigma <= k - 1 <= m (C4).  So
Step 4 with Q = g^sigma gives |Z-| + sigma <= 2kappa.  []

Step 9 (count).  By (C1) the terms of Y' contribute e' to cost(Y).  By Step 6 the terms of Z contribute
(sigma - |Z+|) + sigma.  Hence
  cost(Y) = (W' - L) + 2sigma - |Z+|
          <= (2p - 1 - sigma - L) + 2sigma - |Z+|        (Step 7)
          = e + sigma - |Z+|  =  k - 1 - 2kappa + |Z-| + sigma
          <= k - 1                                       (Step 8).
Every |b| is <= k: for Y' by (C1), for Z by Step 6.  Finally cost(Y) = sum_y (|b| - 1) + #{b < 0} = E + N.  []

Remarks.  (1) The bound is attained: kappa = k - 1 and Y = g^(2p-1) (-g)^kappa give Z = (g (-g))^kappa, Y' =
g^(2p-1-kappa), sigma = kappa and cost(Y) = k - 1 (E = 0, N = k - 1); kappa = 0 and Y = g^(2p-k) give cost 0.
(2) The new step is Step 5.  It uses the full length R through e, and the complementary pair U, U^c of the maximal
zero-sum Z.  Steps 6-9 then bound positive and negative weights together, so neither G >= 2kappa + w_+ (WT (b), (c))
nor (F) is needed.
(3) Limits of the method.  Step 1 needs 4kappa <= 2p, Step 5 needs 4k < 2p + 4, and Step 6 needs 2k - 2 <= p - 1.  All
three hold exactly when k <= (p+1)/2.  At k = p the conclusion is false.  Take kappa = p - 1 and
Y = g^(2p-1) (3g)^(p-1) (R = 3p - 2).  The only length in the (ZP) window is 2p, and g^a (3g)^b with a + b = 2p has
sum 2b g, which is 0 only for b in {0, p}; neither is available.  For any odd generator h, writing g = beta h, the
2p - 1 copies of g already cost at least 2p - 1 > p - 1 unless beta = 1, and for h = g the copies of 3g cost
2(p - 1) > p - 1.  So for k near p a proof must use GRX patterns with sign changes (Phi >= 2), not only (ZP).  For
(p+3)/2 <= k <= p - 1 neither a proof nor a counterexample of Lemma ZS is known here.

## 3. Theorem ROT-HALF

**Theorem ROT-HALF.**  Let p >= 5 be prime and w an avoider of length 4p - 2 over D_(2p) with o_F(w) <= (p+1)/2.  Then
all rotation letters of w lie in one set {rho_c, rho_-c}, c != 0.
Proof.  Take the normal form w^ of proof-ROT-few-E-v4.md Sec. 0 (L32-43).  It is an avoider of the same length and
rotation multiset, given by a cyclic representation with 1 <= k <= o_F(w) odd blocks and every empty run between blocks
of different values; the ending with one even block is impossible there.  If k = 1, Proposition K1 makes all rotations
equal.  Let k >= 2.  Then H = (F - k)/2, kappa = p - 1 - H >= 0, R = 2p + 2kappa - k, Lemma DAV gives kappa <= k - 1,
and GRX gives (ZP) for the sequence Y of the values Y(x) over the rotation letters (L42-43).  As k <= (p+1)/2, Lemma ZS
applies.  Write its generator as g = Y(c).  Then c != 0, since g != (1,0).  Y(x) = b g means x = b c (mod p), so the
SHgen weight of rho_x relative to c (proof-SHgen-v3.md L39-43) is b_x = b(Y(x)).  Every |b| <= k <= p - 2, so no rotation
is rho_0, the lights are the terms with b = +-1, and E and N are those of Lemma ZS: E <= k - 1 - N.  If E = 0 every
rotation is rho_c or rho_-c.  Otherwise eta >= 1 and we check the two hypotheses of Theorem SHgen.
- (H): 2H = 2p - 2 - 2kappa >= 2p - 2k >= k - 1 >= E, since 3k <= 2p + 1.
- (K): every heavy has |b| >= 3, so eta <= E/2 <= (k-1)/2, and a_max <= E + 1 <= k.  Hence
  2p - eta - a_max - 1 >= 2p - (k-1)/2 - k - 1 >= k, because 5k <= 4p - 1 (from k <= (p+1)/2 and p >= 3).
If all runs of w^ are nonempty, w^ is in the setting of proof-SHgen-v3.md Sec. 0 and Theorem SHgen gives w^ an identity
2p-subword.  Otherwise Lemma SHgen-E (proof-ROT-few-E-v4.md Sec. 1) gives one.  Its REFL instances have o_F <= k <= p,
and Corollary REFL-few-odd supplies them.  Either way this contradicts that w^ avoids.  So E = 0.  The rotation multiset
of w is that of w^.  []

## 4. Corollaries

**Corollary INV*-HALF.**  For every prime p >= 5, every avoider w of length 4p - 2 over D_(2p) with
o_F(w) <= (p+1)/2 satisfies INV*: all rotations lie in one {rho_c, rho_-c}, c != 0, and every maximal cyclic
reflection run is constant.
Proof.  Theorem ROT-HALF gives the rotations.  Corollary REFL-few-odd applies to w: (0) p >= 5 is prime, (a) |w| = 4p - 2,
(b) the pair just found, and (d) o_F(w) <= (p+1)/2 <= p.  []

**Corollary OLSON-HALF.**  For every prime p >= 5, every word w of length 4p - 1 over D_(2p) with o_F(w) <= (p+1)/2
has an identity 2p-subword in increasing index order.
Proof.  Use the proof of OLSON-FEW (proof-OLSON-few-v3.md L28-47) verbatim, with B := (p+1)/2 and Corollary INV*-HALF
in place of INV*-FEW.
- Case 1 (R <= 2) needs o_F(w) <= B <= 2p - 3, which holds for p >= 5.
- Case 2 calls INV* on w', where o_F(w') = o_F(w) - 1 <= B.  Case 3 calls it on w_i, where o_F(w_i) is o_F(w) or
  o_F(w) - 2, so <= B.  The deletion ledger of proof-FEW-p5-lift-v3.md Sec. 4.1 (D1)-(D4) does not depend on p.
- RGR-LONG(p) then gives the identity 2p-subword.  []

## 5. Ranges and scope

- Range: o_F <= (p+1)/2, i.e. 6 at p = 11, 7 at p = 13, 9 at p = 17, 10 at p = 19, 12 at p = 23 and 15 at p = 29.  The
  accepted (b) range 5 o_F <= 2p + 4 gives 5, 6, 7, 8, 10 and 12 there.  It is contained in the new range for every
  p >= 3, since (2p+4)/5 <= (p+1)/2.  Together with the accepted o_F <= 4: o_F <= max(4, (p+1)/2) for every prime p >= 5.
- For p = 5 and p = 7, (p+1)/2 <= 4, so nothing new.  KAPPA01 (proof-KAPPA01-v4.md) still covers more on its two slices
  kappa in {0, 1}: 3 o_F <= 2p + 1.
- Not covered: o_F > max(4, (p+1)/2); Remark (3) shows that the (ZP)-only route cannot reach o_F = p.  Not ROT(p),
  INV*(p) or ordered Olson for D_(2p) in general.  No novelty claim.
- Finite aid (not a premise): the earlier exhaustive check code/check_rotfew_v3.py (README 06:37:49) found the
  conclusion E <= k - 1 - N for every (ZP) multiset at (p, k) = (11, 6) and (13, 7), every kappa.  That check takes g
  as the most frequent value of Y and was written before this lemma; it neither uses nor tests Steps 2-9.
