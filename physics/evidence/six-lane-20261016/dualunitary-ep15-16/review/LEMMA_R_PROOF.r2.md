# FROZEN r2 — candidate proof: every non-2-unitary two-qutrit dual unitary has rank U^Γ ≤ 6, hence e_p ≤ 15/16

**Frozen.** Written once (file mtime = host-clock freeze time; `date` captured just before writing: 2026-10-17
05:06:28 PDT). Never edited afterwards; any later correction goes to an r3 file.

**Provenance.** v1 = SHA-256 263f9df93c9af72aec1588fb072e27ba56d0fb62d39bee6a02813a7a914fa6a8, preserved byte-exact as
`review/LEMMA_R_PROOF.v1.md` (copied from the parent pin `institute/runs/six-lane-2026-10-16/review/
dualunitary-rank-bound-parent-inputs-v1/`; the lane path `review/LEMMA_R_PROOF.md` was edited in place after the
v1 message, and that interim text a05e563b…2f7c is the parent pin `…-inputs-v2`, left unchanged). Companion v1
files preserved byte-exact: `review/LEMMA_R_NORMAL_FORM.v1.md` (37fb700e…e587), `review/REDUCTION.v1.md`
(819001f4…df80).

**Changes relative to v1** (the case analysis §§2–5 is mathematically unchanged):
- (F1) Fact K: v1 called J^{-1}σ_m the spanning vector of the complement. Correct statement: the HS complement of
  the three-Pauli span span{σ_k : k ≠ m} is C·σ_m, and W_0 := J^{-1}σ_m is the RIGHT MULTIPLIER with
  span{σ_k : k ≠ m} = Sym(2)·W_0. Full derivation and primary-source quotations in §0.4.
- (F2) Marginal identity: the exact identity is 9ρ_14 = MM† = (U^Γ†U^Γ)^T. The cycle-1 statement
  "U^ΓU^Γ† ≅ 9ρ_14 (fixed index permutation)" (REDUCTION.v1.md lines 12–13) is false in general;
  U^ΓU^Γ† is a fixed permutation conjugate of (M†M)^T = 9ρ_23. Only rank, spectrum and purity are used,
  and these agree (§0.1).
- (F3) Self-contained objective identity (Theorem A) and T-dual transfer. The exact checks are listed in §6.

**Status.** CANDIDATE PROOF, not promoted. The parent reported two independent mathematical reviews: the generic
branch was ACCEPT-WITH-FIXES, the two fixes being F1 and F2 above; the residual A\*/B\*/S/assembly branch was
ACCEPT. The parent also reported an exact relation re-derivation
(`institute/…/review/qutrit-rank-parent-exact-relations-v1.json`). A primary priority audit and an
independent-vendor complete-claim review are pending. No novelty or priority claim.

## Theorem

Let U ∈ U(9) be dual unitary (U^R unitary) and not 2-unitary. Then rank U^Γ ≤ 6. Hence e_p(U) ≤ 15/16, with
equality iff spec(U^ΓU^Γ†) = {3/2 (×6), 0 (×3)}. U_s(2π/3) = S·U(2π/3) attains 15/16 exactly. The same bound
holds for T-dual unitaries that are not 2-unitary (§0.1). No import of [44] is needed for this form; [44]
Theorem 1 is used only to identify "not 2-unitary" with "outside O9 = LU·P9".

## 0. Setup

### 0.1 Conventions, objective, marginals (exact)

Conventions from the survey arXiv:2508.04777v3, as pinned in README §0.1:
- basis |ij⟩ ↔ 3i+j; ⟨ij|U^R|αβ⟩ = ⟨iα|U|jβ⟩; ⟨iβ|U^Γ|jα⟩ = ⟨iα|U|jβ⟩; S = SWAP;
- e_p(U) = [E(U)+E(US)−E(S)]/E(S), E(U) = 1 − tr[(U^RU^R†)²]/81, E(S) = 8/9;
- D = {U : U^R unitary}, T = {U : U^Γ unitary}; 2-unitary means U, U^R, U^Γ all unitary.

