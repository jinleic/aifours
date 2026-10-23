# Theorem ELT0: the excess-length tradeoff N + E <= 4p-2 when kappa = 0 (any number of odd blocks)

Owner OlsonRotationRigidity.  Written after host clock 2026-10-18T05:27:40-07:00.  Status [W], UNREVIEWED.
A general (all o) result for the slice kappa = 0, under an explicit fullness hypothesis; NOT ROT(p) in general.
Imports: Lemma GRX for any constant-block representation and Lemma PM* (parent-accepted, verdict
R/olson-rotation-lowodd-parent-verdict-v2.md, sha256 0853f4ac...ba29); RGR-LONG(p) (parent-accepted, verdict
R/olson-runs-parent-verdict-v1.md, sha256 82adbddd...9237: every RGR word of length 4p-1 has an identity 2p-subword).

## 1. Setting

p >= 5 prime, w a word of length N <= 4p-2 over D_(2p) with F, R >= 1, given by a cyclic constant-block representation
R_1 S_1 ... R_k S_k in which every block is odd (l_i odd), every run X_i is NONEMPTY and blocks are maximal (so every
maximal cyclic reflection run of w is one constant block: w has "RGR shape").  H := sum_i (l_i - 1)/2 and
kappa := p-1-H.  Fix a generator g = (1, c) of Z_2 x Z_p; each rotation value x has a weight a_x in {1, 3, ..., 2p-1}
with (1, x) = a_x g, i.e. x = a_x c mod p.  W := sum_x a_x, E := W - R (sum of a_x - 1).
(FULL) every integer in [0, W] is the weight sum of some sub-multiset of the rotations.

**Theorem ELT0.**  If kappa = 0, (FULL) holds and w avoids, then N + E <= 4p-2.
**Corollary ELT0-ROT.**  If N = 4p-2, kappa = 0, (FULL) holds and w avoids, then E = 0: every rotation of w is rho_c.
(Any word of RGR shape can first be brought to all-odd blocks by Lemma PM*, which preserves avoidance, N, the
rotation multiset, nonempty runs, maximality and H; so "every block odd" is no restriction for avoiders.)

## 2. Proof

GRX facts for this representation (all blocks odd): for a pattern z with plus-set P, Phi = Phi(z) <= k,
delta = k - Phi, C_max = F - k + Phi = 2H + Phi = 2p - 2 + Phi (kappa = 0), so the admissible rotation counts are the
even m with 2 - Phi <= m <= 2p - Phi; and R = N - F = N - (2p - 2 + k) <= 2p - k <= 2p - Phi.
Step 0 (W <= 2p-1).  If W >= 2p, (FULL) gives a sub-multiset of weight exactly 2p: its value sum is 2p c = 0 mod p,
its size is even (odd weights, even total) and at least 2, and at most R < 2p; it is a zero-sum of length in [2, 2p],
i.e. a solution for the all-plus pattern (Phi = 0, C = 2p - m in [0, 2p-2] = [Phi, C_max]): w would not avoid.
Step 1 (the expanded word).  Let u be w with every rotation x replaced, in place, by a_x copies of rho_c.  u has the
same blocks, nonempty runs and all rotations equal to rho_c, so u is an RGR word; its length is N + E.
Step 2 (u avoids).  u and w use the same representation, so Phi, C_max and T(z) agree for every pattern z.  Suppose u
has an identity 2p-subword with pattern z (plus-set P), C reflections and m = 2p - C rotations: q copies of rho_c
from runs in P and q' from runs not in P, q + q' = m, and (q - q') c = T(z) mod p.  Here 0 <= q <= W_P and
0 <= q' <= W_(not P), where W_P is the total weight of the rotations of w in runs of P.
 If Phi = 0 then P is all runs (z_1 = +), q' = 0, T(z) = 0, so q = 0 mod p with q even and 2 <= q <= W <= 2p-1:
 impossible.  So Phi >= 2.
 Let t = q - q'.  The integer t + W_(not P) lies in [0, W]; by (FULL) choose a sub-multiset S of the rotations of w
 with weight exactly t + W_(not P).  Select in w the rotations U := S cap (runs of P) and V := (runs not in P) minus S.
 Their signed sum in pattern z is (sum_U a - sum_V a) c = (weight(S) - W_(not P)) c = t c = T(z) mod p.
 Their number m_w = |U| + |V| satisfies m_w = sum_U a + sum_V a = t (mod 2), and t = q + q' - 2q' = m = 0 (mod 2);
 0 <= m_w <= R <= 2p - Phi; and m_w >= 0 >= 2 - Phi.  So C_w := 2p - m_w is even with Phi <= C_w <= C_max, and by
 GRX (realisability) w has an identity 2p-subword with pattern z: contradiction.  Hence u avoids.
Step 3.  If N + E >= 4p-1, delete N + E - (4p-1) <= E - 1 rotations from runs of u that keep at least one rotation
(u has W = R + E rotations in k <= R nonempty runs, so W - k >= E is enough room).  The result is an RGR word of length
exactly 4p-1 and a subword of the avoider u, hence an avoider, contradicting RGR-LONG(p).  So N + E <= 4p-2.  []

## 3. When does (FULL) hold?

(FULL) holds if the weights, listed in increasing order, satisfy a_(i) <= 1 + a_(1) + ... + a_(i-1); e.g. if L1
(the number of rotations equal to rho_c) is at least a_max - 1.  It is a GLOBAL condition: no assumption on which run
contains which rotation (the "thin heavy" obstruction of Theorem EXP, proof-EXP-v2.md, does not arise here).
If moreover R > p, kappa = 0 makes the rotation sequence zero-sum-free in Z_(2p) (no zero-sum of even length in
[2, 2p], and R < 2p), and the Savchev-Chen theorem [S. Savchev, F. Chen, Discrete Math. 307 (2007) 2671-2679; LITERATURE
IMPORT, statement not re-read in this cycle, parent check required] gives a generator g with all weights positive and
W <= 2p-1.  Then E <= 2p-1-R, every weight is at most 1 + E, and L1 >= R - E/2; (FULL) follows when
1 + E <= 1 + L1, which holds whenever 5(2p - R) <= 4p + 3.  At N = 4p-2, R = 2p - k, so: for kappa = 0, RGR shape and
k <= min(p - 1, (4p+3)/5), Corollary ELT0-ROT applies (conditional on the Savchev-Chen import).

## 4. Scope and relation to the open part

* kappa = 0 is the normal form of the RIGID avoiders (accepted RUNS assembly: inherited avoiders normalise to
  B = kappa = 0); ELT0 shows that in this slice heavy rotations cost exactly their excess in length.
* Not covered: kappa >= 1 (admissible counts then have the lower bound 2kappa + 2 - Phi and R may exceed 2p - Phi; the
  global-subset-sum trick of Step 2 does not control the count), non-RGR shape (u keeps the empty runs; the reflection
  slice's K0* or REFL would be needed), and failures of (FULL).
* Tightness: Prop. SH-ROT and the finite data (README, results-v2.md) show non-rigid avoiders with N + E = 4p-2 (e.g.
  kappa = 0 two-block words g^(2p-5)(3g) at N = 4p-4).
