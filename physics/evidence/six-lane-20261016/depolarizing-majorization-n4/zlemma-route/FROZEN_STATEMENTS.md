# Exact Pauli–Gram / SOS route for the open n = 4 indices — frozen statements and outcome

Frozen 2026-10-17 (host clock), following the parent's direction (exact route; no further float hierarchy levels).
Status: **no exact lemma or certificate closes in this cycle — BLOCKED**, with exact obstructions recorded below.

## 1. Z-lemma (precise statement)

For every 4-qubit state ρ (pure suffices: Z is linear in ρ and K_k is convex) and k = 1, 2, 3, 4:
`K_k(Z(ρ)) ≤ 2 + 2k`, where `Z(ρ) = Σ_{l=1}^{4} Σ_{a∈{x,y,z}} σ_a^{(l)} ρ σ_a^{(l)}`.
Equality holds at |0000⟩: `Z = 4|0000⟩⟨0000| + 2 Σ_l |e_l⟩⟨e_l|`.

**Gram form.** For ρ = |ψ⟩⟨ψ|, `Z = VV†` with columns `v_{(l,a)} = σ_a^{(l)} ψ`. The nonzero spectrum of Z equals that of
the 12×12 matrix `M_{(l,a),(m,b)} = ⟨ψ|σ_a^{(l)} σ_b^{(m)}|ψ⟩ = 1 + B`, where `B = blockdiag_l(i ε_{abc} r^{(l)}_c)` plus
the off-diagonal 3×3 blocks `T^{lm}_{ab} = ⟨σ_a^{(l)} σ_b^{(m)}⟩` (Bloch vectors r, two-body correlations T). Hence the
Z-lemma is equivalent to `K_k(B) ≤ 2 + k` (k ≤ 4). At k = 1 it is equivalent to the operator-norm statement
`‖Σ_l w_l·σ^{(l)}‖_∞ ≤ 2` for all complex `w ∈ ℂ^{12}` with `‖w‖ = 1`.
**Dual form.** `Z(Π) ≤ (2 + 2k)·1` for all 0 ≤ Π ≤ 1 with Tr Π = k.

**Bridge to U_3 and to the target.** `Σ_a σ_a Y σ_a = 2 Tr(Y) 1 − Y` per qubit gives `Z = 2X_3 − 4ρ`, so
`X_3 = 2ρ + Z/2` and `K_k(X_3) ≤ 2 + (2 + 2k)/2 = 3 + k = K_k(T_3)` for k ≤ 4 (and `U_3` is trivial for k ≥ 5).
The Z-lemma therefore implies `U_3(2..4)`. Combined with the certified `U_2(2..4)` and R1, it would give indices
k = 2, 3, 4 for every p ∈ [0, 4/3], leaving only k = 6..10 (which need `U_2(6..10)`).
Numerics (float): `max K_k(X_3 − 2ρ) − (1 + k)` is about −1e-10 for k = 1..4 (`evidence/zlemma_u3.json`).

## 2. Exact obstructions to low-degree certificates

- **Z-map PPT (degree-2, decomposable) relaxation is loose already at k = 1.** The twirled LP objective is
  `obj_S = 48·[|S| = 3]` (closed form, cross-checked against explicit matrices to 4e-14). Exact rational feasible
  points reach 5, 10, 12, 12 against targets 4, 6, 8, 10 (`evidence/zmap_lp_primal_witnesses.json`). So no
  PPT/decomposable certificate exists for the Z-lemma at any k ≤ 4, not even for the k = 1 operator-norm form.
- **The `U_3` map relaxation** is loose by exactly 2, 2, 1 at k = 2, 3, 4 (exact witnesses in
  `frozen-partial-v1/lp1_primal_witnesses.json`). Float level-2 symmetric extension leaves 0.089, 0.231, 0.184.

## 3. Structural reduction R3 (exact identity) and why it does not close

For pure ψ, write the Schmidt form across l | rest: `ψ = √μ_l a_l⊗α_l + √(1−μ_l) b_l⊗β_l` with μ_l ≥ 1/2. Then
`ρ_{¬l} ⊗ 1_l = t_l P_{A_l} + (1 − t_l) Q_l/2`, where `t_l = 2μ_l − 1 ∈ [0,1]`, `P_{A_l} = |α_l⟩⟨α_l| ⊗ 1_l` and
`Q_l = (|α_l⟩⟨α_l| + |β_l⟩⟨β_l|) ⊗ 1_l`. This decomposition was checked numerically to 2e-16. So `X_3` is a convex
combination of the 16 pattern operators `O_L = Σ_{l∈L} P_{A_l} + Σ_{l∉L} Q_l/2`, and
`K_k(X_3) ≤ max_L K_k(O_L)`.

- **Pattern lemma (float, true).** For ψ-derived top Schmidt data, `K_k(O_L) ≤ 3 + k` for all |L| = 0..4 and
  k = 1..4. Worst values are between −1e-7 and −5e-9, with equality at product states; L = ∅ has margin ≥ 1.
- **It is false without the spectral (top-branch) property.** With arbitrary 3-qubit vectors α_l, L = [4] gives
  excess +0.169 at k = 3 and +0.236 at k = 4. With a common ψ but arbitrary local post-selections
  `α_l ∝ (⟨c_l| ⊗ 1)ψ`, the excess is +0.120 and +0.236 (`evidence/logs/u3pat_*.log`).
  So any proof must use the fact that α_l is the TOP Schmidt vector (largest eigenvalue of ρ_l). This is a
  spectral, non-polynomial compatibility condition, which is consistent with low-degree SOS failing.

## 4. Analogue for U_2 (indices 6..10)

The Pauli-twirl expansion is `X_2 = (3/2)ρ + (3/4) Z_1 + (1/4) Z_2`, with `Z_1 = Z` and
`Z_2 = Σ_{l<m} Σ_{a,b} (σ_a^{(l)} σ_b^{(m)}) ρ (σ_a^{(l)} σ_b^{(m)})†` (54 terms). No exact inequality was obtained.
The PPT relaxation is loose by exactly 1 (`lp1_primal_witnesses.json`), the float level-2 relaxation by
0.009–0.110, and the spin-flip Weyl route fails by up to 3 at admissible local spectra.

## 5. Recommendation

The open indices (k = 6..10 for all p; k = 2..4 for p < 2/3) resist PPT/degree-2 SOS (exact obstruction), level-2
DPS (float), and Weyl/local-spectra routes. The only reduction that survives needs a spectral Schmidt-compatibility
argument for which no proof idea exists yet. Recommended: freeze n = 4 as PARTIAL (certified indices) with these
blockers, and move the slot to a materially different target.