**T-dual transfer.** (US)^R = U^ΓS is an exact matrix identity (checked symbolically in
`evidence/controls_exact.json`). It gives E(US) = 1 − tr[(U^ΓU^Γ†)²]/81. Applied to US it also gives
(US)^Γ = U^RS. So U ↦ US maps D onto T, preserves 2-unitarity, and preserves e_p (the formula is symmetric
under U ↔ US). Every statement about D transfers to T.

**Theorem A.** For U ∈ D, E(U) = 8/9 and tr U^ΓU^Γ† = Σ|U_ij|² = 9. Hence
e_p(U) = 1 − ‖U^ΓU^Γ† − I‖_F²/72 = 1 − (Σ_i s_i² − 9)/72, where s_i are the eigenvalues of U^ΓU^Γ† and Σ s_i = 9.
If rank U^Γ = r, Cauchy–Schwarz gives Σ s_i² ≥ 81/r. For r ≤ 6 this means Σ s_i² ≥ 27/2, so e_p ≤ 15/16, with
equality iff six s_i equal 3/2.

**Four-party picture and the exact marginal identity (F2).** Set ψ(a,b,c,d) := U[(c,d),(a,b)]/3. U unitary ⇔
ρ_12 = I/9, and U^R unitary ⇔ ρ_13 = I/9. The 14|23 flattening is M[(a,d),(b,c)] := 3ψ(a,b,c,d) =
U[(c,d),(a,b)]. Then U^Γ[(c,b),(a,d)] = U[(c,d),(a,b)] = M[(a,d),(b,c)], i.e. U^Γ = ΠM^T with Π the fixed row
permutation (b,c) ↦ (c,b). Consequently:

9ρ_14 = MM† = (U^Γ†U^Γ)^T,    U^ΓU^Γ† = Π(M†M)^TΠ^T.

MM† and M†M have the same nonzero spectrum. So rank U^Γ = rank M = rank ρ_14 = dim span{X_ad},
tr(U^ΓU^Γ†)² = tr(MM†)², and U is 2-unitary iff (additionally) MM† = I. Nothing else is used.
U^ΓU^Γ† is in general NOT a fixed permutation conjugate of 9ρ_14 (parent example U = S(V⊗I), V = diag(1,i,1)).
These identities are verified as polynomial identities in `code/marginal_identity_exact.py`
(fa0846cc…2448) → `evidence/marginal_identity_exact.json` (2d4bb571…ffd4). That check also rejects the wrong
form MM† = (U^ΓU^Γ†)^T.

### 0.2 Normal form, sectors, relations

φ(a,b,c,d) := U[(c,d),(a,b)] and X_ad[b,c] := φ(a,b,c,d) (all indices in {0,1,2}); K := {1,2}. U ∈ D ⇔
(1) Σ_d X_adX_a'd† = δ_aa'I, (2) Σ_d X_a'd†X_ad = δ_aa'I, (3) Σ_a X_adX_ad'† = δ_dd'I, (4) Σ_a X_ad'†X_ad = δ_dd'I.
(The block matrix [X_ad] is U^T and [X_da] is (U^R)^T, each up to a fixed ordering of indices.)

**Normal form (WLOG).** Σ = P²×P² and U^{-1}Σ are 4-dimensional subvarieties of P^8, so they intersect:
U(α⊗β) = λγ⊗δ with |λ| = 1. A local unitary change and a phase give φ(0000) = U[(00),(00)] = 1. Then row and
column (00) of U and of U^R are e_00, i.e. φ vanishes at every point ≠ 0000 where both coordinates of one of the
pairs {12,34,13,24} are 0. Local unitaries, the party permutations below and phases preserve D, 2-unitarity and
rank U^Γ.

**Sectors.**
- Slices: X_00 = 1⊕N_0, X_0d = 0⊕N_d, X_a0 = 0⊕Q_a, and X_ad = [[x_ad, r_ad],[t_ad, Ω_ad]] for a,d ∈ K
  (blocks {0}⊕K).
- 2×2 matrices in (a,d): Q_0 := N_0; R_0 := (x_ad), R_c := (r_ad[c]), T_b := (t_ad[b]), T_0 := R_0,
  Ω^{(bc)} := (Ω_ad[b,c]).
