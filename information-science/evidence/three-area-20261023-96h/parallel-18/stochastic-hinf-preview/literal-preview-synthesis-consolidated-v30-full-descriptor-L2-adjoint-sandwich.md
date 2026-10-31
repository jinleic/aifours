# The FULL actuated risk descriptor at all ranks equals the plain L2 norm of the annihilating adjoint, up to √2

Owner **InfoHinfPreview-2 / info-3**. Clock observed with `/bin/date` immediately before writing: **Tue Oct 27 06:46:56 PDT 2026** (same observation that pinned v29).

**Status.**

- NEW COMPLETE WRITTEN OWNER-CANDIDATE; not reviewed or adopted.
- All-variable, source-fixed conventional proofs; no machine-checked identity.
- No chosen numeric/state/control/noise/boundary/decimal probe.
- No scientific interpreter/Eval/calculator/CAS/program/enumeration/solver/replay; no new GO.
- Value side only, under v209 (`1ec52034…`).

## 0. Result

Take canonical constant data at ALL ranks, all h ≥ 0 and every finite T > h. Let 𝒜 be the adopted family of unit raw output duals whose open-plant BSDE annihilates the control channel (b_φ = 0). Define

`g12^Q(T,h) := sup_{0≠v∈E2} ||Q T_C v|| / ||v||_{L2}`,

where ||Q T_C v|| = inf_{u∈U} N1(T_C v + S u) is the adopted risk numerator and ||v||_{L2} = (E∫|v|^2)^{1/2}.

**Theorem D′ (localization removal for the N1 quotient).**

1. beta1(T,h) = g12^Q(T,h).
2. sup_{φ∈𝒜} ||r_φ||_{L2(dP dt)} = sup_{φ∈𝒜} ||r_φ||_* = g12^Q(T,h).
3. Consequently

   `g12^Q(T,h) ≤ kappa_risk(T,h) ≤ √2·g12^Q(T,h)`,

   and kappa_st ≤ kappa_risk ≤ √2·g12^Q ≤ √2·g2^ol.
4. On infinity the same holds after sup_T.
5. Under CP, the adopted CP-NEC gives G1(T,h;F) ≥ kappa_risk ≥ g12^Q for EVERY original admissible controller F.

Here beta1 is the localized quantity of v27, and ||·||_* is v27's conditional future-energy norm.

**What changes for usability.**

- The adopted descriptor needed the adapted quotient norm nu.
- v27 replaced nu by a conditional future-energy (BMO) norm involving stopping-type localizations.
- Theorem D′ removes that localization on canonical constant data. The FULL actuated descriptor equals, up to a factor in [1, √2], the supremum over 𝒜 of the PLAIN Hilbert norm (E∫_0^L |Π_in C^T p_φ(s+h)|^2 ds)^{1/2} of the projected adjoint.
- Equivalently, it equals the RMS-input/N1-output open-loop risk relaxation g12^Q.
- No essential path supremum, quotient norm or stopping time remains in the certificate.

**NOT delivered.**

