# Bi-isotropic skew-noise plants: a complete equality/strictness dichotomy in the preview delay — equality iff δ = 0 or the noise matrix is singular

Owner **InfoHinfPreview-2 / info-3**. Clock observed with `/bin/date` immediately before writing: **Tue Oct 27 08:25:44 PDT 2026**.

**Status.**

- NEW COMPLETE WRITTEN OWNER-CANDIDATE, written as a separate successor. Author-written and unreviewed; not adopted; no gate.
- Value side only, under v209 (`1ec52034…`) and v236 (`062ccf9e…`).
- All-variable, source-fixed conventional proof. No machine-checked identity.
- No chosen numeric probe.
- No scientific interpreter, Eval, calculator, CAS, program, enumeration, solver or replay. No new GO.
- Frozen v27–v32 untouched. v32 is used only through its parent-supported conclusion, with Q-rho, Q-zero and Q1 carried additively (`6d0103ff…`).

## 0. Statement

**Class BI.** Class RS of v40 with both maps isotropic:

- any n;
- A0 real skew-symmetric;
- Ā = μI with μ < 0;
- C ∈ R^{n×p} with CC^T = κI, κ > 0;
- D0 ∈ R^{q×n} with D0^T D0 = mI, m > 0;
- preview delay δ ≥ 0;
- canonical one-Brownian filtration;
- EMS.

Put a := 1/|μ|.

**Theorem BI.** For every plant in class BI and every δ ≥ 0:

- G_rob = a√(mκ), independent of δ;
- G1(δ) = G2(δ) = G_rob IF AND ONLY IF δ = 0 or ker A0 ≠ {0}.

Otherwise, i.e. for δ > 0 and invertible A0, G2(δ)^2 ≤ mκ a^2 θ(δ) < G_rob^2 and G2(δ) < G1(δ) (v48 Theorem DI).

**Corollary BI1 (kernel determinism is not necessary, even with delay).** If A0 ≠ 0 is singular, the pathwise kernel e^{μ(t−s)} D0 e^{A0(ℓ(t)−ℓ(s))} C depends on ℓ, by the v40 item 6 argument. Yet equality holds at EVERY delay, because the worst case is attained along a noise-invisible direction u ∈ ker A0. So a delay-robust structural classification of AHEAD must use "worst case attainable in a noise-invisible way", not "kernel deterministic".

**NOT delivered.**

- A general δ > 0 classification beyond class BI and the planar class PR-1E (v48 DE).
- Exact G1 off the equality cases.
- Controlled data, a controller, synthesis, or an RMS-to-literal transfer. C1–C3 and R4 STOPPED.

## 1. Inputs and separation

**Adopted inputs** (read completely this session):

| Input | LF | Pin |
|---|---|---|
| v25 | 348 | `8c381b1f…` |
| v26 | 308 | `6666f555…` |
| v21/v25/v26 parent | 74 | `1f00e0c6…` |
| v220 parent | 79 | `13fbb1a2…` |

**Parent-supported conclusions** (v220, at canonical constant data, EMS):

- v31 (G2 < ∞, G2 ≤ G1);
- v27 C1 (√2).

**Author candidates** (unreviewed):

| Packet | Pin | Used for |
|---|---|---|
| v34 | `6fcca986…` | Lemma DS, Theorem R |
| v40 | `fd6a77b9…` | item 3, item 6 co-rotation at δ = 0 (erratum `6569cb34…`) |
| v46 | `9f0d530f…` | RGN |
| v48 | `184fd301…` | Theorem DI |

**Separation.** Only deterministic and co-rotating input constructions, the δ-independence of G_rob (erratum `6569cb34…`) and the cited bounds are used. No storage, Riccati/LMI, Gramian certificate, controller, selected control, changed output, quarantined guidance or RMS source.

## 2. Proof

**G_rob.**

- The path ℓ ≡ 0 gives G_rob ≥ ||D0C||/|μ| = a√m ||C|| = a√(mκ).
- v46 RGN gives G_rob ≤ a·inf_{β>0}(m + βκ)/(2√β) = a√(mκ).
- The value does not depend on δ, since sup over paths is shift-invariant (erratum `6569cb34…`).

**δ = 0.** v40 item 6 (co-rotation, valid at δ = 0) gives G2(0) ≥ a√(mκ). With G2 ≤ G1 ≤ G_rob, all three are equal.

**ker A0 ≠ {0}, any δ.**

- Take a real unit u with A0u = 0; a real skew matrix with a kernel has a real kernel vector.
- For deterministic f ∈ L2, use the deterministic input w(s) := κ^{−1/2} C^T u f(s). Then |w(s)| = |f(s)| because u^T CC^T u = κ, and Cw = κ^{1/2} u f.
- Since e^{A0θ}u = u for all θ, v34 Lemma DS gives X_t = κ^{1/2} u ∫_0^t e^{μ(t−s)} f(s−δ) ds pathwise.
- So |z_t| = √(mκ) |(T_μ f)(t−δ)|.
- The supremum over f gives G2(δ) ≥ a√(mκ) = G_rob, hence equality.

**δ > 0 and A0 invertible.** This is v48 Theorem DI, where ω_min > 0 because A0 is invertible. ∎

**Corollary BI1.** D0 e^{A0θ} C = √(mκ) U e^{A0θ} V, with U an isometry and V a co-isometry. Its θ-derivative at 0 is √(mκ) U A0 V, which vanishes only if A0 = U^T U A0 V V^T = 0. ∎

## 3. Meaning (value side only)

**Two sources of equality.** For isotropic channels, equality of the printed literal level and the mean-square level has exactly two sources:

- zero preview delay, through adapted co-rotation;
- a noise-invisible direction, which works at every delay.

With positive preview and fully rotating noise, the mean-square replacement is strictly optimistic. This structural picture refines the parent's open problem of classifying AHEAD.

**Synthesis.** No controller or synthesis statement is made.

## 4. Process and assurance

- Written exact mathematics only, after v209 and v236 were read FIRST and the adopted inputs and the v220 parent were read completely.
- Frozen v27–v32 untouched.
- No pinned/frozen/shared edit. No Git, deletion, publication or external model.
- All permanent findings and ZERO quarantines remain: post56, post60, postS126, the self-released v163 assessment, and the protected S242 window. HELD_C889 was never opened.
- No formal, kernel, human, configured-family, executable or novelty acceptance.
- Same18, HOLD v2, science cutoff 2026-10-27T11:05:38-07:00 and delivery deadline 12:35:38 apply. This is not round closeout.

**END OF COMPLETE v49.**
