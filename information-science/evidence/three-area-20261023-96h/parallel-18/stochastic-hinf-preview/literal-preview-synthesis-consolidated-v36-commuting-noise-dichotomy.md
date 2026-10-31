# Commuting multiplicative noise: a finite algebraic test that decides when the printed literal gain strictly exceeds the RMS gain

Owner **InfoHinfPreview-2 / info-3**. Clock observed with `/bin/date` immediately before writing: **Tue Oct 27 07:25:05 PDT 2026**.

**Status.**

- NEW COMPLETE WRITTEN OWNER-CANDIDATE, written as a separate successor. Not reviewed, not adopted.
- Value side only, under v209 (`1ec52034…`).
- All-variable, source-fixed conventional proofs. No machine-checked identity.
- Only symbolic choices with explicit existence arguments. No chosen numeric/state/control/noise/boundary/decimal probe.
- No scientific interpreter, Eval, calculator, CAS, program, enumeration, solver or replay. No new GO.
- The frozen v27–v32 bodies (under parent wave v220) are not modified. No v220 file, review or assignment was read.

## 0. Setting and statements

**Setting.** As in v32 Theorem S and v34 Theorem R:

- uncontrolled constant data (A, A0, C, D0): B = B0 = D1 = 0, or equivalently the zero law;
- any input/output dimensions and any D0 rank;
- preview delay δ ≥ 0;
- the original single Brownian motion W with its canonical filtration;
- EMS autonomous part: E|X_t|^2 ≤ M e^{−λt}|x_0|^2.

G1,∞ and G2,∞ are the literal (E path-L2) and RMS gains over all original E2 inputs.

**Additional hypothesis (COMMUTING).** AA0 = A0A. Put Ā := A − A0^2/2, which also commutes with A0.

**Spectral notation.** Over C, write the Jordan–Chevalley form A0 = Σ_j (μ_j P_j + N_j):

- μ_j are the distinct eigenvalues;
- P_j are the spectral projectors;
- N_j := (A0 − μ_j)P_j are nilpotent with N_j^n = 0.

Every P_j and N_j is a polynomial in A0, so it commutes with A, Ā and A0. For j, k ≥ 0 and u ≥ 0 define

`Γ_{j,k}(u) := D0 N_j^k P_j e^{Āu} C`.

This is an entire function of u with Taylor coefficients D0 N_j^k P_j Ā^m C / m!.

**Visibility condition (VIS).** There are j, k ≥ 0 and m ∈ {0, …, n−1} such that

- Re μ_j ≠ 0 or k ≥ 1, and
- D0 N_j^k P_j Ā^m C ≠ 0.

Equivalently, some "bad" Γ_{j,k} is not identically zero on [0, ∞). By Cayley–Hamilton the range of m suffices. VIS is a finite algebraic test on (A, A0, C, D0).

Also put J_im := {j : Re μ_j = 0, μ_j ≠ 0, Γ_{j,0} ≢ 0}, the visible nonzero imaginary noise frequencies.

**Theorem V (commuting dichotomy).** Under COMMUTING, at every preview δ ≥ 0:

- **(a)** If VIS holds, then G_rob = ∞. Hence G2,∞ < G1,∞ ≤ √2·G2,∞: STRICT.
- **(b)** If VIS fails and J_im = ∅, then pathwise T_C w = K_0 ⋆ w(· − δ). Here K_0(u) := Γ_{j_0,0}(u) for the index j_0 with μ_{j_0} = 0, and K_0 := 0 if 0 ∉ spec A0. The kernel K_0 is deterministic and integrable, and G1,∞ = G2,∞ = G_rob = ||T_{K_0}||.
- **(c)** If VIS fails and J_im ≠ ∅, then G_rob ≤ Σ_{j: Re μ_j = 0} ||Γ_{j,0}||_{L1(0,∞)} < ∞. This packet does NOT decide whether G1,∞ = G2,∞ in case (c).

**Corollary V1 (real noise spectrum: COMPLETE dichotomy).** Suppose COMMUTING holds and spec A0 ⊂ R. Then J_im = ∅, so:

`G1,∞ = G2,∞  ⇔  VIS fails  ⇔  the input–output kernel is the deterministic K_0`.

