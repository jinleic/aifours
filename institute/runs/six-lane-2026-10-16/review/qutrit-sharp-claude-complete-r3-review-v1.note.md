# Referee report: `LEMMA_R_PROOF.r3.md` (frozen r3, sha256 ae42fcbb…)

**Scope.** This report covers proof correctness only. Machine evidence, numerical evidence and significance are kept separate below, and novelty is not assessed. "Checked" means I checked it by hand reasoning from the text; I ran nothing.

**Headline.** There is **no missing case and no fatal or major issue.**
- I re-derived every step of §§0–5 from the conventions at `LEMMA_R_PROOF.r3.md:104-106`. This includes every relation in §0.2, derived directly from (1)–(4) with signs and conjugations.
- I checked both §W tables entry by entry.
- The case tree S / G / A\* / B\* is exhaustive, and each branch's conclusion follows.
- The parts not previously re-reviewed are correct: R2 (T-dual transfer), R3 (Rank Lemma) and R4 (tables).
- All findings are minor:
  - one formula that is wrong as written but never used in its wrong form;
  - several one-line justifications that r3 asserts but leaves to the companion note or to scripts;
  - notation.

## Findings

**Fatal:** none. **Major:** none.

**Minor** (editorial; none changes a conclusion)

1. **`LEMMA_R_PROOF.r3.md:202`** — For a TP map, Φ(I) = I + t·σ. So "Φ(w₀I + w·σ) = w₀I + (t + Tw)·σ" is false when w₀ ≠ 1 and t ≠ 0.
   - Correction: replace it with "w₀I + (w₀t + Tw)·σ".
   - No downstream effect, because the same step imposes t = 0.

2. **`:256`, `:261`** — Lemma N1 needs Σ_d Y_dN_d† = 0, but (α) at `:168` is in the form Σ_d N_dY_d† = 0. N1 also silently assumes that {N_d} is a unital Kraus triple, which Fact K(a) requires.
   - At `:256`, add "with {N_d} a unital Kraus triple".
   - Replace the first sentence of `:261` with: "Fix a ∈ K and put Y = (Q_a, Ω_a1, Ω_a2). The adjoint of (α) is Σ_dY_dN_d† = 0 and (γ) is Σ_dN_d†Y_d = 0, so N1 gives Q_a, Ω_ad ∈ A. For N1′, the (a,d)-analogues at `:170` already read Σ_cY_cR_c† = 0 = Σ_cR_c†Y_c with Y = (T_b, Ω^(b1), Ω^(b2))."
   - I checked both forms; the step is valid.

3. **`:266`** — "Invariant under u_k ↦ hu_k" is imprecise.
   - Replace it with: "for invertible h, the map u_k ↦ hu_k multiplies the hypothesis on the left by h and sends F ↦ (h⊗I)F. So the hypothesis and rank F are preserved."

4. **`:268`** — r3 asserts that all 3×3 minors of L(u) vanish but gives no reason. The reason appears only at `LEMMA_R_NORMAL_FORM.v1.md:69-70` and in a script.
   - Add: "L(gug⁻¹) = (g⊗g)L(u)(g⊗g)⁻¹. In the basis e₁₁, e₁₂, e₂₁, e₂₂, L(diag(λ₁,λ₂)) = diag(λ₁−λ₂, 0, 0, λ₂−λ₁). Also L(λI+E₁₂) = E₁₂⊗I + I⊗E₁₂, whose image is span{e₁₁, e₁₂+e₂₁}. Hence rank L(u) ≤ 2 for every u, Jordan blocks included."

5. **`:269-270`** — Case (ii) names the sub-cases but not their rank bounds. Add:
   - If dim span{u_k} ≤ 1, a G-move gives u₂ = 0, so F = u₁⊗v₁ has rank ≤ 1·2 = 2.
   - If the span is a 2-plane of singular matrices, it is totally isotropic for the non-degenerate quadratic form det. It is therefore one of the two rulings: all u_k = a_kbᵀ, or all u_k = ab_kᵀ.
   - Then F = (Σa_k⊗v_k)(bᵀ⊗I) or F = (a⊗I)(Σb_kᵀ⊗v_k). Each factors through C², so rank F ≤ 2.
   - The hypothesis of Lemma T is not needed in case (ii).