- Spans: A = span{N_0,N_1,N_2}, B = span{N_0,Q_1,Q_2}, C = span{R_0,R_1,R_2}, D = span{R_0,T_1,T_2}.
- Block form, with row blocks ((00) | (0,d),(a,0) | (a,d)) and column blocks ((00) | (0,c),(b,0) | (b,c)):
  M = [[1, 0, n_0],[0, 0, P],[x, 𝐁, Ω]]. P has rows vec N_1, vec N_2, vec Q_1, vec Q_2; 𝐁 has columns vec R_1,
  vec R_2, vec T_1, vec T_2. Write rP := rank P = dim span{N_1,N_2,Q_1,Q_2} and
  rB := rank 𝐁 = dim span{R_1,R_2,T_1,T_2}.

**Relations used.** Each is literally a block of (1)–(4) with one index equal to 0. All are exact polynomial
identities in the 56 free entries and their formal conjugates: `code/relations_exact.py` (8aae0bba…e7c5ac) →
`evidence/relations_exact.json` (88ca9c6e…ec293), 30/30, with 3 mutation controls rejected.
- (U) {N_0,N_1,N_2}, {N_0,Q_1,Q_2}, {R_0,R_1,R_2}, {R_0,T_1,T_2} are unital Kraus triples
  (ΣKK† = ΣK†K = I_2).
- (α) N_0Q_a† + Σ_{d∈K}N_dΩ_ad† = 0;  (γ) N_0†Q_a + Σ_d N_d†Ω_ad = 0;  (β) N_dN_0† + Σ_{a∈K}Ω_adQ_a† = 0;
  (δ) N_0†N_d + Σ_a Q_a†Ω_ad = 0.
- (a,d)-analogues: T_bR_0† + Σ_c Ω^{(bc)}R_c† = 0 and R_0†T_b + Σ_c R_c†Ω^{(bc)} = 0.
- (O1) Σ_{c,d∈K} N_d[b,c] R̄_c[a,d] = 0;  (O2) Σ_{a,b∈K} Q_a[b,c] T̄_b[a,d] = 0;
  (O3) Σ_{b,d∈K} N_d[b,c] T̄_b[a,d] = 0;  (O4) Σ_{a,c∈K} Q_a[b,c] R̄_c[a,d] = 0.

### 0.3 Symmetries and gauges

**Symmetries** (party permutations fixing |0000⟩; they preserve {12|34, 13|24} as a set and fix 14|23):
- (14): A↔B, C↦C^T, D↦D^T, N_0↦N_0, R_0↦R_0^T;
- (23): C↔D, A↦A^T, B↦B^T, N_0↦N_0^T, R_0↦R_0;
- (12)(34): (A,B,N_0)↔(C,D,R_0).

**Gauges.** Local unitaries 1⊕V on single parties keep the normal form. Parties 2,3 act by N ↦ V_2NV_3' on all
(b,c)-matrices; parties 1,4 act by R ↦ V_1RV_4' on all (a,d)-matrices. They also mix the K-labelled members of a
family, which preserves spans. The two gauges are independent.

### 0.4 Fact K (corrected statement F1, derivation, primary sources)

**Fact K.** Let N_0,N_1,N_2 ∈ M_2 satisfy Σ_dN_dN_d† = Σ_dN_d†N_d = I_2, and put A = span{N_d}. Then
A = V·span{σ_k : k ∈ S}·W for some unitaries V, W and some S ⊆ {0,1,2,3}, where σ_0 = I and σ_1,σ_2,σ_3 are the
Paulis. Consequently:
- (a) If dim A = 3, then S = {0,1,2,3}∖{m}. The HS complement of span{σ_k : k ≠ m} is C·σ_m, so A^⊥ = C·Vσ_mW.
  The right multiplier W_0 := J^{-1}σ_m (J = [[0,1],[−1,0]] = iσ_2) gives span{σ_k : k ≠ m} = Sym(2)·W_0,
  hence A = V·Sym(2)·(W_0W). Explicitly, J^{-1}σ_m ∝ σ_2, σ_3, I, σ_1 for m = 0,1,2,3, and
  Sym(2) = span{σ_0,σ_1,σ_3}, so Sym·σ_2 = span{σ_1,σ_2,σ_3}, Sym·σ_3 = span{σ_0,σ_2,σ_3}, Sym·I = Sym and
  Sym·σ_1 = span{σ_0,σ_1,σ_2}. Equivalently, (Sym(2)·W_0)^⊥ = C·JW_0 = C·σ_m.
