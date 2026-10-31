# Preview delay for general uncontrolled plants: monotonicity, the long-delay limit of the mean-square level, and an initial-interval structure of the equality set

Owner **InfoHinfPreview-2 / info-3**. Clock observed with `/bin/date` immediately before writing: **Tue Oct 27 08:29:00 PDT 2026**.

**Status.**

- NEW COMPLETE WRITTEN OWNER-CANDIDATE, written as a separate successor. Author-written and unreviewed; not adopted; no gate.
- Value side only, under v209 (`1ec52034…`) and v236 (`062ccf9e…`).
- All-variable, source-fixed conventional proofs. No machine-checked identity.
- No chosen numeric probe.
- No scientific interpreter, Eval, calculator, CAS, program, enumeration, solver or replay. No new GO.
- Frozen v27–v32 untouched. v31/v32 are used only through their v220 parent-supported conclusions, with Q-rho, Q-zero and Q1 carried additively (`6d0103ff…`).

## 0. Setting and statements

**Setting.** GENERAL uncontrolled constant data, as in v32 Theorem S and v34 Theorem R:

- any n and any A, A0, C, D0;
- B = B0 = D1 = 0;
- canonical one-Brownian filtration;
- EMS: E|Φ(t,s)x|^2 ≤ M e^{−λ(t−s)}|x|^2 for the stochastic flow Φ.

**Preview delay δ ≥ 0.** The adversary chooses a progressive E2 input w, and the plant receives w̃(t) := w(t−δ), which is zero for t < δ. Write G1(δ) and G2(δ) for the literal (E path-L2) and RMS gains at delay δ. G_rob is δ-independent (erratum `6569cb34…`).

**Deterministic-input mean-square gain.** Define

`G2^det := sup over deterministic v ∈ L2 of (E||T_C v||^2)^{1/2}/||v||`.

