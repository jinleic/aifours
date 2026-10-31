# Rotation-like noise can still force a STRICT literal-vs-RMS gap: periodic-switching visibility

Owner **InfoHinfPreview-2 / info-3**. Clock observed with `/bin/date` immediately before writing: **Tue Oct 27 07:32:49 PDT 2026**.

**Status.**

- NEW COMPLETE WRITTEN OWNER-CANDIDATE, written as a separate successor. Not reviewed, not adopted.
- Value side only, under v209 (`1ec52034…`).
- All-variable, source-fixed conventional proofs. No machine-checked identity.
- Every example parameter is symbolic and constrained by an exact inequality or an existence argument. No chosen numeric probe.
- No scientific interpreter, Eval, calculator, CAS, program, enumeration, solver or replay. No new GO.
- The frozen v27–v32 are not modified. No v220 file, live review or assignment was read.

## 0. Statements

**Setting.** As in v34/v37:

- uncontrolled constant data (A, A0, C, D0), any commutation, any dimensions;
- preview δ ≥ 0;
- canonical one-Brownian filtration;
- EMS autonomous part.

Put Ā := A − A0^2/2.

**Cycle matrices.** For r ≥ 1, kicks θ_1, …, θ_r ∈ R and durations τ_1, …, τ_r > 0, put

`Π := e^{Āτ_r} e^{A0θ_r} ⋯ e^{Āτ_1} e^{A0θ_1}`.

For an eigenvalue λ of Π, Q_λ is its Riesz spectral projector.

**Periodic-switching visibility (VIS-P).** For some cycle matrix Π there are:

- an eigenvalue λ with |λ| > 1, and
- m_1, m_2 ∈ {0, …, n−1},

such that D0 Ā^{m_2} Q_λ Ā^{m_1} C ≠ 0.

**Theorem P.** VIS-P implies G_rob = ∞. Hence, at every preview δ ≥ 0,

`G2,∞ < G1,∞ ≤ √2·G2,∞`.

**Example E (rotation noise + shear, non-commuting).**

- **Data.** n = 2, A0 = σJ with J = [[0,−1],[1,0]] and σ > 0. Then A0 is diagonalizable with imaginary spectrum ±iσ: rotation-like, the residual class of v37. Ā = −I + K E_12 with E_12 = e_1 e_2^T, and C = D0 = I.
- **Parameters.** Assume K τ > 2 cosh τ for some τ > 0. Such K exists for every τ > 0, for example any K > 2cosh(τ)/τ.
- **EMS.** There is σ_0 > 0 such that, for every 0 < σ < σ_0, the plant dX = (Ā − (σ^2/2)I)X dt + σJX dW is EMS.
- **Conclusion.** For those σ, at every preview: G2,∞ < G1,∞ ≤ √2·G2,∞, STRICTLY.

So rotation-like noise, which can never satisfy the single-kick test VIS-1 of v37, can still produce a strict gap through switching amplification.

**Corollary P1 (commuting consistency).** If AA0 = A0A, then every cycle matrix equals e^{Ā Στ_i} e^{A0 Σθ_i}. Under rotation-like noise and EMS, its visible spectral part has modulus < 1. So VIS-P cannot add anything to v36 in the commuting case, and v36 case (c) stays undecided.

**NOT delivered.**

- A decision for commuting rotation-like noise.
- A decision for non-commuting rotation-like noise without VIS-P.
- Exact gains.
- Controlled data, a controller, synthesis, or an RMS-to-literal transfer. C1–C3 and R4 STOPPED.

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
| v31 | `4c2a7b9b…` | G2,∞ < ∞ and G2,∞ ≤ G1,∞ |
| v34 | `6fcca986…` | Lemma DS, Ψ_ℓ, k_ℓ, G_rob and Theorem R |
| v36 | `4ecfa7c6…` | notation |
| v37 | `00788a15…` | the near-instant ramp estimate (Step 3) and the window technique |

**Separation.**

- No storage, Riccati/Gramian/LMI, controller construction, selected control, changed output, quarantined guidance or RMS source.
- The EMS verification for Example E uses only the linear second-moment ODE of the autonomous plant and continuity of eigenvalues. This is a property of the given plant, not a storage certificate or a gain bound.

**Ordinary tools.**