In every other case the printed literal gain is STRICTLY above the RMS gain.

**Corollary V2 (isotropic noise).** Let A0 = σI with σ ≠ 0 real, and A arbitrary. Then VIS holds iff D0 Ā^m C ≠ 0 for some m, i.e. iff the input–output map of (Ā, C, D0) is not identically zero. So, apart from the trivial zero map, every such plant has G2,∞ < G1,∞, at every preview.

**Corollary V3 (nilpotent noise).** Take A = −αI with α > 0, A0 = σ e_1 e_2^T with σ ≠ 0, C = e_2 and D0 = e_1^T. Then N = A0, P = I and μ = 0, and D0 N C = σ ≠ 0, so VIS holds and the gap is STRICT. EMS holds:

- x_2 is the deterministic stable response;
- x_1 = σ∫ e^{−α(t−s)} x_2(s) dW_s has an exponentially decaying second moment.

So strictness does not need any noise eigenvalue with nonzero real part.

**Consistency with earlier packets.**

- **v33 Corollary S3** (scalar, c·d·σ ≠ 0) is the case n = 1 of V1/V2.
- **v34 §4 noise-invisible class.** That class has a deterministic kernel, matching case (b).
- **The rotational example of v34 §0** (A = −αI, A0 = σJ) is commuting with μ = ±iσ and N = 0. VIS fails and J_im = {±iσ}, so it falls under case (c), consistent with v34 leaving it undecided.

**NOT delivered.**

- A decision in case (c).
- Any non-commuting algebraic criterion. There the comparison G_rob vs G2 of v34 remains the only test.
- Exact G1 values.
- Controlled data, a controller or synthesis statement, or an RMS-to-literal transfer. R4 STOPPED; C1–C3 STOPPED.

## 1. Inputs and separation

**Adopted inputs** (read completely this session):

| Input | LF | Pin |
|---|---|---|
| v25 | 348 | `8c381b1f…` |
| v26 | 308 | `6666f555…` |
| parent | 74 | `1f00e0c6…` |

They fix the literal criterion and the uncontrolled descriptor.

**Cited owner packets** (unreviewed):

| Packet | Pin | Used for |
|---|---|---|
| v27 | `af2abd51…` | the √2 upper bound |
| v31 | `4c2a7b9b…` | G2,∞ < ∞ under EMS (Step 0) and G2,∞ ≤ G1,∞ |
| v34 | `6fcca986…` | Lemma DS and Theorem R, including the definitions of T_ℓ, k_ℓ and G_rob |

**Separation.** None of the following is used:

- storage, Riccati/Gramian/LMI, a controller construction, a selected control or a changed output;
- quarantined guidance or the RMS source.

Paths ℓ are noise realizations, not controls.

**Ordinary tools.**

- The Jordan–Chevalley/spectral decomposition.
- Taylor expansion of matrix exponentials.
- Cauchy–Schwarz; Gaussian moments.
- Averages of trigonometric polynomials.
- Young's convolution inequality; unimodular multipliers being isometries of L2.

## 2. Lemma CK — the commuting kernel

Under COMMUTING, the Doss–Sussmann generator of v34 is

`e^{−A0ℓ(t)}(A − A0^2/2)e^{A0ℓ(t)} = Ā`,

so Ψ_ℓ(t,s) = e^{Ā(t−s)}. Hence, for every continuous ℓ with ℓ(0) = 0 and s ≤ t,

`k_ℓ(t,s) = D0 e^{A0(ℓ(t)−ℓ(s))} e^{Ā(t−s)} C = Σ_{j,k} e^{μ_j θ} (θ^k/k!) Γ_{j,k}(t−s)`, where θ := ℓ(t) − ℓ(s).

The second form uses e^{A0θ}P_j = e^{μ_jθ} Σ_k θ^k N_j^k P_j/k! and commutation. ∎

## 3. Lemma EP — bounded exponential polynomials

**Claim.** Let f(θ) = Σ_{(μ,k)∈S} c_{μ,k} θ^k e^{μθ}, with S a finite set of distinct pairs and c_{μ,k} ∈ C. Then f is bounded on R iff c_{μ,k} = 0 whenever Re μ ≠ 0 or k ≥ 1.

**Proof.**

