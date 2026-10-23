# Theorem ROT-FEW: ROT for avoiders with at most (2p+4)/5 odd constant blocks, v3

Owner OlsonRotationRigidity.  Written after host clock 2026-10-18T06:35:53-07:00.  Status [W], UNREVIEWED.
CONDITIONAL on Theorem SHgen (proof-SHgen-v2.md, sha256 8fde88c0...d239, unreviewed).  Supersedes proof-ROT-few-v2.md
(53fed0db...d9e1) and v1 (7ec186ea...4975), both kept unchanged; their theorems are implied by this one.
Change from v2 (only Lemma WT (c), the theorem's hypotheses, Steps 1-5 citations, Sec. 7 and Sec. 8): WT (c) now
balances the negatives with ANY positive terms (g's and positive heavies), not only g's, so it needs |P| >= 4kappa - 2
instead of G >= 4kappa - 1; v2's conditions 4p >= 11(k-1) and p >= 2k-1 disappear and 2p >= 5k - 4 alone implies every
other condition.  The range grows from about 1 + 4p/11 to (2p+4)/5 odd blocks.  Sections 1-4 and WT (a), (b) are
verbatim from v2.
Uniform in kappa; the structure of the rotation multiset uses only the all-plus pattern (ZP).
Imports: GRX, Lemma PM*, (D) [R/olson-rotation-lowodd-parent-verdict-v2.md, 0853f4ac...ba29]; Lemma INC parts (a) and
(b) [proof-ROT-o3-v3.md, parent-accepted in R/olson-rotation-o3o4-parent-verdict-v1.md; parts (a), (b) do not use the
length hypothesis of INC]; the setting, (ZP), (V) (Davenport-alpha instance with erratum m4) and Theorem SHgen of
proof-SHgen-v2.md.
Notation.  Y(x) := (1, x) in Z_2 x Z_p = Z_(2p); elements with first coordinate 1 are "odd".  (1,0) has order 2; every
other odd element generates Z_(2p), and for an odd generator g the odd elements are exactly the r g, r odd in
[1, 2p-1].  For a sequence S, A(S) := {0} u {nonempty subset sums}; S is zero-sum-free if 0 is not a nonempty subset
sum; extras(S) := |A(S)| - 1 - |S|.  Zero-sums of odd elements have even length.
INC (a): for a zero-sum-free S and ANY ordering, each new term adds >= 1 new element to A; so extras(S) >= 0 equals the
sum of (new elements - 1) over any ordering, and |A(S)| <= 2p gives extras(S) <= 2p - 1 - |S|.
INC (b): three distinct values x, y, z of a zero-sum-free sequence have |A(x y z)| = 8.

## 1. Lemma SCHERK

Let A, B be finite subsets of an abelian group with 0 in A n B such that a + b = 0 (a in A, b in B) only for
a = b = 0.  Then |A + B| >= |A| + |B| - 1.
Proof.  Induction on |B|; |B| = 1 is clear.  Let |B| >= 2.  Some e in A has e + B not inside A: otherwise A + b = A
for every b in B, so -b in A, and (-b) + b = 0 with b != 0 in B is forbidden.  Put A' := A u (e + B),
B' := B n (A - e).  Then 0 in A' n B' (e in A), |B'| < |B| (some b in B has e + b outside A), |A'| + |B'| = |A| + |B|
(|A'| = |A| + |B| - |A n (e+B)| and |B'| = |(e+B) n A|), and A' + B' lies in A + B (for b' in B', e + b' is in A, so
(e + b) + b' = b + (e + b')).  If x + y = 0 with x in A', y in B': for x in A, y in B gives x = y = 0; for x = e + b
outside A, b + (e + y) = 0 with b in B, e + y in A forces b = 0, so x = e in A, a contradiction.  By induction
|A + B| >= |A' + B'| >= |A'| + |B'| - 1 = |A| + |B| - 1.  []

## 2. Lemma GROW

Let D be a zero-sum-free SET of d >= 3 distinct odd elements with |A(D)| <= 2p-2.  Then some x in D has
|A(D)| >= |A(D - x)| + 2.
Proof.  Otherwise, by INC (a), |A(D)| = |A(D - x)| + 1 for every x in D.  At most one element is (1,0); take distinct
generators x, y in D.  For a generator x and a set B with 0 < |B| < 2p, |(B + x) - B| is the number of maximal x-arcs of
B on the cycle 0, x, 2x, ..., (2p-1)x.  As A(D) = B u (B + x) with B := A(D - x), B is ONE x-arc {u, u+x, ..., u+jx}
containing 0.  If 0 = u + ix with i >= 1, then -x = u + (i-1)x lies in B, i.e. -x is a nonempty subset sum of D - x,
and with x it gives a zero-sum: impossible.  So u = 0 and A(D) = {0, x, ..., Jx}, J := |A(D)| - 1.  Likewise
A(D) = {0, y, ..., Jy}.  Write y = r x.  Then the index arc I := {0, 1, ..., J} of Z_(2p) equals {0, r, 2r, ..., Jr},
so |I n (I + r)| >= J = |I| - 1.  For an arc of length l, 2 <= l <= 2p-2, and r' in [1, 2p-1] the residue of r,
|I n (I + r')| = max(0, l - r') + max(0, l - 2p + r'); if both terms are positive the sum is 2l - 2p <= l - 2,
otherwise it is >= l - 1 only for r' = 1 or r' = 2p-1.  So y = x (not distinct) or y = -x (zero-sum x y).  []
Corollary SET.  A zero-sum-free set D of d odd elements has |A(D)| >= 2d, i.e. extras(D) >= d - 1.
Proof.  d = 1: |A| = 2.  d = 2: A = {0, x, y, x+y}, four distinct elements (x != y, x + y != 0).  d >= 3: if
|A(D)| >= 2p - 1, then, as D holds at most one of x, -x for each odd x and (1,0) at most once, d <= (p+1)/2 and
|A(D)| >= 2p - 1 >= 2d + 2; otherwise remove, by GROW, one element at a time lowering |A| by >= 2 until three remain
and use INC (b): |A(D)| >= 8 + 2(d-3) = 2d + 2.  []

## 3. Lemma MULT

Let Y' be a zero-sum-free sequence of odd elements of length L, e := 2p - 1 - L, m its largest multiplicity, attained
by the value g.
 (i)   (layers) m >= L - e = 2p - 1 - 2e.
 (ii)  If m >= max(2, e + 1) then g is a generator and Y' = g^m (d_1 g) ... (d_q g) with odd integers d_j >= 3 and
       sum_j (d_j - 1) <= e; in particular q <= e/2.
 (iii) If 2p >= 3e + 2 then m >= max(2, e + 1).
Proof.  (i) Let D_j (1 <= j <= m) be the set of values of multiplicity >= j; Y' is the disjoint union of the D_j and
sum_j |D_j| = L.  Put T_j := A(D_1) + ... + A(D_j) (sumset); T_m lies in A(Y').  If a + b = 0 with a in T_(j-1) and
b in A(D_j), the realising subsequences are disjoint and together sum to 0, so both are empty and a = b = 0.  SCHERK
gives |T_j| >= |T_(j-1)| + |A(D_j)| - 1, hence |A(Y')| - 1 >= sum_j (|A(D_j)| - 1), i.e.
extras(Y') >= sum_j extras(D_j) >= sum_j (|D_j| - 1) = L - m (Corollary SET).  With extras(Y') <= e: m >= L - e.
(ii) g = (1,0) would make g g a zero-sum, so m <= 1; hence g is a generator.  Put g^m first: A = {0, g, ..., mg}
(m+1 distinct elements, no zero-sum).  Add the other terms in any order; before each addition A = {0, g, ..., Mg} with
M >= m and M <= 2p - 2.  The next term is b = d g with d odd in [3, 2p-1].  If d + M >= 2p, then (2p - d)g, with
1 <= 2p - d <= M, is a nonempty subset sum of earlier terms and with b gives a zero-sum: impossible.  So d + M <= 2p - 1
and A + b = {dg, ..., (d+M)g} without wrap-around.  If d >= M + 2 all M + 1 of these are new: extras >= M >= m > e,
impossible.  So d <= M + 1, exactly d sums (M+1)g, ..., (M+d)g are new (extras d - 1), and A becomes {0, ..., (M+d)g}.
Summing, sum_j (d_j - 1) <= e.
(iii) By (i), m >= 2p - 1 - 2e >= e + 1, and 2p - 1 - 2e >= 2 (if e = 0, m = L = 2p - 1).  []

## 4. Lemma EXTRACT

Let Y be a sequence of odd elements and kappa >= 0 with 4kappa <= 2p such that
  (ZP) Y has no zero-sum subsequence of length in [2kappa + 2, 2p].
Then Y = Z Y' with Z a zero-sum subsequence (possibly empty), |Z| <= 2kappa, and Y' zero-sum-free.
Proof.  Take a maximal family of pairwise disjoint minimal zero-sum subsequences Z_1, ..., Z_q.  By (D) a minimal
zero-sum subsequence has length <= 2p (any 2p of its terms would contain a nonempty zero-sum subsequence), hence
<= 2kappa by (ZP).  If |Z_1| + ... + |Z_q| >= 2kappa + 2, the least j with |Z_1| + ... + |Z_j| >= 2kappa + 2 gives a
zero-sum Z_1 ... Z_j of length <= 2kappa + 2kappa <= 2p (lengths are even): contrary to (ZP).  So Z := Z_1 ... Z_q has
|Z| <= 2kappa, and Y' := Y - Z is zero-sum-free by maximality.  []

## 5. Lemma WT (weight bounds)

Let Y satisfy (ZP) for some kappa >= 0 with 4kappa <= 2p, and let g be an odd generator of multiplicity G in Y.
Every term h != g of Y is h = r g with r odd in [3, 2p-1].
 (a) If 2p - r <= G then b := 2p - r <= 2kappa - 1.  Call such h NEGATIVE of weight b (h = -b g); otherwise h is a
     POSITIVE heavy of weight r, and r <= 2p - G - 1.  g is positive of weight 1.  P, N: the positive / negative terms;
     w_+ := the largest weight in P.
 (b) G <= 2p - 1; and if G >= 2kappa + w_+ then sum_(h in P) r_h <= 2p - 1.
 (c) If G >= 2kappa + w_+ and |P| >= 4kappa - 2, then sum_(h in N) (b_h + 1) <= 2kappa.
Proof.  (a) h g^(2p-r) is a zero-sum of length 2p - r + 1 in [2, 2p-2], so 2p - r + 1 <= 2kappa.
(b) g^(2p) would be a zero-sum of length 2p.  Suppose sum_P r >= 2p; then P has heavies.  Add positive heavies one at a
time until their weight sum s first reaches 2p - G; I := those added (|I| >= 1), s <= 2p - G - 1 + w_+ <= 2p.  Then
I g^(2p-s) (0 <= 2p - s <= G) is a zero-sum of length |I| + 2p - s, which is <= 2p (|I| <= s) and
>= 1 + 2p - (2p - G - 1 + w_+) = G + 2 - w_+ >= 2kappa + 2: contrary to (ZP).
(c) Suppose sum_N (b+1) >= 2kappa + 2; take the shortest prefix S (any order) with sum_S (b+1) >= 2kappa + 2.  Since
b + 1 <= 2kappa by (a) and the shorter prefix has sum <= 2kappa, |S| >= 2, sum_S (b+1) <= 4kappa <= 2p, and
t := sum_S b <= 4kappa - 2 <= |P| <= W_P := sum_P r.  Choose Q in P of weight exactly t: if t <= G, Q := g^t;
otherwise add positive heavies one at a time until the remaining weight t - s first is <= G (possible because the
heavies of P weigh W_P - G >= t - G), then add t - s >= G + 1 - w_+ copies of g; so |Q| >= min(t, G + 2 - w_+), and
|Q| <= t (weights >= 1).  S Q is a zero-sum (weights t - t = 0) of length |S| + |Q| <= sum_S (b+1) <= 2p and
>= min(sum_S (b+1), |S| + G + 2 - w_+) >= 2kappa + 2: contrary to (ZP).  []

## 6. Theorem ROT-FEW

**Theorem ROT-FEW.**  Let p >= 5 be prime and k >= 2 an integer with
  (F) 2p >= 5k - 4.
Assume Theorem SHgen (proof-SHgen-v2.md).  Then every avoider of length 4p-2 over D_(2p) whose maximal cyclic
reflection runs are all constant, exactly k of them of odd length, has all rotation letters in one set
{rho_c, rho_-c}, c != 0.
Proof.  If R = 0 there is nothing to prove; F >= k >= 2.  Consecutive maximal reflection runs are separated by
nonempty rotation runs.  Iterated Lemma PM* gives an avoider w^ of length 4p-2 with the same rotation multiset, k odd
constant blocks and nonempty runs (merged runs contain nonempty runs): the form of SHgen-v2 Sec. 0.  For w^:
R = 2p + 2kappa - k, 0 <= kappa <= k - 1 by (V), H = p - 1 - kappa >= p - k.
Step 1.  Y := the sequence of Y(x) over the rotations satisfies (ZP).  4kappa <= 4k - 4 <= 2p by (F).  EXTRACT:
Y = Z Y', |Z| <= 2kappa, Y' zero-sum-free of length L >= R - 2kappa = 2p - k, so e := 2p - 1 - L <= k - 1.
Step 2.  3e + 2 <= 3k - 1 <= 2p (by (F), k >= 2), so MULT (iii), (ii): the most frequent value g of Y' is a generator and
Y' = g^m (d_1 g) ... (d_q g) with q <= e/2.  Hence G := multiplicity of g in Y satisfies
G >= m = L - q >= L - e/2 = (3L - 2p + 1)/2 >= (4p - 3k + 1)/2.
Step 3.  By WT (a) every positive heavy has weight <= 2p - G - 1 <= (3k-3)/2, so w_+ <= max(1, (3k-3)/2) and
G >= 2kappa + w_+ (as (4p - 3k + 1)/2 >= 2k - 2 + (3k-3)/2 is 4p >= 10k - 8, i.e. (F), and
(4p - 3k + 1)/2 >= 2k - 1 follows).  Every term of Y' is positive (a negative has r = 2p - b >= 2p - 2kappa + 1 > k by
(F), while the terms of Y' are g and d_j g with d_j <= e + 1 <= k), so N lies in Z and |P| >= L >= 2p - k >= 4kappa - 2
(by (F)).  WT (b), (c): sum_P r <= 2p - 1 and sum_N (b+1) <= 2kappa.
Step 4.  g = Y(c) with c != 0, and r g = Y(rc).  Positive heavies have 3 <= r <= (3k-3)/2 <= p - 2 and negatives have
1 <= b <= 2kappa - 1 <= 2k - 3 <= p - 2 (by (F): 2p >= 3k + 1 if k >= 3, there are no positive heavies if k = 2,
and p >= 2k - 1); so relative to c each rotation has SHgen weight b_x = r or -b,
lights are exactly g and -g, and no rotation is rho_0 (Y(0) = p g would need r = p or b = p).  Hence
  E = sum_P (r - 1) + sum_N (b - 1) <= (2p - 1 - |P|) + (2kappa - 2|N|) = 2p - 1 + 2kappa - R - |N| = k - 1 - |N|.
Step 5.  If E = 0 every rotation is rho_c or rho_-c.  Otherwise eta >= 1, eta <= E/2 <= (k-1)/2 and
a_max <= E + 1 <= k.  (H): 2H >= 2p - 2k >= k - 1 >= E (by (F)).  (K): 2p - eta - a_max - 1 >= 2p - (k-1)/2 - k - 1
>= k, i.e. 4p >= 5k + 1, implied by (F).  Theorem SHgen gives w^ an identity 2p-subword, contradicting PM*.  []

## 7. Coverage (computed 06:35:53 from (F), p >= 5)

Largest k per prime: p = 5: 2; 7: 3; 11: 5; 13: 6; 17: 7; 19: 8; 23: 10; 29: 12; 31: 13; 37: 15; 41: 17; 43: 18;
47: 19; 53: 22; 59: 24; 61: 25; 67: 27; 71: 29; 73: 30; 79: 32; 83: 34; 89: 36; 97: 39; 101: 41; 103: 42; 107: 43;
109: 44.  Least prime per k: k = 2: 5; 3: 7; 4, 5: 11; 6: 13; 7: 17; 8: 19; 9, 10: 23; 11, 12: 29; 13: 31; 14, 15: 37.
With the accepted ROT-o<=4 (p >= 7) and ROT-o3 (p >= 5): conditional on SHgen, ROT holds for constant-run avoiders
with at most 5 odd blocks for p = 11, at most 6 for p = 13, at most 7 for p = 17, at most 8 for p = 19, and at most
(2p+4)/5 in general.  Finite-exact aids (not premises): the classifier frontier in results-v2.md (p = 7: o <= 7;
11, 13: o <= 6; 17: o <= 5); code/check_rotfew_v1.py and code/check_rotfew_v2.py (README entries 06:18:43, 06:27:42).

## 8. Scope and non-claims

Covered (conditional on SHgen-v2, unreviewed): constant-run avoiders of length 4p-2 with o odd blocks, p >= 5 prime,
5o <= 2p + 4.  Not covered: o > (2p+4)/5; p = 5 beyond o = 3 (separate finite claim); non-constant reflection runs
(REFL, reflection slice).  In this route (F) is used by WT (b) (G >= 2kappa + w_+); MULT needs only 2p >= 3e + 2,
EXTRACT 4kappa <= 2p, and SHgen 2p >= 3k - 1 and 4p >= 5k + 1.  This is not ROT(p), INV*(p) or ordered Olson; no
novelty claim (Scherk's lemma and the layer argument are classical tools, proved here in full rather than imported).