- (b) If dim A ≤ 2, then span{σ_j,σ_k} = σ_j·span{I, σ_jσ_k}, and σ_jσ_k ∝ σ_l = C_lσ_3C_l† for a unitary C_l.
  So span{σ_j,σ_k} = σ_jC_l·Diag·C_l†, and A ⊆ V'·Diag·W' with V', W' unitary. The case |S| = 1 is a special
  case.
- Also, dim A = 3 ⇒ ‖N_0‖_op < 1. In the SVD gauge, a singular value 1 of N_0 forces N_1, N_2 ∈ C·E_22 (the
  computation of Lemma S), so dim A ≤ 2.

*Proof.* Φ(X) := Σ_dN_dXN_d† is completely positive, trace preserving and unital.
1. (Bloch form.) In the basis {I,σ_1,σ_2,σ_3}, Φ(w_0I + w·σ) = w_0I + (t + Tw)·σ with T a real 3×3 matrix, and
   unitality ⇔ t = 0.
2. (Rotation normal form.) Write T = R_1ΛR_2 with R_1, R_2 ∈ SO(3) and Λ real diagonal. Take the real SVD and
   move signs into Λ: −O ∈ SO(3) whenever O ∈ O(3) has det −1. Each R_i is Ad(U_i) on the traceless part for some
   U_i ∈ SU(2). So Φ = Ad(U_1)∘Φ_Λ∘Ad(U_2), where Φ_Λ := Ad(U_1)^{-1}∘Φ∘Ad(U_2)^{-1} is CPTP and unital and acts
   by σ_k ↦ λ_kσ_k.
3. (Diagonal unital maps are Pauli channels.) Ad(σ_j) acts on σ_k by a sign ε_jk ∈ {±1}: ε_j0 = +1 for all j, and
   for k ∈ {1,2,3}, ε_jk = +1 iff j ∈ {0,k}. The 4×4 matrix H := (ε_jk)^T is an invertible Hadamard matrix, so
   Φ_Λ = Σ_jp_jAd(σ_j) for a unique real p
   with H p = (1,λ_1,λ_2,λ_3)^T. The Choi matrix of Φ_Λ is Σ_jp_j|σ_j⟩⟩⟨⟨σ_j|, and the vectors |σ_j⟩⟩ are
   pairwise orthogonal. So CP ⇔ all p_j ≥ 0, in which case {√p_jσ_j : p_j > 0} is a Kraus family.
4. (The Kraus span is an invariant of Φ.) For any Kraus family {K_e} of Φ, the Choi matrix is
   C_Φ = Σ_{i,j}E_ij⊗Φ(E_ij) = Σ_e|K_e⟩⟩⟨⟨K_e|, with |K⟩⟩ := Σ_ie_i⊗Ke_i. The range of a finite sum of positive
   rank-one matrices is the span of their vectors, so span{|K_e⟩⟩} = range C_Φ depends only on Φ, and K ↦ |K⟩⟩
   is a linear isomorphism. Applying this to {N_d} and to the family {√p_jU_1σ_jU_2} of Ad(U_1)∘Φ_Λ∘Ad(U_2)
   gives A = U_1·span{σ_j : p_j > 0}·U_2.
The consequences (a), (b) are the explicit Pauli computations displayed above. ∎

