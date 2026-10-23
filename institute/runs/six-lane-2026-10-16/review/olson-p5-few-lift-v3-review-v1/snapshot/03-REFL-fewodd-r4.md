# Corollary REFL-few-odd: REFL(p) holds for every avoider with at most p odd maximal CONSTANT reflection blocks (r4)

Owner OlsonReflectionRigidity.  r4 written after host clock 2026-10-18T07:55:00-0700: completes Claude m4 in Sec. 3, which r3 had
applied only in the import list.  r3 (d1cdb96e...c435) was never sent and is superseded.  r3 was written after host clock 2026-10-18T07:54:39-0700: errata only for the Claude review of r2
(R/olson-refl-fewodd-r2-claude-v1.note.md, a02b5073...560a, ACCEPT-WITH-FIXES 0/0/9), with the fix map at the end.  r2
(db16274f...c2c6; Codex ACCEPT 0/0/0, R/olson-refl-fewodd-r2-codex-v1.note.md 56e2127a...4cf7) is kept unchanged.
r2 was written after host clock 2026-10-18T07:05:39-0700.
Supersedes proof-REFL-fewodd-r1.md (6058831acc970e86a33f007bf900de397eaba5ccac7318bd3ba93a0bd61d7dd7, kept unchanged, unreviewed).
At the parent's request r2 made three changes: a fuller import list (completed in r3, Sec. 2), explicit hypotheses, and the interface
to the rotation lane is given.  The statement and proof are unchanged (fix map at the end).
Scope: REFL(p) restricted by o_F.  Nothing here concerns rotation values, INV*(p) as a whole or ordered Olson.

## 1. Statement (exact scope)

o_F(w) is the number of blocks of ODD length in the maximal cyclic constant-block decomposition of w.  [r3, Claude m2] These are
maximal CONSTANT blocks, not maximal reflection runs.  Counting runs would give a different and wrong scope.  For example, at
p = 5, w = (sigma_0 sigma_1 rho_1)^6 has six maximal reflection runs, all of even length, but 12 constant blocks of length 1, so
o_F = 12 > p and w lies outside the corollary.  That decomposition cuts
every maximal cyclic reflection run at every change of letter; see proof-K0star-r2.md L22-25.  In it an empty rotation run
always lies between blocks of different values (L25).
**Corollary REFL-few-odd.**  Let p >= 5 be prime, and let w0 be a word of length 4p - 2 over D_(2p) such that
 (i)   all rotation letters of w0 lie in one set {rho_x, rho_-x}, x != 0;
 (ii)  w0 is an avoider, i.e. it has no identity 2p-subword in increasing index order;
 (iii) o_F(w0) <= p.
Then every maximal cyclic reflection run of w0 is constant.
* Nothing else is assumed of w0.  In particular there is no INV* hypothesis, no RGR hypothesis ON w0 [r3, Claude m6], and no
  condition on kappa, A, B, k, run lengths, block lengths or reflection values.  RGR theorems (I1)-(I4) are used only on the RGR
  words that RED's exits produce.
* Standing imports (Sec. 2) [r3, Claude m6]: (I1)-(I4), K0*, Theorem RED and its proof (RED-r2), and B0S-r3 / MXG-r2 with the
  errata listed in the small-k verdict (L44-48).
