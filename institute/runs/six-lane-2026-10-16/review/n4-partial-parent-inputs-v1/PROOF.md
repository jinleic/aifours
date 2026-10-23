# Frozen package v1 — PARTIAL Ky Fan indices for four-qubit depolarizing-output majorization

Status: **PARTIAL** (certain Ky Fan indices only; NOT the full n = 4 statement). Computer-assisted: exact rational
LP dual certificates plus analytic reductions. Unreviewed at freeze time. Lane
`physics/evidence/six-lane-20261016/depolarizing-majorization-n4/`.

## 0. Target and notation

Target (SWTF arXiv:2609.37240v1 Eq. (2), d = 2, n = 4): for every 4-qubit state ρ and `0 ≤ p ≤ 4/3`,
`λ↓(D_p^{⊗4}(ρ)) ≺ λ↓(D_p^{⊗4}(|0000⟩⟨0000|))`, `D_p(X) = (1−p) X + p Tr(X) 1/2`. `K_k(A)` = sum of the k largest
eigenvalues; Ky Fan: `K_k(A) = max{Tr(ΠA) : 0 ≤ Π ≤ 1, Tr Π = k}`; majorization of equal-trace spectra ⟺
`K_k(·) ≤ K_k(·)` for k = 1..15.

`ρ_I` = marginal on qubit set I; `X_s = Σ_{|I|=s} ρ_I ⊗ 1_{I^c}` (`X_0 = 1`, `X_4 = ρ`); `P_I = |0…0⟩⟨0…0|_I ⊗ 1_{I^c}`;
`T_s = Σ_{|I|=s} P_I` (`T_0 = 1`, `T_4 = |0000⟩⟨0000|`). `U_s(k)`: "`K_k(X_s(ρ)) ≤ K_k(T_s)` for every 4-qubit ρ".

## 1. Expansion and the common-order lemma (Reduction R1)

**Expansion.** Expanding each factor of `D_p^{⊗4}` as `(1−p)·id + p·(Tr(·) 1/2)` and choosing `id` on I gives
`D_p^{⊗4}(ρ) = Σ_s a_s X_s` and `D_p^{⊗4}(|0000⟩⟨0000|) = Σ_s a_s T_s =: Y`, `a_s = (1−p)^s p^{4−s} 2^{s−4}`; for
`p ∈ [0,1]` all `a_s ≥ 0`.

**Common-order lemma (same as n = 3).** Let `G_1, …, G_m` be diagonal in one basis, and suppose a single ordering
`x_1, …, x_16` of the basis makes every diagonal `G_b(x_1) ≥ G_b(x_2) ≥ …` non-increasing. Then for every k the set
`{x_1..x_k}` maximizes `Σ_{i≤k} G_b(x_i)` for every b simultaneously, so `K_k(Σ_b G_b) = Σ_b K_k(G_b)` (ties
included). If moreover `K_k(H_b) ≤ K_k(G_b)` for Hermitian `H_b`, Ky Fan subadditivity gives
`K_k(Σ_b H_b) ≤ Σ_b K_k(H_b) ≤ Σ_b K_k(G_b) = K_k(Σ_b G_b)`.

**Hamming alignment.** `T_s(x) = C(z(x), s)` with `z(x)` = number of zeros of x; this is non-increasing in the
Hamming weight `4 − z`. Every ordering of the 16 strings by Hamming weight (ties arbitrary) is a common
non-increasing order for all `a_s T_s` (`a_s ≥ 0`) and for every non-negative combination of the `T_s`.

**Trivial indices.** `U_0`, `U_4`: `K_k(1) = k`, `K_k(ρ) ≤ 1 = K_k(T_4)`. `U_1` (all k): Kronecker-sum lemma (each
`spec ρ_l ≺ (1,0)`; Birkhoff mixture argument as in the n = 3 package, valid for any n). `U_2(1)`:
`λ_max(X_2) ≤ 6 = K_1(T_2)`; `U_2(k)`, k ≥ 11: `K_k(T_2) = 6 + 12 + 6 = 24 = Tr X_2`. `U_3(1)`: `λ_max(X_3) ≤ 4`;
`U_3(k)`, k ≥ 5: `K_k(T_3) = 4 + 4 = 8 = Tr X_3`.

