# The adapted input quotient is a BMO norm up to √2 — evaluability of the adopted risk/output descriptor

Owner **InfoHinfPreview-2 / info-3**. Clock observed with `/bin/date` immediately before writing this body: **Tue Oct 27 06:35:24 PDT 2026**.

**Status: NEW COMPLETE WRITTEN OWNER-CANDIDATE**, not reviewed or adopted.

- All-variable, source-fixed conventional proofs only.
- No identity is machine-checked.
- No chosen numeric/state/control/noise/boundary/decimal probe.
- No scientific interpreter, Eval, calculator, CAS, program, enumeration, solver, replay, CLI or nested agent; no new GO.

This packet works ONLY on the value/usable-certificate side of the original problem, as permitted by v209.

## 0. What is new, and what this is NOT

The adopted v25/v26 descriptors express necessary literal levels through the **adapted input quotient norm**

`nu(r) = inf{ ||g||_{L∞(Ω;H_in)} : Π_in g = r } = sup_{0≠w∈E2} |E<r,w>| / N1(w)`.

Both packets explicitly warned that nu must NOT be replaced by an essential path supremum, and they gave no explicit formula for it. This packet proves three things.

- **A. Two-sided evaluability of nu** with universal constants 1 and √2, by the explicit conditional future-energy (BMO-type) norm

  `||r||_*^2 := sup_{s∈[0,L]} esssup E[ ∫_s^L |r_t|^2 dt | F_s ]`.

- **B. An exact identity.** The supremum of `||r_φ||_*` over the ENTIRE adopted control-annihilating dual family equals a localized conditional-RMS-input quotient gain beta1. Hence beta1 ≤ kappa_risk ≤ √2·beta1 at ALL ranks, all h ≥ 0 and every finite horizon.
- **C. A sharper all-variable bound** on the ENTIRE adopted uncontrolled domain (B = B0 = D1 = 0, ANY D0 rank, ANY A, A0, C, h):
  - G1 ≤ √2·G2;
  - on canonical constant data, g12 ≤ G1 ≤ √2·g12, where g12 is the RMS-input/mean-output gain.

  At the source-fixed gate-I anchor, conditional on that adopted gate, the adopted bracket [γ*, 2√2γ*] narrows to [γ*, √2γ*].

**NOT delivered:**

- an exact value of any literal gain, including scalar gate I;
- sharpness of √2;
- a controller, common causal/stationary policy or internal EMS;
- synthesis, N&S or same-γ RMS equivalence;
- an application of kappa_risk to unpriced non-E1 controls outside CP.

The per-input control infimum appears only inside the adopted quotient norm. It is a relaxation, never a policy.

## 1. Authority, reads, separation and ordinary inputs

**Authority chain:**

- v204 (`ae54a378…`) lifted STOP111 prospectively, but only for genuinely source-separated work.
- My report `primary-continuation-102319-checkpoint-109-…` (`9fc6540d…`) stopped the realization routes C1–C3.
- Main actually read it and issued v209: `Preview-v204-realization-stop-and-full-descriptor-research-direction-v209.json` (`1ec52034a4c80d97d9a271f3a4f2e2eefbfe6c5793cb3a89807adfa58865c932`). I read v209 completely FIRST.

**Adopted inputs read completely before use**, raw, through END:

| Source | LF | SHA256 |
|---|---|---|
| v25 | 348 | `8c381b1f3f0a861952ec2deb75a4e30b8e54e2634a5b22ed0d2b63b3be906318` |
| v26 | 308 | `6666f5551003bc7f38dcd4ca7436431515765e06f9989c6734849014ed5f6745` |
| parent adoption record `preview-v21-v25-v26-stochastic-risk-entire-parent-v1.md` | 74 | `1f00e0c6ccd0a9a75bb7bbdaabb7717247eaff02d43698193201489690ed2a4b` |

They are used only at their adopted cuts:

