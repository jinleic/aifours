# Skew (norm-preserving) noise with isotropic corrected drift in any dimension: invariant-subspace criteria for STRICT literal-vs-RMS gaps, and a co-rotation equality class

Owner **InfoHinfPreview-2 / info-3**. Clock observed with `/bin/date` immediately before writing: **Tue Oct 27 07:48:15 PDT 2026**.

**Status.**

- NEW COMPLETE WRITTEN OWNER-CANDIDATE, written as a separate successor. Author-written and unreviewed; not adopted; no gate.
- Value side only, under v209 (`1ec52034…`).
- All-variable, source-fixed conventional proofs. No machine-checked identity.
- No chosen numeric probe.
- No scientific interpreter, Eval, calculator, CAS, program, enumeration, solver or replay. No new GO.
- Frozen v27–v32 untouched. No v220 file, live review or assignment read.

## 0. Setting and statements

**Class RS (skew noise, isotropic corrected drift).** Uncontrolled constant data with:

- any n ≥ 1;
- A0 real SKEW-symmetric (A0^T = −A0);
- Ā := A − A0^2/2 = μI with μ < 0;
- arbitrary C ∈ R^{n×p} and D0 ∈ R^{q×n};
- preview δ ≥ 0;
- the canonical one-Brownian filtration.

For a symmetric positive semidefinite N, write λ_max(N) for its top eigenvalue and E_top(N) for its top eigenspace. Put M := D0^T D0 (m_1 := λ_max(M)) and κ_1 := λ_max(CC^T) = ||C||^2.

**EMS.** By v34 Lemma DS with commuting data, X_t = e^{A0W_t} e^{μt} x_0, and e^{A0θ} is orthogonal. So |X_t| = e^{μt}|x_0| and the class is EMS.

**Conjugation average.** L(N) := NA0 − A0N maps symmetric matrices to symmetric matrices. It is skew-adjoint for the Frobenius inner product. Over C, L = Σ_ω iω Π_ω, with ω real and Π_ω Frobenius-orthogonal spectral projectors. Define

`Ξ(N) := Σ_ω Π_ω(N)/(2|μ| + ω^2/2) = ∫_0^∞ e^{2μu} E[e^{−A0 a_u} N e^{A0 a_u}] du`, with a_u ~ N(0, u).

Ξ(N) is real symmetric and positive semidefinite, and Ξ(I) = I/(2|μ|).

**Lemma IS (invariant-subspace extremality).** For N ⪰ 0 with λ_max(N) > 0: 2||Ξ(N)|| ≤ λ_max(N)/|μ|. Equality holds IFF E_top(N) contains a nonzero A0-invariant subspace.

**Theorem RS.** For every original E2 input w, with state X and output z = D0X:

1. **(Identity.)** E∫|z|^2 = 2 E∫ <Cw(s), Ξ(M) X_s> ds.
2. **(RMS bound.)** G2,∞^2 ≤ 2||Ξ(M)|| κ_1/|μ|.
3. **(Robust bounds.)** ||D0C||/|μ| ≤ G_rob ≤ √(m_1 κ_1)/|μ|.
4. **(STRICT I.)** If ||D0C||^2 > κ_1 |μ| · 2||Ξ(M)||, then G2,∞ < G1,∞ ≤ √2·G2,∞. In the aligned case ||D0C||^2 = m_1κ_1, the criterion-I inequality holds IFF E_top(M) contains no nonzero A0-invariant subspace (Lemma IS).
5. **(STRICT II.)** If M = mI with m > 0, and E_top(CC^T) contains no nonzero A0-invariant subspace, then the gap is STRICT.
6. **(EQUALITY, co-rotation.)** If M = mI and CC^T = κI with m, κ > 0, then G1,∞ = G2,∞ = G_rob = √(mκ)/|μ|. This holds even though k_ℓ depends on ℓ whenever A0 ≠ 0.

**Corollaries.**

