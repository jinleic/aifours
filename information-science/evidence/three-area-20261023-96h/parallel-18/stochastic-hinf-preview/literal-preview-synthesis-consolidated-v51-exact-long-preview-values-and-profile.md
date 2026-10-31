# Exact long-preview mean-square values and a self-consistent preview profile for rotation-noise plants

Owner **InfoHinfPreview-2 / info-3**. Clock observed with `/bin/date` immediately before writing: **Tue Oct 27 08:32:52 PDT 2026**.

**Status.**

- NEW COMPLETE WRITTEN OWNER-CANDIDATE, written as a separate successor. Author-written and unreviewed; not adopted; no gate.
- Value side only, under v209 (`1ec52034…`) and v236 (`062ccf9e…`).
- All-variable, source-fixed conventional proofs. No machine-checked identity.
- No chosen numeric probe.
- No scientific interpreter, Eval, calculator, CAS, program, enumeration, solver or replay. No new GO.
- Frozen v27–v32 untouched; v31/v32 are used through their v220-supported conclusions, with Q-rho, Q-zero and Q1 carried additively (`6d0103ff…`).

## 0. Statements

The notation of v43/v48/v50 is used:

- a = 1/|μ|, b = 1/(|μ|+σ^2), c_* = (a+b)/2 and q = |μ| + σ^2/2;
- G2^det is the deterministic-input mean-square gain (v50);
- δ is the preview delay.

**Theorem L1 (planar eigen-aligned class PR-1E).** For a single input c e_1 with c > 0 and M = diag(x, y), put γ_M := c_* x + ((a−b)/2) y. Then:

1. G2^det = c (γ_M/q)^{1/2}, exactly.
2. lim_{δ→∞} G2(δ) = c (γ_M/q)^{1/2}, exactly (v50 Theorem LD).
3. **Preview profile.** For every δ ≥ 0,

   `c^2 γ_M/q ≤ G2(δ)^2 ≤ c γ_M ( e^{−qδ} ĝ(δ) + c(1 − e^{−qδ})/q )`,

   where ĝ(δ) := (c c_* e^{−qδ} + (c^2 c_*^2 e^{−2qδ} + 4c^2 c_*(1 − e^{−qδ})/q)^{1/2})/2. The upper bound equals G2(0)^2 = c^2 γ_M c_* at δ = 0 (v43, δ = 0), tends to the exact limit as δ → ∞, and improves v48 Theorem DE for every δ > 0.
4. **Long-preview gap.** G_rob^2 − lim_{δ→∞} G2(δ)^2 = c^2(a^2 Φ(x,y) − γ_M/q) > 0, with Φ from v44 Theorem RG. So the strict gap persists at long preview with an explicit squared size.

**Theorem L2 (bi-isotropic, invertible skew noise).** Let class BI hold (v49) with A0 invertible and ω_min the smallest |eigenvalue| of A0. Put q' := |μ| + ω_min^2/2. Then:

