# Lemma ZX (exchange form of Lemma ZS) and Theorem ROT-ZX: rotation rigidity when the terminal normal form has 3k <= 2p + 1 and kappa <= (p-1)/2, v1

Owner OlsonRotationRigidity.  Written after host clock 2026-10-18T11:40:01-07:00.  Status [W], UNREVIEWED.

This is a new file, and it changes no earlier file.
- proof-ROT-half-v1.md (3b8fa50e...c738) is parent-accepted (R/olson-half-range-parent-verdict-v1.md, b3afb001...1c3b).
- proof-ROT-half-v2.md (7403098f...48eb) is under its own delta reviews; Codex returned ACCEPT-WITH-FIXES in
  R/olson-rotation-zs-v2-delta-codex-v1.note.md (a6927723...56af).
- Neither file is modified or replaced here.  This file has its own proof.

**New here.**
- Lemma ZX, with a new proof: an exchange argument on a longest zero-sum.  It replaces Steps 4-8 of the ZS proof.
  Apart from the length, its only hypothesis is (S1): every zero-sum subsequence has length <= 2 kappa.
- Lemma S1: (ZP) implies (S1) when kappa <= (p-1)/2.  Otherwise it describes exactly the configuration in which (S1)
  fails.
- Theorem ROT-ZX, stated with the TERMINAL normal-form parameters k and kappa^, and Corollaries INV*-ZX and OLSON-ZX.

No novelty claim.  Not ROT(p), INV*(p) or ordered Olson in general.

Paths: R = institute/runs/six-lane-2026-10-16/review/; files without a directory are in this rotation/ directory.

Imports, all parent-accepted at their stated scopes:
- (D) D(Z_(2p)) = 2p, GRX, PM* and Proposition K1: R/olson-rotation-lowodd-parent-verdict-v2.md (0853f4ac...ba29).
- Lemma MULT (i)-(iii): proof-ROT-few-v4.md (abd3973c...b521) L61-81, accepted with ROT-FEW
  (R/olson-fewodd-parent-verdict-v1-addendum-1.md, 279d89d2...a62a, L11).  Its proof uses SCHERK, GROW, SET and
  INC (a), (b) of that file.
- From proof-ROT-few-E-v4.md (ac560eb8...ea8f):
  - the normal form, Lemma DAV / (V) and (ZP) for the normal form: Sec. 0, L28-43;
  - Lemma SHgen-E: Sec. 1, L45-70.
  - Both are used at their own hypotheses (half-range verdict, overlay 3).
- Theorem SHgen with its setting, GRX form, (ZP), (V), kappa >= 0 and weights: proof-SHgen-v3.md (fcbd5a97...eb5e)
  L20-49.
- Corollary REFL-few-odd: reflection/proof-REFL-fewodd-r4.md (1e447754...861d) L21-25 and its Sec. 4 interface
  (R/olson-refl-fewodd-parent-verdict-v1.md, 16436c07...f1ca, L6).
- For Sec. 5 only:
  - RGR-LONG(p): R/olson-runs-parent-verdict-v1.md (82adbddd...9237) L7;
  - the case structure of proof-OLSON-few-v3.md (ae151f9b...d66a) L28-47.

**Notation** (as in proof-ROT-few-v4.md L20-23).
- Y(x) := (1, x) in Z_2 x Z_p = Z_(2p).  Elements with first coordinate 1 are "odd".  (1,0) has order 2, and every
  other odd element generates Z_(2p).
- For an odd generator g, every odd y equals b g for a unique odd integer b = b_g(y) in (-p, p]; (1,0) = p g.
- A sequence is a multiset, and T <= Y means a sub-multiset.  Zero-sums of odd elements have even length.  A
  "zero-sum subsequence" is nonempty unless it is called possibly empty.
