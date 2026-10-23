# ROT for avoiders with at most two odd constant blocks (all primes p >= 5)

Owner OlsonRotationRigidity.  Written after host clock 2026-10-18T02:28:15-07:00.  Status [W], UNREVIEWED.
Uses: Lemma GRX (notes-GRX-v1.md, this directory, [W] unreviewed; it generalises the reviewed Lemma GR); EGZ
(olson/proof-dihedral-partial.md Sec. 1, reviewed); the elementary "pairs" bound (p disjoint equal adjacent pairs
sigma_y sigma_y inside constant blocks give an identity 2p-subword).  No finite computation is a premise.
This proves only a SUBCLASS of ROT(p) (half (a) of INV*(p)); it says nothing about reflection constancy and
nothing about ordered Olson.

## 0. Setting

Conventions of notes-GRX-v1.md.  w has length N = 4p-2, F reflections, R rotations, maximal constant reflection
blocks S_1..S_k (k >= 1 if F >= 1) with lengths l_i, rotation multisets X_1..X_k (possibly empty).  o := number of
odd blocks.  Z_(2p) = Z_2 x Z_p (CRT); to a rotation value x attach Y(x) := (1, x) in Z_2 x Z_p.  A subsequence of
Y = (Y(x))_(x in X) is zero-sum iff it has EVEN length and value sum 0 mod p.  Facts used about Z_n:
(D) every sequence of n elements of Z_n has a nonempty zero-sum subsequence (pigeonhole on partial sums);
(Z1) a zero-sum-free sequence of length n-1 in Z_n is g^(n-1) with g a generator;
(Z2) [n = 2p] a zero-sum-free sequence of length 2p-2 in Z_2 x Z_p all of whose elements have first coordinate 1 is
g^(2p-2), g = (1,c), c != 0.
Proofs.  (Z1): for any ordering the n-1 partial sums are distinct and nonzero, so they are all of Z_n \ {0};
swapping the first two terms changes only the first partial sum, so s_1 = s_2; as any two terms can be put first, all
terms equal some g, and g, 2g, ..., (n-1)g != 0 forces ord(g) = n.  (Z2): for any ordering the 2p-2 partial sums are
distinct and nonzero and their first coordinates alternate 1,0,1,0,...; so the p-1 even-indexed partial sums are
p-1 distinct elements of {(0,y) : y != 0}, i.e. ALL of them.  Swapping the terms in positions 2j, 2j+1 changes only the
partial sum of index 2j, which must again lie in that full set and differ from the other even-indexed partial sums;
so it is unchanged and s_(2j) = s_(2j+1).  Any two terms can be put in positions 2, 3, so all terms are equal, s = g;
g = (1,0) would give the zero-sum g g, so g = (1,c), c != 0.  []

## 1. Lemma PM* (merging across an even block; arbitrary rotations)

Let k >= 2 and S_j an EVEN block.  Let w~ be the word obtained by deleting S_j, merging R_j and R_(j+1) into one run
with multiset X_j + X_(j+1), and lengthening S_(j+1) to sigma_(y_(j+1))^(l_(j+1) + l_j).  Then w~ has the same length,
the same rotation multiset, and k-1 blocks with the same parities except that S_j is gone; if w avoids, w~ avoids.
Proof.  Apply GRX to the given representation of w~ (k-1 blocks; GRX holds for every representation).  A pattern z~
of w~ corresponds to the pattern z of w with z_j = z_(j+1) := z~(merged run).  Then f_j = 0; S_j (even, f_j = 0)
contributes nothing to delta and l_j to F; the lengthened block has the parity and f-value of S_(j+1); hence Phi,
delta, F, C_max agree.  X^z~ = X^z (both merged runs carry the same sign).  The merged run is preceded by S_(j-1) and
followed by the lengthened block, so its theta is y_(j-1) - y_(j+1) = theta_j + theta_(j+1); both are counted in T
iff the common sign is +, so T~(z~) = T(z).  Thus every GRX condition of w~ is one of the conditions of w.  []
Iterating, an avoider with o odd blocks yields an avoider w^ with the same length and rotation multiset and either
k^ = o >= 1 blocks, all odd, or (o = 0) k^ = 1 block, which is even.

## 2. Proposition K1 (one block)

If w avoids and has a single constant block (cyclically w = X sigma_y^F), then F = R = 2p-1 and X = c^(2p-1), c != 0.
Proof.  F >= 1 (else 2p of the R = 4p-2 >= 3p-1 rotations sum to 0, EGZ), F <= 2p-1 (sigma_y^(2p) = 1) and
R <= 3p-2 (EGZ).  Put s := R - (2p-1) in [0, p-1].  For k = 1 the only pattern is z = (+): Phi = 0, T = 0,
C_max = F' := 2 floor(F/2), and GRX says: w avoids iff Y has no zero-sum subsequence whose length m is even with
2p - F' <= m <= 2p.  As F = 2p-1-s, 2p - F' is s+1 (s odd) or s+2 (s even); so
  (*) Y (length 2p-1+s) has no zero-sum subsequence with length in [s+1, 2p].
