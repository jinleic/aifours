# Two-qutrit dual unitaries and the 15/16 conjecture: reduction, local theorem, missing lemma (v1, 2026-10-17 PT)

Status: **intermediate (cycle 1 text)**. Update 2026-10-17 (chunk 2): Lemma R of §5 now has a CANDIDATE proof,
unreviewed, in `LEMMA_R_PROOF.md`; with Theorem A it gives the sharp conjecture. The "open"/"conjectural" wording
below is the cycle-1 record. Rigorous statements are marked (R); numerical observations (N) are evidence only.

## 0. Conventions (source-exact)

Survey arXiv:2508.04777v3: `|ij⟩ ↔ 3i+j`; `⟨ij|U^R|αβ⟩ = ⟨iα|U|jβ⟩`; `⟨iβ|U^Γ|jα⟩ = ⟨iα|U|jβ⟩`;
`E(U) = 1 − Tr(U^RU^R†)²/81`, `E(US) = 1 − Tr(U^ΓU^Γ†)²/81`, `E(S) = 8/9`, `e_p = [E(U)+E(US)−E(S)]/E(S)`.
`D = {U ∈ U(9): U^R ∈ U(9)}`, `O9 = {(v1⊗v2)P9(v3⊗v4)}` (= all 2-unitaries by [44] Thm 1, imported).
Four-party picture `ψ(a,b,c,d) = U[(c,d),(a,b)]/3`: U unitary ⇔ `ρ_12 = I/9`; U^R unitary ⇔ `ρ_13 = I/9`;
`U^ΓU^Γ† ≅ 9ρ_14` (fixed index permutation). Self-dual: `U^R = U` ⇔ ψ symmetric under parties 1↔4.

## 1. Objective identity (R)

For U ∈ D, `Tr U^ΓU^Γ† = 9` and `1 − e_p(U) = ‖U^ΓU^Γ† − I‖_F²/72 = (Σσ_i⁴ − 9)/72` (σ_i = singular values
of U^Γ). So `e_p ≤ 15/16 ⇔ Σσ_i⁴ ≥ 27/2 ⇔ Tr ρ_14² ≥ 1/6`. (Exact check at U_s: `evidence/controls_exact.json`.)

## 2. Theorem A (R): rank ≤ 6 forces e_p ≤ 15/16

If U ∈ D and `rank U^Γ ≤ 6` then `e_p(U) ≤ 15/16`, with equality iff `spec(U^ΓU^Γ†) = {3/2 (×6), 0 (×3)}`.
Proof: Cauchy–Schwarz on ≤ 6 nonzero σ_i² summing to 9. ∎

Corollary A1 (R; the thesis [62] Ch.3 bound for self-dual gates, rephrased). If `U^R = U` then `Λ²(C³) ⊆ ker U^Γ`
(for `x = e_j⊗e_α − e_α⊗e_j`: `(U^Γx)_{(i,β)} = U[(i,α),(j,β)] − U[(i,j),(α,β)] = 0`), so rank U^Γ ≤ 6.
Since `((A⊗B)U(C⊗D))^Γ = (A⊗D^T)U^Γ(C⊗B^T)`, the bound holds on the LU-orbit of every self-dual gate.

Attaining gate (R, exact in Q(√3)): `U_s(2π/3) := S·U(2π/3)` (thesis (3.36)); real orthogonal, dual, not
T-dual, `U_s^R = U_s`, `rank U_s^Γ = 6`, `spec(U_s^ΓU_s^Γ†) = {3/2^6, 0^3}`, `e_p = 15/16`; e_p of U(θ) equals
thesis (3.37) symbolically. Not 2-unitary.

Proposition P (R, exact combinatorics, `evidence/enphased_perms_exact.json`). Of the 9! permutation matrices,
8784 are dual and 72 of those are 2-unitary. For every other dual permutation P, the support of P^Γ has term rank
(maximum matching) ≤ 5 (histogram: 3 → 2556, 4 → 5508, 5 → 648). Enphasing `P_θ` keeps duality and the support
of P_θ^Γ, so `rank P_θ^Γ ≤ 5` and `e_p ≤ 1 − (81/5 − 9)/72 = 9/10` for every enphased non-2-unitary dual
permutation and its LU orbit.

## 3. T-dual counterpart (R)

`(US)^R = U^Γ S` (symbolic identity on a generic matrix); `U ↦ US` maps D bijectively onto T and preserves e_p
(e_p(US) = e_p(U) by definition, since (US)S = U); `P9·S = (p1⊗p2)P9(p3⊗p4)` for explicit local permutations,
so O9·S = O9. Every statement for D∖O9 transfers verbatim to T∖O9.

## 4. Theorem L (R, local): see `LOCAL_THEOREM.md`

Near U_s(2π/3) every dual unitary is LU-equivalent to a self-dual one; hence `e_p ≤ 15/16` on a neighbourhood
of U_s in D, D is a smooth 43-manifold there, and `rank J_dual(U_s) = 119`. Exact certificates (sympy identities
+ mod-p rank lower bounds, with controls P9 → 129, SWAP → 81): `evidence/local_theorem_exact.json`.
So U_s(2π/3) is a (non-strict) local maximiser of e_p over D.

## 5. The missing all-gate reduction

**Lemma R (cycle 1: open; now candidate proof, unreviewed, `LEMMA_R_PROOF.md`).** Every U ∈ D∖O9 has `rank U^Γ ≤ 6`.

