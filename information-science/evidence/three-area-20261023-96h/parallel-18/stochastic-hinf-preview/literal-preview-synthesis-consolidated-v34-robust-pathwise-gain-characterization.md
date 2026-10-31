# Complete equality characterization: printed gain = RMS gain IFF the worst-case "noise-path" gain equals the RMS gain

Owner **InfoHinfPreview-2 / info-3**. Clock observed with `/bin/date` immediately before writing: **Tue Oct 27 07:10:44 PDT 2026**.

**Status.**

- NEW COMPLETE WRITTEN OWNER-CANDIDATE. Not reviewed, not adopted.
- Value side only, under v209 (`1ec52034…`).
- All-variable, source-fixed conventional proofs. No machine-checked identity. No chosen numeric/state/control/noise/boundary/decimal probe.
- No scientific interpreter, Eval, calculator, CAS, program, enumeration, solver or replay. No new GO.

## 0. Statement

**Setting.** As in v32 Theorem S:

- uncontrolled constant data (A, A0, C, D0), meaning B = B0 = D1 = 0 or the zero law;
- any D0 rank;
- preview delay δ ≥ 0, written δ to avoid a clash with path names;
- the ORIGINAL single Brownian motion W, with the canonical filtration;
- EMS autonomous part.

**Noise-path operators.** For every continuous path ℓ ∈ C_0([0,T]) (so ℓ(0) = 0), define the deterministic Doss–Sussmann flow:

`Ż = e^{−A0 ℓ(t)}(A − A0^2/2) e^{A0 ℓ(t)} Z`, with solution operator Ψ_ℓ(t,s),

`k_ℓ(t,s) := D0 e^{A0 ℓ(t)} Ψ_ℓ(t,s) e^{−A0 ℓ(s)} C` for s ≤ t,

`(T_ℓ v)(t) := ∫_0^t k_ℓ(t,s) v(s − δ) ds`.

The operator T_ℓ acts on deterministic v ∈ L2(0, T−δ), with output in L2(0,T).

**Robust pathwise gain.** Define

`G_rob := sup_{T>δ} sup_{ℓ∈C_0([0,T])} ||T_ℓ||_{L2→L2} ∈ [0, ∞]`.

**Theorem R.**

1. G2,∞ ≤ G1,∞ ≤ min(√2·G2,∞, G_rob).
2. **G1,∞ = G2,∞ IF AND ONLY IF G_rob = G2,∞.** Otherwise G2,∞ < G1,∞, so the inequality is STRICT.

So whether the printed literal gain and the mean-square gain coincide is decided by a DETERMINISTIC robust-control comparison: does the worst-case gain over noise realizations treated as continuous paths exceed the RMS average? On the noise-invisible class (v33 Proposition E) G_rob = G2 holds, which gives equality. Gate I (v32) and every scalar plant with c·d·σ ≠ 0 (v33) have G_rob = ∞, which gives strictness. Norm-preserving rotational noise is now decided by the same comparison. Example: A = −αI and A0 = σJ with J the 2×2 rotation generator, input on and output from the first coordinate, and μ := −α + σ^2/2 < 0. There G_rob ≥ 1/|μ| (the constant path ℓ ≡ 0). Whether 1/|μ| exceeds G2,∞ is a deterministic comparison; this packet does not evaluate it.

**NOT delivered:**

- an evaluation of G_rob or G2 for specific data;
- an exact G1;
- any controlled-data, controller or synthesis statement;
- any RMS-to-literal transfer (R4 STOPPED).

## 1. Inputs and separation

**Adopted inputs** (read completely this session):

| Input | LF | Pin |
|---|---|---|
| v25 | 348 | `8c381b1f…` |
| v26 | 308 | `6666f555…` |
| parent | 74 | `1f00e0c6…` |

**Cited owner packets** (unreviewed):

| Packet | Pin | Used for |
|---|---|---|
| v27 | `af2abd51…` | the √2 upper bound |
| v31 | `4c2a7b9b…` | finiteness and the G2 ≤ G1 lower bound |
| v32 | `2cdf4de9…` | Theorem S |
| v33 | `3083dc88…` | context only |

**Separation.** The following are not used:

- storage, Riccati/Gramian/LMI, a controller construction, a selected control or a changed output;
- quarantined guidance or the RMS source.

The paths ℓ are noise realizations of the plant's own Brownian motion. They are not controls and play no role in any controller.

**Ordinary tools.**

- Itô's formula for f(W) = e^{A0 W}. This is legitimate because A0W_t commutes with itself.
- Continuous dependence of linear ODE solutions on a coefficient matrix that is continuous in the sup norm.
- Positivity of Wiener measure on sup-norm tubes around continuous paths. This is the elementary support property: approximate by a Cameron–Martin path, use the equivalence of measures, and use P(sup|W| < η) > 0.
- Dominated convergence.

## 2. Lemma DS — pathwise representation

**Claim.** For every original input w, a.s.,

`T_C w = T_{W(ω)} w(ω)`,

meaning the actual output equals the noise-path operator evaluated at the realized Brownian path, applied pathwise.

