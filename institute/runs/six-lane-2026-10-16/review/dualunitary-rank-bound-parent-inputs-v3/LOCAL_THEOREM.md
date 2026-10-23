# Local maximality of U_s(2π/3): near U_s every dual unitary is LU-equivalent to a self-dual gate

Status: rigorous LOCAL result (draft v1, 2026-10-17 PT), computer-assisted by exact certificates in
`evidence/local_theorem_exact.json` (produced by `code/local_theorem_exact.py`, sympy + exact mod-p ranks; no
floating point). On its own it does NOT prove the global 15/16 conjecture (for the global candidate proof see
`LEMMA_R_PROOF.md`).

**Replay (single command, pinned).** From the lane root:
`../depolarizing/env/bin/python -B code/replay_theorem_L.py`. It checks the SHA-256 of the pinned inputs
(`code/local_theorem_exact.py` b50bf2a4…2bff, `code/gates.py` 8aac87a6…8e), reruns them in a fresh sandbox
`evidence/replay/theorem_L-<host time>/` (modulus p = 1000000007, √3 ↦ 82062379 mod p), and compares every field
with `evidence/theorem_L_manifest.json` and with the pinned output (file SHA f1a73297…7264; canonical SHA without
the wall-time key 95012867…53b1). Replay at host time 2026-10-17T04:50:03-0700: all 25 checks true,
regenerated file byte-identical (`evidence/replay/theorem_L-20261017T045002-0700/receipt.json`).

Conventions as in `REDUCTION.md` §0. `U_s := S·U(2π/3)`, U(θ) = thesis (3.36); U_s is real orthogonal.
`V := {X ∈ M_9(C) : X^R = X}` (complex subspace, real dimension 108), `SD := V ∩ U(9)` (self-dual unitaries),
`G(U) := UU† − I`, `F_dual(U) := (UU† − I, U^RU^R† − I)`, `LU = U(3)^4` acting by `(v1⊗v2)U(v3⊗v4)`.
`tr_1 Y[α,β] = Σ_i Y[(i,α),(i,β)]`, `tr_2 Y[i,j] = Σ_α Y[(i,α),(j,α)]`.

## Theorem L

There is a neighbourhood W of U_s in M_9(C) such that every dual unitary U ∈ D ∩ W is LU-equivalent to a
self-dual unitary. Consequently `rank U^Γ ≤ 6` and `e_p(U) ≤ 15/16` for all U ∈ D ∩ W, with equality at U_s.
Moreover D ∩ W is a smooth 43-dimensional manifold and `rank J_dual(U_s) = 119` exactly.

**Meaning of "local maximiser" (exact statement proved).** Topology: D ⊂ U(9) ⊂ M_9(C) with the norm topology.
(i) *On D:* there is an open set W ∋ U_s of M_9(C) with e_p(U) ≤ e_p(U_s) = 15/16 for every U ∈ D ∩ W.
(ii) *On the LU quotient:* e_p is LU-invariant and each g ∈ LU acts on D as a homeomorphism, so
W' := LU·(D ∩ W) = ∪_g g(D ∩ W) is an open, LU-saturated subset of D containing the whole orbit LU·U_s with
e_p ≤ 15/16 on W'. Since the quotient map π: D → D/LU is open, π(D ∩ W) is an open neighbourhood of [U_s] in
D/LU (quotient topology), and [U_s] is a local maximiser of the induced function there.
(iii) *Non-strict:* equality e_p = 15/16 holds exactly on the points of D ∩ W with spec(U^ΓU^Γ†) = {3/2 (×6), 0 (×3)}
(REDUCTION.md Theorem A); this set contains the orbit LU·U_s. Whether [U_s] is isolated in the equality locus
of D/LU is not claimed. No size of W is certified (the argument is an inverse-function-theorem argument).

## Certified facts (exact)

- A1 (symbolic identity, generic X with U := (X + X^R)/2 ∈ V): `tr_1(UU†) = (tr_2(U†U))^T`.
  Control: fails for generic non-self-dual X. (Meaning: for U ∈ V the four-party state is symmetric under
  1↔4, so ρ_4 = ρ_1; `tr_1(UU†) = 9ρ_4`, `tr_2(U†U) = 9ρ_1^T`.)
- A2: U_s unitary, `U_s^R = U_s`, U_s real.
- A3: for the 8 traceless Hermitian basis matrices k_j (E_ij+E_ji, i(E_ij−E_ji), diag(1,−1,0), diag(0,1,−1)),
  `H_j := I⊗k_j − U_s(k_j^T⊗I)U_s^T` is Hermitian and `(H_jU_s)^R = −H_jU_s`.
  Control: replacing k^T by k breaks the identity for the 3 non-symmetric k_j.
