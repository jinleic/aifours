# Preview delay breaks every rotation-noise equality: for δ > 0 the bi-isotropic class and the whole eigen-aligned planar class are STRICT

Owner **InfoHinfPreview-2 / info-3**. Clock observed with `/bin/date` immediately before writing: **Tue Oct 27 08:20:37 PDT 2026**.

**Status.**

- NEW COMPLETE WRITTEN OWNER-CANDIDATE, written as a separate successor. Author-written and unreviewed; not adopted; no gate.
- Value side only, under v209 (`1ec52034…`).
- All-variable, source-fixed conventional proofs. No machine-checked identity.
- No chosen numeric probe.
- No scientific interpreter, Eval, calculator, CAS, program, enumeration, solver or replay. No new GO.
- Frozen v27–v32 untouched. No v220 file, live review or assignment read.
- Written after, and consistent with, the preview-delay erratum `6569cb34…`.

## 0. Setting and statements

**Class RS (v40).** Uncontrolled constant data with:

- A0 real skew-symmetric;
- Ā = μI with μ < 0;
- input map C and output map D0;
- preview delay δ ≥ 0: the plant receives w(t − δ);
- canonical one-Brownian filtration.

Write G2(δ) and G1(δ) for the gains at delay δ. G_rob does not depend on δ (erratum `6569cb34…`). Put a := 1/|μ|, let ω_min ≥ 0 be the smallest modulus of an eigenvalue of A0, and put

`q := |μ| + ω_min^2/2` and `θ(δ) := e^{−qδ} + (1 − e^{−qδ})/(q a)`.

**Lemma D (delayed conditioning).** For every adapted input, with Y_s := E[X_s | F_{s−δ}] and δ ≤ s,

`Y_s = e^{A0^2 δ/2} e^{μδ} X_{s−δ} + ∫_{s−δ}^{s} e^{(μI + A0^2/2)(s−s')} C w(s'−δ) ds'`.

The plant inputs up to time s are F_{s−δ}-measurable.

**Theorem DI (delay breaks bi-isotropic equality).** Let M := D0^T D0 = mI and CC^T = κI with m, κ > 0, and let A0 be invertible (ω_min > 0). For every δ > 0,

`G2(δ)^2 ≤ m κ a^2 θ(δ) < m κ a^2 = G_rob^2`.

Hence G2(δ) < G1(δ): STRICT. At δ = 0 the gains are EQUAL (v39 item 6 / v40 item 6, as restricted by the erratum).

**Theorem DE (delay breaks the planar equality locus).** In the planar eigen-aligned single-input class PR-1E of v43/v44, with A0 = σJ, σ ≠ 0, ω_min = σ and q = |μ| + σ^2/2, for every δ > 0,

`G2(δ)^2 ≤ c^2 γ_M (c_* e^{−qδ} + (1 − e^{−qδ})/q) < c^2 γ_M c_* = G2(0)^2 ≤ G_rob^2`.

Here γ_M = c_* x + ((a−b)/2) y. Hence EVERY plant in PR-1E is STRICT at every δ > 0, including the v44 locus where G1(0) = G2(0). Moreover G2(δ) < G2(0) for every δ > 0 in this class: the delay strictly lowers the mean-square level.

**Interpretation.** With preview delay, the adversary must commit its plant input δ in advance, while the noise rotation over that window is unknown. So adapted co-rotation and instantaneous phase feedback lose a definite factor. The deterministic worst case G_rob is unchanged.

**NOT delivered.**

- Exact G2(δ) for δ > 0.
- Non-invertible A0 in Theorem DI. A zero-frequency part is noise-invisible and may keep equality.
- Classes beyond those named.
- Controlled data, a controller, synthesis, or an RMS-to-literal transfer. C1–C3 and R4 STOPPED.

## 1. Inputs and separation

**Adopted inputs** (read completely this session):

| Input | LF | Pin |
|---|---|---|
| v25 | 348 | `8c381b1f…` |
| v26 | 308 | `6666f555…` |
| parent | 74 | `1f00e0c6…` |

**Cited author packets** (unreviewed):

| Packet | Pin | Used for |
|---|---|---|
| v31 | `4c2a7b9b…` | G2 ≤ G1 |
| v34 | `6fcca986…` | Lemma DS, G_rob, Theorem R |
| v39 | `4f1903b3…` with errata `1dbf820a…`, `6569cb34…` | identity item 1 |
| v40 | `fd6a77b9…` | class, Ξ(I) = I/(2|μ|) |
| v41 | `913fd056…` | Gmax ≤ c c_*, valid for every adapted plant input |
| v43 | `b4e13943…` | Lemma Γ, the δ = 0 value |
| v44/v46 | `796c420a…` / `9f0d530f…` | G_rob |

**Separation.** No storage function, dissipation inequality, Riccati/LMI, Gramian certificate, controller, selected control, changed output, quarantined guidance or RMS source is used. The only tools are conditional expectation given F_{s−δ}, the Gaussian matrix moment E e^{A0 g} = e^{A0^2 Var(g)/2}, Young and Cauchy–Schwarz.