Equivalent forms: (i) every T-dual V ∉ O9 has operator-Schmidt rank ≤ 6 (V = US); (ii) a four-qutrit pure
state with ρ_12 = ρ_13 = I/9 has rank ρ_14 ≤ 6 or ρ_14 = I/9; (iii) for a 3×3 array of 3×3 matrices X_ad with
[X_ad] and the block transpose [X_da] both unitary, dim span{X_ad} ≤ 6 unless the X_ad are HS-orthonormal.

Lemma R + Theorem A ⇒ the sharp conjecture `max_{D∖O9} e_p = 15/16`, attained by U_s(2π/3); with §3 also on T.
(The thesis remarks after its Conj. 3.3.2 that a possible reason is non-existence of rank-7/8 partial
transposes; Lemma R also excludes rank 9 off O9.)

What does NOT work as the all-gate statement (N): "every U ∈ D∖O9 is LU-equivalent to a self-dual gate"
(true on the whole 43-dimensional stratum sampled; false at some points of a 41-dimensional rank-4 stratum,
where the linear system {w ∈ M_3 : w·Z_bc symmetric for all 14-slices Z_bc} has smallest singular value
0.055 > 0). Those points still satisfy Lemma R (rank 4 ⇒ e_p ≤ 27/32).

Observed structure that a proof must handle (N): D∖O9 has several pieces — the 43-dim main stratum (= LU·SD,
rank 6), 41-dim rank-4 strata, singular lower-rank points, and the gates S·C (C a generic controlled unitary
Σ_a |a⟩⟨a|⊗V_a), which have a 45-dim Zariski tangent space and rank U^Γ = 3 (checked numerically; cf. the count
kn²+nk²−nk = 45 of Deschamps–Nechita–Pellegrini arXiv:1509.06543 Cor. 3.7 on the T-dual side). A uniform proof
must therefore be a single mechanism, not a deformation argument on one component.

Candidate first step in the [44] representation (N). Normal form at a maximal-overlap product state
(U|00⟩ = |00⟩, exact by Chen et al. + LU): K = span{1,2}, `N_d = 3ψ(0,·,·,d)|_{K×K}`, `Q_a = 3ψ(a,·,·,0)|_{K×K}`
(Q_0 = N_0). Exactly, {N_0,N_1,N_2} and {N_0,Q_1,Q_2} are Kraus operators of unital qubit channels (ρ_12 = ρ_13
= I/9 and their complements), and the 14|23 flattening has the block form `[[1/3,0,y],[0,0,N],[z,L,X]]` with
`N = [N_1;N_2;Q_1;Q_2]`, so `rank ρ_14 = 1 + rank N + rank L + rank(coupling)`. Numerically (Newton-polished
normal forms, zero pattern to 10⁻¹⁶; all 33–36 maximal-overlap states of main-stratum points and ~150 of rank-4
and S·controlled points):
**Lemma N (conjectural; not used — the candidate proof in `LEMMA_R_PROOF.md` uses Lemma N1 instead).** Either N_0 = 0 (observed only for P9: then A := span{N_d} and B := span{Q_a} are
complementary 2-planes, rank N = 4) or A = B. On the main stratum moreover span{N_1,N_2} = span{Q_1,Q_2} (2-dim),
rank N = rank L = 2 and the coupling has rank 1, giving rank ρ_14 = 6.
Lemma N alone gives only rank N, rank L ≤ 3 (not ≤ 6 overall); a [44]-style proof would need the finer
main-stratum structure as well.

## 6. Numerical evidence (N; floats, candidates only)

`evidence/search_summary.json` aggregates `evidence/search/*.jsonl` (≈1,300 projected dual points):
- Jacobian rank 119 at random dual points and at U_s (tangent 43; D/LU generically 10-dim); 129 at P9.
- Strata (tangent dim, rank U^Γ): (43,6), (41,4), (33,9) = O9, plus a few singular points (45,3), (45,4),
  (45,5), (36,6). Three apparent (39,8) points were within 3·10⁻⁷ of genuine rank-4 dual points (residual
  4·10⁻¹⁶ after rank-4 alternating projection): unresolved √(residual) singular values; their e_p ≤ 0.77.
- No converged non-O9 point with rank U^Γ ≥ 7, including 600 runs of an optimiser that explicitly rewards
  σ_7..σ_9 under an e_p ≤ 0.99 barrier (`code/seek_rank7.py`).
- Riemannian ascent of e_p on D: max 15/16 (to 10⁻¹⁴) on (43,6) from every start (3 stalls at 0.905), 5/6 on
  (41,4), 1 only on O9. Maximum e_p over all converged non-O9 points: 0.9375000000000067 (float rounding).
- On (43,6): σ_7 stays ≈10⁻¹⁶ under Gauss–Newton-retracted tangent moves; both kernels of U^Γ are (u⊗v)Λ²(C³)
  with u,v unitary; the twist system has a 1-dim solution space spanned by a unitary (P9: smallest singular
  value √2).
- All 9! permutations: dual permutations have rank P^Γ ≤ 5 (random enphasing too) except the 72 2-unitary ones.

## 7. Not claimed

Cycle 1: no proof of Lemma R or of the global conjecture. Chunk 2: candidate proof in `LEMMA_R_PROOF.md`, pending
independent review. Floats are not certificates; no novelty/priority claim (the parent's audit decides).