- An exact value, a formula for g12^Q, sharpness of √2, or a lower bound by g2^ol.
- A controller or common causal/stationary policy; internal EMS; synthesis.
- The application of kappa_risk outside CP to unpriced non-E1 controls (only v25's kappa_st applies there).

Per-input controls appear only inside relaxation infima.

## 1. Inputs and separation

**Adopted inputs read completely before use this session:**

| Input | LF | Pin |
|---|---|---|
| v25 | 348 | `8c381b1f…` |
| v26 | 308 | `6666f555…` |
| v21/v25/v26 parent record | 74 | `1f00e0c6…` |

Adopted facts used:

- EXACT-RISK, SUPPORT, PAIR and BSD (gate VI);
- the E1-boundedness of S and T_C (v26 §3);
- CONTAINS and CP-NEC (gates VI/VII).

**Prior owner packets** (unreviewed owner-candidates; complete proofs displayed in each):

| Packet | SHA256 | Used here |
|---|---|---|
| v27 | `af2abd51001ca6d16dd3d4415d49104c25110b7f16415689052329f1a77f55b5` | Theorem A, Theorem B (items 1–2) |
| v28 | `e30bdd3d196883dd1b7842472c7f9ab1386a06e4ac78ff96cff3a820f64ac87b` | Lemma L, the time-shift setup |
| v29 | `f1e2a0575ef5f76a25690b4e21574ea631565c4e13f88da50f23d677b2b9bc4c` | context only |

**Separation.** None of the following is used:

- storage functions, Riccati/Gramian/LMI, or a controller construction;
- selected controls or changed outputs;
- quarantined guidance;
- the RMS source.

**New ordinary tools.**

- Bochner–Fubini on the canonical product Ω ≅ Ω_1×Ω_2 (independent increments).
- Separability of E1 spaces on the canonical Wiener space with values in a separable Hilbert space.
- Countably valued measurable near-selections from a countable dense subset of a closed subspace.
- Cauchy–Schwarz.

## 2. Proof of Theorem D′

### 2.1 Easy directions and duality

**β1 ≥ g12^Q.** Take s = 0 and A = Ω in the definition of beta1.

**The duality identity (item 2).** Theorem B's duality proof in v27 (§4, item 1), run with s = 0 and A = Ω, gives

sup_{φ∈𝒜} ||r_φ||_{L2} = sup_{||v||_{L2}≤1} ||Q T_C v|| = g12^Q.

The equality with sup_𝒜 ||r_φ||_* is then v27 Theorem B, item 1, combined with item 1 here.

### 2.2 Main inequality: beta1 ≤ g12^Q

Fix s ∈ [0, L), A ∈ F_s with P(A) > 0, and v ∈ V(s,A).

**Step 1 — localized upper bound.**

- Let U(s,A) be the progressive E1 controls vanishing off A×(s,T].
- Since U(s,A) ⊂ U, SUPPORT gives ||Q T_C v|| ≤ dist_{E1}(T_C v, closure S(U(s,A))).
- By Lemma L (v28 §2) the state vanishes on [0,s] and off A, for v and for every u ∈ U(s,A).
- Lemma L was stated for E2 controls. It extends to E1 controls by E1-continuity of S together with stopping at the control's own energy level (v26 §5.1 approximation).

**Step 2 — shift and product structure.**

- Put T' = T − s, W'_σ = W_{s+σ} − W_s and F'_σ = F_{s+σ}.
- Identify Ω ≅ Ω_1×Ω_2 with P = P_1 ⊗ P_2, where ω_1 = (W_t)_{t≤s} and ω_2 = W'. Up to null sets, F_s is σ(ω_1).
- For each relevant separable Hilbert space H, let X(H) be the progressive E1 space of the canonical filtration of W' on horizon T'.
- **Bochner–Fubini.** Simple tensors Σ_i 1_{A_i}(ω_1) x_i(ω_2), with A_i ∈ F_s and x_i ∈ X(H), are F'-progressive, and their E1 norm equals ∫ ||Σ_i 1_{A_i}(ω_1) x_i||_{X(H)} dP_1. This yields an isometric embedding ι: L1(Ω_1,F_s; X(H)) → E1(F'-progressive).
- **The input.** For P_1-a.e. ω_1 the section ṽ^{ω_1}(σ) = v(s+σ)(ω_1, ·) is canonical-progressive and E2. By Fubini, ∫||ṽ^{ω_1}||_{L2}^2 dP_1 = ||v||_{L2}^2.
- **The input response.** The forcing is drift-only, so the pathwise variation-of-constants formula identifies the shifted output section of T_C v with T_C^can ṽ^{ω_1}. This is the SAME constant-data system on horizon T', driven by W', from zero state.
- **Summary.** T_C v = ι(y) with y(ω_1) := T_C^can ṽ^{ω_1}, and y vanishes for ω_1 ∉ A.

**Step 3 — module property and the range.**

- Take u = Σ_i 1_{A_i}(ω_1) u_i(ω_2), with A_i ⊂ A in F_s and u_i ∈ X(control space).
- The F_s-measurable bounded factors pass through the Lebesgue and Itô integrals on the shifted interval, because F'_0 = F_s. Uniqueness then gives S u = ι(Σ_i 1_{A_i} ⊗ S^can u_i).
- Such u lie in U(s,A). Hence closure S(U(s,A)) contains ι of every simple function A → S^can(U^can).
- Let M := closure S^can(U^can) in X(H_out). Then closure S(U(s,A)) ⊇ ι(L1(A; M)), since simple M-valued functions are dense in L1(A; M) and each is approximated by simple S^can(U^can)-valued ones.

**Step 4 — fiberwise distance.**

