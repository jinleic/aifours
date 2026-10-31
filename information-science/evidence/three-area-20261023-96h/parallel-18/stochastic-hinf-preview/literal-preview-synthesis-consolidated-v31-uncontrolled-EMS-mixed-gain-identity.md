# Uncontrolled EMS plants: the mixed RMS-input/N1-output gain EQUALS the RMS gain, and the open descriptor question is exactly G1 = G2

Owner **InfoHinfPreview-2 / info-3**. Clock observed with `/bin/date` immediately before writing: **Tue Oct 27 06:54:29 PDT 2026**.

**Status.** NEW COMPLETE WRITTEN OWNER-CANDIDATE; not reviewed or adopted.

- Value side only, under v209 (`1ec52034…`).
- All-variable, source-fixed conventional proofs; no machine-checked identity.
- No chosen numeric, state, control or noise probe, and no decimals.
- No scientific interpreter, Eval, calculator, CAS, program, enumeration, solver or replay; no new GO.

## 0. Statements

**Setting.** Canonical one-Brownian filtration. Constant data (A, A0, C, D0), any D0 rank, any h ≥ 0. The plant is uncontrolled (B = B0 = D1 = 0), or equivalently it is the zero law. The autonomous part dX = AX dt + A0X dW is EMS:

E|X_t|^2 ≤ M e^{−λt} |x_0|^2 for every deterministic x_0.

**Gains.** On infinity, let

- G2,∞ be the RMS gain over original E2 inputs;
- g12,∞ := sup_T g12(T,h), where g12(T,h) := sup_{v≠0} N1(T_C v)/||v||_{L2} (as in v27);
- G1,∞ = sup_T G1(T,h) (adopted UC-INF).

**Proposition G.**

`g12,∞ = G2,∞ < ∞`.

**Corollary G1.**

- `G2,∞ ≤ G1,∞ ≤ √2·G2,∞`.
  - The lower half is proved freshly here for linear uncontrolled EMS data. It does not use v14, although the adopted v14 also gives it at the zero law.
  - The upper half is v27 Corollary C1.
- When B = B0 = D1 = 0, the adopted UC-ALL/UC-INF give kappa_risk,∞ := sup_T kappa_risk(T,h) = G1,∞. Combined with v30 (S = 0 case), this gives an exact reformulation: **the left descriptor inequality g12^Q ≤ kappa_risk is an equality on infinity IF AND ONLY IF the printed literal gain equals the RMS gain, G1,∞ = G2,∞.** The original "inequivalent mean-square replacement" question for uncontrolled EMS plants is therefore EXACTLY the question of tightness of the v27/v30 lower bound.

**Corollary G2 (gate-I anchor; CONDITIONAL on adopted gate I).**

- **Inputs.** The adopted gate-I family dX = (−aX + cw)dt + σX dW, z = dX, h = 0, q0 = 2a − σ^2 > 0. It is EMS, since d(E X^2)/dt = −q0 E X^2 at zero input. Gate I gives G2,∞ = γ* = 2cd/q0.
- **Exact mixed gain.** g12,∞ = γ*. This is an exact evaluation of the mixed descriptor quantity for the whole symbolic family. It replaces v27's two-sided bracket γ*/√2 ≤ g12,∞ ≤ γ*.
- **Literal gain.** γ* ≤ G1,∞ ≤ √2γ* (unchanged). Exact G1 remains OPEN.

**NOT delivered.**

- the exact G1;
- sharpness of √2;
- any controlled-data analog of Proposition G (adversarial controls inside the quotient infimum block the concatenation argument);
- a controller, internal-EMS synthesis or RMS-to-literal synthesis transfer (R4 stays STOPPED).

## 1. Inputs and separation

**Adopted inputs read completely this session:**

| Source | LF | SHA256 (prefix) | Used for |
|---|---|---|---|
| v25 | 348 | `8c381b1f…` | — |
| v26 | 308 | `6666f555…` | UC-ALL, UC-INF, E1/E2 bounds |
| v21/v25/v26 parent | 74 | `1f00e0c6…` | gate I values, for Corollary G2 only |
| v14 parent | 61 | `e89a06e0…` | cross-check only; not used |

**Owner packets cited** (unreviewed; complete proofs in each):

| Packet | SHA256 (prefix) | Cited for |
|---|---|---|
| v27 | `af2abd51…` | Theorem C and Proposition D |
| v30 | `42d86d0d…` | Theorem D′ |
| addendum | `abd0137e…` | cross-reference only |