1. **"If".** This direction is clear.
2. **Setup for "only if".** Let B be the set of nonzero coefficients with Re μ ≠ 0 or k ≥ 1, and suppose B ≠ ∅.
3. **Case α: B contains a pair with Re μ > 0, or one with Re μ = 0 and k ≥ 1.**
   - Let m+ := max{Re μ : some c_{μ,k} ≠ 0} ≥ 0, and K := max{k : c_{μ,k} ≠ 0, Re μ = m+}.
   - Then m+ > 0 or K ≥ 1.
   - As θ → +∞, e^{−m+θ}θ^{−K} f(θ) = p(θ) + o(1). Here p(θ) := Σ_{Re μ = m+} c_{μ,K} e^{i(Im μ)θ} is a NONZERO trigonometric polynomial with distinct frequencies.
   - Since (1/R)∫_R^{2R}|p|^2 → Σ|c_{μ,K}|^2 > 0 (the cross terms are O(1/R)), |p| ≥ η > 0 at points θ_n → ∞.
   - Hence |f(θ_n)| ≥ (η − o(1)) e^{m+θ_n} θ_n^K → ∞.
4. **Case β: otherwise.** B contains only pairs with Re μ < 0. Apply case α to f(−θ), whose bad pair (−μ, k) has positive real part. ∎

## 4. Proof of Theorem V

### (a) VIS ⇒ G_rob = ∞

**Choice of the bad component.**

- Pick (j_0, k_0) and an entry (a, b) such that the scalar entire function u ↦ e_a^T Γ_{j_0,k_0}(u) e_b is not identically zero, with Re μ_{j_0} ≠ 0 or k_0 ≥ 1.
- Its zeros in [0, ∞) are isolated, so there is u_0 > 0 at which it is nonzero.

**Windows.**

- For 0 < Δ < u_0 put M_Δ := ∫_{u_0}^{u_0+Δ}∫_0^{Δ} e^{Ā(t−s)} ds dt. (The subscript separates it from the EMS constant M.) It is a limit of polynomials in Ā, so it commutes with A0, P_j and N_j.
- By continuity, Δ^{−2} e_a^T D0 N_{j_0}^{k_0} P_{j_0} M_Δ C e_b → e_a^T Γ_{j_0,k_0}(u_0) e_b ≠ 0 as Δ → 0. Fix Δ small with this coefficient nonzero.
- Then, by the expansion of §2 with M_Δ in place of e^{Āu}, the function

  f(θ) := e_a^T D0 e^{A0θ} M_Δ C e_b = Σ_{j,k} e^{μ_jθ}(θ^k/k!) e_a^T D0 N_j^k P_j M_Δ C e_b

  has a nonzero bad coefficient. By Lemma EP, sup_θ |f(θ)| = ∞.

**Path and test functions.** For θ ∈ R let ℓ_θ be continuous on [0, T] with T := δ + u_0 + Δ:

- ℓ_θ = 0 on [0, δ + Δ];
- linear from 0 to θ on [δ + Δ, δ + u_0];
- ℓ_θ = θ on [δ + u_0, T].

Take v := e_b 1_{[0,Δ]} ∈ L2(0, T−δ) and φ := e_a 1_{[δ+u_0, T]}.

**Pairing.** In (T_ℓ v)(t) = ∫_0^t k_ℓ(t,s) v(s−δ) ds, the input acts at s ∈ [δ, δ+Δ] where ℓ_θ = 0. The output window has ℓ_θ = θ, and t − s ≥ u_0 − Δ > 0. By Lemma CK,

`<φ, T_{ℓ_θ} v> = e_a^T D0 e^{A0θ} M_Δ C e_b = f(θ)`.

The window integral of e^{Ā(t−s)} is shift-invariant, so it is M_Δ.

**Conclusion.** ||v|| = ||φ|| = Δ^{1/2}, so ||T_{ℓ_θ}|| ≥ |f(θ)|/Δ, which is unbounded in θ. Hence G_rob = ∞.

**Strictness.** v31 Step 0 gives G2,∞ < ∞, so G_rob > G2,∞, and v34 Theorem R item 2 gives G1,∞ > G2,∞. The upper bound √2·G2,∞ is v27/v34 item 1. ∎(a)

