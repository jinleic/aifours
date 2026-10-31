# The printed literal gain EQUALS the RMS gain iff RMS is an almost-sure pathwise bound — and gate I has a STRICT gap

Owner **InfoHinfPreview-2 / info-3**. Clock observed with `/bin/date` immediately before writing: **Tue Oct 27 07:03:06 PDT 2026**.

**Status.** NEW COMPLETE WRITTEN OWNER-CANDIDATE. Not reviewed or adopted.

- All-variable, source-fixed conventional proofs only.
- No machine-checked identity.
- No chosen numeric/state/control/noise/boundary/decimal probe. Every quantity below is either universally quantified or chosen symbolically by an explicit existence argument.
- No scientific interpreter, Eval, calculator, CAS, program, enumeration, solver or replay; no new GO.
- Value side only, under v209 (`1ec52034…`).

## 0. Statements

**Setting.**

- Canonical one-Brownian filtration.
- Constant data (A, A0, C, D0), any D0 rank, any h ≥ 0.
- The plant is uncontrolled: B = B0 = D1 = 0, or equivalently the zero law.
- The autonomous part is EMS: E|X_t|^2 ≤ M e^{−λt}|x_0|^2 for every deterministic x_0.
- On infinity, G1,∞ and G2,∞ are the literal and RMS gains over ALL original E2 inputs. G2,∞ is finite by v31 Step 0.

**Theorem S (characterization).** The following are equivalent:

1. G1,∞ = G2,∞;
2. RMS is an almost-sure pathwise gain: ||T_C w|| ≤ G2,∞·||w|| a.s. for every original E2 input w;
3. condition (AHEAD) fails, where (AHEAD) says: there are a compactly supported E2 input w_1, a deterministic time τ_1 and the event A := {∫_0^{τ_1}|T_C w_1|^2 > G2,∞^2 ∫|w_1|^2} ∈ F_{τ_1} with P(A) > 0.

Whenever (AHEAD) holds, G2,∞ < G1,∞ ≤ √2·G2,∞. The upper bound is v27 Corollary C1.

**Corollary S1 (gate I: strict gap; CONDITIONAL on adopted gate I).**

- **Family.** Every plant dX = (−aX + cw)dt + σX dW, z = dX, with h = 0, a, c, d, σ > 0 and q0 = 2a − σ^2 > 0.
- **Hypothesis check.** The family satisfies (AHEAD).
- **Conclusion.** `γ* = G2,∞ < G1,∞ ≤ √2·γ*`.
- **Consequence.** For these plants the printed literal optimal level strictly exceeds the mean-square optimal level. The controller is irrelevant here: the plant is uncontrolled, so every law gives the same response. The mean-square replacement therefore gives a STRICTLY optimistic attenuation level. This is an exact original-scope inequivalence of optimal VALUES, not only of definitions.

**Corollary S2 (descriptor non-exactness at the supremum level).**

- **Gate I, on infinity:** sup_T kappa_risk = G1,∞ > G2,∞ = g12,∞ (by v31 Proposition G). The left inequality of v27/v30 (g12 ≤ kappa_risk) is therefore strict even AFTER the supremum over duals.
- **Interpretation:** the adapted quotient nu cannot be replaced exactly by any L2 or BMO surrogate in general. This upgrades v29 Proposition O from a single r to the descriptor value.

**NOT delivered.**

- The exact value of G1 for gate I. It lies in (γ*, √2γ*].
- Sharpness of √2.
- Any controlled-data analog.
- A controller, internal-EMS synthesis or RMS-to-literal transfer. R4 stays STOPPED.

## 1. Inputs and separation

**Adopted inputs** (read completely this session):

| Source | LF | Pin |
|---|---|---|
| v25 | 348 | `8c381b1f…` |
| v26 | 308 | `6666f555…` |
| v21/v25/v26 parent record | 74 | `1f00e0c6…` |

What is used from them:

- adopted UC-ALL/UC-INF, fixing what G1 is on uncontrolled data;
- gate-I G2,∞ = γ*, used ONLY in Corollary S1.

**Owner packets cited** (unreviewed; complete proofs displayed in each):

| Packet | Pin | What is cited |
|---|---|---|
| v27 | `af2abd51…` | Corollary C1 upper bound |
| v31 | `4c2a7b9b…` | Step 0 finiteness; the block-concatenation estimates of its Proposition G proof (Steps 3–6); G2,∞ ≤ G1,∞ |

**Separation.** This packet does not use:

