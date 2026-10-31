# v244-A written review: gate-I RMS value and energy identity

Reviewer: **InfoSPR7-2 / info-2**. Author: **InfoHinfPreview-2 / info-3**. Actual `/bin/date` observation before this report: **Tue Oct 27 08:59:20 PDT 2026**. This is a supplied-source, all-variable, same-harness review; it is not parent adoption, a formal proof, an independent-model-family review, a clean-cognition determination, or a primary SPR resumption.

## 1. Decisions and exact scope

Work throughout on the canonical usual augmented one-Brownian filtration with `a,c,d,σ > 0`, `q0 = 2a − σ² > 0`, zero initial state and zero prehistory. Original disturbances are progressively measurable real `E2` processes. For `h ≥ 0`, the actual plant forcing is `f(t) = 1_{t≥h} w(t−h)` and the output is `z = dX`. Norms below are `||u||₂² = E∫₀∞ |u(t)|² dt`. The finite-horizon gain uses the original delayed support and the actual output prefix, not an anticipative or reset plant.

| Frozen obligation | Mathematics decision | Dependency/application/trust decision |
|---|---|---|
| G.1: flow and upper bound, every `h` | **WRITTEN_SUPPORTED** at these hypotheses: `G₂(h) ≤ 2cd/q0`. | The argument uses the scalar stochastic exponential, Brownian independent increments, Bochner Minkowski and the original delayed `E2` input. It applies to finite horizons and infinity. It asserts no exact value for `h>0`. |
| G.3: exact infinite-horizon energy identity, every `h` | **WRITTEN_SUPPORTED with M1 below**: `E∫ X² = (2c/q0) E∫ fX` for every eligible progressive `E2` plant input `f`, in particular every delayed original disturbance. | The signed-input absolute Fubini bridge is supplied in §3, including finite output energy and both time-boundary limits. Do not read “adapted plant input” as removing progressive measurability or `E2`; no extra `E2+` or bounded-input assumption is used. |
| G.2: sharp lower construction at `h=0` | **WRITTEN_SUPPORTED with M2 below** for every symbolic parameter tuple in the stated class. | The disturbance feedback is a progressively measurable adversary input on the original canonical space, not a controller. Strong existence, local moments, the distinct truncated response and its noncircular uniform bound are paid in §4; the small pulse is chosen symbolically, not by a numerical probe. |
| Original gain and v220 value boundary | **WRITTEN_SUPPORTED**: the original infinite-horizon RMS gain and the supremum of its original finite-horizon gains at `h=0` both equal `2cd/q0`. | The new direct proof does not import the missing v21 proof. If the parent subsequently accepts it at exactly this scope, it can prospectively supply the scalar value input behind `NR-GATE-I-WHOLE-V21`; it cannot retrospectively supply v21 source coverage or automatically adopt a larger composition. Applying the separately parent-supported v31 mixed-gain theorem would also retain that theorem's own assumptions and imports. |

**New mathematical findings:** no FATAL or MAJOR found in these four reconstructed obligations; two localized **MINOR proof-precision qualifications** are explicit below. They are paid by the displayed arguments; they are not assertions that the stated conclusions are false. No result in this report is based on a previous favorable review verdict.

**Excluded / NOT_RECONSTRUCTED.** The original 284-LF v21 proof and v54 are not supplied. The v55 Corollary G1/long-preview endpoint is outside the frozen decision and is not reviewed or accepted. No exact intermediate-`h` gain, `h>0` lower equality, exact literal `G₁`, controlled analog, common causal/stationary controller, internal-EMS synthesis, prescribed-γ synthesis, novelty, or executable certificate is concluded. v39 and v57 are also outside this review. C1–C3 and R4 remain STOPPED.

## 2. Source coverage, order and exposure

Main actually read the complete **45-LF** whole-primary checkpoint and **25-LF** opaque ACK, then explicitly released v244-A in `peer-review-v244-A-explicit-body-release-v1.json`, SHA256 `65679baaf92ab71edda5bc12fcc30d233e950cbbd2d9edf9b0e654d1048db5e6`. I then read the complete v245 cadence finding, the complete release including its previously truncated full scope, and the entire own v244-A manifest entry. Before any new proof-body or packet read I wrote and sent `peer-review-v244-A-post-release-specific-preview-contact-addendum-v1.json`, SHA256 `7a0a93b7ede2e52e6ea2baeb5bbed94530baef1c3aad8f6048d80381b065130c`, 17 LF.

