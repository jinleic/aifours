# Paying part of the AP-aligned stretched-block exception

Owner **MathOlson-2-2**, WRITTEN sufficient-condition candidate. Native `/bin/date` before this write: **Wed Oct 28 20:36:08 PDT 2026**. Mandatory before-source: `frontier-20261028-olson-actual-block-fatal-correction-v1.json`, SHA256 `e11fd87345f8a54012f3a9245d87491c6ceb3a4a113558be07ca4ab62728f90e`. No old f111 verdict or actual-block/floor application is carried across.

## 1. Precisely stated conditional candidate

Let p be an odd prime and W a dihedral word with F=3p−2 actual reflection occurrences. Its cyclic reflection-only projection has exactly p odd maximal constant runs. Suppose one of these is the projection of the ACTUAL consecutive segment

`σ_c ρ_u σ_c (σ_c)^h ρ_(−u)`, where u!=0 and h is odd,  (1)

and it contains NO other c-reflection outside (1). In cyclic order after this c-run, suppose the remaining p−1 odd-run values are exactly

`c+t,c+2t,...,c+(p−1)t`, where `t=2u`.  (2)

There may be additional EVEN projected runs with arbitrary exponents. Suppose W contains a THIRD actual rotation ρ_w, whose gap lies BETWEEN two different projected constant runs, after exactly k of the odd runs in (2), where `1<=k<=p−2`, and `w!=−u`. Then W has an original-order identity subsequence of exactly2p actual occurrences.

This is a conditional selector for part of the explicit exceptional configuration of `frontier-20261028-olson-stretched-fourblock-selector-v1.md`, SHA256 `ef44c034b01a924d0930f26e6c95b70972af31f9666340a06457ff40bc261e7f`. It is independently proved here and does not import that candidate's validity. It does not prove such a third rotation exists, nor handle all w=−u or within-run rotation placements.

## 2. Pair capacity and a cross-cut difference

Cut immediately before (1). Select its first `σ_c ρ_u σ_c` and skip its ρ_(−u). Removing the two selected c-reflections leaves `(3p−4−p)/2=p−2` disjoint equal-reflection pairs: the h remaining c-reflections yield `(h−1)/2` pairs, and each other projected run supplies its own floor-half pairs. Those pairs can be selected without crossing ρ_w because ρ_w lies at a PROJECTED run boundary. The p−1 odd runs in (2) each provide one additional reserved representative.

If w=u, choose all p−2 pairs. The only non-pair product is `σ_cρ_uσ_cρ_u=1`, and the number selected is `4+2(p−2)=2p`.

Now assume w differs from both −u and u. Define `d=−(u+w)/t` in F_p. Then d is neither 0 nor −1, hence has integer representative `1<=d<=p−2`. For every k in `1,...,p−2` there exist `1<=i<=k<j<=p−1` with `j−i=d`: take `i=max(1,k+1−d)` and `j=i+d`. Thus the representatives `y_i=c+i t` before ρ_w and `y_j=c+j t` after ρ_w have difference `y_i−y_j=−d t=u+w`.

Select these two representatives and p−3 of the p−2 equal pairs, in addition to the two c-reflections and rotations ρ_u,ρ_w. Identity pairs may occur on either side of ρ_w. The remaining ordered product is

`σ_c ρ_u σ_c σ_(y_i) ρ_w σ_(y_j) = ρ_(−u+y_i−w−y_j) = 1`.

The selected count is `4+2+2(p−3)=2p`. A cyclic reordering back to increasing original word order preserves identity. QED.

## 3. Exact residual and checks

This pays the AP-aligned exception only when an interior odd-run boundary has an actual rotation with exponent other than −u. If every such rotation has exponent −u, or rotations occur only within projected runs or outside the specified interior, this paper makes no selector or impossibility claim. It neither proves complete OLD/SEL/IPGEN/GS/DS3 failure nor resolves L_RES, and it uses no historical `o_F/e_F` mapping.

`frontier-20261028-olson-exception-third-rotation-experiment.py`, SHA256 `86ba9fa31d5d5258a430212be423a52b5789a603e86593cf5690cb2aa6577330`, generated 500 ACTUAL zero-free singleton-gap words and original-index selectors at p=3,5,7,11,13. Data `frontier-20261028-olson-exception-third-rotation-results.json` SHA256 `042ae4062899abe97753e4fbca559fc6b9449b70f0492f3d0e4b896d3718f492`.

Separately written `frontier-20261028-olson-exception-third-rotation-checker.py`, SHA256 `5015de923ecebba06d7c40301308901bf766e3ccc1449687a0f2ec2b57d9a33e`, imported no producer and returned `PASS_INDEPENDENT_EXCEPTION_THIRD_ROTATION` in `frontier-20261028-olson-exception-third-rotation-check-results.json`, SHA256 `00be9f2374995acc7409bb67c4e9f0928c4b10fb0464ac360ae013d9bf03147a`. It independently checked the actual distinguished run, odd-AP order, third rotation at an interior projected boundary and original selector products: 174 words had w=u and 326 had w different from both ±u. Duplicate-selection and altered-third-rotation controls failed as intended. These fixtures contain no even projected runs; the proof allows them. This is bounded same-model verification, not a disjoint reviewer, formal proof, novelty check, or review/adoption of any older source.

**END — conditional third-rotation selector for the AP-aligned exception.**