- v25 gates II/III, i.e. the bounded-test family and kappa_st;
- v26 gate VI: EXACT-RISK, SUPPORT, BSD, PAIR, and E2 adjoints r_φ, b_φ;
- v26 gate VIII (UC-ALL);
- gate I values (G2 = γ*, γ* ≤ G1), ONLY in the explicitly conditional anchor corollary §6.

Mandatory Q1 (finite-terminal dual reduction) is retained. Nothing here uses the overbroad density sentence.

**Separation.** The following are consumed nowhere:

- controller, storage function, Riccati/Gramian/LMI certificate, selected control or changed output;
- post56/post60/postS126/self-release guidance, an old control/boundary/graph replay, or the RMS source.

The key new step is a duality inequality between two norms on adapted processes. My UNADOPTED v22 claimed G1 ≤ √2·G2 by a different monotone-transfer route. v22 is NOT a premise here, and §5's overlap with it is disclosed. No novelty is claimed. Fefferman/Garsia-type BMO duality has classical ancestry, and the needed inequality is proved in full below.

**Ordinary inputs.** Conditional expectation and Tonelli/Fubini; pathwise Cauchy–Schwarz; the absolutely continuous chain rule; dominated and monotone convergence; product structure of canonical Wiener measure (independent increments) and measurability of sections (only in §5.2); the explicit variation-of-constants formula for linear SDEs with drift-only forcing (only in §5).

## 2. Setting copied from the adopted cut

Use the original constant-data plant (P):

`dX = (AX + Bu + Cw(t−h))dt + (A0X + B0u)dW`, `z = D0X + D1u`, at arbitrary ranks.

- Gain state and negative input history are zero.
- Fix finite T > h ≥ 0 and L = T − h.
- Inputs are ALL progressive expected-L2 (E2) processes on [0, L], zero-extended. Output and control are counted on [0, T].
- N1(v) = E||v|| with the time-L2 path norm. ||v||_{L2} := (E∫|v|^2)^{1/2}.
- U, W, Zout, S, T_C, Z = closure S(U), Q and kappa_risk(T,h) = ||Q T_C|| are as in v26 §§3–4.
- For a unit raw dual φ ∈ L∞(Ω;H_out), BSD gives (p,q) ∈ S2×H2. Then b_φ = B^Tp + B0^Tq + D1^Tf and r_φ = Π_in[C^Tp(·+h)] ∈ E2(H_in).

**Adopted facts used:**

- **PAIR:** E<φ, T_Cv + Su> = E<r_φ, v> + E<b_φ, u> for E2 v, u.
- **SUPPORT:** dist(y, Z) = sup over unit raw φ annihilating Z of E<φ, y>, with annihilation IFF b_φ = 0.
- **EXACT-RISK:** kappa_risk = sup over 𝒜 of nu(r_φ), where 𝒜 := {unit raw φ : b_φ = 0}.
- **UC-ALL:** if B = B0 = D1 = 0, then G1(T,h) = ||T_C|| = kappa_risk(T,h), and G1,∞ = sup_T G1(T,h).
- **v25:** kappa_st = sup over bounded tests of nu(r), with every bounded-test r in E2.

The filtration is v26's canonical one-Brownian filtration with usual augmentation. Theorem A itself needs only the usual conditions.

## 3. Theorem A — the adapted input quotient is equivalent to a conditional future-energy norm

For progressive r ∈ E2(H_in) on [0, L], let `Y_s := E[∫_s^L |r_t|^2 dt | F_s]` and `||r||_*^2 := sup_{s∈[0,L]} esssup Y_s` (deterministic s only).

**Theorem A.**

`||r||_* ≤ nu(r) ≤ √2·||r||_*`,

including the case where both sides are +∞.

**Lower bound.**