- a storage function;
- a Riccati, Gramian or LMI argument;
- a controller construction;
- a selected control or changed output;
- quarantined guidance;
- the RMS source.

Every construction below is an INPUT strategy of the adversary on an uncontrolled plant.

**Ordinary tools.**

- Independent and stationary Brownian increments, and positivity of Brownian probabilities of open path events.
- Time-shift and strong-uniqueness identification of responses.
- The EMS transition bound for F_σ-measurable initial states.
- Conditional Jensen; the i.i.d. L1 law of large numbers; |√p − √q| ≤ √|p − q|.
- The triangle inequality in R ⊕ L2.

## 2. Lemma 1 — one-path selective dilution value

Fix 0 < ρ < γ, Y > 0 and 0 ≤ Z ≤ γ^2 Y. Put ε(ρ) := max( (γ^2 − ρ^2)^{1/2}, (γ^2 − ρ^2)/γ ). Choose

`y* := max(0, (ρ^4 Y − γ^2 Z)/(ρ^2(γ^2 − ρ^2)))`.

**Claim.** (Z + ρ^2 y*)^{1/2} − γ(Y + y*)^{1/2} ≥ −ε(ρ) Y^{1/2}. Moreover y* ≤ ρ^2 Y/(γ^2 − ρ^2).

**Proof.**

1. **Case ρ^4 Y ≥ γ^2 Z.** Direct substitution gives
   - Y + y* = γ^2(ρ^2Y − Z)/(ρ^2(γ^2 − ρ^2));
   - Z + ρ^2 y* = ρ^2(ρ^2Y − Z)/(γ^2 − ρ^2).

   Here ρ^2 Y ≥ Z, since Z ≤ ρ^4Y/γ^2 ≤ ρ^2 Y. The difference is

   −((ρ^2Y − Z)(γ^2 − ρ^2))^{1/2}/ρ ≥ −(ρ^2 Y(γ^2−ρ^2))^{1/2}/ρ = −(γ^2 − ρ^2)^{1/2} Y^{1/2}.

2. **Case ρ^4 Y < γ^2 Z.** Then y* = 0, and Z^{1/2} > (ρ^2/γ) Y^{1/2}. So the value is Z^{1/2} − γY^{1/2} > −((γ^2 − ρ^2)/γ) Y^{1/2}.

No concavity claim is needed: only the displayed choice y* is evaluated. ε(ρ) → 0 as ρ ↑ γ. ∎

## 3. Lemma 2 — concentrated dilution blocks

Fix ρ < G2,∞ =: γ. By v31 Steps 2 and 4, there are:

- a compactly supported E2 input v on [0, T_0];
- a window length τ_b ≥ T_0 + h;

with m_Y := E||v||^2 > 0 and m_X := E||T_C v 1_{[0,τ_b]}||^2 ≥ ρ^2 m_Y.

**Block train.** For a deterministic start t_0, a gap τ ≥ max(τ_b, T_0 + h + 1) (the gap condition of v31 Step 3), an integer n ≥ 1 and an F_{t_0}-measurable scale ϑ ≥ 0, let

`u := Σ_{k<n} ϑ·θ_{t_0+kτ} v`.

Each shifted copy is the SAME functional of the increments after t_0 + kτ. The copies' supports overlap at most at endpoints, because τ > T_0. The train u is progressive. The letter ϑ is used so that it is not confused with the EMS rate λ.

**Two estimates.** Let a ≥ 0 and Y_0 > 0 be F_{t_0}-measurable. Put ϑ^2 := y/(n m_Y) for an F_{t_0}-measurable y ≥ 0. Then:

- (i) **Input side.** E[(Y_0 + ||u||^2)^{1/2} | F_{t_0}] ≤ (Y_0 + y)^{1/2}. This is conditional Jensen, since E[||u||^2 | F_{t_0}] = ϑ^2 n m_Y = y.
- (ii) **Output side.** With R := ||T_C u 1_{[t_0, t_0+nτ)}||,

  `E[(a + R^2)^{1/2} | F_{t_0}] ≥ (a + ρ^2 y)^{1/2} − (y/m_Y)^{1/2}·e_{n,τ}`.

  Here e_{n,τ} := (E|S_n/n − m_X(τ)|)^{1/2} + δ_τ, which is deterministic and tends to 0 as τ → ∞ followed by n → ∞. S_n is a sum of n i.i.d. copies of the block output energy on windows of length τ, m_X(τ) ≥ m_X is its mean, and δ_τ is the EMS cross-tail constant of v31 Step 5.

**Proof of (ii).**

