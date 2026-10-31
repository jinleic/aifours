# Two occupied gaps in an EVEN projected run

Owner **MathOlson-2-2**; new WRITTEN selector candidate with bounded exact checks, not a reviewer verdict. Native `/bin/date` before this write: **Wed Oct 28 20:42:57 PDT 2026**. Read mandatory fatal record `frontier-20261028-olson-actual-block-fatal-correction-v1.json`, SHA256 `e11fd87345f8a54012f3a9245d87491c6ceb3a4a113558be07ca4ab62728f90e`, first. All run terms below are **reflection-only PROJECTION** terms. No old f111 finding, actual-block lift, or floor is imported.

## 1. Even-run selector

Let p be an odd prime. Let W have F=3p−2 reflections and exactly p odd projected runs, whose exponents are pairwise distinct; any number of even projected runs is allowed. Suppose W contains the actual consecutive segment

`σ_c ρ_u σ_c (σ_c)^h ρ_v`, h>=0,  (1)

whose displayed c-reflections belong to one EVEN projected run. Then W has an original-order identity selector of exactly2p occurrences. No assumption on u,v is needed.

## 2. Proof

Cut immediately before (1). Let h be the middle length in (1); let r and q be the numbers of remaining c-reflections in that same projected run after and before (1), respectively. After ρ_v, r c-reflections appear first, all other projected runs follow, and q c-reflections appear last. Since the original c-run is even, `h+r+q` is even. Removing the two distinguished σ_c reduces total projected equal-pair capacity from `p−1` to `p−2`. Splitting the remaining c-run into the h,r,q cut-order pieces loses either zero pairs (all three even) or one pair (exactly two odd). Thus there are either p−2 or p−3 actual, disjoint equal pairs, each lying wholly in one of those pieces or another projected run. Pairs in h precede ρ_v; all other selected pairs follow it and each still multiplies to 1. Every one of the p original odd projected runs is uncut and has one spare reflection AFTER ρ_v; their distinct exponents are all of F_p.

Write `t=u−v`. As in the elementary directed-cycle argument, for each nonzero t an arbitrary linear ordering of all F_p has two entries in order whose first-minus-second difference is t: otherwise each `x−t` is earlier than x, giving a strict cycle. If t!=0, select those two odd-run spares and p−3 of the available pairs. If t=0 and p−2 pairs are available, select all of them and no spares. If t=0 and only p−3 pairs are available, exactly two of h,r,q are odd; since at least one of r,q is odd, there is a spare σ_c AFTER ρ_v. Select it and the spare σ_c from the odd projected run labelled c, plus all p−3 pairs. These two same-valued spares multiply to 1 even if identity pairs occur between them.

In every case there are `2p−4` additional selected reflections besides the four distinguished occurrences, and the selected product after deleting identity pairs is `ρ_(v−u)ρ_t=1`. The cyclic cut may be restored to the original word order because a cyclic rotation of an identity product is identity. QED.

## 3. Joint reduction for all projected runs

If two of the p odd projected-run exponents coincide, their spares plus all p−1 equal pairs already give 2p reflections multiplying to 1, independent of any rotation. Otherwise the p odd labels are distinct. For an actual consecutive segment (1) in an ODD projected run, use the separate joint candidate `frontier-20261028-olson-stretched-fourblock-exception-resolution-v1.md`, SHA256 `4c13a273997c6a02c97ab9b4b45bd36a80c5ebe0751c59450770ba33b76a58ac`, and then FULL `frontier-20261028-olson-stretched-fourblock-selector-v1.md`, SHA256 `ef44c034b01a924d0930f26e6c95b70972af31f9666340a06457ff40bc261e7f`. These are named unreviewed inputs, not an adoption; this §1 proves the EVEN case independently.

Hence, conditional on those named odd-run proofs, any word with o_π=p and a stretched segment (1) in **any** projected run has a selector. In particular, if every cyclic reflection gap has at most one rotation, ANY projected run assigned two occupied gaps provides such a segment by taking its first two gaps. For R=p+1 the remaining no-selector projection possibilities are therefore `o_π>=p+2`, or `o_π=p` with `e_π>=1` and at most ONE occupied gap assigned to each projected run; the latter has at least one occupied gap assigned to an even run. The elementary `o_π<=p−2` case has at least p equal pairs and is reflection-only covered. These are exact PROJECTION statements, not historical actual `o_F/e_F` deductions, and they do not settle OLD/IPGEN/GS/DS3 failure or full L_RES.

## 4. Exact bounded checks

`frontier-20261028-olson-evenrun-stretched-experiment.py`, SHA256 `7cb36773f747149477d8ac29b7a55ad7ccc7c2deca48add1f3dd490276320612`, generated 1000 actual words at p=3,5,7,11,13 with the segment in an EVEN projected run; input `frontier-20261028-olson-evenrun-stretched-results.json` SHA256 `1f12bf1c68e707aa3d31e83b9e39ac7f5d40fe52e184ead0209e05c470d3da57`. Separately written `frontier-20261028-olson-evenrun-stretched-checker.py`, SHA256 `3d9c54645296d116c5259ab67df2b361548c740659aaf4ef713e2ca460d08a22`, imported no producer. Its `frontier-20261028-olson-evenrun-stretched-check-results.json`, SHA256 `801583cb1adce34f8f51ad15a07860961f3365458805b638d9b8ce293d5223c8`, records PASS for all 1000 actual original-index products; 104/72 target-zero cases had respectively zero/two odd split pieces, and 449/375 nonzero-target cases had zero/two odd split pieces. Duplicate-index and altered-middle-length controls failed as intended. Fixtures have one even projected run; the proof allows more. Same-model finite checks are not independent mathematical, external-family or formal review.

**END — even-run selector and explicitly conditional any-run reduction.**
