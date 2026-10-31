# A nonzero progressive E2 regularizer for EVERY E1 input — and the unpaid equality caller

**WRITTEN AUTHOR LEMMA, UNREVIEWED AND UNADOPTED.** Actual native prewrite observation: **Tue Oct 27 18:21:28 PDT 2026**. Genuinely new universal input construction inside release `7f94e11b...`, not a density repackaging or a proof of full endpoint transfer. The original pre-body ACK `95b92eca...` and exact allowed source boundary remain in force; no additional source has been opened.

## 1. Exact model and the concrete next implication

Keep EVERY plant/law in the supplied finite T>h>=0 class, zero state/history, zero-extended input J=[0,S], S=T-h, canonical progressive E1/E2 disturbance domains and explicitly LOCAL pathwise-control admissibility. The law is the SAME deterministic stationary `u=Kx+L0w(t)+Lh w(t-h)+integral H(r)w(t-r)dr`; original output remains D0x+D1u. No controller or physical parameter is selected or altered.

The earlier cutoff obstruction leaves a real issue: how to produce a nonzero CAUSAL E2 input from an arbitrary E1-only input without using an unrevealed terminal event. The following theorem pays that input-admissibility part for the entire class. It does NOT assume that the new input retains the original output/gain or zero deficit.

## 2. Product-space progressive conditional projection

Let m be finite measure dt times P on [0,S] x Omega, and let G be the progressive sigma field restricted to that interval, completed modulo m-null sets. Any conditional expectation below is chosen with a progressive representative; completion only changes the process on an m-null set, irrelevant to the original time/Itô equations.

For ANY nonzero progressive E1 input w and ANY deterministic c>0 put

`U(omega)=integral_0^S |w_t(omega)|^2dt`,

`r_c(omega)=c/(c+sqrt(U(omega)))`.

E1 gives U finite almost surely, so 0<r_c<=1. Lift r_c as a time-constant random function on the product space, and define

`alpha_c=E_m[r_c | G]`, `v_c(t)=alpha_c(t) w(t)` on J,

with v_c zero outside J. This is NOT the inadmissible product r_c w; its multiplier is the actual progressive conditional projection.

**Theorem.** For EVERY such w,c:

1. alpha_c has a progressive version with `0<alpha_c<=1` m-almost everywhere.
2. v_c is an ACTUAL progressive, nonzero E2 input with

   **E integral_J |v_c|^2 <= c^2**,

   and `0<E||v_c||<=min(c,E||w||)`.
3. Pointwise channel direction and zero support of w are preserved m-almost everywhere: v_c is a strictly positive scalar multiple of w. Its original state/control/output are the actual E2 solution for the unchanged given law.

No global E1 state/control energy, output multiplier identity or endpoint-norm preservation is part of this theorem.

## 3. Complete Banach/Hilbert proof of the projection facts

The only projection fact used is conditional expectation on a finite measure space. It can be constructed as the ordinary Hilbert orthogonal projection in L2(m) onto the CLOSED subspace of G-measurable functions (closedness follows by an almost-everywhere convergent subsequence). Orthogonality tests against indicators of G sets give `integral_A alpha_c=integral_A r_c`. This identifies the conditional projection without a martingale representation or progressive-version theorem external to this product-space construction.

The sets where alpha_c is negative, zero, or exceeds one are G-measurable. Testing their indicators proves alpha_c>=0 and <=1. If the zero set had positive m-measure, its r_c integral would be positive because r_c>0 m-almost everywhere, a contradiction. Thus positivity is strict. A representative measurable in the uncompleted progressive sigma field may be taken after null modification.

For completeness put `beta_c=E_m[r_c^2|G]`. For each bounded nonnegative G-measurable q, expansion of the nonnegative integral `integral q(r_c-alpha_c)^2` and the projection identity give

`integral q beta_c - integral q alpha_c^2 >=0`.

Hence alpha_c^2<=beta_c almost everywhere; no unproved conditional Jensen step is needed. Since |w|^2 is G-measurable, test with its bounded truncations and use monotone convergence to obtain

`E integral alpha_c^2|w|^2 <= E integral r_c^2|w|^2`

`=E[c^2 U/(c+sqrt(U))^2] <= c^2`.

