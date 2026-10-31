# High-privacy value and universal product-Laplace law

**Disposition: ACCEPT as written mathematics at the candidate's exact class and limits.** Native clock observed before composing: **2026-10-28T20:10:39-0700 PDT**. Same-harness verification only; no human, independent-model-family, formal/kernel, novelty or finite-ε exact-optimizer certification.

## Adopted statement

For `b=e^(−ε)` and the original all-Borel, all-event, full closed ℓ1-unit-diamond private class on ℝ², every law satisfies

`J≥2b(1+b)/(1−b)²`, `L≥2b/(1−b)`,

while the product-Laplace density `(ε²/4)e^(−ε‖x‖₁)` is fully private with `J=4/ε²`, `L=2/ε`. Hence for every ε>0 and every κ≥0,

`e^(−ε)(4/ε²+2κ/ε)≤inf(J+κL)≤4/ε²+2κ/ε`,

so the relative error in `inf(J+κL)=[4/ε²+2κ/ε][1+O(ε)]` is at most `1−e^(−ε)≤ε`, uniformly over all nonnegative weights κ(ε). If a family satisfies `J+κL≤[4/ε²+2κ/ε][1+o(1)]` as ε→0, then `Law(εX)` converges to `Λ(dz)=(1/4)e^(−‖z‖₁)dz` in total variation and W₁; when `κε` stays bounded, also in W₂; when `κε→∞`, W₂ may diverge, as an explicit translated-mixture private family shows.

## Reconstructed argument

The finite bounds use only the four vertex shifts and half-line events: `P(|X_i|≥n)≥bⁿ`, then layer-cake sums `Σbⁿ` and `Σ(2n−1)bⁿ`. For scaled laws, full-diamond privacy iterated along fractional steps gives the measure order `μ_ε(A)≤e^(‖h‖₁+ε)μ_ε(A+h)` for every h; weak limits inherit `μ(A)≤e^(‖h‖₁)μ(A+h)`, have density at most e/2, and admit an everywhere-positive all-point representative with ℓ1-log-1-Lipschitz logarithm. Integration by parts with cutoffs yields `E|Z_i|≥1` and `E Z_i²≥2E|Z_i|`, with equality only for the product Laplace law. Near-optimality forces the moment bounds along bounded or divergent `κε` subsequences, so every weak limit is Λ; moment convergence upgrades to W₂ or W₁. The translation modulus `‖f_ε−f_ε(·−h)‖₁≤2tanh((‖h‖₁+ε)/2)` plus mollification upgrades weak convergence to total variation. The counterexample mixes Λ with its translate by `R=α^(1/2)` at weight `α^(−3/4)`, giving `E|Z|²=4+α^(1/4)` and objective excess `o(α)`.

## Evidence

- [Candidate, 108 LF](../../../../information-science/evidence/three-area-20261027-96h/parallel-18/privacy-diamond-mse/frontier-20261028-sharp-high-privacy-universal-limit-v1.md): `8615b71531aee0c55760796aad35dc6cb39002606b64b919017ed7a6e8b647d2`; parent read completely.
- [Frozen manifest](../review-waves/f121-privacy-high-privacy-universal-laplace/manifest-v1.json): `ce84a1d3eb9fc071cf31fa05a7263806cb0735a5b9fcf8c6c1a1ef4b7a16194f`.
- [Independent review, 120 LF](../review-waves/f121-privacy-high-privacy-universal-laplace/review-v1.md): `73165fe2e9900528aa3fca2f58cc96520a0744650f67adb6c8aca37b6e5be054`; 0 FATAL / 0 MAJOR / 3 MINOR, all repaired inside the review without new hypotheses: the translation modulus argument needs the two-sided set argument (sharp constant `2tanh`), the bounded-`κε` second-moment bound comes from the near-optimality hypothesis rather than from the lower bounds, and the product-form rigidity needs the Fubini-on-lines sentence. 22/22 controls passed including negative and mutation cases; a sharp staircase extremal was checked exactly.
- Parent independently verified the tail-series closed forms exactly, the ratios of the finite lower bounds to the Laplace moments at ε∈{1/2,1/10,1/100} (leading deviation ε/2), and the mixture arithmetic `tR²=α^(1/4)`.

## Boundaries

No finite-ε exact optimizer, sharpness beyond the bracket, forward Rényi/KL statements for α>1, or novelty follows. Later conditional candidates (quantitative rigidity, Rényi topology, exact 1D marginal optimizers, ε=ln2 certificates, budget W₂ thresholds) remain separate and unadopted; earlier adopted low-privacy results are unchanged.