- X(H_out) is separable, so M has a countable dense subset {m_j}. Fix η > 0.
- Let j(ω_1) be the least j with ||y(ω_1) − m_j|| < dist(y(ω_1), M) + η, and put m(ω_1) := m_{j(ω_1)}.
- m is countably valued and measurable. It satisfies ||m(ω_1)|| ≤ 2||y(ω_1)|| + η, since 0 ∈ M gives dist ≤ ||y||. So m ∈ L1(A; M), and

  `dist(T_C v, closure S(U(s,A))) ≤ ||y − m||_{L1(A;X)} ≤ ∫_A dist(y(ω_1), M) dP_1 + η`.

- By definition, dist(y(ω_1), M) = ||Q^can T_C^can ṽ^{ω_1}||, the canonical horizon-T' risk numerator. It is at most g12^Q(T',h)·||ṽ^{ω_1}||_{L2(Ω_2)}.

**Step 5 — integrate.** Let η ↓ 0. Cauchy–Schwarz in ω_1 gives

`||Q T_C v|| ≤ g12^Q(T',h) ∫_A ||ṽ^{ω_1}|| dP_1 ≤ g12^Q(T',h) P(A)^{1/2} ||v||_{L2}`.

**Step 6 — horizon monotonicity: g12^Q(T',h) ≤ g12^Q(T,h).**

- An input counted up to T' − h, zero-extended, is counted up to T − h.
- For ANY control on [0,T], the horizon-T output's N1 norm dominates the N1 norm of its restriction to [0,T'].
- By causality that restriction is the horizon-T' output produced by the control's restriction to [0,T'].
- So the horizon-T risk numerator dominates the horizon-T' one.
- The canonical problem driven by W' on horizon T' is an isometric copy of the original canonical problem on horizon T'.

**Conclusion.** Dividing Step 5 by P(A)^{1/2}||v||_{L2} and taking suprema gives beta1 ≤ g12^Q.

### 2.3 Remaining items

- **Item 3:** from v27 Theorem B, beta1 ≤ kappa_risk ≤ √2·beta1, with beta1 = g12^Q. kappa_st ≤ kappa_risk is adopted CONTAINS. g12^Q ≤ g2^ol holds because N1 ≤ RMS inside each infimum.
- **Item 4:** take sup_T.
- **Item 5:** adopted CP-NEC.

∎

## 3. Consistency checks

- **Uncontrolled data.** With S = 0, Theorem D′ reduces to v27 Proposition D: g12^Q = g12 and G1 ∈ [g12, √2·g12].
- **Gate-I anchor (conditional).** Combined with v29 Corollary U and the adopted gate I, G1,∞ ∈ [γ*, √2γ*]. The exact value is OPEN.
- **Deterministic inputs.** For a deterministic input v, ||v||_{L2} = N1(v). Hence g12^Q ≥ sup over deterministic v of ||Q T_C v||/||v||, which is the deterministic-input risk gain.
- **Strictness.** Whether the left inequality kappa_risk ≥ g12^Q is ever strict, or always an equality, is OPEN at the descriptor level. v29 Proposition O shows strictness only at the level of a single nu.

## 4. Boundaries and residual

- **Where D′ applies.** Theorem D′ requires the canonical one-Brownian filtration and constant data.
- **Earlier statements that do not need this.** v27 Theorems A/B and v28 Theorem E hold more generally (Theorem A needs only the usual conditions).
- **CP.** CP is required to apply kappa_risk to actual unknown controllers. Outside CP only kappa_st applies, and kappa_st ≤ √2·g12^Q still caps it.
- **Original problem.** The common causal/stationary printed controller, internal EMS, prescribed-γ synthesis and same-γ equivalence remain UNRESOLVED. The realization routes C1–C3 stay STOPPED (v209). The R4 RMS-transfer route is not used.

## 5. Process and assurance

**What was done.**

- Written exact mathematics only, after v209 was read FIRST and the adopted inputs were read completely.
- No pinned/frozen/shared edit; no Git, deletion, publication or external model.

**Retained histories.**

- All permanent findings remain.
- ZERO quarantines remain: post56, post60, postS126, the self-released v163 assessment, and the protected S242 window.
- HELD_C889 was never opened.

**Not claimed.**

- No formal, kernel, human, configured-family, executable or novelty acceptance.
- Same18, HOLD v2, science cutoff 2026-10-27T11:05:38-07:00 and delivery 12:35:38 apply.
- This is not an early final park.

**END OF COMPLETE v30.**
