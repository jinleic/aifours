# Every nontrivial planar rotation-noise plant is STRICT at all sufficiently long previews: G2^det < G_rob

Owner **InfoHinfPreview-2 / info-3**. Clock observed with `/bin/date` immediately before writing: **Tue Oct 27 08:36:20 PDT 2026**.

**Status.**

- NEW COMPLETE WRITTEN OWNER-CANDIDATE, written as a separate successor. Author-written and unreviewed; not adopted; no gate.
- Value side only, under v209 (`1ec52034…`) and v236 (`062ccf9e…`).
- All-variable, source-fixed conventional proofs. No machine-checked identity.
- No chosen numeric probe.
- No scientific interpreter, Eval, calculator, CAS, program, enumeration, solver or replay. No new GO.
- Frozen v27–v32 untouched; v31/v32 are used through their v220-supported conclusions, with Q-rho, Q-zero and Q1 carried additively (`6d0103ff…`).

## 0. Statement

**Class PR.** Planar rotation noise as in v39:

- A0 = σJ with σ ≠ 0;
- Ā = μI with μ < 0;
- ANY C ∈ R^{2×p} and D0 ∈ R^{q×2}, both nonzero;
- canonical one-Brownian filtration.

Put a := 1/|μ|, b := 1/(|μ|+σ^2), r := b/a ∈ (0,1) and q := |μ| + σ^2/2, so 1/q = a·2r/(1+r).

**Theorem PLS.** For every plant in class PR:

1. G2^det = ((1/q) max_{|v|=1} (Cv)^T 2Ξ(M) (Cv))^{1/2}, exactly, where Ξ is v39's matrix and M := D0^T D0.
2. G2^det < G_rob = a · max_{|u|=1} |C^T u||D0 u| (v46).
3. Consequently, by v50 Theorem EI, the equality set E = {δ ≥ 0 : G1(δ) = G2(δ)} is NOT all of [0, ∞). There is δ* < ∞ such that

   `G2(δ) < G1(δ) ≤ √2·G2(δ)` for every δ ≥ δ*.

   So for every nontrivial planar rotation-noise plant, the mean-square replacement is strictly optimistic at all sufficiently long previews.

**Key inequality (Lemma K).** For every r ∈ (0,1), every angle ψ_0 and all m_1 ≥ m_2 ≥ 0 with m_1 > 0, put w̄ := (m_1+m_2)/2 and Δ := (m_1−m_2)/2. Then

`(2r/(1+r)) (w̄ + rΔ cos 2ψ_0) < Λ(ψ_0) := max_{k∈[0,1]} k (m_2 + (m_1−m_2)(√k|cos ψ_0| + √(1−k)|sin ψ_0|)^2)`.

**Consistency.**

- At δ = 0 equality can occur: bi-isotropic data (v39 item 6) and the v44 locus. So E ∈ {∅, {0}, [0, δ_0), [0, δ_0]} for planar data.
- v48 shows E ⊆ {0} for the bi-isotropic and PR-1E classes.
- v51 gives the exact G2^det in those classes, consistent with item 1.

**NOT delivered.**

- An explicit δ*.
- Whether E ⊆ {0} for all planar data.
- n ≥ 3.
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

**Author candidates** (unreviewed):

| Packet | Pin | Used for |
|---|---|---|
| v39 | `4f1903b3…`, errata `1dbf820a…`, `6569cb34…` | identity |
| v43 | `b4e13943…` | Lemma Γ |
| v45 | `d7c9814c…` | single-input G_rob = c a √Λ |
| v46 | `9f0d530f…` | G_rob formula |
| v50 | `173796d0…` | Theorem EI |
| v51 | `a4364749…` | for comparison |

**Separation.** Deterministic-input moment kernels, a reduction to a single input direction, and elementary inequalities are used. No storage, Riccati/LMI, Gramian certificate, controller, selected control, changed output, quarantined guidance or RMS source.

## 2. Proof of item 1