**Consequence R1.** For `p ∈ [0,1]` and any k at which `U_2(k)` and `U_3(k)` hold,
`K_k(D_p^{⊗4}(ρ)) ≤ Σ_s a_s K_k(X_s) ≤ Σ_s a_s K_k(T_s) = K_k(Y)`.

## 2. Spin flip removes X_3 for p ≥ 2/3 (Reduction R2)

For any 2×2 X, `σ_y X^T σ_y = Tr(X) 1 − X`. Tensoring, `ρ̃ := σ_y^{⊗4} ρ^T σ_y^{⊗4} = Σ_I (−1)^{|I|} ρ_I ⊗ 1_{I^c}
= Σ_s (−1)^s X_s`, a state. Hence for any t, `D = Σ_s (a_s + (−1)^s t) X_s − t ρ̃`. Take `t = a_3`:
`D = D⁺ − a_3 ρ̃`, `D⁺ = b_0 1 + b_1 X_1 + b_2 X_2 + b_4 ρ` with `b_0 = a_0 + a_3`, `b_1 = a_1 − a_3`, `b_2 = a_2 + a_3`,
`b_4 = a_4 + a_3`.

Sign conditions: `b_0, b_2, b_4 ≥ 0` always (p ∈ [0,1]); `b_1 ≥ 0 ⟺ (1−p)p³/8 ≥ (1−p)³p/2 ⟺ p ≥ 2/3` (p ∈ (0,1)).
For `p ∈ [2/3, 1]`: `a_3 ρ̃ ≥ 0` ⇒ `λ_i(D) ≤ λ_i(D⁺)` (Weyl) ⇒ `K_k(D) ≤ K_k(D⁺) ≤ Σ b_s K_k(T_s) = K_k(Y⁺)` with
`Y⁺ = Σ b_s T_s` (common order; uses `U_1`, `U_2(k)`, `U_0`, `U_4`). The same identity for |0000⟩ (`|0000⟩~ =
|1111⟩` up to phase; `Σ_s (−1)^s C(z, s) = [z = 0]`) gives `Y⁺ = Y + a_3 |1111⟩⟨1111|`. `Y(x) = Σ_s a_s C(z(x), s)` is
non-decreasing in z; its smallest entry is `Y(1111) = a_0`, the next ones `a_0 + a_1` (z = 1). Since `a_3 ≤ a_1`,
`Y⁺(1111) = a_0 + a_3` is still a smallest entry of `Y⁺`, so the 15 largest entries of `Y⁺` and `Y` coincide and
`K_k(Y⁺) = K_k(Y)` for k ≤ 15. Hence `U_2(k)` alone gives index k for every `p ∈ [2/3, 1]`.

**Reflection.** `σ_y D_p(X)^T σ_y = D_{2−p}(X)` per qubit, hence `D_{2−p}^{⊗4}(Z) = σ_y^{⊗4} D_p^{⊗4}(Z)^T σ_y^{⊗4}`:
equal spectra for ρ and for |0000⟩. `p ∈ (1, 4/3]` reduces to `2 − p ∈ [2/3, 1)`.

## 3. Twirled PPT relaxation: an exact 16-variable LP

Let N be linear on 4-qubit operators and local-unitary covariant: `N(UXU†) = U N(X) U†` for `U = U_1⊗…⊗U_4`.
Here `N = Φ_s`, `Φ_s(X) = Σ_{|I|=s} (⊗_{l∈I} id_l ⊗ ⊗_{l∉I} (Tr_l(·) 1_l))(X)`, so `Φ_s(ρ) = X_s(ρ)` and
`Φ_s(|0000⟩⟨0000|) = T_s`.

