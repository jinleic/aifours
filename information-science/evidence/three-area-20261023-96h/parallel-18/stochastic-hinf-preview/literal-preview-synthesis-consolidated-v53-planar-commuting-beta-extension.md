# The full planar commuting class Ā = αI + βJ: the robust-gain formula and the bi-isotropic delay dichotomy are unchanged by a deterministic rotation β

Owner **InfoHinfPreview-2 / info-3**. Clock observed with `/bin/date` immediately before writing: **Tue Oct 27 08:40:55 PDT 2026**.

**Status.**

- NEW COMPLETE WRITTEN OWNER-CANDIDATE, written as a separate successor. Author-written, UNREVIEWED and not adopted. Main's v240 decision applies: no review wave before cutoff.
- Value side only, under v209 (`1ec52034…`) and v236 (`062ccf9e…`).
- All-variable, source-fixed conventional proofs. No machine-checked identity.
- No chosen numeric probe.
- No scientific interpreter, Eval, calculator, CAS, program, enumeration, solver or replay. No new GO.
- Frozen v27–v32 untouched; v31/v32 are used through their v220-supported conclusions, with Q-rho, Q-zero and Q1 carried additively (`6d0103ff…`).

## 0. Setting and statements

**Class PC (planar commuting rotation noise).** Uncontrolled constant data with:

- n = 2 and A0 = σJ, σ ≠ 0;
- Ā := A − A0^2/2 commuting with J;
- arbitrary C ∈ R^{2×p} and D0 ∈ R^{q×2};
- preview δ ≥ 0;
- canonical one-Brownian filtration.

The real 2×2 matrices commuting with J are exactly {αI + βJ}, so Ā = αI + βJ.

- **EMS.** By v34 Lemma DS (commuting form), the autonomous solution is X_t = R(σW_t + βt) e^{αt} x_0, so |X_t| = e^{αt}|x_0|. The class is EMS iff α < 0.
- Assume α < 0 and put a := 1/|α|.
- Class PR of v39–v52 is the case β = 0, μ = α.

**Theorem B1 (robust gain).**

`G_rob = a · max_{|u|=1} |C^T u| |D0 u|`,

independently of β and of δ. So v46 Theorem RGP holds on the whole class PC. The closed-form literal certificate G2 ≤ G1 ≤ min(√2·G2, a·max_u |C^T u||D0 u|) holds for every plant in PC and every δ.

**Theorem B2 (bi-isotropic delay dichotomy).** If CC^T = κI and D0^T D0 = mI with κ, m > 0, then for every β:

- G1(0) = G2(0) = G_rob = a√(mκ);
- for every δ > 0,

  `G2(δ)^2 ≤ mκa^2 θ(δ) < G_rob^2`,

  where θ(δ) = e^{−qδ} + (1 − e^{−qδ})/(qa) and q = |α| + σ^2/2.

Hence the equality set is exactly E = {0} (v50 notation).

**Remark (not claimed).** The exact mean-square results of v43/v44/v51 and Lemma K of v52 involve the second-moment coefficient of the spin-2 part. For β ≠ 0 this coefficient becomes complex, 1/(|α| + σ^2 − iβ) in place of b. Those results are NOT extended here.

**NOT delivered.**

- β ≠ 0 versions of v41, v43, v44, v51 and v52.
- Non-commuting planar drift; v38 shows switching effects there.
- Exact G1.
- Controlled data, a controller, synthesis, or an RMS-to-literal transfer. C1–C3 and R4 STOPPED.

## 1. Inputs and separation

**Adopted inputs** (read completely this session):

| Input | LF | Pin |
|---|---|---|
| v25 | 348 | `8c381b1f…` |
| v26 | 308 | `6666f555…` |
| v21/v25/v26 parent | 74 | `1f00e0c6…` |
| v220 parent | 79 | `13fbb1a2…` |

**Parent-supported conclusions.** v31/v32 S at any preview h (= δ); v27 C1.

**Author candidates** (UNREVIEWED):

| Packet | Pin | Used for |
|---|---|---|
| v34 | `6fcca986…` | Lemma DS, T_ℓ, Theorem R |
| v39 | `4f1903b3…`, errata `1dbf820a…`, `6569cb34…` | identity method |
| v46 | `9f0d530f…` | Theorem RGP |
| v48 | `184fd301…` | Lemma D method |
| v49 | `9092585d…` | co-rotation |
| v50 | `173796d0…` | Theorem EI |