- G2^det = (mκa/q')^{1/2}, exactly;
- lim_{δ→∞} G2(δ) = G2^det;
- G_rob^2 − lim G2^2 = mκa(a − 1/q') > 0.

For n = 2, q' = q.

**NOT delivered.**

- Exact G2(δ) for 0 < δ < ∞.
- Exact G1(δ).
- Controlled data, a controller, synthesis, or an RMS-to-literal transfer. C1–C3 and R4 STOPPED.

## 1. Inputs and separation

**Adopted inputs** (read completely this session):

| Input | LF | Pin |
|---|---|---|
| v25 | 348 | `8c381b1f…` |
| v26 | 308 | `6666f555…` |
| v21/v25/v26 parent | 74 | `1f00e0c6…` |
| v220 parent | 79 | `13fbb1a2…` |

**Author candidates** (unreviewed):

| Packet | Pin | Used for |
|---|---|---|
| v39 | `4f1903b3…`, with errata | identity |
| v41 | `913fd056…` | Gmax |
| v43 | `b4e13943…` | Lemma Γ; δ = 0 value |
| v44 | `796c420a…` | Φ, G_rob |
| v48 | `184fd301…` | Lemma D |
| v49 | `9092585d…` | class BI |
| v50 | `173796d0…` | Theorem LD |

**Separation.** Deterministic-input moment kernels, conditioning on F_{s−δ}, Cauchy–Schwarz and the triangle inequality are used. No storage, Riccati/LMI, Gramian certificate, controller, selected control, changed output, quarantined guidance or RMS source.

## 2. Proof of Theorem L1

**Item 1.**

- For a deterministic plant input v, Lemma Γ gives E∫X^T M X = c γ_M ∫ v(s) E[y_1(s)] ds.
- E[y_1(s)] = c ∫_0^s e^{−q(s−s')} v(s') ds', because E R(σ(W_s − W_{s'})) = e^{−σ^2(s−s')/2} I.
- Hence E∫X^T M X = (c^2 γ_M/2) ∫∫ v(s) v(s') e^{−q|s−s'|} ds ds'.
- The kernel e^{−q|u|} has Fourier transform 2q/(q^2 + ω^2), with maximum 2/q at ω = 0, attained in the limit by long constant inputs. So the supremum ratio is c^2 γ_M/q.

**Item 2.** This is v50 Theorem LD together with Item 1.

**Item 3.** The lower bound is v50 (G2^det ≤ G2(δ)). For the upper bound, let g(δ) be the RMS gain at delay δ for the aligned functional y_1 (M = e_1 e_1^T, γ = c_*).

- By Lemma Γ and conditioning on F_{s−δ}, as in v48 §3, E∫X^T M X = c γ_M E∫ w̃ Ŷ_1, with Ŷ_1(s) := E[y_1(s) | F_{s−δ}] = e^{−qδ} y_1(s−δ) + c ∫_{s−δ}^s e^{−q(s−s')} w̃(s') ds'.
- Cauchy–Schwarz, the triangle inequality, ||y_1|| ≤ g(δ)||w|| (the same delayed input) and Young give

  E∫X^T M X ≤ c γ_M ||w||^2 (e^{−qδ} g(δ) + c(1 − e^{−qδ})/q).

- With M = e_1e_1^T this reads g^2 ≤ c c_*(e^{−qδ} g + c(1−e^{−qδ})/q). Solving the quadratic inequality gives g ≤ ĝ(δ).
- Insert this into the general bound.
- **Endpoints.** At δ = 0, ĝ = c c_* and the bound is c^2 γ_M c_*. As δ → ∞, ĝ → c(c_*/q)^{1/2} and the bound → c^2 γ_M/q.
- **Improvement over v48 DE.** v48 used c c_* in place of g(δ), and ĝ(δ) < c c_* for δ > 0, since 1/q < c_*.

**Item 4.**

- γ_M/q < γ_M c_* because 1/q < c_*.
- c_* γ_M ≤ a^2 Φ, because G2(0) ≤ G_rob (v44).
- Hence a^2 Φ − γ_M/q > 0. ∎

## 3. Proof of Theorem L2

**The deterministic-input value.** For a deterministic plant input v:

- E∫|z|^2 = m E∫|X|^2 = m a ∫ <Cv(s), E X_s> ds (v40 item 1 with M = I);
- E X_s = ∫_0^s e^{(μI + A0^2/2)(s−s')} C v(s') ds', since E e^{A0 g} = e^{A0^2 Var(g)/2}.

Hence E∫|z|^2 = (m a/2) ∫∫ v(s)^T C^T e^{(μI + A0^2/2)|s−s'|} C v(s') ds ds'. Here μI + A0^2/2 is symmetric, so the symmetrized kernel is valid.

**Spectral bound.** Diagonalize A0^2 = −Σ_j ω_j^2 P_j with orthogonal real projectors P_j. The kernel's operator norm on L2 is

max_j (2/(|μ| + ω_j^2/2)) ||C^T P_j C|| = 2κ/q',

attained in the DC limit along the ω_min component. Here C^T P_j C has norm κ because CC^T = κI.

**Conclusion.** G2^det^2 = (m a/2)(2κ/q') = mκa/q'. The limit statement is v50 Theorem LD. The gap uses G_rob^2 = mκa^2 (v49) and 1/q' < a. ∎

## 4. Meaning (value side only)

**The preview profile.** For these rotation-noise plants the mean-square (L2-surrogate) level now has an exact value at zero preview (v43), an exact value at infinite preview, monotonicity in between (v50), and an explicit interpolating upper bound.

**The literal level.** The printed literal level stays strictly above it at every positive preview (v48), with an explicit long-preview squared gap.

**Synthesis.** No controller or synthesis statement is made.

## 5. Process and assurance

- Written exact mathematics only, after v209 and v236 were read FIRST and the adopted inputs and the v220 parent were read completely.
- Frozen v27–v32 untouched.
- No pinned/frozen/shared edit. No Git, deletion, publication or external model.
- All permanent findings and ZERO quarantines remain: post56, post60, postS126, the self-released v163 assessment, and the protected S242 window. HELD_C889 was never opened.
- No formal, kernel, human, configured-family, executable or novelty acceptance.
- Same18, HOLD v2, science cutoff 2026-10-27T11:05:38-07:00 and delivery deadline 12:35:38 apply. This is not round closeout.

**END OF COMPLETE v51.**