- **RS1 (planar).** n = 2 and A0 = σJ recovers v39 (`4f1903b3…`) items 1–6, as corrected by erratum `1dbf820a…`. The lines E_top(M) for m_1 > m_2 are never σJ-invariant.
- **RS2 (one input or one output channel).** If p = 1 with input column c ≠ 0, then E_top(CC^T) = span(c). If q = 1 with output row d^T ≠ 0, then E_top(M) = span(d). A line span(v) is A0-invariant iff A0 v = 0, because a real eigenvalue of a skew matrix is 0. So, for instance:
  - single output d with A0 d ≠ 0 and aligned data: STRICT;
  - isotropic output, single input c with A0 c ≠ 0: STRICT.
- **RS3 (noise-invisible directions).** If E_top(M) ∩ ker A0 ≠ {0}, that intersection contains an A0-invariant line. By Lemma IS, the criterion-I inequality then FAILS in the aligned case and item 4 gives no conclusion. This is consistent with v33/v36 equality for noise-invisible kernels; no equality claim is made here.

**NOT delivered.**

- A decision when criteria I/II fail and the data are not bi-isotropic.
- Non-isotropic corrected drift (Ā ≠ μI) with skew noise. There the switching mechanism of v38 may also act.
- Exact G1.
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
| v31 | `4c2a7b9b…` | G2 < ∞; G2 ≤ G1 |
| v34 | `6fcca986…` | Lemma DS, G_rob, Theorem R |
| v36 | `4ecfa7c6…` | Lemma CK |
| v39 | `4f1903b3…` with erratum `1dbf820a…` | the planar method this packet generalizes |

**Separation.** The proof is a direct Fubini/conditional-expectation computation of E||T_C w||^2 from the explicit kernel. No storage function, dissipation inequality, Riccati/LMI, controller, selected control, changed output, quarantined guidance or RMS source is used. Ξ is an explicit Gaussian average inside one expectation identity.

**Ordinary tools.** Spectral theorem for skew-adjoint operators; Gaussian characteristic function; Cauchy–Schwarz; compactness of the unit sphere; continuity.

## 2. Proofs

**Conjugation average.**

- L is skew-adjoint because ⟨L(N), P⟩_F = tr(NA0P) − tr(NPA0) = −⟨N, L(P)⟩_F.
- Hence e^{aL} is Frobenius-orthogonal, and e^{−A0a} N e^{A0a} = e^{aL}(N) = Σ_ω e^{iωa} Π_ω(N).
- E e^{iωa_u} = e^{−ω^2u/2}, and ∫_0^∞ e^{2μu − ω^2u/2} du = 1/(2|μ| + ω^2/2).
- Positive semidefiniteness: each congruence e^{−A0a} N e^{A0a} is PSD.
- Ξ(I) = I/(2|μ|) because L(I) = 0.

**Lemma IS.** For a unit vector v,

`v^T 2Ξ(N) v = ∫_0^∞ 2e^{2μu} E[(e^{A0a_u}v)^T N (e^{A0a_u}v)] du ≤ λ_max(N)/|μ|`,

because e^{A0a}v is a unit vector.

- Equality forces (e^{A0a}v)^T N (e^{A0a}v) = λ_max(N), i.e. e^{A0a}v ∈ E_top(N), for almost every a. The Gaussian law of a_u has full support for every u > 0, so by continuity this holds for every a ∈ R.
- span{e^{A0a}v : a ∈ R} is invariant under every e^{A0b}, hence under A0 (differentiate at b = 0). It is nonzero and contained in E_top(N).
- Conversely, a unit v in an invariant subspace V ⊆ E_top(N) has its whole orbit in V, which gives equality.
- Since Ξ(N) ⪰ 0, ||Ξ(N)|| = max_{|v|=1} v^TΞ(N)v, and the maximum is attained. ∎

**Item 1.** This is the v39 §2 computation verbatim with R(σ·) replaced by e^{A0·}, which is legitimate because e^{A0a}e^{A0b} = e^{A0(a+b)}:

