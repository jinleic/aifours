# Theorem ROT-FEW: ROT for avoiders with few odd constant blocks (o roughly <= 1 + sqrt(2p-2)), v1

Owner OlsonRotationRigidity.  Written after host clock 2026-10-18T06:15:09-07:00.  Status [W], UNREVIEWED.
CONDITIONAL on Theorem SHgen (proof-SHgen-v2.md, unreviewed).  Uniform in kappa; uses only the all-plus pattern (ZP)
for the structure of the rotation multiset, then SHgen.  Covers o = 5 for every prime p >= 11.
Imports: GRX, Lemma PM*, (D) [R/olson-rotation-lowodd-parent-verdict-v2.md, 0853f4ac...ba29]; Lemma INC parts (a) and
(b) [proof-ROT-o3-v3.md, parent-accepted R/olson-rotation-o3o4-parent-verdict-v1.md; parts (a), (b) do not use INC's
length hypothesis]; Davenport-alpha instance (V) and the form of SHgen-v2 Sec. 0 (with its erratum-m4 citation);
Theorem SHgen (SHgen-v2 Sec. 1).
Notation.  Y(x) := (1, x) in Z_2 x Z_p = Z_(2p); elements with first coordinate 1 are "odd".  (1,0) has order 2; every
other odd element generates Z_(2p), and for an odd generator g the odd elements are exactly the r g, r odd in
[1, 2p-1].  For a sequence S, A(S) := {0} u {nonempty subset sums}; S is zero-sum-free if 0 is not a nonempty subset
sum; extras(S) := |A(S)| - 1 - |S|.  Zero-sums of odd elements have even length.
INC (a): for a zero-sum-free S and ANY ordering, each new term adds >= 1 new element to A; so extras(S) >= 0 equals the
sum of (new elements - 1) over any ordering, and |A(S)| <= 2p gives extras(S) <= 2p - 1 - |S|.
INC (b): three distinct values x, y, z of a zero-sum-free sequence have |A(x y z)| = 8.

## 1. Lemma GROW

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

## 2. Lemma MULT

Let Y' be a zero-sum-free sequence of odd elements of length L, e := 2p - 1 - L, d its number of distinct values, m its
largest multiplicity, attained by the value g.
 (i)   If d >= 3 then d <= e - 1.
 (ii)  If m >= max(2, e + 1) then g is a generator and Y' = g^m (d_1 g) ... (d_q g) with odd integers d_j >= 3 and
       sum_j (d_j - 1) <= e; in particular q <= e/2.
 (iii) If p >= 7 and 2p >= e^2 + 2 then m >= max(2, e + 1).
