# Assembly note RIGID-STRUCT: the two rotation patterns of RGR-shape avoiders (kappa in {0, k-1}), v1

Owner OlsonRotationRigidity.  Written after host clock 2026-10-18T07:29:58-07:00.  Status [W], UNREVIEWED assembly note:
no new lemma; it combines parent-accepted results exactly as Lemma Ua of proof-SHgen-v2.md does (Codex round B:
"Both capped-case exclusions are valid ... KB is consequently used only through its uncapped implication").
Imports (accepted scopes): GRX, PM*, K1 (lowodd verdict v2); Corollary B'(b), the C1 composition, Theorem KBH, the
uncapped implication of Theorem KB (RUNS verdict R/olson-runs-parent-verdict-v1.md); Davenport-alpha instance (V)
(erratum m4); the trivial cut.

## Statement

Let p >= 5 be prime and w an avoider of length 4p-2 over D_(2p) whose rotations lie in one {rho_c, rho_-c}, c != 0,
and whose maximal cyclic reflection runs are constant (RGR shape).  Bring w to all-odd form by PM* (k >= 1 blocks, runs
nonempty), H = sum (l_i - 1)/2, kappa = p - 1 - H; replace c by -c so that A := #rho_c >= B := #rho_-c.  Then exactly
one of the following holds:
 (I)  kappa = 0 and B = 0: all R = 2p - k rotations equal rho_c;
 (II) 1 <= kappa = k - 1 <= p - 1 (so 2 <= k <= p): one run consists of exactly 2p - 1 letters rho_c, and each of the
      other k - 1 runs consists of exactly one letter rho_-c (R = 2p + k - 2).

## Proof

k = 1: Proposition K1 gives all rotations equal (and F = R = 2p - 1, kappa = 0): case (I).  Let k >= 2.  A <= 2p - 1
(trivial cut).  B <= kappa, since otherwise (rho_c rho_-c)^(kappa+1) is a zero-sum of admissible length
2kappa + 2 <= 2p for the all-plus pattern.  If 1 <= B < kappa, Corollary B'(b) solves w; if B = 0 < kappa, the C1
composition solves w.  So B = kappa.  If kappa = 0: case (I).  If B = kappa >= 1: (V) gives kappa <= k - 1; KBH solves
w if k >= p + 1; for k <= p the uncapped implication of KB solves w unless a capped segment G exists, i.e. (all blocks
odd, so the OR-segments are the single runs) A_G - B_G >= 2p - 1, which with A <= 2p - 1 gives A_G = A = 2p - 1 and
B_G = 0: G holds every rho_c and the other k - 1 runs hold only rho_-c, B = kappa of them.  Runs are nonempty, so
kappa = B >= k - 1, hence kappa = k - 1 and each other run holds exactly one rho_-c: case (II).  []

## Remarks

* The avoiders listed in out/bases_p5_N18.txt and out/bases_p7_N26.txt show both patterns for every k <= p (README
  06:42:14 observation (o, H) table: H = p - 1 is (I), H = p - k is (II)), so neither case is vacuous [O].
* Consequence for ROT: any proof of ROT on a range of avoiders yields, with this note and REFL where needed, their
  complete rotation pattern.  In the rotation-structure arguments (ROT-FEW, KAPPA01) the target is therefore (I) or
  (II); in particular the Davenport-tight case kappa = k - 1 must end with a single run carrying 2p - 1 equal letters.
* Not ROT(p), REFL(p), INV*(p) or ordered Olson; no novelty claim (it may duplicate statements of the RUNS assembly).