**Separation.** Nothing in this packet uses:

- a storage function, Riccati/Gramian/LMI certificate or controller construction;
- a selected control or changed output;
- quarantined guidance;
- the RMS source.

**Ordinary tools.** The concatenation of independent increment blocks is an INPUT construction for the adversary; it is not a control or a controller. Beyond it, only ordinary results are used:

- independent and stationary Brownian increments; the time-shift and strong-uniqueness identification of responses;
- the EMS transition bound applied to F_σ-measurable initial states (conditioning plus independent increments);
- Minkowski's and Young's convolution inequalities;
- the i.i.d. L1 law of large numbers; |√a − √b| ≤ √|a − b|.

## 2. Proof of Proposition G

**Step 0 — G2,∞ is finite.**

- **Flow bound.** The input response is X_t = ∫_0^t Φ(t,σ) C w(σ−h) dσ, pathwise, because the forcing is drift-only. Here Φ is the stochastic fundamental flow.
  - For F_σ-measurable ξ with E|ξ|^2 < ∞, independence of increments after σ and EMS give E|Φ(t,σ)ξ|^2 ≤ M e^{−λ(t−σ)} E|ξ|^2.
- **Minkowski.** E|X_t|^2 ≤ (∫_0^t (M e^{−λ(t−σ)} ||C||^2 E|w(σ−h)|^2)^{1/2} dσ)^2.
- **Young.** With kernel k(u) = ||C|| M^{1/2} e^{−λu/2}, ∫ E|X|^2 dt ≤ ||k||_{L1}^2 ∫ E|w|^2. Here ||k||_{L1} = 2||C|| M^{1/2}/λ.
- **Conclusion.** Hence G2,∞ ≤ 2||D0|| ||C|| M^{1/2}/λ < ∞. This is a symbolic bound, not evaluated.

**Step 1 — the easy direction.** g12(T,h) ≤ G2(T,h) by Jensen on the output, and G2(T,h) ≤ G2,∞ by prefix comparison. So g12,∞ ≤ G2,∞.

**Step 2 — reduction to compactly supported inputs.**

- Truncating an infinite-horizon E2 input at T0 converges in L2.
- By Step 0 the outputs converge in L2.
- So G2,∞ is the supremum of ρ(v) := (E||T_C v||^2_{L2(0,∞)})^{1/2}/||v||_{L2} over nonzero E2 inputs v supported in [0, T0], with T0 finite.
- Fix such a v. It is a progressive functional Ψ of the Brownian path.

**Step 3 — concatenation.**

- **Shifted copies.** Fix τ ≥ T0 + h + 1. For k ≥ 0, let θ_k v be the SAME functional applied to the increments W_{kτ+·} − W_{kτ}. It is placed on [kτ, kτ + T0].
  - Each θ_k v is progressive, and the copies are identically distributed.
  - Copies built from disjoint increment windows are independent.
- **The input.** Put w_N := Σ_{k<N} θ_k v. The supports are disjoint, so ||w_N||_{L2}^2 = N||v||_{L2}^2.
- **The horizon.** Take T = Nτ. Then L = T − h ≥ (N−1)τ + T0, so w_N is a finite-horizon original input.

**Step 4 — block outputs.**

- **Notation.** Let I_k := [kτ, (k+1)τ) and z^{(k)} := T_C θ_k v. By linearity, T_C w_N = Σ_k z^{(k)}.
- **Independence of the leading pieces.** z^{(k)} vanishes before kτ, by Lemma L of v28 with A = Ω. On I_k it depends only on increments in I_k, because the response starts from zero at kτ and all input of block k lies in I_k. So the variables X_k := ||z^{(k)} 1_{I_k}||^2 are i.i.d.
- **Their mean.** By time-shift and strong uniqueness, E X_k = m_τ := E||T_C v 1_{[0,τ)}||^2. As τ → ∞, m_τ ↑ m := E||T_C v||^2_{(0,∞)}.

**Step 5 — tails.**

- **Splitting.** On I_k, T_C w_N = a_k + b_k with a_k := z^{(k)} 1_{I_k} and b_k := Σ_{j<k} z^{(j)} 1_{I_k}.
- **Triangle inequality.** In the direct sum ⊕_k L2(I_k),

  `||T_C w_N||_{L2(0,T)} ≥ (Σ_k X_k)^{1/2} − (Σ_k ||b_k||^2)^{1/2}`.