- A4: `M_ij := tr(k_i tr_1 H_j) − tr(k_i^T tr_2(U_s^T H_j U_s))` has `det M = 3^17/4 ≠ 0`.
- B1: `rank J_dual(U_s) ≥ 119` (rank mod p = 10^9+7 with √3 ↦ 82062379; a minor nonzero mod a prime ideal is
  nonzero over Q(√3)). Controls: same code gives 129 at P9 (prior lane's exact value) and 81 at SWAP.
- B2: `rank (dG_{U_s}|_V) ≥ 73`.  B5: the H_j are linearly independent (rank ≥ 8).
- B3: the 36 LU-generator vectors `ξ·U_s` span ≥ 33 dimensions; the four phase generators coincide (exact),
  so `dim T_LU = 33`.  B4: `rank (R − id)|_{T_LU} ≥ 8`.

## Proof

**Step 1 (SD is a 35-manifold near U_s).** For X ∈ V, `tr(H_j dG_{U_s}(X)) = 2 Re⟨H_jU_s, X⟩_HS = 0` because
`H_jU_s` lies in the (−1)-eigenspace of the HS-isometric involution R (A3), which is orthogonal to V. So
`im dG_{U_s}|_V ⊆ 𝓗^⊥ =: W` where `𝓗 = span{H_j}` has dimension 8 (B5); with B2, `im = W` and
`dim ker = 108 − 73 = 35`. Let `F := P_W∘G|_V`; F is a submersion at U_s, so `Z' := F^{-1}(0)` is a smooth
35-manifold near U_s containing SD. Conversely let U ∈ Z' be close to U_s; then `G(U) ∈ 𝓗`. A1 with
`UU† = I + G(U)` and `U†U = I + U^{-1}G(U)U` gives, for every traceless Hermitian k,
`ℒ_U(G(U))_k := tr(k tr_1 G(U)) − tr(k^T tr_2(U^{-1}G(U)U)) = 0`. The linear map `ℒ_U|_𝓗` depends
continuously on U and equals M (A4) at U_s, so it is invertible near U_s; hence G(U) = 0 and U ∈ SD.
Thus SD = Z' near U_s and `T_{U_s}SD = ker dG_{U_s}|_V` (dimension 35).

**Step 2 (LU·SD contains a 43-dimensional submanifold through U_s).** `T_LU ⊆ T_{U_s}U(9) = ker dG_{U_s}`, so
`T_LU ∩ T_{U_s}SD = T_LU ∩ V = ker (R − id)|_{T_LU}`, of dimension ≤ 33 − 8 = 25 (B3, B4). Hence
`dim(T_LU + T_{U_s}SD) ≥ 33 + 35 − 25 = 43`. The map `Π: LU × SD → M_9, (g,V) ↦ g·V` is smooth near (e,U_s)
(Step 1) with `im dΠ = T_LU + T_{U_s}SD`; restricting Π to a 43-dimensional submanifold through (e,U_s) on
whose tangent space dΠ is injective gives an embedded 43-manifold `N ⊆ LU·SD ⊆ D` through U_s.

**Step 3 (D = N near U_s).** By B1 pick 119 real components of F_dual with independent differentials at U_s;
their common zero set Z is a smooth 43-manifold near U_s with D ⊆ Z. Since N ⊆ D ⊆ Z and dim N = dim Z = 43,
the inclusion N ↪ Z is a local diffeomorphism at U_s, so N contains a neighbourhood of U_s in Z. Therefore,
near U_s, `D = Z = N ⊆ LU·SD`, `rank J_dual(U_s) = 119` and `ker J_dual(U_s) = T_LU + T_{U_s}SD`.

**Conclusion.** Every U ∈ D near U_s equals g·V with V self-dual; by REDUCTION.md Corollary A1,
`rank U^Γ = rank V^Γ ≤ 6`, and Theorem A gives `e_p(U) ≤ 15/16`. ∎

## Remarks and limits

- The equality locus near U_s (six equal nonzero singular values of U^Γ) is non-trivial (contains the LU orbit
  of U_s), so U_s is a non-strict local maximiser of e_p on D in the sense (i)–(iii) above.
- Analytic continuation: on the open subset of D where D is locally cut out by 119 independent polynomial
  equations (a real-analytic 43-manifold), the 7×7 minors of U^Γ vanish identically on the connected component
  containing U_s. This component is not identified explicitly, and numerically D∖O9 also has other components
  (e.g. a 41-dimensional rank-4 stratum where the twisted self-duality fails). So this does not give the global
  conjecture.
- The same certificate scheme applies verbatim at any other self-dual point where the analogous ranks are
  attained; it is a local statement only.
