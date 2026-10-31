# Revealed delayed martingale: exact literal gain and strict endpoint

**Disposition: same-harness written support at the exact scalar-law scope.** Let `T>h≥S:=T−h>0`, with canonical Brownian filtration, zero initial state, progressively measurable input supported on `[0,S]`, and

`dx_t = w_(t−h) dW_t`, `z_t=x_t`.

For admissible nonzero E1 and E2 inputs, the literal gain uses `E‖z‖/E‖w‖`, with `‖w‖²=∫₀^S |w_s|²ds`. Define, for probabilities `ν` on `[0,1]`,

`F(ν)=E sqrt(∫₀¹ B_s² ν(ds))`, `κ=max_{ν∈P[0,1]} F(ν)`.

Then both literal gains are exactly `√S κ`; the relaxed maximizer `ν*` is unique, has support contained in `[a,1]` for some `a>0`, and has `sup supp ν*=1`. No nonzero physical E1 or E2 input attains the gain. Consequently the original **pointwise** strict inequality holds at `γ=√S κ`, despite the absence of a uniform positive margin. The bounds `√(2/π)<κ≤[√(2/π)+√(2−2/π)]/2<1` hold. The separate E2 RMS gain is `√S`, strictly larger than the literal gain.

This is one output-visible pure-delayed scalar law, not a general endpoint, arbitrary-matrix, feedback-synthesis or book-equivalence theorem. The variational optimizer and a closed or numerical value of κ remain unknown; the conclusion does not assert an atom at 1. No novelty, priority, formal/kernel, human or independent-model-family acceptance is claimed.

Native clock observed before composing: **2026-10-29T07:08:11-0700 PDT**; not a file-creation time.

## Parent reconstruction

Since `S≤h`, the entire progressively measurable input path, as an `L²[0,S]`-valued random variable, is `F_h`-measurable. Brownian increments after h are independent of it. Conditional freezing and localization therefore reduce the E1 literal ratio to a `‖w‖`-weighted average of deterministic-path ratios without assuming an E2 moment; deterministic inputs also show equality of the E1/E2 suprema. A strictly positive deterministic deficit at the supremum remains strictly positive after expectation on the nonzero-input event, but it need not be uniformly bounded away from zero.

For a unit deterministic input, its continuous nondecreasing energy clock `A(u)=∫₀^{Su}|v_t|²dt` is absolutely continuous with `A(0)=0`, `A(1)=1`; deterministic Gaussian time change gives the ratio `√S F(A_#Leb)`. Monotone piecewise-linear quantile approximations with fixed endpoints yield weak density of these physical clock laws in `P[0,1]`. Brownian continuity and domination by the integrable Brownian maximum give weak continuity of F, so compactness yields a relaxed maximizer and the exact supremum formula.

For distinct probability measures put `η=ν₁−ν₂`. Gaussian fourth moments give

`Var(∫ B_s² η(ds)) = 4∫₀¹ r η([r,1])²dr`.

Zero variance forces the signed tail to vanish away from zero; total mass zero then forces `η=0`. Thus distinct pathwise integrals differ with positive probability, strict concavity of the square root gives strict concavity of F, and the relaxed maximizer is unique. The source's two-time perturbation of `δ₁` gives a positive `ε log(1/ε)` term dominating its `O(ε)` loss, so `κ>√(2/π)`; this excludes a one-point positive-time optimizer. Moving any atom at zero to 1 strictly increases F. Two separated positive-mass intervals then supply two nondegenerate Gaussian averages; Jensen gives a rank-two lower bound on `Y*=∫ B_s²ν*(ds)` and the two-dimensional radial integral gives `E(Y*)^(−3/4)<∞`.

With `f(t)=E[B_t²/√Y*]`, that inverse moment justifies the directional derivative by domination and gives continuity by Hölder. Maximality gives `f≤κ` everywhere; integrating against `ν*` and using continuity gives `f=κ` throughout its support. Since `f(0)=0<κ`, the support has a positive gap above zero. Brownian scaling sends any positive-value law supported in `[0,b]`, `b<1`, to a law with value multiplied by `b^(−1/2)>1`; hence the support reaches 1. Every physical energy clock is continuous at zero and spends positive physical time in `[0,a)`, so its pushforward cannot equal `ν*`. Uniqueness and input revelation imply nonattainment and the pointwise strict endpoint for every nonzero admissible E1/E2 input.

## Evidence and boundaries

Parent read all five original candidate inputs, in the review's declared order: [input revelation](../../../../information-science/evidence/three-area-20261027-96h/parallel-18/stochastic-hinf-preview/frontier-20261028-full-input-revelation-strict-endpoint.txt) (`592d9a37…94b3abc`, 46 LF), [literal/RMS bracket](../../../../information-science/evidence/three-area-20261027-96h/parallel-18/stochastic-hinf-preview/frontier-20261028-revealed-martingale-strict-literal-rms-gap.txt) (`f5196dbc…f7e8b60c3`, 67 LF), [variational candidate](../../../../information-science/evidence/three-area-20261027-96h/parallel-18/stochastic-hinf-preview/frontier-20261028-revealed-martingale-exact-unique-variational-gain.txt) (`018f2343…59380cb1`, 89 LF), [KKT detail](../../../../information-science/evidence/three-area-20261027-96h/parallel-18/stochastic-hinf-preview/frontier-20261028-revealed-martingale-endpoint-kkt-proof-detail.txt) (`4e00f3ee…8eeea9671`, 67 LF) and [support endpoint](../../../../information-science/evidence/three-area-20261027-96h/parallel-18/stochastic-hinf-preview/frontier-20261028-revealed-martingale-optimizer-support-endpoints.txt) (`4a2355d2…6c184bb8c`, 25 LF). Parent read the complete 336-LF [f150 review](../review-waves/f150-hinf-revealed-martingale-unique-variational-gain/review-v1.md), SHA-256 `0caa3eacbdee9a902ed758788fbe1e1ca63c779de3dec179bb4d72fa06d862a6`, and [manifest-v2](../review-waves/f150-hinf-revealed-martingale-unique-variational-gain/manifest-v2.json), SHA-256 `04b3e2fd0f81456070c150e5ca358c126bc9b758bf267cb2901bd7d8bed9730c`.

The review reconstructed the original epsilon-log argument on its own merits and found 0 FATAL / 0 MAJOR / 0 MINOR mathematical findings. Its independently written final controls report 40 PASS / 0 FAIL in the [v2 receipt](../review-waves/f150-hinf-revealed-martingale-unique-variational-gain/reviewer-f150-run-receipt-v2.json), SHA-256 `5b7a5820e5f31d5f14cdbb61e9ec9f002945fcdb78d47aba5f15f8c7fb14d19e`. The review's earlier v1 diagnostic failed because it incorrectly demanded the sufficiently-small-ε conclusion at ε=0.1; that failure and its additive correction are preserved and are not described as a source failure. The reviewer separately checked optional two-pulse inputs; this disposition does **not** adopt their quantitative finite-pulse claim because parent did not read those optional sources. The reviewer disclosed an unrelated f138 sample display and out-of-directory non-scientific copy files; neither is used as evidence, and no deletion is claimed.

Standard Brownian independent increments/scaling, deterministic Wiener-integral time change, Gaussian covariance, weak compactness, quantile approximation, Itô isometry, Hölder, Tonelli and dominated convergence are mathematical imports. The general matrix claim in the input-revelation source is not adopted; the scalar reduction is reconstructed here and in the review.