I read the entire 27-LF packet receipt and the entire **938-physical-LF** single packet `peer-review-wave-v244-v244-A-part1-v1.md`, live SHA256 `890376dbb9dadb1f5080fdba5e0644f2d7696fbb5fb3fba9aa9f387c08b289a1`, in serial exact raw windows `1–110`, `111–220`, `221–330`, `331–440`, `441–550`, `551–660`, `661–770`, `771–880`, and `881–938`. Every supplied source and ending was read before the fresh reconstruction. The receipt's source-roundtrip and persisted-byte-equality flags bind packet construction; they are not a mathematical verdict.

The sixteen complete supplied bodies are S1–S4 (v9 35 LF, v10 31, v11 40, HOLD 19); S5–S12 (11, 8, 41, 15, 145, 17, 8, 17 LF); S13 v220 parent (79 LF); S14 v21/v25/v26 parent boundary (74 LF); S15 **complete v31** (186 LF, SHA256 `4c2a7b9b2101efc49e29e1bc445eb8d0b3a5daaa9d32ace96999de1ade5d9cea`); and S16 **complete v55** (129 LF, SHA256 `c51562e845a609bc00d46f1e4f65eec77e10355bdbf81db63e7b8a680004c43a`). The v21 parent record is not the original v21 proof; v54 is absent. Source-reading checkpoint 1 is SHA256 `8efbfd84f29237f7d62663519bf9f817dae11bb712cff71bd8c7f32ee0073ac1`; the subsequent reconstruction checkpoint 2 is `d5c51ad98a177736a6120bb00a10e58aa5120580e8789f37683e5c1dc97fff72`.

The reviewer actually authored the earlier v220-A review of the same preview author/source chain, including v31, and an earlier six-file review in the same owner root. The precise positive contact inventory is in the sent addendum. This is serial, nonblind, same-harness review; neither contact list nor this report is an exhaustive access, private-thought, provenance or non-influence census. The old review's favorable verdict is not a premise of the new direct proof.

The supplied S13 records the **later actual parent disposition** of the v220 union: it is written-supported at its stated imports with its `Q-rho` and `Q-zero` qualifications, while the gate-I numerical value remains conditional at `NR-GATE-I-WHOLE-V21`. This updates, rather than backdates, the earlier own checkpoint's then-last-known “received, not adopted” boundary.

## 3. Flow, every-delay upper bound and exact identity

### 3.1 Actual input and stochastic flow

Let `f` first be any real progressively measurable `E2` plant input. The scalar equation

`dX_t = (−aX_t + cf_t)dt + σX_t dW_t`, `X_0 = 0`,

has the usual unique continuous strong solution on finite intervals. Variation of constants gives

`Φ(t,s) = exp(−(a + σ²/2)(t−s) + σ(W_t−W_s))`,

`X_t = c∫₀ᵗ Φ(t,s) f(s) ds`, and `E[Φ(s+u,s)² | F_s] = e^(−q0 u)`.

The future increment in the last equality is independent of `F_s`; no independence between `f(s)` and earlier forcing or between distinct input times is claimed. Progressive measurability gives the needed `F_s`-measurability for almost every `s`. Standard localized strong existence/variation of constants applies on each finite interval; the bound below then puts the actual response in global `E2`.

For original `w`, the shifted `f(t)=1_{t≥h}w(t−h)` is progressive for the physical filtration. Deterministic time substitution gives `||f||₂=||w||₂` on infinity. On a finite horizon `T`, only `w` up to `(T−h)_+` can affect the output; extending that admissible input by zero and taking an output prefix cannot enlarge the infinite-horizon upper bound.

Using `u=t−s`, Minkowski in `L²(Ω×[0,∞))`, then independence at time `s` and Tonelli, gives

`||X||₂ ≤ c ∫₀∞ [ E∫₀∞ Φ(s+u,s)² f(s)² ds ]^(1/2) du`

`= c ||f||₂ ∫₀∞ e^(−q0 u/2)du = (2c/q0)||f||₂`.

This is a genuine product-space `L²` bound, so `z=dX` gives the claimed all-`h` upper bound. Finite horizons use the preceding prefix/shift argument; no infinite-horizon output is silently substituted into a finite-horizon numerator.

### 3.2 M1: absolute Fubini for signed inputs

At v55 LF84 the author invokes the same Minkowski bound for all relevant integrands without displaying the absolute-integrability step. The conclusion is correct for eligible `E2` inputs, but the following **M1** bridge is required: apply the just-proved bound not only to `f`, but to `|f|`. Because `Φ` is positive, define

`Y_t = c∫₀ᵗ Φ(t,s)|f(s)|ds`.

Then `||Y||₂ ≤ (2c/q0)||f||₂`. Tonelli shows that the absolute triangular triple integral arising from the expansion of `X²` is exactly `E∫Y²`, up to the null diagonal. Thus it is finite even when `f` changes sign; there is no appeal merely to cancellation in `E∫X²`.

