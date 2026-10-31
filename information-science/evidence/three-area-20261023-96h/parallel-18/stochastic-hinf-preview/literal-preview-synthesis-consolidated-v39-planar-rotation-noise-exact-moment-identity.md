# Planar rotation noise: an exact second-moment kernel identity decides the v34 rotational example (STRICT) and shows the rotation-like commuting class is genuinely mixed

Owner **InfoHinfPreview-2 / info-3**. Clock observed with `/bin/date` immediately before writing: **Tue Oct 27 07:44:16 PDT 2026**.

**Status.**

- NEW COMPLETE WRITTEN OWNER-CANDIDATE, written as a separate successor. Author-written and unreviewed; not adopted. Per Main's decision, it is not part of v220 and has no successor gate.
- Value side only, under v209 (`1ec52034…`).
- All-variable, source-fixed conventional proofs. No machine-checked identity.
- No chosen numeric probe: every parameter is symbolic.
- No scientific interpreter, Eval, calculator, CAS, program, enumeration, solver or replay. No new GO.
- Frozen v27–v32 untouched. No v220 file, live review or assignment read.

## 0. Setting and statements

**Class PR (planar rotation noise, scalar corrected drift).** Uncontrolled constant data with:

- n = 2, A0 = σJ with J = [[0,−1],[1,0]] and σ ≠ 0;
- Ā := A − A0^2/2 = μI with μ < 0, i.e. A = (μ − σ^2/2)I;
- arbitrary C ∈ R^{2×p} and D0 ∈ R^{q×2};
- preview δ ≥ 0;
- the canonical one-Brownian filtration.

Write R(θ) := e^{θJ}, M := D0^T D0 with eigenvalues m_1 ≥ m_2 ≥ 0, and M_0 := M − ((m_1+m_2)/2)I, the traceless part. Write κ_1 ≥ κ_2 ≥ 0 for the eigenvalues of CC^T, so ||C||^2 = κ_1.

**EMS.** The class is EMS: by v34 Lemma DS with commuting data, the autonomous solution is X_t = R(σW_t)e^{μt}x_0, so E|X_t|^2 = e^{2μt}|x_0|^2.

The plant is commuting and rotation-like; VIS of v36 fails. It lies in v36 case (c) whenever the noise is visible, or in case (b) otherwise.

**Kernel.** By v34 Lemma DS (commuting form, v36 Lemma CK), the state driven by an input w is

`X_t = ∫_0^t e^{μ(t−s)} R(σ(W_t − W_s)) C w(s−δ) ds`.

The output is z = D0 X. Below, the shift by δ is suppressed: it is an isometric relabelling of input times and changes nothing.

**Theorem Q.** Fix any original E2 input w.

1. **(Exact second-moment identity.)** With Ξ := ((m_1+m_2)/(4|μ|)) I + M_0/(2(|μ|+σ^2)),

   `E∫_0^∞ |z_t|^2 dt = 2 E∫_0^∞ <C w(s), Ξ X_s> ds`.

2. **(RMS bound.)** G2,∞^2 ≤ (κ_1/|μ|)·[(m_1+m_2)/(2|μ|) + (m_1−m_2)/(2(|μ|+σ^2))].
3. **(Robust lower bound.)** G_rob ≥ ||D0 C||/|μ|, from the path ℓ ≡ 0. Also G_rob ≤ √m_1 √κ_1/|μ|.
4. **(STRICT, criterion I.)** If ||D0C||^2 > κ_1[(m_1+m_2)/2 + |μ|(m_1−m_2)/(2(|μ|+σ^2))], then G2,∞ < G1,∞ ≤ √2·G2,∞. In particular, if ||D0C||^2 = m_1κ_1 (the "aligned" case), the gap is STRICT iff m_1 > m_2, i.e. the output is anisotropic.
5. **(STRICT, criterion II.)** If M = mI with m > 0 (isotropic output) and κ_1 > κ_2 (anisotropic input, e.g. a single input column), then the gap is STRICT.
6. **(EQUALITY.)** If M = mI and CC^T = κI, then G1,∞ = G2,∞ = G_rob = √(mκ)/|μ|. This holds although the noise IS visible in the kernel: k_ℓ depends on ℓ.

**Corollary Q1 (the v34 rotational example is STRICT).** Take C = e_1 and D0 = e_1^T, i.e. A = −αI with μ = −α + σ^2/2 < 0. This is aligned with m_1 = 1 > m_2 = 0. Moreover the identity gives the sharper value bound

`G2,∞ ≤ c_* := (1/2)(1/|μ| + 1/(|μ|+σ^2)) < 1/|μ| = G_rob`.

Hence

`G2,∞ ≤ c_* < G1,∞ ≤ min(√2·G2,∞, 1/|μ|)`.

This settles the comparison that v34 §0 left open and the addendum `022c66b8…` item X3 kept open.