(a) **Bilinear form.** `J := Σ_{ij} |i⟩⟨j| ⊗ N(|i⟩⟨j|)` on `ℋ_σ ⊗ ℋ_Π` satisfies `Tr[(σ ⊗ Π) J] = Tr[Π N(σ^T)]`.
So `sup_ρ K_k(N(ρ)) = sup {Tr[(σ⊗Π) J] : σ state, 0 ≤ Π ≤ 1, Tr Π = k}` (σ = ρ^T ranges over all states).

(b) **Relaxation.** `R_k` = set of ω ≥ 0 on `ℋ_σ⊗ℋ_Π` with `Tr ω = k`, `σ_ω ⊗ 1 − ω ≥ 0` where
`σ_ω := Tr_Π(ω)/k`, `Tr_σ ω ≤ 1`, `ω^{T_Π} ≥ 0`, `(σ_ω ⊗ 1 − ω)^{T_Π} ≥ 0`. It contains every `σ ⊗ Π`
(`σ⊗(1−Π) ≥ 0`, `Tr_σ(σ⊗Π) = Π ≤ 1`, `σ⊗Π^T ≥ 0`, `σ⊗(1−Π)^T ≥ 0`). All constraints are linear or PSD in ω, so
`R_k` is convex. Therefore `sup_ρ K_k(N(ρ)) ≤ LP_k := sup_{ω∈R_k} Tr(Jω)`.

(c) **Symmetry.** `G = {V = Ū ⊗ U : U local unitary}` (Ū on ℋ_σ, U on ℋ_Π). Covariance gives `V J V† = J`
(write `U|i⟩ = Σ_a U_{ai}|a⟩`; the sums over i, j collapse by unitarity). For `V ∈ G`: `VωV† ≥ 0`;
`σ_{VωV†} = Ū σ_ω Ū†` so `σ_{VωV†}⊗1 − VωV† = V(σ_ω⊗1 − ω)V†`; `Tr_σ(VωV†) = U Tr_σ(ω) U†`;
`(V A V†)^{T_Π} = (Ū⊗Ū) A^{T_Π} (Ū⊗Ū)†`. So `R_k` is G-invariant and the objective is G-invariant. By convexity
the Haar twirl `ω_G = ∫ VωV† dV` stays in `R_k` with the same objective. **So restricting to the commutant loses
nothing:** `LP_k = sup` over G-invariant ω ∈ R_k.

(d) **Commutant (why 16 variables suffice).** Per site, `Ū ⊗ U` decomposes `ℂ²⊗ℂ²` into the trivial irrep
(spanned by `|Φ⁺⟩`, since `(Ū⊗U)|Φ⁺⟩ = (1 ⊗ U Ū^T)|Φ⁺⟩ = |Φ⁺⟩`) and the 3-dimensional adjoint irrep, each with
multiplicity one; per-site commutant `= span{Φ⁺, 1−Φ⁺}`. For the product group U(2)^4 acting site-wise the
irreps are tensor products of per-site irreps, still multiplicity-free and pairwise inequivalent, so the commutant
is spanned by the 16 orthogonal projectors `E_S = ⊗_{l∈S} Φ⁺_l ⊗ ⊗_{l∉S} (1−Φ⁺)_l` (S ⊆ {1,2,3,4}), `Σ_S E_S = 1`.
Hence G-invariant `ω = Σ_S c_S E_S`.