This is a deterministic quantity of the plant: the norm of the second-moment kernel E[k(t,s)^T k(t,s')], with k(t,s) = D0 Φ(t,s) C. Always G2^det ≤ G2(δ) ≤ G_rob.

**Theorem PM (monotonicity).** G1(δ) and G2(δ) are non-increasing in δ.

**Theorem LD (long-delay limit).** For every δ > 0,

`G2^det ≤ G2(δ) ≤ G2^det + 2ε(δ)`, where ε(δ) := ||D0|| ||C|| ∫_{δ/2}^∞ (E||Φ(u)||^2)^{1/2} du ≤ ||D0|| ||C|| (nM)^{1/2} (2/λ) e^{−λδ/4}.

Hence G2(δ) ↓ G2^det as δ → ∞, exponentially fast.

**Theorem EI (equality set).** Let E := {δ ≥ 0 : G1(δ) = G2(δ)}.

- E = {δ : G2(δ) = G_rob}, by v34 Theorem R applied at each δ. E is an initial interval of [0, ∞): empty, [0, δ_0], [0, δ_0) or all of [0, ∞).
- E = [0, ∞) iff G2^det = G_rob.
- Equivalently, there are deterministic inputs v_k with E||T_C v_k||^2/||v_k||^2 → G_rob^2. In that case the deterministic worst case is reached in mean square by noise-insensitive inputs, and equality holds at EVERY delay.
- Otherwise there is δ* < ∞ with G2(δ) < G1(δ) ≤ √2·G2(δ) for every δ ≥ δ*. Strictness for all sufficiently long previews.

**Consistency.**

| Case | Outcome | Source |
|---|---|---|
| Noise-invisible kernels | G2^det = ‖T_det‖ = G_rob, so E = [0, ∞) | v33 E, v36 (b) |
| Bi-isotropic, singular A0 | E = [0, ∞) | v49 |
| Bi-isotropic, invertible A0 | E = {0} | v48 DI, v49 |
| Planar PR-1E on the v44 locus | E = {0} | v44 at δ = 0, v48 DE |
| PR-1E off the locus, VIS-1/VIS-P plants, SISO planar | E = ∅ | v44, v37, v38, v41 |

**NOT delivered.**

- The limit of G1(δ) as δ → ∞.
- An example with E = [0, δ_0] and δ_0 > 0.
- A closed form of G2^det beyond the classes above.
- Controlled data, a controller, synthesis, or an RMS-to-literal transfer. C1–C3 and R4 STOPPED.

## 1. Inputs and separation

**Adopted inputs** (read completely this session):

| Input | LF | Pin |
|---|---|---|
| v25 | 348 | `8c381b1f…` |
| v26 | 308 | `6666f555…` |
| v21/v25/v26 parent | 74 | `1f00e0c6…` |
| v220 parent | 79 | `13fbb1a2…` |

**Parent-supported conclusions.** v31 (G2 < ∞, G2 ≤ G1) and v32 S, both stated for any preview h ≥ 0 (v31 LF14, v32 LF18) and supported at that domain by v220; and v27 C1.

**Author candidates** (unreviewed): v34 `6fcca986…` (Theorem R), erratum `6569cb34…`, and v33/v36/v37/v38/v41/v44/v48/v49 for the consistency table only.

**Separation.**

- The tools are the standard variation-of-constants formula X_t = ∫_0^t Φ(t,s) C w̃(s) ds for drift inputs, independence of the flow Φ(t,s) from F_s, the EMS flow bound, Minkowski's integral inequality, conditional expectation, and the observation that delayed inputs are known before the recent noise.
- No storage function, dissipation inequality, Riccati/LMI, Gramian certificate, controller, selected control, changed output, quarantined guidance or RMS source is used. The adversary strategies are input strategies only.

**Note on the delay.** The preview h of v31/v32 is exactly the delay δ here. So the parent-supported v31 and v32 conclusions apply at each δ directly. The unreviewed v34 Theorem R is built on them at each fixed δ, with G_rob δ-independent.

## 2. Proof of Theorem PM

Let δ_2 > δ_1 and let w be admissible at delay δ_2. Put w'(s) := w(s − (δ_2 − δ_1)), with w'(s) := 0 for s < δ_2 − δ_1.

- w' is progressive, because w(s − Δ) is F_{s−Δ} ⊆ F_s-measurable.
- w' has the same path energy and the same distribution of path energy.
- It produces the same plant input w'(t − δ_1) = w(t − δ_2), hence the same output.

So every ratio achievable at δ_2 is achievable at δ_1, for both the N1 and the RMS criterion. ∎

## 3. Proof of Theorem LD

**Lower bound.** Deterministic inputs are admissible at every delay, and a delay shift is an isometry on deterministic inputs.

**Upper bound.** Fix an admissible w at delay δ, with plant input w̃. Split the output as T w̃ = T_≤ w̃ + T_> w̃, using memory u := t − s ≤ δ/2 and > δ/2 respectively.

1. **Long memory.** By Minkowski in u, ||T_> w̃||_{L2(dP dt)} ≤ ∫_{δ/2}^∞ ||D0 Φ(t, t−u) C w̃(t−u)||_{L2(dP dt)} du.
   - Φ(t, t−u) is independent of F_{t−u}, which contains w̃(t−u).
   - So E|D0 Φ(t,t−u) C w̃(t−u)|^2 ≤ ||D0||^2 ||C||^2 E||Φ(u)||^2 E|w̃(t−u)|^2.
   - Hence ||T_> w̃|| ≤ ε(δ) ||w̃||.
   - The EMS bound E||Φ(u)||^2 ≤ nM e^{−λu} gives the displayed estimate for ε(δ).
2. **Short memory, the key step.** For s ∈ [t − δ/2, t], w̃(s) = w(s−δ) is F_{t−δ}-measurable, hence F_{t−δ/2}-measurable. The kernel k(t,s) = D0 Φ(t,s) C depends only on Brownian increments on [s, t] ⊆ [t − δ/2, t], which are independent of F_{t−δ/2}. Therefore

   E[ |(T_≤ w̃)(t)|^2 | F_{t−δ/2} ] = q_t[w̃],

   where for a deterministic function v, q_t[v] := E'|∫_{t−δ/2}^t k'(t,s) v(s) ds|^2 with an independent copy k'.
3. **Integrating.** For each ω, ∫ q_t[v] dt evaluated at v = w̃(ω) equals E'||T'_≤ v||^2. For deterministic v,

   (E'||T'_≤ v||^2)^{1/2} ≤ (E'||T' v||^2)^{1/2} + (E'||T'_> v||^2)^{1/2} ≤ (G2^det + ε(δ)) ||v||,

   by Step 1 applied to deterministic inputs. Hence ||T_≤ w̃||^2_{L2(dP dt)} ≤ (G2^det + ε(δ))^2 ||w̃||^2.
4. **Conclusion.** ||T w̃|| ≤ (G2^det + 2ε(δ)) ||w̃||, and ||w̃|| = ||w||. ∎

## 4. Proof of Theorem EI

**Characterization of E.** At each δ, v34 Theorem R (with G2(δ) < ∞ by v31) gives G1(δ) = G2(δ) iff G_rob = G2(δ). Since G2(δ) ≤ G_rob, this means G2(δ) = G_rob.

**Initial interval.** By Theorem PM, G2 is non-increasing and bounded by G_rob. So {δ : G2(δ) = G_rob} is an initial interval.

**E = [0, ∞) iff G2^det = G_rob.**

- If G2^det = G_rob, then for every δ, G_rob ≥ G1(δ) ≥ G2(δ) ≥ G2^det = G_rob.
- Conversely, if G2^det < G_rob, Theorem LD gives G2(δ) < G_rob for all δ with 2ε(δ) < G_rob − G2^det. Then Theorem R gives G1(δ) > G2(δ).
- The reformulation with v_k is the definition of G2^det.

**Consistency table.**

- **Noise-invisible kernels.** The deterministic kernel gives E||T v||^2 = ||T_det v||^2.
- **Singular bi-isotropic (v49).** The deterministic inputs along ker A0 reach G_rob.
- **Invertible bi-isotropic.** v48 DI shows E ∌ δ > 0, so G2^det < G_rob.
- **PR-1E on the locus.** E ∋ 0 (v44, δ = 0) and E ∌ δ > 0 (v48 DE).
- **Strict classes.** G2(0) < G_rob already. ∎

## 5. Meaning for the original preview problem (value side only)

**More preview helps the mean-square criterion.** For every uncontrolled EMS plant, increasing the preview delay can only lower both levels. The mean-square level converges exponentially fast to a deterministic second-moment quantity G2^det.

**When the printed level matches.** The printed E path-L2 level coincides with the mean-square level at long previews exactly in the "noise-insensitive worst case" situation G2^det = G_rob, and then it coincides at EVERY preview. In every other situation the mean-square replacement is strictly optimistic for all sufficiently long previews.

**Synthesis.** No controller, internal-EMS or synthesis statement is made. The original synthesis problem remains UNRESOLVED.

## 6. Process and assurance

- Written exact mathematics only, after v209 and v236 were read FIRST and the adopted inputs and the v220 parent were read completely.
- Frozen v27–v32 untouched.
- No pinned/frozen/shared edit. No Git, deletion, publication or external model.
- All permanent findings and ZERO quarantines remain: post56, post60, postS126, the self-released v163 assessment, and the protected S242 window. HELD_C889 was never opened.
- No formal, kernel, human, configured-family, executable or novelty acceptance.
- Same18, HOLD v2, science cutoff 2026-10-27T11:05:38-07:00 and delivery deadline 12:35:38 apply. This is not round closeout.

**END OF COMPLETE v50.**
