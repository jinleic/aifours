# Uniform low-privacy joint-budget inversion

**Disposition: ACCEPT as written mathematics with explicit constants supplied by the review.** Native clock observed before composing: **2026-10-28T20:07:55-0700 PDT**. Same-harness verification only; not a human, independent-model-family, formal/kernel, novelty or exact finite-b optimizer certification.

## Adopted statement

For the full closed ℓ1-unit-diamond private class on ℝ², let `b_max(j,ℓ)` be the largest `b=e^(−ε)` admitting a law with `J≤j` and `L≤ℓ`. Put `r=j/ℓ`, `F(r)=27r(1−2r)²/4` for `r<1/6` and `F(r)=1/2` for `r≥1/6`, and `η=ℓ+ℓ²/j`. The finite necessary conditions

`b≤ℓ³F(r)/(1−9j)` for `r<1/6, j<1/9`, and `b≤ℓ³/(2−3ℓ)` for `ℓ<2/3` and every r,

hold for every feasible pair. For every `(j,ℓ)` with `ℓ≤1/150` and `η≤1/8`, and every `r>0`,

`(1−7η)³ℓ³F(r)≤b_max(j,ℓ)≤ℓ³F(r)/(1−1.5ℓ)≤ℓ³F(r)(1+2ℓ)`,

hence `|b_max/(ℓ³F(r))−1|≤21η` and `ε_min=3log(1/ℓ)−log F(r)+O(η)`. The estimate is pointwise, so arbitrary oscillating, vanishing or diverging ratios r, including crossing or equality at r=1/6, are covered without any order-of-limits argument. Equivalently the candidate's `b_max=ℓ³F(r)[1+O(ℓ+ℓ²/j)]` holds uniformly in r on that regime.

## Reconstructed argument

Upper bounds come from the floor/capped bathtub dual of the finite-privacy disposition and the containment `G(H)≤2H³/(3κ²)`, with the exact substitution `κ=2r/(1−6r)` for `r<1/6`; the L-only bound never uses J. Lower bounds come from explicit private diamond-shell laws with density proportional to `b^k` on successive ℓ1 shells around `aD`; shifts by D change the shell index by at most one, so the law is fully private. Abel-summed geometric moment sums give exact normalizer and cost series; for `a≤1/100` and `b≤a³/2` the review's Lemma E brackets L and J with explicit constants uniformly in `b/a³`, including the genuine `a⁴/b` inner-diamond term. Choosing `a=γ(3/2)(1−2r)ℓ, b=γ³ℓ³F(r)` for `r<1/6` and `a=γℓ, b=a³/2` for `r≥1/6`, with `γ=1−7η`, makes both budgets hold.

## Evidence

- [Candidate, 82 LF](../../../../information-science/evidence/three-area-20261027-96h/parallel-18/privacy-diamond-mse/frontier-20261028-explicit-uniform-budget-theorem-v1.md): `f020dab0002911f8222182725ba123da2b25f4b62102bd84ac0282f4496e75cc`; parent read completely.
- [Frozen manifest](../review-waves/f119-privacy-uniform-joint-budget/manifest-v1.json): `d99311e516485267b0f36ba0c12a919f97cfc0e013c51f7f40f46a4c64cd8583`.
- [Independent review, 135 LF](../review-waves/f119-privacy-uniform-joint-budget/review-v1.md): `08c240822a773d619fc30cca08f2e2cf07b4586a38d275d86a363b11afc40e55`; 0 FATAL / 0 MAJOR / 6 MINOR, with a full reconstruction replacing every unquantified constant, exact Eulerian-polynomial moment sums, 80 shell laws and 385 mixtures checked at their own exact moments, 34 adversarial rational sequences, scope-boundary and three negative controls, one observed run with receipt.
- Parent verified the exact rational κ-substitution identities and sample F values independently.

## Boundaries

The six MINORs are adopted as qualifications: dimension ℝ² is implicit; the all-point representative's regularity is proved in the review, not the candidate; the universal constants are those of the review's explicit regime; the L-only bound holds for all r; `κ=2r/(1−6r)` optimizes only the leading-order bound; the error is asymmetric and sharpness of the `ℓ²/j` term is not established. No exact finite-b optimizer, novelty, high-privacy or product-Laplace claim follows; those later candidates remain under separate review.
