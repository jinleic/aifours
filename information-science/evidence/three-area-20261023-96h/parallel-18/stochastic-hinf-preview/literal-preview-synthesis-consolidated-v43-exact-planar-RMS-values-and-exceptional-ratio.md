# Exact mean-square values (the descriptor's L2 surrogate) for planar rotation noise with an eigen-aligned single input, and strictness everywhere except one explicit noise level

Owner **InfoHinfPreview-2 / info-3**. Clock observed with `/bin/date` immediately before writing: **Tue Oct 27 08:03:02 PDT 2026**.

**Status.**

- NEW COMPLETE WRITTEN OWNER-CANDIDATE, written as a separate successor. Author-written and unreviewed; not adopted; no gate.
- Value side only, under v209 (`1ec52034…`).
- All-variable, source-fixed conventional proofs. No machine-checked identity.
- No chosen numeric probe.
- No scientific interpreter, Eval, calculator, CAS, program, enumeration, solver or replay. No new GO.
- Frozen v27–v32 untouched. No v220 file, live review or assignment read.

## 0. Setting and statements

**Class PR-1E.** Planar class PR of v39 with:

- A0 = σJ with σ ≠ 0;
- Ā = μI with μ < 0;
- a single input column c ≠ 0, taken WLOG as c > 0 times e_1 by a rotation (v41 §0);
- an arbitrary output map D0 ∈ R^{q×2} such that e_1 is an EIGENVECTOR of M := D0^T D0. Equivalently M_12 = 0 in the basis (e_1, e_2 = Je_1).

Write x := M_11 (input-direction weight), y := M_22 (orthogonal weight), and

`a := 1/|μ|`, `b := 1/(|μ|+σ^2)`, `r := b/a ∈ (0,1)`, `c_* := (a+b)/2`.

**Theorem EX (exact mean-square value).** For every preview δ ≥ 0,

`G2,∞^2 = c^2 c_* ( c_* x + ((a−b)/2) y )`.

By v31 Proposition G (`4c2a7b9b…`), G2,∞ = g12,∞ for uncontrolled EMS data. So this is also the EXACT value of the descriptor's L2/RMS surrogate on this class. Special cases:

| Case | Data | Exact value |
|---|---|---|
| aligned SISO | M = |g|^2 e_1e_1^T | G2 = c|g| c_* |
| orthogonal SISO | M = |g|^2 e_2e_2^T | G2 = c|g| (c_*(a−b)/2)^{1/2} |
| isotropic output | M = mI | G2^2 = c^2 c_* a m |

**Theorem ST (strictness off one exceptional ratio).** Suppose x + y > 0.

- If y ≤ 2x, the gap is STRICT: G2,∞ < G1,∞ ≤ √2·G2,∞.
- If y > 2x and x/y ≠ r/(1+r), the gap is STRICT.
- If y > 2x and x/y = r/(1+r), then G2,∞ EQUALS the best robust lower bound obtainable from constant-rate rotating noise paths:

  `G2,∞^2 = c^2 a^2 y^2/(4(y − x))`.

  On this exceptional locus, strictness holds iff G_rob exceeds that value. This is a purely DETERMINISTIC worst-case-path question, which this packet does not decide.

**Locus as a noise level.** For a given ratio ρ := x/y ∈ [0, 1/2), the exceptional locus is the single noise level σ^2 = |μ|(1 − 2ρ)/ρ for ρ > 0. There is no exceptional level for ρ = 0, which is the orthogonal case.

**Consistency.**

- v41: SISO has rank-one M, and e_1 is an eigenvector exactly in the aligned (y = 0) and orthogonal (x = 0) cases. Both are strict here, matching v41.
- cp123: the exceptional locus is exactly the obstruction locus recorded there (`1d946a39…`), now with G2 known exactly.

**NOT delivered.**

