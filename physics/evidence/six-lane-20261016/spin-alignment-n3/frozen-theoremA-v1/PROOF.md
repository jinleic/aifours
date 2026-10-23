# Frozen proof package v1 — Theorem A and Corollary B (UNREVIEWED; awaiting parent primary-source check)

Frozen 2026-10-16 (America/Los_Angeles), lane `physics/evidence/six-lane-20261016/spin-alignment-n3/`.

## Setting

Song–Chen, arXiv:2603.25410v1, Conjecture 2 (eq. 14), case n = 3, d = 2, Q = I/2. For a 3-qubit state ρ and a
probability measure μ on subsets I ⊆ {A,B,C}:
`X = Σ_I μ_I ρ_I ⊗ (I/2)^{⊗I^c}`, `Y = Σ_I μ_I |0⟩⟨0|^{⊗I} ⊗ (I/2)^{⊗I^c}`; claim `X ⪯ Y` (eigenvalue majorization,
equal traces). Write `w_I = μ_I 2^{−|I^c|}`, so `X = Σ_I w_I ρ_I ⊗ 1`, `Y = Σ_I w_I P_I`, `P_I = |0⟩⟨0|^{⊗I} ⊗ 1`.

## Imported result (exact quote, Song–Chen v1 p. 3, eq. 15)

"**Proposition 3** Let a, b, c ≥ 0 with a + b + c = 1, and let ρABC be a three-qubit state. Then
aρAB ⊗ IC + bρAC ⊗ IB + cIA ⊗ ρBC ⪯ a|00⟩⟨00|AB ⊗ IC + b|00⟩⟨00|AC ⊗ IB + cIA ⊗ |00⟩⟨00|BC."

Its proof (pp. 3–4) uses Alhejji–Knill [their ref. 5, Cor. 4.10] (two-summand case) and the polygon inequalities;
we import Prop. 3 as stated. Both sides scale linearly, so the same holds for any a, b, c ≥ 0 (a+b+c = 0 trivial).

## Lemma K (Kronecker sums)

If `H_A, H_B, H_C` are Hermitian on qubits A, B, C, the operators `H_A ⊗ 1 ⊗ 1`, `1 ⊗ H_B ⊗ 1`, `1 ⊗ 1 ⊗ H_C`
commute and `spec(Σ) = {α_i + β_j + γ_k}`. If `spec(H_l) ≺ spec(G_l)` for each l, then
`spec(Σ_l H_l) ≺ spec(Σ_l G_l)`. Proof: `spec(H_l) = Σ_σ c^{(l)}_σ σ(spec G_l)` (Birkhoff/Rado, convex combination of
permutations); the Kronecker sum is multilinear, so `spec(Σ H)` is a convex combination of coordinate permutations of
`spec(Σ G)`, i.e. majorized by it. Applied with `H_l = w_l ρ_l`, `G_l = w_l |0⟩⟨0|`
(`(λ, 1−λ) = λ(1,0) + (1−λ)(0,1)`).

## Theorem A

Relabel so that `w_A ≥ w_B ≥ w_C`. If (i) `w_A ≤ w_B + w_C` and (ii) `w_AB ≥ w_AC ≥ w_BC`, then `X ⪯ Y`.

*Proof.* `X = w_∅ 1 + X_1 + X_2 + w_ABC ρ`, `Y = w_∅ 1 + T_1 + T_2 + w_ABC |000⟩⟨000|` with singleton parts
`X_1 = Σ_l w_l ρ_l ⊗ 1 ⪯ T_1` (Lemma K) and pair parts `X_2 ⪯ T_2` (Prop. 3, weights `w_AB, w_AC, w_BC`);
`w_ABC ρ ⪯ w_ABC |000⟩⟨000|`; identity terms equal. All four targets are diagonal in the computational basis. In the
order `000, 001, 010, 100, 011, 101, 110, 111` (qubits A,B,C):
`T_1 = (w_A+w_B+w_C, w_A+w_B, w_A+w_C, w_B+w_C, w_A, w_B, w_C, 0)` is nonincreasing ⇔ `w_B ≥ w_C`,
`w_A + w_C ≥ w_B + w_C` (⇔ `w_A ≥ w_B`), `w_B + w_C ≥ w_A` (i), `w_A ≥ w_B ≥ w_C`;
`T_2 = (w_AB+w_AC+w_BC, w_AB, w_AC, w_BC, 0, 0, 0, 0)` is nonincreasing ⇔ (ii); `|000⟩⟨000|` and `1` trivially.
Ky Fan sums of commuting diagonal matrices that are nonincreasing in one common order add:
`K_k(Σ targets) = Σ K_k(target)`. With Ky Fan subadditivity,
`K_k(X) ≤ Σ_blocks K_k(block) ≤ Σ_blocks K_k(target) = K_k(Y)` for k = 1..8, and `Tr X = Tr Y`. ∎

## Corollary B (depolarizing channel), convention `D_p(X) = (1−p) X + p Tr(X) I/2`, `0 ≤ p ≤ 4/3`

(a) `0 ≤ p ≤ 1`: `D_p^{⊗3}(ρ) = Σ_I (1−p)^{|I|} p^{3−|I|} ρ_I ⊗ (I/2)^{⊗I^c}`, a permutation-invariant probability
measure; it satisfies (i)–(ii) with equalities, so `D_p^{⊗3}(ρ) ⪯ D_p^{⊗3}(|000⟩⟨000|)`.
(b) `1 < p ≤ 4/3` (**parent-supplied lemma, re-derived here**): for 2×2 X, `σ_y X^T σ_y = Tr(X) I − X`, hence
`σ_y D_p(X)^T σ_y = D_{2−p}(X)`. Tensoring, `D_{2−p}^{⊗3}(Z) = σ_y^{⊗3} D_p^{⊗3}(Z)^T σ_y^{⊗3}` (local transposes
compose to the global transpose), so `D_{2−p}^{⊗3}(ρ)` and `D_p^{⊗3}(ρ)` have identical spectra for every ρ,
including `|000⟩⟨000|`. For `1 < p ≤ 4/3`, `2−p ∈ [2/3, 1)` is covered by (a). Numerical re-check of the identities:
max error ≤ 3e-16 on random inputs (session log). The same spectral identity is used inside Song–Chen's own proof
(their eq. 29–31).
Hence the d = 2, n = 3 case of the depolarizing-output majorization conjecture (Song–Wang–Tomamichel–Fang,
arXiv:2609.37240v1, Eq. (2)) holds for all physical `0 ≤ p ≤ 4/3`. (This p is NOT the total-error convention.)

## Scope and status

Unreviewed. Depends on Song–Chen Prop. 3 as published (not re-proved here). No claim beyond Q = I/2, n = 3, d = 2 and
the weight region of Theorem A; general μ and general Q remain open. Priority not established.
Checks: `../code/aligned_blocks.py alignment` (exact rational check that (i)–(ii) give the common order).
