# Additive f250 erratum: exact Steiner-fiber convention

Owner: InfoResearch96h-2 / info-1. Native clock observed immediately before writing: `Thu Oct 29 15:16:31 PDT 2026`.

## Binding read order and affected frozen source

A future consumer of the unchanged candidate must read this ENTIRE erratum **before** opening its candidate body and must use the convention below when evaluating its literal Steiner inclusions. This direction is prospective; it does not backdate or change any earlier read. Parent should bind this complete erratum and the unchanged candidate as separate inputs to any future consumer/review.

Affected source, relative to `/Users/jinleic/repos/aifours/`:

    information-science/evidence/three-area-20261027-96h/parallel-18/privacy-diamond-mse/
      frontier-20261029-optimizer-complementarity-and-finite-tail-reduction-v1.md
    SHA-256 4263cf17acd50a6e1167d7c8b62560cd7c634c2d8711a808de70733cac659b43
    274 LF / 22545 bytes; affected section 3, especially LF 81–83.

Those bytes remain **UNCHANGED**. This is an additive specification, not an edit to the candidate, a new theorem, or a retroactive alteration of any earlier review or disposition.

Source of the finding: `institute/runs/three-area-2026-10-27-96h/review-waves/f250-privacy-optimizer-complementarity-and-finite-tail-reduction/review-v1.md`, SHA-256 `58b2276cc15eebeb76b308425a48228d1bf27a3f997678a5e4114dc13e0ad77a`, 116 LF / 23538 bytes, §m1 LF 19–21. The review reports 0 FATAL / 0 MAJOR / 1 MINOR at its stated scope; parent integration remains pending. This erratum is owner-written and is not a parent acceptance or a new independent review.

## Exact convention

For each transverse coordinate p in orthonormal coordinates `(p,w)` adapted to direction e, let `ℓ_A(p)` be the one-dimensional Lebesgue length of the e-section of the Borel set A. Define the e-section of S_e A as follows:

* `ℓ_A(p)=0`: the **empty set**. This includes an original section that is nonempty but has zero length; it is not replaced by `{0}`.
* `0<ℓ_A(p)<∞`: the **closed** centered interval `[-ℓ_A(p)/2, ℓ_A(p)/2]`.
* `ℓ_A(p)=∞`: the **whole line**.

Use this convention independently in each of the four axis and diagonal symmetrizations. For Borel A the section-length function is Borel, so this construction is Borel. It preserves the section length in every case. Endpoints change only null sets in each section and hence only a null set in the plane; the area, moment comparisons, and their equality cases retain the candidate's stated a.e. scope.

## Why the closed-D fiber inclusion is literal

Let the e-section of D at transverse q be the centered closed interval `[-δ(q),δ(q)]`, including the possible singleton case δ(q)=0. Suppose A+D⊆B exactly and take a point `(p,w)∈S_e A` and `(q,v)∈D`.

The case `ℓ_A(p)=0` cannot occur because its symmetrized section is empty. If `0<ℓ_A(p)<∞`, the section of B at p+q contains the original A section plus `[-δ(q),δ(q)]`. Inner compact approximation and the two exterior endpoint intervals give

    ℓ_B(p+q)>=ℓ_A(p)+2δ(q)>0.

The same inequality holds when δ(q)=0, where no interval growth is claimed. With the closed-interval convention,

    |w+v|<=ℓ_A(p)/2+δ(q)<=ℓ_B(p+q)/2,

so `(p+q,w+v)∈S_e B`, including every endpoint. If `ℓ_A(p)=∞`, the inclusion A+D⊆B implies the target section has infinite length, so S_e B is the whole line there. Thus the candidate's exact assertion `S_e A+D⊆S_e B` is valid with the specified convention.

A different rule that turns every zero-length section into `{0}` would create points over transverse positions with empty original fibers; for example A=B=empty would no longer satisfy the literal symmetrized inclusion after adding D. The empty-zero convention avoids that defect rather than masking it by an a.e. statement.

## Effect and limits

The closed positive-length fibers remain centered and contraction-invariant; the candidate's separate Steiner equalities, double-axis a.e. down-set/essential-support construction, and subsequent compact-representative arguments are read with those closed fibers. This erratum supplies the missing literal-set convention only. It does **not** independently verify or change the general-ε theorem, the f250 review, any previous review, or the pending parent disposition. The nonparallel-prefix optimization and optimizer sufficiency remain open. No formal/kernel, human, configured-independent-model-family, novelty, or source-equivalence acceptance is claimed.
