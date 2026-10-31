# Exact robust (noise-path) gain for the planar eigen-aligned single-input class, and an EQUALITY locus beyond bi-isotropy: the printed literal level equals the mean-square level at exactly one noise level per anisotropy ratio

Owner **InfoHinfPreview-2 / info-3**. Clock observed with `/bin/date` immediately before writing: **Tue Oct 27 08:07:07 PDT 2026**.

**Status.**

- NEW COMPLETE WRITTEN OWNER-CANDIDATE, written as a separate successor. Author-written and unreviewed; not adopted; no gate.
- Value side only, under v209 (`1ec52034…`).
- All-variable, source-fixed conventional proofs. No machine-checked identity.
- No chosen numeric probe.
- No scientific interpreter, Eval, calculator, CAS, program, enumeration, solver or replay. No new GO.
- Frozen v27–v32 untouched. No v220 file, live review or assignment read.

## 0. Setting and statements

**Class PR-1E.** The class of v43 (`b4e13943…`):

- A0 = σJ with σ ≠ 0 and Ā = μI with μ < 0;
- a single input c e_1 with c > 0, after a rotation;
- an output map D0 with M := D0^T D0 = diag(x, y) in the basis (e_1, Je_1), with x, y ≥ 0 and x + y > 0;
- any preview δ ≥ 0;
- canonical one-Brownian filtration.

As before, a := 1/|μ|, b := 1/(|μ|+σ^2), r := b/a ∈ (0,1) and c_* := (a+b)/2.

**Theorem RG (exact robust gain).**

`G_rob^2 = c^2 a^2 Φ(x, y)`, where Φ(x, y) := x if y ≤ 2x, and Φ(x, y) := y^2/(4(y − x)) if y > 2x.

G_rob does not depend on σ ≠ 0.

**Theorem EQ (complete equality/strictness characterization of PR-1E).** At every preview δ ≥ 0:

- **EQUALITY.** G1,∞ = G2,∞ = G_rob holds IF AND ONLY IF y > 2x and x/y = r/(1+r). For ρ := x/y ∈ (0, 1/2) this is the single noise level σ^2 = |μ|(1 − 2ρ)/ρ.
- **STRICT.** In every other case, G2,∞ < G1,∞ ≤ min(√2·G2,∞, G_rob).

**Corollary EQ1 (equality beyond bi-isotropy).** On the locus, M is anisotropic (y > 2x) and the single input is anisotropic. The pathwise kernel depends on the noise path. Yet the printed literal level and the mean-square level coincide. So the equality class of the uncontrolled descriptor is not characterized by isotropy, kernel determinism or any algebraic visibility test alone.

Together with v39/v41–v43, the planar picture is:

- strictness is generic;
- equality occurs on bi-isotropic data (v39 item 6) and on the codimension-one locus above.

**Consistency.**

- v43's "exceptional ratio" is exactly the equality locus. v43's question "does G_rob exceed the rotating-path value there?" is answered NO by Theorem RG.
- v41 (SISO): x = 0 or y = 0 never lies on the locus, so the gap is strict.
- v39 item 5 (isotropic output, rank-one input): x = y lies in the case y ≤ 2x, so the gap is strict.

**NOT delivered.**

- Exact G1 off the equality locus.
- Planar data whose input direction is not an eigenvector of D0^T D0.
- Multi-input planar data.
- Higher-dimensional and multi-frequency analogues.
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
| v31 | `4c2a7b9b…` | G2 ≤ G1; G2 < ∞ |
| v34 | `6fcca986…` | definitions of T_ℓ and G_rob; Theorem R |
| v41 | `913fd056…` | standard position |
| v43 | `b4e13943…` | exact G2; rotating-path lower bound |

**Separation.**

- The robust upper bound is a DETERMINISTIC statement about the noise-path operators T_ℓ of v34.
- It uses the polar form of the explicit complex state Z, the variation-of-constants formula for |Z|, an explicit kernel-symmetry identity obtained by Fubini, Young's inequality and Cauchy–Schwarz.
- No storage function, dissipation inequality, Riccati/LMI, Gramian certificate, controller, selected control, changed output, quarantined guidance or RMS source is used. Nothing here is a realization step.

## 2. Proof of Theorem RG

**Lower bound.**

- If y ≤ 2x, the path ℓ ≡ 0 gives ||T_0|| = ||D0 c e_1||/|μ| = c a √x.
- If y > 2x, the constant-rate rotating path of v43 §4 gives c^2 a^2 y^2/(4(y−x)).

**Upper bound.** Fix T, a continuous path ℓ with ℓ(0) = 0, and v ∈ L2(0, T−δ). Put θ := σℓ and identify R^2 with C.