**Corollary Q2 (v36 case (c) is genuinely mixed).** Within commuting rotation-like noise, both outcomes occur: STRICT (Q1, item 4, item 5) and EQUALITY with a non-deterministic kernel (item 6). So the equality class is strictly larger than the deterministic-kernel class. No algebraic dichotomy of the v36 V1 type can hold for complex noise spectrum without further invariants.

**NOT delivered.**

- A decision for anisotropic misaligned planar data where criterion I fails.
- A decision for higher-dimensional rotation noise.
- Exact G2 or G1 values. Item 6 is exact only in the equality case.
- Controlled data, a controller, synthesis, or an RMS-to-literal transfer. C1–C3 and R4 STOPPED.

## 1. Inputs and separation

**Adopted inputs** (read completely this session):

| Input | LF | Pin |
|---|---|---|
| v25 | 348 | `8c381b1f…` |
| v26 | 308 | `6666f555…` |
| parent | 74 | `1f00e0c6…` |

**Cited owner packets** (author-written, unreviewed):

| Packet | Pin | Used for |
|---|---|---|
| v27 | `af2abd51…` | √2 bound |
| v31 | `4c2a7b9b…` | G2,∞ < ∞; G2 ≤ G1 |
| v34 | `6fcca986…` | Lemma DS, G_rob, Theorem R |
| v36 | `4ecfa7c6…` | Lemma CK, case labels |

**Separation.**

- The proof is a direct computation of E||T_C w||^2 from the explicit kernel, using Fubini, independence of Brownian increments and the Gaussian characteristic function.
- No storage function, dissipation inequality, Riccati/LMI, controller, selected control, changed output, quarantined guidance or RMS source is used.
- The constant matrix Ξ is an explicit Gaussian average of rotated output weights inside one expectation identity. It is not used as a certificate for any controller or storage function.

**Ordinary tools.**

- E cos(2a) = e^{−2σ^2u} and E sin(2a) = 0 for a ~ N(0, σ^2u).
- The conjugation rule R(−a) M_0 R(a) = cos(2a) M_0 + sin(2a) M_0', where M_0' is traceless symmetric.
- Cauchy–Schwarz; the pathwise bound ||X|| ≤ ||Cw||/|μ|; the H∞ norm of e^{μu}·(constant matrix).

## 2. Proof of item 1 (identity)