1. Fix s ∈ [0, L) and A ∈ F_s with Q_A := E[1_A ∫_s^L |r|^2] > 0.
2. Put w := 1_A·1_(s,L]·r. It is progressive, since A ∈ F_s and the time set is (s, L]. It is E2, because its energy is at most that of r. So w is an original input.
3. Then E<r,w> = Q_A. By Cauchy–Schwarz, N1(w) = E[1_A (∫_s^L|r|^2)^{1/2}] ≤ P(A)^{1/2} Q_A^{1/2}.
4. Hence nu(r) ≥ Q_A/N1(w) ≥ (Q_A/P(A))^{1/2}.
5. Since Y_s is F_s-measurable, its essential supremum equals the supremum of E[1_A Y_s]/P(A) over such A, and E[1_A Y_s] = Q_A. Taking suprema over A and s gives nu(r) ≥ ||r||_*.

**Energy inequality.** For f ≥ 0 integrable on [0, L], (∫_0^L f)^2 = 2∫_0^L f(s)(∫_s^L f(t)dt) ds. Apply this with f = |r|^2 and use Tonelli. For fixed s, |r_s|^2 is F_s-measurable, so

`E(∫_0^L|r|^2)^2 = 2∫_0^L E[|r_s|^2 Y_s] ds ≤ 2||r||_*^2 E∫_0^L|r|^2 ≤ 2||r||_*^4`,

using E∫_0^L|r|^2 = E Y_0 ≤ ||r||_*^2.

**Stieltjes lemma.**

- **Claim.** Let B be continuous, adapted and nondecreasing on [0, L], with B_0 a positive constant and E B_L^2 < ∞. If ||r||_* < ∞, then `E∫_0^L |r_t|^2 B_t dt ≤ ||r||_*^2 · E B_L`.
- **Partition and split.** Take a deterministic partition 0 = s_0 < … < s_N = L and write I_k = ∫_{s_k}^{s_{k+1}} |r|^2 and ΔB_k = B_{s_{k+1}} − B_{s_k} ≥ 0. Monotonicity of B gives
  - ∫ |r|^2 B dt ≤ Σ_k B_{s_{k+1}} I_k = Σ_k B_{s_k} I_k + Σ_k ΔB_k I_k;
  - Σ_k B_{s_k} I_k = B_0 ∫_0^L|r|^2 + Σ_j ΔB_j ∫_{s_{j+1}}^L|r|^2.
- **Main sum.** ΔB_j ≥ 0 is F_{s_{j+1}}-measurable, so E[ΔB_j ∫_{s_{j+1}}^L|r|^2] = E[ΔB_j Y_{s_{j+1}}] ≤ ||r||_*^2 E ΔB_j. Also E[B_0∫_0^L|r|^2] ≤ B_0||r||_*^2. These sum to at most ||r||_*^2 E B_L.
- **Remainder.** Σ_k ΔB_k I_k ≤ (max_k ΔB_k) ∫_0^L|r|^2.
  - It tends to 0 pathwise as the mesh tends to 0, by uniform continuity of B.
  - It is dominated by B_L ∫_0^L|r|^2, which is integrable by Cauchy–Schwarz, E B_L^2 < ∞ and the energy inequality.
  - Dominated convergence therefore proves the claim.

**Upper bound.**

1. Let w be an original E2 input. Put A_t = ∫_0^t|w|^2 and, for ε > 0, B_t = (A_t + ε)^{1/2}. Then B is continuous, adapted and nondecreasing, with E B_L^2 = E A_L + ε < ∞.
2. Pathwise Cauchy–Schwarz gives ∫|r||w| ≤ (∫|w|^2/B)^{1/2}(∫|r|^2 B)^{1/2}.
3. The chain rule for the absolutely continuous A gives ∫_0^L |w_t|^2/B_t dt = 2(B_L − B_0) ≤ 2B_L.
4. Take expectations, apply Cauchy–Schwarz and the lemma:

   `|E<r,w>| ≤ E∫|r||w| ≤ (2E B_L)^{1/2}(||r||_*^2 E B_L)^{1/2} = √2 ||r||_* E(A_L+ε)^{1/2}`.

