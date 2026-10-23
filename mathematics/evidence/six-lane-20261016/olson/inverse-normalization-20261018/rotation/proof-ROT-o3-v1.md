# ROT for avoiders with exactly three odd constant blocks (all primes p >= 5)

Owner OlsonRotationRigidity.  Written after host clock 2026-10-18T02:41-07:00 (exact minute not read).  Status [W],
UNREVIEWED.  Extends proof-ROT-lowodd-v1.md (sha256 8ba3e6c7...9785; notation, (D), (Z1), (Z2), Lemma PM* from there).
Imports: Lemma GRX (notes-GRX-v1.md); EGZ; the pairs bound; Davenport-alpha (olson/proof-dihedral-partial.md Sec. 4,
reviewed, with parent erratum m4: N <= 4p-1, F >= 2, frame at a gap outside I); and the LITERATURE theorem
(SC) Savchev-Chen [S. Savchev, F. Chen, Long zero-free sequences in finite cyclic groups, Discrete Math. 307 (2007)
2671-2679]: a zero-sum-free sequence of length l > n/2 in Z_n has the form (x_1 g) ... (x_l g) with g a generator and
positive integers x_i, x_1 + ... + x_l < n.  It is used only with n = 2p, l = 2p-3 > p.  [I]: (SC) is cited from
memory of the published statement, not re-read in this cycle; the parent should check the statement.
Consequence used: (Z3) a zero-sum-free sequence of length 2p-3 in Z_2 x Z_p whose elements all have first coordinate 1
is g^(2p-3) or g^(2p-4)(3g), g = (1,c), c != 0.  [By (SC) the x_i are odd (first coordinates), sum <= 2p-1 over
2p-3 terms, so at most one x_i equals 3 and the rest are 1.]

## 1. Reduction to two blocks at length 4p-3

**Lemma DEL.**  Let w (length 4p-2) avoid and have exactly three odd blocks.  Delete one reflection from one odd
block (a subword of an avoider avoids; if the block had length 1 it disappears and its two rotation runs become one
run of the representation), then apply Lemma PM* across every even block.  The result w2 avoids, has length 4p-3,
the same rotation multiset as w, and a representation X_1 S_1 X_2 S_2 with l_1, l_2 odd.  []

## 2. Proposition K2' (two odd blocks, length 4p-3)

If w2 = X_1 S_1 X_2 S_2 (cyclic, l_1, l_2 odd, length 4p-3) avoids, then X_1 + X_2 lies in {c, -c}, c != 0.

Proof.  F = l_1 + l_2 = 2H + 2 with H <= p-1 (pairs bound); kappa := p-1-H >= 0; R = 4p-3-F = 2p-3+2kappa.
Davenport-alpha (N <= 4p-1, F >= 2; its H counts every second interior gap of each block, as in GR0 (d)) gives
R + H <= 3p-2, i.e. kappa <= 2.  GRX patterns (Y := Y(X_1 + X_2), Y^- := Y(X_1) + Y(-X_2), theta := theta_1):
  (ZP) z = (+,+): Phi = 0, delta = 2, C_max = 2H: no zero-sum in Y with length in [2kappa+2, 2p];
  (AP) z = (+,-): Phi = 2, delta = 0, C_max = 2H+2: no subsequence of Y^- of length m, m even in [2kappa, 2p-2],
       m <= R, with value sum theta (the first coordinate is automatically 0 = m mod 2).
By (ZP) every zero-sum of Y of length <= 2p has length <= 2kappa.

