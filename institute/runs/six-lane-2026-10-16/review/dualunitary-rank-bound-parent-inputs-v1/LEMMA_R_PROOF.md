# Candidate proof: every non-2-unitary two-qutrit dual unitary has rank U^Γ ≤ 6, hence e_p ≤ 15/16 (v1, 2026-10-17 PT)

Status: **CANDIDATE PROOF** (worker-written, not yet independently reviewed; computer checks are floating-point
sanity checks of the identities used, not certificates). Supersedes the residual-case status of
`LEMMA_R_NORMAL_FORM.md` (kept for history).

## Theorem

Let U ∈ U(9) be dual unitary (U^R unitary) and not 2-unitary. Then rank U^Γ ≤ 6, so (REDUCTION.md Theorem A)
e_p(U) ≤ 15/16, with equality iff spec(U^ΓU^Γ†) = {3/2 (×6), 0 (×3)}. U_s(2π/3) = S·U(2π/3) attains 15/16 exactly.
By U ↦ US the same holds for T-dual unitaries. No import of [44] is needed for this form; [44] Theorem 1 only
identifies "not 2-unitary" with "outside O9".

## 0. Setup

Conventions as in REDUCTION.md. φ(a,b,c,d) := U[(c,d),(a,b)]; X_ad[b,c] := φ(a,b,c,d) (a,b,c,d ∈ {0,1,2});
K := {1,2}. U ∈ D ⇔ the biunitarity relations
(1) Σ_d X_adX_a'd† = δ_aa'I, (2) Σ_d X_a'd†X_ad = δ_aa'I, (3) Σ_a X_adX_ad'† = δ_dd'I, (4) Σ_a X_ad'†X_ad = δ_dd'I
(𝒳 = [X_ad] is U^T and [X_da] is (U^R)^T up to index order). rank U^Γ = rank ρ_14 = dim span{X_ad}, because the
14|23 flattening M[(a,d),(b,c)] = X_ad[b,c] is U^Γ up to transposition and index order. U is 2-unitary iff, in
addition, MM† = I (i.e. U^Γ unitary).

**Normal form (WLOG).** Σ = P²×P² and U^{-1}Σ are 4-dimensional subvarieties of P^8, hence intersect: U(α⊗β) =
λγ⊗δ, |λ| = 1. A local unitary change and a phase give φ(0000) = U[(00),(00)] = 1. Then row/column (00) of U and of
U^R are e_00, i.e. φ vanishes at all points ≠ 0000 with both coordinates of a pair in {12,34,13,24} equal to 0.
Local unitaries, the party permutations below and phases preserve D, 2-unitarity and rank U^Γ.

**Sectors.** X_00 = 1⊕N_0, X_0d = 0⊕N_d, X_a0 = 0⊕Q_a, X_ad = [[x_ad, r_ad],[t_ad, Ω_ad]] (a,d ∈ K; blocks {0}⊕K).
Q_0 := N_0; R_0 := (x_ad), R_c := (r_ad[c]), T_b := (t_ad[b]), T_0 := R_0, Ω^{(bc)} := (Ω_ad[b,c]) (2×2 in (a,d)).
A = span{N_0,N_1,N_2}, B = span{N_0,Q_1,Q_2}, C = span{R_0,R_1,R_2}, D = span{R_0,T_1,T_2}. Writing the
flattening with row blocks ((00) | (0,d),(a,0) | (a,d)) and column blocks ((00) | (0,c),(b,0) | (b,c)):

M = [[1, 0, n_0],[0, 0, P],[x, 𝐁, Ω]],  P = rows vec N_1, vec N_2, vec Q_1, vec Q_2;  𝐁 = columns vec R_1, vec R_2,
vec T_1, vec T_2;  rP := rank P = dim span{N_1,N_2,Q_1,Q_2}, rB := rank 𝐁 = dim span{R_1,R_2,T_1,T_2}.