**Separation.** Only a path reparametrization, co-rotating inputs at δ = 0, and conditioning on F_{s−δ} are used. No storage, Riccati/LMI, Gramian certificate, controller, selected control, changed output, quarantined guidance or RMS source.

## 2. Proof of Theorem B1

**The kernel.** For every continuous path ℓ with ℓ(0) = 0, v34 Lemma DS (commuting form) gives

`k_ℓ(t,s) = D0 e^{A0(ℓ(t)−ℓ(s))} e^{Ā(t−s)} C = e^{α(t−s)} D0 R(σ(ℓ(t)−ℓ(s)) + β(t−s)) C`.

**Reparametrization.** Put ℓ̃(t) := ℓ(t) + βt/σ. This is continuous with ℓ̃(0) = 0, and k_ℓ is exactly the class-PR kernel (β = 0, μ = α) at the path ℓ̃. The map ℓ ↦ ℓ̃ is a bijection of C_0([0,T]) onto itself, with inverse ℓ̃ ↦ ℓ̃ − β·/σ. So the families {T_ℓ} for (α, β) and (α, 0) coincide, hence so do their suprema.

**Conclusion.** v46 RGP gives the formula. The certificate follows from v34 item 1 and v27 C1. δ-independence is as in erratum `6569cb34…`. ∎

## 3. Proof of Theorem B2

**G_rob.** By B1, G_rob = a max_u |C^T u||D0 u| = a√(mκ).

**Equality at δ = 0.**

- Use the adapted input w(s) := κ^{−1/2} C^T R(σW_s + βs) u f(s), with unit u and deterministic f ∈ L2. Then |w| = |f| and Cw = κ^{1/2} R(σW_s + βs) u f(s).
- Rotations commute, so X_t = κ^{1/2} R(σW_t + βt) u (T_α f)(t), where T_α is convolution with e^{αu}.
- Hence |z_t| = √(mκ)|T_α f(t)| pathwise, and the supremum over f gives G2(0) ≥ a√(mκ).
- With G2 ≤ G1 ≤ G_rob, all three are equal.

**Strictness for δ > 0.**

1. **Identity.** The v39 identity with M = I is rotation-invariant: R^T R = I removes β from the conditional energy factor. So for every adapted plant input w̃,

   E∫|X|^2 = a E∫ <C w̃(s), X_s> ds,

   by the same Fubini/conditioning computation as v39 §2 with μ replaced by α. Hence E∫|z|^2 = m a E∫<C w̃, X>.
2. **Conditioning.** Condition on F_{s−δ}, as in v48 Lemma D:

   E[X_s | F_{s−δ}] = e^{−σ^2δ/2} e^{αδ} R(βδ) X_{s−δ} + ∫_{s−δ}^s e^{(α − σ^2/2)(s−s')} R(β(s−s')) C w̃(s') ds',

   because E R(σg) = e^{−σ^2 Var(g)/2} I.
3. **Norms.** The norms are bounded by e^{−qδ}||X|| and ((1−e^{−qδ})/q)||C w̃||, respectively.
4. **Conclusion.** The v48 DI computation gives E∫|z|^2 ≤ mκa^2 θ(δ)||w||^2, with θ(δ) < 1 since 1/q < a. Then v34 Theorem R. ∎

## 4. Meaning (value side only)

For every planar rotation-noise plant whose drift commutes with the noise, a deterministic co-rotation β is invisible to the worst case over noise realizations. The closed-form robust certificate and the "equality only at zero preview" phenomenon for isotropic channels therefore cover the whole commuting planar class.

No controller or synthesis statement is made.

## 5. Process and assurance

- Written exact mathematics only, after v209, v236 and v240 (with addendum `6affc672…`) were read. The adopted inputs and the v220 parent were read completely.
- Frozen v27–v32 untouched.
- No pinned/frozen/shared edit. No Git, deletion, publication or external model.
- All permanent findings and ZERO quarantines remain: post56, post60, postS126, the self-released v163 assessment, and the protected S242 window. HELD_C889 was never opened.
- No formal, kernel, human, configured-family, executable or novelty acceptance.
- Same18, HOLD v2, science cutoff 2026-10-27T11:05:38-07:00 and delivery deadline 12:35:38 apply. This is not round closeout.

**END OF COMPLETE v53.**
