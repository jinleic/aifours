# The kappa = 0 and kappa = 1 slices: ROT and INV* for 3 o_F <= 2p + 1, v2

Owner OlsonRotationRigidity.  Written after host clock 2026-10-18T07:09:07-07:00.  Status [W], UNREVIEWED.
v2 supersedes proof-KAPPA01-v1.md (sha256 adbee100...fbb4, kept unchanged, never sent for review).  Changes:
(1) ERROR in v1 fixed: v1's Proposition K1 claimed 3k <= 2p + 4, but its triangle case (iii) applies Lemma MULT with
e = k - 1, which needs 3k - 1 <= 2p; K1 is now stated for 3k <= 2p + 1 (and p >= 5), where every case is valid.
(2) The normal form is cited from proof-ROT-few-E-v2.md (its terminal one-even-block case is excluded there).
(3) REFL-few-odd is cited in its review version r2 (reflection/proof-REFL-fewodd-r2.md, sha256
db16274fffccde41e65025a46c4992bb3c11c26bce9bcc97f5bc3efaae65c2c6; same statement and proof as r1).  (4) The corollary is
stated for 3 o_F <= 2p + 1 on both slices.  No other change.
CONDITIONAL on Theorem SHgen (proof-SHgen-v2.md 8fde88c0...d239; Codex round-B ACCEPT) and, for non-constant
reflection runs and for the INV* conclusion, on Corollary REFL-few-odd (r2, [W]).
Imports: the normal form (Sec. 0) and Lemma SHgen-E of proof-ROT-few-E-v2.md; the REFL interface of
proof-INVstar-few-v1.md (026753c9...16bc4); Lemma MULT (ii), (iii) of proof-ROT-few-v3.md (5f158d69...efaa; Codex
round-B ACCEPT); GRX, PM*, K1, (D) (accepted); Davenport-alpha instance (V).
Intrinsic parameters of an avoider w: o := o_F(w) (odd maximal constant reflection blocks), kappa(w) := p - 1 - (F - o)/2.
The normal form w^ (ROT-few-E-v2 Sec. 0) has 1 <= k <= o blocks, k = o mod 2, all odd (the one-even-block ending is
impossible), and kappa(w^) = p - 1 - (F - k)/2 <= kappa(w), kappa(w^) >= 0; so kappa(w) = 0 forces k = o and
kappa(w^) = 0, and kappa(w) = 1 gives kappa(w^) = 1 with k = o, or kappa(w^) = 0 with k = o - 2.  If k = 1,
Proposition K1 makes all rotations equal; so let k >= 2 below.

## 1. Proposition K0 (kappa = 0)

Let p >= 5 be prime and w an avoider of length 4p-2 with kappa(w^) = 0 and 3k <= 2p + 1.  Then the rotations of w lie
in one {rho_c, rho_-c}, c != 0 [SHgen; REFL-few-odd if w^ has an empty run].  If moreover w has constant runs, all its
rotations are equal without SHgen (Corollary ELT0-FEW, proof-ELT0-FEW-v2.md; Codex round-B ACCEPT).
Proof.  R = 2p - k.  With kappa = 0 the all-plus pattern forbids every zero-sum of length in [2, 2p], so Y (the
rotation sequence, length L = R) is zero-sum-free and e := 2p - 1 - L = k - 1.  As 3e + 2 = 3k - 1 <= 2p, MULT gives a
generator g = Y(c) with Y = g^m (d_1 g) ... (d_q g), d_j odd >= 3, sum (d_j - 1) <= k - 1.  Relative to c every heavy
is positive of weight d_j <= k <= p - 2 (3k <= 2p + 1 gives k <= p - 2 for p >= 7, and k <= 3 = p - 2 for p = 5), no
rotation is rho_0 (that would need d_j = p), and E <= k - 1, eta <= (k-1)/2, a_max <= k.  (H): 2H = 2p - 2 >= E.
(K): 2p - eta - a_max - 1 >= 2p - (k-1)/2 - k - 1 >= k because 5k <= 4p - 1 (from 3k <= 2p + 1, p >= 4).  If E >= 2,
Theorem SHgen (all runs of w^ nonempty) or Lemma SHgen-E (some run of w^ empty; its REFL instance has
o_F = k <= p, supplied by REFL-few-odd as in proof-INVstar-few-v1.md) gives w^ an identity 2p-subword: contradiction.
So E = 0.  []