- Fubini, with domination by m_1κ_1 E∫(T_μ|w|)^2;
- symmetrization over s' < s;
- conditioning on F_s, using a := W_t − W_s independent of F_s and β := W_s − W_{s'} F_s-measurable;
- E[e^{−A0a} M e^{A0a}] = Σ_ω e^{−ω^2(t−s)/2} Π_ω(M);
- the time integral gives e^{μ(s−s')} C^T Ξ(M) e^{A0β} C;
- recognize X_s = ∫_0^s e^{μ(s−s')} e^{A0(W_s−W_{s'})} C w(s') ds'. ∎

**Item 2.** Pathwise ||X|| ≤ ||Cw||/|μ|, because e^{A0θ} is orthogonal. Then Cauchy–Schwarz. ∎

**Item 3.**

- The path ℓ ≡ 0 gives convolution with e^{μu} D0C, whose norm is ||D0C||/|μ|.
- Upper bound: |z| ≤ √m_1 |X| and item 2's pathwise bound, for every path. ∎

**Item 4.**

- Compare item 3's lower bound with item 2, then apply v34 Theorem R.
- In the aligned case the inequality reads 2||Ξ(M)|| < m_1/|μ|, which is Lemma IS. ∎

**Item 5.**

- With output map I, Ξ(I) = I/(2|μ|), so item 1 gives E∫|X|^2 = (1/|μ|) E∫⟨w, C^T X⟩ ≤ (1/|μ|)||w|| ||C^T X||.
- Item 2 for the output map C^T, whose weight is CC^T, gives ||C^T X||^2 ≤ 2||Ξ(CC^T)|| (κ_1/|μ|) ||w||^2.
- By Lemma IS, 2||Ξ(CC^T)|| < κ_1/|μ|. Hence G2^2 ≤ m (2||Ξ(CC^T)|| κ_1/|μ|)^{1/2}/|μ| < mκ_1/μ^2.
- The bound is uniform over w. And G_rob ≥ ||D0C||/|μ| = √(mκ_1)/|μ|.
- Apply v34 Theorem R. ∎

**Item 6.**

- G_rob ≤ √(mκ)/|μ| by item 3.
- For the lower bound, take a unit u ∈ R^n, deterministic f ∈ L2, and the adapted input w(s) := κ^{−1/2} C^T e^{A0W_s} u f(s). Then |w(s)| = |f(s)| and Cw(s) = κ^{1/2} e^{A0W_s} u f(s).
- So X_t = κ^{1/2} e^{A0W_t} u (T_μ f)(t) and |z_t| = √(mκ)|(T_μ f)(t)|.
- The supremum over f gives G2 ≥ √(mκ)/|μ|.
- With v31 and v34 item 1, G2 ≤ G1 ≤ G_rob, so all are equal.
- ℓ-dependence: D0 e^{A0θ} C = √(mκ)·(an isometry composed with e^{A0θ} composed with a co-isometry) is constant in θ only if A0 = 0. ∎

**Corollaries.**

- **RS1.** σJ has no real eigenvector, so no line is invariant.
- **RS2.** A line span(v) is A0-invariant iff A0v = λv with λ real. A0 is skew, so λ = 0, i.e. v ∈ ker A0.
- **RS3.** As stated. ∎

## 3. Meaning (value side only)

**Norm-preserving noise.** For norm-preserving noise with isotropic corrected drift, strictness of the literal-vs-RMS gap is governed by a geometric condition: whether the extreme output or input directions contain a noise-invariant subspace.

**Equality.** Bi-isotropic data allow adapted co-rotation and give equality even though the noise is visible in the kernel.

**Synthesis.** No statement about controllers or synthesis is made.

## 4. Process and assurance

- Written exact mathematics only, after v209 was read FIRST and the adopted inputs were read completely.
- Frozen v27–v32 untouched.
- Main's decisions were received: v220 freeze, and v33+ remain author-written unreviewed candidates without a gate. No v220 file, review or assignment was opened.
- No pinned/frozen/shared edit. No Git, deletion, publication or external model.
- All permanent findings and ZERO quarantines remain: post56, post60, postS126, the self-released v163 assessment, and the protected S242 window. HELD_C889 was never opened.
- No formal, kernel, human, configured-family, executable or novelty acceptance.
- Same18, HOLD v2, science cutoff 2026-10-27T11:05:38-07:00 and delivery deadline 12:35:38 apply. This is not an early final park.

**END OF COMPLETE v40.**
