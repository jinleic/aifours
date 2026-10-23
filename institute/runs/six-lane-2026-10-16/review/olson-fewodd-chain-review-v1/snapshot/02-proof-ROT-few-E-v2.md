# Reduction ROT-FEW-E: on 5o <= 2p + 4, INV*(p) follows from REFL(p) (arbitrary reflection runs), v2

Owner OlsonRotationRigidity.  v2 = ERRATA version of proof-ROT-few-E-v1.md (sha256 79f6e2f1...b897, kept unchanged),
written after host clock 2026-10-18T07:08:27-07:00.  Codex round-B review R/olson-rotation-roundB-codex-v1.note.md
(sha256 b589f978...c966): ACCEPT-WITH-FIXES (0 FATAL, 0 MAJOR, 1 MINOR); v2 applies that single correction (the normal
form may end with one even block) and NOTHING else; exact diff and fix map in Sec. 4.  v2 itself is unreviewed.
CONDITIONAL on Theorem SHgen (proof-SHgen-v2.md 8fde88c0...d239) and on REFL(p) (the reflection slice's open target:
every avoider of length 4p-2 whose rotations lie in one {rho_x, rho_-x}, x != 0, has every maximal cyclic reflection
run constant).  Extends Theorem ROT-FEW (proof-ROT-few-v3.md 5f158d69...efaa) from constant runs to arbitrary
reflection runs.  Not INV*(p) and not ordered Olson: REFL(p) is open.
Imports: GRX (any cyclic constant-block representation, empty runs allowed), PM*, K1 (lowodd verdict v2);
Davenport-alpha instance (Lemma DAV of proof-ROT-o3-v4.md: any constant-block representation, maximal or not);
proof-ROT-few-v3.md Sec. 1-5 (SCHERK, GROW, SET, MULT, EXTRACT, WT: statements about sequences only);
proof-SHgen-v2.md Sec. 0-4.

## 0. Representation

Split every maximal cyclic reflection run of an avoider w into its maximal constant sub-blocks; consecutive sub-blocks
of one run are separated by EMPTY rotation runs and have different values.  o := the number of odd sub-blocks.
Normal form: F >= 1, since F = 0 would leave R = 4p-2 >= 3p-1 rotations and EGZ (twice) would give an identity
2p-subword.  Apply PM* across every even sub-block (it allows empty runs); whenever two blocks of the same value become
separated by an empty run, read them as one (even) block and apply PM* again; each such step lowers the number of odd
blocks by 2.  The process ends with an avoider w^ of the same length and rotation multiset, given EITHER by a cyclic
representation with 1 <= k <= o blocks, all odd, in which every EMPTY run separates two blocks of DIFFERENT values,
OR (no odd block left, possibly after an equal-valued merge) by ONE EVEN block.  The even-block case is impossible:
accepted Proposition K1 forces F = 2p-1, which is odd (equivalently, Davenport-alpha with H = F/2 and F >= 2 gives
R + F/2 <= 3p-2, i.e. F/2 >= p, and 2p reflections of that block form an identity 2p-subword).  If k = 1, Proposition
K1 makes all rotations equal.  So let k >= 2.  As before H = (F - k)/2, kappa = p - 1 - H, R = 2p + 2kappa - k, and Lemma DAV
(boundary gaps are never in I; the frame is a boundary gap) gives kappa <= k - 1; GRX gives (ZP).

## 1. Lemma SHgen-E

Let w be as in SHgen-v2 Sec. 0 except that runs may be empty, every empty run separating blocks of different values.
Assume REFL(p).  If eta >= 1, (H) 2H >= E and (K) k <= 2p - eta - a_max - 1, then w has an identity 2p-subword.
Proof.  If every run is nonempty this is Theorem SHgen.  Otherwise follow SHgen-v2 Sec. 4 (induction on eta, w
assumed to avoid), with two observations.  (1) Lemma FLEXa and its proof never use nonempty runs (they use GRX for
the given representation, kappa >= 0, Phi <= k and R = 2p + 2kappa - k only), so FLEXa holds verbatim.  (2) For
eta = 1, Lemma Ua is replaced by: u°(h) has all rotations in {rho_c, rho_-c}, length 4p-2, and a maximal reflection
run that is not constant (the expansion deletes reflection pairs only inside blocks, every block stays nonempty, so
the empty run between two different values survives); by REFL(p), u°(h) is not an avoider.  The induction step
(eta >= 2) is unchanged; u° keeps the empty runs.  []

## 2. Theorem ROT-FEW-E

