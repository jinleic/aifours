# The FULL risk descriptor at all ranks is capped by √2 times the adapted open-loop RMS relaxation

Owner **InfoHinfPreview-2 / info-3**. Clock observed with `/bin/date` immediately before writing this body: **Tue Oct 27 06:40:35 PDT 2026**.

**Status.** NEW COMPLETE WRITTEN OWNER-CANDIDATE. Not reviewed, not adopted.

- All-variable, source-fixed conventional proofs only.
- No machine-checked identity.
- No chosen numeric, state, control, noise, boundary or decimal probe.
- No scientific interpreter, Eval, calculator, CAS, program, enumeration, solver, replay, CLI, nested agent or new GO.
- This is value-side work only, under v209 (`1ec52034a4c80d97d9a271f3a4f2e2eefbfe6c5793cb3a89807adfa58865c932`).

## 0. Result and non-results

**Prerequisite.** v27 (`literal-preview-synthesis-consolidated-v27-descriptor-BMO-evaluability.md`, SHA256 `af2abd51001ca6d16dd3d4415d49104c25110b7f16415689052329f1a77f55b5`, 283 LF) proved two things:

- the adapted input quotient nu is equivalent to the conditional future-energy norm, with constants 1 and √2;
- beta1 ≤ kappa_risk ≤ √2·beta1, with an exact identity for the BMO descriptor.

v27 is my own unreviewed owner-candidate. Its proofs are short and complete, and the steps used here (Theorem A, Theorem B items 1–2) are restated as citations to its displayed proofs. A combined gate must read both packets completely.

**What this packet adds.** It extends the "sharper all-variable bound" from the uncontrolled domain to the FULL actuated descriptor at ALL ranks, with no CP assumption for the abstract value statement:

- **Theorem E:** kappa_risk(T,h) ≤ √2·beta2(T,h), where beta2 is a localized Hilbert (RMS) open-loop relaxation.
- **Proposition F:** on the canonical filtration with constant data, beta2 = g2^ol(T,h), the ordinary adapted open-loop RMS relaxation. So kappa_risk ≤ √2·g2^ol, and also kappa_st ≤ √2·g2^ol.
- **Corollary F1:** for every original controller whose actual controls are E2, kappa_risk ≤ √2·G2(F). The risk/bounded-test necessity can therefore NEVER certify infeasibility of a literal level γ when some E2-control controller has RMS gain below γ/√2. This is a precise limitation of the descriptor itself.

**NOT delivered:**

- evaluation of g2^ol (no Riccati, storage or LQ construction is performed or consumed);
- a matching lower bound;
- an exact value;
- a controller, common causal/stationary policy, internal EMS or synthesis;
- the CP extension.

Per-input controls appear ONLY inside relaxation infima, never as a policy.

## 1. Setting, adopted inputs, separation

**Model and descriptor.** Model (P) has arbitrary ranks, a single Brownian motion, a canonical augmented filtration, zero gain state/history, and finite T > h ≥ 0 with L = T − h. All definitions follow v26 §§2–4 (adopted gate VI): S, T_C, U, Q, kappa_risk, and the PAIR/SUPPORT facts. kappa_st is from v25 (adopted gates II/III), and kappa_st ≤ kappa_risk is adopted CONTAINS.

**Sources read completely before use** this session, raw, through END:

| Source | LF | SHA256 (prefix) |
|---|---|---|
| v25 | 348 | `8c381b1f…` |
| v26 | 308 | `6666f555…` |
| parent adoption record | 74 | `1f00e0c6…` |

**Not consumed:**

- storage function, Riccati/Gramian/LMI, or controller construction;
- selected control or changed output;
- quarantined post56/post60/postS126/self-release guidance;
- RMS source.

The only new tools are:

- the localization identity for linear SDEs with an F_s-measurable indicator;
- the independent-σ-field tensor structure of L2 progressive spaces;
- norms of Hilbert tensor-product operators.

**Notation.** For s ∈ [0, L) and A ∈ F_s with P(A) > 0:

- V(s,A) is the progressive E2 inputs on [0, L] vanishing off A×(s, L];
- V_U(s,A) is the progressive E2 controls on [0, T] vanishing off A×(s, T];
- ||·||_{L2} = (E∫|·|^2)^{1/2}.

Define

- `beta2(T,h) := sup_{s,A,0≠v∈V(s,A)} inf_{u∈V_U(s,A)} ||T_C v + S u||_{L2} / ||v||_{L2}`;
- `g2^ol(T,h) := sup_{0≠v∈E2} inf_{u∈E2 controls} ||T_C v + S u||_{L2} / ||v||_{L2}`.

