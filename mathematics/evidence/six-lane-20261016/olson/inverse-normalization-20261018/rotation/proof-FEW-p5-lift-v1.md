# INV*-FEW (a) and OLSON-FEW (a) at p = 5 with o_F <= 4: lift note, v1

Owner OlsonRotationRigidity.  Written after host clock 2026-10-18T10:22:24-07:00.  Status [W]: combination note, no new
lemma.  CONDITIONAL on C5 (ROT-o4 at p = 5; parent verdict pending, Sec. 1.3) and on the parent-accepted texts pinned
in Sec. 1, at their accepted scopes.  Status "conditional, unaudited" until the narrow Codex review requested by the
parent.  Written for MAJOR M1 of the Claude complete-claim review R/olson-p5o4-complete-claim-claude-v1.note.md
(sha256 7816550f746a00ee330cd83a3613d9103f6d423e1820664985d5f9d0dd006a5f, L97-110).  That review graded the lift
stated at proof-ROT-o4-p5-finite-v2.md L61-63 INCONCLUSIVE on its packet.  No existing file is edited.
Paths: T = mathematics/evidence/six-lane-20261016/olson/inverse-normalization-20261018/, R = institute/runs/six-lane-
2026-10-16/review/, both under /Users/jinleic/repos/aifours.  "Lx" are line numbers of the pinned file named.
Notation as in the pinned texts: D_(2p) with (v,e)(v',e') = (v + e v', e e'), rho_x = (x,+1), sigma_y = (y,-1).  An
avoider has no identity 2p-subword in increasing index order.  o_F(w) is the number of odd blocks in the maximal cyclic
constant-block decomposition (every maximal cyclic reflection run cut at every change of value).  INV* for w: all
rotations in one {rho_c, rho_-c}, c != 0, and every maximal cyclic reflection run constant; RGR is the same shape.

## 0. Claims

**L-INV (INV*-FEW (a) at p = 5).**  Every avoider w of length 18 over D_10 with o_F(w) <= 4 satisfies INV*.
**L-OLS (OLSON-FEW (a) at p = 5).**  Every word w of length 19 over D_10 with o_F(w) <= 4 has an identity 10-subword
in increasing index order.
For o_F <= 3 both are already parent-accepted (R/olson-fewodd-parent-verdict-v1.md L6-7).  The new content is o_F = 4
at p = 5.  With the accepted p >= 7 statements, INV*-FEW (a) and OLSON-FEW (a) then hold with the range o_F <= 4 for
every prime p >= 5.

## 1. Pinned texts and the verdicts that accept them  [item (a)]

1.1 Theorem texts (paths under T).

