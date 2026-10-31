# Review f284-werner-qubit-side-projectors — review-v1

Reviewer: ReviewF284Qubit (same-harness written review; not human, independent-family, formal/kernel or novelty verification).
Input: literal-packet-v1.md (SHA256 4abf197f062de29bdba73a82829a3df5e394c6b97aabfc558bb2a897e8e10489, 9168 bytes, 121 LF) carrying S1 = frontier-20261029-d4-t2-qubit-side-test-projectors-complete-v1.md (SHA256 ce6a62889b044e898525b3478d78d227f0e3dc0686a087a396f7d3f6d8bcd02c, 8408 bytes, 119 LF), COMPLETE_BODY, lines 1–119. Manifest 8fe0896249001f4ff994727790bc91db0d80c802042cde59e96cef165ead1159; freeze receipt 13f10f847c1a2e8c5633db21275043cf90b4fb0e3fc8b40529b6fee4ce5eb9d2.
Mode: WRITTEN_ONLY. Every derivation below is hand reconstruction from the packet text only; no selected instances, no interpreter/CAS/program/enumeration, no network, no sibling review, no author code, no held payload. The two algebraic parameter choices in Finding 1 are symbolic observations of the same kind as the packet's own S1|41|, used to refute a literally false general quantification, not sampled diagnostics. Line references "LFn" are S1 lines.

## Verdict summary

Counts: **FATAL 0, MAJOR 1, MINOR 4.**

- Main theorems all SUPPORTED: (1.1) dimension-free rank≤2 partial-trace inequality (LF7–9); (1.2) lift to every original d=4 rank-two test projector with either marginal rank≤2, arbitrary complex traceless A,B (LF11–13); strictness when both original squares are nonnormal (LF15 sentence 1); exact slack identity (2.2) (LF27–33); leakage identity (LF69); gap decomposition (3.2) (LF71–77); equality analysis incl. rank-one and rank-two marginal cases and the rank-two pivot (LF83–115).
- One MAJOR (Finding 1): the Section 3 weighted-duality statement is false **as literally quantified** because L45 omits the needed `Tr D = 0`; algebraic counterexample below. All actual uses are inside the traceless family, so nothing downstream is affected. This is a defect of the stated lemma hypothesis, not of (1.1)/(1.2)/strictness.
- MINOR: T2 terminology external (Finding 2); notation overload Q/P (Finding 3); rank-zero marginal and n=1 boundary not spelled out (Finding 4); S₂ defined only via the dual formula (Finding 5).

No claim about both local ranks ≥ 3, f274 η, physical/η counterexamples, source correctness, novelty or any global target is made or required; the packet itself disclaims them (LF17, LF119) and this review draws no such conclusion.

## Read/process coverage (complete)

- Manifest, freeze receipt and the three status-only controls read; controls used for authority/status only, no mathematical payload followed. One administrative pre-body ACK sent to Main before any mathematical body read.
- Packet read in raw windows ≤20 LF: packet lines 1–20, 21–40, 41–60, 61–80, 81–100, 101–121 (packet line N = S1 line N−2 for N≥3). Packet byte/LF/hash re-verified live: 9168 bytes, 121 LF, SHA 4abf…0489 = freeze receipt.
- Display-collapsed even lines resolved: every even S1 line is encoded as a bare prefix line `S1|N|` with empty body. Verified programmatically over packet lines 3–121: every line carries its exact `S1|N|` prefix, no even line has any body byte, no odd line is empty; even-line byte lengths are only 5/6/7 = the prefix itself. Source file re-hashed live = manifest input hash, 119 lines, all even lines blank. Hence all 60 non-blank S1 lines were read verbatim and all 59 blank separators are certified blank: no elision, no truncation.
- Clocks: native /bin/date checkpoints 2026-10-30T03:24:39−0700 and 03:25:29−0700 recorded before writing; ≤30 min cadence maintained (run began ≈03:14 PDT).

## Reconstruction and per-claim verdicts

Conventions: ⟨M,N⟩ = Tr(M†N); ||·|| = Frobenius; ||·||₁ nuclear; blocks of R∈M(C²⊗Cⁿ) written along the C² factor. Rank/singular values over C throughout; nothing assumes Hermitian, normal, separable or PPT structure anywhere (audit item "do not narrow" — satisfied: every step is for arbitrary complex operators).