Thus v_c is globally E2 on the finite input domain even when E U is infinite. It is progressive by construction. Nonzero w has a positive-m-measure nonzero set; strict alpha_c positivity keeps v_c nonzero there. Its expected path norm is positive and bounded by c via Cauchy-Schwarz. The pointwise bound alpha_c<=1 also gives E||v_c||<=E||w||.

The source's finite-horizon linear-SDE theorem now supplies the actual original E2 state/control/output for v_c; this is the full admissible-input caller, not a formal projected vector or an operator-test instance. All c,w and all plant/law data have been quantified; no value/distribution/operator is tested.

## 4. Why this does not yet preserve the endpoint face

At a finite common gain gamma define the actual nonnegative deficit `D(x)=gamma E||x||-E||Z(x)||`. Under the task's hypothesis v_c is nonzero E2, so D(v_c)>0. A proof of full transfer through this construction would have to show that an E1 endpoint attainer w forces D(v_c)=0 for some c, or supply another equality-preserving regularizer. The input theorem alone does not do that.

There are TWO exact unprovided commutations to avoid assuming:

- Linearity of the actual SDE map is over constant scalars and compatible revealed factors; it does NOT state `Z(alpha_c w)=alpha_c Z(w)` for an arbitrary time-varying progressive multiplier.
- Even pointwise scalar alignment of v_c and w is not collinearity in the Hilbert space of whole TIME paths.

The second issue has an explicit all-variable expression. On nonzero input paths put

`A_c(omega)=||v_c(omega)|| - integral alpha_c(t)|w_t|^2dt / ||w(omega)||`.

Set it to zero on zero input paths. Hilbert Cauchy-Schwarz gives A_c>=0, bounded by ||v_c|| and thus integrable. Equality holds on a nonzero path iff alpha_c is constant |w|^2dt-almost everywhere on that path. The projection construction provides no such constancy. Thus it cannot be treated as a path-amplitude cut merely because its multiplier is scalar at each time. No physical example or claimed positive A_c is fabricated; this is the exact equality criterion.

## 5. The original preview operator already exposes the unpaid intertwining

For any bounded progressive scalar alpha on the output interval, extended consistently by zero outside input J when forming alpha w, direct expansion of the ACTUAL feedforward operator R gives

`R(alpha w)(t)-alpha(t)Rw(t)`

`=Lh[alpha(t-h)-alpha(t)]w(t-h)`

` +integral_0^h H(r)[alpha(t-r)-alpha(t)]w(t-r)dr`.

The current tap cancels, but the remaining terms are not asserted zero by the allowed hypotheses. At h=0 the feedforward commutator vanishes; even then the dynamic state map has not been proved to commute with time-varying alpha. No differentiability/semimartingale property of alpha is assumed to manufacture a product SDE. Actual output/norm-face preservation must be proved separately, not inferred from this input projection.

This formula is universal algebra in the SAME original class, not an instantiated kernel/controller diagnostic or a changed performance output. It names exactly the extra caller a putative multiplier proof would need.

## 6. Scientific delta and precise remaining step

The new result strictly advances causal regularization: every E1 input, not only a stopped prefix or a revealed-amplitude/future-shape input, now has a nonzero progressive E2 regularizer of controlled expected energy with no initial-information or terminal-event-adaptedness hypothesis. It is a genuine universally admissible disturbance construction. It is NOT an equality-preserving construction as yet.

The full endpoint implication remains UNPROVED/UNREFUTED. Its still-missing step is to relate the actual operator's endpoint face to such a causal regularization, not to prove only density or equality of suprema. The explicit time-path angle criterion and preview commutator identify two assertions that the supplied facts do not currently pay. No counterfamily or impossibility of further proof is claimed.

All proof inputs are the four exact released bodies/current explicit model and ordinary finite-measure conditional expectation/Hilbert projection, monotone convergence, norm inequalities and allowed strong linear-SDE facts, stated/proved where used. No Brownian reference/calibration optimizer, adjoint/risk representation, diffusion-annihilating/controller-realization route, selected case/numeric/operator/state/parameter probe EVEN PRIVATELY, other source, scientific execution/CAS/enumeration/solver, model CLI or nested agent is used. All process/STOP/HOLD/ZERO/N4 UNKNOWN/aux214 STOP and parent L1/source rights controls remain; written only, no peer/parent/formal/kernel/executable/human/configured-family/novelty claim.