**Primary sources** (pinned in `sources/`; line numbers refer to the pdftotext `-layout` files):
- M. B. Ruskai, S. Szarek, E. Werner, *An Analysis of Completely-Positive Trace-Preserving Maps on M2*,
  arXiv:quant-ph/0101003v2 (3 Nov 2001). PDF `sources/quant-ph-0101003v2.pdf`, SHA-256
  85ef009e8df2207498f501f13fb2d186d2b1e751b8db7f65874195381b5565cd; text `…layout.txt` 5025dc20…f987.
  - l.170–177: "Since Φ is a linear map on M2, it can also be represented in this basis by a unique 4 × 4 matrix
    T, and Φ is trace-preserving if and only if the first row satisfies t1k = δ1k, i.e., T = (1 0; t T) … so that
    Φ(w0 I + w · σ) = w0 I + (t + Tw) · σ. (2)"
  - l.185–187, 195–202: "When Φ is also positivity-preserving, it maps the subspace of self-adjoint matrices in
    M2 into itself, which implies that T is real. King and Ruskai [13] showed that any such map can be reduced,
    via changes of basis in C2, to the form (3) … Because a unitary change of basis ρ → VρV† on C2 is equivalent
    to a 3-dimensional rotation w → Rw acting on the Pauli matrices, this is equivalent to
    Φ(ρ) = U[Φt,Λ(VρV†)]U†, (4) where U, V ∈ U(2) and Φt,Λ denotes the map corresponding to (3). The reduction to
    (3) is obtained by applying a modification of the singular value decomposition to the 3 × 3 real matrix T".
  - l.998–1001: "II) All |λk| = 1, t = 0. … these four possibilities correspond to 4 points of a tetrahedron.
    Each of these extreme points is a map with exactly one Kraus operator corresponding to the identity or one of
    the three Pauli matrices."
  - l.1162–1163: "In a fixed basis, an arbitrary bistochastic map can be written (uniquely) as a convex
    combination of 4 true extreme points".
    (Bistochastic means unital CPTP, l.142–143.)
- C. King, M. B. Ruskai, *Minimal Entropy of States Emerging from Noisy Quantum Channels*,
  arXiv:quant-ph/9911079v1 (17 Nov 1999). PDF `sources/quant-ph-9911079v1.pdf`, SHA-256
  a709d13ee324e20f6e523fe51b9d319926f5303dce1a1140127363223c68f43b; text `…layout.txt` 61363331…3ef7, whose
  extraction has broken inter-letter spacing (normalised here).
  - l.370–380, 385–388: "The map Φ is unital if and only if t = 0. Thus, any unital stochastic map acting on
    density matrices on C2 can be written in the form Φ(½[I + w·σ]) = ½[I + (Tw)·σ] (11) where T is a real 3×3
    matrix. Using the singular value decomposition (see Appendix A), we can write T = RS (12) where R is a
    rotation and S is self-adjoint. … the rotation R defines a unitary operator U such that for any state ρ,
    Φ(ρ) = U[Φ_S(ρ)]U† (14)".
  - l.393–396: "since S is self-adjoint it can be diagonalized by a change of basis. Hence without loss of
    generality we need henceforth consider only unital stochastic maps whose matrix T defined in (10) is
    diagonal".
- Step 4 (Kraus-span invariance) is proved in full above, so it needs no citation. Steps 1–3 are also proved in
  full above; the quotations are the published form of the normal form.

## 1. Lemmas