Consequently ordinary Fubini and `Φ(t,r)=Φ(t,s)Φ(s,r)` for `r≤s≤t` are legitimate. The factor `f(s) f(r) Φ(s,r)` is `F_s`-measurable. Conditional on `F_s`, independent increments give

`E[∫ₛ∞ Φ(t,s)²dt | F_s] = ∫₀∞ e^(−q0 u)du = 1/q0`.

Therefore

`E∫₀∞ X_t²dt = (2c²/q0) E∫₀∞ f(s)∫₀ˢ Φ(s,r)f(r)dr ds`

`= (2c/q0) E∫₀∞ f(s)X_s ds`.

The latter cross term is absolutely integrable by Cauchy–Schwarz, `E∫|fX| ≤ ||f||₂||X||₂`. For finite `T`, the same argument gives the exact version

`E∫₀ᵀ X_t²dt = (2c/q0) E∫₀ᵀ (1−e^(−q0(T−s))) f(s)X_s ds`.

Its exponential remainder tends to zero by dominated convergence against the absolutely integrable `|fX|`. The lower boundary is `X₀=0`. Independently, if `g(s)=(E f(s)²)^(1/2)`, the pointwise bound

`(E X_t²)^(1/2) ≤ c∫₀ᵗ e^(−q0(t−s)/2) g(s)ds`

also tends to zero as `t↓0` and as `t→∞`. For the latter, split at a fixed `A`: the early piece decays exponentially, while the remaining piece is uniformly bounded by `c||e^(−q0·/2)||_{L²(0,∞)} ||g 1_[A,∞)||₂`, which tends to zero as `A→∞`. Thus both actual time boundaries are controlled; no unjustified endpoint cancellation is needed.

The theorem is stated in a setting whose adversary inputs are progressive `E2`. In particular M1 does **not** assert the formula for an arbitrary merely adapted, nonintegrable process or imply that undefined infinite integrals are equal.

## 4. Sharp `h=0` lower bound and noncircular admissibility

Put `λc=q0/(2c)`. Fix a **symbolic** `ε>0` and `0<λ<λc`, and consider the source's adversarial forcing

`w_t = 1_[0,ε](t) + λ X_t 1_(ε,∞)(t)`.

At `h=0` this is the actual plant forcing. It is not a proposed control or a selected numerical diagnostic. Before assuming any infinite energy property, solve the closed scalar SDE with piecewise deterministic, globally Lipschitz linear drift and diffusion. It has a unique global strong solution on the same canonical filtration, with finite second moments on each finite interval; hence the displayed `w` is progressive and locally `E2`.

### 4.1 M2: distinguish the truncated response

The source LF94–98 suppresses the distinction between the feedback response and the response to its truncated input, as well as the harmless restriction `T≥ε`. The following **M2** argument makes the energy step noncircular. For each finite `T≥ε`, define

`w^T = 1_[0,ε] + λ X 1_(ε,T]`.

Local second moments make `w^T` an admissible global `E2` input. Let `X^T` be the actual response driven by `w^T`; it is **not** assumed equal to `X` after `T`. By pathwise uniqueness and identical forcing up to `T`, `X^T=X` on `[0,T]`. Apply §3.2 only to the admissible pair `(w^T,X^T)`. Writing

`P = E∫₀^ε X_s ds`, `Qε = E∫₀^ε X_s² ds`, `Q_T = E∫_ε^T X_s² ds`,

and using nonnegative output energy after `T`, yields

`Qε + Q_T ≤ (2c/q0)(P + λ Q_T)`.

Thus `(1−2cλ/q0) Q_T ≤ (2c/q0)P` uniformly in `T`. Here `P` is finite by local moments. Since `λ<λc`, monotone convergence gives `E∫_ε∞ X²<∞`; the finite pulse already has finite energy, so the original untruncated `w` is indeed `E2`. The proof has not assumed its admissibility to obtain its admissibility. On `[0,ε]`, the equation does not involve `λ`, so `P` and `Qε` are independent of `λ` for fixed `ε`.

### 4.2 A positive symbolic pulse and divergence

During the pulse,

`E X_s = c∫₀ˢ e^(−a(s−r))dr ≥ c s e^(−aε)` for `0≤s≤ε`,

so `P ≥ c ε² e^(−aε)/2 > 0`. The same scalar `L²` flow bound, now using `e^(−q0(s−r)/2)≤1`, gives `(E X_s²)^(1/2)≤cs`, hence `Qε≤c²ε³/3`. Therefore

`P − λc Qε ≥ (c ε²/2) [e^(−aε) − q0 ε/3]`.

By continuity at zero, a sufficiently small positive **symbolic** `ε` makes the bracket positive. Fix that `ε` once, independently of `λ`. This is an all-variable existence argument, not evaluation at a chosen numerical parameter, state or control.