### R1. 2×2 complex hollowing (LF21) — SUPPORTED
Schur: traceless 2×2 is unitarily similar to [[λ,z],[0,−λ]]. For |ψ⟩=(cosθ, e^{iφ}sinθ): ⟨ψ|A|ψ⟩ = λcos²θ + z e^{iφ}cosθsinθ − λsin²θ = λcos2θ + (z e^{iφ}/2)sin2θ (checked termwise, conjugations tracked). Choose φ so z e^{iφ} is real opposite in sign to λ (any φ if λ=0); as θ runs [0,π/4], λcos2θ+(|z|... )sin2θ moves continuously from the λ-term to the z-term, so some θ cancels exactly (immediate if λ=0 or z=0). Orthogonal complement expectation = Tr A − ⟨ψ|A|ψ⟩ = 0. Hence the traceless part of Tr_n R can be hollowed by U∈U(2) acting on the qubit factor.

### R2. Invariance (LF23) — SUPPORTED
For R=ΣAᵢ⊗Bᵢ: (U⊗I)R(U⊗I)† = Σ UAᵢU†⊗Bᵢ, so Tr_n R is unchanged (Tr(UAᵢU†)=TrAᵢ), Tr₂ R = U(Tr₂R)U†, Tr R unchanged, rank and ||R|| unchanged. Both partial-trace Frobenius norms preserved (one invariant, one conjugated). Also used later at LF99: Tr₂ is invariant and (Tr₄R)_₀ conjugates covariantly with C, so hollowing does not disturb (4.1).

### R3. Block form (LF25) — SUPPORTED
Tr_n R = [[TrP, TrQ],[TrT, TrS]]; (Tr_nR)₀ = [[(TrP−TrS)/2, ·],[·, −(TrP−TrS)/2]]; hollow ⟺ TrP = TrS ⟺ Tr(P−S)=0 (2.1).

### R4. Exact slack identity (2.2) (LF27–33) — SUPPORTED
Expansion: ||R||² = Σ||block||²; ||Tr_nR||² = |TrP|²+|TrQ|²+|TrT|²+|TrS|²; ||Tr₂R||² = ||P+S||²; |TrR|² = |TrP+TrS|². Collecting:
2||R||² − LHS(1.1) = ||P−S||² + 2||Q||² + 2||T||² − |TrP|² − |TrQ|² − |TrT|² − |TrS|² + |TrP+TrS|²/2,
and with a=TrP, b=TrS the parity |a+b|²/2 + |a−b|²/2 − |a|² − |b|² = 0 (parallelogram) turns the trace terms into −|Tr(P−S)|²/2 exactly. So (2.2) is an exact identity for **any** block matrix — no hypothesis needed; (2.1) only zeroes the first trace term. First bracket then = ||P−S||² ≥ 0.

### R5. Rank-two trace bounds (LF35–39) — SUPPORTED
Q = (e₁*⊗I)R(e₂*⊗I) as a compressed submatrix, so rank Q, rank T ≤ 2. For any Z: |TrZ| ≤ ||Z||₁ (triangle on SVD) and ||Z||₁² ≤ rank(Z)·||Z||² (Cauchy–Schwarz on singular values). Hence 2||Q||²−|TrQ|² ≥ 2||Q||² − 2||Q||² = 0, likewise T. With R4 this proves **(1.1)** for all complex R, rank≤2, all n≥1. Boundary n=1: LHS(1.1) = ||R||²+|TrR|²/2 ≤ 2||R||² by |TrR| ≤ √2||R|| — consistent, no exception.

### R6. Rank sharpness (LF41) — SUPPORTED
R = C⊗I₃, C∈M₂ nonzero traceless: rank 6; Tr₃R = 3C, Tr₂R = (TrC)I₃ = 0, TrR = 0; LHS = 9||C||², RHS = 2·3||C||² = 6||C||². Correctly labelled a symbolic observation about a false stronger premise.

### R7. Ky Fan/Frobenius duality (LF49–51) — SUPPORTED
√S₂(Y) := max_{rankR≤2,||R||=1}|Tr(R†Y)|. Von Neumann trace inequality: |Tr(R†Y)| ≤ Σᵢ₌₁²σᵢ(R)sᵢ(Y) ≤ ||R||·(s₁²+s₂²)^{1/2}; equality at R = (s₁u₁v₁†+s₂u₂v₂†)/√(s₁²+s₂²). So S₂ = σ₁²+σ₂². (Finding 5 notes the σ-identification is implicit, not restated.)

