# A stretched same-run two-rotation selector and one exact construction exception

Owner **MathOlson-2-2**. Native `/bin/date` immediately before writing: **Wed Oct 28 20:33:27 PDT 2026**. NEW **WRITTEN sufficient-condition candidate** with bounded actual-word checks in §5. Read mandatory fatal record `frontier-20261028-olson-actual-block-fatal-correction-v1.json`, SHA256 `e11fd87345f8a54012f3a9245d87491c6ceb3a4a113558be07ca4ab62728f90e`, first. No f111 review/adoption is transferred; no historical `o_F/e_F` inference is made.

## 1. Exact theorem candidate

Let p be an odd prime and W an actual dihedral word with F=3p−2 reflections. Its cyclic reflection-only projection has exactly p odd maximal constant runs, with pairwise distinct exponents; even projected runs are allowed. Suppose its ACTUAL cyclic word contains the consecutive segment

`σ_c ρ_u σ_c (σ_c)^h ρ_v`,  h>=0,  (1)

where all displayed reflections belong to the SAME odd projected run. There are no undisplayed occurrences inside (1). Its first σ_c need not be the first member of that projected run, and its final rotation can be at the end of or inside that run. Let q be the number of c-reflections in that projected run BEFORE the segment's first σ_c, and r the number AFTER its final displayed reflection, both in the cyclic projection run's natural order. Thus `2+h+r+q` is odd. Enumerate the other p−1 odd projected-run exponents in order after the c-run, starting just after (1) in the cyclic cut.

Then W has an original-order identity selector of exactly2p occurrences EXCEPT that the following precise constellation is not covered by this construction:

* `q=r=0`, `u+v=0`, `u!=0`; and
* setting `t=u−v=2u`, the other p−1 odd-run exponents, in the said cyclic order, are exactly `c+t,c+2t,...,c+(p−1)t`.

The exception is a statement that THIS construction has not paid that case; it is **not** a claim that no selector exists or a counterexample to Olson or L_RES. Rotations u,v may otherwise be zero, equal or unequal. There is no requirement that the word satisfy any other OLD/caller failure.

## 2. Pair accounting in the actual cut

Cut immediately before the first displayed σ_c. The h middle c-reflections occur between the second σ_c and ρ_v. After ρ_v come the r c-reflections, all other projected runs, then the q c-reflections at the end of the cut. Rotations other than the two displayed ones can all be skipped. In each of these three c-segments and each other projected run, pair equal reflections consecutively in the projection, reserving the last one of an odd segment. The p−1 other odd projected runs have one reserved representative each; their values are precisely F_p except c.

Before splitting, `(F−p)/2=p−1` equal pairs are available. The two distinguished σ_c leave `p−2` pairs when exactly ONE of h,r,q is odd, and `p−3` when all THREE are odd. In the latter case the two outside odd c-segments separately reserve one c at the beginning and one c at the end of the post-ρ_v cut. Actual full-word rotation gaps do not define or change this projection accounting.

A useful elementary fact is that every nonzero t occurs as `x_i−x_j` for some i<j in any linear ordering of all p field values: otherwise `position(x−t)<position(x)` for every x, contradicting the full additive t-cycle. When only F_p minus c is ordered, t is absent from the ordered differences if and only if the entire order is `c+t,c+2t,...,c+(p−1)t`: the same inequalities impose that single chain, and that order indeed has only differences `−kt`, 1<=k<=p−2.

## 3. Construction, all parity cases

Put `t=u−v`. Unless noted, keep the two distinguished σ_c and both displayed rotations; their product with NO other odd representative is `ρ_(v−u)=ρ_(−t)`. Equal pairs selected before or after ρ_v are identity subproducts and can be selected or omitted without changing that product.

**h even.** Exactly one of r,q is odd; after ρ_v there is one reserved c plus one reserved representative from each of the other odd runs, hence p distinct field values in some linear order. There are p−2 pairs total. If t=0 choose all pairs. If t!=0 choose two post-ρ_v representatives in order with difference t, and choose p−3 pairs. They give the required `ρ_t`.

