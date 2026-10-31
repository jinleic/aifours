# Additive erratum 1 and supplement to author-candidate-v1

**Status.** This file adds to `author-candidate-v1.md` (27,145 bytes as written) and leaves that file unchanged. It was prepared after a line-by-line author self-check of the candidate against the same frozen packet. It changes no conclusion, quantifier, or case result. E1–E5 tighten justifications or wording. E6 makes the case accounting explicit. S1–S3 add an explicit F-set enumeration and two independent direct eliminations as cross-checks. This is nonblind, same-harness author material. It is not a review, disposition, or acceptance. No native clock was observed for this file, so it carries no timestamp claim.

## Corrections to the candidate

**E1 (§2, degree of twin columns).** The sentence "If their only two neighboring rows were degree two, those two orthonormal rows would span the two columns and isolate a 2-by-2 component" covers only the subcase where the second neighbor row also has degree two. Replace it with: *A twin column has degree at least two. Suppose both twins had degree two, with common neighbor rows r and r′. The 2-by-2 block on r, r′ and the twins then contains both entire columns. Its columns are therefore orthonormal and the block is unitary. Its rows then have unit norm inside the block, so r′ has no further entry. The block is an isolated 2-by-2 component, contrary to order greater than two.* The degree-at-least-three conclusion is unchanged.

**E2 (§2, order six).** Add: *A low column cannot meet a low row, because a low row's only neighbors are its twin columns, which have degree at least three. Hence both low columns have only high-row neighbors.* The partition argument then proceeds as written.

**E3 (§4, outside-a extension).** Add after (6): *The AB line (a,b) has multiplicity four, and its four words are exactly the words of (6) with B=b; similarly for AC and AD. Hence the third word on any high/high BC, BD, or CD pair cannot have A=a.*

**E4 (§4, the three mates).** Replace "gives three distinct mates: if two mates coincided, they and the starting word would give two outside-a extensions of one high/high pair. On the binary triple they are the three two-bit flips" with: *Each mate is high at B, C and D, shares the compared coordinate with w, and differs from w. It cannot share a second coordinate with w; otherwise w and the mate would be two outside-a extensions of one high/high pair, which has only one outside-a slot. So the mates found through B, C and D are the flips of (C,D), (B,D) and (B,C) relative to w: three distinct words.* The parity class and phase triangle then follow as written.

**E5 (status paragraph).** Replace "Equivalently, the F-edge set defined below is empty" with: *In particular, the F-edge set defined below is empty. Conversely, given the §4 surplus classification, an empty F set yields the stated degree and multiplicity conclusions.*

**E6 (§6, accounting for all ten unordered type pairs).** Items 1–6 treat nine of the ten unordered pairs from {X,Y,Z,W}. The tenth, **X/W**, is exactly residual case I of (7) after matched-label relabeling; crossed **Y/Z** is case II. The full accounting is: XX → item 3; XY/XZ → item 4; XW → case I; YY/ZZ → item 2; matched YZ → item 6, crossed YZ → case II; YW/ZW → item 5; WW → item 1. Both residual cases are eliminated in §6b, and independently in S2–S3 below.

## Supplement

**S1 (all F/T edge sets).** The six pair systems form three complementary pairs, and §2 forbids F on both members of one. Hence |F|≤3, and any two F edges are adjacent. The possible F sets are thus ∅, a single edge, two adjacent edges, a triangle, or a three-edge star. Every set with at least two edges contains two adjacent edges, which §5 excludes whatever the remaining edges are. §6 excludes a single edge. Hence F=∅.

**S2 (direct elimination of any single-X arrangement, including case I).** Suppose exactly one sparse row is X, relabeled as `(a_0,b_1)`. The other sparse row is not `(a_1,b_0)`. In the AC|BD cut, the row `(a_0,c)` consists of `(b_0,d_0),(b_0,d_1)` from the F row and `(b_1,d_X(c))` from the X row. This exhausts multiplicity three. The row `(a_1,c′)` contains `(b_1,d_0),(b_1,d_1)` and one more entry. If that entry had B=`b_0` and high D, then `(a_1,b_0)` would be a row of the 12-entry core, since every high-CD column lies in that core; it is not. The common entry `(b_1,d_X(c))` is therefore the only overlap. This contradicts actual orthogonality, and it covers X/Y, X/Z and X/W=case I simultaneously.

**S3 (direct elimination of case II).** Take sparse rows `(a_0,β)` and `(α,b_1)`, and fix high c. By core membership, the third word of the multiplicity-three AC line `(a_1,c)` has low D; write its BD entry `(x,y)`. Likewise, the second word of the multiplicity-two line `(α,c)` has low D (α has surplus zero); write its BD entry `(x′,y′)`. The rows `(a_1,c)` and `(α,c)` share `(b_1,d_Z(c))`, where `d_Z(c)` is the high D in the Z row's word at c. They can share nothing else except possibly `(x,y)=(x′,y′)`, so orthogonality forces `x=x′`. Since c has exactly one low D neighbor, whose line has multiplicity two, the two low-D words at c are precisely these two words. But the BC line counts at c (`b_0`: 2+1, `b_1`: saturated by 2+1, `β`: 1+1, no fourth neighbor because c has degree three) require their B symbols to be `b_0` and `β`, one each. Then x≠x′, a contradiction. This avoids (8) and the matching count, and agrees with §6b.

## Gap statement for f860 §§1–4

My reconstruction finds **no mathematical error and no missing case** in f860 §§1–4. It does find these unstated justifications, all supplied in the candidate or above:

* the twin-column degree-three step (E1);
* the reason why some high row avoids the twins at order five, k=1 (candidate §2);
* the low-column/high-row point at order six (E2);
* "outside a" for the extra high/high extension (E3);
* the double-flip property of the mates (E4);
* the low-D third entry in Y/W and the low-D second entry in matched Y/Z, both by core membership (candidate §6, items 5–6);
* the unnamed X/W pair, which is case I (E6).

f861 and its notation erratum remained nonblind context and were not used as premises. These are author findings, subject to separate independent checks and parent disposition. No global theorem, family, human, or formal acceptance, or priority is claimed.

## Process

No new source, link, held episode, held consumer, or peer science was read. No network, external model, code execution, subprocess, scientific evaluation, test, solver, build, lint, formatter, Git, deletion, or verifier preparation was used, so there is no code hash. The original candidate was not edited.