5. Let ε ↓ 0. By monotone convergence, E(A_L+ε)^{1/2} ↓ E A_L^{1/2} = N1(w). Taking the supremum over w gives nu(r) ≤ √2||r||_*. ∎

**Remarks.**

1. For deterministic r, ||r||_* = ||r||_{L2(0,L)} = nu(r) (v25's aligning input), so the lower constant 1 is attained.
2. No essential path supremum, no contraction of Π_in in a mixed norm, no martingale representation and no inf/sup exchange is used.
3. **Corollary A1.** If nu(r) < ∞, then r has bounded conditional future energy. In particular, for every φ ∈ 𝒜, `E[∫_s^L|r_φ|^2 | F_s] ≤ kappa_risk(T,h)^2` a.s. for every s. In the uncontrolled case the same holds for EVERY unit raw φ, with bound G1(T,h)^2.

## 4. Theorem B — exact identity for the BMO descriptor, and the √2 sandwich

For s ∈ [0, L) and A ∈ F_s with P(A) > 0, let V(s,A) be the progressive E2 inputs vanishing outside A×(s, L]. Define

`beta1(T,h) := sup_{s, A, 0≠v∈V(s,A)} ||Q T_C v|| / ( P(A)^{1/2} ||v||_{L2} )`,

where ||Q T_C v|| = inf_{u∈U} N1(T_C v + Su), the adopted risk numerator.

**Theorem B.** At ALL ranks, all h ≥ 0 and every finite T > h:

1. `sup_{φ∈𝒜} ||r_φ||_* = beta1(T,h)` (exact identity);
2. `beta1(T,h) ≤ kappa_risk(T,h) ≤ √2·beta1(T,h)`;
3. for the v25 bounded-test family, `sup_tests ||r||_* ≤ kappa_st(T,h) ≤ √2·sup_tests ||r||_*`, and kappa_st ≤ kappa_risk ≤ √2·beta1 (the adopted CONTAINS);
4. on infinity, sup_T beta1 ≤ sup_T kappa_risk ≤ √2·sup_T beta1.

**Proof of 1.**

- By definition of the essential supremum, ||r_φ||_*^2 = sup_{s,A} E[1_A∫_s^L|r_φ|^2]/P(A).
- E[1_A∫_s^L|r_φ|^2]^{1/2} is the L2(dP dt) norm of 1_{A×(s,L]} r_φ. That process belongs to V(s,A), so this norm equals sup over v ∈ V(s,A) with ||v||_{L2} ≤ 1 of E<r_φ, v>.
- For φ ∈ 𝒜, PAIR with u = 0 gives E<r_φ, v> = E<φ, T_C v>.
- These are two independent suprema, so sup_{φ∈𝒜} sup_v = sup_v sup_{φ∈𝒜}.
- SUPPORT identifies sup_{φ∈𝒜} E<φ, T_C v> = dist(T_C v, Z) = ||Q T_C v||. The set 𝒜 is symmetric, so signs cause no change.
- Dividing by P(A)^{1/2} and taking sup_{s,A} yields the identity. No inf/sup exchange occurs: the control infimum lives inside SUPPORT, which the adopted gate proved first.

**Proof of 2.**

- EXACT-RISK and Theorem A give sup_𝒜 ||r_φ||_* ≤ kappa_risk ≤ √2·sup_𝒜 ||r_φ||_*. Then apply 1.
- **Direct proof of the lower half.** For v ∈ V(s,A), N1(v) = E[1_A||v||] ≤ P(A)^{1/2}||v||_{L2}. Hence ||QT_Cv||/(P(A)^{1/2}||v||) ≤ ||QT_Cv||/N1(v) ≤ kappa_risk.

**Proofs of 3 and 4.** Item 3 is Theorem A applied to each bounded test; its r is in E2. Item 4 takes suprema in T.

**Application boundaries.**

- **Under CP (JD0 = 0, JD1 = I).** The adopted CP-NEC gives, for every original admissible controller F, G1(T,h;F) ≥ kappa_risk(T,h) ≥ beta1(T,h). The quotient lower bound can never exceed √2·beta1.
- **Outside CP.** Only the v25 route applies to actual unknown controllers: G1(F) ≥ kappa_st ≥ sup_tests ||r||_*. No lower-bound application of kappa_risk or beta1 to unpriced non-E1 controls is asserted.
- **Never asserted:**
  - that an infimizing control exists;
  - a common causal selector;
  - that a stationary printed law attains beta1;
  - internal EMS.

## 5. Theorem C — the ENTIRE uncontrolled domain: G1 ≤ √2·G2, and the mixed gain g12

Let B = B0 = D1 = 0, with ANY D0 rank, ANY constant A, A0, C and any h ≥ 0. Then S = 0 and ||QT_Cv|| = N1(T_Cv). Write G2(T,h) := sup_{v≠0} (E||T_Cv||^2)^{1/2}/||v||_{L2}, which is finite by v26 §3, and g12(T,h) := sup_{v≠0} N1(T_C v)/||v||_{L2}.

### 5.1 Localization and the bound beta1 ≤ G2

**Localization.**

- Let v ∈ V(s,A). The forcing Cv(t−h) vanishes before s + h and off A, so X = 0 on [0, s].
- For t ≥ s, multiply the integral equation by the F_s-measurable indicator 1_{A^c}. Since 1_{A^c}v = 0, Y := 1_{A^c}X solves the homogeneous linear SDE on [s, T] with Y_s = 0. Hence Y ≡ 0.
- Therefore T_C v = 1_A T_C v.

**Bound.** Cauchy–Schwarz gives N1(T_Cv) = E[1_A ||T_C v||] ≤ P(A)^{1/2}(E||T_Cv||^2)^{1/2} ≤ P(A)^{1/2} G2(T,h) ||v||_{L2}. So beta1 ≤ G2(T,h).

**Corollary C1.** With UC-ALL and Theorem B, for ALL uncontrolled data:

- G1(T,h) = kappa_risk ≤ √2·beta1 ≤ √2·G2(T,h);
- G1,∞ = sup_T G1(T,h) ≤ √2·sup_T G2(T,h) ≤ √2·G2,∞.

The last step holds because a finite counted input, zero-extended, is an infinite-horizon input whose output prefix is dominated.

### 5.2 Exact localization removal on canonical constant data

**Proposition D.** On the canonical one-Brownian filtration with constant data, beta1(T,h) = g12(T,h). Hence

`g12(T,h) ≤ G1(T,h) ≤ √2·g12(T,h) ≤ √2·G2(T,h)`.

Also g12 = sup over unit raw φ of ||r_φ||_{L2(dP dt)}.

**Proof.**

1. **Lower inclusion.** beta1 ≥ g12 by taking s = 0 and A = Ω.
2. **Product structure.** Fix s and A, and use the canonical product structure Ω ≅ Ω_1×Ω_2 (Wiener measures on [0, s] and on the increments after s), which holds by independent increments. Up to null sets, F_s is the σ-field of ω_1. A ∈ F_s is a set of ω_1, and v ∈ V(s,A) has the form 1_A(ω_1)ṽ(t, ω_1, ω_2).
3. **Sections.** By Fubini, for P_1-a.e. ω_1 the section ṽ^{ω_1}(u, ·) = v_{s+u}(ω_1, ·) is progressive for the increment filtration and E2: its energies integrate to E∫|v|^2.
4. **Restart.** Drift-only forcing gives the pathwise variation-of-constants formula X_{s+u} = Φ_u ∫_0^u Φ_σ^{-1} C ṽ(σ−h) dσ. Here Φ is the fundamental solution driven by the increments ω_2. So the section of the output is EXACTLY the output of the SAME constant-data system restarted at time 0, on horizon T − s, with input ṽ^{ω_1}.
5. **Conditional bound.** Hence E_2||z(ω_1, ·)|| ≤ g12(T−s, h)(E_2||ṽ^{ω_1}||^2)^{1/2}. Horizon monotonicity gives g12(T−s, h) ≤ g12(T,h): an input counted up to T − s − h is also counted up to T − h, and its longer output norm dominates the shorter one.
6. **Integrate.** Integrating over ω_1 ∈ A with Cauchy–Schwarz in ω_1 gives N1(T_Cv) ≤ g12(T,h) P(A)^{1/2} ||v||_{L2}. So beta1 ≤ g12.
7. **The φ formula.** The final identity is Theorem B's duality with s = 0 and A = Ω. In the uncontrolled case every unit raw φ annihilates Z = {0}.

∎

**Infinite horizon.** g12,∞ := sup_T g12(T,h) satisfies g12,∞ ≤ G1,∞ ≤ √2·g12,∞.

**Why g12 is a usable certificate.** The INPUT side of g12 is now Hilbert (L2(dP dt)). The heavy-tailed N1 input normalization that made nu non-explicit has been removed, at a cost of at most √2. The OUTPUT side remains the literal N1 norm, so g12 is not an RMS gain. No exact formula for g12 is claimed.

## 6. Source-fixed gate-I anchor (CONDITIONAL; not a replacement target)

The adopted gate I covers the uncontrolled scalar h = 0 family dX = (−aX + cw)dt + σX dW, z = dX, with q0 = 2a − σ^2 > 0. It gives G2,∞ = γ* = 2cd/q0 and γ* ≤ G1.

This family lies inside the domain of Theorem C. Conditional on gate I's adopted values, Corollary C1 and Proposition D give:

- **G1.** γ* ≤ G1,∞ ≤ √2·γ*.
- **g12.** γ*/√2 ≤ g12,∞ ≤ γ*.

Here g12,∞ ≤ G2,∞ follows from Jensen, and g12,∞ ≥ G1,∞/√2 from Proposition D.

This narrows the adopted bracket [γ*, 2√2γ*]. The exact value of G1 for gate I remains OPEN. No parameter instance, decimal or probe is used, and the full descriptor domain (§§3–5) is the target, not this anchor. My unadopted v22 reached the same upper bracket by another route; it is not used.

## 7. Exact remaining value-side and original gaps

**Value side.**

- Exact evaluation of nu is open beyond the √2 band and the deterministic case.
- Exact evaluation of beta1, g12 or kappa_risk for actuated or general data is open, including the scalar gate-I value.
- The sharpness of √2 in Theorem A for adapted processes is not claimed.
- For controlled data, localization removal (Proposition D) would require a measurable near-optimal control selection; it is NOT asserted.

**Original problem.** These remain explicitly UNRESOLVED and are not touched:

- ONE common causal/stationary printed controller;
- internal EMS;
- prescribed-γ synthesis or N&S;
- same-γ RMS equivalence;
- application beyond CP to unpriced non-E1 controls.

The realization routes C1–C3 stay STOPPED under v209.

## 8. Process and assurance

**Scope of the work.**

- Written exact mathematics only, after v204 → cp109 → Main's actual read → v209 read FIRST, with the adopted inputs read completely first.
- No pinned, frozen or shared file was edited.
- No Git, deletion, publication or external model was used.

**Retained histories.** All permanent findings and ZERO quarantines remain: post56, post60, postS126, the self-released v163 assessment, the protected S242 window, and HELD_C889 (never opened).

**Not claimed.** This is not formal, kernel, human, configured-family, executable or novelty acceptance. Same18, HOLD v2, science cutoff 2026-10-27T11:05:38-07:00 and delivery deadline 12:35:38 apply. This is not an early final park.

**END OF COMPLETE v27.**
