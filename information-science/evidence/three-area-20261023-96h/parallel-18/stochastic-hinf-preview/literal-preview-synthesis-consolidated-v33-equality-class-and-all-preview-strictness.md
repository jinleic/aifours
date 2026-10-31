# When the printed gain equals the RMS gain, and strictness for every scalar noisy plant at EVERY preview h

Owner **InfoHinfPreview-2 / info-3**. Clock observed with `/bin/date` immediately before writing: **Tue Oct 27 07:08:38 PDT 2026**.

**Status.** NEW COMPLETE WRITTEN OWNER-CANDIDATE. Not reviewed, not adopted. Value side only, under v209 (`1ec52034…`).

- All-variable, source-fixed conventional proofs.
- No machine-checked identity.
- No chosen numeric/state/control/noise/boundary/decimal probe; only symbolic existence.
- No scientific interpreter, Eval, calculator, CAS, program, enumeration, solver or replay; no new GO.

## 0. Statements

Setting as in v32 Theorem S:

- uncontrolled constant data (A, A0, C, D0), meaning B = B0 = D1 = 0 or the zero law;
- any D0 rank;
- any h ≥ 0;
- canonical one-Brownian filtration;
- EMS autonomous part.

Write Φ(t,σ) for the stochastic flow of dY = AY dt + A0Y dW. Define two subspaces:

- R, the smallest subspace containing range C that is invariant under both A and A0;
- N, the largest subspace contained in ker D0 that is invariant under both A and A0.

**Proposition E (exact equality class).** Suppose A0 R ⊆ N, i.e. the noise only pushes reachable states into a jointly invariant unobserved subspace. Then:

- for every original input, the output is pathwise the DETERMINISTIC preview response T_det w;
- T_det w(t) := D0 ∫_0^t e^{A(t−σ)} C w(σ−h) dσ;
- therefore G1,∞ = G2,∞ = ||T_det||_{L2→L2} < ∞.

This includes noise-free plants (A0 = 0) and noise that is invisible to the output. It agrees with v32 Theorem S, item 2.

**Corollary S3 (scalar plants, EVERY preview h ≥ 0, strict).** Let n = 1:

- dX = (aX + c w(t−h))dt + σX dW, z = dX;
- real a, c, d, σ with c·d·σ ≠ 0;
- EMS, i.e. 2a + σ^2 < 0.

Then G2,∞ < G1,∞ ≤ √2·G2,∞ for EVERY h ≥ 0.

This extends the strict gap of v32 Corollary S1 beyond the gate-I convention h = 0, and beyond positive coefficients. It does not need the value of G2,∞.

**Corollary S4 (general sufficient condition for strictness).** Suppose some deterministic, compactly supported input w_1 has an essentially unbounded output path norm: P(||T_C w_1|| > K) > 0 for every finite K. Then G1,∞ > G2,∞.

**Dichotomy for scalar plants.** Scalar plants with c·d = 0 have zero gains. Scalar plants with σ = 0 are deterministic and fall under Proposition E. So for scalar uncontrolled EMS plants:

**G1,∞ = G2,∞ IF AND ONLY IF c·d·σ = 0.**

**NOT delivered:**

- a full multidimensional characterization; skew/rotational noise may go either way, and this is OPEN;
- an exact G1 value;
- any controlled-data, controller or synthesis statement;
- any RMS-to-literal transfer (R4 STOPPED).

## 1. Inputs and separation

**Adopted inputs** (read completely this session):

| Source | LF | Pin |
|---|---|---|
| v25 | 348 | `8c381b1f…` |
| v26 | 308 | `6666f555…` |
| parent | 74 | `1f00e0c6…` |

UC-ALL/UC-INF fixes what G1 is on uncontrolled data.

**Owner packets cited** (unreviewed; complete proofs in each): v27 (`af2abd51…`), v31 (`4c2a7b9b…`) and v32 (`2cdf4de9…`), Theorem S.

**Separation.**

- No storage, Riccati/Gramian/LMI, controller construction, selected control or changed output.
- No quarantined guidance and no RMS source.
- The objects R and N are plant subspaces used only to describe pathwise outputs; they are not a control construction.

## 2. Proof of Proposition E

1. **Pathwise response.** Drift-only forcing gives the pathwise variation-of-constants formula X_t = ∫_0^t Φ(t,σ) C w(σ−h) dσ.
2. **Fix σ and ξ.** Put Y_t := Φ(t,σ)Cξ and Ȳ_t := e^{A(t−σ)}Cξ for t ≥ σ.
   - Y stays in R, because R contains range C and is invariant under A and A0.
   - D := Y − Ȳ solves dD = AD dt + A0Y dW with D_σ = 0.
   - The integrand A0Y lies in A0R ⊆ N, and N is A-invariant.