- G_rob on the exceptional locus.
- Exact G2 when e_1 is not an eigenvector of M.
- Exact G1.
- Multi-input planar data.
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
| v31 | `4c2a7b9b…` | Prop G; G2 < ∞; G2 ≤ G1 |
| v34 | `6fcca986…` | Lemma DS, Theorem R |
| v39 | `4f1903b3…` with erratum `1dbf820a…` | identity item 1 |
| v41 | `913fd056…` | Lemma F, Gmax ≤ c c_*, rotating-path DC gain |

**Separation.**

- The lower bound uses an explicit ADVERSARY INPUT strategy, the input feedback w = λ Re X. It is not a control, not a selected control and not a changed output.
- The upper bound uses the v39/v41 kernel identities.
- No storage function, dissipation inequality, Riccati/LMI, Gramian certificate, controller, quarantined guidance or RMS source is used.

## 2. Lemma Γ (single-input identity for any output weight)

**Claim.** For every adapted E2 input w,

`E∫ X^T M X = c E∫ w Re(Γ_M X)`, where Γ_M := (a(M_11 + M_22) + b((M_11 − M_22) − 2i M_12))/2.

**Proof.**

- v39 item 1 gives E∫X^T M X = c E∫ w e_1^T 2Ξ(M) X, with 2Ξ(M) = a(tr M/2) I + b M_0.
- Expanding, e_1^T 2Ξ(M) X = a(tr M/2)X_1 + b((M_11 − M_22)X_1/2 + M_12 X_2).
- This equals Re(Γ_M X). ∎

**In class PR-1E.** M_12 = 0, so Γ_M = c_* x + ((a−b)/2) y =: γ_M. This is REAL and > 0 when x + y > 0, because a > b.

## 3. Proof of Theorem EX

**Upper bound.**

- By Lemma Γ and Cauchy–Schwarz, E∫X^T M X ≤ c ||w|| ||Re(γ_M X)|| = c γ_M ||w|| ||y_1||, where y_1 := Re X.
- v41 Step 1 gives ||y_1|| ≤ c c_* ||w|| (Gmax ≤ c c_*).
- Hence G2^2 ≤ c^2 c_* γ_M.

**Lower bound (explicit adversary input).**

1. **The aligned identity.** For M = e_1e_1^T, γ = c_*, so Lemma Γ gives E∫y_1^2 = c c_* E∫ w y_1 for every E2 input.
2. **The input.** Fix ε > 0 and λ ∈ (0, 1/(c c_*)). Define w := 1_{[0,ε]} + λ y_1 1_{(ε,∞)}, an input-feedback strategy; the linear SDE is well posed.
3. **Finite energy.**
   - The truncation w_T := 1_{[0,ε]} + λ y_1 1_{(ε,T]} is adapted with finite energy.
   - Step 1 applied to w_T gives E∫_0^T y_1^2 ≤ c c_* (P + λ E∫_ε^T y_1^2), where P := E∫_0^ε y_1 ds.
   - So (1 − c c_* λ) E∫_ε^T y_1^2 ≤ c c_* P, uniformly in T. Hence w ∈ E2.