Both are finite, by the E2 bound of v26 §3 (take u = 0).

## 2. Localization lemma (any data, any ranks)

**Lemma L.** If v ∈ V(s,A) and u ∈ V_U(s,A), then the open-loop response X to (v, u) vanishes on [0, s], and also on A^c × [0, T]. Hence T_C v + S u = 1_A (T_C v + S u).

**Proof.**

1. Before s, the control vanishes, and the delayed forcing Cv(t−h) vanishes up to s + h. So X = 0 on [0, s].
2. For t ≥ s, multiply the integral equation on [s, t] by the bounded F_s-measurable 1_{A^c}. This factor passes inside both the Lebesgue integral and the Itô integral on [s, t].
3. Since 1_{A^c}u = 0 and 1_{A^c}v = 0, the process Y = 1_{A^c}X solves dY = AY dt + A0 Y dW on [s, T] with Y_s = 0.
4. Strong uniqueness gives Y ≡ 0. The output D0X + D1u then vanishes off A. ∎

**Note.** The diffusion forcing B0u dW is covered. No pathwise variation-of-constants formula is needed.

## 3. Theorem E — the full descriptor is at most √2 times a localized RMS relaxation

**Theorem E.** At ALL ranks, all h ≥ 0 and every finite T > h:

`kappa_st(T,h) ≤ kappa_risk(T,h) ≤ √2·beta1(T,h) ≤ √2·beta2(T,h)`.

On infinity: sup_T kappa_risk ≤ √2·sup_T beta2.

**Proof.**

1. The first inequality is adopted CONTAINS.
2. The second is v27 Theorem B, item 2, proved there from v27 Theorem A plus adopted EXACT-RISK, SUPPORT and PAIR.
3. For the third, fix s, A and v ∈ V(s,A). By SUPPORT, ||Q T_C v|| = inf over u ∈ U of N1(T_C v + S u). That infimum is at most the infimum over the smaller set V_U(s,A) ⊂ E2 ⊂ U.
4. For u ∈ V_U(s,A), Lemma L and Cauchy–Schwarz give

   `N1(T_C v + S u) = E[1_A ||T_C v + S u||] ≤ P(A)^{1/2} ||T_C v + S u||_{L2}`.

5. Dividing by P(A)^{1/2}||v||_{L2} and taking suprema gives beta1 ≤ beta2.
6. The infinite-horizon statement follows by taking suprema in T. ∎

## 4. Proposition F — localization removal for the Hilbert relaxation

**Proposition F.** On the canonical one-Brownian filtration with constant data, at ALL ranks, all h ≥ 0 and every finite T > h:

`beta2(T,h) = g2^ol(T,h)`.

Consequently kappa_risk(T,h) ≤ √2·g2^ol(T,h), and sup_T kappa_risk ≤ √2·sup_T g2^ol.

**Proof of beta2 ≥ g2^ol.** Take s = 0 and A = Ω.

**Proof of beta2 ≤ g2^ol.** Fix s, A. Put T' = T − s, W'_σ = W_{s+σ} − W_s and F'_σ = F_{s+σ}. Then W' is an F'-Brownian motion, independent of F'_0 = F_s, and F'_σ = F_s ∨ F^{W'}_σ (augmented).