**Lemma N1.** If dim A = 3 and Y = (Y_0,Y_1,Y_2) satisfies Σ_dY_dN_d† = 0 = Σ_dN_d†Y_d, then all Y_d ∈ A.
*Proof.* By Fact K(a), gauge A = Sym; the hypotheses are covariant under Y ↦ V'†YW'†, N ↦ V'†NW'†. Then
N_d† = N̄_d. Transposing the second condition gives Σ_dY_d^TN̄_d = 0, and subtracting from the first gives
Σ_d(Y_d − Y_d^T)N̄_d = 0. Writing Y_d − Y_d^T = δ_dJ, this says J·Σ_dδ_dN̄_d = 0, and since the N̄_d are
independent, δ = 0. ∎ (The algebra is checked exactly in `evidence/lemma_T_exact.json`, key N1.)
With (α) and (γ): Q_a, Ω_ad ∈ A. By (12)(34): dim C = 3 ⇒ T_b, Ω^{(bc)} ∈ C (Lemma N1').

**Lemma T.** If u_1Jv_1^T + u_2Jv_2^T = 0 for 2×2 matrices u_i, v_i, then rank(u_1⊗v_1 + u_2⊗v_2) ≤ 2.
Equivalently, a tensor T[s,c,a,d] symmetric in (a,d) with rank_{(s,a)|(c,d)} ≤ 2 has rank_{(s,c)|(a,d)} ≤ 2.
*Proof* (LEMMA_R_NORMAL_FORM.v1.md §2). Both the hypothesis and F := u_1⊗v_1 + u_2⊗v_2 are invariant under
(u_1,u_2) ↦ (u_1,u_2)G, (v_1,v_2) ↦ (v_1,v_2)G^{-T}, and under u_k ↦ hu_k.
- (i) If span{u_1,u_2} contains an invertible matrix, arrange u_1 = I. Then v_1 = −v_2 adj(u) with u := u_2, and
  F = (I⊗v_2)L(u) with L(u) = u⊗I + I⊗u − tr(u)I. Every 3×3 minor of L(u) vanishes identically, so rank F ≤ 2.
- (ii) Otherwise either the span is ≤ 1-dimensional with u_1 singular, or all u_k = a_kb^T, or all
  u_k = ab_k^T. In each case rank F ≤ 2.
All of these identities are checked exactly in `evidence/lemma_T_exact.json`. ∎

**Lemma S.** If ‖N_0‖_op = 1 (or ‖R_0‖_op = 1, by (12)(34)), then rank U^Γ ≤ 6.
*Proof.* Gauge N_0 = diag(1,σ). Then (U) forces N_d = ν_dE_22 and Q_a = κ_aE_22. So X_00 = diag(1,1,σ) and
X_0d, X_a0 ∈ C·E_22, and the nine slices span at most 2 + #{X_ad : a,d ∈ K} = 6 dimensions. ∎

**Rank bounds from spans.** Suppose all rows of the last column block of M lie in a k-dimensional space and all
columns of the last row block lie in an l-dimensional space. Then rank M ≤ (1 + rP) + l and
rank M ≤ (1 + rB) + k. With k = l = 3 and rowspace P ⊆ that space, colspace 𝐁 ⊆ that space, eliminating the
(00) pivot and applying the Marsaglia–Styan formula gives
rank M = 1 + rP + rB + rank(E_𝐁Ω'F_P) ≤ 4 + min(rP, rB).

## 2. Proposition G (dim A = 3 and dim C = 3) ⇒ rank ≤ 6

Gauge A = C = Sym. Lemma N1/N1' give k = l = 3, so rank M ≤ 4 + min(rP, rB). Since ‖N_0‖ < 1, the 2×4 matrix
𝐍[b,(c,d)] = N_d[b,c] (d ∈ K) has rank 2, because 𝐍𝐍† = I − N_0N_0†. With N symmetric, (O1) and (O3) put the four
vectors (S_c[a,d])_{(c,d)}, for S ∈ {R,T} and a ∈ K, into the 2-dimensional space ker 𝐍 (conjugated). The tensor
𝔖[S,c,a,d] := S_c[a,d] is symmetric in (a,d) (C = Sym and T ∈ C), so Lemma T gives rB ≤ 2. Hence rank M ≤ 6.

## 3. Proposition A\* (dim C = 3, dim A ≤ 2, ‖N_0‖ < 1) ⇒ rank ≤ 6

Gauge C = Sym (then T_b, Ω^{(bc)} ∈ Sym by N1') and A ⊆ Diag (Fact K(b)). So N_d = diag(p_d, q_d) with p, q ∈ C³
unit vectors, and p_K := (p_1,p_2) ≠ 0, q_K ≠ 0 because ‖N_0‖ < 1. Write n^{(1)} = p, n^{(2)} = q.
- (O1) gives R_b n̄^{(b)}_K = 0 and (O3) gives T_b n̄^{(b)}_K = 0 (b ∈ K). A symmetric 2×2 matrix with a nonzero
  kernel vector v is a multiple of (Jv)(Jv)^T. So R_b = ρ_bw_bw_b^T and T_b = τ_bw_bw_b^T with w_b := J n̄^{(b)}_K.
- dim C = 3 forces ρ_1ρ_2 ≠ 0 and w_1 ∦ w_2. (U) for C and D gives
  Σ_b(|ρ_b|² − |τ_b|²)‖w_b‖²w_bw_b† = 0, so |τ_b| = |ρ_b| ≠ 0.
- (O4) and (O2) then give Σ_{a∈K}Q_a[b,c]w̄_c[a] = 0 and Σ_aQ_a[b,c]w̄_b[a] = 0 for all b,c ∈ K.
  - For b ≠ c, w̄_b and w̄_c span C², so Q_a[b,c] = 0.
  - For b = c, (Q_a[b,b])_a ∥ n^{(b)}_K.
  So every Q_a (a ∈ K) is diagonal, span{N_1,N_2,Q_1,Q_2} ⊆ Diag, and rP ≤ 2.
- Every column of the last row block lies in C (3-dimensional), so rank M ≤ (1 + rP) + 3 ≤ 6.

dim A = 1 is impossible here: then p ∥ q, contradicting w_1 ∦ w_2.

## 4. Proposition B\* (all of dim A,B,C,D ≤ 2; ‖N_0‖, ‖R_0‖ < 1) ⇒ U 2-unitary or rank ≤ 5

Gauge A ⊆ Diag and C ⊆ Diag: N_d = diag(p_d,q_d) and R_c = diag(r_c,s_c), with all four of p_K, q_K, r_K, s_K
nonzero.
1. (O1) reads n^{(b)}_a·conj(ρ^{(a)}_b) = 0 (ρ^{(1)} = r, ρ^{(2)} = s), i.e. p_1r_1 = p_2s_1 = q_1r_2 = q_2s_2 = 0.
   With all four K-parts nonzero this forces, after swapping the K-bases of parties 1 and 4 if needed,
   **p_2 = q_1 = r_1 = s_2 = 0**: N_1 = p_1E_11, N_2 = q_2E_22, R_1 = s_1E_22, R_2 = r_2E_11, with p_1, q_2, r_2,
   s_1 ≠ 0. In particular dim A = dim C = 2.
2. (O4) gives Q_1e_2 = 0 and Q_2e_1 = 0, so Q_1 = αE_11 + βE_21 and Q_2 = γE_12 + δE_22. (O3) gives T_1e_1 = 0
   and T_2e_2 = 0, so T_1 = x_1E_12 + y_1E_22 and T_2 = x_2E_11 + y_2E_21.
3. (U) for B: |α|²+|β|² = |α|²+|γ|² = |p_1|², |γ|²+|δ|² = |β|²+|δ|² = |q_2|², and αβ̄+γδ̄ = 0; so |β| = |γ|.
   (U) for D: |x_1|²+|x_2|² = |x_2|²+|y_2|² = |r_2|² and |y_1|²+|y_2|² = |x_1|²+|y_1|² = |s_1|².
4. (O2) gives βx_2 = αx_1 = δy_2 = γy_1 = 0.
5. If β = γ = 0: |α| = |p_1| and |δ| = |q_2| are nonzero, so x_1 = y_2 = 0, and all Q_a, T_b are diagonal.
   Entries (1,2) and (2,1) of (α) and (γ) in the diagonal gauge (using p_2 = q_1 = 0, p_1q_2 ≠ 0 and Q_a
   off-diagonal zero) make Ω_ad diagonal in (b,c). The mirrored argument (R, T diagonal, r_1 = s_2 = 0,
   r_2s_1 ≠ 0) makes Ω^{(bc)} diagonal in (a,d). So the rows of the last column block and the columns of the last
   row block all lie in Diag, and rank M ≤ (1 + rP) + 2 ≤ 1 + 2 + 2 = 5.
6. If β ≠ 0 (⇔ γ ≠ 0): x_2 = y_1 = 0, so |x_1| = |r_2| ≠ 0 and |y_2| = |s_1| ≠ 0, hence α = δ = 0.
   - B = span{diag(p_0,q_0), E_21, E_12} has dim ≤ 2 only if N_0 = 0; likewise D forces R_0 = 0. So
     |p_1| = |q_2| = |r_2| = |s_1| = |β| = |γ| = |x_1| = |y_2| = 1.
   - With N_0 = 0, (α) and (γ) give Ω_a1 = ω_aE_22 and Ω_a2 = ω'_aE_11. Then (δ) and (β) with Q_1 = βE_21,
     Q_2 = γE_12 give ω = ω' = 0, so Ω = 0.
   - Then M = [[1,0,0],[0,0,P],[0,𝐁,0]] with P and 𝐁 monomial unitaries (distinct matrix units with unimodular
     coefficients). So MM† = I: **U is 2-unitary**.

## 5. Assembly

Take any maximal-overlap normal form of a dual U.
- If ‖N_0‖ = 1 or ‖R_0‖ = 1: Lemma S.
- Else, if some sector has dimension 3: by the symmetries assume dim C = 3. The symmetries preserve the hypothesis
  that both corners are strict contractions. Then Proposition G (dim A = 3) or Proposition A\* (dim A ≤ 2)
  applies.
- Else all sector dimensions are ≤ 2: Proposition B\*.
In every case rank U^Γ ≤ 6 or U is 2-unitary. ∎

## 6. Verification record (exact; no floating point enters any proof step)

- `code/relations_exact.py` (8aae0bba…e7c5ac) → `evidence/relations_exact.json` (88ca9c6e…ec293): all 30
  relations of §0.2 are blocks of (1)–(4) (polynomial identities). 3 mutation controls are rejected:
  (α) with N_d ↦ N_d^T, (O1) without conjugation, and (U) with the order reversed.
- `code/lemma_T_exact.py` (2550537b…adf3) → `evidence/lemma_T_exact.json` (dc08d040…70cd): Lemma T (invertible
  pencil factorisation; rank L(u) ≤ 2 via 3×3 minors; both singular rulings; tensor ⇔ pencil form; exact random
  instances) and the Lemma N1 identity. Controls: rank 4 without the hypothesis; some 2×2 minor of L(u) is nonzero.
- `code/case_algebra_exact.py` (7ffe251c…aad) → `evidence/case_algebra_exact.json` (b33d47bf…aaa3): the
  computational steps of A\* and B\*. This covers:
  - all 2^8 support patterns of step B\*.1;
  - (O3)/(O4) under pattern I;
  - the (U) and (O2) expansions;
  - Ω = 0 as the unique solution when p_1q_2βγ ≠ 0;
  - off-diagonal Ω forced to 0 when β = γ = 0;
  - PP† and 𝐁𝐁†;
  - the A\* factorisations and solve.
  Controls: Ω is not forced when β = 0; the solve has more than 2 free parameters when w_1 ∥ w_2.
- `code/marginal_identity_exact.py` (fa0846cc…2448) → `evidence/marginal_identity_exact.json` (2d4bb571…ffd4):
  the identities of §0.1 (F2), with the wrong form rejected.
- The attaining gate is checked exactly in `evidence/controls_exact.json` (adafcff9…3281). The parent reports an
  independent Q(√3) verification of it.
- Floating-point material is evidence only: the survey `evidence/search/nfcases_*.jsonl` (main stratum: case G
  only; rank-3/4: case S only; degenerate cases only at 2-unitaries) and `code/scratch/relations_check.py`.
- Not done: formalisation. Pending at the parent: primary priority audit and independent-vendor complete-claim
  review.

## 7. Errata carried by r2

- v1 §0, Fact K parenthetical "(complement spanned by J^{-1}σ_m)" is wrong. The complement of the three-Pauli span
  is C·σ_m, and J^{-1}σ_m is the right multiplier (F1). The normal-form note's longer proof (v1 file
  LEMMA_R_NORMAL_FORM.v1.md, lines 48–51) was already correct.
- REDUCTION.v1.md lines 12–13 (and the same line in later REDUCTION.md revisions), "U^ΓU^Γ† ≅ 9ρ_14 (fixed index
  permutation)", is wrong in general. The correct identity is 9ρ_14 = MM† = (U^Γ†U^Γ)^T, with
  U^ΓU^Γ† = Π(M†M)^TΠ^T (F2). No argument in the lane depended on the wrong form: only rank, spectrum and purity
  were used.
- v1's status line ("computer checks are floating-point sanity checks") is superseded by §6.