**Relations used** (each is a block of (1)–(4) with one index 0; float-checked to 3·10⁻¹⁵ on normal forms of
main, rank-4, controlled and 2-unitary points, `code/scratch/relations_check.py`):
- (U) {N_0,N_1,N_2}, {N_0,Q_1,Q_2}, {R_0,R_1,R_2}, {R_0,T_1,T_2} are unital Kraus triples (ΣKK† = ΣK†K = I_2).
- (α) N_0Q_a† + Σ_{d∈K}N_dΩ_ad† = 0, (γ) N_0†Q_a + Σ_d N_d†Ω_ad = 0, (β) N_dN_0† + Σ_{a∈K}Ω_adQ_a† = 0,
  (δ) N_0†N_d + Σ_a Q_a†Ω_ad = 0; and the (a,d)-analogues T_bR_0† + Σ_c Ω^{(bc)}R_c† = 0, R_0†T_b + Σ_c R_c†Ω^{(bc)} = 0.
- (O1) Σ_{c,d∈K} N_d[b,c] R̄_c[a,d] = 0, (O2) Σ_{a,b∈K} Q_a[b,c] T̄_b[a,d] = 0,
  (O3) Σ_{b,d∈K} N_d[b,c] T̄_b[a,d] = 0, (O4) Σ_{a,c∈K} Q_a[b,c] R̄_c[a,d] = 0.

**Symmetries** (party permutations fixing |0000⟩): (14): A↔B, C↦C^T, D↦D^T, N_0↦N_0, R_0↦R_0^T;
(23): C↔D, A↦A^T, B↦B^T, N_0↦N_0^T; (12)(34): (A,B,N_0)↔(C,D,R_0).

**Gauges.** Local unitaries 1⊕V on single parties keep the normal form. Parties 2,3 act by N ↦ V_2 N V_3' on all
(b,c)-matrices; parties 1,4 by R ↦ V_1 R V_4' on all (a,d)-matrices (and they mix the K-labelled members of a family,
which preserves spans). The two gauges are independent.

**Fact K** (Pauli normal form of unital qubit channels). A Kraus span of a unital qubit channel is
V·span{σ_k : k ∈ S}·W with V,W unitary. Hence dim 3 ⇒ V'·Sym(2)·W' (complement spanned by J^{-1}σ_m), and dim ≤ 2 ⇒
contained in V''·Diag·W''. Also dim A = 3 ⇒ ‖N_0‖_op < 1 (a singular value 1 of N_0 forces N_1,N_2 to be multiples of
one rank-one matrix by (U)).

## 1. Lemmas

