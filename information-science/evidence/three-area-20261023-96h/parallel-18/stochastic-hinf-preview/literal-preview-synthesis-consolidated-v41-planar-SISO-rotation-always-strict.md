# Planar rotation noise, single input and single output: the literal-vs-RMS gap is ALWAYS strict (every input/output direction)

Owner **InfoHinfPreview-2 / info-3**. Clock observed with `/bin/date` immediately before writing: **Tue Oct 27 07:54:09 PDT 2026**.

**Status.**

- NEW COMPLETE WRITTEN OWNER-CANDIDATE, written as a separate successor. Author-written and unreviewed; not adopted; no gate.
- Value side only, under v209 (`1ec52034…`).
- All-variable, source-fixed conventional proofs. No machine-checked identity.
- No chosen numeric probe.
- No scientific interpreter, Eval, calculator, CAS, program, enumeration, solver or replay. No new GO.
- Frozen v27–v32 untouched. No v220 file, live review or assignment read.

## 0. Setting and statement

**Class PR-SISO.** This is the planar class of v39 (`4f1903b3…`, with erratum `1dbf820a…`) with p = q = 1:

- A0 = σJ with σ ≠ 0;
- Ā = μI with μ < 0;
- input column c ∈ R^2 \ {0} and output row d^T with d ∈ R^2 \ {0};
- any preview δ ≥ 0;
- canonical one-Brownian filtration;
- EMS, as in v39.

**Reduction to standard position.** Identify R^2 with C, so that J acts as multiplication by i. A fixed rotation R_0 commutes with J and with the noise. The change of state X' = R_0^T X maps (C, D0) to (R_0^T C, D0 R_0) and preserves every input–output path operator, hence G1, G2 and G_rob. So WLOG c > 0 is real. Write the output as z = Re(gX) with g ∈ C \ {0}, and put φ := arg g. Set

`a := 1/|μ|`, `b := 1/(|μ| + σ^2)`, `r := b/a ∈ (0,1)`, `c_* := (a+b)/2`.

**Theorem SISO.** For every such plant and every preview,

`G2,∞ ≤ c|g| (c_* |a + e^{2iφ} b|/2)^{1/2} < c|g| a (1 + |cos φ|)/2 ≤ G_rob`.

Hence, by v34 Theorem R,

`G2,∞ < G1,∞ ≤ √2·G2,∞`

for EVERY direction of input and output. The gap is STRICT throughout PR-SISO.

**Planar status after v39/v40/v41.** In the planar class PR:

| Case | Outcome | Source |
|---|---|---|
| SISO | STRICT | this packet |
| isotropic output, anisotropic input | STRICT | v39 item 5 |
| isotropic input (CC^T = κI; automatically aligned), anisotropic output | STRICT | v39 item 4 as corrected by E1 |
| criterion I | STRICT | v39 item 4 |
| bi-isotropic | EQUALITY | v39 item 6 |

OPEN: planar multi-channel data with anisotropic, misaligned input and output for which criterion I fails.

**NOT delivered.**

- The open planar multi-channel case above.
- Higher-dimensional analogues beyond v40.
- Exact gains.
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
| v27 | `af2abd51…` | √2 bound |
| v31 | `4c2a7b9b…` | G2 < ∞; G2 ≤ G1 |
| v34 | `6fcca986…` | Lemma DS, G_rob, Theorem R |
| v39 | `4f1903b3…` with erratum `1dbf820a…` | identity item 1 and the planar cases |

**Separation.** None of the following is used: storage function, dissipation inequality, Riccati/LMI, controller, selected control, changed output, quarantined guidance, RMS source.

**Ordinary tools.**

- v39's Fubini/conditional-expectation identity.
- Cauchy–Schwarz.
- DC gain of an L1 causal convolution.
- Elementary calculus on a quartic polynomial.

## 2. Lemma F — functional recursion

**Claim.** For every adapted E2 input w and every h ∈ C, define y_h := Re(hX). Then

`E∫ y_h^2 = c E∫ w · y_{Γ(h)}`, where Γ(h) := (|h|^2 a + h^2 b)/2.

**Proof.** Apply v39 item 1 with D0 = d^T, where d ↔ h̄ so that d^T X = Re(hX):

- M = dd^T, with m_1 = |h|^2, m_2 = 0 and M_0 = dd^T − (|h|^2/2)I;
- Cw = c w e_1.

Then e_1^T 2Ξ X = (|h|^2 a/2) X_1 + b(d_1 d^T X − (|h|^2/2)X_1). Writing h = h_R + i h_I, so d = (h_R, −h_I),

`d_1 d^T X − (|h|^2/2) X_1 = (h_R^2 − h_I^2)X_1/2 − h_R h_I X_2 = Re(h^2 X)/2`.

Hence e_1^T 2Ξ X = Re(Γ(h) X), and v39 item 1 gives the claim. ∎

## 3. Proof of Theorem SISO

**Step 1 — uniform bound over unit functionals.** Let G(h) be the RMS gain from w to y_h, and Gmax := sup_{|h|=1} G(h). Gmax is finite: Gmax ≤ G_rob ≤ c a by v39 item 3.

- By homogeneity G(h) = |h| G(h/|h|) ≤ |h| Gmax.
- Lemma F and Cauchy–Schwarz give, for unit h,

  G(h)^2 ≤ c G(Γ(h)) ≤ c |Γ(h)| Gmax,

  with |Γ(h)| = |a + e^{2i arg h} b|/2 ≤ (a+b)/2 = c_*.