- The Jordan/Riesz decomposition of a matrix power.
- Cesàro averages of finitely many unimodular exponentials.
- Continuity of eigenvalues.
- Itô's formula for the second moment E[XX^T] of a linear SDE.

## 2. Lemma DEP — bounded discrete exponential polynomials

**Claim.** Let f(N) = Σ_{λ∈S} λ^N p_λ(N) for N ∈ N, where S is a finite set of distinct nonzero complex numbers and p_λ are complex polynomials. If p_λ ≢ 0 for some |λ| > 1, then f is unbounded.

**Proof.**

1. Let R := max{|λ| : p_λ ≢ 0} > 1, and K := max{deg p_λ : |λ| = R}.
2. Then f(N)/(R^N N^K) = q(N) + o(1), with q(N) := Σ_{|λ|=R, deg p_λ=K} lc(p_λ) e^{iNω_λ}. The angles ω_λ are distinct mod 2π because the λ are distinct with the same modulus.
3. The Cesàro mean (1/N)Σ_{n<N}|q(n)|^2 tends to Σ|lc(p_λ)|^2 > 0, because the cross terms average to 0.
4. Hence |q(N_i)| ≥ η > 0 along a sequence N_i → ∞, and |f(N_i)| ≥ (η − o(1)) R^{N_i} → ∞. ∎

## 3. Proof of Theorem P

**Step 1 — a nonzero two-time coefficient.**

- Pick an entry (a, b) with e_a^T D0 Ā^{m_2} Q_λ Ā^{m_1} C e_b ≠ 0.
- H(u_1, u_2) := e_a^T D0 e^{Āu_2} Q_λ e^{Āu_1} C e_b is entire and ≢ 0, so it is nonzero at some u_1*, u_2* > 0 (as in v37 Step 1).
- Fix 0 < Δ < u_1*.

**Step 2 — the path.**

- Input window: s ∈ [δ, δ+Δ] in plant time, with ℓ = 0 there and until t_0 := δ + u_1*.
- Then N cycles. In cycle i, for j = 1, …, r:
  - a near-instant linear ramp of duration ε raises ℓ by θ_j;
  - ℓ then stays constant for time τ_j.
- After the last cycle ends at t_N, ℓ stays constant. The output window is t ∈ [t_N + u_2*, t_N + u_2* + Δ].

**Step 3 — the kernel on these windows.** On a constant level ϑ the generator is e^{−A0ϑ} Ā e^{A0ϑ}, with flow e^{−A0ϑ} e^{Āτ} e^{A0ϑ}. Ramps contribute Ψ_ramp → I as ε → 0, by v37 Step 3: for fixed N there are finitely many ramps and the levels are bounded. Telescoping the conjugations gives, as ε → 0,

`k_ℓ(t,s) = D0 e^{A0ℓ(t)} Ψ(t,s) e^{−A0ℓ(s)} C → D0 e^{Ā(t−t_N)} Π^N e^{Ā(t_0−s)} C`.

**Step 4 — the pairing.** With v := e_b 1_{[0,Δ]} and φ := e_a 1_{output window}, the limit pairing is

`f_Δ(N) := e_a^T D0 L_out Π^N L_in C e_b`,

where

- L_in := ∫_δ^{δ+Δ} e^{Ā(t_0−s)} ds;
- L_out := ∫ over [u_2*, u_2*+Δ] of e^{Āu} du.

**Step 5 — unboundedness.**

- Write Π^N = Σ_{μ ∈ spec Π, μ≠0} μ^N Σ_{k<n} C(N,k) μ^{−k}(Π − μ)^k Q_μ, plus a term from μ = 0 that vanishes once N ≥ n.
- The λ-polynomial of f_Δ has constant-term coefficient e_a^T D0 L_out Q_λ L_in C e_b. Divided by Δ^2, this tends to H(u_1*, u_2*) ≠ 0 as Δ → 0. Fix Δ with it nonzero.
- Lemma DEP gives sup_N |f_Δ(N)| = ∞.
- For each target K, choose N with |f_Δ(N)| ≥ K, then ε small so that the actual pairing is within 1. Then ||T_ℓ|| ≥ (K − 1)/Δ. So G_rob = ∞.

**Step 6 — strictness.** v31 Step 0 gives G2,∞ < ∞. Then v34 Theorem R gives G1,∞ > G2,∞. The upper bound √2·G2,∞ is v27 Corollary C1. ∎

