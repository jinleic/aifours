# Corollary OLSON-FEW: ordered Olson at length 4p-1 for words with few odd maximal constant reflection blocks, v2

Owner OlsonRotationRigidity.  Written after host clock 2026-10-18T07:34:34-07:00.  Status [W], UNREVIEWED combination
note (no new lemma).  Supersedes proof-OLSON-few-v1.md (2d29fcd2...afeb, kept): v1 deleted an arbitrary letter and so
needed INV* up to o_F(w) + 1; v2 chooses the deletions (a letter of an odd block of length >= 3, or two rotations), so
INV* is needed only up to o_F(w), and the ranges improve by one block.
CONDITIONAL on Corollary REFL-few-odd (reflection/proof-REFL-fewodd-r2.md, sha256
db16274fffccde41e65025a46c4992bb3c11c26bce9bcc97f5bc3efaae65c2c6, [W], inputs parent-accepted) and, for part (b), on
Theorem SHgen (proof-SHgen-v2.md 8fde88c0...d239, Codex round-B ACCEPT).
Imports: Corollary INV*-FEW (proof-INVstar-few-v1.md 026753c9...16bc4; its REFL citation r1 has the same statement as
r2); RGR-LONG(p) (parent-accepted, R/olson-runs-parent-verdict-v1.md: every RGR word of length 4p-1 has an identity
2p-subword).  o_F(w): number of maximal constant reflection blocks of odd length (maximal cyclic decomposition).

## Statement

**Corollary OLSON-FEW.**  Let p >= 5 be prime and w a word of length 4p-1 over D_(2p).
 (a) If o_F(w) <= 3, or p >= 7 and o_F(w) <= 4, then w has an identity 2p-subword (conditional on REFL-few-odd only).
 (b) If 5 o_F(w) <= 2p + 4, then w has an identity 2p-subword (conditional on REFL-few-odd and SHgen).

## Proof

Suppose w has no identity 2p-subword; every subword then avoids.  Let B denote the bound on o_F in (a) or (b); by
Corollary INV*-FEW every avoider of length 4p-2 with o_F <= B is RGR (rotations in one {rho_c, rho_-c}, c != 0, every
maximal cyclic reflection run constant).
Case 1: R <= 2.  Then F >= 4p - 3 and the blocks contain (F - o_F(w))/2 >= p disjoint adjacent equal pairs
sigma_y sigma_y (o_F(w) <= B <= 2p - 3); p of them form an identity 2p-subword: contradiction.
Case 2: some odd block has length >= 3.  Deleting one of its letters gives a word w' of length 4p-2 with
o_F(w') = o_F(w) - 1 (that block becomes even; nothing else changes).  w' is RGR.  w has the same rotations as w', and
its reflection runs differ from those of w' only by one more copy of a letter inside a constant block, so w is RGR.
Case 3: R >= 3 and every odd block has length 1.  Delete two different rotation letters x1, x2: w_i := w - x_i has
o_F(w_i) <= o_F(w) (deleting a rotation never raises o_F: if its run becomes empty the two neighbouring blocks keep
their identity or fuse, and fusing never increases the number of odd blocks).  Both w_i are RGR.  A third rotation
lies in both, so their pairs {c_1, -c_1}, {c_2, -c_2} coincide and every rotation of w lies in it; deleting a rotation
only creates new adjacencies between reflections, so two adjacent reflections of different values in w would stay
adjacent in w_1.  Hence w is RGR.
In Cases 2 and 3, RGR-LONG(p) gives w an identity 2p-subword: contradiction.  []

## Scope

* Range of (b): o_F(w) <= 5 at p = 11, 6 at p = 13, 7 at p = 17, 8 at p = 19, 10 at p = 23, about 2p/5 in general.
* This is ordered Olson only for the stated class of words of length 4p-1; the general ordered Olson statement for
  D_(2p) remains open (it would follow from INV*(p) for avoiders with more odd blocks, not proved in this lane).
  Conditional as stated; no novelty claim.