### R8. Weighted dual constants and conjugation (LF53–57) — REFUTED as literally quantified (Finding 1); SUPPORTED with Tr D = 0
With **Tr C = 0 and Tr D = 0** the three source pieces tI, C⊗Iₙ, I₂⊗D are HS-orthogonal (⟨I,C⊗I⟩ = n·TrC = 0; ⟨I,I⊗D⟩ = 2TrD; ⟨C⊗I,I⊗D⟩ = TrC†·TrD = 0). Pairing computation (conjugations tracked): ⟨R,tI⟩ = t·conj(TrR); ⟨R,C⊗I⟩ = ⟨Tr_nR,C⟩; ⟨R,I⊗D⟩ = ⟨Tr₂R,D⟩. Orthogonal projections of R: R_I = (TrR/2n)I with ||R_I||² = |TrR|²/2n; R_C = ((Tr_nR)₀⊗I)/n with ||R_C||² = ||(Tr_nR)₀||²/n; R_D = I₂⊗(Tr₂R)₀/2 with ||R_D||² = ||(Tr₂R)₀||²/2. Weights: ||tI||² = 2n|t|² (w_I=1); ||C⊗I||² = n||C||² against the source weight 2||C||² (w_C = 2/n — the nonobvious constant); ||I⊗D||² = 2||D||² (w_D=1). Weighted Cauchy–Schwarz gives |Tr(R†Y)| ≤ √(|TrR|²/2n + ||(Tr_nR)₀||²/2 + ||(Tr₂R)₀||²/2)·√(2n|t|²+2||C||²+2||D||²), i.e. exactly the LF55 dual with constants /(2n), /2, /2 — the C-coefficient is /2 and not /n precisely because w_C = 2/n. Combining with (1.1) (whose half-left side is exactly the dual expression: ||Tr_nR||² = |TrR|²/2+||(Tr_nR)₀||², ||Tr₂R||² = |TrR|²/n+||(Tr₂R)₀||², so LHS(1.1)/2 = |TrR|²/2n + ||(Tr_nR)₀||²/2 + ||(Tr₂R)₀||²/2 — verified) yields (3.1). The converse direction of "exactly equivalent" also checks: given (3.1), apply it to Y built from any rank≤2 R as t = TrR/2n, C = (Tr_nR)₀/2, D = (Tr₂R)₀/2 (both traceless automatically); then Tr(R†Y) = N*(R)² and N(Y)² = N*(R)², and R7 bounds N*(R)² ≤ √S₂(Y)||R|| ≤ N(Y)||R||, forcing N*(R) ≤ ||R||, i.e. (1.1).

### R9. Support reduction and ρ (LF61–67) — SUPPORTED
Tr_B P supported in a 2-dim S ⟹ (Π_{S⊥}⊗I)P(Π_{S⊥}⊗I) ⪰ 0 has trace 0 ⟹ vanishes ⟹ (Π_{S⊥}⊗I)P = 0; P lives on S⊗C⁴. If the marginal rank is 1, S is chosen containing the support (any 2-dim S works). A|_S = αI₂+C with TrC = 0 (α = Tr(A|_S)/2, arbitrary complex). ρ = Tr_B P ⪰ 0, Trρ = rank P = 2.

### R10. Leakage identity (LF69) — SUPPORTED
X's block column over the support is [Y; A₂₁⊗I₄] with Y = αI₈+C⊗I₄+I₂⊗B, so the (1,1) block of X†X is Y†Y + (A₂₁†A₂₁)⊗I₄ — the cross term is absent exactly because the two outputs occupy orthogonal local-A subspaces (row-block orthogonality). Then Tr(P·(A₂₁†A₂₁⊗I₄)) = Tr(ρA₂₁†A₂₁) by the standard partial-trace pairing Tr((M⊗I)P) = Tr(M·Tr_B P) — conjugation verified on R = ΣAᵢ⊗Bᵢ. Hence Tr(PX†X) = Tr(PY†Y) + Tr(ρA₂₁†A₂₁).