- cost_g(Y) := sum over the terms with b > 0 of (b - 1)  +  sum over the terms with b < 0 of |b|.
- For a word w:
  - F = F(w) is the number of reflections;
  - o = o_F(w) is the number of odd blocks in the maximal cyclic constant reflection-block decomposition, and F = o
    (mod 2);
  - kappa(w) := p - 1 - (F - o)/2.
- For the normal form w^ of an avoider (proof-ROT-few-E-v4.md Sec. 0): the terminal number of blocks k satisfies
  1 <= k <= o and k = o (mod 2); H = (F - k)/2; and kappa^ := p - 1 - H = kappa(w) - (o - k)/2.

## 1. Statements

**Lemma ZX.**  Let p >= 5 be prime and let k, kappa be integers with
  (G') k >= 1,  3k <= 2p + 1,  0 <= kappa <= k - 1.
Let Y be a sequence of R = 2p + 2kappa - k odd elements of Z_(2p) such that
  (S1) every zero-sum subsequence of Y has length <= 2kappa.
Let Z be a zero-sum subsequence of Y of maximal length (possibly empty), Y' := Y - Z, and g a value of largest
multiplicity in Y'.  Then g is a generator, and
  cost_g(Y) <= e := k - 1 - 2kappa + |Z| <= k - 1.
Moreover:
- every term of Y has |b_g| <= k, so no term is (1,0);
- every term of Z with b_g > 0 equals g;
- E + N = cost_g(Y), where E := sum over all terms of (|b| - 1) and N := #{terms with b < 0}.

**Lemma S1.**  Let kappa >= 0 and let Y be a sequence of odd elements such that
  (ZP) Y has no zero-sum subsequence of length in [2kappa + 2, 2p].
 (a) If 4kappa <= 2p - 2, then (S1) holds.
 (b) Suppose 6kappa <= 4p + 2 and (S1) fails.  Then Y contains two disjoint minimal zero-sum subsequences P, P' with
     2p - 2kappa + 2 <= |P|, |P'| <= 2kappa and |P| + |P'| >= 2p + 2.  In particular 2kappa >= p + 1.

**Corollary ZS+.**  Under (G'), kappa <= (p - 1)/2 and (ZP), the conclusion of Lemma ZX holds (by Lemma S1 (a)).
- This contains hypothesis (G) of proof-ROT-half-v2.md, where kappa <= min(k - 1, p - k) <= (p - 1)/2.
- It contains the accepted Lemma ZS of v1: k <= (p + 1)/2 gives kappa <= k - 1 <= (p - 1)/2.
- Under (G'), kappa <= k - 1 <= (2p - 2)/3, so 6kappa <= 4p - 4 and Lemma S1 (b) applies whenever (S1) fails.

## 2. Proof of Lemma ZX

Step A (splitting, MULT, weights).
- By (S1), |Z| <= 2kappa.
- Y' is zero-sum-free: a zero-sum V <= Y' would make Z V a longer zero-sum.
- By (D), L := |Y'| <= 2p - 1, and L = R - |Z| >= 2p - k.  So e := 2p - 1 - L = k - 1 - 2kappa + |Z| satisfies
  0 <= e <= k - 1, and 3e + 2 <= 3k - 1 <= 2p.
- Lemma MULT (iii), (ii) apply: the multiplicity m of g in Y' satisfies m >= max(2, e + 1), g is a generator, and
  Y' = g^m (d_1 g) ... (d_q g) with odd d_j >= 3 and e' := sum_j (d_j - 1) <= e.
- (A1) Each d_j - 1 >= 2, so q <= e'/2 and m = L - q >= L - e'/2.
- (A2) Every d_j <= e' + 1 <= e + 1 <= m.  Also d_j <= k <= p - 2: for p >= 7, 3k <= 2p + 1 gives k <= p - 2, and for
  p = 5 it gives k <= 3.  Hence b_g(d_j g) = d_j.
- Weights.  For Q <= Y' put w(Q) := #(g in Q) + (sum of the d_j over the terms d_j g in Q).  The sum of Q is w(Q) g.
  Put W' := w(Y') = L + e'.

COMP (as in proof-ROT-half-v1.md Step 3):
 (a) every integer t in [0, W'] is w(Q) for some Q <= Y';
 (b) W' <= 2p - 1;
 (c) |Q| = w(Q) - (sum of d_j - 1 over the terms d_j g in Q) >= w(Q) - e'.
Proof.
- (a) The weights of subsequences of g^m are exactly [0, m].  If every integer in [0, M] is a weight and d <= M + 1,
  then after adding d g every integer in [0, M + d] is a weight.  Add d_1, ..., d_q in turn; each d_j <= m <= M + 1 by
  (A2).
- (b) If W' >= 2p, then by (a) some Q has weight 2p, which is a nonempty zero-sum in Y'.
- (c) is clear.  []

Consequences:
- (A3) W' >= L >= 2p - k >= p + 2.
- (A4) Every single term of Y' has weight 1 or some d_j, both <= m.  So every Q <= Y' with w(Q) > m has |Q| >= 2.  For
  t <= m, Q = g^t has w(Q) = t and |Q| = t.

Step B (exchange).  For U <= Z put s(U) := the sum of b_g over the terms of U, an integer; the sum of U is s(U) g.
  (EX) If U <= Z and Q <= Y' satisfy w(Q) = s(U) (mod 2p), then |Q| <= |U|.
Proof.  Z* := (Z - U) Q is a subsequence of Y, because Q is disjoint from Z.  Its sum is (s(Z) - s(U) + w(Q)) g = 0.
By the maximality of |Z|, |Z| - |U| + |Q| <= |Z|.  []

Step C (positive terms of Z).  Every term z of Z with b := b_g(z) > 0 has b = 1, i.e. z = g.
Proof.  Suppose b >= 3 (b is odd).  Then b <= p < W' by (A3).
- If b <= m, then Q := g^b has w(Q) = b and |Q| = b >= 3.
- If b > m, then COMP (a) gives some Q with w(Q) = b, and |Q| >= 2 by (A4).
Either way, (EX) with U = {z} gives |Q| <= 1: a contradiction.  []
So Z = g^r T, where r := #(g in Z) and T consists of the terms of Z with b < 0.  For z in T put
beta(z) := -b_g(z), an odd integer in [1, p - 2].  Put sigma := the sum of beta over T.

Step D (terms of T are light).  Every z in T has beta(z) <= e - e'.
Proof.  Let beta := beta(z).  Then s({z}) = -beta = 2p - beta (mod 2p), and 2p - beta >= p + 2.
Suppose 2p - beta <= W'.  By COMP (a) there is a Q <= Y' with w(Q) = 2p - beta and |Q| >= 2: take
Q = g^(2p - beta) if 2p - beta <= m, and use (A4) otherwise.  (EX) with U = {z} gives |Q| <= 1: a contradiction.
So 2p - beta >= W' + 1 = L + e' + 1 = 2p - e + e', i.e. beta <= e - e'.  []

Step E (Z is balanced).  sigma = r.
Proof.  s(Z) = r - sigma = 0 (mod 2p).  Also 0 <= r <= |Z| <= 2kappa <= 2k - 2 < 2p and sigma >= 0, so
sigma = r + 2pt for some integer t >= 0.  Suppose t >= 1.
- Then T is nonempty, so e - e' >= 1 by Step D.
- By (A1), and since 3e <= 3k - 3 <= 2p - 2,
    2m - 2p + 1 >= 2L - e' - 2p + 1 = 2p - 1 - 2e - e' >= e - e' >= 1.
- So the integer interval I := [2p - m, m] has |I| = 2m - 2p + 1 >= e - e' elements.  It is nonempty, lies in
  [1, 2p - 1] (as m <= L <= 2p - 1), and is symmetric under x -> 2p - x.
- List T as z_1, ..., z_s and put S_j := beta(z_1) + ... + beta(z_j).  Then S_0 = 0 < 2p - m, S_s = sigma >= 2p > m,
  and S_j - S_(j-1) <= e - e' by Step D.
- For the least j with S_j >= 2p - m: S_j <= (2p - m - 1) + (e - e') <= (2p - m - 1) + |I| = m.  So S_j lies in I.
- Let U := {z_1, ..., z_j}.  Then s(U) = -S_j = 2p - S_j (mod 2p), and 2p - S_j lies in I.  So
  Q_1 := g^(2p - S_j) <= Y', and (EX) gives 2p - S_j <= j.
- Let U^c := Z - U.  Then s(U^c) = s(Z) - s(U) = S_j (mod 2p).  So Q_2 := g^(S_j) <= Y', and (EX) gives
  S_j <= |Z| - j.
- Adding the two inequalities: 2p <= |Z| <= 2kappa < 2p, a contradiction.
So t = 0.  []

Step F (room left in Y').  W' <= 2p - 1 - r.
Proof.  For r = 0 this is COMP (b).  Let r >= 1, and suppose 2p - r <= W'.  COMP (a) and (c) give a Q <= Y' with
w(Q) = 2p - r and |Q| >= 2p - r - e'.  By Step E, s(T) = -sigma = -r = 2p - r (mod 2p), so (EX) with U = T gives
|Q| <= |T|.  Hence 2p <= r + |T| + e' = |Z| + e' <= 2kappa + e <= 3(k - 1) <= 2p - 2, a contradiction.  []

Step G (count).  The contributions to cost_g(Y) are:
- the terms of Y': sum_j (d_j - 1) = e', since each has b = 1 or b = d_j (A2);
- the r copies of g in Z: 0;
- T: sigma = r.
Hence
  cost_g(Y) = e' + r = (W' - L) + r <= (2p - 1 - r - L) + r = e = k - 1 - 2kappa + |Z| <= k - 1,
using Step F and |Z| <= 2kappa.
Every |b| is <= k: on Y' by (A2), on g^r trivially, and on T by Step D (beta <= e <= k - 1).  So no term is (1,0),
whose b is p > k.  Finally E + N = sum over all terms of (|b| - 1) + #{b < 0} = cost_g(Y).  []

Remarks.
(1) Equality.
- If kappa = 0, Y is zero-sum-free, Z is empty and Y = Y'.
- If kappa = k - 1, take Y = g^(2p-1) (-g)^kappa.  Its zero-sums are the (g (-g))^j, of length 2j <= 2kappa, so (S1)
  holds for every k in (G').  Here Z = (g (-g))^kappa, r = sigma = kappa, Y' = g^(2p-1-kappa), e = kappa, e' = 0, and
  cost_g(Y) = kappa = k - 1.  So the bound k - 1 is attained at every k in (G'), with no condition kappa <= p - k.
(2) Difference from the ZS proof.
- Steps 4-8 of proof-ROT-half-v1.md bounded |U| + |Q| <= 2kappa through Step 1 (Step 4).  They used the complementary
  pair U, Z - U (Step 5), which needed 2kappa <= 2p - 2k.
- Here the maximality of |Z| is used directly as the exchange (EX).  This is sharper, |Q| <= |U| (equivalently
  |U^c| + |Q| <= |Z|), and gives Steps C and D one term at a time.
- The window argument of Step E replaces Step 5 and needs only 3e <= 2p - 1.
- A longest Z is needed for (EX); an inclusion-maximal Z would not do.
(3) Where the hypotheses are used:
- 3k <= 2p + 1: in Step A (MULT needs 3e + 2 <= 2p; also k <= p - 2 and (A3)), Step E (3e <= 2p - 2) and Step F
  (3k - 3 < 2p);
- kappa <= k - 1: in Steps E and F;
- (S1): only through |Z| <= 2kappa, in Steps A, E, F and G.

## 3. Proof of Lemma S1

(a) This is Step 1 of proof-ROT-half-v1.md.
- A minimal zero-sum subsequence has length <= 2p: deleting one term leaves a zero-sum-free sequence, of length
  <= 2p - 1 by (D).  Its length is even, so by (ZP) it is <= 2kappa.
- Every zero-sum T is a product T_1 ... T_r of minimal zero-sum subsequences: take one, then induct on the rest.
- If |T| >= 2kappa + 2, let j be least with |T_1| + ... + |T_j| >= 2kappa + 2.  Then T_1 ... T_j is a zero-sum of
  length in [2kappa + 2, 4kappa], and 4kappa <= 2p - 2: contrary to (ZP).  []
(b) Let T be a zero-sum with |T| >= 2kappa + 2.  By (ZP), |T| >= 2p + 2.
- Write T = T_1 ... T_r as in (a).  Every |T_i| <= 2kappa.  Every union of some of the T_i is a zero-sum, so its length
  is not in [2kappa + 2, 2p].
- Call T_i long if |T_i| >= 2p - 2kappa + 1.  Suppose at most one T_i is long, and number it T_1 if it exists.
  - The lengths l_j := |T_1| + ... + |T_j| increase from l_1 <= 2kappa to l_r = |T| >= 2kappa + 2.
  - At the least j with l_j >= 2kappa + 2 we have j >= 2 and l_(j-1) <= 2kappa.  Also |T_j| <= 2p - 2kappa, as T_j is
    not long.
  - So l_j lies in [2kappa + 2, 2p], contrary to (ZP).
- Hence two pieces P, P' are long, and |P|, |P'| >= 2p - 2kappa + 2 (they have even length).
- Then |P| + |P'| >= 4p - 4kappa + 4 >= 2kappa + 2, as 6kappa <= 4p + 2.  P P' is a zero-sum, so |P| + |P'| >= 2p + 2.
- As |P|, |P'| <= 2kappa, it follows that 4kappa >= 2p + 2.  []

## 4. Theorem ROT-ZX

**Theorem ROT-ZX.**  Let p >= 5 be prime and w an avoider of length 4p - 2 over D_(2p).  Let w^ be its normal form
(proof-ROT-few-E-v4.md Sec. 0, L28-43), with terminal k and kappa^ = p - 1 - (F - k)/2.  Suppose that k = 1, or that
  3k <= 2p + 1 and the rotation sequence of w^ satisfies (S1) with kappa = kappa^.
In particular the second condition holds whenever 3k <= 2p + 1 and kappa^ <= (p - 1)/2.  Then all rotation letters of
w lie in one set {rho_c, rho_-c}, c != 0.
Proof.
- Normal form.  By Sec. 0, w^ is an avoider with the same length, rotation multiset and F as w.  It is given by a
  cyclic representation with 1 <= k <= o odd blocks, and every empty run lies between blocks of different values.
  The ending with one even block is impossible (L39-41).
- k = 1.  Proposition K1 makes all rotations equal (and then F = 2p - 1 and kappa^ = 0).
- Let k >= 2.
  - kappa^ >= 0: if H >= p, GRX's all-plus pattern with m = 0 selected rotations is already an identity selection
    (proof-SHgen-v3.md L37).  GRX allows empty runs.
  - Lemma DAV gives kappa^ <= k - 1 (L42-43).  So (G') holds.
  - GRX with z = all + gives (ZP) for the sequence Y of the values Y(x) over the rotation letters of w^.  Y has length
    R = 2p + 2kappa^ - k (L42-43).
  - If kappa^ <= (p - 1)/2, Lemma S1 (a) gives (S1).
  - Lemma ZX gives a generator g = Y(c) with c != 0 (as g != (1,0)), cost_g(Y) <= k - 1, and every |b_g| <= k.
- Weights.  Since k <= p - 2, every rotation has |b| <= k <= p - 2.  Y(x) = b g means x = b c (mod p).  As b is odd
  with |b| <= p - 2, it is the SHgen weight b_x of rho_x relative to c (proof-SHgen-v3.md L39-41).  x = 0 would need
  b = p (b_0 := p), which is excluded.  So the lights are the rotations with b = +-1, and E and N are those of Lemma
  ZX, with E + N <= k - 1.
- If E = 0, every rotation is rho_c or rho_-c.
- Otherwise eta >= 1, and both hypotheses of Theorem SHgen hold:
  - (H): 2H = 2p - 2 - 2kappa^ >= 2p - 2k >= k - 1 >= E, by 3k <= 2p + 1.
  - (K): every heavy has |b| >= 3, so eta <= E/2 <= (k - 1)/2 and a_max <= E + 1 <= k.  Hence
    2p - eta - a_max - 1 >= 2p - (k - 1)/2 - k - 1 >= k, because 5k <= 4p - 1 (from 3k <= 2p + 1 and p >= 4).
- If all runs of w^ are nonempty, w^ is in the setting of proof-SHgen-v3.md Sec. 0, and Theorem SHgen gives w^ an
  identity 2p-subword.  Otherwise Lemma SHgen-E (proof-ROT-few-E-v4.md Sec. 1) gives one.
  - SHgen-E needs REFL(p) only for words with o_F <= k <= p, which Corollary REFL-few-odd supplies.
  - The caller obligation o_F <= k <= p holds throughout its induction (half-range verdict, overlay 3).
- Either way this contradicts that w^ avoids, so E = 0.  The rotation multiset of w is that of w^.  []

**Corollary ROT-ZX (uniform sufficient conditions).**  Let w be an avoider of length 4p - 2 and o = o_F(w).  Theorem
ROT-ZX applies if 3o <= 2p + 1 and either
- o <= (p + 1)/2, or
- kappa(w) <= (p - 1)/2, i.e. F >= o + p - 1.
Proof.  k <= o gives 3k <= 2p + 1, and kappa^ = kappa(w) - (o - k)/2 <= kappa(w).  If o <= (p + 1)/2, then
kappa^ <= k - 1 <= o - 1 <= (p - 1)/2.  []
Only the terminal parameters matter: an avoider with 3o > 2p + 1 is covered whenever its terminal k satisfies
3k <= 2p + 1 and kappa^ <= (p - 1)/2.

## 5. Corollaries INV*-ZX and OLSON-ZX

**Corollary INV*-ZX.**  Every avoider w of length 4p - 2 (p >= 5 prime) that is covered by Theorem ROT-ZX and has
o_F(w) <= p satisfies INV*.  In particular this holds for every avoider with 3 o_F(w) <= 2p + 1 and either
o_F(w) <= (p + 1)/2 or F(w) >= o_F(w) + p - 1.
Proof.  Theorem ROT-ZX gives the pair.  Corollary REFL-few-odd applies to w, with (0) p >= 5 prime, (a) |w| = 4p - 2,
(b) that pair, and (d) o_F(w) <= p.  []

**Corollary OLSON-ZX.**  Let p >= 5 be prime and w a word of length 4p - 1 over D_(2p), with o := o_F(w) and
F := F(w).  Suppose 3o <= 2p + 1, and either o <= (p + 1)/2 or F - o >= p - 1.  Then w has an identity 2p-subword in
increasing index order.
Proof.  Suppose not, so every subword avoids.  Follow proof-OLSON-few-v3.md L28-47 with Corollary INV*-ZX in place of
INV*-FEW.  The deletion calculations:
- Case 1 (R <= 2; L31-36).  F >= 4p - 3 and o <= (2p + 1)/3 <= 2p - 3, so the blocks contain (F - o)/2 >= p disjoint
  adjacent equal pairs.  No INV* call is made.
- Case 2 (an odd block of length >= 3; L37-39).  Deleting one of its letters gives w' with o' = o - 1 and F' = F - 1:
  that block becomes even and nonempty, and no other block changes.  So 3o' <= 2p + 1 and F' - o' = F - o.  Also
  o' <= (p + 1)/2 if o <= (p + 1)/2.  So INV*-ZX applies to w'.
- Case 3 (R >= 3; L40-46).  w_i := w - x_i has F_i = F and o_i := o_F(w_i) <= o, since deleting a rotation never
  raises o_F (L42-43; a fusion of two odd blocks lowers it by 2).  So 3o_i <= 2p + 1 and F_i - o_i >= F - o.  Also
  o_i <= (p + 1)/2 if o <= (p + 1)/2.  So INV*-ZX applies to w_i.
Then L37-47 show that w is RGR, and RGR-LONG(p) gives an identity 2p-subword: a contradiction.  []

## 6. Ranges, residual and scope

Terminal-parameter coverage.
- Lemma ZX with Lemma S1 (a) covers every (k, kappa^) with 3k <= 2p + 1 and kappa^ <= min(k - 1, (p - 1)/2).
  - v1 covers k <= (p + 1)/2.
  - v2's (G) covers kappa^ <= min(k - 1, p - k).
- New terminal pairs exist exactly when k >= (p + 3)/2; they are those with p - k < kappa^ <= (p - 1)/2.
  - p = 7: (5, 3).
  - p = 11: (7, 5).
  - p = 13: (8, 6), (9, 5), (9, 6).
  - p = 17: (10, 8), (11, 7), (11, 8).

Uniform word conditions.
- The new condition is 3o <= 2p + 1 and F >= o + p - 1, besides the accepted o <= (p + 1)/2.
- Compared with v2's F >= 3o - 2, it is new for (p + 1)/2 < o and o + p - 1 <= F <= 3o - 4, with F = o (mod 2).
- Examples:
  - p = 7, o = 5: F >= 11 (v2: F >= 13);
  - p = 13, o = 8: F >= 20 (v2: 22);
  - p = 13, o = 9: F >= 21 (v2: 25).

Residual inside 3k <= 2p + 1 (terminal parameters).
- What remains is kappa^ >= (p + 1)/2, which needs k >= (p + 3)/2.
  - p = 7: (5, 4).
  - p = 11: (7, 6).
  - p = 13: (8, 7), (9, 7), (9, 8).
  - p = 17: (10, 9), (11, 9), (11, 10).
- If the rotation sequence satisfies (S1), Theorem ROT-ZX applies, since its hypothesis is (S1) itself.  The type-II
  sequence of Remark (1) is such a case.
- By Lemma S1 (b), (S1) can fail only if the rotation sequence contains two disjoint minimal zero-sums P, P' with
  2p - 2kappa^ + 2 <= |P|, |P'| <= 2kappa^ and |P| + |P'| >= 2p + 2.  For such sequences nothing is proved here: the
  conclusion of Lemma ZS is neither proved nor refuted.

Outside 3k <= 2p + 1 (terminal).
- Such avoiders are not covered by the statements of this file; Remark (3) lists where the proof uses 3k <= 2p + 1.
- This is a limit of these sufficient conditions.  It is not a claim that MULT or this method is unavailable there:
  the actual e of a given sequence may be small.
- The sequence g^(2p-1) (3g)^(p-1) of proof-ROT-half-v2.md Remark (3) refutes the cost conclusion under (ZP) only at
  the one pair (k, kappa) = (p, p - 1).

Finite aid, not a premise: run1 of zs-check-v1 (out/run1.jsonl, bb8ddafb...9b1a; README 11:07:11).
- The ZS cost conclusion held for every (ZP) multiset at (7,5,3..4), (11,7,5..6), (13,8,6..7) and (13,9,5..8).
- These include the new pairs (7,5,3), (11,7,5), (13,8,6), (13,9,5..6) and the residual pairs (7,5,4), (11,7,6),
  (13,8,7), (13,9,7..8).
- It did not test (S1) or Steps B-G at these items.

Not ROT(p), INV*(p) or ordered Olson for D_(2p) in general.  No novelty claim.  No finite census is used as a premise.