| role | file | sha256 | accepted by (file under R, lines) |
|---|---|---|---|
| INV*-FEW | rotation/proof-INVstar-few-v3.md | 779218b4a92c29c996172c361052d2ac9c16cbca003f49921af3713b3ca05531 | olson-fewodd-parent-verdict-v1.md L6, L12 (part (a)); addendum-1 L6, L13 (part (b)) |
| OLSON-FEW | rotation/proof-OLSON-few-v3.md | ae151f9b38af60ba3a16b954f470b53976317fede4efddc8181fb98ce18cd66a | olson-fewodd-parent-verdict-v1.md L7, L12; addendum-1 L7, L13 |
| REFL-few-odd, text of record | reflection/proof-REFL-fewodd-r4.md | 1e447754e8c7238c2a1918254f674cfb9a4889015a845517e3170087f932861d | olson-refl-fewodd-parent-verdict-v1.md L6 |
| REFL-few-odd, current errata (statement and proof unchanged: r5 L3-6, L171-178) | reflection/proof-REFL-fewodd-r5.md | 4615dcb957966ee4c18166c269e1c9c8a1bc4ee6f9bc48539155079b297a5363 | errata-only successor of r4 |
| REFL-few-odd, Codex-reviewed text cited at INV*-FEW v3 L10 and OLSON-FEW v3 L10-11 | reflection/proof-REFL-fewodd-r2.md | db16274fffccde41e65025a46c4992bb3c11c26bce9bcc97f5bc3efaae65c2c6 | olson-refl-fewodd-parent-verdict-v1.md L6 (r4 is its errata-only successor), L9 |
| ROT-o2 with K1, K2, PM* | rotation/proof-ROT-lowodd-v1.md | 8ba3e6c7eeff5ec556166b76eb014d8141d5541c9c702ec3f537e602522f9785 | olson-rotation-lowodd-parent-verdict-v2.md L8-9, L12 |
| GRX | rotation/notes-GRX-v1.md | afc6c31a2f9c9502655e3666595e535f4a003ccd7670ddbe993ebe4b620b1a30 | olson-rotation-lowodd-parent-verdict-v2.md L7, L13 |
| ROT-o3, reviewed text | rotation/proof-ROT-o3-v3.md | 9b0a37dbcb30b9f989c530d74a9106b8ea312072860fae349232492a329b9ab7 | olson-rotation-o3o4-parent-verdict-v1.md L7 |
| ROT-o3, wording errata (no proof step changed, v4 L3-9) | rotation/proof-ROT-o3-v4.md | 55670658a819af5ef5570fa71137ad51ee111e46e720cbac5bfdbfd7f51be8cf | same verdict (parent-listed fixes) |
| ROT-o4, reviewed text | rotation/proof-ROT-o4-v2.md | 878fd123cf69941b0e4f0f86e0dde20ab7fb29481c61c30a4b81e8b34fa1e741 | olson-rotation-o3o4-parent-verdict-v1.md L8-11: p >= 7 only |
| ROT-o4, restated for p >= 7 | rotation/proof-ROT-o4-v3.md | db4eee8a5a43aee17a4bef38f79792a3488c9c7a4b8de4e6bcaa3e599550148e | same verdict L8, L22-27 |
| ROT-o4, wording errata (no proof step changed, v4 L3-8) | rotation/proof-ROT-o4-v4.md | 7fa49e970603210639f1a0b834c54f5418859bc3dfaf164e34e67836cdaa425a | same verdict (parent-listed fixes) |
| RGR-LONG(p) | the RUNS assembly, through its verdict | (verdict below) | olson-runs-parent-verdict-v1.md L7 |

1.2 Verdicts (files under R).

| file | sha256 | statement lines used here |
|---|---|---|
| olson-fewodd-parent-verdict-v1.md | 375c534c3254ed5fe1a5ba0bcae6c86c65ca19529997f9fd322e03eb53d717a8 | L5-7 statements; L9 exclusion; L12 texts of record; L17 imports; L20 boundary |
| olson-fewodd-parent-verdict-v1-addendum-1.md | 279d89d2d74046745a0db7600e06956d9ab5c7c200a598aff78c2a37b33ba62a | L6-7 part (b); L19 p = 5 boundary |
| olson-refl-fewodd-parent-verdict-v1.md | 16436c07e2dc1b6b773989b2ff5d05900ea92f8e6c1d681b0c5979673688f1ca | L6 statement (every prime p >= 5, o_F <= p); L12 imports; L16 caller obligations |
| olson-rotation-lowodd-parent-verdict-v2.md | 0853f4ac231a63e76fd97e8c986686fe53c6758a771ee67c504435f8cf1cba29 | L7 GRX; L8 PM*; L9 K1/K2, ROT-o2 for every prime p >= 5 |
| olson-rotation-o3o4-parent-verdict-v1.md | 1225ce75847bfd748cacec51a5f0d41e1e686606b03b4b06a3c35112db34547f | L7 ROT-o3 for every prime p >= 5; L8-11 ROT-o4 for p >= 7 only, p = 5 not accepted |
| olson-runs-parent-verdict-v1.md | 82adbdddd87dff5af0ef8e0e1ceb82b2a20257213966ae45789811a91a859237 | L7 RGR-LONG(p) for every prime p >= 5; L49 conjugation |
| olson-reflection-K0star-RED-parent-verdict-v1.md | 879aeee781a080d1b1cb4a4489f62e45e2fa332f7c2d9242f725cfae1d00c02a | L7 K0* for every prime p >= 5; L8 RED |
| olson-reflection-smallk-parent-verdict-v1.md | b71fcaf461a98bf9f034871208a298a471dcbb2006aa26c9153d523e140413b8 | L3: RES_<(p) has no avoider with k <= p, every prime p >= 5 |
| olson-reflection-smallk-errata-binding-v1.md | f3b712ca4cd1218cabcc524227daa5df817077d08b80257d62fa734c2e619fcb | errata of the small-k verdict |