### R11. Constants at LF71 — SUPPORTED
TrA = 0 ⟹ TrA₂₂ = −2α ⟹ |TrA₂₂|² = 4|α|² ≤ 2||A₂₂||² ⟹ ||A₂₂||² ≥ 2|α|². ρ ≤ 2I₂: write P = |ψ₁⟩⟨ψ₁|+|ψ₂⟩⟨ψ₂| (rank 2); each pure marginal ⪯ I₂, so ρ = ρ₁+ρ₂ ⪯ 2I₂. Tr(PY†Y) ≤ S₂(Y): R7 with R' = YP gives Tr(PY†Y) = Tr(R'†Y) ≤ √S₂(Y)||R'|| = √S₂(Y)√(Tr(PY†Y)). (3.1) with n=4, t=α, D=B (TrB=0 ✓, TrC=0 ✓ — the valid traceless instance) gives S₂(Y) ≤ 8|α|²+2||C||²+2||B||².

### R12. Gap decomposition (3.2) (LF73–77) — SUPPORTED
2||A||² = 2(2|α|²+||C||²+||A₁₂||²+||A₂₁||²+||A₂₂||²) and 2||B||²; subtract Tr(PX†X) = Tr(PY†Y)+Tr(ρA₂₁†A₂₁) and use 2||A₂₁||² = Tr(2I₂·A₂₁†A₂₁): the difference is exactly 2||A₁₂||² + Tr((2I₂−ρ)A₂₁†A₂₁) + 2(||A₂₂||²−2|α|²) + [8|α|²+2||C||²+2||B||²−Tr(PY†Y)], with each bracket ≥ 0 (second: Tr of product of PSD matrices, Tr(H^{1/2}MH^{1/2}) ≥ 0). Proves **(1.2)** for A-marginal ≤ 2; B-case by the tensor swap (Tr(PX†X) and L invariant, roles of A,B exchanged) — LF79. No assumption on the other marginal, separability or PPT anywhere. Degenerate marginal rank 0 means P = 0 and (1.2) is 0 ≤ 2L trivially (Finding 4: unstated but harmless).

### R13. Rank-one marginal equality (LF83–87) — SUPPORTED
P = |v⟩⟨v|⊗Q, rank Q = 2 (forced by rank P = 2 and support). Term-by-term: Tr(PX†X) = 2||Av||² + ||BQ||² + āb + conj(āb) = 2||Av||²+||BQ||²+2Re(āb) with a = ⟨v,Av⟩, b = Tr(QB) (all conjugations checked). ||A||²−||Av||² = ||A|_{v⊥}||² and trace zero give |a| = |Σ_{j≥2}⟨e_j,Ae_j⟩| ≤ Σ||Ae_j|| ≤ √3·||A|_{v⊥}||, i.e. ≥ |a|²/3. |b| ≤ ||BQ||₁ ≤ √2||BQ|| (rank ≤ 2) and Tr(B(I−Q)) = −b give both B bounds |b|²/2. Total gap ≥ (2/3)|a|²+(3/2)|b|²−2|a||b| = (√(2/3)|a|−√(3/2)|b|)² ≥ 0 (product of the two coefficients is exactly 1 — the constant structure is sharp). If the total gap vanishes, each of the three nonnegative slacks vanishes separately, so both B inequalities are tight; tightness in |TrZ|² = 2||Z||² for Z = BQ (Z = ZQ) forces Z = λΠ with Π = Q by the R15 characterization and rank comparison, λ = TrZ/2 = b/2; likewise B(I−Q) = (−b/2)(I−Q) (Π₂ = I−Q); hence B = (b/2)(2Q−I₄), Hermitian, so **B² = (b²/4)I₄ normal** (b = 0 included: B = 0). Swap orientation gives A² normal.

### R14. Rank-two marginal equality and (4.1) (LF89–97) — SUPPORTED
Both eigenvalues of ρ positive and summing to 2 ⟹ 2I₂−ρ ≻ 0. Equality in (3.2): A₁₂ = 0; A₂₁ = 0 (strict positivity); equality in ||A₂₂||² ≥ |TrA₂₂|²/2 forces A₂₂ = λΠ, and the only rank-2 projection on the 2-dim S⊥ is I₂, with 2λ = −2α, so A₂₂ = −αI₂; and saturation Tr(PY†Y) = 8|α|²+2||C||²+2||B||². R := YP on C²⊗C₄ has rank ≤ 2, ||R||² = Tr(PY†Y), Tr(R†Y) = Tr(PY†Y). Chaining R7 + R8: Tr(R†Y) ≤ √S₂(Y)||R|| ≤ N(Y)||R|| = N(Y)² = ||R||² = Tr(R†Y), so equality holds throughout: equality in (1.1) for R (N*(R) = ||R||) and equality in the weighted Cauchy–Schwarz. Equality in Σ⟨Rᵢ,Yᵢ⟩ forces Rᵢ = c·wᵢYᵢ with one positive real c and Rᵢ = 0 where Yᵢ = 0; pairing both sides against Y gives c = 1 since N(Y)² = Tr(R†Y) > 0 (if N(Y)² = 0 then α=C=B=0, Y=0, B² = 0 normal — the trivial case LF97). Hence (4.1): (TrR)/(2n) = t, **(Tr₄R)₀ = 2C, (Tr₂R)₀ = 2B**.