Now the untruncated pair is admissible, so the identity in §3 applies. With `Q=E∫₀∞X²`,

`Q(1−2cλ/q0) = (2c/q0)(P−λQε)`.

The right side stays bounded below by a strictly positive constant as `λ↑λc`, whereas the factor on the left tends to zero. Hence `Q→∞`. Pulse and feedback time supports are disjoint, so

`E∫w² = ε + λ²(Q−Qε)`, and

`E∫z² / E∫w² = d² Q / [ε + λ²(Q−Qε)] → (2cd/q0)²`.

The denominator is finite and positive for each admissible `λ`. Taking square roots and combining with §3.1 proves the exact infinite-horizon RMS value. For each fixed `λ`, truncating the actual input at `T` preserves the actual response through `T`; numerator and denominator of the **finite-horizon** ratio converge to the corresponding finite global energies as `T→∞`. Thus the supremum over original finite horizons reaches the same lower limit. This is a supremum/limit, not an assertion that the critical feedback itself is an admissible maximizing input.

## 5. Applications, imports and precise nonclaims

The scalar autonomous equation is EMS because its squared-flow expectation is `e^(−q0 t)`; the scalar output and constant coefficients fit the original gate-I model on the canonical filtration. In the direct proof above the only substantive inputs are standard scalar Itô/strong-uniqueness and stochastic-exponential facts, independent Brownian increments, progressive-measurability facts, Tonelli/Fubini, Cauchy–Schwarz, Minkowski and elementary limit/convergence theorems. No original v21 proof, v54, storage function, controller certificate, selected numerical probe or prior favorable review verdict is used as a mathematical premise.

S15 v31 and S13's later parent disposition identify an already-supported, separate uncontrolled-EMS statement `g12,∞=G₂,∞` under their named model and imports. The present scope does **not** re-decide that theorem or transfer an old verdict. If the parent accepts this new scalar value and separately applies the already-qualified v31 result, the mixed-gain substitution would additionally consume that prior result and its scope. Any use in the v220 strict literal/RMS statement also retains the applicable AHEAD, `Q-rho`, `Q-zero` and other inherited boundaries; this review does not silently promote the whole union. The absent v21 proof remains NOT_RECONSTRUCTED and earlier v220 coverage cannot be backdated.

## 6. Process and assurance disclosures

After the frozen packet and during this review I actually read the complete `preview-v55-energy-balance-method-separation-disclosure-v248.json`, SHA256 `a0f525c170818900c4cf9704d7fa3f75b580dc7e44596fe33fe94f582a4c8fb1`, and the complete referenced v209 direction, SHA256 `1ec52034a4c80d97d9a271f3a4f2e2eefbfe6c5793cb3a89807adfa58865c932`. The owner reports that the v55 Fubini/conditioning identity is mathematically equivalent to an integrated quadratic/Gramian balance, but reports not consuming a storage function, controller certificate or quarantined guidance. That report is **not** an independent cognition or history audit. As v248 states, equivalence by itself proves neither a violation nor non-consumption; v209 still forbids consuming the stopped route. This review derives the identity by the displayed flow, absolute Fubini and conditional increments; it makes no claim that unobserved prohibited source use did or did not occur. Any actually established forbidden consumption requires its own precise finding and affected-consumer ZERO boundary. No assessment of v39, v57 or v54 follows from this disclosure.

The actually read `SPR-v244-idle-gap-and-opaque-ACK-read-findings-v245.json`, SHA256 `bb61a447b2f95d27273946ade424229b10c181d64a83e619d71c05e702076ce2`, records one distinct cadence PROCESS MAJOR for the 60m22 observed first-wake gap. It does not establish the gap's cause, continuous work or mathematical falsity. All prior author/reviewer/parent findings, the six SPR primary findings, all `post56`/`post60`/`postS126`/self-release guidance and every quarantined consumer remain ZERO/NONINPUT; no finding is cured by this mathematical reconstruction. Protected windows and HELD_C889 were not reopened by this review.

Original SPR78 SOURCE/PROOF/METHOD STOP, HOLD v2, N4 UNKNOWN with historical child exit unestablished, and aux214 STOP persist. No scientific interpreter, calculator, CAS, program, enumeration, solver, replay, test, model CLI, nested agent, selected numerical/control/state probe, timer/poll, Git, deletion, publication or new GO was used. Original science cutoff **2026-10-27T11:05:38-07:00** and final deadline **2026-10-27T12:35:38-07:00** remain unchanged. This is neither round closeout nor a stronger-family/human/formal/kernel/executable/novelty acceptance.

**END OF COMPLETE v244-A REVIEW.**