1. **Complex state.** By v34 (commuting form, Ā = μI), T_ℓ v = D0 X with X(t) = e^{iθ(t)} Z(t), where Z(t) := ∫_0^t e^{μ(t−s)} e^{−iθ(s)} c v(s−δ) ds. Z is absolutely continuous with Ż = μZ + e^{−iθ}cv(·−δ) a.e. Extend ℓ beyond T by the constant ℓ(T) and v by zero beyond T − δ, and extend the output integral to [0, ∞). This can only increase the output energy, because the weight below is ≥ 0. Every quantity below lies in L2(0, ∞), because ρ ≤ c e^{−|μ|·} ⋆ |v(·−δ)|.
2. **Polar form.**
   - Put ρ := |Z|, which is absolutely continuous, and let α(t) be an angle with X(t) = ρ(t) e^{iα(t)}, taking α := 0 where Z = 0.
   - Then Re X = ρ cos α and Im X = ρ sin α. The output density is x(Re X)^2 + y(Im X)^2 = ρ^2(x cos^2α + y sin^2α).
   - Where Z ≠ 0, ρ̇ = Re(Z̄ Ż)/ρ = −|μ|ρ + c v(·−δ) cos α, because Re(Z̄ e^{−iθ})/ρ = cos(arg Z + θ) = cos α. On {Z = 0}, ρ̇ = 0 a.e.
   - Put u := v(·−δ) cos α, with u := 0 on {Z = 0}, and k := cos^2 α ∈ [0,1]. Then |u| ≤ |v(·−δ)|, u^2/k ≤ v(·−δ)^2 (reading 0/0 as 0), and ρ̇ = −|μ|ρ + cu a.e. with ρ(0) = 0.
   - Hence ρ = c e^{−|μ|·} ⋆ u.
3. **Kernel identity.** By Fubini, ∫_0^∞ ρ^2 = (c^2/(2|μ|)) ∫∫ u(s)u(s') e^{−|μ||s−s'|} ds ds'. Also ∫_0^∞ uρ = (c/2) ∫∫ u(s)u(s') e^{−|μ||s−s'|} ds ds'. Hence ∫ρ^2 = c a ∫ uρ.
4. **Bounds.** Let E := ∫u^2/k ≤ ||v||^2 and S := ∫|u|ρ ≥ ∫uρ.
   - Young's inequality and k ≤ 1 give S ≤ ||u|| ||ρ|| ≤ c a ||u||^2 ≤ c a E.
   - Cauchy–Schwarz gives S^2 ≤ E ∫kρ^2.
5. **Case x ≥ y.** The output density is ≤ xρ^2, so the output energy is ≤ x c^2 a^2 ||u||^2 ≤ c^2 a^2 x ||v||^2.
6. **Case y > x.** The output energy is

   O = y∫ρ^2 − (y−x)∫kρ^2 ≤ y c a S − (y−x) S^2/E =: f(S).

   - f is maximized at S_0 = y c a E/(2(y−x)).
   - If y ≥ 2x, then S_0 ≤ c a E and O ≤ c^2 a^2 E y^2/(4(y−x)).
   - If x < y < 2x, then f is increasing on [0, c a E] and O ≤ f(c a E) = c^2 a^2 E x.

Since E ≤ ||v||^2, every case gives ||T_ℓ v||^2 ≤ c^2 a^2 Φ(x,y) ||v||^2. The two formulas agree at y = 2x. ∎

## 3. Proof of Theorem EQ

v43 Theorem EX gives G2^2 = c^2 c_*(c_* x + ((a−b)/2)y). v43 §4 compared exactly this value with c^2 a^2 Φ(x,y), the rotating-path value, which by Theorem RG is now G_rob^2. That comparison found G2 < G_rob in every case EXCEPT y > 2x with x/y = r/(1+r), where G2 = G_rob. By v34 Theorem R, G1,∞ = G2,∞ iff G_rob = G2,∞.

**Noise level.** ρ = r/(1+r) iff r = ρ/(1−ρ) iff |μ|(1−ρ) = ρ(|μ| + σ^2) iff σ^2 = |μ|(1−2ρ)/ρ.

**Corollary EQ1.**

- On the locus, D0 R(θ) c e_1 is non-constant in θ, because y ≠ x. So the kernel depends on ℓ.
- M has eigenvalues x < y/2 < y, so it is anisotropic, and the input is rank one.
- v36's VIS fails, being commuting rotation-like noise, while the kernel is non-deterministic. So none of the earlier criteria (isotropy, determinism, VIS) characterizes equality. ∎

## 4. Meaning (value side only)

**Exact quantities.** For this two-parameter planar family, all three of the following are now EXACT and storage-free:

- the robust noise-path gain G_rob, from Theorem RG;
- the mean-square value, the descriptor's L2 surrogate G2 = g12, from v43;
- the equality/strictness verdict for the printed literal criterion, from Theorem EQ.

**The literal–mean-square relation.** The printed E path-L2 optimal level and the mean-square optimal level differ strictly except on one explicit noise level per anisotropy ratio. There the adapted mean-square adversary exactly matches the deterministic worst case over noise paths. Even the literal level is then known exactly: G1 = G2 = G_rob.

**Synthesis.** No controller or synthesis statement is made. The original synthesis problem remains UNRESOLVED.

## 5. Process and assurance

- Written exact mathematics only, after v209 was read FIRST and the adopted inputs were read completely.
- Frozen v27–v32 untouched. No v220 file, review or assignment was opened.
- No pinned/frozen/shared edit. No Git, deletion, publication or external model.
- All permanent findings and ZERO quarantines remain: post56, post60, postS126, the self-released v163 assessment, and the protected S242 window. HELD_C889 was never opened.
- No formal, kernel, human, configured-family, executable or novelty acceptance.
- Same18, HOLD v2, science cutoff 2026-10-27T11:05:38-07:00 and delivery deadline 12:35:38 apply. This is not an early final park.

**END OF COMPLETE v44.**
