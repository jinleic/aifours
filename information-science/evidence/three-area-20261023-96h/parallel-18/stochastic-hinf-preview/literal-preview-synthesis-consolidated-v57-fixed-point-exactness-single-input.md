# A fixed-point exactness theorem for the mean-square gain of single-input uncontrolled plants (any dimension, no commutation), unifying v43 and v55

Owner **InfoHinfPreview-2 / info-3**. Clock observed with `/bin/date` immediately before writing: **Tue Oct 27 08:50:50 PDT 2026**.

**Pre-pin note.** This text replaces an unhashed first draft of this same file. That draft had an unclear lower-bound step (a garbled sentence and an unjustified "choice of pulse" claim). The lower bound is now proved through the post-pulse energy R below. Disclosed in the next checkpoint.

**Status.**

- NEW COMPLETE WRITTEN OWNER-CANDIDATE, written as a separate successor. Author-written, UNREVIEWED and not adopted.
- This packet is OUTSIDE the v243 narrow exception, which covers only v55 Theorem G items 1–3. It does not modify v55, which stays frozen at `c51562e8…`.
- Value side only, under v209 (`1ec52034…`) and v236 (`062ccf9e…`).
- All-variable, source-fixed conventional proofs. No machine-checked identity.
- No chosen numeric probe.
- No scientific interpreter, Eval, calculator, CAS, program, enumeration, solver or replay. No new GO.
- Frozen v27–v32 untouched; v31 is used through its v220-supported conclusion, with Q-rho, Q-zero and Q1 carried additively (`6d0103ff…`).

## 0. Setting and statements

**Setting.** Uncontrolled constant data with:

- any n and any A, A0, with NO commutation assumption;
- a SINGLE input column c ∈ R^n, so the plant input is c·w̃(t) with w̃(t) = w(t−h);
- canonical one-Brownian filtration;
- EMS for the stochastic flow Φ: E||Φ(u)||^2 ≤ nM e^{−λu}.

For a symmetric M define the second-moment matrix

`Ξ(M) := ∫_0^∞ E[Φ(u)^T M Φ(u)] du`.

It converges absolutely by EMS and is used only as an explicit moment integral inside expectation identities. It is not a certificate for any controller or storage function.

**Lemma I (general identity).** For every adapted E2 plant input w̃ and every symmetric M,

`E∫_0^∞ X^T M X dt = 2 E∫_0^∞ w̃(s) (Ξ(M)c)^T X_s ds`.

**Theorem FX (fixed-point exactness).** Let f ∈ R^n satisfy:

- the fixed-point condition 2Ξ(f f^T) c = κ f for some κ > 0;
- the visibility condition f^T c > 0.

Under the fixed-point condition, f^T c > 0 is equivalent to c^T Ξ(ff^T) c > 0, i.e. to the output y := f^T X not being invisible from c.

Let M be symmetric positive semidefinite with 2Ξ(M)c = γ_M f for some γ_M ≥ 0. Then:

1. G2(M; h)^2 ≤ κ γ_M for every preview h ≥ 0.
2. G2(M; 0)^2 = κ γ_M exactly.
3. In particular, G2(ff^T; 0) = κ.

**Corollary FX1 (the v55 mechanism).** For n = 1, gate I has A = −a, A0 = σ, c and f = d. Then Ξ(d^2) = d^2/q_0, 2Ξ(d^2)c = (2cd/q_0)d and f^T c = dc > 0, so κ = 2cd/q_0. This is the same value as v55 Theorem G. v55 itself stays the frozen object of the v243 exception, and this corollary is not part of that exception.

**Corollary FX2 (recovers v43 at h = 0).** In the planar class PR-1E with input c e_1:

- Lemma I's Ξ equals v39's Ξ, because Φ(u) = e^{μu} R(σW_u).
- For diagonal M = diag(x, y), 2Ξ(M)e_1 = γ_M e_1 with γ_M = c_* x + ((a−b)/2) y.
- So f = e_1 gives κ = c c_*, and M gives the coefficient c γ_M. Hence G2^2 = c^2 c_* γ_M.

**Corollary FX3 (existence of an exactly evaluable output direction).** Suppose c^T Ξ(ff^T) c > 0 for every f ≠ 0 (no invisible output functional). Then there are a unit f* and κ* > 0 with 2Ξ(f* f*^T)c = κ* f* and f*^T c > 0. Hence G2(f*; 0) = κ*.

**NOT delivered.**

- Exact G2 for weights not satisfying the proportionality condition.
- Exact G1.
- h > 0 exact values.
- Multi-input data.
- Controlled data, a controller, synthesis, or an RMS-to-literal transfer. C1–C3 and R4 STOPPED.

## 1. Inputs and separation

**Adopted inputs** (read completely this session):

| Input | LF | Pin |
|---|---|---|
| v25 | 348 | `8c381b1f…` |
| v26 | 308 | `6666f555…` |
| v21/v25/v26 parent | 74 | `1f00e0c6…` |
| v220 parent | 79 | `13fbb1a2…` |

**Parent-supported conclusion.** v31 (G2 < ∞).

**Author candidates** (UNREVIEWED), for the corollaries only:

| Packet | Pin |
|---|---|
| v39 | `4f1903b3…` |
| v43 | `b4e13943…` |
| v55 | `c51562e8…` |

**Separation.** The tools are:

- the variation-of-constants formula X_t = ∫_0^t Φ(t,s) c w̃(s) ds;
- the flow property;
- independence of Φ(t,s) from F_s, and stationarity;
- Fubini/Minkowski and Cauchy–Schwarz;
- an explicit adversary input-feedback strategy;
- for FX3, the standard fact that an even continuous self-map of S^{n−1} with n ≥ 2 has even degree, while the antipodal map has degree (−1)^n.