* Relative to REFL(p) (README.md L17-19: "every avoider w of length 4p-2 over D_(2p) whose rotation letters all lie in one set
  {rho_x, rho_-x}, x != 0, has every maximal CYCLIC reflection run constant"), the only restriction is (iii).
* Words without reflections are vacuous.  Words without rotations are handled by Lemma AR, exactly as in the proof of Theorem RED
  [r3, Claude m7: Lemma AR is cited at RED-r2 L138-139 and K0star-r2 L66-67, L161].
Remark (sub-blocks).  Suppose a word is given by any cyclic constant-block representation, in which adjacent blocks may have equal
values across empty runs.  Then its o_F is at most the number of odd blocks of that representation.  Passing to the maximal
decomposition fuses equal-valued blocks across empty runs: odd + odd -> even and odd + even -> odd, so the odd count never rises.

## 2. Imports (accepted texts only; list completed in r3 [Claude m1])

1. **Theorem RED and its PROOF.**  Source: proof-RED-r2.md, sha256 c4e7697f0f691980e19ef3332a1e2c6b0dbdc76ba268e87c32eb563f4d3fd3d7.
   It is CORRECTNESS-ACCEPTED in R/olson-reflection-K0star-RED-parent-verdict-v1.md (sha256
   879aeee781a080d1b1cb4a4489f62e45e2fa332f7c2d9242f725cfae1d00c02a, L8: "Assume the accepted RGR imports (I1)-(I4) at their
   stated scopes, plus K0*").
   * Used: not only the statement but the proof, RED-r2 L136-164: the normalisation; the moves P1-P4 (L140-147); Exit P3
     (L150-151); Exit P1 (L152-161); and the terminal state (L162-164).
   * Imported through it, applied inside that proof only to the words it produces, at their stated scopes:
     - (I1)-(I4) of RED-r2 L23-37 (parent-accepted RGR results);
     - Theorem K0*;
     - from proof-K0star-r2.md (sha256 6681676e4f80018e792c7117ce9fc524a31aeb397c35880f57468ada9c0396e1, same verdict): the move
       lemmas FUS (L84-97), TR (L104-106) and PM0 (L107-114; its bookkeeping is at L113-114 [r3, Claude m4]), and the
       decomposition definitions (L22-30);
     - [r3, Claude m1] everything else that RED-r2 and K0star-r2 use, at their accepted scopes:
       * GRX (rotation/notes-GRX-v1.md, afc6c31a...620b1a30) and PM* (rotation/proof-ROT-lowodd-v1.md Sec. 1, 8ba3e6c7...f9785).
         Both enter only through RED-r2 L17-22 and K0star-r2 (GR0, PM0), at the scopes of the K0*/RED verdict (L7-8, read with
         its dispositions at L39).
       * Lemma H0 (K0star-r2 L55-65).
       * Theorem P, EGZ / Lemma AR and Davenport-alpha (RED-r2 L38; K0star-r2 Sec. 1).
       * Lemma M0 of inverse-run-count/proof-RUNS.md L408-410, used for P4 (RED-r2 L146).
       * Lemma BC of inverse-parity/proof-PAR-K0.md, via BC' (K0star-r2 L129).
       * SING, KB*, CAP, KBH*, K1*, TII and QQ (RED-r2 Secs. 1-4).
   * Not used: proof-RED-r3.md (9eb74e96...e3e6) and proof-K0star-r3.md (845d2ddf...ba1d).  Both are unreviewed documentation
     successors.  Every citation here is to the accepted r2 texts.
2. **The small-k verdict.**  Source: R/olson-reflection-smallk-parent-verdict-v1.md, sha256
   b71fcaf461a98bf9f034871208a298a471dcbb2006aa26c9153d523e140413b8, L3 and L13: "RES_<(p) has no avoider with k <= p, for every
   prime p >= 5".  It rests on B0S (proof-B0S-r3.md, 95851b9c...1ee) and MXG (proof-MXG-r2.md, f2235ed9...ae2f), with their imports
   (verdict L30, L46) and the errata of L44-48.
   RES_<(p) is defined in RED-r2 L132-133.
3. **New in this file, unreviewed:** Claim MON (Sec. 3).
[r3, Claude m1] No rotation-RIGIDITY result (no ROT, SHgen or INV* statement) is used.  The only rotation-lane files that enter
are GRX and PM*, through RED-r2 and K0star-r2 at their accepted scopes.  No finite computation is used.

## 3. Proof (unchanged from r1; line citations added)

Suppose w0 violates the conclusion.  The proof of Theorem RED (RED-r2 L136-164) normalises x = 1 and A >= B.  [r3, Claude m3]
Both normalisations are automorphisms (K0star-r2 L15-16, L35-36).  They change block VALUES, but they preserve the block
partition, the block lengths and the inequality of neighbouring values, hence k, g, H and o_F.  It then applies the first applicable move among P1-P4 until none applies.  Every exit with g = 0 (Exit P1, Exit P3) is
contradictory there.  The terminal state with g >= 1 is an avoider in RES_<(p) with kappa >= 2.  In RES_<(p) every block is odd, so
its number of runs is k = o_F.
**Claim MON.**  o_F never increases along P1-P4.
Given MON, the terminal word has k <= o_F(w0) <= p, which the small-k verdict excludes: a contradiction.
Proof of MON.  Throughout, an empty run of the maximal decomposition lies only between blocks of different values.
* P1 (FUS; K0star-r2 L84-97).  An even block E is recoloured to the value u of a block X adjacent to it across an empty run.
  X and E fuse, and the result has the parity of X.  If the run on E's other side is empty and the block Y there also has value u,
  X, E and Y all fuse (a "double fusion", L95-97), and the new block has the parity of |X| + |Y|.  Before the move the three blocks
  contribute the odd ones among X and Y.  After it, the merged block is odd iff exactly one of X, Y is odd.  So o_F drops by 2 or
  is unchanged.
* P2 (PM0; K0star-r2 L107-114, bookkeeping L113-114 [r4, Claude m4]).  Two nonempty runs R_j, R_(j+1) are merged and the even
  block S_j is appended to S_(j+1).
  S_(j+1) keeps its parity, S_j (even) disappears, and the merged run is nonempty, so nothing fuses.  o_F is unchanged.
* P3 (TR-fill; K0star-r2 L104-106, RED-r2 L142-143).  One rho_1 rho_-1 pair moves from a run with r >= 3, which stays nonempty,
  into an empty run.  No block changes, and none splits, since the filled run lay between different values.  o_F is unchanged.
* P4 (M0'; RED-r2 L144-147).  The two letters of a (1,1)-run are deleted, and sigma_y sigma_y is inserted into a block, which keeps
  that block's parity.  The neighbours of the new empty run fuse if they have equal values: odd + odd -> even, odd + even -> odd,
  even + even -> even.  So o_F drops by 2 or is unchanged.  []
[r3, Claude m5]
* RED-r2 L147 says that a P4 fusion "lowers kappa by one more".  That is the overstated bookkeeping noted in the K0*/RED
  verdict (L39) and corrected in RED-r3: the extra drop happens only when both fused blocks are odd.  MON does not use it.
* One-line check.  o_F = F - 2H over the maximal blocks (K0star-r2 L29-30), so Delta o_F = Delta F - 2 Delta H:
  - P1 single fusion: (0, 0);
  - P1 double fusion: (0, [both odd]);
  - P2, P3: (0, 0);
  - P4 with unequal neighbours: (+2, +1);
  - P4 with fusing neighbours: (+2, 1 + [both odd]).
  So Delta o_F is in {0, -2}.

## 4. Interface to the rotation lane (ROT-few-E)

**How to apply.**  A user must check, for the word u to which REFL is applied:
* (0) p >= 5 is prime and u is a word over D_(2p) [r3, Claude m9];
* (a) |u| = 4p - 2;
* (b) the rotation letters of u lie in one set {rho_c, rho_-c}, c != 0;
* (d) o_F(u) <= p, computed from the MAXIMAL decomposition of u.  It suffices that u has some cyclic constant-block representation
  with at most p odd blocks (Remark, Sec. 1).
Then: if u avoids, every maximal cyclic reflection run of u is constant.  Equivalently, if u satisfies (a), (b) and (d) and has an
empty rotation run between two blocks of different values, then u has an identity 2p-subword.
**Report by OlsonRotationRigidity (IRC after 07:02 PDT; I have not checked the file).**  rotation/proof-ROT-few-E-v1.md
(79f6e2f1...b897) applies REFL to two words:
* u°(h): length 4p - 2, rotations in {rho_c, rho_-c}, and blocks the k blocks of their normal form (all odd, every empty run
  between DIFFERENT values, every block nonempty).  [r3, Claude m8] The rotation runs of u°(h) need not stay nonempty, so that
  representation need not be maximal.  By the Remark (Sec. 1), o_F(u°) <= k <= o_F(w) <= (2p + 4)/5 <= p.  See
  ROT-few-E-v1 L19-20, L32-34, L39-47; ROT-few-E-v2 is cb4bca7b...917e;
* w itself, with o_F(w) <= (2p + 4)/5 <= p.
On that report both instances satisfy (0), (a), (b), (d).  Whether ROT-few-E's own hypotheses are met is for its reviewers.
[r3, Claude m9] Caller-side obligations if ROT-few-E is rebased on this corollary:
* its Lemma SHgen-E, stated under (K) only (which allows k > p), must carry k <= p through its induction.  At its only call
  k <= (2p + 4)/5 <= p;
* condition (d) must be checked for the base word u°(h) at every induction level.  This depends on SHgen-v2, which is not
  audited here.

## Fix map r1 -> r2 (parent request; documentation only)

1. Imports.  RED is cited as the accepted r2 text, with full SHA and line ranges, and the PROOF of Theorem RED (not only its
   statement) is named as used.  The K0star-r2 move lemmas are cited with line ranges.  RED-r3 and K0star-r3 are explicitly not
   used.  The small-k verdict is cited with full SHA and lines.
2. Scope.  The hypotheses (i)-(iii) are listed, with o_F taken from the maximal decomposition.  It is stated that no INV*, RGR or
   kappa hypothesis is placed on w0.
3. The r1 "Use" paragraph is replaced by the interface of Sec. 4 and the peer's report.
The statement and the proof are unchanged.

## Fix map r2 -> r3 (Claude review R/olson-refl-fewodd-r2-claude-v1.note.md; errata only)

- m1 (r2 L5, L29-49): the import list is completed.  It now lists GRX, PM*, H0, Theorem P, EGZ/AR, Davenport-alpha, Lemma M0,
  Lemma BC, SING, KB*, CAP, KBH*, K1*, TII, QQ, and the B0S/MXG imports and errata.  "No rotation-lane result" is replaced by
  "no rotation-RIGIDITY result; GRX/PM* enter only via RED-r2/K0star-r2 at their accepted scopes".
- m2 (title, Sec. 1): "maximal CONSTANT reflection blocks", with the p = 5 example of the wrong (runs) reading.
- m3 (r2 L53-54): the normalisations change values but preserve the partition, the lengths and the neighbour inequality.
- m4 (r2 L65): PM0 is cited as K0star-r2 L107-114, with its bookkeeping at L113-114.
- m5 (r2 L69-71): RED-r2 L147's overstated kappa bookkeeping is noted; the o_F = F - 2H check is added.
- m6 (r2 L14-20): the standing imports are stated; "no RGR hypothesis ON w0".
- m7 (r2 L23-24): Lemma AR is cited at RED-r2 L138-139 and K0star-r2 L66-67, L161.
- m8 (r2 L82-88): "o_F(u°) = k" is replaced by "o_F(u°) <= k (Remark)", with the ROT-few-E citations.
- m9 (r2 L75-81): "(0) p >= 5 prime, u over D_(2p)" is added, and the caller-side SHgen-E (k <= p) and base-case (d)
  obligations are stated.
The statement (except for the title wording) and the proof are unchanged.

## Fix map r3 -> r4

- m4 completed: the P2 bullet of Sec. 3 (r2 L65 = the line Claude cites) now cites K0star-r2 L107-114, with its bookkeeping at
  L113-114.  r3 had changed only the import-list citation.  Nothing else changed.