**Fubini.** E∫_0^∞|z_t|^2 dt = E∫dt ∫∫_{s,s'<t} w(s)^T k(t,s)^T k(t,s') w(s') ds ds', where k(t,s) = e^{μ(t−s)} D0 R(σ(W_t−W_s)) C. The integrand is absolutely integrable: it is bounded by m_1κ_1 E∫(T_μ|w|)^2 ≤ m_1κ_1 E∫|w|^2/μ^2.

**Symmetry.** The integrand is symmetric in (s, s') as a real scalar, so the integral is twice the integral over s' < s.

**Conditioning.** For s' < s < t, put a := σ(W_t − W_s) ~ N(0, σ^2(t−s)), independent of F_s, and β := σ(W_s − W_{s'}), which is F_s-measurable. Since rotations commute, R(a + β) = R(a)R(β). The factors w(s), w(s') and R(β) are F_s-measurable, so

`E[k(t,s)^T k(t,s') | F_s] = e^{μ(2t−s−s')} C^T E[R(−a) M R(a)] R(β) C = e^{μ(2t−s−s')} C^T [((m_1+m_2)/2) I + e^{−2σ^2(t−s)} M_0] R(β) C`.

This uses R(−a) M_0 R(a) = cos(2a) M_0 + sin(2a) M_0' for a traceless symmetric M_0: conjugation rotates the (diagonal, off-diagonal) pair by the double angle.

**Time integral.** Integrating t over (s, ∞), with e^{μ(2t−s−s')} = e^{μ(s−s')} e^{2μ(t−s)}, gives e^{μ(s−s')} C^T Ξ R(β) C.

**Recognizing the state.** Summing over s' < s gives

`E∫|z|^2 = 2E∫ w(s)^T C^T Ξ [∫_0^s e^{μ(s−s')} R(σ(W_s−W_{s'})) C w(s') ds'] ds = 2E∫ <Cw(s), Ξ X_s> ds`. ∎

## 3. Proof of items 2–6

**Item 2.** Ξ is symmetric with eigenvalues (m_1+m_2)/(4|μ|) ± (m_1−m_2)/(4(|μ|+σ^2)), so 2||Ξ|| = (m_1+m_2)/(2|μ|) + (m_1−m_2)/(2(|μ|+σ^2)).

- Pathwise ||X|| ≤ ||Cw||/|μ|, because rotations are orthogonal and ∫e^{μu}du = 1/|μ|.
- Cauchy–Schwarz then gives E∫|z|^2 ≤ 2||Ξ|| (E∫|Cw|^2)^{1/2}(E∫|X|^2)^{1/2} ≤ (2||Ξ||/|μ|) κ_1 E∫|w|^2.

**Item 3.**

- For ℓ ≡ 0, T_0 is convolution with e^{μu} D0C, with norm ||D0C||/|μ|, attained at zero frequency through the supremum over T.
- The upper bound: |z| ≤ √m_1 |X| pathwise for every path, combined with item 2's pathwise bound.

**Item 4.** G_rob^2 ≥ ||D0C||^2/μ² exceeds item 2's bound exactly under the displayed inequality, so v34 Theorem R gives strictness.

- In the aligned case the inequality reads m_1 > (m_1+m_2)/2 + |μ|(m_1−m_2)/(2(|μ|+σ^2)), i.e. (m_1−m_2)σ^2/(2(|μ|+σ^2)) > 0. That is m_1 > m_2, since σ ≠ 0.
- If m_1 = m_2, the aligned inequality fails; that case is covered by item 5 or item 6.

**Item 5.** Here |z|^2 = m|X|^2. Apply item 1 with the output map I, for which M = I, M_0 = 0 and Ξ = I/(2|μ|):

`E∫|X|^2 = (1/|μ|) E∫ <w(s), C^T X_s> ds ≤ (1/|μ|) ||w|| ||C^T X||`.

Now C^T X is the output of the same plant with output map C^T, whose weight is CC^T with eigenvalues κ_1 > κ_2. Item 2 gives

||C^T X||^2 ≤ (κ_1/|μ|)[(κ_1+κ_2)/(2|μ|) + (κ_1−κ_2)/(2(|μ|+σ^2))] ||w||^2 < (κ_1^2/μ^2)||w||^2,

with norms in L2(dP dt). Hence G2^2 ≤ m sup ||X||^2/||w||^2 < m κ_1/μ^2. Meanwhile G_rob ≥ ||D0C||/|μ| = √m √κ_1/|μ|, because D0^T D0 = mI gives ||D0 C|| = √m ||C||. So G2 < G_rob, and v34 Theorem R gives strictness.

**Item 6.** Here G_rob ≤ √m √κ/|μ| by item 3. For the lower bound on G2:

- Fix a unit vector u ∈ R^2 and a deterministic f ∈ L2, and use the adapted input w(s) := κ^{−1/2} C^T R(σW_s) u f(s).
- Then |w(s)| = |f(s)| and Cw(s) = κ^{1/2} R(σW_s) u f(s). So X_t = κ^{1/2} R(σW_t) u (T_μ f)(t) and |z_t| = √(mκ) |(T_μ f)(t)| pathwise.
- Taking the supremum over f gives G2 ≥ √(mκ)/|μ|.

Hence G2 ≥ G_rob ≥ G1 ≥ G2 (v34 item 1 and v31), so all are equal. The kernel e^{μ(t−s)} D0 R(σ(ℓ(t)−ℓ(s))) C depends on ℓ whenever D0, C ≠ 0. ∎

**Corollary Q1.** Here M = e_1e_1^T, with (m_1+m_2)/2 = 1/2 and M_0 = (1/2)diag(1, −1). So e_1^T Ξ = (c_*/2) e_1^T, and item 1 reads

`E∫ z^2 = c_* E∫ w z`.

Cauchy–Schwarz gives ||z|| ≤ c_* ||w||, so G2 ≤ c_*. The bound c_* < 1/|μ| holds since σ ≠ 0. And G_rob = 1/|μ|, by item 3 with ||D0C|| = 1 = √m_1 √κ_1. ∎

## 4. Meaning (value side only)

**Rotation noise.** Even pure rotation (norm-preserving) noise makes the printed E path-L2 level STRICTLY exceed the mean-square level when the input or output is anisotropic, for example the canonical first-coordinate example.

**Equality.** When both input and output are rotation-isotropic, adapted inputs can co-rotate with the noise. Then the levels coincide, even though the noise is visible in every pathwise kernel.

**Consequence.** The equality/strictness boundary is governed by symmetry, not merely by kernel determinism.

## 5. Process and assurance

- Written exact mathematics only, after v209 was read FIRST and the adopted inputs were read completely.
- Frozen v27–v32 untouched.
- Main's decisions were received: v220 freeze, and v33–v38 remain separate unreviewed candidates without a gate. No v220 file, review or assignment was opened.
- No pinned/frozen/shared edit. No Git, deletion, publication or external model.
- All permanent findings and ZERO quarantines remain: post56, post60, postS126, the self-released v163 assessment, and the protected S242 window. HELD_C889 was never opened.
- No formal, kernel, human, configured-family, executable or novelty acceptance.
- Same18, HOLD v2, science cutoff 2026-10-27T11:05:38-07:00 and delivery deadline 12:35:38 apply. This is not an early final park.

**END OF COMPLETE v39.**
