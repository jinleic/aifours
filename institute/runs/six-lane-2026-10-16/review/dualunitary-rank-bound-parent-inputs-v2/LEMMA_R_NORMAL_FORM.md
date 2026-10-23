# Lemma R in the maximal-overlap normal form: proof for the generic and split cases (draft v1, 2026-10-17 PT)

Status: **rigorous for cases G and S below; one residual case R\* open.** Lemma R (every U ∈ D∖O9 has
rank U^Γ ≤ 6) and hence e_p ≤ 15/16 follow for every dual unitary having at least one maximal-overlap normal form
in case G or S. The residual case R\* (both corners strict contractions, one side of the normal form degenerate) is
not excluded. Numerically R\* was met only at 2-unitaries (`evidence/search/nfcases_*.jsonl`).

**Update (same day, chunk 2):** the residual case R\* is now handled in `LEMMA_R_PROOF.md` (Proposition A\*: some
sector 3-dimensional; Proposition B\*: all sectors ≤ 2 ⇒ 2-unitary or rank ≤ 5). That file is the candidate full
proof; this draft is kept as the record of cases G and S and of the Lemma T proof it cites.

## 0. Normal form (WLOG, exact)

**Existence of a product-to-product pair.** In P^8 the Segre variety Σ = P²×P² and U^{-1}(Σ) are both
4-dimensional, so they intersect (projective dimension theorem). Hence U(α⊗β) = λ γ⊗δ with unit vectors and
|λ| = 1 (this is also Chen–Duan–Ji–Ying–Yu 2008, used by [44]). Local unitaries and a phase give
**U[(00),(00)] = 1**. LU maps preserve D, O9, rank U^Γ and e_p.

Write φ(a,b,c,d) := U[(c,d),(a,b)] (= 3ψ). Unitarity of U and of U^R with U[(00),(00)] = U^R[(00),(00)] = 1 force
row and column (00) of U and of U^R to be e_00, i.e. **φ vanishes at every point ≠ 0000 having both coordinates of
one of the pairs {1,2}, {3,4}, {1,3}, {2,4} equal to 0**, and φ(0000) = 1.

X-array. X_ad[b,c] := φ(a,b,c,d) (3×3 matrices, a,d ∈ {0,1,2}). Then 𝒳 = [X_ad] (rows (a,b), cols (d,c)) is U^T up
to index order and the block transpose [X_da] is (U^R)^T up to index order, so U ∈ D ⇔
(1) Σ_d X_ad X_a'd† = δ_aa' I, (2) Σ_d X_a'd† X_ad = δ_aa' I, (3) Σ_a X_ad X_ad'† = δ_dd' I, (4) Σ_a X_ad'† X_ad = δ_dd' I.
The 14|23 flattening has rows (a,d), columns (b,c): **rank ρ_14 = rank U^Γ = dim span{X_ad}**.

Sectors (K := span{e_1, e_2}). From the zero pattern: X_00 = 1 ⊕ N_0, X_0d = 0 ⊕ N_d, X_a0 = 0 ⊕ Q_a (a,d ∈ K),
and for a,d ∈ K, X_ad = [[x_ad, r_ad],[t_ad, Ω_ad]] (blocks {e_0} ⊕ K). Set Q_0 := N_0,
R_0[a,d] := x_ad, R_c[a,d] := r_ad[c], T_b[a,d] := t_ad[b] (T_0 := R_0), Ω^{(bc)}[a,d] := Ω_ad[b,c]. All N, Q, Ω_ad are
2×2 in (b,c); all R, T, Ω^{(bc)} are 2×2 in (a,d). Sector spans: A = span{N_0,N_1,N_2}, B = span{N_0,Q_1,Q_2},
C = span{R_0,R_1,R_2}, D = span{R_0,T_1,T_2}.

Exact consequences of (1)–(4) used below (index ranges: d,a ∈ K unless stated):
- (U) unitality: Σ_{d=0}^2 N_dN_d† = Σ N_d†N_d = I_2; same for {N_0,Q_1,Q_2}, {R_0,R_1,R_2}, {R_0,T_1,T_2}.
- (α) N_0Q_a† + Σ_d N_dΩ_ad† = 0, (γ) N_0†Q_a + Σ_d N_d†Ω_ad = 0 [(1),(2) with rows 0 and a, K×K block];
  (β) N_dN_0† + Σ_a Ω_adQ_a† = 0, (δ) N_0†N_d + Σ_a Q_a†Ω_ad = 0 [(3),(4)].
