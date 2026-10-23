# Reduction ROT-FEW-E: on 5o <= 2p + 4, INV*(p) follows from REFL(p) (arbitrary reflection runs), v3

Owner OlsonRotationRigidity.  v3 written after host clock 2026-10-18T08:26:19-07:00: ERRATA of v2 (sha256
cb4bca7be188a19fa46f31602c60beeb7c962c14598d0edaeb210a3ae20d917e) for the Claude few-odd chain review
R/olson-fewodd-chain-claude-v1.note.md (Sec. 0 and Sec. 2 ACCEPT-WITH-FIXES; Sec. 1 INCONCLUSIVE because the proof text
of SHgen was not in that packet): m6 (fusion parity in the normal form) and m7 (Lemma SHgen-E with explicit line
citations of proof-SHgen-v3.md, sha256 fcbd5a972fdfe64f8b4c1798aef64d75375c334595bae6d400902e04546feb5e)
applied, fix map at the end.  Codex round C accepted v2.  No statement changes; v3 itself unreviewed.
v2 = ERRATA version of proof-ROT-few-E-v1.md (sha256 79f6e2f1...b897, kept unchanged),
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
separated by an empty run, read them as one block (its length is the sum of theirs, so it is odd exactly when one of
them is odd) and apply PM* again if it is even; each such step lowers the number of odd blocks by 2 or leaves it
unchanged (e.g. A | E1 | E2 with A odd, E1, E2 even and E2 of A's value: PM* across E1 lets A and E2 fuse into one
odd block), so k <= o and k = o (mod 2).  The process ends with an avoider w^ of the same length and rotation multiset, given EITHER by a cyclic
representation with 1 <= k <= o blocks, all odd, in which every EMPTY run separates two blocks of DIFFERENT values,
OR (no odd block left, possibly after an equal-valued merge) by ONE EVEN block.  The even-block case is impossible:
accepted Proposition K1 forces F = 2p-1, which is odd (equivalently, Davenport-alpha with H = F/2 and F >= 2 gives
R + F/2 <= 3p-2, i.e. F/2 >= p, and 2p reflections of that block form an identity 2p-subword).  If k = 1, Proposition
K1 makes all rotations equal.  So let k >= 2.  As before H = (F - k)/2, kappa = p - 1 - H, R = 2p + 2kappa - k, and Lemma DAV
(boundary gaps are never in I; the frame is a boundary gap) gives kappa <= k - 1; GRX gives (ZP).

## 1. Lemma SHgen-E

