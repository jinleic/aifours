# Corollary REFL-few-odd: REFL(p) holds for every avoider with at most p odd maximal reflection blocks

Owner OlsonReflectionRigidity.  Written after host clock 2026-10-18T06:54:37-0700.  Status: written proof [W], UNREVIEWED.  Short
corollary; its only new content is the monotonicity of o_F along the reduction process of Theorem RED.
Scope: REFL(p) restricted by o_F; nothing about rotation values, INV*(p) as a whole, or ordered Olson.

## Statement

o_F(w) := number of maximal constant reflection blocks of ODD length (maximal cyclic decomposition, proof-K0star-r2.md Sec. 0;
equals k for an all-odd word).  REFL(p) is quoted from README.md Sec. 1: "every avoider w of length 4p-2 over D_(2p) whose
rotation letters all lie in one set {rho_x, rho_-x}, x != 0, has every maximal CYCLIC reflection run constant".
**Corollary REFL-few-odd.**  Let p >= 5 be prime and w0 an avoider of length 4p - 2 whose rotation letters lie in one set
{rho_x, rho_-x}, x != 0, with o_F(w0) <= p.  Then every maximal cyclic reflection run of w0 is constant.
Inputs (all parent CORRECTNESS-ACCEPTED):
* Theorem RED with its process and imports (I1)-(I4): proof-RED-r2.md (verdict R/olson-reflection-K0star-RED-parent-verdict-v1.md,
  879aeee7...c02a; documentation errata in proof-RED-r3.md, 9eb74e96...e3e6);
* "no avoider in RES_<(p) with k <= p" (Theorems B0S and MXG; R/olson-reflection-smallk-parent-verdict-v1.md, b71fcaf4...13b8).
Remark: a REFL-violating word built from finer constant SUB-blocks has o_F (maximal blocks) <= its number of odd sub-blocks, since
fusing equal-valued sub-blocks across empty runs never increases the number of odd blocks (odd + odd = even, odd + even = odd).

## Proof

Suppose w0 violates the conclusion.  The proof of Theorem RED (proof-RED-r2.md Sec. 5) normalises x = 1 and A >= B (no block
changes) and runs the moves P1-P4 until it stops.  Every exit with g = 0 (Exit P1, Exit P3) is contradictory there, and the
terminal state with g >= 1 is an avoider in RES_<(p) with kappa >= 2.  In RES_<(p) every block is odd, so its number of runs is
k = o_F.  Claim: o_F never increases along P1-P4.  Then the terminal word has k <= o_F(w0) <= p, which the small-k verdict
excludes.  This is a contradiction.
Proof of the claim.  Empty runs of the maximal decomposition lie only between blocks of different values.
* P1 (FUS, proof-K0star-r2.md Lemma FUS) recolours an even block E to the value u of a block X that is adjacent across an empty
  run. X and E then fuse, and the result has the parity of X.  If the run on E's other side is empty and the block Y there also
  has value u, then X, E and Y all fuse.  The new block has the parity of |X| + |Y|.  Before the move, X, E, Y contributed the
  odd blocks among X and Y.  After it, the merged block is odd iff exactly one of X, Y is odd.  So o_F drops by 2 or is unchanged.
* P2 (PM0, proof-K0star-r2.md L107-110) merges two nonempty runs R_j, R_(j+1) and appends the even block S_j to S_(j+1).  So
  S_(j+1) keeps its parity, S_j (even) disappears, and the merged run is nonempty, so nothing fuses.  o_F is unchanged.
* P3 (TR-fill) moves one rho_1 rho_-1 pair from a run with r >= 3 (which stays nonempty) into an empty run.  No block changes, and
  no block splits, because the filled run lay between different values.  o_F is unchanged.
* P4 (M0') deletes the two letters of a (1,1)-run and inserts sigma_y sigma_y into a block, which keeps that block's parity.  The
  neighbours of the new empty run fuse if they have equal values.  odd + odd -> even, odd + even -> odd, even + even -> even, so
  o_F drops by 2 or is unchanged.  []

## Use

R/olson rotation lane: rotation/proof-ROT-few-E-v1.md (OlsonRotationRigidity, 79f6e2f1...b897) reports that, conditional on
rotation/proof-SHgen-v2.md, INV*(p) for avoiders with o <= (2p + 4)/5 odd constant sub-blocks needs REFL only for an expanded word
of length 4p - 2 with rotations in {rho_c, rho_-c}.  If that expanded word has o_F <= p (by the Remark it suffices that it has at
most p odd sub-blocks; (2p + 4)/5 <= p), this corollary supplies that REFL instance.  I have not checked that file; the
combination is [INFERENCE] until its author confirms which word and which o are meant.