## 2. Proposition K1 (kappa = 1)

Let p >= 5 be prime and w an avoider of length 4p-2 with kappa(w^) = 1 and 3k <= 2p + 1.  Then the rotations of w lie
in one {rho_c, rho_-c}, c != 0 [SHgen; REFL-few-odd if w^ has an empty run].
Proof.  R = 2p + 2 - k.  The all-plus pattern forbids zero-sums of length in [4, 2p], so every zero-sum of Y of length
<= 2p is a pair {u, -u}, and two such pairs intersect (two disjoint ones would give length 4).  Pairwise intersecting
pairs of positions form: (i) nothing, (ii) a star (all pairs share one position c0), or (iii) a triangle (three
positions pairwise opposite: three copies of (1,0); a fourth copy would give two disjoint pairs, and any other pair
would have to meet all three edges).  Removing at most two positions as below leaves a zero-sum-free sequence (a
zero-sum would contain a minimal one of length <= 2p by (D), i.e. a pair avoiding the removed positions).
 (i) Y is zero-sum-free, so R <= 2p - 1, k >= 3, e = k - 3, 3e + 2 = 3k - 7 <= 2p: MULT gives Y = g^m (d_j g) with
     sum (d_j - 1) <= k - 3.
 (iii) Y minus two copies of (1,0) is zero-sum-free of length 2p - k, e = k - 1, 3e + 2 = 3k - 1 <= 2p; MULT puts the
     remaining (1,0) = p g among the d_j g, so p <= e + 1 = k, contradicting 3k <= 2p + 1.
 (ii) Y' := Y - c0 is zero-sum-free of length 2p + 1 - k, e = k - 2, 3e + 2 = 3k - 4 <= 2p: Y' = g^m' (d_j g) with
     sum (d_j - 1) <= k - 2, so m' >= (2p + 1 - k) - (k - 2)/2.  c0 = -v for some v = d g in Y' (d = 1 or a d_j), and
     d <= k - 1 <= m' (2.5k <= 2p + 3 follows from 3k <= 2p + 1), so c0 g^d is a zero-sum of length d + 1 <= 2p: it is
     a pair, d = 1, c0 = -g.
In cases (i), (ii), relative to c (g = Y(c)) the lights are g and at most one -g, every heavy is a positive d_j g with
d_j <= k - 1 <= p - 2 (k <= (2p+1)/3 <= p - 1), no rotation is rho_0, E <= k - 2, eta <= (k-2)/2, a_max <= k - 1.
(H): 2H = 2p - 4 >= E.  (K): 2p - eta - a_max - 1 >= 2p - (k-2)/2 - k >= k because 5k <= 4p + 2, which follows from
3k <= 2p + 1.  If E >= 2, SHgen or SHgen-E (as in Proposition K0) contradicts avoidance; so E = 0.  []

## 3. Corollary (INV* on the two slices)

Conditional on SHgen and REFL-few-odd: every avoider w of length 4p-2 (p >= 5 prime) with kappa(w) in {0, 1} and
3 o_F(w) <= 2p + 1 is RGR.
Proof.  If kappa(w^) = kappa(w), use Proposition K0 or K1 with k = o.  If kappa(w) = 1 and kappa(w^) = 0, then
k = o - 2 and 3k <= 2p - 5, so Proposition K0 applies.  Hence the rotations lie in one {rho_c, rho_-c}.  As
o_F(w) <= (2p+1)/3 <= p, REFL-few-odd makes every maximal cyclic reflection run of w constant.  []

## 4. Scope

* Extends INV*-FEW (5 o_F <= 2p + 4) on these slices to 3 o_F <= 2p + 1.
* The limit here is Lemma MULT (iii) (2p >= 3e + 2).  For kappa = 0 the full slice (o_F <= p) would follow, for
  constant runs and without SHgen, from ELT0 and a Savchev-Chen structure lemma for zero-sum-free odd sequences of
  length >= p in Z_(2p); an experiment (README 06:59) found that lemma true at p <= 13 and false at length p - 1.  An
  upward induction (remove one term; a "jump" would need W' <= p - 1 < W') reduces it to length exactly p, which is
  open here.
* Observation [O]: the listed avoiders at p = 5, 7 have kappa in {0, o_F - 1}; kappa = 1 occurs there only with o_F = 2.
* Not INV*(p); not ordered Olson; no novelty claim.