- **Bounding the tails.** By Minkowski in L2(Ω; L2(I_k)),

  (E||b_k||^2)^{1/2} ≤ Σ_{j<k} e_{k−j}^{1/2}, with e_ℓ := E||T_C v 1_{[ℓτ, (ℓ+1)τ)}||^2,

  using time-shift equality in law.
- **EMS decay.** Put t_1 := T0 + h. For t ≥ t_1 the response is autonomous, so for ℓ ≥ 1

  `e_ℓ ≤ ||D0||^2 M E|X_{t_1}|^2 ∫_{ℓτ}^{(ℓ+1)τ} e^{−λ(t − t_1)} dt ≤ ||D0||^2 M E|X_{t_1}|^2 e^{−λ(ℓτ − t_1)}/λ`.

- **Summation.** Hence Σ_{ℓ≥1} e_ℓ^{1/2} ≤ δ_τ := C_v Σ_{ℓ≥1} e^{−λ(ℓτ − t_1)/2}. Here C_v depends on v but not on τ or N. The geometric series gives δ_τ → 0 as τ → ∞.
- **Expectation of the tail term.** E(Σ_k ||b_k||^2)^{1/2} ≤ (Σ_k E||b_k||^2)^{1/2} ≤ N^{1/2} δ_τ.

**Step 6 — law of large numbers.**

- By the i.i.d. L1 law of large numbers, S_N/N := (1/N)Σ_{k<N} X_k → m_τ in L1.
- Then E|(S_N/N)^{1/2} − m_τ^{1/2}| ≤ (E|S_N/N − m_τ|)^{1/2} → 0.
- So E(S_N)^{1/2}/N^{1/2} → m_τ^{1/2}.

**Step 7 — conclusion.**

- Combining Steps 3–6,

  `g12(Nτ, h) ≥ E||T_C w_N||_{L2(0,Nτ)}/||w_N||_{L2} ≥ [E(S_N)^{1/2} − N^{1/2}δ_τ]/(N^{1/2}||v||_{L2})`.

- Let N → ∞, then τ → ∞. This gives g12,∞ ≥ m^{1/2}/||v||_{L2} = ρ(v).
- Taking the supremum over v gives g12,∞ ≥ G2,∞. ∎

## 3. Proofs of the corollaries

**Corollary G1.**

- Since N1(w) ≤ ||w||_{L2}, we have G1(T,h) ≥ g12(T,h). So G1,∞ ≥ g12,∞ = G2,∞.
- The upper half is v27 Corollary C1.
- For the reformulation: kappa_risk,∞ = G1,∞ by the adopted UC-ALL/UC-INF, and g12^Q = g12 when S = 0 (v30). Hence kappa_risk,∞ = sup_T g12^Q(T,h) iff G1,∞ = G2,∞, by Proposition G.

**Corollary G2.**

- The gate-I family satisfies the hypotheses: it is scalar constant data, with EMS since q0 > 0.
- Adopted gate I gives G2,∞ = γ*.
- Proposition G then gives g12,∞ = γ*, and Corollary G1 gives γ* ≤ G1,∞ ≤ √2γ*.

## 4. Boundaries and residual

**What remains open.**

- The value-side core question is now isolated exactly: for uncontrolled EMS plants (gate I included), decide whether G1,∞ = G2,∞.
- Equivalently, decide whether the adapted-quotient descriptor ever exceeds its L2/BMO surrogate after taking the supremum over duals.
- v29 Proposition O shows a strict gap for a SINGLE r. It does not decide the supremum.

**Controlled data.**

- The concatenation argument fails inside the quotient infimum, because adversarial controls can couple blocks.
- So no analog of Proposition G is claimed there.
- The v28/v30 caps remain the only controlled-data value statements.

**Not touched.** The original common causal/stationary printed controller, internal EMS and prescribed-γ synthesis remain UNRESOLVED. The realization routes C1–C3 stay STOPPED (v209).

## 5. Process and assurance

- Written exact mathematics only, after v209 was read FIRST and the adopted inputs were read completely.
- No pinned, frozen or shared edit; no Git, deletion, publication or external model.
- All permanent findings remain, and the ZERO quarantines remain: post56, post60, postS126, the self-released v163 assessment, the protected S242 window, and HELD_C889 (never opened).
- This is not formal, kernel, human, configured-family, executable or novelty acceptance.
- Same18, HOLD v2, science cutoff 2026-10-27T11:05:38-07:00 and delivery deadline 12:35:38 apply. This is not an early final park.

**END OF COMPLETE v31.**
