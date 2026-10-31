# A finite adapted input beats every deterministic input for one stochastic law

**Disposition: same-harness written support at the exact fixed-law scope.** For the scalar law `dx_t=w_t dW_t`, `z_t=x_t`, `x₀=0`, any finite `T>h≥0`, and the ratio `E‖z‖_{L²[0,T]} / E‖w‖_{L²[0,T−h]}`, one explicit predictable, bounded-energy input has ratio greater than

`(2329315625/2168455168)√T > 1.07√T`.

Every deterministic nonzero input has ratio at most `√T`. Thus this finite adapted input beats the entire deterministic class by more than 7% under this **expectation of path norms** criterion. This is a given-law result, not an optimized controller, an exact progressive gain, an E1/E2 endpoint-transfer theorem, or an unrestricted synthesis result.

Native clock observed before composing: **2026-10-28T20:59:41-0700 PDT**, not an asserted creation time.

## Model and construction

The registered [literal criterion](../written-releases/info-3-literal-criterion-definitions-v1.md) is an expectation of pathwise L² norms, and the separately bound [linear-preview class](../written-releases/info-3-linear-preview-class-definitions-v1.md) includes the fixed law `u_t=w_t` with scalar unit control-diffusion and state-output coefficients and other plant coefficients zero. The printed book text is a dossier transcription, not fresh page-image authentication. The following argument uses the canonical Brownian filtration and a progressive square-integrable disturbance supported in `[0,T−h]`.

Let `N=4096`, `δ=min((T−h)/2,T/8192)`, and `B_s=√(N/δ) W_{δs/N}`. This is a standard Brownian motion in the correspondingly time-scaled filtration. Let `τ=inf{s:|B_s|=1}` and `ρ=δ(τ∧N)/N`. Set

`w_t=√(N/δ) 1_{t≤ρ}`.

The left-continuous adapted version displayed here is predictable; changing it to `1_{t<ρ}` changes it only on a `dt×P`-null graph and leaves the Itô integral and path norms unchanged. It is supported in `[0,δ]⊂[0,T−h]`, and `‖w‖²=τ∧N≤4096` almost surely. The solution is `x_t=B_{(tN/δ)∧(τ∧N)}`, so for `t≥δ`, `x_t=B_{τ∧N}`. Consequently

`E‖z‖/E‖w‖ ≥ √(T−δ) E|B_{τ∧N}| / E√(τ∧N)`.

Optional stopping for `B_s²−s` gives `Eτ=1`; Markov therefore gives `E|B_{τ∧N}|≥P(τ≤N)≥4095/4096`. Since `δ≤T/8192`, `√(1−δ/T)≥8191/8192`. The killed-heat expansion for the first exit from `(-1,1)` and termwise integration give

`E√τ = 4√(2π) G/π²`, where `G=Σ_{k≥0}(−1)^k/(2k+1)²`,

with the exact rational enclosure `E√τ<9306/10000`. Substituting yields the strict displayed bound. For deterministic `w`, Itô isometry, Tonelli and Jensen give `E‖z‖≤√T‖w‖`, proving the comparison.

## Evidence and qualifications

- Parent read the complete [finite witness](../../../../information-science/evidence/three-area-20261027-96h/parallel-18/stochastic-hinf-preview/frontier-20261028-explicit-finite-brownian-stopping-gap.txt), [Catalan derivation](../../../../information-science/evidence/three-area-20261027-96h/parallel-18/stochastic-hinf-preview/frontier-20261028-brownian-exit-catalan-certified-gap.txt), [strengthened candidate](../../../../information-science/evidence/three-area-20261027-96h/parallel-18/stochastic-hinf-preview/frontier-20261028-catalan-strengthened-finite-e2-witness.txt) (SHA-256 `a8cb383f407eeba75bc6c0ab98fe553b7f838e8f0eca99168d8cb428ba94f9cb`), and [f138 review](../review-waves/f138-hinf-finite-e2-witness-catalan-gap/review-v1.md), `9d397e6eca476af1e64084329089a865eb659fd933b4a623c011edd912ee72c1`.
- The review independently reconstructs the stopped input, Brownian exit series and gluing of the arithmetic, with no FATAL/MAJOR and four disclosed MINORs. Its [additive correction](../review-waves/f138-hinf-finite-e2-witness-catalan-gap/reviewer-correction-1-v1.md), `26404a8f9dae9a5381dd686d535a6de31f14996171b6f11b4304e9ba231932a2`, corrects its erroneous claim that `1_{t<ρ}` is left-continuous; the predictable version above gives the same integrals. Its exact parts A/B had 31/31 controls pass, but the complete v1 and v2 scripts exited 1 on separate numerical quadrature checks; an additional probe with the singularity removed exited 0 and isolated the quadrature tolerance issue. No blanket passing-script claim is made.
- Parent independently ran the nonblind standard-library [rational checker](../review-waves/f138-hinf-finite-e2-witness-catalan-gap/parent-catalan-fraction-check-v1.py), SHA-256 `6b7437fbb0da7b50702040a151280db915cc999cda00348a3e34cb48a6411e54`; its [receipt](../review-waves/f138-hinf-finite-e2-witness-catalan-gap/parent-catalan-fraction-result-v1.json), `955fd65a4a5fe70e3802031cb9c0f957361f9dbc94bd91bfd1a2e71030d7f5ed`, checks the Catalan/π rational enclosure, exact gap fraction, five preview-window cases and negative controls. It checks arithmetic, not the universal stochastic proof.

## Boundaries

For the RMS criterion `(E‖z‖²)^{1/2}/(E‖w‖²)^{1/2}`, Itô isometry bounds **all** progressive inputs by `√T`, so this is not an RMS-gap result. No exact gain, optimal synthesis, strict E1/E2 endpoint equivalence, priority, human, independent-model-family or formal/kernel proof is established. The separately named limiting/supremal stopping-source claim and later controller-class candidates are not adopted here.