6. **`:343`** — This step uses ρ_c, τ_b ≠ 0 and the independence of w₁, w₂ in the free index d.
   - Add: "With R_c = ρ_cw_cw_cᵀ, (O4) reads Σ_c ρ̄_c(Σ_a Q_a[b,c]w̄_c[a]) w̄_c[d] = 0 for all d. Since w̄₁, w̄₂ are independent and ρ_c ≠ 0, each bracket vanishes. (O2) is the same with τ_b."

7. **`:357-358`** — The reduction to a single support pattern is asserted, and enumerated by machine at `:467`, but never derived. Add the two chains:
   - If p₁ ≠ 0: then r₁ = 0, so r₂ ≠ 0, so q₁ = 0, so q₂ ≠ 0, so s₂ = 0, so s₁ ≠ 0, so p₂ = 0.
   - If p₁ = 0: then p₂ ≠ 0, so s₁ = 0, so s₂ ≠ 0, so q₂ = 0, so q₁ ≠ 0, so r₂ = 0. This gives the second pattern p₁ = q₂ = r₂ = s₁ = 0.
   - The simultaneous swap e₁↔e₂ on parties 1 and 4 maps the second pattern to the first. It sends p_K ↦ (p₂,p₁) and q_K ↦ (q₂,q₁), swaps r and s, and keeps A, C ⊆ Diag.

8. **`:382`** — "Maximal-overlap normal form" is never defined in r3.
   - Replace it with "any normal form of §0.2 (φ(0000) = 1)".
   - Nothing changes, because |U[(00),(00)]| ≤ 1.

9. **`:146`** — Name the theorem used.
   - Add: "Over C, projective varieties X, Y ⊂ Pⁿ with dim X + dim Y ≥ n intersect. Here U⁻¹Σ is the image of Σ under the automorphism [U⁻¹], so it is isomorphic to Σ."

10. **`:400`** — The identification of table W1 with S·U(2π/3) from thesis eq. (3.36) cannot be checked from the frozen text.
    - The attainment claim at `:84` does not depend on it: the printed table is itself a dual, non-2-unitary gate with e_p = 15/16 (checked below).
    - Add: "Attainment is certified by the table itself, independently of this identification."

11. **`:163`** — "With one index equal to 0" is accurate for (U), (α)–(δ) and (O1)–(O4), but not for the (a,d)-analogues at `:170`.
    - Those are the {b}×{0} entries of (1) and (3) with both block indices in K.
    - Reword as: "each is an entry block of (1)–(4) after imposing the zero pattern."

12. **Notation collisions** (no logical effect):
    - x = vec R₀ (`:159`) versus x₁, x₂ inside T_b (`:361-364`).
    - The scalars α, β, γ, δ versus the relation labels (α)–(δ); both appear in `:366`.
    - S is used for SWAP, for the Pauli index set (`:188`) and for the label S ∈ {R,T} (`:332`).
    - H is used for the Hadamard matrix (`:209`) and for the gate (`:423`).
    - σ is used for a singular value (`:274`) and for the Pauli matrices.
    - Suggested renames: T₁ = ξ₁E₁₂ + η₁E₂₂ and T₂ = ξ₂E₁₁ + η₂E₂₁; Pauli index set 𝒮; Hadamard matrix H₄.

## Requested points (all checked, all correct)

- **Normal form** (`:146-161`).
  - The dimension count 4 + 4 ≥ 8 gives the product-to-product pair.
  - The (00) rows and columns of U and Uᴿ give the vanishing on the pairs {12, 34, 13, 24}.
  - The slice shapes follow, and rank U^Γ = rank M = dim span{X_ad}.
- **Independent gauges** (`:181-183`).
  - Parties 2 and 3 act on the (b,c)-matrices and only re-mix the K-labels of R and T, leaving R₀ fixed.
  - Parties 1 and 4 act on the (a,d)-matrices and only re-mix the labels of N, Q and Ω, leaving N₀ fixed.
  - So A = C = Sym (and Sym/Diag) can be imposed together.
