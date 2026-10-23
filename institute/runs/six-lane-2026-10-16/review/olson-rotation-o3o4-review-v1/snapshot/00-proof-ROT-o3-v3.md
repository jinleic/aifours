# ROT for avoiders with exactly three odd constant blocks (all primes p >= 5), v3 (self-contained)

Owner OlsonRotationRigidity.  Written after host clock 2026-10-18T03:0x-07:00.  Status [W], UNREVIEWED.
Supersedes proof-ROT-o3-v2.md (2c02086c...7ae0, kept unchanged) and v1 (0ab9ae7d...cfea, kept; its memory-only
Savchev-Chen import is superseded).  Changes from v2: (1) Lemma INC step (c), case n >= 2, repaired as suggested by the
parent (v2 line 31 claimed "m+6 = 2p+1 forces n = 4-e <= 1", false for e <= 2); (2) Proposition K2' is written out in
full here instead of being imported by reference from v1.
Imports: proof-ROT-lowodd-v1.md (sha256 8ba3e6c7...9785): Lemma GRX (notes-GRX-v1.md), EGZ, pairs bound, (D), (Z1),
(Z2), Lemma PM*; Davenport-alpha (olson/proof-dihedral-partial.md Sec. 4, reviewed; parent erratum m4: N <= 4p-1,
F >= 2, frame at a gap outside I; its H may count every second interior gap of each constant block, as in GR0 (d)).
Notation: Y(x) = (1, x) in Z_2 x Z_p = Z_(2p); "odd" = first coordinate 1; zero-sums have even length.

## 0. Lemma INC

Let p >= 5 and Y a zero-sum-free sequence of odd elements of Z_(2p) of length L = 2p-1-e, 0 <= e <= 3.  Then Y = g^L
with g a generator, or e >= 2 and Y = g^(L-1)(3g).
Proof.  For an ordering y_1..y_L let A_0 = {0}, A_t = A_(t-1) u (A_(t-1) + y_t), delta_t = |A_t| - |A_(t-1)|.
(a) delta_t >= 1: else A_(t-1) + y_t lies in A_(t-1), so A_(t-1) contains 0, y_t, 2y_t, ..., hence -y_t, which is 0 or a
    subsequence sum of y_1..y_(t-1): a zero-sum.  As |A_L| <= 2p, sum (delta_t - 1) <= 2p-1-L = e <= 3 ("extras").
(b) At most two distinct values: put three distinct values a, b, c first.  A_2 = {0, a, b, a+b} (a+b even, nonzero);
    A_2 + c = {c, a+c, b+c, a+b+c} is disjoint from A_2 (c != a, b; a+b+c = a or b gives a zero-sum pair; a+c, b+c are even,
    nonzero, and a+c = a+b iff c = b, b+c = a+b iff c = a).  Deltas 1, 2, 4: extras 4 > 3.
(c) Y = a^m b^n, m >= n >= 1.  L >= 6 gives m >= 3; a = (1,0) would make a a a zero-sum, so a is a generator; b = d a with
    d odd, 3 <= d <= 2p-1.  Order a^m first: A = {0, a, ..., m a}, deltas 1.  First b:
    - if 2p-d <= m, b a^(2p-d) is a zero-sum;
    - if d <= m: m+d >= 2p would give the previous case, so A + b = {d a, ..., (m+d) a} adds d new sums, extras d-1 <= 3,
      d = 3;
    - otherwise b + i a = j a (0 <= i, j <= m) is impossible, A + b is disjoint from A, extras m >= ceil(L/2) >= p-2 > 3
      unless p = 5, e = 3, m = n = 3.  In that case order b a a a b b: deltas 1, 2, 2, 2 (each a adds two new sums by
      the same parity checks as in (b), using b != 3a, -3a), then the fifth letter adds 2b + i a (i = 0..3), none in the
      current set (2b + i a = j a forces 2d = j - i in [-3, 3] mod 10, so b in {a, -a, (1,0)}, all impossible;
      2b + i a = b + j a forces b = (j-i) a, excluded), so extras >= 6.
    So b = 3a.  If n >= 2: when m+6 >= 2p, the subsequence b b a^(2p-6) is a zero-sum (2p-6 >= 0 and 2p-6 <= m); so
    m+6 < 2p, A = {0, ..., (m+3) a} after the first b, and the second b adds the three new sums (m+4)a, (m+5)a, (m+6)a:
    extras >= 2 + 2 > 3.  Hence n = 1, Y = a^(L-1)(3a), extras 2 <= e.  []
Remark: (1,0) = p g for every generator g, and p g is neither g nor 3g (p != 1, 3 mod 2p).

## 1. Lemma DEL

If w (length 4p-2) avoids and has exactly three odd blocks, delete one reflection from one odd block (subwords of
avoiders avoid; a block of length 1 disappears and its two runs form one run of the representation) and apply Lemma
PM* across every even block.  The result w2 avoids, has length 4p-3, the same rotation multiset, and a representation
X_1 S_1 X_2 S_2 with l_1, l_2 odd.  []

## 2. Proposition K2'

If w2 = X_1 S_1 X_2 S_2 (cyclic, l_1, l_2 odd, length 4p-3) avoids, then X_1 + X_2 lies in {c, -c}, c != 0.
Proof.  F = 2H+2, H <= p-1 (pairs), kappa := p-1-H >= 0, R = 2p-3+2kappa.  Davenport-alpha gives R + H <= 3p-2, so
kappa <= 2.  Y := Y(X_1 + X_2), Y^- := Y(X_1) + Y(-X_2), theta := theta_1.  GRX gives:
(ZP) z = (+,+): Phi = 0, delta = 2, C_max = 2H: Y has no zero-sum with length in [2kappa+2, 2p];
(AP) z = (+,-): Phi = 2, delta = 0, C_max = 2H+2: no sub-multiset of Y^- of even size m in [2kappa, 2p-2], m <= R,
     has value sum theta.