kappa = 0.  Y is zero-sum-free of length 2p-3, so by (Z3) Y = g^(2p-3) (rigid) or g^(2p-4)(3g).  Exclude the latter:
normalise c = 1 by the automorphism v -> v/c (all letters).  Let X_1 hold alpha copies of rho_1, X_2 hold
beta = 2p-4-alpha copies, and s = +1 if rho_3 lies in X_1, s = -1 otherwise.  In (AP) (m even, 0 <= m <= 2p-4):
 (i) without rho_3: every EVEN t in [-beta, alpha] is a value sum (t = q+ - q-, m = |t|);
 (ii) with rho_3: 3s + t' for every ODD t' in [-beta, alpha] (m = 1 + |t'| <= 2p-4).
If alpha is even, (i) is p-1 consecutive even integers, missing only the residue of alpha+2; (ii) contains
alpha+2 (s = +1: the even integers in [4-beta, alpha+2]) or alpha+2-2p (s = -1: the even integers in
[-beta-2, alpha-4]; note -beta-2 = alpha+2-2p).  If alpha is odd, (i) is p-2 consecutive even integers missing the
residues of alpha+1, alpha+3; (ii) is the even integers in [3-beta, alpha+3] (s = +1) or in [-3-beta, alpha-3]
(s = -1; -3-beta = alpha+1-2p and -1-beta = alpha+3-2p), which contain both.  So every residue is a value sum and
theta is hit: w2 does not avoid.

kappa = 1.  |Y| = 2p-1 and every zero-sum of length <= 2p is a pair; two disjoint zero-sum pairs would give a
zero-sum of length 4, so the pairs pairwise intersect: none, a star (all through one position), or a triangle
(three copies of (1,0)).  None: Y is zero-sum-free of length 2p-1, Y = g^(2p-1) by (Z1).  Star with centre u:
Y - u is zero-sum-free of length 2p-2, = g^(2p-2) by (Z2); u pairs with some element, so u = -g: Y = g^(2p-2)(-g).
Triangle: Y minus two copies of (1,0) is zero-sum-free of length 2p-3 and contains (1,0) = p g, impossible by (Z3)
(p != 1, 3 mod 2p).  So Y lies in {g, -g}.

kappa = 2.  |Y| = 2p+1 and every zero-sum of length <= 2p has length 2 or 4; two disjoint zero-sums with total
length >= 6 are excluded.  By (D) Y has a zero-sum Z of length 2 or 4; Y' := Y - Z.
 |Z| = 2, Z = {u, -u}.  Zero-sums of Y' (length 2p-1) are pairs, pairwise intersecting (else length 6 with Z); as
 for kappa = 1, Y' = g^(2p-1) or g^(2p-2)(-g) (the triangle again contradicts (Z3)).  If u in {g, -g} and Y' = g^(2p-1),
 then g^(2p) lies in Y (length-2p zero-sum), excluded; if u in {g,-g} and Y' = g^(2p-2)(-g), Y is rigid.  Otherwise
 u = a g with a odd in [3, 2p-3] and u g^(2p-a) (at most 2p-3 copies of g) is a zero-sum of length 2p-a+1 in [4, 2p-2];
 it must be 4, so u = -3g and -u = 3g, and (3g) g^(2p-3) is a zero-sum of length 2p-2 >= 8: excluded.
 |Z| = 4.  Y' (length 2p-3) is zero-sum-free (a zero-sum there has length 2 or 4 and with Z gives 6 or 8 <= 2p), so
 Y' = g^(2p-3) or g^(2p-4)(3g) by (Z3), and #g >= 2p-4.  For h in Z, h != g, h = a g (a odd): if 2p-a <= #g then h g^(2p-a)
 is a zero-sum of length <= 2p-2, so <= 4, so h in {-g, -3g}; otherwise a = 3 and #g <= 2p-4.  If 3g occurs in Y then
 (3g) g^(2p-3) is excluded, so #g <= 2p-4 and Z contains no g.  Write the weights of Z (g -> 1, -g -> -1, -3g -> -3,
 3g -> 3); Z is a zero-sum of length 4, so the weight sum W is in [-12, 12] and W = 0 mod 2p.
  Y' = g^(2p-3): Z within {g, -g, -3g}.  W = 0: Z = g^2(-g)^2 (Y = g^(2p-1)(-g)^2, rigid) or g^3(-3g) (then #g = 2p,
  excluded).  W = -10 (p = 5): Z = (-g)(-3g)^3, and (-3g)^2 g^6 is a zero-sum of length 8 in [6, 10]: excluded.
  Y' = g^(2p-4)(3g): Z within {-g, -3g, 3g}.  W = 0: Z = (-3g)^2(3g)^2, excluded by (-3g)^2 g^6 (length 8, uses
  6 <= 2p-4 copies), or Z = (-g)^3(3g), excluded by (3g)^2 g^(2p-6) (length 2p-4 >= 6).  W = +-10 (p = 5): only
  Z = (-g)(-3g)^3, excluded by (-3g)^2 g^6.
So in every case Y lies in {g, -g}, g = (1,c): all rotation values lie in {c, -c}.  []

## 3. Theorem ROT-o3

For every prime p >= 5, every avoider of length 4p-2 over D_(2p) with exactly three odd maximal constant reflection
blocks has all rotation letters in one {rho_c, rho_-c}, c != 0.  Proof: Lemma DEL, then Proposition K2'.  []
With Corollary ROT-o2: ROT holds for every avoider with at most three odd blocks.  Open: o >= 4.
