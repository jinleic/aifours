# Gate-I preview profile: an interpolating upper bound exact at both ends; and the delay-independent dichotomy for commuting real-spectrum noise

Owner **InfoHinfPreview-2 / info-3**. Clock observed with `/bin/date` immediately before writing: **Tue Oct 27 08:46:13 PDT 2026**.

**Pre-pin note.** This text replaces an earlier draft of this same file before its first hash. That draft also asserted that the bound x̂(h) below is non-increasing in h, and contained an incomplete attempted proof of it. That claim is NOT made here. This is disclosed in the next checkpoint.

**Status.**

- NEW COMPLETE WRITTEN OWNER-CANDIDATE, written as a separate successor. Author-written, UNREVIEWED and not adopted. Main's v240 decision applies.
- Value side only, under v209 (`1ec52034…`) and v236 (`062ccf9e…`).
- All-variable, source-fixed conventional proofs. No machine-checked identity.
- No chosen numeric probe: all parameters stay symbolic.
- No scientific interpreter, Eval, calculator, CAS, program, enumeration, solver or replay. No new GO.
- Frozen v27–v32 untouched. The gate-I value identification stays CONDITIONAL at NR-GATE-I-WHOLE-V21 in the adopted record. v55 (`c51562e8…`) is an UNREVIEWED independent proof of it.

## 0. Statements

**Theorem GB (gate-I preview profile).** Take the gate-I family of v54/v55:

- dX = (−aX + c w(t−h)) dt + σX dW and z = dX;
- a, c, d, σ > 0 with q_0 = 2a − σ^2 > 0.

For every h ≥ 0,

`c d (2/(a q_0))^{1/2} ≤ G2(h) ≤ d x̂(h)`,

where x̂(h) is the positive root of

`x^2 − (2c/q_0) e^{−ah} x − (2c/q_0) c (1 − e^{−ah})/a = 0`.

The bound is exact at both ends:

- x̂(0) = 2c/q_0, so the upper bound equals the v55 value 2cd/q_0 at h = 0;
- x̂(h) → c(2/(a q_0))^{1/2} as h → ∞, which is the exact limit of v54.

Monotonicity of x̂ in h is NOT claimed. G2 itself is non-increasing by v50 PM.

**Theorem RD (commuting real spectrum: delay-independent dichotomy).** Take uncontrolled EMS constant data with AA0 = A0A and spec A0 ⊂ R (v36 Corollary V1 class). For the equality set E of v50:

- E = ∅ if VIS holds;
- E = [0, ∞) if VIS fails.

Equality never depends on the preview in this class.

**NOT delivered.**

- Exact G2(h) for 0 < h < ∞.
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

**Parent-supported conclusions.** v31, v32 S at any h; v27 C1.

**Author candidates** (UNREVIEWED):

| Packet | Pin | Used for |
|---|---|---|
| v34 | `6fcca986…` | Theorem R |
| v36 | `4ecfa7c6…` | V1, (a), (b) |
| v50 | `173796d0…` | PM; E notation |
| v54 | `2b9bbee2…` | lower bound and limit |
| v55 | `c51562e8…` | identity, h = 0 value |

**Separation.** The tools are conditioning on F_{s−h}, the v55 identity, Cauchy–Schwarz, Young and a quadratic inequality. No storage, Riccati/LMI, Gramian certificate, controller, selected control, changed output, quarantined guidance or RMS source.

## 2. Proof of Theorem GB

**Lower bound.** This is v54 item 2.

**Upper bound.** Let w̃ be the plant input. It is F_{s−h}-adapted at time s.

1. **Identity.** The v55 identity gives E∫X^2 = (2c/q_0) E∫ w̃(s) X_s ds.
2. **Conditioning.** Condition on F_{s−h}, using E Φ(s, s−h) = e^{−ah} and independence:

   E[X_s | F_{s−h}] = e^{−ah} X_{s−h} + c ∫_{s−h}^s e^{−a(s−s')} w̃(s') ds'.

3. **Bound.** By Cauchy–Schwarz and Young,

   E∫X^2 ≤ (2c/q_0)(e^{−ah} ||w|| ||X|| + c((1 − e^{−ah})/a) ||w||^2).

   With x := ||X||/||w||, this reads x^2 − (2c/q_0)e^{−ah} x − (2c/q_0)c(1 − e^{−ah})/a ≤ 0. Hence x ≤ x̂(h), and G2(h) ≤ d x̂(h) because z = dX.
4. **Endpoints.**
   - At h = 0 the constant term vanishes and x̂(0) = 2c/q_0.
   - As h → ∞ the linear coefficient tends to 0 and the constant term tends to 2c^2/(a q_0), so x̂ → c(2/(a q_0))^{1/2}. ∎

## 3. Proof of Theorem RD

- **VIS holds.** v36 (a) gives G_rob = ∞, independently of δ (erratum `6569cb34…`). With G2(δ) ≤ G2(0) < ∞ (v31, v50 PM), v34 Theorem R gives strictness at every δ, so E = ∅.
- **VIS fails.** Since spec A0 ⊂ R, J_im = ∅. v36 (b) gives a deterministic pathwise kernel K_0, so T_C w = K_0 ⋆ w(·−δ) for every input.
  - Pathwise, ||T_C w|| ≤ ||T_{K_0}|| ||w||, so G1(δ) ≤ ||T_{K_0}||.
  - Deterministic inputs give G2(δ) ≥ ||T_{K_0}||.
  - With G2 ≤ G1, G1(δ) = G2(δ) for every δ, and E = [0, ∞). ∎

## 4. Meaning (value side only)

- **Gate I.** The mean-square level along preview is pinned between explicit unconditional curves. These are exact at h = 0 (given v55) and at h = ∞. The literal level stays strictly above it throughout (v54).
- **Commuting real-spectrum noise.** Preview never changes whether the two criteria coincide.
- **Synthesis.** No controller or synthesis statement is made.

## 5. Process and assurance

- Written exact mathematics only, after v209, v236 and v240 were read and the adopted inputs and the v220 parent were read completely.
- Frozen v27–v32 untouched.
- No pinned/frozen/shared edit. No Git, deletion, publication or external model.
- All permanent findings and ZERO quarantines remain: post56, post60, postS126, the self-released v163 assessment, and the protected S242 window. HELD_C889 was never opened.
- No formal, kernel, human, configured-family, executable or novelty acceptance.
- Same18, HOLD v2, science cutoff 2026-10-27T11:05:38-07:00 and delivery deadline 12:35:38 apply. This is not round closeout.

**END OF COMPLETE v56.**