Let w be as in SHgen-v2 Sec. 0 except that runs may be empty, every empty run separating blocks of different values.
Assume REFL(p).  If eta >= 1, (H) 2H >= E and (K) k <= 2p - eta - a_max - 1, then w has an identity 2p-subword.
Proof.  If every run is nonempty this is Theorem SHgen.  Otherwise follow the proof of SHgen (proof-SHgen-v3.md
Sec. 4, L115-121: induction on eta, w assumed to avoid), with three observations; line numbers refer to
proof-SHgen-v3.md, whose proof text is that of v2.
(0) The only word operation in that proof is the expansion u°(h) (L51-55): the rotation letter h is replaced IN PLACE,
inside its own run (nonempty, as it contains h), by a copies of rho_(sc), and (a-1)/2 pairs sigma_y sigma_y are
deleted inside blocks so that every block stays odd and nonempty.  No rotation letter is placed into an empty run, no
block is merged, split or recoloured, and every block keeps its value; so u°(h) has the same k blocks, the same block
values and the same empty runs, each still between the same two blocks of different values.  The induction step
(L119-121) applies the same expansion to u° and one of its heavies; hence every induction descendant of w has these
properties as well, and every empty run of w survives at every level.
(1) Lemma FLEXa (L78-113) never uses nonempty runs: it uses GRX for the given representation (accepted for any cyclic
constant-block representation, empty runs allowed), kappa >= 0, Phi <= k and R = 2p + 2kappa - k only, and its
comparison of u° with w (L84-86: same k, block parities, Phi(z), T(z) and the run of every rotation other than h and
its copies) holds by (0).  So FLEXa holds verbatim.
(2) For eta = 1, Lemma Ua (L57-76, which uses nonempty runs through B'(b), C1, KB and KBH) is replaced by: u°(h) has
length 4p-2, all its rotations in {rho_c, rho_-c} with c != 0, and, by (0), an empty run between two blocks of
different values; these two blocks lie in one maximal cyclic reflection run, which is therefore not constant; by
REFL(p), u°(h) is not an avoider.  The induction step (eta >= 2, L119-121) is unchanged.  []

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

## Errata diff and fix map (proof-ROT-few-E-v2.md -> proof-ROT-few-E-v3.md)

Fix map (Claude few-odd chain review R/olson-fewodd-chain-claude-v1.note.md):
m6 (SOURCE02:21-23: an equal-valued fusion lowers the odd count by 2 OR 0, counterexample A | E1 | E2) -> Sec. 0,
normal-form sentence (parity of the sum; odd count drops by 2 or 0; k <= o and k = o mod 2 unaffected).
m7 (SOURCE02:35-41: SHgen-E's observations are claims about SHgen's proof; the facts that no rotation letter enters an
empty run and no block is merged or recoloured were not stated) -> Sec. 1 proof, observations (0)-(2) with line
citations of proof-SHgen-v3.md (expansion L51-55, Ua L57-76, FLEXa L78-113 with the comparison at L84-86, Sec. 4
L115-121).  Header: version line and this provenance.  No statement, hypothesis or range changed.
Generated by unique string replacement from proof-ROT-few-E-v2.md (sha256 cb4bca7be188a19fa46f31602c60beeb7c962c14598d0edaeb210a3ae20d917e); body diff:

```diff
--- proof-ROT-few-E-v2.md
+++ proof-ROT-few-E-v3.md (body)
@@ -1,6 +1,12 @@
-# Reduction ROT-FEW-E: on 5o <= 2p + 4, INV*(p) follows from REFL(p) (arbitrary reflection runs), v2
+# Reduction ROT-FEW-E: on 5o <= 2p + 4, INV*(p) follows from REFL(p) (arbitrary reflection runs), v3
 
-Owner OlsonRotationRigidity.  v2 = ERRATA version of proof-ROT-few-E-v1.md (sha256 79f6e2f1...b897, kept unchanged),
+Owner OlsonRotationRigidity.  v3 written after host clock 2026-10-18T08:26:19-07:00: ERRATA of v2 (sha256
+cb4bca7be188a19fa46f31602c60beeb7c962c14598d0edaeb210a3ae20d917e) for the Claude few-odd chain review
+R/olson-fewodd-chain-claude-v1.note.md (Sec. 0 and Sec. 2 ACCEPT-WITH-FIXES; Sec. 1 INCONCLUSIVE because the proof text
+of SHgen was not in that packet): m6 (fusion parity in the normal form) and m7 (Lemma SHgen-E with explicit line
+citations of proof-SHgen-v3.md, sha256 fcbd5a972fdfe64f8b4c1798aef64d75375c334595bae6d400902e04546feb5e)
+applied, fix map at the end.  Codex round C accepted v2.  No statement changes; v3 itself unreviewed.
+v2 = ERRATA version of proof-ROT-few-E-v1.md (sha256 79f6e2f1...b897, kept unchanged),
 written after host clock 2026-10-18T07:08:27-07:00.  Codex round-B review R/olson-rotation-roundB-codex-v1.note.md
 (sha256 b589f978...c966): ACCEPT-WITH-FIXES (0 FATAL, 0 MAJOR, 1 MINOR); v2 applies that single correction (the normal
 form may end with one even block) and NOTHING else; exact diff and fix map in Sec. 4.  v2 itself is unreviewed.
@@ -19,8 +25,10 @@
 of one run are separated by EMPTY rotation runs and have different values.  o := the number of odd sub-blocks.
 Normal form: F >= 1, since F = 0 would leave R = 4p-2 >= 3p-1 rotations and EGZ (twice) would give an identity
 2p-subword.  Apply PM* across every even sub-block (it allows empty runs); whenever two blocks of the same value become
-separated by an empty run, read them as one (even) block and apply PM* again; each such step lowers the number of odd
-blocks by 2.  The process ends with an avoider w^ of the same length and rotation multiset, given EITHER by a cyclic
+separated by an empty run, read them as one block (its length is the sum of theirs, so it is odd exactly when one of
+them is odd) and apply PM* again if it is even; each such step lowers the number of odd blocks by 2 or leaves it
+unchanged (e.g. A | E1 | E2 with A odd, E1, E2 even and E2 of A's value: PM* across E1 lets A and E2 fuse into one
+odd block), so k <= o and k = o (mod 2).  The process ends with an avoider w^ of the same length and rotation multiset, given EITHER by a cyclic
 representation with 1 <= k <= o blocks, all odd, in which every EMPTY run separates two blocks of DIFFERENT values,
 OR (no odd block left, possibly after an equal-valued merge) by ONE EVEN block.  The even-block case is impossible:
 accepted Proposition K1 forces F = 2p-1, which is odd (equivalently, Davenport-alpha with H = F/2 and F >= 2 gives
@@ -32,13 +40,24 @@
 
 Let w be as in SHgen-v2 Sec. 0 except that runs may be empty, every empty run separating blocks of different values.
 Assume REFL(p).  If eta >= 1, (H) 2H >= E and (K) k <= 2p - eta - a_max - 1, then w has an identity 2p-subword.
-Proof.  If every run is nonempty this is Theorem SHgen.  Otherwise follow SHgen-v2 Sec. 4 (induction on eta, w
-assumed to avoid), with two observations.  (1) Lemma FLEXa and its proof never use nonempty runs (they use GRX for
-the given representation, kappa >= 0, Phi <= k and R = 2p + 2kappa - k only), so FLEXa holds verbatim.  (2) For
-eta = 1, Lemma Ua is replaced by: u°(h) has all rotations in {rho_c, rho_-c}, length 4p-2, and a maximal reflection
-run that is not constant (the expansion deletes reflection pairs only inside blocks, every block stays nonempty, so
-the empty run between two different values survives); by REFL(p), u°(h) is not an avoider.  The induction step
-(eta >= 2) is unchanged; u° keeps the empty runs.  []
+Proof.  If every run is nonempty this is Theorem SHgen.  Otherwise follow the proof of SHgen (proof-SHgen-v3.md
+Sec. 4, L115-121: induction on eta, w assumed to avoid), with three observations; line numbers refer to
+proof-SHgen-v3.md, whose proof text is that of v2.
+(0) The only word operation in that proof is the expansion u°(h) (L51-55): the rotation letter h is replaced IN PLACE,
+inside its own run (nonempty, as it contains h), by a copies of rho_(sc), and (a-1)/2 pairs sigma_y sigma_y are
+deleted inside blocks so that every block stays odd and nonempty.  No rotation letter is placed into an empty run, no
+block is merged, split or recoloured, and every block keeps its value; so u°(h) has the same k blocks, the same block
+values and the same empty runs, each still between the same two blocks of different values.  The induction step
+(L119-121) applies the same expansion to u° and one of its heavies; hence every induction descendant of w has these
+properties as well, and every empty run of w survives at every level.
+(1) Lemma FLEXa (L78-113) never uses nonempty runs: it uses GRX for the given representation (accepted for any cyclic
+constant-block representation, empty runs allowed), kappa >= 0, Phi <= k and R = 2p + 2kappa - k only, and its
+comparison of u° with w (L84-86: same k, block parities, Phi(z), T(z) and the run of every rotation other than h and
+its copies) holds by (0).  So FLEXa holds verbatim.
+(2) For eta = 1, Lemma Ua (L57-76, which uses nonempty runs through B'(b), C1, KB and KBH) is replaced by: u°(h) has
+length 4p-2, all its rotations in {rho_c, rho_-c} with c != 0, and, by (0), an empty run between two blocks of
+different values; these two blocks lie in one maximal cyclic reflection run, which is therefore not constant; by
+REFL(p), u°(h) is not an avoider.  The induction step (eta >= 2, L119-121) is unchanged.  []
 
 ## 2. Theorem ROT-FEW-E
 
```
