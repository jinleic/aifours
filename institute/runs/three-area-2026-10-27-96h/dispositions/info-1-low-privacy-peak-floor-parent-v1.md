# All-law low-privacy asymptotics from the peak-floor bound

**Disposition: same-harness written support at fixed finite λ ≥ 0.** For the full closed-diamond additive privacy class, the minimum mixed cost has the leading low-privacy asymptotic and universal near-optimal scaled limit stated below. This result does not assume a known optimizer, a radial law, or the earlier LAW642, MDA, v241 or PMLR results. Standard measure-theoretic and geometric facts remain imports. No independent-model-family, human, formal/kernel, publication or novelty acceptance is claimed.

Native clock observed before writing: **2026-10-28T19:21:21-0700 PDT**; this is a prewrite observation, not an exact creation timestamp. Historical held outputs are not premises.

## Exact claim

For finite ε>0 put `b=e^(−ε)` and `D={h∈R²: ||h||₁≤1}`. Let `F_ε` contain every Borel probability law satisfying `μ(A)≤b⁻¹μ(A+h)` for every Borel A and every h in the **closed** D. For a fixed finite `λ≥0`, write

`c_λ(x)=||x||₂²+λ||x||₁²`, `H_λ(b)=inf_{μ∈F_ε} E_μ c_λ(X)`,

`A_λ=area{c_λ≤1}`, `C_D=∫_D c_λ(x) dx=2/3+λ`, and `C_λ=√(2C_D/A_λ)`. At λ=0, `A₀=π` and `C₀=2/√(3π)`.

1. **All-law lower bound.** For every `0<b<1` and every μ in `F_ε`,

   `E_μ c_λ ≥ √(2b C_D/A_λ + 4b²/A_λ²) − 2b/A_λ`.

2. **Leading value.** As `b→0`, `H_λ(b)=C_λ√b+O_λ(b^(3/4))`. The upper bound is supplied by an actual full-D-private shell law, not by a restriction of the infimum.
3. **All-near-optimal limit.** For every sequence of feasible laws with `E c_λ≤C_λ√b+o(√b)`, the laws of `b^(−1/4)X` converge in total variation to the uniform law on `{z:c_λ(z)≤C_λ}`. The rescaled c_λ expectation tends to `C_λ`, whereas the uniform limit has expectation `C_λ/2`; consequently this convergence is **not W₂ convergence**. The cost carried by the vanishing tail is not inferred from total variation alone.

These are fixed-λ statements. They do not by themselves prove a λ-uniform error bound or any finite-ε optimal law.

## Source and peer review

Main read the complete [author proof](../../../../information-science/evidence/three-area-20261027-96h/parallel-18/privacy-diamond-mse/frontier-20261028-peak-floor-low-privacy-universal-v1.md) (171 LF; SHA-256 `d44029e458b8af871d2d849e2a5159e1885e99402d615a88eabe39d89ab4ad43`) and the complete [f94 review](../review-waves/f94-privacy-peak-floor-universal-chain/review-v1.md) (133 LF; `ec506df5635511a7476dc00082a502f1a5fc254c3c5b32ea97c79ab7b1db1d46`). The reviewer reports **0 FATAL / 0 MAJOR / 0 MINOR** for this proof, with independently written exact Fraction checks. Its separate first-norm successor has a shell-normalization MINOR, and a different overlap successor has an undefined-measure MINOR; neither successor is adopted here or silently substituted for this proof.

## Parent reconstruction

Integrating the privacy inequality over D gives `μ(A)≤|A|/(2b)`, hence an essentially bounded density. Shrinking-ball limsups give a representative bounded by its essential supremum `M` and satisfying the pointwise shift inequality without taking an uncountable union of null sets. A point within factor `1−η` of `M` forces density at least `ℓ=b(1−η)M` on a translate of D. Its translated cost integral is at least `C_D`, and in fact at least `C_D+2||x₀||₂²`.

After removing that floor, the remaining density g has mass `h=1−2ℓ` and cap M. Since the area and cost integral of `{c_λ≤t}` are `A_λ t` and `A_λ t²/2`, the exact bathtub inequality gives `∫c_λg≥h²/(2A_λM)`. Letting η tend to zero and writing `x=bM` gives

`E c_λ ≥ (C_D+2b/A_λ)x + b/(2A_λx) − 2b/A_λ`,

whose AM–GM minimum is the displayed lower bound. The matching cost-body shell's layer index changes by at most one under every D shift, so its density is actually private. Layer integrals yield the leading `C_λ√b` term and stated error.

For a near-optimal sequence, the nonnegative floor and bathtub deficits force the scaled density cap and peak location to their unique limits and the bathtub deficit to zero. Comparing the remaining density with the capped uniform sublevel density away from a thin threshold band, then letting the band shrink, gives L¹ and hence total-variation convergence. The scaled floor has vanishing mass but carries a nonvanishing cost contribution, accounting for the W₂ distinction.

## Independently exercised parent controls

The parent wrote and ran [an exact shell-control script](../review-waves/f94-privacy-peak-floor-universal-chain/parent-shell-control-v1.py), SHA-256 `76218385d6e1366681960089dbdbe9677e76cab6ce1cef19d080aaead0e5398e`; its [receipt](../review-waves/f94-privacy-peak-floor-universal-chain/parent-shell-control-result-v1.json), `d818cb427fff5cb8b4b5d413e5b44eb93047fc6d294c8714e693a6399b008974`, binds the candidate hash. It independently integrated the diamond moments `area=2`, `∫||x||₂²=2/3`, `∫||x||₁²=1`, and `∫||x||₁=4/3` using rational simplex integrals. For three rational b/core-radius pairs it computed the exact normalization and squared cost of a **diamond-core** shell and checked them against the sampled peak-floor expression. It checked 2,106 rational point/shift pairs; a doubled-layer-exponent mutation was rejected at a unit shift.

Those finite point checks are diagnostics, not proof of all-event privacy. The diamond-core shells are feasible examples, not the claimed optimal cost-body shells. The universal result rests on the written proof and its review, not on interpolation from these examples.

## Remaining boundaries

No worldwide priority search, source-equivalence audit, numerical optimizer, human review, external-family review, or proof-assistant certification was performed. This does not determine the full finite-ε mixed-loss optimum, optimizer uniqueness, a λ-uniform rate, or any of the unreviewed further moment-region candidates.