## 2. Proof of Lemma D

The plant input at time s' is w(s'−δ), which is F_{s'−δ} ⊆ F_{s−δ}-measurable for s' ≤ s. By v34 Lemma DS (commuting form),

X_s = ∫_0^s e^{μ(s−s')} e^{A0(W_s − W_{s'})} C w(s'−δ) ds'.

**Old inputs (s' ≤ s − δ).** Write e^{A0(W_s−W_{s'})} = e^{A0(W_s − W_{s−δ})} e^{A0(W_{s−δ} − W_{s'})}. The first factor is independent of F_{s−δ}, with mean e^{A0^2δ/2}, because A0 commutes with itself and g ~ N(0, δ). Collecting these terms gives e^{A0^2 δ/2} e^{μδ} X_{s−δ}.

**Recent inputs (s − δ < s' ≤ s).** The increment W_s − W_{s'} is independent of F_{s−δ}, with mean factor e^{A0^2(s−s')/2}. ∎

## 3. Proofs of the theorems

**Common bound.** Skewness gives A0^2 = −A0^T A0 ⪯ −ω_min^2 I, so ||e^{A0^2 u/2}|| ≤ e^{−ω_min^2 u/2}. Hence, in L2(dP ds),

`||Y|| ≤ e^{−qδ} ||X|| + ((1 − e^{−qδ})/q) ||C w(·−δ)||`.

**Theorem DI.**

- By v40 item 1 with Ξ(I) = I/(2|μ|) and M = mI,

  E∫|z|^2 = m E∫|X|^2 = m a E∫ <C w(s−δ), X_s> ds = m a E∫ <C w(s−δ), Y_s> ds,

  by conditioning on F_{s−δ}.
- Since ||X|| ≤ a ||Cw||, Cauchy–Schwarz gives E∫|z|^2 ≤ m a ||Cw|| (e^{−qδ} a + (1 − e^{−qδ})/q) ||Cw|| = m a^2 θ(δ) ||Cw||^2 ≤ m κ a^2 θ(δ) ||w||^2.
- θ(δ) < 1 for δ > 0, because 1/q < a, which follows from ω_min > 0.
- G_rob = a√(mκ) in every dimension. The path ℓ ≡ 0 gives G_rob ≥ ||D0C||/|μ| = a√m ||C|| = a√(mκ), because D0^T D0 = mI. v46 RGN gives G_rob ≤ a·inf_β (m + βκ)/(2√β) = a√(mκ). Only the lower bound is needed: G2(δ) < a√(mκ) ≤ G_rob, and v34 Theorem R gives strictness. ∎

**Theorem DE.**

- By v43 Lemma Γ, E∫X^T M X = c γ_M E∫ w(s−δ) y_1(s) ds, with y_1 := Re X.
- Conditioning on F_{s−δ}, this equals c γ_M E∫ w(s−δ) e_1^T Y_s ds.
- By Lemma D, e_1^T Y_s = e^{−qδ} y_1(s−δ) + c ∫_{s−δ}^s e^{−q(s−s')} w(s'−δ) ds'. Here A0^2 = −σ^2 I, so e^{A0^2 u/2} = e^{−σ^2u/2} I.
- v41 gives ||y_1|| ≤ c c_* ||w|| for every adapted plant input, and Young bounds the second term by c((1 − e^{−qδ})/q)||w||.
- Hence G2(δ)^2 ≤ c^2 γ_M (c_* e^{−qδ} + (1−e^{−qδ})/q).
- Strict convexity of 1/x gives c_* = (1/|μ| + 1/(|μ|+σ^2))/2 > 1/(|μ| + σ^2/2) = 1/q. So for δ > 0 the bracket is < c_*.
- G2(0)^2 = c^2 γ_M c_* (v43 at δ = 0) and G2(0) ≤ G_rob (v44). v34 Theorem R gives strictness. ∎

## 4. Meaning (value side only)

**Two kinds of equality.**

- Equality between the printed literal level and the mean-square level in rotation-noise plants is a ZERO-DELAY phenomenon. Every such equality found here (bi-isotropic co-rotation; the v44 locus) breaks for any δ > 0.
- Equality from noise invisibility (v33/v36 deterministic kernels) is delay-independent.

**Synthesis.** No controller or synthesis statement is made.

## 5. Process and assurance

- Written exact mathematics only, after v209 was read FIRST and the adopted inputs were read completely.
- Frozen v27–v32 untouched. No v220 file, review or assignment was opened.
- No pinned/frozen/shared edit. No Git, deletion, publication or external model.
- All permanent findings and ZERO quarantines remain: post56, post60, postS126, the self-released v163 assessment, and the protected S242 window. HELD_C889 was never opened.
- No formal, kernel, human, configured-family, executable or novelty acceptance.
- Same18, HOLD v2, science cutoff 2026-10-27T11:05:38-07:00 and delivery deadline 12:35:38 apply. This is not an early final park.

**END OF COMPLETE v48.**