Reviews read for the exclusion reason: R/olson-fewodd-chain-claude-v1.note.md
(6f130cfeb4417fd708287d406418b4e199e9b3d810ec235e7ac0e6e70e0ffabc, L18-28); R/olson-olsonfew-v2-codex-v1.note.md
(878d6c804413823f88cfe60c151c1867988f050f01f54a560fc89419579221c7); R/olson-roundC-codex-v1.note.md
(233778ccab9efe4a5d5a346bd5a9c13797a90b969a057906cd7e5506a6a2b581).

1.3 The new input C5 (parent verdict pending at the time of writing).
**C5.**  Every word of length 18 over D_10 with no identity 10-subword in increasing index order and exactly four odd
blocks in its maximal cyclic constant-block decomposition has all rotation letters in one {rho_c, rho_-c}, c != 0.
This is ROT-o4's statement (proof-ROT-o4-v4.md L121-122) at p = 5 word for word: 4p - 2 = 18, D_(2p) = D_10, 2p = 10.
Like ROT-o2/o3/o4 it is stated for every avoider with exactly four odd maximal constant blocks and assumes nothing about
run constancy.  Sources:
- rotation/proof-ROT-o4-p5-finite-v2.md c2ce5f0a5dd5582e13ba873c0b1690efd3b4e87bf943bf5ee0e9a62a76517e2f (statement L19-21);
- rotation/p5o4-v1/PLAN-v1.md 7d7793cbf137f2ddf01d7cc64872657ba26d15fbac0276101894972038e50588 (C5 L10-12; reduction
  C5 -> C5' through PM*, Sec. 2 L16-28);
- run1: rotation/p5o4-v1/out/run1/verdict-v2.json 780f0b6f7c8c0693888c48f23b2f8ba59514be8dd016f899664e6630624b5e30 and
  dp_avoiders.txt 78a91ba247016568e5b23ba06d5b6221ca989211ddaf79f82229e7c5807d5967;
- parent replay: R/olson-p5o4-parent-replay-v1/RESULT-v1.json
  d823a969064fbf473ea9ab8288b487dbd75c3b68608e857fb3ae6aa7e9efddf1 and NOTE-v1.md
  1c3ae5faab8df3518cd578c98ed5a287766b80016e4c9987783058bb13a555ec.  NOTE L9-21: C5' CONFIRMED on D, and the parent
  avoider list is byte-identical to dp_avoiders.txt.  NOTE L20-21: the reduction is not re-audited there;
- reduction audit: R/olson-p5o4-complete-claim-claude-v1.note.md L13-26 (A1: PM* re-derived in the PLAN-v1 L20 form),
  L143-148 (C5 established after fixes, and with it ROT-o<=4 for every prime p >= 5);
- comparator and code: R/olson-p5o4-comparator-v2-codex-v1.note.md
  e559b597b84d3ff4ca81ae8b2fa1be4d1ed0de7e33f4ddcb02c1167c8e5c9d36 (ACCEPT 0/0/0) and
  R/olson-p5o4-code-result-codex-v1.note.md e0504765e211dbc6d628b2bfbfaf286cb2253eeac406be624be2d839c39c6468
  (ACCEPT-WITH-FIXES; both fixes applied in compare_p5o4_v2.py).

## 2. ROT-o4 at p = 5 was the only reason for the exclusion  [item (b)]

2.1 Every p >= 7 restriction in the texts of the (a) chain.  Search: the regular expression
`p\s*(>=|≥|>)\s*(6|7|11|13)\b`, plus the string "p = 5", over INV*-FEW v3, OLSON-FEW v3, ROT-lowodd-v1, ROT-o3-v3/v4,
ROT-o4-v2/v3/v4 and notes-GRX-v1.  The search also covered the whole reflection/ directory: REFL-few-odd r1-r5 and its
imports RED-r2, K0star-r2, B0S-r3 and MXG-r2.  It covered every verdict in 1.2 as well.  These are all the hits:

| # | location | text (abridged) | traced to |
|---|---|---|---|
| 1 | INV*-FEW v3 L22 | "(a) If o_F(w) <= 3, or p >= 7 and o_F(w) = 4" | #2 |
| 2 | INV*-FEW v3 L31-32 | "ROT-o4 (accepted for primes p >= 7)" | ROT-o4's accepted scope (o3o4 verdict L8, L11) |
| 3 | INV*-FEW v3 L54-55; the same lines quoted inside its errata diffs, L112-113, L146, L175-176 | "p = 5 with o_F = 4 is not covered by (a) (ROT-o4 is accepted only for p >= 7)" | #2 |
| 4 | OLSON-FEW v3 L23 | "(a) If o_F(w) <= 3, or p >= 7 and o_F(w) <= 4" | the range B of INV*-FEW (a), imported at L28-30, i.e. #1 |
| 5 | ROT-o3-v4 L32 (= diff L138) | "(for p >= 7, m >= ...; for p = 5 and e <= 2, ...) unless p = 5, e = 3, ..." | a case split inside Lemma INC that covers p = 5; ROT-o3 is accepted for every prime p >= 5 (o3o4 verdict L7); not a restriction |
| 6 | ROT-o4-v2 L1, L18, L67, L104, L117, L120; v3 L1, L5-6, L21, L70, L108, L120, L122; v4 L1, L4, L22, L71, L109, L121, L123, L168-169; v4 Sec. 5 L134-147 | the written ROT-o4 proof for p >= 7; p = 5 only through the unaudited lane census | ROT-o4 itself; replaced at p = 5 by C5 (Sec. 3) |
| 7 | fewodd verdict v1 L6, L7, L9, L17, L20 | L6-7 "or with p >= 7 and o_F(w) = 4" / "<= 4"; L9 "The case p = 5 with o_F = 4 is excluded here (ROT-o4 is accepted only for p >= 7)"; L17 "ROT-o4 (p >= 7)"; L20 boundary "o_F >= 4 at p = 5" | #2; the verdict names the reason at L9 |
| 8 | addendum-1 L7, L19 | "(a): o_F <= 3 for p >= 5, <= 4 for p >= 7"; "until accepted, part (a) at p = 5 stays at o_F <= 3" | #7 and the pending p = 5 verification |
| 9 | o3o4 verdict L8, L11, L15-16, L22-27, L36 | ROT-o4 "for primes p >= 7 only"; L11 "Not accepted: the p = 5 case of ROT-o4 ... rests only on an unaudited exhaustive D10 census"; L36 "Open in rotation: ... (and = 4 at p = 5)" | the census; replaced by C5 |

No hit in ROT-lowodd-v1, notes-GRX-v1, REFL-few-odd r2/r4/r5, RED-r2, K0star-r2, B0S-r3 or MXG-r2.  The only
reflection/ hit is the status file reflection/results.md L36-37, which is not an import.  No hit either in the lowodd
v2, REFL, RUNS, K0*/RED, small-k or errata-binding verdicts.  The independent reviewer gave the same reason: Claude
few-odd chain review L25-26 (read with OLSON-FEW v2 line numbers): "INV* is needed exactly up to B: B = 3 at p = 5
(ROT-o3 is accepted for p >= 5) and B = 4 at p >= 7.  p = 5 with o_F = 4 is correctly excluded.  Case 3 would need
INV* at o_F = 4, p = 5, which neither (a) nor (b) supplies (5·4 > 14)."

2.2 Every p-dependent condition of the (a) chain, evaluated at p = 5.  Every other condition concerns one fixed word.

| condition | where | at p = 5 |
|---|---|---|
| p >= 5 prime | INV*-FEW v3 L21; OLSON-FEW v3 L22; REFL r4 L21 and r5 L25 (interface (0): r4 L110, r5 L117); ROT-o2 (lowodd verdict v2 L9); ROT-o3 (o3o4 verdict L7); RGR-LONG (RUNS verdict L7); K0* (K0*/RED verdict L7); small-k (small-k verdict L3) | holds |
| o_F(u) <= p for the word u that REFL is applied to | REFL r4 L24 (iii) and L113-114 (d); r5 L28 and L120-121; INV*-FEW v3 L35 "o_F(w) <= 4 <= p" | 4 <= 5 |
| o_F(w) <= B <= 2p - 3 | OLSON-FEW v3 L34 (Case 1) | B = 4 <= 7 |
| F >= 4p - 3 and (F - o_F(w))/2 >= p | OLSON-FEW v3 L31, L33 | F >= 17; F - o_F(w) is even (F = sum of the block lengths, = o_F mod 2) and >= 13, so >= 14: at least 7 >= 5 disjoint pairs |
| lengths 4p - 2 and 4p - 1 | throughout | 18 and 19 |

So "o_F <= 4 <= p" admits p = 5 without any p >= 7 lemma.  REFL-few-odd is accepted for every prime p >= 5 with
o_F <= p (REFL verdict L6), and its text assumes only that p >= 5 is prime (r4 L21-25).  It imports RED-r2, whose
(I1)-(I4) come from the RUNS and PAR/MIX_low verdicts; K0*, accepted for every prime p >= 5; and the small-k verdict,
for every prime p >= 5.  By 2.1 none of these texts contains a p >= 7 restriction.  The only p >= 7 restriction in the
(a) chain is therefore ROT-o4 (#2), and C5 supplies ROT-o4 at p = 5.

## 3. Proof of L-INV

Let w be an avoider of length 18 over D_10, and o := o_F(w) <= 4.  Rotations (INV*-FEW v3 L30-35 with p = 5):
- o = 0 is impossible (ROT-o2: lowodd verdict v2 L9; F = 0 is excluded by EGZ, ROT-lowodd-v1 L86);
- o in {1, 2}: ROT-o2;  o = 3: ROT-o3 (accepted for every prime p >= 5);
- o = 4: C5, in place of ROT-o4.
So the rotations lie in one {rho_c, rho_-c}, c != 0.  Reflections: REFL-few-odd applies to w by its interface (r4
L110-114).  (0) p = 5 is prime.  (a) |w| = 18 = 4p - 2.  (b) The rotations lie in the pair just found.
(d) o_F(w) = o <= 4 <= 5 = p.  So every maximal cyclic reflection run of w is constant.  []
Only o = 4 uses C5.  For o <= 3 this is the accepted INV*-FEW (a) at p = 5.

## 4. Proof of L-OLS, with every call at p = 5  [item (c)]

The proof of OLSON-FEW v3 (L28-47) is used verbatim with p = 5 and B = 4.  Let w have length 19 and o := o_F(w) <= 4,
and suppose w has no identity 10-subword.  Then every subword of w avoids.

4.1 Deletions and insertions (this is all of them).
(D1) Case 2 (L37-39) deletes ONE letter of an odd maximal constant block S with |S| >= 3.  S keeps at least 2 letters, so
no rotation run changes, no two blocks become adjacent and nothing splits.  Only the parity of S changes, from odd to
even.  Hence o_F(w') = o - 1 exactly.
(D2) Case 3 (L40-46) deletes ONE rotation letter x_i, giving two separate words w_1 and w_2.  If the run of x_i stays
nonempty, the decomposition is unchanged.  Suppose the run becomes empty.  As R >= 3, some other rotation run is
nonempty, so the reflection runs on either side of it are different runs.  Let X be the last block before the run and
Y the first block after it.
- If X and Y have different values, they keep their identity; the merged maximal reflection run now contains a value
  change.
- If they have the same value, they fuse into one block of that value, of length |X| + |Y|.  Odd + odd gives even, and
  o_F drops by 2.  Odd + even gives odd and even + even gives even, and o_F is unchanged.
The outer neighbours of the fused block already differ from its value, or are separated from it by rotation runs, so
nothing cascades.  Hence o_F(w_i) is o or o - 2.  Compare the Claude chain review L22: "at most one fusion and no
cascade".
(D3) The following are never done in part (a):
- deleting a letter of an EVEN block.  That would raise o_F by one: an even block of length l >= 2 becomes odd, of
  length l - 1.  OLSON-FEW v1, which deleted an arbitrary letter, therefore needed INV* up to o + 1 = 5 at p = 5, which is
  not available.  v1 is not used here;
- deleting a block of length 1, which removes an odd block and may fuse its neighbours;
- deleting a reflection in Case 3;
- deleting two letters from one word;
- any insertion before a call.
(D4) Insertions occur only in deductions, never before a call.
- Case 2 (L38-39) puts the deleted sigma_y back inside its own constant block.  The rotations are unchanged.  The maximal
  reflection runs of w are those of w', with one run longer by a letter equal to its neighbours, so they stay constant.
- Case 3 (L43-46) puts x_i back into its run.  Every rotation of w lies in w_1 or in w_2, hence in their common pair.
  Two cyclically adjacent reflections of w with different values stay adjacent in w_1.
No INV*, ROT or REFL statement is applied to a word obtained by an insertion.

4.2 Every call, with o_F of the word it is applied to.

| case (OLSON-FEW v3 lines) | statement called | word | length | o_F of that word | accepted scope covering the call |
|---|---|---|---|---|---|
| 1, R <= 2 (L31-36) | none: equal pairs in a cyclic frame, or sigma_y^(2p) = 1; conjugation back (RUNS verdict L49) | w | 19 | o <= 4 (only o <= 2p - 3 = 7 is used) | none needed |
| 2 (L37-39) | INV*-FEW (a) | w' = w minus one letter of an odd block of length >= 3 | 18 | o - 1 <= 3 (D1) | fewodd verdict L6 (o_F <= 3, every prime p >= 5) |
| 2, inside that call | ROT-o2 (o - 1 <= 2) or ROT-o3 (o - 1 = 3) | w' | 18 | <= 3 | lowodd verdict v2 L9; o3o4 verdict L7 |
| 2, inside that call | REFL-few-odd | w' | 18 | <= 3 <= 5 | REFL verdict L6 |
| 3 (L40-46) | INV*-FEW (a), twice | w_i = w - x_i, i = 1, 2 | 18 | o or o - 2, so <= 4 (D2) | o_F(w_i) <= 3: fewodd verdict L6; o_F(w_i) = 4, possible only if o = 4: L-INV |
| 3, inside those calls | ROT-o2, ROT-o3 or C5 | w_i | 18 | <= 2, = 3 or = 4 respectively | lowodd verdict v2 L9; o3o4 verdict L7; C5 (parent verdict pending) |
| 3, inside those calls | REFL-few-odd | w_i | 18 | <= 4 <= 5 | REFL verdict L6 |
| 2 and 3 (L47) | RGR-LONG(5) | w, RGR by (D4) | 19 | no o_F hypothesis | RUNS verdict L7 (every prime p >= 5) |

An INV* call on a word with o_F = 0 is vacuous: no avoider of length 18 has o_F = 0 (ROT-o2), so that branch closes at
once.  C5 is called only in Case 3, with o = o_F(w_i) = 4.  No call is made to INV*-FEW (b), Theorem SHgen, Lemma
SHgen-E, ROT-FEW, ROT-FEW-E, KAPPA01 or ELT0-FEW.

4.3 The k <= p conditions.
- REFL-few-odd (iii) and (d), o_F(u) <= p, hold at every REFL call: 3 <= 5 in Case 2, and 4 <= 5 in Case 3 and in
  L-INV.
- Inside REFL-few-odd, the terminal RES_<(p) word has k <= o_F(w0) <= p by Claim MON (r5 L82-87).  The small-k verdict
  excludes it for every prime p >= 5 (L3).  The caller has no further obligation.
- REFL-few-odd's caller-side obligation to carry k <= p through Lemma SHgen-E (r4 L125-129, r5 L134-138, REFL verdict
  L16) concerns part (b) only.  Part (a) never calls SHgen-E.
- RED's (I3) split, K0 for k <= p and branch C2 for k >= p + 1 (RED-r2 L32-35), and the RUNS assembly's o_F <= p /
  o_F >= p + 1 branches (RUNS verdict L47) are internal case splits, not hypotheses on the caller.
- C5, ROT-o2 and ROT-o3 have no k <= p hypothesis.  The reduction of C5 ends with k = 4 blocks (PLAN-v1 L22-25).
- OLSON-FEW Case 1 uses o <= B = 4 <= 2p - 3 = 7.

4.4 Conclusion.  In Cases 2 and 3, w is RGR by (D4), and RGR-LONG(5) gives w an identity 10-subword: a contradiction.
Case 1 gives one directly.  So L-OLS holds.  []

## 5. Scope and status

- CONDITIONAL on (i) C5: finite exact, obtained from PLAN-v1 Sec. 2 via the accepted PM* and the run1 decision of C5'.
  The parent replay CONFIRMED C5' (NOTE-v1 L9-21).  The Claude complete-claim review re-derived the reduction (A1).
  The parent verdict is pending.  (ii) The parent-accepted texts of Sec. 1, at their accepted scopes.
- Status "conditional, unaudited" until the narrow Codex review requested by the parent; the parent verdict decides.
- Covered: INV*-FEW (a) and OLSON-FEW (a) at p = 5 with o_F <= 4.  With the accepted p >= 7 statements this gives
  o_F <= 4 for every prime p >= 5.  Part (b) at p = 5 (5 o_F <= 14, i.e. o_F <= 2) lies inside (a).
- Not covered: INV*(5) and ordered Olson for D_10 with o_F >= 5; ROT with five or more odd blocks; any claim about
  reflection structure beyond REFL-few-odd's statement.  No novelty claim.