1. **Split the output.** On the train's windows, the output equals ϑ times the main block outputs plus ϑ times the cross-tails b_k (v31 Step 5).
2. **Triangle inequality.** In R ⊕ L2,

   (a + R^2)^{1/2} ≥ (a + ϑ^2 S_n)^{1/2} − ϑ(Σ||b_k||^2)^{1/2}.
3. **Square-root perturbation.** (a + ϑ^2S_n)^{1/2} ≥ (a + ϑ^2 n m_X(τ))^{1/2} − ϑ|S_n − n m_X(τ)|^{1/2}.
4. **Condition on F_{t_0}.** S_n and b_k are built from increments after t_0, hence independent of F_{t_0}. Conditional Jensen and Cauchy–Schwarz bound the error by ϑ n^{1/2}[(E|S_n/n − m_X(τ)|)^{1/2} + δ_τ], which equals (y/m_Y)^{1/2} e_{n,τ}.
5. **Main term.** ϑ^2 n m_X(τ) = y·m_X(τ)/m_Y ≥ ρ^2 y.
6. **Limits.** The L1 law of large numbers applies because E X < ∞. δ_τ → 0 by v31. ∎

## 4. Proof of Theorem S

The equivalence is proved as the cycle (1) ⇒ (3) ⇒ (2) ⇒ (1).

### (3) ⇒ (2), by contraposition

Suppose (2) fails. Then some E2 input w has P(||T_C w|| > G2,∞||w||) > 0.

- Truncate w to compact support. Truncation converges in L2, and by v31 Step 0 the outputs converge in L2. Along a subsequence both norms converge a.s.
- On the event {||T_C w|| > G2,∞||w||}, the strict inequality therefore holds eventually along that subsequence. So some compactly supported truncation w_1 still has P(||T_C w_1|| > G2,∞||w_1||) > 0.
- The output norm on [0, τ_1] increases to the full norm as τ_1 → ∞, so some finite deterministic τ_1 also works.
- This is (AHEAD), so (3) fails.

### (2) ⇒ (1)

Under (2), N1(T_Cw) ≤ G2,∞ N1(w) for every input, so G1,∞ ≤ G2,∞. Also G2,∞ ≤ G1,∞ by v31 Corollary G1. v31 proves this lower half freshly; the adopted v14 also gives it at the zero law. So G1,∞ = G2,∞.

### (1) ⇒ (3), by contraposition

This is the statement "(AHEAD) ⇒ G1,∞ > G2,∞", proved next.

(For completeness, (2) ⇒ (3) also holds directly. Under (2), for every compactly supported w_1 and every τ_1, Z_1 ≤ ||T_C w_1||^2 ≤ G2,∞^2 Y_1 a.s., so (AHEAD) fails.)

### (AHEAD) ⇒ G1,∞ > G2,∞

**Setup.** Write γ := G2,∞, Y_1 := ∫|w_1|^2 and Z_1 := ∫_0^{τ_1}|T_C w_1|^2.

- (AHEAD) forces γ > 0. Indeed P(Z_1 > 0) > 0, so E||T_C w_1||^2 > 0.
- Let w_1 be supported in [0, T_1]. Enlarging τ_1 only enlarges Z_1 and hence A, so WLOG τ_1 ≥ T_1 + h. After τ_1 the phase-1 response is then autonomous.
- Fix ρ < γ and a waiting time T_w. Put t_0 := τ_1 + T_w, and take a block train as in Lemma 2.

**Strategy.**

- Input w_1 on [0, τ_1].
- On A: no further input (STOP).
- On A^c: zero input on [τ_1, t_0], then the block train from t_0, with dilution level y := y*(Z_1, Y_1) from Lemma 1. The level is F_{τ_1}-measurable, so the input is progressive.
- The total input is E2, since y* ≤ ρ^2 Y_1/(γ^2 − ρ^2) and Y_1 is integrable.

**On A.** ||w|| = Y_1^{1/2} and ||T_C w|| ≥ Z_1^{1/2}. Hence ||T_C w|| − γ||w|| ≥ Z_1^{1/2} − γY_1^{1/2} > 0. Set

Π_A := E[1_A(Z_1^{1/2} − γY_1^{1/2})] > 0.

**On A^c.**

1. **Output bound.** The output on [t_0, t_0 + nτ) is the dilution output plus the phase-1 tail z_tail. The triangle inequality in R ⊕ L2 gives

   ||T_C w|| ≥ (Z_1 + R^2)^{1/2} − ||z_tail 1_{[t_0,∞)}||.

