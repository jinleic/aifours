# Theorem EXP: expanding heavy rotations to reach the accepted rigid theory (any number of odd blocks), v2

Owner OlsonRotationRigidity.  v2 written after host clock 2026-10-18T05:13:20-07:00; v1 (sha256 bbae26e4...8900) kept
unchanged; v1's header label 04:1x was not a clock read (addendum-timestamps-v2.md: v1 was written between 04:13:12
and 04:14:11).  Changes: the C1 import is now stated as confirmed by the parent at its lemma-composition scope; a
kappa = 0 remark is added (Sec. 3).  Status [W], UNREVIEWED.  A partial
result toward ROT(p) valid for every number of odd blocks, under explicit hypotheses (X1), (X2) below; it is NOT ROT.
Imports: GRX for any constant-block representation (parent-accepted, R/olson-rotation-lowodd-parent-verdict-v2.md,
sha256 0853f4ac...ba29); from the parent-accepted RUNS assembly (R/olson-runs-assembly-proof-v4.md, verdict
R/olson-runs-parent-verdict-v1.md, sha256 82adbddd...9237):
 (B') Corollary B'(b): every RGR word of length 4p-2 with F, R >= 1, A >= B and 1 <= B < kappa is solvable (no inherited
      hypothesis);
 (C1) branch C1 of Theorem C: every RGR word of length 4p-2 with F, R >= 1, B = 0 < kappa is solvable (Lemma OR, then
      S1'/A1'/trivial cut if o_F <= p, C0-B'/A1/trivial cut if o_F >= p+1; v4 Remark (2) and Sec. 5 state that this branch
      applies to every k and uses no inherited condition).  Parent IRC (between 05:05:09 and 05:06:06): this
      composition import (OR, then S1'/A1'/trivial cut if o_F <= p, C0-B'/A1/trivial cut otherwise; RGR length 4p-2,
      F, R >= 1, B = 0 < kappa, any k) is confirmed at its accepted lemma-composition scope; it is NOT Theorem C's
      inherited conclusion used outside its domain.
(A, B = numbers of rho_x, rho_-x after normalisation A >= B; kappa = p-1-H, H = sum of floor(l/2) over maximal
reflection runs.)

## 1. Setting

p >= 5, w a word of length 4p-2 with F, R >= 1, and a cyclic constant-block representation R_1 S_1 ... R_k S_k (blocks
S_i = sigma_(y_i)^(l_i), l_i >= 1; runs X_i possibly empty).  Fix c != 0 and the generator g = (1, c) of
Z_2 x Z_p = Z_(2p).  Every rotation value x satisfies (1, x) = a_x g for a unique odd a_x in [1, 2p-1] (so x = a_x c mod p).
Call x MINUS if a_x = 2p-1 (x = -c), LIGHT if a_x = 1 (x = c), HEAVY otherwise (3 <= a_x <= 2p-3; this includes x = 0,
a_x = p, and every value outside {c, -c}).  For a run X_i let P_i be the multiset of a_x over its non-MINUS rotations.
E := sum over HEAVY rotations of (a_x - 1) (even).
(X1) Fullness: for every i, every integer in [0, sum P_i] is a sub-multiset sum of P_i.
(X2) Pairs: sum_i floor((l_i - 1)/2) >= E/2.

## 2. Lemma EXP

Assume (X1), (X2) and that w avoids.  Let w° be obtained by replacing every HEAVY rotation, in place, by a_x copies of
rho_c, and deleting E/2 pairs of letters from blocks (two letters of the same block at a time, never emptying a block).
Then w° avoids.  w° has length 4p-2, all rotations in {rho_c, rho_-c}, the same block values and parities, nonempty
runs exactly where w had them, #rho_-c unchanged and H(w°) = H(w) - E/2 (H counted over the representation's blocks).
Proof.  GRX for w° uses the representation inherited from w; for each pattern z, Phi and delta are unchanged, F drops
by E, so C_max° = C_max - E; T(z) is unchanged (block values unchanged).  Suppose w° has an identity 2p-subword:
a pattern z, an even C° in [Phi, C_max°], and in each run i a choice of q_i copies of rho_c (out of sum P_i) and q_i'
copies of rho_-c, with sum_i (q_i + q_i') = 2p - C° and sum_i z_i (q_i - q_i') c = T(z).  By (X1) choose, in X_i, non-MINUS
rotations with weight sum exactly q_i; their value sum is q_i c, their number c_i satisfies c_i <= q_i and c_i = q_i
mod 2 (all weights odd), and q_i - c_i is at most the sum of (a_x - 1) over the chosen HEAVY ones.  Keep the same q_i'
MINUS rotations.  The new count m = sum (c_i + q_i') lies in [2p - C° - E, 2p - C°] with the parity of 2p - C°, so
C := 2p - m is even with C° <= C <= C° + E <= C_max, and C >= Phi.  By GRX (realisability direction) w has an identity
2p-subword with pattern z and C reflections: contradiction.  []

## 3. Corollary EXP-RGR (constant reflection runs)

Assume moreover that the representation is the maximal-block one and every run is nonempty (equivalently, every maximal
cyclic reflection run of w is constant), that #rho_-c <= #rho_c in w, and that w avoids.  Then w has no HEAVY rotation:
all rotation values lie in {c, -c}.
Proof.  If E >= 2, w° (Lemma EXP) is an RGR word of length 4p-2 that avoids, with B° = #rho_-c(w),
A° = #rho_c(w) + sum_HEAVY a_x >= B°, and kappa° = kappa(w) + E/2.  The GRX zero pattern of w forbids zero-sums of
length 2j in [2kappa+2, 2p], so (rho_c)^j (rho_-c)^j shows min(#rho_c, #rho_-c) <= kappa; with #rho_-c <= #rho_c,
B° <= kappa < kappa°.  (B') (if B° >= 1) or (C1) (if B° = 0) says w° is solvable: contradiction.  []

Remark (kappa = 0).  If kappa(w) = 0 in an all-odd representation (H = p-1, all blocks odd), then
sum_i floor((l_i - 1)/2) = H = p-1, and E <= 2p-2 always holds when E/2 <= p-1; in particular (X2) holds whenever
E <= 2p-2, e.g. whenever the zero-sum-free multiset Y(X) has total weight <= 2p-1 with respect to g (then
E = W - R <= 2p-1-R).  So for kappa = 0 the only hypothesis left is the fullness (X1).

## 4. Corollary EXP-REFL (conditional; for the reflection interface)

If w avoids, satisfies (X1), (X2), E >= 2, and its representation has an empty run between two blocks of different
values, then w° is a rigid avoider with a non-constant maximal reflection run.  So any proof of the reflection slice's
REFL(p) (rigid avoiders of length 4p-2 have constant reflection runs) excludes such w.  (No claim about REFL here.)

## 5. What EXP leaves open (precise)

ROT(p) is open exactly for avoiders with >= 5 odd blocks (o <= 4: proof-ROT-o3-v3.md, proof-ROT-o4-v1.md, unreviewed;
o <= 2 accepted) such that for every c with #rho_-c <= #rho_c, (X1) or (X2) fails, or the reflection runs are not all
constant (then EXP needs REFL).  Typical failures: a HEAVY rotation whose run has too few other light rotations ("thin",
(X1)); HEAVY values near -c (a_x close to 2p-1) whose expansion cost exceeds the reflection pairs ((X2)).  Moves that
can repair (X1)/(X2) without changing avoidance: M0* (a same-run zero-sum pair {x, -x}, any x, becomes a pair sigma_y
sigma_y in any block: +1 to the left side of (X2), and removes HEAVY pairs {x, -x}); moving a same-run zero-sum pair or a
single rho_0 to another run (GRX-exact, the contribution {x, -x} resp. {0} is sign-free).