For a deterministic plant input v (vector valued), the v39 identity and E R(σ(W_s − W_{s'})) = e^{−σ^2(s−s')/2} I give

E∫|z|^2 = ∫∫ v(s)^T C^T Ξ(M) C v(s') e^{−q|s−s'|} ds ds',

after symmetrization; C^T Ξ C is symmetric. The kernel is a matrix times the positive-definite scalar kernel e^{−q|u|}, whose Fourier maximum is 2/q at ω = 0, approached by long constant inputs. Hence G2^det^2 = (2/q) λ_max(C^T Ξ(M) C). ∎

## 3. Proof of Lemma K

**Positivity.** Ξ(M) = (a/2) w̄ I + (b/2) M_0 has eigenvalues (a w̄ ± bΔ)/2 > 0, because a > b and w̄ ≥ Δ.

**Lower bound for Λ.** Dropping 2CS√(k(1−k)) ≥ 0 from h(k), with C = |cos ψ_0| and S = |sin ψ_0|, gives

W(k) ≥ A' + B'k, where A' := w̄ − Δc_2, B' := 2Δc_2 and c_2 := cos 2ψ_0.

Also W(1) = w_0 := w̄ + Δc_2 = A' + B'. Write L := (2r/(1+r))(w̄ + rΔc_2) for the left side.

**Case Δc_2 ≥ 0 (this includes Δ = 0).** Then w_0 ≥ w̄ > 0, and L ≤ (2r/(1+r)) w_0 < w_0 = 1·W(1) ≤ Λ, because 2r/(1+r) < 1.

**Case Δc_2 < 0, i.e. Δ > 0 and c_2 < 0.** Put d := Δ|c_2| > 0. Then A' = w̄ + d, B' = −2d, w_0 = w̄ − d, and t := w̄/d ≥ 1, since w̄ ≥ Δ ≥ d.

- **Sub-case t > 3.** Λ ≥ w_0 = w̄ − d. Then L − (w̄ − d) = (1−r)(d(1+2r) − w̄)/(1+r) < 0, because w̄ > 3d ≥ (1+2r)d.
- **Sub-case 1 ≤ t ≤ 3.** The maximizer of k(A' − 2dk) is k = (w̄+d)/(4d) ∈ [1/2, 1], so Λ ≥ (w̄+d)^2/(8d). Dividing by d, it suffices that g(r) := 2r(t − r)/(1+r) < (t+1)^2/8 for r ∈ (0,1).
  - g'(r) has the sign of t − 2r − r^2, so g increases up to r* := √(1+t) − 1 ∈ [√2 − 1, 1] and then decreases. There g(r*) = 2r*^2.
  - With s := √(1+t) ∈ [√2, 2], the claim 2(s−1)^2 < s^4/8 is equivalent to 4(s−1) < s^2, i.e. (s−2)^2 > 0. This holds for s < 2.
  - If s = 2, i.e. t = 3, then r* = 1, so g is increasing on (0,1) and g(r) < g(1) = 2 = (t+1)^2/8. ∎

## 4. Proof of item 2

**Single-direction reduction.** Let v* attain λ_max in item 1 and x := C v*. Then x ≠ 0, because C ≠ 0 and Ξ(M) ≻ 0. Put x̂ := x/|x| and let ψ_0 be the angle from x̂ to the top eigenvector of M.

**Comparison plant.** Consider the planar plant with the single input column x and the same D0.

- Its deterministic-input value equals G2^det^2 of the original plant: (1/q) x^T 2Ξ(M) x, since one input direction realizes the maximum.
- By v43 Lemma Γ, the input-direction coefficient is e_1^T 2Ξ(M) e_1 = Re Γ_M = a(w̄ + rΔ cos 2ψ_0) in x̂-coordinates.
- Hence G2^det^2 = |x|^2 a^2 (2r/(1+r))(w̄ + rΔ cos 2ψ_0).

**Robust side.** The comparison plant has G_rob,x^2 = |x|^2 a^2 Λ(ψ_0) (v45 with input direction x̂). Its inputs x·(scalar) = C(v*·scalar) form a subset of the original plant's inputs, so G_rob,x ≤ G_rob.

**Conclusion.** Lemma K gives G2^det < G_rob,x ≤ G_rob.

**Item 3.** v50 Theorem EI: E = [0, ∞) iff G2^det = G_rob. Otherwise strictness holds for all δ ≥ δ*, with 2ε(δ*) < G_rob − G2^det from v50 Theorem LD. ∎

## 5. Meaning (value side only)

For every planar rotation-noise channel with isotropic corrected drift, a long enough preview makes the printed E path-L2 level strictly exceed the mean-square level. Equality is possible only at short previews: δ = 0 in the classes decided so far.

No controller or synthesis statement is made.

## 6. Process and assurance

- Written exact mathematics only, after v209 and v236 were read FIRST and the adopted inputs and the v220 parent were read completely.
- Frozen v27–v32 untouched.
- No pinned/frozen/shared edit. No Git, deletion, publication or external model.
- All permanent findings and ZERO quarantines remain: post56, post60, postS126, the self-released v163 assessment, and the protected S242 window. HELD_C889 was never opened.
- No formal, kernel, human, configured-family, executable or novelty acceptance.
- Same18, HOLD v2, science cutoff 2026-10-27T11:05:38-07:00 and delivery deadline 12:35:38 apply. This is not round closeout.

**END OF COMPLETE v52.**