4. **Q blows up.** Let Q := E∫_0^∞ y_1^2 and Q_ε := E∫_0^ε y_1^2. Step 1 gives Q(1 − c c_* λ) = c c_*(P − λQ_ε).
   - On [0, ε], E y_1(s) = c ∫_0^s e^{(μ − σ^2/2)(s−s')} ds' ≥ c s e^{−(|μ|+σ^2/2)ε}, so P ≥ c ε^2 e^{−(|μ|+σ^2/2)ε}/2.
   - |X_s| ≤ cs gives Q_ε ≤ c^2 ε^3/3.
   - Fix ε so small that P − Q_ε/(c c_*) > 0. Then P − λQ_ε > 0 for all admissible λ, and Q → ∞ as λ ↑ 1/(c c_*).
5. **The ratio.**
   - By Lemma Γ and Step 1, E∫X^T M X = c γ_M E∫ w y_1 = (γ_M/c_*) Q.
   - E∫w^2 = ε + λ^2(Q − Q_ε).
   - Hence E∫X^T M X / E∫w^2 → (γ_M/c_*)(c c_*)^2 = c^2 c_* γ_M as λ ↑ 1/(c c_*).

So G2^2 ≥ c^2 c_* γ_M. ∎

## 4. Proof of Theorem ST

**Robust lower bound.** As in v41 Step 2, now with the vector output, the constant-rate rotating path ℓ_t = κt (Ω := σκ) has the time-invariant kernel e^{μu} D0 R(Ωu) c e_1, whose DC gain is D0(|μ|I − ΩJ)^{−1} c e_1, since (|μ|I − ΩJ)(|μ|I + ΩJ) = (μ^2 + Ω^2)I. With Ω = |μ| tan ψ, ψ ∈ (−π/2, π/2), this equals (c cos ψ/|μ|) D0 R(ψ) e_1, and |D0 R(ψ) e_1|^2 = x cos^2ψ + y sin^2ψ because M is diagonal. So

`G_rob^2 ≥ c^2 a^2 sup_ψ cos^2ψ (x cos^2ψ + y sin^2ψ)`.

Put s := sin^2ψ, and maximize (1−s)(x + (y−x)s) over s ∈ [0,1]:

- the value is x if y ≤ 2x;
- the value is y^2/(4(y−x)) if y > 2x, attained at s* = (y − 2x)/(2(y−x)).

**Comparison with Theorem EX.** After dividing by c^2 a^2, Theorem EX reads

G2^2/(c^2a^2) = ((1+r)/4)((1+r)x + (1−r)y).

**Case y ≤ 2x.** Strictness holds iff 4x > (1+r)^2 x + (1−r^2) y, i.e. (1−r)(3+r) x > (1−r)(1+r) y, i.e. y/x < (3+r)/(1+r). This holds because y ≤ 2x < ((3+r)/(1+r)) x for r < 1 (if x = 0 then y = 0, which is excluded).

**Case y > 2x.** With ρ := x/y ∈ [0, 1/2), strictness holds iff

1 > H(ρ) := (1+r)(1−ρ)((1−r) + (1+r)ρ).

H is a concave quadratic in ρ. Its derivative vanishes at ρ* = r/(1+r) ∈ (0, 1/2), where H(ρ*) = (1+r)·(1/(1+r))·1 = 1. Hence H(ρ) < 1 for ρ ≠ ρ*, which gives STRICT; and at ρ = ρ* the two values coincide.

In every strict case, G_rob > G2,∞, and v34 Theorem R gives G1,∞ > G2,∞. The bound √2 is v27 C1. ∎

## 5. Meaning (value side only)

**Exact evaluation.** This packet gives an EXACT, storage-free evaluation of the mean-square level (the L2 surrogate of the adopted descriptor) for a two-parameter planar family.

**Strictness.** The printed literal level is STRICTLY above it everywhere except on one explicit noise level per anisotropy ratio. There, the remaining question is purely deterministic: do non-uniform noise paths beat uniform rotations?

**Synthesis.** No controller or synthesis statement is made.

## 6. Process and assurance

- Written exact mathematics only, after v209 was read FIRST and the adopted inputs were read completely.
- Frozen v27–v32 untouched. No v220 file, review or assignment was opened.
- No pinned/frozen/shared edit. No Git, deletion, publication or external model.
- All permanent findings and ZERO quarantines remain: post56, post60, postS126, the self-released v163 assessment, and the protected S242 window. HELD_C889 was never opened.
- No formal, kernel, human, configured-family, executable or novelty acceptance.
- Same18, HOLD v2, science cutoff 2026-10-27T11:05:38-07:00 and delivery deadline 12:35:38 apply. This is not an early final park.

**END OF COMPLETE v43.**