### R15. Equality block form and Z = λΠ (LF99–103) — SUPPORTED
Hollow (Tr₄R)₀ as R1 (invariances R2 preserve everything relevant). Equality in (1.1) = all (2.2) brackets zero: P-block = S-block =: G; |TrQ|² = 2||Q||², |TrT|² = 2||T||². For nonzero rank≤2 Z with |TrZ|² = 2||Z||²: rank 1 is impossible (|TrZ| ≤ σ₁ = ||Z|| < √2||Z||), so σ₁ = σ₂ = σ; |TrZ| = 2σ needs both |⟨uᵢ,vᵢ⟩| = 1 and equal phases of ⟨u₁,v₁⟩, ⟨u₂,v₂⟩ — the common-phase point — giving uᵢ = e^{iθ}vᵢ with one θ, i.e. **Z = λΠ, Π a rank-two orthogonal projection**, λ = σe^{iθ}. (Conversely λΠ attains equality.) So each of Q,T is 0 or λ·(rank-2 projection).

### R16. Q = T = 0 (LF105) — SUPPORTED
Then Tr₄R = (TrG)I₂, (Tr₄R)₀ = 0, C = 0 by (4.1); A = αdiag(I₂,−I₂) so A² = α²I₄ normal.

### R17. Rank-two pivot (4.2) (LF107–109) — SUPPORTED
Column swap preserves rank ≤ 2; [[λΠ,G],[G,T]] has top-left block of rank 2 = full rank. Diagonalize Π = diag(I₂,0) and eliminate on the pivot λI₂: every other row is a combination of the two pivot rows; rows 3,4 (from the zero rows of λΠ) force the lower block-row of G to vanish; rows 5–8 force the off-corner block G₁₂ = 0 (pivot-row combinations have zeros in the columns where those rows carry G₁₂), then matching coefficients gives T = λ⁻¹G₁₁² ⊕ 0 and the lower blocks of T vanish. Net: G = ΠGΠ and **T = λ⁻¹G²**. (Both ΠG = G and GΠ = G are used; the conclusion is exactly (4.2).) The Q = 0, T ≠ 0 case is the row-swapped symmetric argument; Tr₂R = G+G either way.

### R18. T cases (LF111) — SUPPORTED
T = 0 ⟹ G² = 0. T = μΠ′ ≠ 0: range(G²) ⊆ range(Π) (G = ΠGΠ), so Π′ = Π by rank equality, and G² = λT = λμΠ.

### R19. B² normality (LF113–115) — SUPPORTED
Tr₂R = 2G and (4.1) give B = G−(TrG/4)I₄. If G² = 0 then TrG = 0 (nilpotent), B = G, B² = 0 normal. If G² = κΠ, κ ≠ 0: G = ΠGΠ satisfies (G|_Π)² = κI₂; z²−κ has distinct roots, so G|_Π is diagonalizable with eigenvalues ±√κ: if both signs occur, TrG = 0 and B² = G² = κΠ, normal (Π Hermitian); if one sign, G = ±√κΠ and B = ±√κ(Π−I₄/2), Hermitian, hence normal. So **B² is normal in every nonzero-Q/T equality case**. Together with R13, R16 and the factor-swap: equality in (1.2) always forces A² or B² normal; contrapositive gives strictness when both original squares are nonnormal (LF15 sentence 1). The claim that block-diagonality is a conclusion of equality, not an assumption, is accurate.

