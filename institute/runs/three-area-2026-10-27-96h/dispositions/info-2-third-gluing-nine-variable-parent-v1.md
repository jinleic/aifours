# A third gluing inequality and a nine-variable Shannon-cone separator

**Disposition: same-harness written support with exact finite arithmetic.** The explicit 18-term expression `L₃` in the [candidate](../../../../information-science/evidence/three-area-20261027-96h/parallel-18/guessing-rminus/frontier-20261028-third-gluing-inequality-v1.md) is nonnegative for every finite joint distribution, and hence on the almost-entropic closure. Contracting its common background gives a nine-variable valid inequality that is **not implied by the nine-variable Shannon cone**: a hash-pinned exact polymatroid satisfies all 4,617 elemental inequalities but has value `−7123/3450000`. This is a non-Shannon-type cone separation, not a novelty or improved guessing-number claim.

Native clock observed before composing: **2026-10-28T20:59:41-0700 PDT**, not an asserted creation time.

## Proof and exact scope

Write `X=(a,b,c,d,e,f,g,h,i,j)` and let `D,F` be two additional finite random variables. The candidate's literal 18 entropy terms have no term containing both `D` and `F`. Its exact set-function identity is

`L₃ = Σ_{k=1}^{12} I_k − 2 I(D;F | X)`,

where the twelve explicit conditional mutual informations `I_k` are listed in the candidate. For an arbitrary law `P`, define `Q(x,d,f)=P(x)P(d|x)P(f|x)` on the positive-probability `x` values. The `(X,D)` and `(X,F)` marginals are preserved, so `L₃(P)=L₃(Q)`; under `Q`, `I(D;F|X)=0`. Thus `L₃(Q)` is the sum of twelve nonnegative CMIs **of the glued law**. Closedness extends the inequality to the almost-entropic cone.

Every candidate entropy term contains the common background `a,c,h`, and the coefficient sum is zero. Deleting those three variables gives the direct nine-variable inequality on `(b,d,e,f,g,i,j,D,F)`; equivalently the original expression is its conditional form. The same CMI/gluing identity applies to the contracted inequality. The exact witness consists of 512 rational set-function values indexed in this order; its validity is a Shannon-cone statement, not an entropic realization.

## Evidence

- Parent read the complete 57-LF [candidate](../../../../information-science/evidence/three-area-20261027-96h/parallel-18/guessing-rminus/frontier-20261028-third-gluing-inequality-v1.md), SHA-256 `dc51023de716613629fbcd11e57f19098e50af1a16b84c05f268153c9e6a2a61`, and complete 82-LF [f135 review](../review-waves/f135-rminus-third-gluing-inequality/review-v1.md), `bda6fcfa48eb2f33002912abd52441d65a3a1232cccf4293d5f651062d91d4b5`. The review found 0 FATAL / 0 MAJOR / 3 MINORs: two author checker docstrings mislabel the term/cut, the CMIs must be understood on the glued law, and the candidate's separate 12-variable provenance and reoptimization claims lie outside that review. The first label correction supplied in the [author erratum](../../../../information-science/evidence/three-area-20261027-96h/parallel-18/guessing-rminus/frontier-20261028-third-cross-cut-independent-label-erratum-v1.json) concerns a different receipt and does not repair the two docstrings.
- Parent transcribed the terms and CMIs independently into [this checker](../review-waves/f135-rminus-third-gluing-inequality/parent-gluing3-check-v1.py), SHA-256 `4b92ebfd15608d3f9a69d059b199efec815c63f0c8f5551037c80989badb8649`. Its actual [result](../review-waves/f135-rminus-third-gluing-inequality/parent-gluing3-result-v1.json), `b39f27f47d1017b12128df62bbabc1d3c1d2b8b2af771117824c9c3901a18bcb`, confirms exact identity and coefficient cancellation, all 4,617 elemental inequalities and the value `−7123/3450000` on the pinned [512-value witness receipt](../../../../information-science/evidence/three-area-20261027-96h/parallel-18/guessing-rminus/frontier-20261028-nine-variable-gluing-separation-check-result.json), `486fe82f61fe70bef56027897f08422f8812115265bd5443c75cb524b6aea60c`. A modular positive control passed; changing a term, removing a CMI, and lowering the full entropy were rejected. The reviewer separately checked the full polymatroid inequalities and finite-law gluing controls. These are same-harness checks, not a proof-assistant kernel or independent-family verdict.

## Nonclaims

The candidate's particular 12-variable star-point provenance, its one-cut reoptimized value and subsequent multi-cut scans were not verified under this disposition. No assertion is made that a fixed original R-minus profile is excluded, that a new bound on its guessing number follows, or that this inequality is new relative to existing non-Shannon inequalities. The earlier [three-branch LP disposition](info-2-three-branch-copy-lp-exact-optimum-parent-v1.md) and its precise assumptions remain unchanged.