(e) **Exact LP data.** `Tr E_S = 3^{4−|S|}`. `Tr_Π Φ⁺ = 1/2·1`, `Tr_Π(1−Φ⁺) = 3/2·1`, so `σ_ω = 1/16` and the
constraints become: `ω ≥ 0 ⟺ c_S ≥ 0`; `σ_ω⊗1 − ω ≥ 0 ⟺ c_S ≤ 1/16`; `Σ_S c_S 3^{4−|S|} = k`;
`Tr_σ ω ≤ 1 ⟺ Σ_S c_S (1/2)^{|S|} (3/2)^{4−|S|} ≤ 1` (redundant). Partial transpose: `Φ⁺^{T_Π} = F/2`,
`(1−Φ⁺)^{T_Π} = 1 − F/2` with F = swap (+1 on the 3-dim symmetric, −1 on the antisymmetric space), so `ω^{T_Π}` is
diagonal in the per-site sym/anti decomposition with eigenvalue `e_τ(c) = Σ_S c_S Π_l g(l∈S, τ_l)`, `g(in,sym) =
1/2`, `g(in,anti) = −1/2`, `g(out,sym) = 1/2`, `g(out,anti) = 3/2`, τ ∈ {sym,anti}^4; the PPT constraints are
`0 ≤ e_τ(c) ≤ 1/16`. Objective: per-site Choi of `id` is `2Φ⁺`, of `Tr(·)1` is `1⊗1`, so
`Tr(J E_S) = Σ_{|I|=s, I⊆S} 2^s 3^{4−|S|} = C(|S|, s) 2^s 3^{4−|S|}`.

(f) **Dual and certificates.** Dual of `max Σ obj_S c_S` subject to `c_S ≤ 1/16 [w_S]`, `Σ 3^{4−|S|} c_S = k [z]`,
`Σ t_S c_S ≤ 1 [y]`, `−e_τ(c) ≤ 0 [u_τ]`, `e_τ(c) ≤ 1/16 [v_τ]`, `c ≥ 0`: any `w, y, u, v ≥ 0`, z real with
`w_S + 3^{4−|S|} z + t_S y + Σ_τ G_{τS}(v_τ − u_τ) ≥ obj_S` for all S gives `LP_k ≤ Σ w_S/16 + k z + y + Σ v_τ/16`
(weak duality, using c ≥ 0). `u2_dual_certificates.json` stores rational dual points; `u2_dual_cert.py` checks them
with exact `fractions` arithmetic: bound = `K_k(T_2)` (6, 9, 12, 15, 18 for k = 1..5; 24 for k = 11..15).

**Controls.** Positive: the bound is attained by |0000⟩ (target values are actual values). Negative/mutation (float
HiGHS, `u2_lp_mutation_controls.log`): dropping the PPT constraints gives 15.25, 19.25, 23.25, 24 at k = 2..5 (targets
9, 12, 15, 18); dropping `c_S ≤ 1/16` gives 12, 18, 24, 30; `Tr_σ ω ≤ 1` is redundant. An independent float build
with explicit 256×256 matrices (`twirl_ppt_lp.py`) reproduces the LP values. At k = 6..10 the exact LP value is
`K_k(T_2) + 1` (LOOSE); for `U_3` at k = 2, 3, 4 it is `K_k(T_3) + 2, 2, 1` (LOOSE).

## 4. Partial theorem (computer-assisted; PARTIAL indices)

For every 4-qubit state ρ:
1. for all `p ∈ [0, 4/3]`: `K_k(D_p^{⊗4}(ρ)) ≤ K_k(D_p^{⊗4}(|0000⟩⟨0000|))` for **k ∈ {1, 5, 11, 12, 13, 14, 15}**
   (R1 with `U_2(5)` from the certificate and trivial `U_2`, `U_3` elsewhere; reflection for p > 1);
2. for `p ∈ [2/3, 4/3]`: additionally **k ∈ {2, 3, 4}** (R2 with `U_2(2..4)` certificates; reflection).
Equivalently: at p ∈ [2/3, 4/3] the full majorization reduces to k = 6..10; at p ∈ (0, 2/3) to k ∈ {2,3,4,6,…,10}.
p = 0, 1 are trivial. k = 1 is also a consequence of King's multiplicativity (SWTF Remark 5, eq. (28), q = ∞).

Not claimed: any index k ∈ {6..10} for any p ∈ (0,1)∪(1,4/3]; k ∈ {2,3,4} for p ∈ (0, 2/3); `U_2(6..10)`, `U_3(2..4)`.