### R20. T2 consequence (LF15 sentence 2) — internal logic SUPPORTED; external identification INCONCLUSIVE
If some maximizing top-two right-singular projector P* of X = A⊗I₄+I₄⊗B (i.e. sup over rank-2 projectors of Tr(PX†X) is attained at P*) has a marginal of rank ≤ 2, then every rank-2 P satisfies Tr(PX†X) ≤ Tr(P*X†X) ≤ 2L, and < 2L when both squares are nonnormal since (1.2) is then strict for every marginal-≤2 projector. This conditional is internally sound (multiple maximizers share the same value, so one qualifying maximizer suffices). "T2" itself is not defined in the packet, so the identification with the round's T2 statement is INCONCLUSIVE here (Finding 2); no global-target conclusion is drawn.

### R21. Scope statements (LF17, LF119) — SUPPORTED
The unhandled domain is exactly both local marginal ranks ≥ 3 within this route; no counterexample asserted there; no f274/η/T3/Z2/q3/physical/source-correctness/novelty claims. Consistent with what is proved above.

## Findings

**Finding 1 (MAJOR; LF45/LF53–57): Section 3 as literally quantified is false — missing hypothesis Tr D = 0.**
L45 admits arbitrary D∈Mₙ(C) (only C is required traceless). Orthogonality of I₂⊗D against tI fails unless Tr D = 0, and both the pairing bound and (3.1) fail. Algebraic refutation: n = 1, t = 1, C = 0, D = [1]: Y = 2I₂; by the packet's own L51 definition S₂(Y) = 8 while 2n|t|²+2||C||²+2||D||² = 4, so (3.1) reads 8 ≤ 4. Pairing form: R = I₂/√2 (rank 2, ||R||=1) has |Tr(R†Y)| = 2√2 > 2 = N*(R)N(Y). Also n = 2, t = 1, C = 0, D = diag(2,0): Y = diag(3,3,1,1), S₂ = 18 > 12. Repair (not retroactive correctness): require Tr D = 0, or replace (t,D) by the orthogonalized (t+TrD/n, D−(TrD/n)I). Downstream impact: none — every use is the traceless instance (L63 "arbitrary and traceless" B; L65/LF71 with D = B, TrB = 0; the LF57 equivalence is correct for the traceless family, both directions reconstructed in R8). (1.1), (1.2), strictness and all other claims are unaffected.

**Finding 2 (MINOR; LF15):** "satisfies T2" uses round-external terminology never defined in the packet; the internal conditional is verified (R20), the external identification is left INCONCLUSIVE by this review.

**Finding 3 (MINOR; LF25/LF35 vs LF11/LF67, LF83 vs LF101):** symbol overload — P names both the test projector and an n×n block of R; Q names both the B-side rank-2 projector (LF83) and a 4×4 block of R (LF101). Presentational only; both readings are unambiguous in context.

**Finding 4 (MINOR; LF11, LF83, LF89):** degenerate cases marginal rank 0 (P = 0, trivial 0 ≤ 2L) and the n = 1 boundary of (1.1) (holds, R5) are not spelled out; no mathematical gap results.

**Finding 5 (MINOR; LF51):** S₂ is introduced only through the dual formula; the identity S₂ = σ₁²+σ₂² is implicit behind "Ky Fan/Frobenius duality". Reconstructed in R7; no defect beyond presentation.

## Degenerate and equality boundary inventory

n = 1 (valid, R5); marginal rank 0 ⟹ P = 0 (trivial); marginal rank 1 (R13, B² = (b²/4)I₄, b = 0 included); marginal rank 2 with ρ degenerate-vs-full (2I−ρ ≻ 0 exactly at rank 2 — used to kill A₂₁; rank < 2 handled by R13); α = 0 / zero source (B² = 0 normal, R14); λ = 0 excluded by Q ≠ 0; Q or T zero (R16, R18); G² = 0 vs G² = κΠ, κ ≠ 0, with opposite/coincident eigenvalue subcases (R19); b = 0 and ab-phase alignment in R13; equality in |TrZ| ≤ ||Z||₁ ≤ √2||Z||_F needs rank exactly 2, equal singular values and common phase (R15); strictness boundary: equality forces A² or B² normal, so both-nonnormal ⟹ strict (R19); sharpness of the rank hypothesis in (1.1) at rank ≥ 3 (R6). No both-ranks-≥3 statement is made or implied.

## Verification limits

Same-harness single-reviewer written reconstruction only; not human review, not independent-family, not formal/kernel, not novelty, no original-target or f274 conclusion, no execution. Proof repairs in Finding 1 do not retroactively make the original Section 3 statement correct.