**Lemma N1.** If dim A = 3 and Y = (Y_0,Y_1,Y_2) satisfies Σ_dY_dN_d† = 0 = Σ_dN_d†Y_d, then all Y_d ∈ A.
(Gauge A = Sym; transposing the second condition and subtracting gives Σ_d (Y_d − Y_d^T)N̄_d = 0, so the
antisymmetric parts δ_dJ satisfy Σ δ_dN̄_d = 0, whence δ = 0.) With (α),(γ): Q_a, Ω_ad ∈ A. By (12)(34):
dim C = 3 ⇒ T_b, Ω^{(bc)} ∈ C (Lemma N1').

**Lemma T.** u_1Jv_1^T + u_2Jv_2^T = 0 ⇒ rank(u_1⊗v_1 + u_2⊗v_2) ≤ 2 (proof in LEMMA_R_NORMAL_FORM.md §2:
reduce to u_1 = I, then F = (I⊗v_2)(u⊗I + I⊗u − tr(u)I); singular pencils by the two rulings of {det = 0}).
Equivalently: a tensor T[s,c,a,d] symmetric in (a,d) with rank_{(s,a)|(c,d)} ≤ 2 has rank_{(s,c)|(a,d)} ≤ 2.

**Lemma S.** If ‖N_0‖_op = 1 (or ‖R_0‖_op = 1, by (12)(34)) then rank U^Γ ≤ 6.
(Gauge N_0 = diag(1,σ); (U) forces N_d = ν_dE_22, Q_a = κ_aE_22; then X_00 = diag(1,1,σ), X_0d,X_a0 ∈ C·E_22 and the
nine slices span ≤ 2 + #{X_ad : a,d ∈ K} = 6 dimensions.)

**Rank bounds from spans.** If all rows of the last column block of M lie in a k-dim space and all columns of the
last row block lie in an l-dim space, then rank M ≤ (1 + rP) + l and rank M ≤ (1 + rB) + k; with k = l = 3 the
pivot/Marsaglia–Styan formula gives rank M = 1 + rP + rB + rank(E_𝐁Ω'F_P) ≤ 4 + min(rP, rB).

## 2. Proposition G (dim A = 3 and dim C = 3) ⇒ rank ≤ 6

Gauge A = C = Sym. Lemma N1/N1' give k = l = 3, so rank M ≤ 4 + min(rP, rB). Since ‖N_0‖ < 1, the 2×4 matrix
𝐍[b,(c,d)] = N_d[b,c] (d ∈ K) has rank 2 (𝐍𝐍† = I − N_0N_0†). With N symmetric, (O1) and (O3) put the four vectors
(S_c[a,d])_{(c,d)}, S ∈ {R,T}, a ∈ K, into the 2-dim space ker 𝐍 (conjugated). The tensor 𝔖[S,c,a,d] := S_c[a,d] is
symmetric in (a,d) (C = Sym, T ∈ C), so Lemma T gives rB ≤ 2. Hence rank M ≤ 6.

## 3. Proposition A\* (dim C = 3, dim A ≤ 2, ‖N_0‖ < 1) ⇒ rank ≤ 6

Gauge C = Sym (then T_b, Ω^{(bc)} ∈ Sym by N1') and A ⊆ Diag: N_d = diag(p_d, q_d), p,q ∈ C³ unit vectors with
p_K := (p_1,p_2) ≠ 0, q_K ≠ 0 (‖N_0‖ < 1). Write n^{(1)} = p, n^{(2)} = q.
- (O1) gives R_b n̄^{(b)}_K = 0, (O3) gives T_b n̄^{(b)}_K = 0 (b ∈ K). A symmetric 2×2 matrix with a nonzero kernel
  vector v is a multiple of (Jv)(Jv)^T, so R_b = ρ_b w_bw_b^T, T_b = τ_b w_bw_b^T with w_b := J n̄^{(b)}_K.
- dim C = 3 forces ρ_1ρ_2 ≠ 0 and w_1 ∦ w_2. (U) for C and D gives Σ_b(|ρ_b|² − |τ_b|²)‖w_b‖²w_bw_b† = 0, so
  |τ_b| = |ρ_b| ≠ 0.
- (O4) and (O2) then give Σ_{a∈K} Q_a[b,c] w̄_c[a] = 0 and Σ_a Q_a[b,c] w̄_b[a] = 0 for all b,c ∈ K. For b ≠ c the two
  vectors w̄_b, w̄_c span C², so Q_a[b,c] = 0; for b = c, (Q_a[b,b])_a ∥ n^{(b)}_K. So every Q_a (a ∈ K) is diagonal and
  span{N_1,N_2,Q_1,Q_2} ⊆ Diag: rP ≤ 2.
- Every column of the last row block lies in C (3-dim), so rank M ≤ (1 + rP) + 3 ≤ 6.
(dim A = 1 is impossible here: then p ∥ q, contradicting w_1 ∦ w_2.)

## 4. Proposition B\* (all of dim A,B,C,D ≤ 2; ‖N_0‖, ‖R_0‖ < 1) ⇒ U 2-unitary or rank ≤ 5

Gauge A ⊆ Diag and C ⊆ Diag: N_d = diag(p_d,q_d), R_c = diag(r_c,s_c), all four of p_K,q_K,r_K,s_K nonzero.
1. (O1) reads n^{(b)}_a conj(ρ^{(a)}_b) = 0 (ρ^{(1)} = r, ρ^{(2)} = s), i.e. p_1r_1 = p_2s_1 = q_1r_2 = q_2s_2 = 0. With all
   four K-parts nonzero this forces (after swapping the K-bases of parties 1 and 4 if needed)
   **p_2 = q_1 = r_1 = s_2 = 0**: N_1 = p_1E_11, N_2 = q_2E_22, R_1 = s_1E_22, R_2 = r_2E_11 (p_1,q_2,r_2,s_1 ≠ 0).
   (In particular dim A = dim C = 2.)
2. (O4): Q_1e_2 = 0, Q_2e_1 = 0, so Q_1 = αE_11 + βE_21, Q_2 = γE_12 + δE_22. (O3): T_1e_1 = 0, T_2e_2 = 0, so
   T_1 = x_1E_12 + y_1E_22, T_2 = x_2E_11 + y_2E_21.
3. (U) for B: |α|²+|β|² = |α|²+|γ|² = |p_1|², |γ|²+|δ|² = |β|²+|δ|² = |q_2|², αβ̄+γδ̄ = 0 (so |β| = |γ|). (U) for D:
   |x_1|²+|x_2|² = |x_2|²+|y_2|² = |r_2|², |y_1|²+|y_2|² = |x_1|²+|y_1|² = |s_1|².
4. (O2) gives βx_2 = αx_1 = δy_2 = γy_1 = 0.
5. If β = γ = 0: |α| = |p_1|, |δ| = |q_2| are nonzero, so x_1 = y_2 = 0: all Q_a, T_b are diagonal. Then (α),(γ) in the
   diagonal gauge (entries (1,2),(2,1), using p_2 = q_1 = 0, p_1q_2 ≠ 0, Q_a off-diagonal zero) give Ω_ad diagonal in
   (b,c); the mirrored argument (R, T diagonal, r_1 = s_2 = 0, r_2s_1 ≠ 0) gives Ω^{(bc)} diagonal in (a,d). Hence rows of
   the last column block lie in Diag (2-dim) and columns of the last row block lie in Diag, and
   rank M ≤ (1 + rP) + 2 ≤ 1 + 2 + 2 = 5.
6. If β ≠ 0 (⇔ γ ≠ 0): x_2 = y_1 = 0, so |x_1| = |r_2| ≠ 0, |y_2| = |s_1| ≠ 0, hence α = δ = 0. Then
   B = span{diag(p_0,q_0), E_21, E_12} has dim ≤ 2 only if N_0 = 0; likewise D forces R_0 = 0. So |p_1| = |q_2| =
   |r_2| = |s_1| = |β| = |γ| = |x_1| = |y_2| = 1. With N_0 = 0, (α),(γ) give Ω_a1 = ω_aE_22, Ω_a2 = ω'_aE_11, and (δ),(β)
   with Q_1 = βE_21, Q_2 = γE_12 give ω = ω' = 0: Ω = 0. Then M = [[1,0,0],[0,0,P],[0,𝐁,0]] where P and 𝐁 are monomial
   unitaries (distinct matrix units with unimodular coefficients), so MM† = I: **U is 2-unitary**.

## 5. Assembly

Take any maximal-overlap normal form of a dual U.
- If ‖N_0‖ = 1 or ‖R_0‖ = 1: Lemma S.
- Else, if some sector has dimension 3: by the symmetries assume dim C = 3; then Proposition G (dim A = 3) or
  Proposition A\* (dim A ≤ 2) applies.
- Else all sector dimensions are ≤ 2: Proposition B\*.
In every case rank U^Γ ≤ 6 or U is 2-unitary. ∎

## 6. What is and is not verified

- Every identity in §0 was checked numerically on Newton-polished normal forms (residuals ≤ 3·10⁻¹⁵); the case tree
  matches the float survey (main stratum: case G only; rank-4/controlled/S·diag: case S only; R\*/B\* only at
  2-unitaries; `evidence/search/nfcases_*.jsonl`).
- Not yet done: independent hostile review; exact (non-float) re-derivation of the relation list by a second
  implementation; formalisation. Fact K is cited (Ruskai–Szarek–Werner / King–Ruskai normal form), not re-proved.
- No novelty or priority claim.