- Taking the supremum over unit h gives Gmax^2 ≤ c c_* Gmax, so Gmax ≤ c c_*.
- Hence, for the given g,

  `G2,∞ = G(g) ≤ |g| (c |Γ(e^{iφ})| · c c_*)^{1/2} = c|g| (c_* |a + e^{2iφ} b|/2)^{1/2}`.

**Step 2 — a rotating noise path.** For κ ∈ R take the continuous path ℓ_t = κt (ℓ_0 = 0) and put Ω := σκ.

- The pathwise operator is the time-invariant causal convolution with K(u) = e^{μu} Re(g e^{iΩu}) c, which is in L1.
- Its L2(0,∞) norm, over the supremum in T, is at least |K̂(0)|, using long constant inputs.
- K̂(0) = c Re(g/(|μ| − iΩ)).
- Writing Ω = −|μ| tan ψ with ψ ∈ (−π/2, π/2), K̂(0) = c|g| cos(φ − ψ) cos ψ/|μ|.
- Replacing g by −g flips the sign of the output and changes no gain, so WLOG cos φ ≥ 0, i.e. φ ∈ [−π/2, π/2]. Choose ψ := φ/2 ∈ [−π/4, π/4]. Then cos(φ − ψ) cos ψ = cos^2(φ/2) = (1 + cos φ)/2, so |K̂(0)| = c|g| a (1 + |cos φ|)/2.
- Hence G_rob ≥ c|g| a (1 + |cos φ|)/2.

**Step 3 — the elementary inequality.** Put C := |cos φ| ∈ [0,1]. Since |1 + r e^{2iφ}|^2 = (1+r)^2 − 4r(1 − C^2), the strict middle inequality of the theorem is equivalent to

`(1+C)^4 > g_C(r) := (1+r)^4 − 4r(1+r)^2(1 − C^2)` for every r ∈ (0,1).

**Derivative.** g_C'(r) = 4(1+r) h_C(r), with h_C(r) := r^2 + (3C^2 − 1) r + C^2. Note:

- h_C(0) = C^2;
- h_C(1) = 4C^2;
- h_C(C) = C(3C − 1)(C + 1);
- g_C(1) = 16C^2 and g_C(0) = 1.

**Case C ≥ 1/3.** Either the vertex (1 − 3C^2)/2 ≤ 0, or the minimum C^2 − (1 − 3C^2)^2/4 ≥ 0 (equivalent to (3C−1)(C+1) ≥ 0). In both sub-cases h_C ≥ 0 with at most isolated zeros on [0,1].

- So g_C is strictly increasing there, and g_C(r) < g_C(1) = 16C^2 for r < 1.
- Also (1+C)^4 − 16C^2 = (1−C)^2((1+C)^2 + 4C) ≥ 0.
- Hence g_C(r) < (1+C)^4.

**Case 0 < C < 1/3.** h_C(0) > 0, h_C(C) < 0 and h_C(1) > 0, so h_C has roots r_1 < C < r_2 < 1.

- g_C increases on [0, r_1], decreases on [r_1, r_2] and increases on [r_2, 1].
- So for r ∈ (0,1), g_C(r) ≤ max(g_C(r_1), g_C(1)).
- g_C(r_1) ≤ (1 + r_1)^4 < (1+C)^4, because the subtracted term is ≥ 0 and r_1 < C.
- g_C(1) = 16C^2 < (1+C)^4 by the identity above, since C < 1.

**Case C = 0.** h_0(r) = r(r − 1) < 0 on (0,1). So g_0 is strictly decreasing, and g_0(r) < g_0(0) = 1 = (1+C)^4.

**Step 4 — conclusion.** Squaring the middle inequality of the theorem and dividing by c^2|g|^2 a^2/4 gives exactly Step 3, so the middle inequality holds. Steps 1–3 then give G2,∞ < G_rob, and v34 Theorem R gives G1,∞ > G2,∞. The upper bound √2·G2,∞ is v27 Corollary C1. ∎

## 4. Remarks

- **Tightness.** The rotating-path bound of Step 2 is not claimed to equal G_rob. It is only a sufficient lower bound, and it already beats the RMS bound in every direction.
- **Fully cross-coupled case.** For φ = π/2 the noise is the ONLY coupling: the ℓ ≡ 0 gain d^T c is zero. The adapted adversary still cannot reach the robust level G_rob ≥ c|g|a/2, while G2 ≤ c|g|(c_*(a−b)/2)^{1/2}.
- **No synthesis statement** is made.

## 5. Process and assurance

- Written exact mathematics only, after v209 was read FIRST and the adopted inputs were read completely.
- Frozen v27–v32 untouched.
- Main's decisions were received: v220 freeze, and successors remain author-written unreviewed candidates without a gate. No v220 file, review or assignment was opened.
- No pinned/frozen/shared edit. No Git, deletion, publication or external model.
- All permanent findings and ZERO quarantines remain: post56, post60, postS126, the self-released v163 assessment, and the protected S242 window. HELD_C889 was never opened.
- No formal, kernel, human, configured-family, executable or novelty acceptance.
- Same18, HOLD v2, science cutoff 2026-10-27T11:05:38-07:00 and delivery deadline 12:35:38 apply. This is not an early final park.

**END OF COMPLETE v41.**
