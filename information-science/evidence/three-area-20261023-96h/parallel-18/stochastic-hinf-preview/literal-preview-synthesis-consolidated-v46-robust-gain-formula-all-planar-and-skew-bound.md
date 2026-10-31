# A closed-form robust noise-path gain for EVERY planar rotation-noise plant, G_rob = max_{|u|=1} |C^T u||D0 u| / |μ|, and a duality upper bound in every dimension

Owner **InfoHinfPreview-2 / info-3**. Clock observed with `/bin/date` immediately before writing: **Tue Oct 27 08:14:16 PDT 2026**.

**Status.**

- NEW COMPLETE WRITTEN OWNER-CANDIDATE, written as a separate successor. Author-written and unreviewed; not adopted; no gate.
- Value side only, under v209 (`1ec52034…`).
- All-variable, source-fixed conventional proofs. No machine-checked identity.
- No chosen numeric probe.
- No scientific interpreter, Eval, calculator, CAS, program, enumeration, solver or replay. No new GO.
- Frozen v27–v32 untouched. No v220 file, live review or assignment read.

## 0. Statements

**Class RS (v40).** Uncontrolled constant data with:

- A0 real skew-symmetric;
- Ā := A − A0^2/2 = μI with μ < 0;
- arbitrary C ∈ R^{n×p} and D0 ∈ R^{q×n};
- preview δ ≥ 0;
- canonical one-Brownian filtration;
- EMS (v40).

Put a := 1/|μ|, M := D0^T D0 and N := CC^T.

**Theorem RGN (any dimension, upper certificate).**

`G_rob ≤ a · inf_{β>0} λ_max(M + βN)/(2√β)`.

Hence the printed literal gain satisfies G1,∞ ≤ a · inf_{β>0} λ_max(M + βN)/(2√β).

**Theorem RGP (planar: exact).** Let n = 2 and A0 = σJ with σ ≠ 0, i.e. class PR with ANY C and D0. Then

`G_rob = a · max_{|u|=1} |C^T u| |D0 u| = a · inf_{β>0} λ_max(M + βN)/(2√β)`.

**Corollaries.**

- **P1.** Theorem RGP contains v44 Theorem RG (eigen-aligned single input) and v45 Theorem RG1 (any single input). With C = c e_1, |C^T u|^2 = c^2 cos^2 α and |D0 u|^2 = W at angle α.
- **P2.** Bi-isotropic data (N = κI, M = mI) give G_rob = a√(κm), matching v39 item 6.
- **P3 (literal certificate).** For every planar rotation-noise plant,

  `G2,∞ ≤ G1,∞ ≤ min(√2·G2,∞, a·max_{|u|=1}|C^T u||D0 u|)`,

  and G1 = G2 iff G2 = a·max_u |C^T u||D0 u| (v34 Theorem R).
- **P4 (comparison with the noise-free gain).** max_u |C^T u||D0 u| ≥ ||D0 C||, with u := Cv/|Cv|. So the robust certificate is never below the ℓ ≡ 0 gain ||D0C||/|μ|.

**NOT delivered.**

- Attainability of Theorem RGN's bound for n ≥ 3. Noise paths reach only orbit directions.
- Exact G2 beyond v43.
- Exact G1 beyond the v44 equality locus and v39 item 6.
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
| v27 | `af2abd51…` | √2 |
| v31 | `4c2a7b9b…` | G2 ≤ G1 |
| v34 | `6fcca986…` | T_ℓ, G_rob, Theorem R |
| v40 | `fd6a77b9…` | class RS and EMS |
| v43 | `b4e13943…` | rotating-path DC gain technique |
| v44 | `796c420a…` | polar reduction and kernel identity |
| v45 | `d7c9814c…` | supporting-line step |

**Separation.** This is a deterministic statement about v34's noise-path operators. It uses explicit kernel identities (Fubini), Young, Cauchy–Schwarz, the eigenvalue bound u^T(M + βN)u ≤ λ_max for unit u, and a supporting line of a concave function. No storage function, dissipation inequality, Riccati/LMI, Gramian certificate, controller, selected control, changed output, quarantined guidance or RMS source is used, and nothing here is a realization step.

## 2. Proof of Theorem RGN

Fix T, a continuous path ℓ with ℓ(0) = 0 (extended constantly beyond T), and an input v ∈ L2 (extended by 0). Put θ := ℓ.

1. **Norm reduction.** By v34, T_ℓ v = D0 X with X(t) = ∫_0^t e^{μ(t−s)} e^{A0(θ(t)−θ(s))} C v(s−δ) ds.
   - Put Z := e^{−A0θ} X, so Ż = μZ + e^{−A0θ} C v(·−δ) a.e.
   - Since e^{A0θ} is orthogonal, ρ := |Z| = |X| is absolutely continuous with ρ̇ = −|μ|ρ + u a.e., where u := <C v(·−δ), X̂> and X̂ := X/|X|. Put u := 0 on {X = 0}, where ρ̇ = 0 a.e.
   - Hence ρ = e^{−|μ|·} ⋆ u.