- (O1) Σ_{c,d∈K} N_d[b,c] conj(R_c[a,d]) = 0, (O3) Σ_{b,d∈K} N_d[b,c] conj(T_b[a,d]) = 0 [(1),(2) rows 0,a, K×{0} block];
  (O4) Σ_{a,c} Q_a[b,c] conj(R_c[a,d]) = 0, (O2) Σ_{a,b} Q_a[b,c] conj(T_b[a,d]) = 0 [(3),(4)].
- the (a,d)-sector analogues of (α)–(δ) (e.g. T_bR_0† + Σ_c Ω^{(bc)}R_c† = 0 is the ({0}×K) block of (1) for rows
  a,a' ∈ K; R_0†T_b + Σ_c R_c†Ω^{(bc)} = 0 is the same block of (3)).

Symmetries. The party permutations (14), (23), (12)(34) preserve D, fix the product state |0000⟩ and the normal form,
and preserve rank ρ_14. They act on sectors as (14): A ↔ B, C ↦ C^T, D ↦ D^T; (23): A ↦ A^T, B ↦ B^T, C ↔ D;
(12)(34): (A,B) ↔ (C,D), N_0 ↔ R_0.

## 1. Lemma N1 (qubit row lemma)

Let N_0,N_1,N_2 ∈ M_2 satisfy (U) with dim A = 3. If Y = (Y_0,Y_1,Y_2) satisfies Σ_d Y_dN_d† = 0 and
Σ_d N_d†Y_d = 0, then every Y_d ∈ A.

Proof. A unital qubit channel is unitarily equivalent to a Pauli channel (Ruskai–Szarek–Werner normal form), so
A = V·span{σ_k : k ∈ S}·W with V,W unitary and |S| = 3. Since (Sym(2)·W_0)^⊥ = C·J W_0 (HS complement) and the
complement of span{σ_k : k ∈ S} is C·σ_m (σ_m the missing Pauli), span{σ_k : k ∈ S} = Sym(2)·(J^{-1}σ_m); hence
A = V'·Sym(2)·W' with V', W' unitary. The hypotheses are covariant under
Y ↦ V'†YW'†, N ↦ V'†NW'†, so assume A = Sym(2): N_d^T = N_d and N_d† = N̄_d. Transposing the second condition
gives Σ_d Y_d^T N̄_d = 0; subtracting from the first, Σ_d (Y_d − Y_d^T) N̄_d = 0. Write Y_d − Y_d^T = δ_d J
(J = [[0,1],[−1,0]]); then J·Σ_d δ_d N̄_d = 0, and linear independence of the N̄_d gives δ_d = 0. ∎

Applied to rows a ∈ K via (α),(γ): Q_a, Ω_ad ∈ A. By (12)(34) symmetry, dim C = 3 gives T_b, Ω^{(bc)} ∈ C (Lemma N1').
Also dim A = 3 ⇒ ‖N_0‖_op < 1: if N_0 had singular value 1, (U) would force N_1, N_2 to be multiples of one rank-1
matrix, so dim A ≤ 2.

## 2. Lemma T (2×2×2×2 tensor lemma)

If u_1,u_2,v_1,v_2 ∈ M_2 satisfy u_1Jv_1^T + u_2Jv_2^T = 0, then rank(u_1⊗v_1 + u_2⊗v_2) ≤ 2.
Equivalently: a tensor T[s,c,a,d] (all indices 2-valued), symmetric in (a,d), whose (s,a)|(c,d) flattening has
rank ≤ 2 has (s,c)|(a,d) flattening of rank ≤ 2.

Proof. The hypothesis and the rank are invariant under u_k ↦ Au_kB, v_k ↦ Cv_kB (A,B,C invertible) and under
(u_1,u_2) ↦ (u_1,u_2)G, (v_1,v_2) ↦ (v_1,v_2)G^{-T}. (i) If span{u_1,u_2} contains an invertible matrix, arrange
u_1 = I; then v_1 = v_2 J u^T J = −v_2 adj(u) (u := u_2), and F := I⊗v_1 + u⊗v_2 = (I⊗v_2)(u⊗I + I⊗u − tr(u) I).
The last factor has eigenvalues λ_i + λ_j − λ_1 − λ_2, two of which vanish; if u is a Jordan block it equals N⊗I + I⊗N
(N² = 0), of rank 2. So rank F ≤ 2. (ii) Otherwise every element of span{u_1,u_2} is singular: either the span is ≤ 1-dim
(then F = u_1⊗w with u_1 singular) or all u_k = a_k b^T or all u_k = a b_k^T (the two rulings of {det = 0}), and
F = (Σ_k a_k⊗v_k)(b^T⊗I) or F = (a⊗I)(Σ_k b_k^T⊗v_k). In all cases rank F ≤ 2. ∎

## 3. Theorem G (generic normal form)

If a maximal-overlap normal form of U ∈ D has (dim A = 3 or dim B = 3) and (dim C = 3 or dim D = 3), then
rank U^Γ ≤ 6, hence e_p(U) ≤ 15/16.

Proof. By the symmetries assume dim A = dim C = 3. Lemma N1/N1': all N_d, Q_a, Ω_ad ∈ A and all R_c, T_b, Ω^{(bc)} ∈ C;
gauge (local unitaries 1⊕V on parties 2,3 and on 1,4, which keep the normal form) to A = C = Sym(2).
Block form of the flattening with rows ((00) | (0,d),(a,0) | (a,d)) and columns ((00) | (0,c),(b,0) | (b,c)):
M = [[1, 0, n_0],[0, 0, P],[x, 𝐁, Ω]], P = [N_1;N_2;Q_1;Q_2], 𝐁 = [R_1,R_2,T_1,T_2] (as columns). Every row of the
last column block lies in A and every column of the last row block lies in C. Eliminating the pivot,
rank M = 1 + rP + rB + rank(E_𝐁 Ω' F_P) with Ω' = Ω − x n_0, and the last term is ≤ min(3 − rP, 3 − rB). Hence
**rank M ≤ 4 + min(rP, rB).**
Since ‖N_0‖ < 1, the 2×4 matrix 𝐍[b,(c,d)] := N_d[b,c] (d ∈ K) has rank 2 (𝐍𝐍† = I − N_0N_0†). With N_d symmetric,
(O1) and (O3) say that for S ∈ {R,T} and a ∈ K the vectors (S_c[a,d])_{(c,d)} lie in the 2-dim space ker 𝐍 (conj).
So the tensor 𝔖[S,c,a,d] := S_c[a,d], symmetric in (a,d) because C = Sym, has (S,a)|(c,d) flattening of rank ≤ 2;
Lemma T gives rank_{(S,c)|(a,d)} = dim span{R_1,R_2,T_1,T_2} = rB ≤ 2. Therefore rank M ≤ 6. ∎

## 4. Lemma S (norm-one corner splits)

If ‖N_0‖_op = 1 or ‖R_0‖_op = 1 in some maximal-overlap normal form, then rank U^Γ ≤ 6.

Proof. Say ‖N_0‖ = 1 (the R_0 case follows by (12)(34)). Gauge N_0 = diag(1,σ). (U) for {N_d} and for {N_0,Q_a}
gives N_dN_d†, N_d†N_d, Q_aQ_a†, Q_a†Q_a ≤ diag(0, 1−σ²), so N_d = ν_dE_22 and Q_a = κ_aE_22 (d,a ∈ K). Then
X_00 = diag(1,1,σ) and X_0d, X_a0 ∈ C·E_22, so the nine slices lie in span{diag(1,1,0), E_22} + span{X_ad : a,d ∈ K},
of dimension ≤ 2 + 4 = 6. ∎

## 5. Consequence and residual case

Corollary. If some maximal-overlap normal form of U ∈ D is in case G or case S, then rank U^Γ ≤ 6 and
e_p(U) ≤ 15/16 (Theorem A of REDUCTION.md).

Residual case R\* (open): every maximal-overlap normal form has ‖N_0‖ < 1, ‖R_0‖ < 1 and
[(dim A ≤ 2 and dim B ≤ 2) or (dim C ≤ 2 and dim D ≤ 2)]. Every 2-unitary is in R\* (N_0 = R_0 = 0,
dim A = dim B = dim C = dim D = 2). To finish Lemma R one must show **R\* ⇒ U ∈ O9 (or rank U^Γ ≤ 6)**.
Partial facts in R\*: with dim A ≤ 2, the row relations (α),(γ) no longer force Q ∈ A (the Ω-system with
N_0 = sI, A = Diag, B = V·Diag·V† is solvable for 0 < s < 1, `code/scratch/degenerate_omega.py`), so the border
and KK relations must be used.

Numerical status (floats, evidence only): every maximal-overlap normal form found for main-stratum points is in
case G (dims 3,3,3,3); every one found for rank-4, S·controlled and S·diagonal points is in case S; R\* occurred only
at 2-unitaries. See `evidence/search/nfcases_*.jsonl` and LOG.