**Proof.**

1. **Ansatz.** Put X_t = e^{A0W_t} Z_t, where Z has absolutely continuous paths. Itô's formula gives

   d(e^{A0W}) = A0 e^{A0W} dW + (1/2)A0^2 e^{A0W} dt.

2. **Product rule.** Hence dX = A0X dW + (1/2)A0^2 X dt + e^{A0W} Ż dt.
3. **Matching coefficients.** X solves the plant equation dX = (AX + Cw(t−δ))dt + A0X dW exactly when

   Ż = e^{−A0W_t}(A − A0^2/2) e^{A0W_t} Z + e^{−A0W_t} C w(t−δ).

4. **Pathwise solution.** For each ω this is a linear ODE whose coefficient is continuous in t. Its pathwise solution is given by Ψ_{W(ω)} and the variation-of-constants formula.
5. **Identification.** The resulting X is a strong solution, so strong uniqueness identifies it with the actual response. Multiply by D0. ∎

## 3. Proof of Theorem R

**Item 1.**

- **Pathwise bound by G_rob.** Lemma DS gives, pathwise on [0,T], ||T_C w(ω)|| ≤ ||T_{W(ω)}|| ||w(ω)|| ≤ G_rob ||w(ω)||. Taking expectations gives G1(T) ≤ G_rob. Letting T → ∞ gives G1,∞ ≤ G_rob.
- **The other inequalities.** G1,∞ ≤ √2·G2,∞ is v27 Corollary C1. G2,∞ ≤ G1,∞ is v31 Corollary G1.

**Item 2, "if" direction.** Suppose G_rob = G2,∞. The pathwise bound above, with constant G2,∞, is condition (2) of v32 Theorem S. Hence G1,∞ = G2,∞.

**Item 2, "only if" direction.** Suppose G_rob > G2,∞. Choose ε > 0 and the following symbolically:

- T;
- a path ℓ ∈ C_0([0,T]);
- a deterministic v ∈ L2(0, T−δ) with ||v|| = 1 and ||T_ℓ v|| > G2,∞ + 2ε.

Then argue in three steps.

1. **Continuity.** The map ℓ' ↦ T_{ℓ'} v ∈ L2(0,T) is continuous for the sup norm. The coefficient e^{−A0ℓ'}(A − A0^2/2)e^{A0ℓ'} and the outer factors depend continuously on ℓ' uniformly on [0,T]. Continuous dependence of Ψ follows, and dominated convergence carries it through the Volterra integral. So there is η > 0 with ||T_{ℓ'} v|| > G2,∞ + ε whenever sup_{[0,T]}|ℓ' − ℓ| < η.
2. **Support.** Wiener measure gives the tube {sup_{[0,T]}|W − ℓ| < η} positive probability. With the deterministic input w_1 := v, Lemma DS gives

   P(||T_C w_1 1_{[0,T]}|| > G2,∞ ||w_1||) > 0.

   This is (AHEAD) of v32 with τ_1 = T.
3. **Conclusion.** v32 Theorem S gives G1,∞ > G2,∞. ∎

**Remark.** Item 1 also gives the pathwise upper bound G1,∞ ≤ G_rob. For bounded-amplification noise, such as norm-preserving rotations, this can be sharper than √2·G2,∞. Its value is a deterministic quantity; it is not evaluated here.

## 4. Consistency with earlier packets

**Noise-invisible class (v33 Proposition E).**

- k_ℓ(t,s) = D0 e^{A(t−s)}C for every ℓ, by the same invariant-subspace argument applied to the deterministic flow.
- Hence G_rob = ||T_det|| = G2,∞, and Theorem R gives equality.

**Scalar plants with c·d·σ ≠ 0 (v33 Corollary S3, gate I).**

- For a constant positive slope segment of ℓ, the scalar flow multiplies the state by exp(σ times the slope integral), times a fixed decay factor.
- So G_rob = ∞, and Theorem R gives strictness. This matches v33.

## 5. Boundaries and residual

**Open.**

- Evaluation of G_rob and G2 for multidimensional data.
- Exact G1.
- Controlled data, where the adversary faces a control infimum.
- The original synthesis problem (common causal/stationary controller, internal EMS) remains UNRESOLVED.

**Stopped routes.**

- C1–C3 remain STOPPED.
- R4 is not used.
- No statement is made about controllers.

## 6. Process and assurance

- **Method.** Written exact mathematics only, after v209 was read FIRST and the adopted inputs were read completely.
- **No changes.** No pinned/frozen/shared edit. No Git, deletion, publication or external model.
- **Retained.** All permanent findings and ZERO quarantines remain: post56, post60, postS126, the self-released v163 assessment, and the protected S242 window. HELD_C889 was never opened.
- **No acceptance claimed.** This is not formal, kernel, human, configured-family, executable or novelty acceptance.
- **Unchanged scope.** Same18, HOLD v2, science cutoff 2026-10-27T11:05:38-07:00 and delivery deadline 12:35:38. This is not an early final park.

**END OF COMPLETE v34.**