2. **Cost.** Put K := X̂^T N X̂ = |C^T X̂|^2. Cauchy–Schwarz gives u^2 ≤ |v(·−δ)|^2 K, so E := ∫u^2/K ≤ ||v||^2, reading 0/0 as 0.
3. **Kernel identity.** ∫ρ^2 = a ∫uρ, by the Fubini computation of v44 §2 Step 3 with c absorbed.
4. **Bound.** Put S := ∫|u|ρ. Then S^2 ≤ E ∫Kρ². For any β > 0, unit vectors satisfy X̂^T M X̂ ≤ λ_β − βK with λ_β := λ_max(M + βN). Hence

   O := ∫|D0 X|^2 = ∫ρ^2 X̂^T M X̂ ≤ λ_β a S − β S^2/E ≤ λ_β^2 a^2 E/(4β).

5. **Conclusion.** ||T_ℓ v||^2 ≤ a^2 (λ_β^2/(4β)) ||v||^2 for every β, path and input. ∎

## 3. Proof of Theorem RGP

**Lower bound.** Take the constant-rate rotating path with Ω = |μ| tan ψ and ψ ∈ (−π/2, π/2). As in v43 §4, the DC transfer matrix is (cos ψ/|μ|) D0 R(ψ) C.

- For a unit input v with Cv = s u_β, the DC gain is a s cos ψ |D0 u_{β+ψ}|.
- Fix a state direction α = β + ψ. Maximizing s cos(α − β) over unit v gives max_v <Cv, u_α> = |C^T u_α|, attained at v = C^T u_α/|C^T u_α|, with the angle difference in (−π/2, π/2).
- Hence G_rob ≥ a · max_α |C^T u_α| |D0 u_α|.

**Upper bound (strong duality in the plane).** Write K(α) := u_α^T N u_α and w(α) := u_α^T M u_α.

- Both are affine in (cos 2α, sin 2α), so the joint range {(K(α), w(α))} is an ellipse, a segment or a point.
- Its upper boundary W̃(K) := max{w : (K, w) in the range} is concave on [κ_2, κ_1], where κ_1 ≥ κ_2 are the eigenvalues of N.
- Let F := max_α K(α)w(α) = max_K K W̃(K), assumed > 0 (otherwise everything vanishes), attained at K* > 0.
- The first-order conditions F'(K*+) ≤ 0 ≤ F'(K*−) (one-sided where K* is an endpoint) show that B := −W̃(K*)/K* is a supergradient of the concave W̃ at K*.
  - At an interior point, B lies between the one-sided derivatives.
  - At the right endpoint, every B ≤ W̃'(κ_1−) is a supergradient.
  - At the left endpoint, every B ≥ W̃'(κ_2+) is a supergradient.
- Hence, for every α, w(α) ≤ W̃(K(α)) ≤ 2W̃(K*) − βK(α), with β := W̃(K*)/K*.
- So λ_β ≤ 2W̃(K*), and Theorem RGN gives G_rob^2 ≤ a^2 (2W̃(K*))^2/(4β) = a^2 K* W̃(K*) = a^2 F.
- If N = κI, then K ≡ κ, and the bound is direct: O ≤ m_1 ∫ρ^2 ≤ m_1 a^2 κ E.

Combining with the lower bound, G_rob^2 = a^2 F. The infimum form equals a^2 F by the same β together with weak duality: Kw ≤ (w + βK)^2/(4β) by AM–GM. ∎

**Corollaries.**

- **P1.** Substitution.
- **P2.** |C^T u|^2 = κ and |D0 u|^2 = m for every unit u.
- **P3.** v34 Theorem R, v27, v31.
- **P4.** |C^T u| ≥ <C^T u, v> = |Cv| for unit v, so |C^T u||D0 u| ≥ |D0 C v|. ∎

## 4. Meaning (value side only)

**Planar.** For every planar rotation-noise plant with isotropic corrected drift, the deterministic worst case over noise realizations is now an explicit, storage-free two-matrix quantity: max over unit u of |C^T u||D0 u|, divided by |μ|. It gives a closed-form upper certificate for the printed literal gain, alongside √2·G2.

**Every dimension.** The same quantity, in its dual inf_β form, bounds the robust gain in every dimension with skew noise.

**Synthesis.** No controller or synthesis statement is made.

## 5. Process and assurance

- Written exact mathematics only, after v209 was read FIRST and the adopted inputs were read completely.
- Frozen v27–v32 untouched. No v220 file, review or assignment was opened.
- No pinned/frozen/shared edit. No Git, deletion, publication or external model.
- All permanent findings and ZERO quarantines remain: post56, post60, postS126, the self-released v163 assessment, and the protected S242 window. HELD_C889 was never opened.
- No formal, kernel, human, configured-family, executable or novelty acceptance.
- Same18, HOLD v2, science cutoff 2026-10-27T11:05:38-07:00 and delivery deadline 12:35:38 apply. This is not an early final park.

**END OF COMPLETE v46.**