**h odd; r,q odd.** There are p−3 pairs and two c representatives after ρ_v, one at each end. If t=0 take both c representatives. If t!=0 take the FIRST c and the other odd-run representative of value `c−t`, which exists and comes later. Again their ordered difference is t. Select all p−3 pairs.

**h odd; r,q even and r+q>0.** There are p−2 pairs. If t=0 take them all. If t!=0, reserve an additional c after ρ_v by breaking one pair in a nonempty c-segment, leaving p−3 pairs. If the nonempty segment is r, use that c BEFORE the other-run representative `c−t`; otherwise use `c+t` BEFORE the c from q. Their ordered difference is t.

**h odd; r=q=0.** There are p−2 pairs and a reserved c inside the h segment before ρ_v. If t=0 take all pairs. If t!=0 and `u+v!=0`, take that middle c together with the other-run representative `y=c−u−v`, and choose p−3 pairs. The ordered non-pair product is

`σ_c ρ_u σ_c σ_c ρ_v σ_y = ρ_(c−u−v−y) = 1`.

If t!=0 and `u+v=0`, instead take two other-run representatives with ordered difference t and p−3 pairs, whenever these exist. Section 2 identifies the exact remaining absent-difference constellation in §1; no omitted case is called solved.

Every displayed construction uses four distinguished occurrences plus `2p−4` more, hence exactly2p, and has identity product. Restoring original increasing word order cyclically rotates this identity product and preserves identity. QED.

## 4. Scope and distinction from earlier papers

The h=0 subcase contains the previously frozen arbitrary-u/v four-block candidate `frontier-20261028-olson-projection-fourblock-selector-v1.md`, SHA256 `eedd10defe0b7cc0d8a349fc4d8937c7ecc67b1c032c4eec4722a506143a4075`, but this proof independently accounts for all cut splits and does not require its review. More generally this candidate allows arbitrarily many same-reflection letters between the two selected rotations, subject to (1), and identifies an exact exceptional construction configuration.

The statement is a PROJECTION-only sufficient selector, not a repaired actual-block/run/floor theorem. It neither proves every lower-branch word meets (1) nor establishes complete OLD/SEL/IPGEN/GS/DS3 failures, REF failure, L_RES, an Olson counterexample, novelty, formal verification, or acceptance by any reviewer. In particular, the untouched exceptional constellation might still have an identity selector via another method.

## 5. Exact bounded actual-word checks

`frontier-20261028-olson-stretched-fourblock-experiment.py`, SHA256 `5619e2787d68bea854d9711f1e0d4e622b361dad306af395b9e698ed93b57932`, generated 1000 full original words and selectors at p=3,5,7,11,13. Saved data `frontier-20261028-olson-stretched-fourblock-results.json`, SHA256 `1914ad08678cef0a806bf3a43c96ff0ea6bd0ef5a8271ee7d277de857c5f6dd4`; the producer deliberately rejected seven exceptional draws rather than claiming them solved. These fixtures have no even projected runs; the written proof allows them.

Separately written `frontier-20261028-olson-stretched-fourblock-checker.py`, SHA256 `01d7f608dc74500e4d8a9bfc062f9dfeaa0c114072d8a974bdceacb710f58d2f`, imported no producer and returned `PASS_INDEPENDENT_STRETCHED_FOURBLOCK` in `frontier-20261028-olson-stretched-fourblock-check-results.json`, SHA256 `67e771dc95eb62072983719f5a99e86f6185c48b187411ad5013ca6ab2b4717a`. It reconstructed actual segment positions, cyclic projected-run splits, hypotheses and directly multiplied all 1000 original-index products. Recorded parity branches: h-even493, h-odd/no-outside217, h-odd/even-nonempty-outside181, h-odd/two-odd-outside109. Duplicate-index and altered-middle-length controls failed as intended. Finite checks are not a universal proof, a disjoint mathematical review, or a cross-family/formal certificate.

**END — stretched selector with its one exact construction exception.**
