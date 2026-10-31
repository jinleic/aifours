# Exact robust noise-path gain for EVERY planar single-input rotation-noise plant: a closed-form upper certificate for the printed literal gain

Owner **InfoHinfPreview-2 / info-3**. Clock observed with `/bin/date` immediately before writing: **Tue Oct 27 08:09:51 PDT 2026**.

**Status.**

- NEW COMPLETE WRITTEN OWNER-CANDIDATE, written as a separate successor. Author-written and unreviewed; not adopted; no gate.
- Value side only, under v209 (`1ec52034…`).
- All-variable, source-fixed conventional proofs. No machine-checked identity.
- No chosen numeric probe.
- No scientific interpreter, Eval, calculator, CAS, program, enumeration, solver or replay. No new GO.
- Frozen v27–v32 untouched. No v220 file, live review or assignment read.

## 0. Setting and statement

**Class PR-1.** Planar class PR with:

- A0 = σJ with σ ≠ 0 and Ā = μI with μ < 0;
- a single input c e_1 with c > 0 (WLOG by a rotation, v41 §0);
- an ARBITRARY output map D0 ∈ R^{q×2};
- any preview δ ≥ 0;
- canonical one-Brownian filtration.

Write M := D0^T D0 = m_2 I + (m_1 − m_2) e e^T with m_1 ≥ m_2 ≥ 0, m_1 > 0, and e = (cos φ_0, sin φ_0). Put a := 1/|μ|, C := |cos φ_0| and S := |sin φ_0|.

**Weight profile.** For k ∈ [0,1] define

`W(k) := m_2 + (m_1 − m_2)(√k·C + √(1−k)·S)^2`.

W(k) is the largest output weight (cos α, sin α) M (cos α, sin α)^T over state angles α with cos^2 α = k.

**Theorem RG1 (exact robust gain).**

`G_rob^2 = c^2 a^2 Λ`, where Λ := max_{k∈[0,1]} k W(k).

Consequently, the printed literal gain satisfies the closed-form certificate

`G2,∞ ≤ G1,∞ ≤ min(√2·G2,∞, c a √Λ)`.

The maximum exists by continuity. G_rob does not depend on σ ≠ 0.

**Corollary RG1a (consistency).**

- **Eigen-aligned case.** If φ_0 ∈ {0, π/2}, i.e. CS = 0, then Λ = Φ(x, y) of v44 with (x, y) = (M_11, M_22). This recovers v44 Theorem RG.
- **SISO (m_2 = 0).** Λ = m_1((1 + C)/2)^2, matching the v41 lower bound c|g|a(1 + |cos φ|)/2 with m_1 = |g|^2. That lower bound is now exact.

**Corollary RG1b (strictness test).** By v43 Lemma Γ and the v41 recursion, G2,∞^2 ≤ c^2 c_* |Γ_M|, where

c_* := (a + b)/2, b := 1/(|μ| + σ^2), and |Γ_M| = |a(m_1 + m_2) + b(m_1 − m_2) e^{2iφ_0}|/2.

Hence the gap is STRICT whenever c_* |Γ_M| < a^2 Λ. In the eigen-aligned case v43/v44 decide everything exactly, with equality only on the v44 locus. Off the eigen-aligned case this test is sufficient, not necessary; an exact G2 there is NOT delivered.

**NOT delivered.**

- Exact G2 or G1 for non-eigen-aligned data.
- A complete equality characterization for non-eigen-aligned data.
- Multi-input planar data and higher dimensions.
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
| v31 | `4c2a7b9b…` | G2 ≤ G1 |
| v34 | `6fcca986…` | T_ℓ, G_rob, item 1 |
| v41 | `913fd056…` | Lemma F, recursion |
| v43 | `b4e13943…` | Lemma Γ |
| v44 | `796c420a…` | the polar-form reduction and kernel identity, §2 Steps 1–4 |

**Separation.** This is a deterministic statement about v34's noise-path operators. It uses the explicit kernel (Fubini) identity, Young, Cauchy–Schwarz and the supporting line of a concave function. No storage function, dissipation inequality, Riccati/LMI, Gramian certificate, controller, selected control, changed output, quarantined guidance or RMS source is used, and nothing here is a realization step.

## 2. Proof of Theorem RG1

**Weight profile.**

- With X = ρ e^{iα}, the output density is ρ^2 (m_2 + (m_1 − m_2) cos^2(α − φ_0)).
- For cos^2 α = k, the sign choices give cos(α − φ_0) = ±√k cos φ_0 ± √(1−k) sin φ_0, whose largest square is (√k C + √(1−k) S)^2.
- h(k) := (√k C + √(1−k) S)^2 = kC^2 + (1−k)S^2 + 2CS √(k(1−k)) is concave on [0,1], because √(k(1−k)) is concave. So W is concave and continuous.