### (b) and (c): VIS fails

**Kernel reduction.** By Lemma CK, every term with Re μ_j ≠ 0 or k ≥ 1 vanishes identically. Hence

`k_ℓ(t,s) = Σ_{j: Re μ_j = 0} e^{μ_j(ℓ(t)−ℓ(s))} Γ_{j,0}(t−s)`.

**Integrability from EMS.** Fix j with Re μ_j = 0.

- By Lemma DS with w = 0 and commuting coefficients, e^{−A0W_t}X_t = e^{Āt}x_0 pathwise. So P_j e^{Āt} x_0 = e^{−A0W_t} P_j X_t.
- |e^{−μ_jW_t}| = 1, and ||e^{−N_jW_t}|| ≤ Σ_{k<n}|W_t|^k ||N_j||^k/k!.
- Cauchy–Schwarz and Gaussian moments give |P_j e^{Āt}x_0| ≤ ||P_j|| Q(t)^{1/2} M^{1/2} e^{−λt/2}|x_0|, with Q a polynomial in t.
- So Γ_{j,0} decays exponentially and lies in L1(0, ∞).

**Case (b).** J_im = ∅, so only the j_0 term with μ_{j_0} = 0 can survive, and k_ℓ(t,s) = K_0(t−s) for every ℓ.

- By Lemma DS, T_C w = K_0 ⋆ w(·−δ) pathwise.
- Pathwise ||T_C w(ω)|| ≤ ||T_{K_0}|| ||w(ω)||, so G1,∞ ≤ ||T_{K_0}||. Squaring and taking expectations gives G2,∞ ≤ ||T_{K_0}||.
- Deterministic inputs give both gains ≥ ||T_{K_0}||, using the supremum over T.
- Hence G1,∞ = G2,∞ = ||T_{K_0}||. Also G_rob = ||T_{K_0}|| because the kernel does not depend on ℓ. ∎(b)

**Case (c).** Each term is U_{j,ℓ} T_{Γ_{j,0}} U_{j,ℓ}^{δ*}, where:

- U_{j,ℓ} multiplies by the unimodular function e^{μ_jℓ(t)};
- U^{δ*}_{j,ℓ} multiplies the delayed input by e^{−μ_jℓ(s)}.

Both are isometries of L2. So ||T_ℓ|| ≤ Σ_j ||T_{Γ_{j,0}}|| ≤ Σ_j ||Γ_{j,0}||_{L1} by Young's inequality, uniformly in ℓ and T. Complexification does not change norms of real kernels. ∎(c)

### Corollaries

- **V1.** spec A0 ⊂ R gives J_im = ∅. Combine (a) and (b); the kernel equals K_0 exactly when VIS fails.
- **V2.** Here P = I, N = 0 and μ = σ ≠ 0, so VIS reads D0 Ā^m C ≠ 0 for some m.
- **V3.** The verification is displayed with the statement in §0. ∎

## 5. Meaning for the original problem (value side only)

**Commuting class.** For uncontrolled constant-data plants with commuting noise and real noise spectrum, the printed E path-L2 criterion and the mean-square criterion have the SAME optimal level ONLY in the degenerate case where noise is invisible in the input–output kernel. In every other such plant, at every preview, the printed literal level is STRICTLY larger. The mean-square replacement is then strictly optimistic.

**Non-commuting data.** The test is v34's G_rob vs G2.

**Imaginary noise spectrum.** Visible imaginary noise frequencies (case (c)) remain the one undecided commuting configuration.

## 6. Process and assurance

- Written exact mathematics only, after v209 was read FIRST and the adopted inputs were read completely.
- The frozen v27–v32 are untouched. Main's wave-v220 notice was received, and no v220 file, live review or assignment was opened.
- No pinned/frozen/shared edit. No Git, deletion, publication or external model.
- All permanent findings and ZERO quarantines remain: post56, post60, postS126, the self-released v163 assessment, and the protected S242 window. HELD_C889 was never opened.
- No formal, kernel, human, configured-family, executable or novelty acceptance.
- Same18, HOLD v2, science cutoff 2026-10-27T11:05:38-07:00 and delivery deadline 12:35:38 apply. This is not an early final park.

**END OF COMPLETE v36.**
