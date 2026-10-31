# Matrix preview law: a strict upper bound for the literal E1 gain

Native clock observed before writing: **2026-10-28T18:19:00-0700 PDT**. Same-harness written support with exact analytic specialization checks. Not a true-gain formula, general H∞ synthesis theorem, endpoint transfer, human/cross-model/formal review or novelty determination.

## Exact model and result

Fix finite `T>h≥0`, S=T−h, arbitrary compatible real drift/feedback/output matrices, scalar Brownian motion and scalar progressive disturbance w, zero history/state and w=0 outside [0,S]. Consider

`dx=[(A+BK)x+Bℓ w_t+c w_(t−h)]dt+σx dW`, `z=Dx`,

with actual law `u=Kx+ℓ w_t`, common scalar multiplicative state noise, and `B₀=D₁=0`. For every progressive **E1** input `E||w||₂<∞`—hence every E2 input—the constructed deterministic constants satisfy

`E||z||₂ ≤ (1−ε)Γ E||w||₂ ≤ (1−ε)H E||w||₂`,

with **ε>0** in every nonzero-output case. Here Γ is the L2 norm over input time of the expected output-column norm, and H is its second-moment bound. Consequently γ=Γ is strictly feasible for all nonzero inputs. Γ is **not** asserted equal to the actual gain.

Let P=A+BK and b=Bℓ. The zero-output cases are exactly: h>0 and both b,c invisible under `D P^j`, 0≤j<n; or h=0 and b+c invisible. The true gain is positive otherwise. The candidate gives explicit model-dependent ε; no uniform parameter bound is claimed.

## Complete source and review boundary

The parent read the full [matrix candidate](/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/stochastic-hinf-preview/frontier-20261028-matrix-scalar-noise-preview-literal-gain-gap.txt), the complete [elementary predecessor](/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/stochastic-hinf-preview/frontier-20261028-positive-two-tap-preview-causal-gain-gap.txt), full [f69 review](../review-waves/f69-stochastic-matrix-preview-gain-gap/review-v1.md) including its evidence ending, and [exact specialization evidence](../review-waves/f69-stochastic-matrix-preview-gain-gap/exact-specializations-v1.txt). Review verdict: **0 FATAL / 0 MAJOR / 1 MINOR**.

The MINOR is source provenance: the [linear-preview definitions](../written-releases/info-3-linear-preview-class-definitions-v1.md) supplement an older literal-criterion packet, not independently checked book pages. The parent also read the full [literal-criterion definitions](../written-releases/info-3-literal-criterion-definitions-v1.md), a canonical dossier transcription. The model above is an explicitly interpreted finite-horizon subclass of that printed expectation-of-pathwise-L2 criterion, not an independently authenticated full-book equivalent. It does not silently replace the criterion by RMS energy or claim the more general controller class solved.

## Parent reconstruction

The commuting scalar-noise integrating factor gives the actual vector-valued output column

`K_s(t)=1_(t≥s)ν(t,s)D exp(P(t−s))b + 1_(t≥s+h)ν(t,s+h)D exp(P(t−s−h))c`,

`ν(t,s)=exp(−σ²(t−s)/2+σ(W_t−W_s))`.

For each s the full column uses only future increments, hence is independent of the adapted w_s. This pays `E∫|w_s|||K_s||ds≤Γ E||w||` for E1 inputs by Tonelli; no input second moment is assumed. Cayley–Hamilton and the exposed immediate/delayed prefix give the stated zero cases and positive nonzero-gain argument.

Writing `g_v(t)=D exp(Pt)v`, the exact Gaussian calculation yields

`H²=S∫₀ʰ e^(σ²v)||g_b(v)||²dv + ∫₀ˢ(S−v)e^(σ²v)[||g_b(h+v)+g_c(v)||²+(e^(σ²h)−1)||g_b(h+v)||²]dv`.

The square plus variance term handles arbitrary tap signs/directions and destructive mean cancellation. If h=0 the taps combine; if σ=0 the variance term vanishes.

Near equality in the deterministic Cauchy–Schwarz bound forces the normalized input magnitude close to `C/Γ`. Its early-time amplitude is measurable before an independent future small-ball event and is close in weighted L1 to the full input norm; the full norm itself is **not** assumed independent of that event. On a positive fraction of input-norm weight, the event bounds the stochastic scalar factors and keeps two time-separated column groups uniformly noncollinear, using their nonzero exposed prefixes and an **absolute** vector inner-product bound. The exact Hilbert-space double-integral deficit then forces a positive uniform gap. The predecessor's shape and weighted-event estimates and every constant were reconstructed in f69; no selected maximizing disturbance is assumed.

## Exact check and exclusions

For `P=0,D=1,b=1,c=−1,T=2,h=1,σ=0`, the columns are `1_[s,s+1)` and Γ=H=1. The normal operator has kernel `1−|s−u|`; its Hilbert–Schmidt norm squared is exactly 1/2, so **every** input path obeys `||z||≤2^(−1/4)||w||`. The deterministic w=1 has `||z||²=2/3`. The parent independently checked these rational integral constants, and f69 supplies the written operator calculation. This proves Γ is nonsharp in a concrete actual model, not that its general value is the gain. Further exact noisy/opposite-sign, vector-output and invisible-tap controls are preserved in the review evidence.

Standard imports include the localized Itô integrating factor, Brownian independent increments/small-ball positivity, Gaussian moments, measurable Bochner/Tonelli integration, finite-dimensional analyticity/Cayley–Hamilton and Hilbert inequalities. General matrix multiplicative noise, vector disturbance, nonzero control-noise/direct feedthrough, infinite horizon, controller optimization and actual-gain endpoint transfer are outside this adopted scope. The author's later extensions are separate unreviewed candidates, not accepted by this disposition.