**Lower bound.** Take the constant-rate rotating path with Ω = |μ| tan ψ and ψ ∈ (−π/2, π/2), as in v43 §4. Its DC gain is (c cos ψ/|μ|) D0 R(ψ) e_1, so

G_rob^2 ≥ c^2 a^2 cos^2ψ (m_2 + (m_1 − m_2) cos^2(ψ − φ_0)).

For a given k = cos^2 ψ ∈ (0,1], cos ψ = √k and sin ψ = ±√(1−k). Choosing the sign of sin ψ equal to the sign of cos φ_0 sin φ_0 gives cos^2(ψ − φ_0) = h(k). Hence G_rob^2 ≥ c^2 a^2 sup_{k∈(0,1]} k W(k) = c^2 a^2 Λ, since the value at k = 0 is 0.

**Upper bound.** Fix a path and an input, and use v44 §2 Steps 1–4 verbatim: ρ = c e^{−|μ|·} ⋆ u, with u = v(·−δ) cos α, k = cos^2 α and E = ∫u^2/k ≤ ||v||^2. Then:

- ∫ρ^2 = c a ∫uρ;
- S := ∫|u|ρ satisfies S^2 ≤ E ∫kρ^2.

The output energy is O ≤ ∫ρ^2 W(k(t)) dt. Let k* be a maximizer of kW(k).

**Case 1: k* ∈ (0,1) and W differentiable at k*.** The first-order condition is W(k*) + k* W'(k*) = 0. Concavity gives the supporting line

W(k) ≤ L(k) := W(k*) + W'(k*)(k − k*) = W(k*)(2 − k/k*) on [0,1].

Hence

O ≤ 2W(k*) ∫ρ^2 − (W(k*)/k*) ∫kρ^2 ≤ 2W(k*) c a S − (W(k*)/k*) S^2/E ≤ max_{S≥0} [⋯] = k* W(k*) c^2 a^2 E = Λ c^2 a^2 E.

**Case 2: CS ≠ 0 and m_1 > m_2.** Then k* lies in (0,1) and h is smooth there, so Case 1 applies.

- Λ > 0 while kW(k) = 0 at k = 0.
- As k → 1, h'(k) → −∞ because C > 0 and S > 0. Since m_1 > m_2, d/dk[kW(k)] → −∞, and k = 1 is not a maximizer.

**Case 2': m_1 = m_2 (isotropic M).** Every direction is an eigenvector, so choose e = e_1, i.e. S = 0. This is Case 3. Directly: W ≡ m_1, Λ = m_1, and the output density is ≤ m_1 ρ^2.

**Case 3: CS = 0.** Then h(k) = k (if S = 0) or h(k) = 1 − k (if C = 0). W is affine, and this is v44's class: Theorem RG there gives exactly c^2 a^2 Λ, with Λ = Φ(x, y).

In all cases O ≤ c^2 a^2 Λ ||v||^2. ∎

**Corollary RG1a.**

- **Eigen-aligned.** For S = 0, i.e. φ_0 ∈ {0, π}, x = m_1 ≥ y = m_2. Then W(k) = m_2 + (m_1 − m_2)k, kW is increasing, and Λ = m_1 = x = Φ. For C = 0, x = m_2 and y = m_1; maximizing k(m_1 − (m_1 − m_2)k) gives Φ.
- **SISO.** max_ψ cos^2 ψ cos^2(ψ − φ_0) = ((1 + C)/2)^2, at ψ = φ_0/2 after reducing to cos φ_0 ≥ 0, as in v41 Step 2.

**Corollary RG1b.** This combines the displayed bounds with v34 Theorem R. ∎

## 3. Meaning (value side only)

**Closed-form upper certificate.** For every planar single-input rotation-noise plant, the deterministic worst case over noise realizations is now an explicit one-variable concave maximization. It is a closed-form upper certificate for the printed literal gain, alongside the √2 Fefferman certificate.

**Comparison with √2.** Whether c a √Λ or √2·G2 is the smaller certificate is data-dependent. No general comparison is asserted.

**Synthesis.** No controller or synthesis statement is made.

## 4. Process and assurance

- Written exact mathematics only, after v209 was read FIRST and the adopted inputs were read completely.
- Frozen v27–v32 untouched. No v220 file, review or assignment was opened.
- No pinned/frozen/shared edit. No Git, deletion, publication or external model.
- All permanent findings and ZERO quarantines remain: post56, post60, postS126, the self-released v163 assessment, and the protected S242 window. HELD_C889 was never opened.
- No formal, kernel, human, configured-family, executable or novelty acceptance.
- Same18, HOLD v2, science cutoff 2026-10-27T11:05:38-07:00 and delivery deadline 12:35:38 apply. This is not an early final park.

**END OF COMPLETE v45.**
