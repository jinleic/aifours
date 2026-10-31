# Single-frequency skew noise in any dimension, single input and single output: reduction to the planar case, hence ALWAYS strict

Owner **InfoHinfPreview-2 / info-3**. Clock observed with `/bin/date` immediately before writing: **Tue Oct 27 07:59:08 PDT 2026**.

**Status.**

- NEW COMPLETE WRITTEN OWNER-CANDIDATE, written as a separate successor. Author-written and unreviewed; not adopted; no gate.
- Value side only, under v209 (`1ec52034…`).
- All-variable, source-fixed conventional proof. No machine-checked identity.
- No chosen numeric probe.
- No scientific interpreter, Eval, calculator, CAS, program, enumeration, solver or replay. No new GO.
- Frozen v27–v32 untouched. No v220 file, live review or assignment read.

## 0. Statement

**Class SF-SISO.** Uncontrolled constant data with:

- n even;
- A0 real skew-symmetric with A0^2 = −σ^2 I and σ ≠ 0, i.e. a single noise frequency;
- Ā := A − A0^2/2 = μI with μ < 0;
- a single input column c ≠ 0 (p = 1) and a single output row d^T (q = 1);
- any preview δ ≥ 0;
- canonical one-Brownian filtration.

The class is EMS, as in v40.

**Theorem SF.** Let V_c := span(c, A0c) and d' := P_{V_c} d, the orthogonal projection.

- If d' = 0, the output is identically 0, and G1 = G2 = 0.
- If d' ≠ 0, then G2,∞ < G1,∞ ≤ √2·G2,∞ at every preview: STRICT.

**Scope.** Only SISO and a single noise frequency are covered. Multi-input/multi-output data and skew noise with several distinct frequencies are NOT treated here. There the state need not stay in one invariant plane.

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
| v34 | `6fcca986…` | Lemma DS, and the fact that G1, G2 and G_rob depend only on the input–output path operators |
| v41 | `913fd056…` | Theorem SISO |

The v41 dependencies are v27, v31, v34 and v39 with erratum `1dbf820a…`.

**Separation.** None of the following is used: storage, Riccati/LMI, controller, selected control, changed output, quarantined guidance, RMS source.

## 2. Proof

**1. Invariant plane.**

- A0 is skew, so <c, A0c> = 0. A0 is invertible since A0^2 = −σ^2 I, so A0c ≠ 0.
- Hence V_c is 2-dimensional. It is A0-invariant because A0(A0c) = −σ^2 c.
- In the orthonormal basis (ĉ, A0ĉ/σ) of V_c, with ĉ := c/|c|, A0 acts as σJ: A0ĉ = σ(A0ĉ/σ) and A0(A0ĉ/σ) = −σĉ.

**2. The state stays in V_c.** By v34 Lemma DS with commuting data (Ā = μI commutes with A0),

`X_t = ∫_0^t e^{μ(t−s)} e^{A0(W_t−W_s)} c w(s−δ) ds`.

Every e^{A0θ}c lies in V_c, so X_t ∈ V_c for all t, pathwise. The same holds for every noise-path operator T_ℓ.

**3. Identical input–output maps.**

- For every path ℓ and every input, d^T X = d'^T X.
- So the original plant and the planar plant have the SAME input–output map, both pathwise and for every adapted input. The planar plant is (V_c, σJ, μI, input |c| e_1, output d'^T).
- Hence their G1, G2 and G_rob coincide.
- The planar plant is in v41's class PR-SISO, with c ↦ |c| > 0 real and g ↔ d' ≠ 0.

**4. Conclusion.**

- v41 Theorem SISO gives G2 < G_rob for the planar plant, hence for the original one.
- v34 Theorem R gives G2,∞ < G1,∞.
- If d' = 0, then d^T X ≡ 0. ∎

## 3. Meaning (value side only)

For any even dimension, a single-frequency rotation noise acting on an isotropically damped state cannot make the printed E path-L2 level equal the mean-square level for a scalar input–output channel. This holds unless the channel does not see the noise plane at all.

No controller or synthesis statement is made.

## 4. Process and assurance

- Written exact mathematics only, after v209 was read FIRST and the adopted inputs were read completely.
- Frozen v27–v32 untouched. No v220 file, review or assignment was opened.
- No pinned/frozen/shared edit. No Git, deletion, publication or external model.
- All permanent findings and ZERO quarantines remain: post56, post60, postS126, the self-released v163 assessment, and the protected S242 window. HELD_C889 was never opened.
- No formal, kernel, human, configured-family, executable or novelty acceptance.
- Same18, HOLD v2, science cutoff 2026-10-27T11:05:38-07:00 and delivery deadline 12:35:38 apply. This is not an early final park.

**END OF COMPLETE v42.**