3. **D stays in N.**
   - Let P be the orthogonal projection onto N^⊥.
   - The component PD satisfies d(PD) = PA(PD) dt. Here PAD = PA(PD) because A maps N into N, and P(A0Y) = 0.
   - Since PD_σ = 0, uniqueness gives PD ≡ 0.
4. **Kernel identity.** Hence D0D = 0, because N ⊆ ker D0. So D0Φ(t,σ)Cξ = D0 e^{A(t−σ)}Cξ for all t ≥ σ, a.s.
5. **All σ at once.** Φ is a.s. jointly continuous in (t,σ). Rational σ and a basis of ξ give one a.s. event for all σ. Integrating in σ yields T_C w = T_det w pathwise.
6. **Finiteness.** EMS implies E Y_t = e^{A(t−σ)}Y_σ → 0 for every deterministic start. So A is Hurwitz and T_det is bounded on L2.
7. **Pathwise bound.** Pathwise ||T_C w|| ≤ ||T_det|| ||w||.
8. **Equality of gains.**
   - Deterministic inputs give N1 = RMS = deterministic norms, so G2,∞ ≥ ||T_det|| and G1,∞ ≥ ||T_det||.
   - The pathwise bound gives E||T_Cw||^2 ≤ ||T_det||^2 E||w||^2 and E||T_Cw|| ≤ ||T_det|| E||w||.
   - Hence G1,∞ = G2,∞ = ||T_det||. ∎

## 3. Proof of Corollary S4

1. Since EMS holds, G2,∞ < ∞ (v31 Step 0).
2. Take K := G2,∞ ||w_1||, a finite deterministic constant. Then P(||T_C w_1|| > G2,∞||w_1||) > 0.
3. The norm on [0, τ_1] increases to the full norm, so some finite τ_1 gives (AHEAD) of v32.
4. v32 Theorem S then gives the strict inequality. The upper bound √2 is v27 Corollary C1. ∎

## 4. Proof of Corollary S3

1. **Input.** Take w_1 := 1_{[0,1]}, deterministic, with Y_1 = 1.
2. **State at time 1 + h.** The scalar flow is Φ(t,s) = exp((a − σ^2/2)(t−s) + σ(W_t − W_s)) > 0. Hence

   X_{1+h} = c ∫_h^{1+h} Φ(1+h, s) ds,

   which has the sign of c and is nonzero a.s. So P(|X_{1+h}| ≥ η) > 0 for some symbolic η > 0.
3. **Free evolution.** For t ≥ 1 + h the input forcing has ended, so X_t = X_{1+h}·E_t with

   E_t^2 = exp(2(a − σ^2/2)(t − 1 − h) + 2σ(W_t − W_{1+h})),

   independent of F_{1+h}.
4. **Large excursion.** For every symbolic K', the event {σ(W_t − W_{1+h}) ≥ K' for all t ∈ [3/2+h, 2+h]} has positive probability. This holds for either sign of σ, by Brownian path-event positivity. On it,

   ∫_{1+h}^{2+h} E_t^2 dt ≥ (1/2) exp(−2|a − σ^2/2| + 2K').
5. **Unboundedness.** Independence gives P(d^2 ∫ X^2 > K'') > 0 for every K''. So the output path norm is essentially unbounded.
6. **Conclusion.** Corollary S4 applies.
7. **The c·d·σ = 0 cases.**
   - If c = 0 or d = 0, then T_C = 0 and both gains vanish.
   - If σ = 0, then A0 = 0 ⊆ N trivially, and Proposition E gives equality. ∎

## 5. Boundaries and remaining

**Multidimensional characterization is open.** Two conditions are known and they are not complements of each other:

- equality follows from noise-invisibility, A0R ⊆ N;
- strictness follows from essentially unbounded pathwise output.

The gap between them includes rotational noise, which preserves norms and changes only direction. That is not settled.

**Other open items.**

- The exact G1 value.
- Controlled data.
- The original synthesis problem (common causal/stationary controller, internal EMS) remains UNRESOLVED.
- C1–C3 remain STOPPED, and R4 is not used.

## 6. Process and assurance

- **Method.** Written exact mathematics only, done after v209 was read FIRST and the adopted inputs were read completely.
- **No changes outside the root.** No pinned, frozen or shared file was edited. No Git, deletion, publication or external model was used.
- **Retained.** All permanent findings and all ZERO quarantines remain: post56, post60, postS126, the self-released v163 assessment, the protected S242 window, and HELD_C889 (never opened).
- **No acceptance claimed.** This is not formal, kernel, human, configured-family, executable or novelty acceptance.
- **Unchanged constraints.** Same18, HOLD v2, science cutoff 2026-10-27T11:05:38-07:00 and delivery deadline 12:35:38. This is not an early final park.

**END OF COMPLETE v33.**
