# Referee report: Claims A, B, C

**Verdict: ACCEPT.** This is conditional only on Song–Chen Prop. 3 holding exactly as quoted. Claims A, B and C follow with their stated quantifiers:

- **A** holds for every ρ, pure or mixed, and every μ that meets the hypotheses under some labeling.
- **B** holds for every ρ and every p ∈ [0,1].
- **C** holds for every ρ and every p ∈ [0,4/3].

I found no mathematical error and no hidden hypothesis. The items marked *precision* are wording fixes and do not change whether any claim is true. All checks were done by hand, with no code.

## Claim A — verified

**Normalization.** μ_I ρ_I⊗Q_{I^c} = w_I ρ_I⊗I_{I^c}. So X = w_∅I₈ + X1 + X2 + w_ABC ρ exactly, and tr X = tr Y = Σμ_I = 1.

**X1 ≺ T1 holds with no hypothesis on w.**
- U_A⊗U_B⊗U_C diagonalizes X1. At s ∈ {0,1}³ its eigenvalue is v(s) = Σ_l w_l x_l(s_l), where x_l = (λ_l, 1−λ_l).
- T1 has diagonal t(s) = Σ_l w_l[s_l=0].
- Then v(s) = Σ_τ π(τ) t(s⊕τ), with π(τ) = ∏_l (λ_l if τ_l=0, else 1−λ_l). This works because the l-th term only sees the marginal of π on τ_l.
- Each bit-flip s ↦ s⊕τ is a permutation. So v = Dt with D doubly stochastic, which gives v ≺ t.

**X2 ≺ T2.** Apply Prop. 3 with (a,b,c) = (w_AB, w_AC, w_BC). With factors restored to A,B,C order, its terms are exactly the terms of X2. The import holds up under any plausible variant of the source's hypotheses:
- **Normalization a+b+c=1:** remove it by positive scaling; the case a=b=c=0 is 0≺0.
- **Strict positivity, if assumed:** remove it by continuity of K_k.
- **Pure states only, if that is how it is stated:** X2 is affine in ρ and K_k is convex, so the mixed case follows.

**Spot checks of Prop. 3 found no contradiction.**
- Product states give equality up to local unitaries.
- GHZ gives L equal to the average of R and a bit-flipped copy of R.
- W with a=b=c=1/3 gives spec L = (5,4,3,2,2,1,1,0)/9, against spec R = (9,3,3,3,0,0,0,0)/9. Partial sums are 5,9,12,14 ≤ 9,12,15,18.

Prop. 3 remains the only unverified input. If it were false, A–C would be unproven, not disproven.

**w_ABC ρ ≺ w_ABC P.** This holds because spec ρ ≺ (1,0,…,0).

**Final step.** K_k(H) = max over rank-k projectors Π of tr(ΠH). This is subadditive for any Hermitian summands, so the proof never needs X1, X2 and ρ to commute. Diagonals in bit order (A,B,C):

| s | 000 | 001 | 010 | 100 | 011 | 101 | 110 | 111 |
|---|---|---|---|---|---|---|---|---|
| T1 | wA+wB+wC | wA+wB | wA+wC | wB+wC | wA | wB | wC | 0 |
| T2 | wAB+wAC+wBC | wAB | wAC | wBC | 0 | 0 | 0 | 0 |
| P | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

- **T1 is nonincreasing.** The consecutive steps use, in order: w_C≥0, w_B≥w_C, w_A≥w_B, **w_B+w_C≥w_A**, then w_A≥w_B≥w_C≥0.
- **T2 is nonincreasing.** This uses w_AB≥w_AC≥w_BC≥0.
- **P** is trivially nonincreasing.
- Ties and zero weights are fine.

Y's diagonal is a sum of terms that are all nonincreasing in one common order. So Y's diagonal is nonincreasing in that order too. That gives K_k(Y) = k·w_∅ + K_k(T1) + K_k(T2) + w_ABC·K_k(P), which closes the chain. Traces agree.

**Precision: labeling.** The hypothesis should read "for some labeling."
- Relabeling is legitimate. For a qubit-permutation unitary V_π, X(V_πρV_π†; μ^π) = V_π X(ρ;μ) V_π†, and Y(μ^π) = V_π Y(μ) V_π† because |000⟩ is permutation-symmetric. Since ρ ranges over all states, the conclusion does not depend on the labeling.
- When singleton weights tie, the pair condition depends on how the tie is broken. Example: w_A=w_B=w_C with w_BC>w_AB satisfies A only after swapping A and C.
- The pair ordering is a real hypothesis, not WLOG. If w_A>w_B but w_BC>w_AC, then T1 and T2 rank 100 and 010 in opposite orders. Some K_k then becomes strictly subadditive, and the proof is inconclusive there. The theorem is not refuted in that case.

## Claim B — verified