1. **Shift.** By Lemma L the state vanishes on [0, s]. Shifting time by s identifies pairs (v, u) ∈ V(s,A)×V_U(s,A) isometrically with F'-progressive pairs (ṽ, ũ) supported on A. The output norm is unchanged. The SDE becomes the SAME constant-data system on [0, T'] driven by W', started from zero.
2. **Tensor structure.** Let K_in, K_U, K_out be the L2 spaces of F^{W'}-progressive processes on the respective horizons, and 𝒦_in, 𝒦_U, 𝒦_out the F'-progressive ones.
   - Simple predictable processes with F'_{t_i}-measurable coefficients are dense.
   - L2(F_s ∨ F^{W'}_{t_i}) is the closed span of products ξζ with ξ ∈ L∞(F_s) and ζ ∈ L∞(F^{W'}_{t_i}), by products of indicators of generating π-systems.
   - Independence gives E[ξξ'<η,η'>] = E[ξξ'] E<η,η'>.
   - Hence 𝒦_* ≅ L2(Ω,F_s) ⊗ K_* as Hilbert tensor products.
3. **Module property.** For bounded F_s-measurable ξ and canonical η, ξ passes through the Lebesgue and Itô integrals on [0, σ], because F'_0 = F_s. Uniqueness then shows that the response to ξη equals ξ times the response to η. By linearity, density and boundedness, the shifted operators are T'_C = I ⊗ T_C^can and S' = I ⊗ S^can. Here T_C^can and S^can are the open-loop maps of the SAME system on horizon T' with the canonical filtration of W'. By the canonical isomorphism, these are isometric copies of the original canonical-filtration maps on horizon T'.
4. **Distance.** The closure of (I ⊗ S^can)(1_A L2(F_s) ⊗ K_U) is 1_A L2(F_s) ⊗ closure S^can(K_U). Let P^⊥ be the orthogonal projection of K_out onto the complement of closure S^can(K_U). Since T'_C ṽ lies in 1_A L2(F_s) ⊗ K_out,

   `inf_{u∈V_U(s,A)} ||T_C v + S u||_{L2} = ||(I ⊗ P^⊥ T_C^can) ṽ|| ≤ ||P^⊥ T_C^can|| · ||v||_{L2}`.

   The last step uses ||I ⊗ X|| = ||X||. By definition ||P^⊥ T_C^can|| = g2^ol(T', h). No measurable selection of near-optimal controls is needed: only the distance to a closed subspace enters.
5. **Horizon monotonicity.** g2^ol(T', h) ≤ g2^ol(T,h) for T' ≤ T.
   - An input counted up to T' − h, zero-extended, is an input counted up to T − h.
   - For any control on [0, T], the output norm on [0, T] dominates its restriction to [0, T'].
   - By causality, that restriction depends only on the control on [0, T'].
6. **Conclusion.** Hence inf_{u∈V_U(s,A)} ||T_C v + S u||_{L2} ≤ g2^ol(T,h)||v||_{L2}, so beta2 ≤ g2^ol. ∎

## 5. Corollary F1 — a precise limitation of the necessity descriptors

**Hypothesis.** Let F be ANY original admissible controller such that, for every original E2 input w, its actual control u_F is an E2 control on [0, T]. Strong uniqueness then identifies the actual output with the open-loop response T_C w + S u_F. Put G2(T,h;F) := sup_w (E||z_F||^2)^{1/2}/||w||_{L2}.

**Claim.** g2^ol ≤ G2(T,h;F), because u_F is one admissible control in the infimum. Hence

`kappa_st(T,h) ≤ kappa_risk(T,h) ≤ √2·G2(T,h;F)`

on canonical constant data, at all ranks.

**Interpretation.** Whenever one such controller has RMS gain below γ/√2, neither adopted necessity value (kappa_st, valid without CP, or kappa_risk, applicable under CP) can certify infeasibility of the literal level γ. This bounds what the descriptors can ever prove.

**Not claimed:**

- that such a controller satisfies the literal bound;
- that its N1 gain is related to the descriptor;
- that the descriptors are complete;
- sufficiency or internal EMS.

Under CP the adopted CP-NEC still gives G1(F) ≥ kappa_risk.

## 6. Boundaries and remaining gaps

**Not established:**

- an exact formula for g2^ol, beta1 or kappa_risk at actuated data;
- a lower bound of kappa_risk by g2^ol;
- sharpness of √2 (v27 Theorem A constant);
- measurable-selection localization removal for the N1 quantity beta1 at actuated data (Proposition F concerns the Hilbert quantity only).

**Scope boundaries.**

- Outside CP, kappa_risk is not applied to unpriced non-E1 unknown controls; only v25's kappa_st applies to them.
- Stationary printed controllers, the common causal policy, internal EMS and prescribed-γ synthesis remain UNRESOLVED.
- The realization routes C1–C3 stay STOPPED (v209).

## 7. Process and assurance

**Scope of the work.**

- Written exact mathematics only, after v209 was read FIRST and the adopted inputs were read completely.
- No pinned, frozen or shared edit; no Git, deletion, publication or external model.

**Retained.** All permanent findings and ZERO quarantines remain: post56, post60, postS126, the self-released v163 assessment, the protected S242 window, and HELD_C889 (never opened).

**Not claimed.** This is not formal, kernel, human, configured-family, executable or novelty acceptance. Same18, HOLD v2, science cutoff 2026-10-27T11:05:38-07:00 and delivery deadline 12:35:38 apply. This is not an early final park.

**END OF COMPLETE v28.**