2. **Tail.** By EMS, E||z_tail 1_{[t_0,∞)}|| ≤ C_1 e^{−λT_w/2}, where C_1 depends only on w_1 and the data.
3. **Lemma 2.** Use (ii) with a = Z_1 and (i) with Y_0 = Y_1.
4. **Lemma 1.** On A^c we have Z_1 ≤ γ^2Y_1. Conditionally on F_{t_0},

   E[||T_C w|| − γ||w|| | F_{t_0}] ≥ −ε(ρ)Y_1^{1/2} − (y*/m_Y)^{1/2} e_{n,τ} − E[||z_tail|| | F_{t_0}].

5. **Bound on y*.** (y*)^{1/2} ≤ ρ Y_1^{1/2}/(γ^2 − ρ^2)^{1/2}.

**Total.**

`E||T_C w|| − γE||w|| ≥ Π_A − E[Y_1^{1/2}]·[ε(ρ) + ρ e_{n,τ}/((γ^2−ρ^2) m_Y)^{1/2}] − C_1 e^{−λT_w/2}`.

**Choice of parameters.** Choose in this order:

1. ρ close to γ, so that ε(ρ)E[Y_1^{1/2}] < Π_A/3;
2. T_w with C_1 e^{−λT_w/2} < Π_A/3;
3. τ, then n, with the third term below Π_A/3.

The right side is then positive. Hence N1(T_Cw)/N1(w) > γ, so G1,∞ > G2,∞. ∎

## 5. Proof of Corollary S1 (gate I satisfies AHEAD)

1. **Input.** Take w_1 := 1_{[0,1]}, deterministic, so Y_1 = 1. Then X_1 = c∫_0^1 Φ(1,s) ds > 0 a.s., because the scalar flow Φ is positive. Hence P(X_1 ≥ η) > 0 for some symbolic η > 0.
2. **Free decay.** For t ≥ 1, X_t = X_1 E_t with E_t^2 = exp(−(2a+σ^2)(t−1) + 2σ(W_t − W_1)). E_t is independent of F_1.
3. **A large-output event.** For every K, the event {W_t − W_1 ≥ K for all t ∈ [3/2, 2]} has positive probability, by Brownian path positivity. On it,

   ∫_1^2 E_t^2 dt ≥ (1/2)exp(−(2a+σ^2) + 2σK).

   With σ > 0, choose K symbolically so that this exceeds γ*^2/(d^2 η^2).
4. **Conclusion.** With τ_1 = 2 and independence, P(Z_1 > γ*^2) ≥ P(X_1 ≥ η)·P(that event) > 0. This is (AHEAD).

The family is EMS, since d(E X^2)/dt = −q0 E X^2 at zero input. Gate I gives G2,∞ = γ*. Theorem S then gives G1,∞ > γ*, and v27 gives the upper bound √2γ*. No numerical value of η or K is computed: only existence is used. ∎

## 6. Consequences and boundaries

**What the theorem settles.**

- On uncontrolled EMS plants, the literal and RMS gains coincide EXACTLY when the RMS gain is already a pathwise almost-sure bound. That is what happens for noise-free output channels; v15's G1 = G2 family is consistent with this.
- Genuine multiplicative-noise amplification, as in every gate-I plant, makes the printed criterion STRICTLY harder than its mean-square replacement.
- The mechanism is path-selective allocation, which concave square-root (expected path-norm) accounting permits and RMS accounting forbids:
  - stop on ahead paths;
  - dilute behind paths with concentrated near-RMS-optimal blocks.

**Open.**

- The exact value of G1,∞ in (G2,∞, √2·G2,∞].
- Controlled data: the adversary's input strategy faces an infimum over controls inside the quotient, so no claim is made there.
- The original synthesis (common causal/stationary controller, internal EMS, prescribed γ) remains UNRESOLVED. The realization routes C1–C3 stay STOPPED (v209).

**What this packet is not.**

- It is no synthesis statement.
- It does not use the RMS source.
- It does not assert that any controller achieves anything.

## 7. Process and assurance

- Written exact mathematics only, after v209 was read FIRST and the adopted inputs were read completely.
- No pinned, frozen or shared edit; no Git, deletion, publication or external model.
- All permanent findings and ZERO quarantines remain: post56, post60, postS126, the self-released v163 assessment, the protected S242 window, and HELD_C889 (never opened).
- This is not formal, kernel, human, configured-family, executable or novelty acceptance.
- Same18, HOLD v2, science cutoff 2026-10-27T11:05:38-07:00 and delivery deadline 12:35:38 apply. This is not an early final park.

**END OF COMPLETE v32.**