s = 0: Y has length 2p-1 and every nonempty zero-sum subsequence has length in [1, 2p]; so Y is zero-sum-free and by
(Z1) Y = g^(2p-1); g = (1,c) generates, c != 0.  X = c^(2p-1).
s >= 1: by (*) every nonempty zero-sum subsequence of length <= 2p has length <= s.  Build Z: start Z = empty; while
|Z| <= s-1 the rest has >= 2p elements, so (D) gives a zero-sum U in the rest with 1 <= |U| <= 2p, hence |U| <= s;
Z u U is zero-sum of length <= 2s-1 <= 2p, hence <= s; replace Z by Z u U.  The loop ends with |Z| = s; as zero-sums
have even length, s is even (s odd is already a contradiction).  The rest Y' has length 2p-1; a zero-sum U' in Y'
has |U'| <= s and then Z u U' has length in [s+2, 2s] within [s+1, 2p]; so Y' is zero-sum-free and by (Z1)
Y' = g^(2p-1).  Each h in Z is h = a_h g with a_h odd in [1, 2p-1]; e_h := 2p - a_h; h g^(e_h) is a zero-sum of
length 1 + e_h <= 2p, so 1 + e_h <= s.  Order Z = h_1 ... h_s and let l_i := sum_(j<=i) (1 + e_(h_j)); l_1 <= s and
l_s >= 2s.  For the least i with l_i >= s+1 we have l_i <= 2s <= 2p-2, and h_1 ... h_i g^(l_i - i) (at most 2p-1
copies of g are used) is a zero-sum of length l_i in [s+1, 2p], contradicting (*).  []
(The words rho_c^(2p-1) sigma_y^(2p-1), c != 0, do avoid: m even in [2, 2p-2] and mc = 0 forces p | m.)

## 3. Proposition K2 (two odd blocks)

If w avoids, k = 2 and l_1, l_2 are odd, then X_1 + X_2 is contained in {c, -c} for some c != 0.
Proof.  F = l_1 + l_2 is even; the pairs bound gives H = (F-2)/2 <= p-1, so F <= 2p; EGZ gives R <= 3p-2, so
F >= p, hence F >= p+1.  Put t := (2p - F)/2 in [0, (p-1)/2]; R = 2p-2+2t.  Pattern z = (+,+): Phi = 0, delta = 2,
C_max = F-2, T = 0, so (GRX):
  (**) Y (length 2p-2+2t) has no zero-sum subsequence with length in [2t+2, 2p].
Every nonempty zero-sum of length <= 2p has length <= 2t.  As in K1 build a zero-sum Z: while |Z| <= 2t-2 the rest
has >= 2p elements; the new U has |U| <= 2t and |Z u U| <= 4t-2 <= 2p, hence |Z u U| <= 2t; the loop ends with
|Z| = 2t.  The rest Y' (length 2p-2) is zero-sum-free: a zero-sum U' there has |U'| <= 2t and Z u U' would have length
in [2t+2, 4t] within [2t+2, 2p].  By (Z2) Y' = g^(2p-2), g = (1,c), c != 0.  If Z contains g twice, g^(2p) is a
zero-sum of length 2p, excluded; so Z has at least 2t-1 terms h != g, each h = a_h g with a_h odd in [3, 2p-1];
e_h := 2p - a_h in [1, 2p-3]; h g^(e_h) is a zero-sum of length 1 + e_h <= 2p-2, so e_h <= 2t-1.
t = 0: Y = g^(2p-2).  t = 1: e_h = 1, h = -g = (1,-c); so Y lies in {g, -g}.  t >= 2: there are >= 3 terms h != g;
with l_i as in K1 (over these terms) l_1 <= 2t and the total is >= 2(2t-1) >= 2t+2; the least i with l_i >= 2t+2 has
l_i <= 4t <= 2p and uses l_i - i <= 4t-2 <= 2p-2 copies of g; a zero-sum of length in [2t+2, 2p], contradiction.
So all rotation values lie in {c, -c}.  []

## 4. Corollary ROT-o2

Every avoider of length 4p-2 over D_(2p) (p >= 5 prime) whose maximal constant reflection blocks include at most
two of odd length has all rotation letters in one {rho_c, rho_-c}, c != 0.  (o = 0 is impossible; o = 1: R = 2p-1
equal rotations.)  Proof: F >= 1 by EGZ; Lemma PM* reduces to k^ = o blocks (or one even block), preserving the
rotation multiset and avoidance; apply K1 or K2.  []
Remark (scope).  Blocks are maximal constant pieces, so an avoider with a non-constant reflection run is covered as
long as o <= 2.  The remaining case of ROT(p) is o >= 3 (o odd or even with o = R mod 2).