- D_p = (1−p)·id + p·R, where R(Z) = tr(Z)Q.
- Expanding the tensor power gives D_p^{⊗3} = Σ_I (1−p)^{|I|} p^{3−|I|} (id_I⊗R_{I^c}).
- (id_I⊗R_{I^c})(ρ) = ρ_I⊗Q_{I^c}. Applying the same expansion to P gives exactly Y.
- Σμ = ((1−p)+p)³ = 1, and μ ≥ 0 on [0,1].
- Permutation invariance gives w_l ≡ w₁ and w_lm ≡ w₂. A's conditions then reduce to w₁ ≤ 2w₁, which holds.

**Endpoints.** *Precision:* state the convention 0⁰ = 1.
- p=0 gives ρ ≺ P.
- p=1 gives I/8 ≺ I/8.

## Claim C — verified

**J(Z) = tr(Z)I − Z.** For Z = [[a,b],[c,d]], conjugating Zᵀ by σ_y gives σ_y Zᵀ σ_y = [[d,−b],[−c,a]], which is tr(Z)I − Z.

**J∘D_p = D_{2−p}.** J(D_pZ) = (p−1)Z + ((2−p)/2)tr(Z)I = D_{2−p}(Z). This holds for every real p.

**J^{⊗n} is a conjugated global transpose.**
- (J∘D_{p'})^{⊗n} = J^{⊗n}∘D_{p'}^{⊗n}, by functoriality of ⊗ on linear maps.
- On product operators, J^{⊗n}(⊗Z_i) = U(⊗Z_i)ᵀU, with U = σ_y^{⊗n} = U†.
- By linearity, J^{⊗n}(Z) = UZᵀU for every Z. This is a global transpose, not a partial one.
- Zᵀ has the same characteristic polynomial as Z, so J^{⊗n}(Z) is isospectral to Z.

**Non-CP issue.** Only these linear identities are used. Neither CP nor positivity of J, or of J⊗id, is ever invoked. The negative μ_I that appear for p>1 never enter the argument.

**Range [1,4/3].** For p ∈ [1,4/3], p' = 2−p ∈ [2/3,1]. Then D_p^{⊗3}(ρ) is isospectral to D_{p'}^{⊗3}(ρ). That is ≺ D_{p'}^{⊗3}(P), which is isospectral to D_p^{⊗3}(P).

**Endpoints.**
- p=1 is the fixed point of p ↦ 2−p.
- p=4/3 maps to 2/3. Check: D_{4/3}(|0⟩⟨0|) = diag(1/3,2/3) and D_{2/3}(|0⟩⟨0|) = diag(2/3,1/3).

**"No other n" disclaimer.** This is correct. The symmetry pairs p with 2−p at a fixed n. It proves nothing about other n at a fixed p.

## Strongest correct statement (same proof, no new input)

Write w_{−l} for the weight of the pair not containing l: w_{−A} = w_BC, w_{−B} = w_AC, w_{−C} = w_AB.

**Theorem (assuming Prop. 3).** Let ρ be any three-qubit density operator and μ ≥ 0 with Σμ = 1. Suppose:
- (i) (w_l − w_m)(w_{−l} − w_{−m}) ≤ 0 for all l, m; and
- (ii) w_l ≤ Σ_{j≠l} w_j for every l with w_{−l} > 0.

Then X ≺ Y.

**Why it holds.**
- Write e_l for the string with a single 1 at position l, and f_l for the string with a single 0 at position l.
- (i)+(ii) is exactly the condition that the T1 and T2 diagonals are comonotone. Condition (i) handles the pairs (e_l, e_m). Condition (ii) handles the pairs (e_l, f_l). Every other pair of strings is automatic.
- P and w_∅I are comonotone with everything.
- For comonotone vectors, sorting by their sum gives a common nonincreasing order. A common order is necessary and sufficient for the final equality step.

**Relation to Claim A.** A's hypotheses imply (i)+(ii), and the inclusion is strict. Example: μ_A = 1/2, μ_AB = μ_AC = 1/4.
- This fails A under every labeling, since w_A = 1/8 > 0 = w_B + w_C.
- It satisfies (i)+(ii), since w_{−A} = 0.
- A common order is 000, 001, 010, 011, 100, …

**Corollary.** For every p ∈ [0,2], which includes the full CPTP range [0,4/3], and every three-qubit density operator ρ:

D_p^{⊗3}(ρ) ≺ D_p^{⊗3}(|000⟩⟨000|).

- By unitary covariance of D_p, the reference can be any pure product state.
- For p ∈ (4/3,2], D_p is not CP. The C argument still applies unchanged, because 2−p ∈ [0,2/3).

## Scope

The scope sentences are accurate. One thing cannot be checked here: whether SWTF Eq. 2 is literally this statement, including its parametrization and reference state. Thanks to the covariance remark, any formulation with a pure-product reference over p ∈ [0,4/3] (equivalently λ = 1−p ∈ [−1/3,1]) is covered.