By (ZP) every zero-sum of Y of length <= 2p has length <= 2kappa.
kappa = 0.  Y is zero-sum-free of length 2p-3; by INC (e = 2) Y = g^(2p-3) (rigid) or g^(2p-4)(3g).  In the latter
case normalise g = (1,1) (automorphism v -> v/c on all letters).  X_1 holds alpha copies of rho_1 and X_2 holds
beta = 2p-4-alpha; s = +1 if rho_3 lies in X_1, else s = -1.  (AP) with even m in [0, 2p-4]:
 (i) every even t in [-beta, alpha] is a value sum (q+ - q- = t, m = |t|);
 (ii) 3s + t' for every odd t' in [-beta, alpha] is a value sum (m = 1 + |t'| <= 2p-4).
alpha even: (i) is p-1 consecutive even integers, missing only the residue of alpha+2; (ii) contains the even integers
of [4-beta, alpha+2] (s = +1) or of [-beta-2, alpha-4] (s = -1, where -beta-2 = alpha+2-2p): the missing residue is hit.
alpha odd: (i) is the p-2 even integers of [1-beta, alpha-1], missing the residues of alpha+1, alpha+3; (ii) contains
the even integers of [3-beta, alpha+3] (s = +1) or of [-3-beta, alpha-3] (s = -1; -3-beta = alpha+1-2p,
-1-beta = alpha+3-2p): both are hit.  So theta is a value sum: w2 does not avoid.
kappa = 1.  |Y| = 2p-1; zero-sums of length <= 2p are pairs; two disjoint ones give a length-4 zero-sum, so they pairwise
intersect: none, a star through one position u, or a triangle (three copies of (1,0)).  None: Y = g^(2p-1) by (Z1).
Star: Y - u is zero-sum-free of length 2p-2, = g^(2p-2) by (Z2), and u pairs with g: Y = g^(2p-2)(-g).  Triangle: Y minus
two copies of (1,0) is zero-sum-free of length 2p-3 containing (1,0), impossible by INC (e = 2) and the Remark.
kappa = 2.  |Y| = 2p+1; zero-sums of length <= 2p have length 2 or 4, and two disjoint zero-sums of total length >= 6
are excluded.  (D) gives a zero-sum Z of length 2 or 4 in Y; Y' := Y - Z.
 |Z| = 2, Z = {u, -u}: zero-sums of Y' (length 2p-1) are pairs and pairwise intersect (else total length 6 with Z), so as
 for kappa = 1, Y' = g^(2p-1) or g^(2p-2)(-g).  If u in {g, -g}: Y' = g^(2p-1) gives g^(2p) in Y (excluded), Y' =
 g^(2p-2)(-g) gives Y rigid.  Otherwise u = a g, a odd in [3, 2p-3], and u g^(2p-a) is a zero-sum of length 2p-a+1 in
 [4, 2p-2]; it must be 4, so u = -3g, -u = 3g, and (3g) g^(2p-3) is a zero-sum of length 2p-2 >= 8: excluded.
 |Z| = 4: Y' (length 2p-3) is zero-sum-free (a zero-sum there, of length 2 or 4, plus Z has length 6 or 8 <= 2p), so
 Y' = g^(2p-3) or g^(2p-4)(3g) by INC, and #g >= 2p-4.  For h in Z, h != g, h = a g: if 2p-a <= #g, h g^(2p-a) is a
 zero-sum of length <= 2p-2, hence <= 4, so h in {-g, -3g}; otherwise a = 3 and #g <= 2p-4.  If 3g occurs in Y,
 (3g) g^(2p-3) is excluded, so #g <= 2p-4 and Z has no g.  Weights g -> 1, -g -> -1, -3g -> -3, 3g -> 3: Z is a zero-sum
 of length 4, so its weight sum W lies in [-12, 12] and W = 0 mod 2p.
  Y' = g^(2p-3): Z within {g, -g, -3g}.  W = 0: Z = g^2(-g)^2 (Y rigid) or g^3(-3g) (#g = 2p: excluded).  W = -10
  (p = 5): Z = (-g)(-3g)^3, and (-3g)^2 g^6 is a zero-sum of length 8: excluded.
  Y' = g^(2p-4)(3g): Z within {-g, -3g, 3g}.  W = 0: Z = (-3g)^2(3g)^2 (excluded by (-3g)^2 g^6, length 8, 6 <= 2p-4
  copies) or (-g)^3(3g) (excluded by (3g)^2 g^(2p-6), length 2p-4 >= 6).  W = +-10 (p = 5): only Z = (-g)(-3g)^3,
  excluded by (-3g)^2 g^6.
In every case Y lies in {g, -g} with g = (1, c): all rotation values lie in {c, -c}.  []

## 3. Theorem ROT-o3

For every prime p >= 5, every avoider of length 4p-2 over D_(2p) with exactly three odd maximal constant reflection
blocks has all rotation letters in one {rho_c, rho_-c}, c != 0.  Proof: Lemma DEL, then Proposition K2'.  []
With Corollary ROT-o2 (lowodd-v1): ROT holds for every avoider with at most three odd blocks.

## 4. Finite-exact aids (not premises)

As in v2 Sec. 4 (code/kblock_exact_v1.py, v2.py; out/kblock*.jsonl): no non-rigid avoider in S(2, 4p-3), S(3, 4p-2)
at p = 5, 7; S(2, 4p-4) fails (K2' is sharp in length).
