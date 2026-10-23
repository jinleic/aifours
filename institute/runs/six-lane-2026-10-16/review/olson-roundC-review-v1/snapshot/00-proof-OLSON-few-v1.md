# Corollary OLSON-FEW: ordered Olson at length 4p-1 for words with few odd maximal constant reflection blocks, v1

Owner OlsonRotationRigidity.  Written after host clock 2026-10-18T07:32:27-07:00.  Status [W], UNREVIEWED combination
note (no new lemma).  CONDITIONAL on Corollary REFL-few-odd (reflection/proof-REFL-fewodd-r2.md, sha256
db16274fffccde41e65025a46c4992bb3c11c26bce9bcc97f5bc3efaae65c2c6, [W], inputs parent-accepted) and, for part (b), on
Theorem SHgen (proof-SHgen-v2.md 8fde88c0...d239, Codex round-B ACCEPT, not yet parent-accepted).
Imports: Corollary INV*-FEW (proof-INVstar-few-v1.md 026753c9...16bc4; its REFL citation r1 has the same statement as
r2); RGR-LONG(p) (parent-accepted, R/olson-runs-parent-verdict-v1.md: every RGR word of length 4p-1 has an identity
2p-subword).  o_F(w): number of maximal constant reflection blocks of odd length (maximal cyclic decomposition).

## Statement

**Corollary OLSON-FEW.**  Let p >= 5 be prime and w a word of length 4p-1 over D_(2p).
 (a) If o_F(w) <= 2, or p >= 7 and o_F(w) <= 3, then w has an identity 2p-subword (conditional on REFL-few-odd only).
 (b) If 5 o_F(w) <= 2p - 1, then w has an identity 2p-subword (conditional on REFL-few-odd and SHgen).

## Proof

Lemma (one deletion).  If w' is obtained from w by deleting one letter, then o_F(w') <= o_F(w) + 1.
Proof.  Deleting a rotation leaves every block unchanged unless its run becomes empty; then the two neighbouring
blocks either keep their identity (different values) or fuse into one block whose parity is that of the sum of their
lengths, which never increases the number of odd blocks.  Deleting a reflection from a block of length >= 2 flips that
block's parity (change +-1).  Deleting a block of length 1 removes one odd block; its two runs merge, and if the merged
run is empty and the two neighbouring blocks have equal values they fuse, again without increasing the count.  []
Suppose w has no identity 2p-subword.  Every subword w' of length 4p-2 then avoids and has o_F(w') <= o_F(w) + 1, which
is <= 3 (resp. <= 4 with p >= 7) in case (a) and satisfies 5 o_F(w') <= 2p + 4 in case (b).  By Corollary INV*-FEW
(part (a), resp. (b)) every such w' is RGR: its rotations lie in one {rho_c, rho_-c}, c != 0, and its maximal cyclic
reflection runs are constant.  Then w is RGR: two rotation letters of w whose values are not in one pair {c, -c} with
c != 0 (or a letter rho_0) survive together in some w' (delete any third letter; 4p - 1 >= 3), and two adjacent
reflections of different values survive, still adjacent, in the subword obtained by deleting a letter away from them.
RGR-LONG(p) gives w an identity 2p-subword: a contradiction.  []

## Scope

* Range of (b): o_F(w) <= 4 at p = 11, 5 at p = 13, 6 at p = 17, 7 at p = 19, 9 at p = 23, about 2p/5 in general.
* This is ordered Olson only for the stated class of words of length 4p-1; the general ordered Olson statement for
  D_(2p) remains open (its remaining part is equivalent to INV*(p) on avoiders with more odd blocks, which this lane
  does not prove).  Conditional as stated; no novelty claim.