Proof.  (i) Put one copy of each value first (the set D), then the rest: e >= extras(Y') >= |A(D)| - 1 - d.  If
|A(D)| >= 2p - 1: D holds at most one of x, -x for each odd x and (1,0) at most once, so d <= (p+1)/2 and
|A(D)| >= 2p - 1 >= 2d + 2.  Otherwise every subset of D has |A| <= 2p - 2; removing by Lemma GROW, one at a time,
an element whose removal lowers |A| by >= 2 until three remain, and using INC (b), |A(D)| >= 8 + 2(d-3) = 2d + 2.
Either way e >= d + 1.
(ii) g = (1,0) would make g g a zero-sum, so m <= 1; hence g is a generator.  Put g^m first: A = {0, g, ..., mg}
(m+1 distinct elements, no zero-sum).  Add the other terms in any order; before each addition A = {0, g, ..., Mg} with
M >= m and M <= 2p - 2.  The next term is b = d g with d odd in [3, 2p-1].  If d + M >= 2p, then (2p - d)g, with
1 <= 2p - d <= M, is a nonempty subset sum of earlier terms and with b gives a zero-sum: impossible.  So d + M <= 2p - 1
and A + b = {dg, ..., (d+M)g} without wrap-around.  If d >= M + 2 all M + 1 of these are new: extras >= M >= m > e,
impossible.  So d <= M + 1, exactly d sums (M+1)g, ..., (M+d)g are new (extras d - 1), and A becomes {0, ..., (M+d)g}.
Summing, sum_j (d_j - 1) <= e.
(iii) If d <= 2: m >= L/2 = (2p - 1 - e)/2 >= e + 1 because 2p >= 3e + 3 (for e <= 3 as 2p >= 14; for e >= 4 as
e^2 + 2 >= 3e + 3), and m >= L/2 >= 2.  If d >= 3: by (i) e >= 4 and d <= e - 1, so m >= L/(e-1) > e because
L = 2p - 1 - e > e(e-1) is 2p > e^2 + 1.  []

## 3. Lemma EXTRACT

Let Y be a sequence of odd elements and kappa >= 0 with 4kappa <= 2p such that
  (ZP) Y has no zero-sum subsequence of length in [2kappa + 2, 2p].
Then Y = Z Y' with Z a zero-sum subsequence (possibly empty), |Z| <= 2kappa, and Y' zero-sum-free.
Proof.  Take a maximal family of pairwise disjoint minimal zero-sum subsequences Z_1, ..., Z_q.  By (D) a minimal
zero-sum subsequence has length <= 2p (any 2p of its terms would contain a nonempty zero-sum subsequence), hence
<= 2kappa by (ZP).  If |Z_1| + ... + |Z_q| >= 2kappa + 2, the least j with |Z_1| + ... + |Z_j| >= 2kappa + 2 gives a
zero-sum Z_1 ... Z_j of length <= 2kappa + 2kappa <= 2p (lengths are even): contrary to (ZP).  So Z := Z_1 ... Z_q has
|Z| <= 2kappa, and Y' := Y - Z is zero-sum-free by maximality.  []

## 4. Lemma WT (weight bounds)

Let Y satisfy (ZP) for some kappa >= 0 with 4kappa <= 2p, and let g be an odd generator of multiplicity G in Y.
Every term h != g of Y is h = r g with r odd in [3, 2p-1].
 (a) If 2p - r <= G then b := 2p - r <= 2kappa - 1.  Call such h NEGATIVE of weight b (h = -b g); otherwise h is a
     POSITIVE heavy of weight r, and r <= 2p - G - 1.  g is positive of weight 1.  P, N: the positive / negative terms;
     w_+ := the largest weight in P.
 (b) G <= 2p - 1; and if G >= 2kappa + w_+ then sum_(h in P) r_h <= 2p - 1.
 (c) If G >= 4kappa - 1 then sum_(h in N) (b_h + 1) <= 2kappa.
Proof.  (a) h g^(2p-r) is a zero-sum of length 2p - r + 1 in [2, 2p-2], so 2p - r + 1 <= 2kappa.
(b) g^(2p) would be a zero-sum of length 2p.  Suppose sum_P r >= 2p; then P has heavies.  Add positive heavies one at a
time until their weight sum s first reaches 2p - G; I := those added (|I| >= 1), s <= 2p - G - 1 + w_+ <= 2p.  Then
I g^(2p-s) (0 <= 2p - s <= G) is a zero-sum of length |I| + 2p - s, which is <= 2p (|I| <= s) and
>= 1 + 2p - (2p - G - 1 + w_+) = G + 2 - w_+ >= 2kappa + 2: contrary to (ZP).
(c) Suppose sum_N (b+1) >= 2kappa + 2; take the shortest prefix S (any order) with sum_S (b+1) >= 2kappa + 2.  Since
b + 1 <= 2kappa by (a) and the shorter prefix has sum <= 2kappa, sum_S (b+1) <= 4kappa <= 2p, and sum_S b <= 4kappa - 1
<= G.  S g^(sum_S b) is a zero-sum of length sum_S (b+1) in [2kappa + 2, 2p]: contrary to (ZP).  []

## 5. Theorem ROT-FEW

**Theorem ROT-FEW.**  Let p >= 7 be prime and k >= 2 an integer with
  (F1) 2p >= (k-1)^2 + 2,   (F2) 4p >= 11(k-1),   (F3) 2p >= 5k - 4,   (F4) p >= 2k - 1.
Assume Theorem SHgen (proof-SHgen-v2.md).  Then every avoider of length 4p-2 over D_(2p) whose maximal cyclic
reflection runs are all constant, exactly k of them of odd length, has all rotation letters in one set
{rho_c, rho_-c}, c != 0.
Proof.  If R = 0 there is nothing to prove; F >= k >= 2.  Consecutive maximal reflection runs are separated by
nonempty rotation runs.  Iterated Lemma PM* gives an avoider w^ of length 4p-2 with the same rotation multiset, k odd
constant blocks and nonempty runs (merged runs contain nonempty runs): the form of SHgen-v2 Sec. 0.  For w^:
R = 2p + 2kappa - k, 0 <= kappa <= k - 1 by (V), H = p - 1 - kappa >= p - k.
Step 1.  Y := the sequence of Y(x) over the rotations satisfies (ZP) (SHgen-v2 Sec. 0).  4kappa <= 4k - 4 <= 2p by (F4).
EXTRACT: Y = Z Y', |Z| <= 2kappa, Y' zero-sum-free of length L >= R - 2kappa = 2p - k, so e := 2p - 1 - L <= k - 1.
Step 2.  2p >= (k-1)^2 + 2 >= e^2 + 2 and p >= 7, so MULT (iii), (ii): the most frequent value g of Y' is a generator
and Y' = g^m (d_1 g) ... (d_q g) with q <= e/2.  Hence G := multiplicity of g in Y satisfies
G >= m = L - q >= L - e/2 = (3L - 2p + 1)/2 >= (4p - 3k + 1)/2.
Step 3.  By WT (a) every positive heavy has weight <= 2p - G - 1 <= (3k-3)/2, so w_+ <= max(1, (3k-3)/2) and
G >= 2kappa + w_+ (as (4p - 3k + 1)/2 >= 2k - 2 + (3k-3)/2 is 4p >= 10k - 8, i.e. (F3)); and G >= 4kappa - 1 (as
(4p - 3k + 1)/2 >= 4k - 5 is (F2)).  WT (b), (c): sum_P r <= 2p - 1 and sum_N (b+1) <= 2kappa.
Step 4.  g = Y(c) with c != 0, and r g = Y(rc).  Positive heavies have 3 <= r <= (3k-3)/2 <= p - 2 and negatives have
1 <= b <= 2kappa - 1 <= 2k - 3 <= p - 2 (by (F4)); so relative to c each rotation has SHgen weight b_x = r or -b,
lights are exactly g and -g, and no rotation is rho_0 (Y(0) = p g would need r = p or b = p).  Hence
  E = sum_P (r - 1) + sum_N (b - 1) <= (2p - 1 - |P|) + (2kappa - 2|N|) = 2p - 1 + 2kappa - R - |N| = k - 1 - |N|.
Step 5.  If E = 0 every rotation is rho_c or rho_-c.  Otherwise eta >= 1, eta <= E/2 <= (k-1)/2 and
a_max <= E + 1 <= k.  (H): 2H >= 2p - 2k >= k - 1 >= E (by (F4)).  (K): 2p - eta - a_max - 1 >= 2p - (k-1)/2 - k - 1
>= k, i.e. 4p >= 5k + 1, implied by (F3).  Theorem SHgen gives w^ an identity 2p-subword, contradicting PM*.  []

## 6. Coverage (computed 06:15:09 from (F1)-(F4) and p >= 7)

Least prime p per k: k = 2, 3: 7; k = 4, 5: 11; 6: 17; 7: 19; 8: 29; 9: 37; 10: 43; 11: 53; 12: 67; 13: 73.
Largest k per prime: p = 7: 3; 11, 13: 5; 17: 6; 19, 23: 7; 29, 31: 8; 37, 41: 9; 43, 47: 10; 53, 59, 61: 11;
67, 71: 12; 73, 79, 83: 13; 89, 97: 14; 101-109: 15.  For k >= 7 the binding condition is (F1).
With the accepted ROT-o<=4 (p >= 7) and ROT-o3 (p >= 5): conditional on SHgen, ROT holds for constant-run avoiders
with at most 5 odd blocks for every prime p >= 11.  Finite-exact aids (not premises): the classifier frontier
(results-v2.md) found no non-rigid avoider at p = 7 (o <= 7), 11, 13 (o <= 6), 17 (o <= 5), consistent with the table.

## 7. Scope and non-claims

Covered (conditional on SHgen-v2, unreviewed): constant-run avoiders of length 4p-2 with o odd blocks, p >= 7 and
(F1)-(F4).  Not covered: o above the table (roughly o > 1 + sqrt(2p-2), where MULT (iii) fails), p = 5 (separate finite
claim), non-constant reflection runs (REFL, reflection slice).  The only obstruction to larger o in this route is
MULT (iii): a zero-sum-free sequence of length 2p - o must have a value of multiplicity >= o; Steps 3-5 need only
o <= about 4p/11.  This is not ROT(p), INV*(p) or ordered Olson; no novelty claim.