## 4. Verification of Example E

**(i) A cycle with |λ| > 1.**

- Take r = 2, τ_1 = τ_2 = τ, θ_1 = π/(2σ) and θ_2 = −π/(2σ). Then e^{A0θ_1} = J and e^{A0θ_2} = J^T. By Step 2's order,

  Π = e^{Āτ} J^T e^{Āτ} J = e^{Āτ} e^{(J^T Ā J)τ}.

- J^T E_12 J = −E_21, since J^T e_1 = −e_2 and J^T e_2 = e_1 give J^T e_1 e_2^T J = (J^T e_1)(J^T e_2)^T = (−e_2)(e_1)^T. Hence J^T Ā J = −I − K E_21.
- E_12^2 = E_21^2 = 0, so e^{Āτ} = e^{−τ}(I + Kτ E_12) and e^{(J^TĀJ)τ} = e^{−τ}(I − Kτ E_21).
- Since E_12 E_21 = E_11,

  `Π = e^{−2τ} [[1 − K^2τ^2, Kτ], [−Kτ, 1]]`,

  with tr Π = e^{−2τ}(2 − K^2τ^2) and det Π = e^{−4τ}.
- The characteristic polynomial χ(z) = z^2 − (tr Π) z + det Π satisfies

  χ(−1) = 1 + tr Π + det Π = e^{−2τ}((e^{τ} + e^{−τ})^2 − K^2τ^2),

  which is NEGATIVE exactly when Kτ > 2 cosh τ. Since χ(z) → +∞ as z → −∞, there is a real root λ* < −1. It is simple, because χ(−1) < 0 forces two distinct real roots.

**(ii) Visibility.** C = D0 = I, so D0 Q_{λ*} C = Q_{λ*} ≠ 0. This is VIS-P with m_1 = m_2 = 0.

**(iii) EMS for small σ.**

- J^2 = −I, so A = Ā + A0^2/2 = Ā − (σ^2/2)I.
- By Itô's formula, P_t := E[X_t X_t^T] satisfies the linear ODE Ṗ = L_σ(P), where

  L_σ(P) = ĀP + PĀ^T − σ^2 P + σ^2 J P J^T.

- At σ = 0, L_0(P) = ĀP + PĀ^T has spectrum {λ_i + λ_j} = {−2}, because Ā has the double eigenvalue −1. So L_0 is Hurwitz.
- Eigenvalues depend continuously on σ, so L_σ is Hurwitz for 0 < σ < σ_0, for some σ_0 > 0.
- Then E|X_t|^2 = tr P_t ≤ M e^{−λt}|x_0|^2.

**(iv) Conclusion.** The cycle in (i) does not depend on σ, because the kicks are exact quarter-turns. Theorem P applies for every 0 < σ < σ_0. ∎

**Corollary P1.** In the commuting case, Π = e^{ĀΣτ} e^{A0Σθ}. On the visible imaginary components, e^{A0θ} has modulus-one eigenvalues and e^{Āt} decays (v36 §4, integrability from EMS). So every visible eigenvalue has modulus < 1. ∎

## 5. Meaning (value side only)

**Mechanism.** The literal-vs-RMS gap is not tied to the noise amplifying the state directly. Bounded rotation noise acting on a non-normal drift creates path-dependent switching amplification. That amplification is invisible to the mean square, yet it makes the noise-path gain infinite. By v34 Theorem R, the printed E path-L2 optimal level is then STRICTLY above the mean-square level.

**What remains undecided.**

- Commuting rotation-like noise (v36 case (c)).
- Non-commuting rotation-like noise without a visible expanding cycle.

## 6. Process and assurance

- Written exact mathematics only, after v209 was read FIRST and the adopted inputs were read completely.
- The frozen v27–v32 are untouched. No v220 file, review or assignment was opened.
- No pinned/frozen/shared edit. No Git, deletion, publication or external model.
- All permanent findings and ZERO quarantines remain: post56, post60, postS126, the self-released v163 assessment, and the protected S242 window. HELD_C889 was never opened.
- No formal, kernel, human, configured-family, executable or novelty acceptance.
- Same18, HOLD v2, science cutoff 2026-10-27T11:05:38-07:00 and delivery deadline 12:35:38 apply. This is not an early final park.

**END OF COMPLETE v38.**