- **Fact K** (`:187-218`).
  - The Kraus span equals the range of the Choi matrix.
  - The Pauli/Hadamard step is correct.
  - The table of J⁻¹σ_m and the products Sym·W₀ is correct.
  - dim A = 3 implies ‖N₀‖ < 1.
- **N1** is correct once the adjoint of (α) is taken (finding 2).
- **Lemma T** (`:263-271`).
  - F annihilates the singlet if and only if the tensor is (a,d)-symmetric, so the tensor and pencil forms are equivalent.
  - The invertible branch is correct, including Jordan blocks: v₁ = −v₂ adj(u), F = (I⊗v₂)L(u).
  - Both singular rulings are correct.
- **Rank Lemma** (`:277-318`).
  - The pivot is correct.
  - The E_𝐁/F_P splitting is correct: col Y ∩ col 𝐁 = 0 and row Y ∩ row P = 0.
  - The rank formula holds unconditionally.
  - n₀ ∈ 𝒜 and x ∈ 𝒞 keep Ω′ inside 𝒜 and 𝒞.
  - E_𝐁𝒞 ⊆ 𝒞 and 𝒜F_P ⊆ 𝒜 give the bound.
- **Proposition G** (`:320-333`).
  - 𝐍𝐍† = I − N₀N₀† has rank 2.
  - (O3) needs N_d to be symmetric, which holds in the A = Sym gauge.
  - The (S,a)|(c,d) flattening lies in the 2-dimensional ker 𝐍̄.
  - The (S,c)|(a,d) flattening has rank rB, and Lemma T gives rB ≤ 2.
- **Lemma S** (`:198-199`, `:273-275`) is correct.
- **Proposition A\*** (`:335-350`) is correct over C.
  - A complex symmetric rank-one matrix has the form λwwᵀ.
  - Isotropic w are harmless, because only ‖w‖² is used.
- **Proposition B\*** (`:352-378`) is correct.
  - Both support patterns are handled.
  - In the case β = γ = 0, the rank is ≤ 5.
  - In the case β, γ ≠ 0, dim B, D ≤ 2 forces N₀ = R₀ = 0 and then Ω = 0, so M is block-monomial unitary.
- **Coverage** (`:176-179`, `:380-388`).
  - The three permutations act transitively on {A, B, C, D}.
  - They preserve D, 2-unitarity, rank U^Γ, the normal form and the corner norms (up to swap or transpose).
- **Objective and marginal identity** (`:103-138`).
  - The following are correct: (XS)ᴿ = X^ΓS, (US)^Γ = UᴿS, E(S) = 8/9, the formula e_p = 9/8 − tr W²/72, and the Cauchy–Schwarz equality case.
  - The identities 9ρ₁₄ = (U^Γ†U^Γ)ᵀ and U^ΓU^Γ† = S(M†M)ᵀS are correct.
  - The side claim at `:135` is also correct: 9ρ₁₄ = 9|ψ⟩⟨ψ| has entries ±i, while any permutation conjugate of U^ΓU^Γ† = 9|Φ⟩⟨Φ| is real.
- **T-dual transfer** (`:87-88`, `:108-119`).
  - V ↦ VS is a bijection between non-2-unitary T-duals and non-2-unitary duals.
  - Vᴿ = U^ΓS, so the bound is on rank Vᴿ (the operator-Schmidt rank).
- **Equality and exclusion of 2-unitaries** are correct.
  - e_p = 1 if and only if W = I, which holds if and only if U is 2-unitary.
  - Both witnesses have rank 6, so neither is 2-unitary.

## Witness tables (hand checks)

**W1** (`:402-412`).
- U_s is orthogonal. The rows pair up on disjoint column supports: {0,8} on {2,3}, {1,6} on {0,8}, {2,4} on {5,7} and {5,7} on {4,6}. Row 3 is 2e₁. Every row of 2U_s has squared norm 4.
- U_sᴿ = U_s: I checked all 17 nonzero entries under the map (i,α),(j,β) ↦ (i,j),(α,β).
- The rows of 2U_s^Γ are:
  - r₀ = √3(e₁+e₃) and r₈ = √3(e₂+e₆);
  - r₁ = −r₃ = √3e₈;
  - r₂ = −r₆ = e₀+e₅+e₇;
  - r₄ = 2e₀ − e₅ − e₇;
  - r₅ = r₇ = √3e₄.