No storage function, dissipation inequality, Riccati/LMI, Gramian certificate, controller, selected control, changed output, quarantined guidance or RMS source is used.

## 2. Proofs

**Lemma I.**

- **Integrability.** Minkowski with EMS gives (E∫|X|^2)^{1/2} ≤ |c| (nM)^{1/2} (2/λ) ||w̃||, so Fubini applies.
- **Expansion.** Symmetrizing,

  E∫X^T M X = 2E∫∫_{s'<s} w̃(s) w̃(s') c^T [∫_s^∞ Φ(t,s)^T M Φ(t,s') dt] c ds' ds.

- **Conditioning.** Since Φ(t,s') = Φ(t,s)Φ(s,s') and Φ(t,s) is independent of F_s with the law of Φ(t−s), conditioning on F_s turns the bracket into Ξ(M)Φ(s,s').
- **Recognizing the state.** Hence the right side equals 2E∫ w̃(s) c^T Ξ(M) X_s ds. ∎

**Equivalence in the hypothesis.** c^T Ξ(ff^T) c = ∫ E[(f^T Φ(u) c)^2] du ≥ 0. Under the fixed-point condition it equals (κ/2) f^T c. So f^T c > 0 iff the output f^T Φ(·) c is not identically 0.

**Theorem FX, item 1.**

- Lemma I with M = ff^T gives E∫y^2 = κ E∫ w̃ y. By Cauchy–Schwarz, ||y|| ≤ κ ||w̃||.
- For general M, E∫X^T M X = γ_M E∫ w̃ y ≤ κ γ_M ||w̃||^2.

**Theorem FX, item 2 (h = 0).**

1. **Pulse.** For ε > 0 take the deterministic pulse v_0 := 1_{[0,ε]}. Put P := E∫_0^ε v_0 y, Q_ε := E∫_0^ε y^2 and R := E∫_ε^∞ y_{pulse}^2, where y_{pulse} is the output under v_0 alone.
   - Lemma I for v_0 alone gives κP = Q_ε + R.
   - Conditioning on F_ε, R = E[X_ε^T Ξ(ff^T) X_ε].
   - Here X_ε = ∫_0^ε Φ(ε,s) c ds, and X_ε/ε → c in L^2 as ε → 0.
   - Since c^T Ξ(ff^T) c > 0, we get R/ε^2 → c^T Ξ(ff^T) c > 0. Fix ε with R > 0.
2. **Feedback.** For λ ∈ (0, 1/κ), use w := v_0 on [0, ε] and w := λy on (ε, ∞).
   - The truncations at T are E2, because the linear feedback SDE is well posed on finite horizons.
   - Lemma I gives E∫_0^T y^2 ≤ κ(P + λE∫_ε^T y^2), so (1 − κλ) E∫_ε^T y^2 ≤ κP uniformly in T. Hence w ∈ E2.
3. **Blow-up.** With Q := E∫_0^∞ y^2, Lemma I gives Q = κ(P + λ(Q − Q_ε)). Using κP = Q_ε + R,

   Q (1 − κλ) = Q_ε(1 − κλ) + R, i.e. Q = Q_ε + R/(1 − κλ).

   Since R > 0, Q → ∞ as λ ↑ 1/κ.
4. **Ratio.**
   - E∫X^T M X = γ_M E∫ w y = (γ_M/κ) Q, using E∫ w y = Q/κ from Lemma I with ff^T.
   - E∫w^2 = ε + λ^2 (Q − Q_ε).
   - The ratio tends to (γ_M/κ)/λ^2 as Q → ∞, and then to κγ_M as λ ↑ 1/κ.

With item 1, G2(M; 0)^2 = κγ_M. Item 3 is the case M = ff^T, where γ = κ. ∎

**Corollary FX3.**

- Put T(f) := 2Ξ(ff^T)c, which is even and homogeneous of degree 2.
- On the unit sphere, c^T T(f) = 2 c^T Ξ(ff^T) c > 0, so T(f) ≠ 0.
- Hence g(f) := T(f)/|T(f)| is a continuous even self-map of S^{n−1}.
- For n ≥ 2, if g had no fixed point, the straight-line homotopy from g to the antipodal map would avoid 0. Then deg g = (−1)^n would be odd, contradicting evenness. So g has a fixed point f*: T(f*) = κ* f* with κ* = |T(f*)| > 0.
- Then f*^T c = c^T T(f*)/κ* > 0.
- For n = 1 take f* = sign(c).
- Theorem FX item 3 applies. ∎

## 3. Meaning (value side only)

**The common mechanism.** The exact mean-square values found so far — scalar gate I (v55) and the eigen-aligned planar class (v43) — are instances of one mechanism. A fixed point of the quadratic map f ↦ 2Ξ(ff^T)c lets the critical adversary feedback attain the Cauchy–Schwarz bound of the general energy identity.

**Generality.** Every single-input uncontrolled EMS plant without invisible output functionals has at least one output direction whose mean-square gain is exactly computable.

**Synthesis.** No controller or synthesis statement is made.

## 4. Process and assurance

- Written exact mathematics only, after v209, v236, v240 and v243 were read and the adopted inputs and the v220 parent were read completely.
- Frozen v27–v32 and v55 untouched.
- No pinned/frozen/shared edit. No Git, deletion, publication or external model.
- All permanent findings and ZERO quarantines remain: post56, post60, postS126, the self-released v163 assessment, and the protected S242 window. HELD_C889 was never opened.
- No formal, kernel, human, configured-family, executable or novelty acceptance.
- Same18, HOLD v2, science cutoff 2026-10-27T11:05:38-07:00 and delivery deadline 12:35:38 apply. This is not round closeout.

**END OF COMPLETE v57.**
