# Theorem EXP2: expansion with side-fullness (any kappa, any number of odd blocks); negative heavies

Owner OlsonRotationRigidity.  Written after host clock 2026-10-18T05:29:23-07:00.  Status [W], UNREVIEWED.
Strengthens Theorem EXP (proof-EXP-v2.md, frozen): its per-run fullness (X1) is replaced by the weaker per-pattern
"side fullness" (X1'), and heavy rotations near -c are treated by expanding them into copies of rho_-c.  Not ROT.
Imports as in proof-EXP-v2.md: GRX (accepted, any representation); accepted Corollary B'(b) (RGR, length 4p-2,
F, R >= 1, A >= B, 1 <= B < kappa => solvable) and the accepted lemma composition C1 (same with B = 0 < kappa).

## 1. Setting and hypotheses

p >= 5, w of length 4p-2 with F, R >= 1, maximal constant-block representation with all runs nonempty (RGR shape).
Fix c != 0.  Each rotation value x gets a SIGNED weight b_x: the odd integer in (-p, p) with x = b_x c (mod p) and
(1, x) = b_x (1, c) in Z_(2p).  x is LIGHT (b = 1), MINUS (b = -1) or HEAVY (|b| >= 3; this includes x = 0, b = +-p is
excluded since p is odd and |b| < p ... we take b in {-(p-2), ..., p-2} odd, and x = 0 gets b = p or -p: such x is
treated as a heavy with |b| = p).  [Convention: for x = 0 choose b = p.]
For a pattern z with plus-set P define the EFFECTIVE weight e_x = +b_x if x lies in a run of P and -b_x otherwise;
POS_P = {x : e_x > 0}, NEG_P = {x : e_x < 0}, with absolute weights |b_x|.
E := sum over heavy x of (|b_x| - 1).  A := #LIGHT + sum_{heavy, b > 0} b,  B := #MINUS + sum_{heavy, b < 0} |b|.
(X1') for every pattern P, the absolute weights of POS_P and those of NEG_P each have full subset sums (every integer
      from 0 to the total is a sub-multiset sum).
(X2)  sum_i floor((l_i - 1)/2) >= E/2 (spare equal reflection pairs inside blocks).
(X4)  min(A, B) < kappa(w) + E/2, where kappa(w) = p-1-H(w).

**Theorem EXP2.**  Under (X1'), (X2), (X4), w is not an avoider unless E = 0 (w rigid).
Proof.  Suppose w avoids and E >= 2.  Let w° be w with every heavy x replaced in place by |b_x| copies of
rho_(sign(b_x) c), and with E/2 equal pairs deleted from blocks (never emptying a block, parities kept).  w° has
length 4p-2, all rotations in {rho_c, rho_-c}, RGR shape, A(w°) = A, B(w°) = B, kappa(w°) = kappa(w) + E/2.
w° avoids: for each pattern z, Phi and T(z) agree with w, and C_max(w°) = C_max(w) - E.  A solution of w° uses C°
reflections and q+ effective-positive and q- effective-negative rotations (copies), q+ + q- = 2p - C°, signed sum
(q+ - q-) c = T(z).  Each effective-positive copy of w° comes from an element of POS_P of w (a light or minus element
contributes one copy, a heavy |b| copies), so q+ is at most the total absolute weight of POS_P; by (X1') choose
T+ within POS_P of absolute weight exactly q+, and T- within NEG_P of absolute weight q-.  Selecting T+ u T- in w gives
signed sum (q+ - q-) c and count m in [q+ + q- - E, q+ + q-] with m = q+ + q- (mod 2) (each |b| is odd; only heavies
compress, by |b|-1 each).  So C := 2p - m is even with C° <= C <= C° + E <= C_max(w) and C >= Phi: w would have a
solution (GRX).  Hence w° avoids.  By (X4), min(A(w°), B(w°)) < kappa(w°); after the automorphism v -> -v if
necessary, w° is an RGR avoider of length 4p-2 with A >= B and B < kappa, contradicting (B') if B >= 1 or (C1) if B = 0.  []

## 2. When (X4) holds

The GRX zero pattern of w forbids zero-sums of even length in [2kappa+2, 2p].
* If every heavy has b > 0 and #MINUS <= #LIGHT: (LIGHT)^j (MINUS)^j shows #MINUS <= kappa, so B = #MINUS <= kappa
  < kappa + E/2: (X4) holds.  (This is Corollary EXP-RGR of proof-EXP-v2.md, now with (X1') instead of (X1).)
* One negative heavy x = -3c (b = -3) and no other heavy, with #LIGHT >= #MINUS + 3: the zero-sum
  x (LIGHT)^3 (LIGHT MINUS)^j has length 4 + 2j, so #MINUS + 2 <= kappa; then B = #MINUS + 3 <= kappa + 1 = kappa + E/2,
  with equality exactly when #MINUS = kappa - 2.  (X4) holds unless #MINUS = kappa - 2 ("boundary").  Every negative-
  heavy non-rigid avoider found at lengths 4p-4 .. 4p-6 (README log 05:14-05:16) is at this boundary.

## 3. When (X1') fails (single heavy of weight +-3)

For one heavy x (|b| = 3) in run j, (X1') fails only for patterns whose side containing x has fewer than two other
elements of that side: for P = {j}, POS_P = (non-minus elements of run j) u (minus elements outside run j).  So (X1')
holds unless (#LIGHT in run j) + (#MINUS outside run j) <= 1 (b = 3), or the analogous count with LIGHT/MINUS exchanged
is <= 1 (b = -3), up to the same condition for the other patterns whose relevant side is that small.
(X1') is GLOBAL across runs of a zone, so the "thin heavy" of Theorem EXP is covered as soon as its zone has two other
units of its effective sign.

## 4. Residual after EXP2 (for RGR-shape avoiders of length 4p-2)

Single-heavy residual: (a) a heavy whose pattern side has <= 1 other unit of its effective sign; (b) the boundary
negative heavy -3c with #MINUS = kappa - 2; (c) multiple heavies or larger |b| with (X1')/(X2)/(X4) failing.  kappa = 0
is completely covered by Theorem ELT0 (proof-ELT0-v1.md) under global fullness.  Non-RGR shape needs REFL / K0*.