**Theorem ROT-FEW-E.**  Let p >= 5 be prime, assume Theorem SHgen and REFL(p), and let w be an avoider of length
4p-2 over D_(2p) with o odd maximal constant reflection sub-blocks, 5o <= 2p + 4.  Then all rotation letters of w lie
in one {rho_c, rho_-c}, c != 0; and, by REFL(p), every maximal reflection run of w is constant, so w is RGR.
Proof.  Sec. 0 gives w^ with k <= o, so 5k <= 2p + 4, and k >= 2 (or the cases k <= 1 are settled there).  Steps 1-4
of proof-ROT-few-v3.md Sec. 6 use only (ZP), kappa <= k - 1 and statements about sequences, so they hold for w^: with
c from Step 4, every rotation has SHgen weight r or -b, no rotation is rho_0, and E <= k - 1 - |N|.  If E = 0 the
rotations lie in {rho_c, rho_-c}.  Otherwise Step 5's inequalities give (H) and (K), and Lemma SHgen-E gives w^ an
identity 2p-subword, contradicting PM*.  The rotation multiset of w is that of w^.  The last sentence is REFL(p)
applied to w.  []

## 3. Consequence and scope

* Conditional on Theorem SHgen: on the range 5o <= 2p + 4 (o counted on maximal constant sub-blocks), INV*(p)
  is implied by REFL(p).  In particular the reflection slice's REFL(p) would close INV*(p) for every avoider with at
  most (2p+4)/5 odd sub-blocks.
* Unconditional parts used here: the normal form of Sec. 0 (ending with 1 <= k odd blocks or one even block, the
  latter excluded there), FLEXa without nonempty runs, Steps 1-4 of ROT-FEW.
* Not covered: o > (2p+4)/5; the kappa = 0 corollary ELT0-FEW is NOT extended (ELT0 needs nonempty runs for RGR-LONG).
* No novelty claim; not INV*(p), REFL(p) or ordered Olson.

## 4. Errata diff and fix map (v1 -> v2)

Fix map: Codex round-B MINOR 1 (SOURCE03 LF17-23, LF54: PM* can terminate with one even block; exclude F = 0 by the
rotations-only EGZ bound; state the two terminal forms, also after equal-valued merges; kill the even block by K1 or
by Davenport with H = F/2) -> Sec. 0 "Normal form" paragraph and Sec. 3 first-but-one bullet.  Header: version line and
this provenance only.  No other change; theorem range and conclusion unchanged.
Unified diff of the body (header excluded):
```
--- proof-ROT-few-E-v1.md (body)
+++ proof-ROT-few-E-v2.md (body)
@@ -14 +14,2 @@
-Normal form: apply PM* across every even sub-block (it allows empty runs); whenever two blocks of the same value become
+Normal form: F >= 1, since F = 0 would leave R = 4p-2 >= 3p-1 rotations and EGZ (twice) would give an identity
+2p-subword.  Apply PM* across every even sub-block (it allows empty runs); whenever two blocks of the same value become
@@ -16,4 +17,6 @@
-blocks by 2.  The process ends with an avoider w^ of the same length and rotation multiset, given by a cyclic
-representation with k <= o blocks, all odd, in which every EMPTY run separates two blocks of DIFFERENT values.  If
-k = 0, Davenport-alpha gives H >= p and the all-plus pattern solves w^ (contradiction); if k = 1, Proposition K1 makes
-all rotations equal.  So let k >= 2.  As before H = (F - k)/2, kappa = p - 1 - H, R = 2p + 2kappa - k, and Lemma DAV
+blocks by 2.  The process ends with an avoider w^ of the same length and rotation multiset, given EITHER by a cyclic
+representation with 1 <= k <= o blocks, all odd, in which every EMPTY run separates two blocks of DIFFERENT values,
+OR (no odd block left, possibly after an equal-valued merge) by ONE EVEN block.  The even-block case is impossible:
+accepted Proposition K1 forces F = 2p-1, which is odd (equivalently, Davenport-alpha with H = F/2 and F >= 2 gives
+R + F/2 <= 3p-2, i.e. F/2 >= p, and 2p reflections of that block form an identity 2p-subword).  If k = 1, Proposition
+K1 makes all rotations equal.  So let k >= 2.  As before H = (F - k)/2, kappa = p - 1 - H, R = 2p + 2kappa - k, and Lemma DAV
@@ -51 +54,2 @@
-* Unconditional parts used here: the normal form of Sec. 0, FLEXa without nonempty runs, Steps 1-4 of ROT-FEW.
+* Unconditional parts used here: the normal form of Sec. 0 (ending with 1 <= k odd blocks or one even block, the
+  latter excluded there), FLEXa without nonempty runs, Steps 1-4 of ROT-FEW.
```
