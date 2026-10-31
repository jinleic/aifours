# Werner d=4 original q3: product operators factor exactly, and no universal strict gap exists

**Disposition: same-harness written support at exact scope.** Let `q3` be the original unnormalized-partial-trace functional on operators of `(ℂ⁴)^{⊗3}` as stated in the pinned dossier definition. For every product `C=X₁⊗X₂⊗X₃` of arbitrary complex 4×4 matrices,

`q3(C)=∏_i g(X_i)`, `g(X)=‖X‖²_HS−|Tr X|²/2`.

For nonzero products of rank at most 2, `q3(C)≥0`; it is strictly positive when all three factors have rank 1, and it vanishes **iff** exactly one factor is a nonzero scalar multiple of a rank-two orthogonal projection while the other two have rank 1. Since such operators exist and `q3` is quadratically homogeneous, normalized equality operators exist in the original rank-≤2 domain: **no constant δ>0 satisfies `q3(C)≥δ‖C‖²` on that domain**, and even `q3(C)>0` for all nonzero rank-≤2 C is false. Nothing here asserts nonnegativity of `q3` on nonproduct operators, a global equality classification, an infimum value, priority or novelty; the dossier's own theorems are not adopted.

Native clock observed before composing: **2026-10-28T21:55:23-0700 PDT**, not an asserted file-creation time.

## Reconstruction

The unnormalized partial trace of a product multiplies out: `Tr_S(⊗X_i)=∏_{i∈S}Tr(X_i)·⊗_{i∉S}X_i`, and Hilbert–Schmidt norms multiply on tensor products. Substituting into the eight-term definition gives exactly the expansion of `∏(n_i−t_i/2)` with `n_i=‖X_i‖²`, `t_i=|Tr X_i|²`; no rank, Hermiticity or normality is used. A nonzero product of rank at most 2 has rank pattern (1,1,1) or one rank-2 factor with two rank-1 factors. For rank r, singular values give `|Tr X|≤‖X‖₁≤√r‖X‖_HS`, so `g≥(1−r/2)‖X‖²`. For rank 2, equality forces equal singular values, `|⟨v_j|u_j⟩|=1` for both pairs, and a common phase, i.e. `X=λP` with P an orthogonal rank-2 projection; the converse is a direct computation. Parent checked by hand `g(diag(1,1,0,0))=2−2=0`, `g(E₀₀)=1−1/2>0`, and `g(diag(1,1,1,0))=3−9/2<0`, which shows the rank hypothesis is load-bearing.

## Evidence and limits

Parent read the complete 42-LF [candidate](../../../../physics/evidence/three-area-20261027-96h/parallel-18/werner3-ququart/frontier-20261028-d4-original-q3-product-equality-v1.md), SHA-256 `b4d5f2673d9a2d605681f627e3ad2da943c68b010313c377d6d6fd4b6bd5fb1a`, and the complete 130-LF [f153 review](../review-waves/f153-werner-q3-product-equality-falsified-premise/review-v1.md), `e675b0b115d96ba6e05ae550980a953fbb311a449e800d0b6a663bde0e529811`. The review found no FATAL or MAJOR item and three MINOR notes (compressed equality-case exposition; an unverified out-of-scope attribution to a public source; the author's formal check covers only the eight-monomial expansion). It reconstructed every step from the dossier's §1 definition alone, and its exact Gaussian-rational control evaluated the definition literally on explicit 64×64 matrices for 11 operators plus formal and corrupted-evaluator controls, 18/18 PASS with every intended-reason negative detected.

The owner-elected quarantined auxiliary-family episode was not used, reconstructed or salvaged; this result rests on the q3 definition, tensor identities and the singular value decomposition only. It falsifies a universal strict-gap premise on the original domain; it does not decide the original rank-≤2 nonnegativity question. All evidence is same-harness, not human, independent-model-family, formal/kernel or novelty acceptance.