- So 4W has spectrum {6⁶, 0³}. Hence W has spectrum {3/2⁶, 0³}, tr W² = 27/2 and e_p = 15/16.

**W2** (`:434-442`).
- All 9 rows reproduce φ from the stated data at `:424-429`.
- H is orthogonal. Rows {1,3,4,8} live on columns {1,3,4,8}, and rows {2,5,6,7} live on columns {2,5,6,7}. Each block has orthogonal rows of squared norm 16.
- Hᴿ = H, checked entrywise.
- The rows of 4H^Γ are:
  - g₀ = 4e₀ + 2e₄ + 2e₈;
  - g₄ = 2e₀ ± √6(e₁+e₃) − 2e₄ − 2e₈ with the + sign, and g₈ is the same with the − sign;
  - g₁ = g₃ = √6(e₄−e₈);
  - g₂ = g₆ = −√6(e₅+e₇);
  - g₅ = g₇ = √6(e₂+e₆).
- The Gram matrix equals 12(I+S) entrywise, so H^ΓH^Γ† = (3/4)(I+S), with rank 6 and e_p = 15/16.
- Consistency check: H is a case-G gate with rP = rB = 2 (and rank Y = 1), so the G bound is attained.

## Independent proof map

1. **Objective.** For U ∈ D, e_p = 9/8 − tr W²/72 with W = U^ΓU^Γ† and tr W = 9. If rank W ≤ 6, then e_p ≤ 15/16, with equality if and only if spec W = {3/2⁶, 0³}. The T-dual statements follow through V = US.
2. **Normal form.** The dimension theorem, local unitaries and a phase give φ(0000) = 1, which fixes the zero pattern and the sectors. The relations are entry blocks of (1)–(4).
3. **Tools.** Fact K, N1/N1′, Lemma T and the Rank Lemma.
4. **Case S** (‖N₀‖ = 1 or ‖R₀‖ = 1). The five border slices lie in span{diag(1,1,σ), E₂₂}, so rank ≤ 2 + 4 = 6.
5. **Remaining cases.** Permute parties so that dim C = 3, or else all four sector dimensions are ≤ 2.
   - **G** (dim A = 3): Rank Lemma (ii) gives rank ≤ 4 + rB, and Lemma T gives rB ≤ 2, so rank ≤ 6.
   - **A\*** (dim A ≤ 2): R_b and T_b are multiples of w_bw_bᵀ with w₁ ∦ w₂. (O2) and (O4) make Q_a diagonal, so rP ≤ 2. Rank Lemma (i) with vec C gives rank ≤ 6.
   - **B\*** (all ≤ 2): N and R are diagonal and only one support pattern survives. If β = γ = 0, the rank is ≤ 5. Otherwise N₀ = R₀ = Ω = 0 and U is 2-unitary.
6. **Sharpness.** W1 and W2 attain the bound.

## Trust boundary

- **Checked by me, by hand:**
  - all of §§0.1–5, including the relations derived independently from (1)–(4);
  - the side claim at `:135`;
  - both §W tables.
- **Supplied and not checked:**
  - the identification W1 = S·U(2π/3) in thesis eq. (3.36);
  - all quotations, page numbers, line numbers and SHA-256 values in §P, §0.4 and §6;
  - the README §0.1 convention pin. The results are unchanged under the standard alternative R/Γ conventions, which differ by fixed index permutations or transposes and so preserve unitarity, rank and singular values;
  - all scripts and JSON receipts, including `parent-exact-relations.json` and `parent-sqrt6-gate.json`. Their reported gate properties agree with my hand results, but nothing above relies on them.
- **No evidential weight for the proof:** the floating-point searches and the failed counterexample attempts.
- **Novelty and priority:** not assessed.
- **Significance (separate from correctness).** If the §P quotations are accurate, the Theorem and Corollary state exactly Conjecture 3.3.2, for both D and T and with no restriction on the class of gates. That includes the e_p gap and the exclusion of rank 7 and 8. I did not verify the quotations.

VERDICT: ACCEPT-WITH-FIXES
