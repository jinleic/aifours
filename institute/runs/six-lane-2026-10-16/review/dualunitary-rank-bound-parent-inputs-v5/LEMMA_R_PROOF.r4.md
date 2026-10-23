# FROZEN r4 — candidate proof: every non-2-unitary two-qutrit dual unitary has rank U^Γ ≤ 6, hence e_p ≤ 15/16

**Frozen (final revision requested by the parent).** Composed from a byte copy of r3 (`cp` at 2026-10-17 05:52:37
PDT, captured `date`) and frozen at this file's mtime (host clock). Its SHA-256 is recorded outside the file
(README §1, evidence/LOG.md, evidence/SHA256SUMS.txt). Never edited after the freeze. r3 is untouched.

**Diff from r3 — editorial only.** The substantive case analysis of §§2–5 is unchanged. r4 applies the 12 minor
findings of the complete Claude CLI claude-opus-5-5 review of r3
(`institute/runs/six-lane-2026-10-16/review/qutrit-sharp-claude-complete-r3-review-v1.note.md`), mostly in that
review's own words:
- (E1) §0.4, Fact K proof step 1: the Bloch formula is corrected to Φ(w_0I + w·σ) = w_0I + (w_0t + Tw)·σ. r3 had
  (t + Tw), which is wrong when w_0 ≠ 1 and t ≠ 0; there is no downstream effect, because the same step imposes
  t = 0. A bracketed note after the quoted RSW eq. (2) records the same point; the quotation itself is unchanged.
- (E2) §1, Lemma N1 now assumes that {N_d} is a unital Kraus triple. Its application names Y = (Q_a, Ω_a1, Ω_a2),
  uses the adjoint of (α) together with (γ), and writes out the N1′ form of the (a,d)-analogues.
- (E3) §1, Lemma T: covariance under u_k ↦ hu_k is stated for invertible h, with F ↦ (h⊗I)F.
- (E4) §1, Lemma T case (i): a short proof that rank L(u) ≤ 2 for every u (conjugation, diagonal and Jordan forms)
  replaces the bare assertion. One-line derivations of v_1 = −v_2 adj(u) and of the factorisation are added.
- (E5) §1, Lemma T case (ii): the rank bounds for a span of dimension ≤ 1 and for the two rulings (totally isotropic
  planes of det) are written out.
- (E6) §3, Proposition A\*: the one-line derivation of the bracket equations from (O4) and (O2), using ρ_c, τ_b ≠ 0
  and the independence of w̄_1, w̄_2.
- (E7) §4, Proposition B\* step 1: the two implication chains giving the two support patterns, and the swap that maps
  the second pattern to the first.
- (E8) §5: "maximal-overlap normal form" is replaced by "any normal form of §0.2 (φ(0000) = 1)".
- (E9) §0.2: the projective dimension theorem is stated, with U^{-1}Σ ≅ Σ.
- (E10) §W, W1: attainment is certified by the printed table itself, independently of its identification with
  S·U(2π/3).
- (E11) §0.2: the relations are described as entry blocks of (1)–(4) after imposing the zero pattern (r3 said "with
  one index equal to 0", which does not fit the (a,d)-analogues).
- (E12) §0: a notation-disambiguation note; nothing is renamed.

Also updated: the title, frozen, provenance and status lines; the §W sentence on `--check-doc` (the r4 tables are
byte-identical to r3's); §6 "Not done"; §7 errata. The r2 → r3 diff (R1–R5) is recorded at the top of r3.

**Provenance.**
- v1 263f9df9…a6a8: `review/LEMMA_R_PROOF.v1.md`, a byte copy of the parent pin
  `…/review/dualunitary-rank-bound-parent-inputs-v1/`.
- Interim a05e563b…2f7c: `review/LEMMA_R_PROOF.md`, parent pin `…-inputs-v2`, unchanged.
- r2 c8e62cba20241fae36b5405cba5c4c19c4b02fab7aecbb5fcf1c837ecb3e4284: `review/LEMMA_R_PROOF.r2.md`, unchanged.
- r3 ae42fcbb99247aaa453a2f05ddb5482226b910ba898af07c29fb81e4a03890ea: `review/LEMMA_R_PROOF.r3.md`, unchanged.
- This r4.
- Companion v1 files: `review/LEMMA_R_NORMAL_FORM.v1.md` (37fb700e…e587) and `review/REDUCTION.v1.md`
  (819001f4…df80).

**Status.** CANDIDATE PROOF, not promoted; no novelty or priority claim. The parent has reported the following.
- Two independent mathematical reviews of v1. The generic branch was ACCEPT-WITH-FIXES, with fixes F1 and F2, both
  applied in r2. The residual branch was ACCEPT.
- An exact standard-library re-derivation of every displayed relation
  (`institute/…/review/qutrit-rank-parent-exact-relations-v1.json`).
- A Codex CLI gpt-6.1-sol hostile review of the interim text a05e…2f7c: ACCEPT-WITH-FIXES, no fatal or major defect
  (`institute/…/review/qutrit-sharp-codex-hostile-review-v1.note.md`). Its minors 1–4 are F2, R2, R3 and R4,
  applied in r2 and r3.
- A byte-identical replay of the four exact scripts (`institute/…/review/qutrit-rank-exact-replay-v1/`).
- A bounded priority audit that found no prior proof (`institute/…/review/qutrit-sharp-priority-audit.md`). A search
  miss is not novelty.
- A complete Claude CLI claude-opus-5-5 review of r3: ACCEPT-WITH-FIXES, with no missing case and no fatal or major
  issue. It re-derived §§0–5 by hand and hand-checked both §W tables entry by entry. Its 12 minor findings are
  E1–E12 above.
The r3 → r4 delta is editorial; the parent reviews it and freezes the acceptance record.

## P. Primary statements of the problem (quoted; typography normalised)

**Thesis.** S. A. Rather, PhD thesis (IIT Madras, 2023), ch. 3, §3.3.1.2 "Two-qutrit case". Lane copy
`sources/rather-thesis-2023/07_chapter3.pdf` (SHA-256 98598d45c6d51ba166b833da92d16181d9fd46c448f38fcb2c175db3b2d122e7),
page with printed footer 85 = PDF page 17. Text from `07_chapter3.layout.txt`, lines 738–751:
> "The largest possible entangling power obtained numerically from ensemble of dual unitaries (excluding
> 2-unitaries) generated using the MR map in d² = 9 is also 15/16. Numerical results seem to suggest that there are
> no two-qutrit dual-unitary gates with entangling power between 15/16 and 1. […]
> **Conjecture 3.3.2.** There are no two-qutrit d² = 9 dual-unitary or, equivalently, T-dual gates with entangling
> power in the range 15/16 < e_p(U) < 1.
> A possible reason for the discontinuity in the entangling power may be due to the non-existence of two-qutrit
> dual-unitary gates whose partial transpose has rank 7 and 8 or, equivalently, two-qutrit T-dual gates with
> Schmidt rank 7 and 8."

The family U(θ), eq. (3.36), is on the page with footer 84 (PDF page 16). Its θ = 2π/3 member gives
U_s(2π/3) = S·U(2π/3). Eq. (3.37) and the value e_p[U(2π/3)] = 15/16 are on the conjecture's page.

**Survey.** Rajchel-Mieldzioć et al., arXiv:2508.04777v3, p. 9 (PDF SHA-256
bc8ee8fc5648b574dc8e994eb7d27b7ef213e1873a2204e4060cc3613e15760b; parent's layout text, lines 567–572 and 576–578):
> "[…] a one-parameter family of dual unitaries Us(θ) and SUs(θ), their T-dual cousins. The dual unitary Us(2π/3)
> is an orthogonal matrix with entangling power 15/16 = 0.9375 which is likely to be the highest possible value for
> dual unitaries that are not 2-unitary. […] so that this reveals better the region of the gap, the rigorous
> existence of which is yet to be established."

**How the Theorem below answers these, if it is correct.**
- For a dual U, Theorem A gives e_p(U) = 1 − ‖U^ΓU^Γ† − I‖²_F/72, so e_p(U) = 1 iff U is 2-unitary. Otherwise the
  Theorem gives e_p(U) ≤ 15/16. Together with the precise T-dual transfer, this is the statement of
  Conjecture 3.3.2.
- The rank statement excludes rank U^Γ ∈ {7, 8} for dual gates and operator-Schmidt rank (= rank V^R) ∈ {7, 8} for
  T-dual gates. That is the "possible reason" named in the thesis.
- The survey sentence's scope, "dual unitaries that are not 2-unitary", is the hypothesis of the Theorem word for
  word. No import of [44] is needed for it.

## Theorem

Let U ∈ U(9) be dual unitary (U^R unitary) and not 2-unitary. Then rank U^Γ ≤ 6. Hence e_p(U) ≤ 15/16, with
equality iff spec(U^ΓU^Γ†) = {3/2 (×6), 0 (×3)}. Both U_s(2π/3) = S·U(2π/3) and the gate H of §W attain 15/16
exactly.

**T-dual form** (§0.1, R2). If V ∈ U(9) is T-dual (V^Γ unitary) and not 2-unitary, then rank V^R ≤ 6 and
e_p(V) ≤ 15/16, with equality iff spec(V^RV^R†) = {3/2 (×6), 0 (×3)}. V^Γ itself is unitary, of rank 9.

**Corollary** (Conjecture 3.3.2 of §P). No dual and no T-dual two-qutrit gate has 15/16 < e_p < 1. For dual gates,
and likewise for T-dual gates, e_p = 1 iff the gate is 2-unitary.

**Scope.**
- The sharp maximum 15/16 is over the non-2-unitary part of D ∪ T. It is not a statement about all of U(9): there
  an unrestricted bound fails by continuity near a 2-unitary, where e_p → 1.
- "Not 2-unitary" equals "outside O9 = LU·P9" only through the imported uniqueness theorem [44]
  (arXiv:2212.06737v2, Thm 1). The Theorem, its T-dual form and the Corollary do not use [44].

## 0. Setup

**Notation note (E12; nothing is renamed, no logical effect).** Some symbols carry two meanings, always separated by
context:
- x = vec R_0 in the block form of M (§0.2) versus the scalars x_1, x_2 (and y_1, y_2) inside T_1, T_2 in
  Proposition B\*;
- the scalars α, β, γ, δ (entries of Q_1, Q_2 in Proposition B\*) versus the relation labels (α)–(δ) of §0.2, which
  are always written in parentheses;
- S = SWAP versus the Pauli index set S ⊆ {0,1,2,3} (Fact K) versus the label S ∈ {R,T} (Proposition G);
- H = the 4×4 Hadamard matrix (Fact K, proof step 3) versus the attaining gate H (§W);
- σ = the second singular value of N_0 (Lemma S) versus the Pauli matrices σ_k;
- T = the set of T-dual gates (§0.1) versus the Bloch matrix T (Fact K), the tensor T[s,c,a,d] (Lemma T) and the
  sector matrices T_b; D = the set of dual gates versus the sector span D = span{R_0,T_1,T_2}.
The r3 review suggested ξ_b, η_b for x_b, y_b, 𝒮 for the Pauli index set and H_4 for the Hadamard matrix; readers may
substitute them.

### 0.1 Conventions, objective, marginals (exact)

Conventions from the survey arXiv:2508.04777v3, as pinned in README §0.1:
- basis |ij⟩ ↔ 3i+j; ⟨ij|U^R|αβ⟩ = ⟨iα|U|jβ⟩; ⟨iβ|U^Γ|jα⟩ = ⟨iα|U|jβ⟩; S = SWAP;
- e_p(U) = [E(U)+E(US)−E(S)]/E(S), E(U) = 1 − tr[(U^RU^R†)²]/81, E(S) = 8/9;
- D = {U : U^R unitary}, T = {U : U^Γ unitary}; 2-unitary means U, U^R, U^Γ all unitary.

**T-dual transfer (precise; R2).** For every X ∈ M_9(C), (XS)^R = X^ΓS; this exact identity is checked symbolically
in `evidence/controls_exact.json`. Applying it to X = US and using S² = I gives (US)^Γ = U^RS. In particular
E(US) = 1 − tr[(U^ΓU^Γ†)²]/81. The defining formula of e_p is symmetric under U ↔ US because (US)S = U, so
e_p(US) = e_p(U). Let U be dual and not 2-unitary, and put V := US. Then:
- V is unitary and V^Γ = U^RS is unitary. So V is T-dual, and rank V^Γ = 9.
- V^R = U^ΓS, so V^RV^R† = U^ΓU^Γ†. Hence rank V^R = rank U^Γ ≤ 6 (Theorem) and spec(V^RV^R†) = spec(U^ΓU^Γ†).
- V is not 2-unitary (V^R has rank ≤ 6), and e_p(V) = e_p(U) ≤ 15/16, with equality iff
  spec(V^RV^R†) = {3/2 (×6), 0 (×3)}.

Conversely, let V be T-dual and not 2-unitary. Then V = US with U := VS. This U is dual, because (VS)^R = V^ΓS is
unitary. It is not 2-unitary, because (VS)^Γ = V^RS is not unitary when V^R is not. So the bullets cover every
T-dual non-2-unitary gate. What transfers is rank V^R ≤ 6 and the e_p bound, not a bound on rank V^Γ.

**Theorem A.** For U ∈ D, E(U) = 8/9 and tr U^ΓU^Γ† = Σ|U_ij|² = 9. Hence
e_p(U) = 1 − ‖U^ΓU^Γ† − I‖_F²/72 = 1 − (Σ_i s_i² − 9)/72, where s_i are the eigenvalues of U^ΓU^Γ† and Σ s_i = 9.
If rank U^Γ = r, Cauchy–Schwarz gives Σ s_i² ≥ 81/r. For r ≤ 6 this means Σ s_i² ≥ 27/2, so e_p ≤ 15/16, with
equality iff six s_i equal 3/2.

**Four-party picture and the exact marginal identity (F2).** Set ψ(a,b,c,d) := U[(c,d),(a,b)]/3. U unitary ⇔
ρ_12 = I/9, and U^R unitary ⇔ ρ_13 = I/9. The 14|23 flattening is M[(a,d),(b,c)] := 3ψ(a,b,c,d) =
U[(c,d),(a,b)]. Then U^Γ[(c,b),(a,d)] = U[(c,d),(a,b)] = M[(a,d),(b,c)], i.e. U^Γ = ΠM^T with Π the fixed row
permutation (b,c) ↦ (c,b). Π is the matrix S, so equivalently M = (U^Γ)^TS. Consequently:

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

**Normal form (WLOG).** Σ = P²×P² and U^{-1}Σ are 4-dimensional subvarieties of P^8, so they intersect. (Projective
dimension theorem: over C, projective varieties X, Y ⊂ P^n with dim X + dim Y ≥ n intersect. Here U^{-1}Σ is the
image of Σ under the automorphism [U^{-1}] of P^8, so it is isomorphic to Σ.) Thus
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

**Relations used.** Each is an entry block of (1)–(4) after imposing the zero pattern. All are exact polynomial
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
1. (Bloch form.) In the basis {I,σ_1,σ_2,σ_3}, Φ(w_0I + w·σ) = w_0I + (w_0t + Tw)·σ with T a real 3×3 matrix, and
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
    [Quoted as printed. For w0 ≠ 1 the translation term is w0·t (proof step 1); this is immaterial here, since t = 0.]
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

**Lemma N1.** If {N_d} is a unital Kraus triple with dim A = 3 and Y = (Y_0,Y_1,Y_2) satisfies
Σ_dY_dN_d† = 0 = Σ_dN_d†Y_d, then all Y_d ∈ A.
*Proof.* By Fact K(a), gauge A = Sym; the hypotheses are covariant under Y ↦ V'†YW'†, N ↦ V'†NW'†. Then
N_d† = N̄_d. Transposing the second condition gives Σ_dY_d^TN̄_d = 0, and subtracting from the first gives
Σ_d(Y_d − Y_d^T)N̄_d = 0. Writing Y_d − Y_d^T = δ_dJ, this says J·Σ_dδ_dN̄_d = 0, and since the N̄_d are
independent, δ = 0. ∎ (The algebra is checked exactly in `evidence/lemma_T_exact.json`, key N1.)
If dim A = 3, fix a ∈ K and put Y = (Q_a, Ω_a1, Ω_a2). The adjoint of (α) is Σ_dY_dN_d† = 0 and (γ) is Σ_dN_d†Y_d = 0, so N1
(applicable because {N_0,N_1,N_2} is a unital Kraus triple by (U)) gives Q_a, Ω_ad ∈ A. For N1′, the
(a,d)-analogues of §0.2 already read Σ_cY_cR_c† = 0 = Σ_cR_c†Y_c with Y = (T_b, Ω^{(b1)}, Ω^{(b2)}). By (12)(34):
dim C = 3 ⇒ T_b, Ω^{(bc)} ∈ C (Lemma N1').

**Lemma T.** If u_1Jv_1^T + u_2Jv_2^T = 0 for 2×2 matrices u_i, v_i, then rank(u_1⊗v_1 + u_2⊗v_2) ≤ 2.
Equivalently, a tensor T[s,c,a,d] symmetric in (a,d) with rank_{(s,a)|(c,d)} ≤ 2 has rank_{(s,c)|(a,d)} ≤ 2.
*Proof* (LEMMA_R_NORMAL_FORM.v1.md §2). Both the hypothesis and F := u_1⊗v_1 + u_2⊗v_2 are invariant under
(u_1,u_2) ↦ (u_1,u_2)G, (v_1,v_2) ↦ (v_1,v_2)G^{-T}. Also, for invertible h, the map u_k ↦ hu_k multiplies the
hypothesis on the left by h and sends F ↦ (h⊗I)F, so the hypothesis and rank F are preserved.
- (i) If span{u_1,u_2} contains an invertible matrix, arrange u_1 = I. Then v_1 = −v_2 adj(u) with u := u_2: the
  hypothesis reads Jv_1^T = −uJv_2^T, and J^{-1}uJ = adj(u)^T for 2×2 matrices. Since adj(u) = tr(u)I − u, this gives
  F = I⊗v_1 + u⊗v_2 = (I⊗v_2)L(u) with L(u) = u⊗I + I⊗u − tr(u)I. Moreover rank L(u) ≤ 2 for every u, so
  rank F ≤ 2. Indeed L(gug^{-1}) = (g⊗g)L(u)(g⊗g)^{-1}. In the basis e_11, e_12, e_21, e_22 (e_ij := e_i⊗e_j),
  L(diag(λ_1,λ_2)) = diag(λ_1−λ_2, 0, 0, λ_2−λ_1). Also L(λI+E_12) = E_12⊗I + I⊗E_12, whose image is
  span{e_11, e_12+e_21}. Hence rank L(u) ≤ 2 for every u, Jordan blocks included; equivalently, every 3×3 minor of
  L(u) vanishes identically.
- (ii) Otherwise every element of span{u_1,u_2} is singular, and the hypothesis of Lemma T is not needed.
  - If dim span{u_k} ≤ 1, a G-move gives u_2 = 0, so F = u_1⊗v_1 has rank ≤ 1·2 = 2.
  - If the span is a 2-plane of singular matrices, it is totally isotropic for the non-degenerate quadratic form det.
    It is therefore one of the two rulings: all u_k = a_kb^T, or all u_k = ab_k^T. Then F = (Σa_k⊗v_k)(b^T⊗I) or
    F = (a⊗I)(Σb_k^T⊗v_k). Each factors through C², so rank F ≤ 2.
These identities are also checked exactly in `evidence/lemma_T_exact.json`. ∎

**Lemma S.** If ‖N_0‖_op = 1 (or ‖R_0‖_op = 1, by (12)(34)), then rank U^Γ ≤ 6.
*Proof.* Gauge N_0 = diag(1,σ). Then (U) forces N_d = ν_dE_22 and Q_a = κ_aE_22. So X_00 = diag(1,1,σ) and
X_0d, X_a0 ∈ C·E_22, and the nine slices span at most 2 + #{X_ad : a,d ∈ K} = 6 dimensions. ∎

**Rank Lemma (R3).** Use the block form M = [[1, 0, n_0],[0, 0, P],[x, 𝐁, Ω]] of §0.2, with row and column blocks of
sizes 1, 4, 4, and rP = rank P, rB = rank 𝐁. Let 𝒜 be a subspace of row vectors indexed by (b,c) ∈ K×K, and 𝒞 a
subspace of column vectors indexed by (a,d) ∈ K×K.
- (i) If every column of the last row block [x, 𝐁, Ω] lies in 𝒞, then rank M ≤ 1 + rP + dim 𝒞.
- (ii) Suppose that:
  - row P ⊆ 𝒜, n_0 ∈ 𝒜, and every row of Ω lies in 𝒜;
  - col 𝐁 ⊆ 𝒞, x ∈ 𝒞, and every column of Ω lies in 𝒞.

  Put Ω' := Ω − x n_0, E_𝐁 := I − 𝐁𝐁^+ and F_P := I − P^+P, where ^+ is the Moore–Penrose inverse. E_𝐁 is the
  orthogonal projector onto (col 𝐁)^⊥, and F_P is the orthogonal projector onto ker P. Then
  rank M = 1 + rank [[0, P],[𝐁, Ω']] = 1 + rP + rB + rank(E_𝐁Ω'F_P), and
  rank(E_𝐁Ω'F_P) ≤ min(dim 𝒜 − rP, dim 𝒞 − rB).
  With dim 𝒜 = dim 𝒞 = 3 this gives rank M ≤ 1 + rP + rB + 3 − max(rP, rB) = 4 + min(rP, rB).

*Proof of (i).* The first two row blocks [[1, 0, n_0],[0, 0, P]] have rank exactly 1 + rP, because only the first
row has a nonzero entry in the first column. The last row block has rank ≤ dim 𝒞. Rank is subadditive over row
blocks.

*Proof of (ii).*
1. *Pivot.* Subtract x·(first row) from the last row block, then subtract (first column)·n_0 from the last column
   block. Both operations are invertible, and they turn M into [[1, 0, 0],[0, 0, P],[0, 𝐁, Ω']]. Hence
   rank M = 1 + rank M', where M' := [[0, P],[𝐁, Ω']].
2. *The constraints survive the pivot.* Row (a,d) of Ω' is (row (a,d) of Ω) − x_ad·n_0, which lies in 𝒜 because
   n_0 ∈ 𝒜. Column (b,c) of Ω' is (column (b,c) of Ω) − N_0[b,c]·x, which lies in 𝒞 because x = vec R_0 ∈ 𝒞.
3. *Splitting.*
   - Subtract (first block column)·𝐁^+Ω' from the second block column. This replaces Ω' by
     Ω' − 𝐁𝐁^+Ω' = E_𝐁Ω' and leaves [0, P] unchanged.
   - Subtract (E_𝐁Ω'P^+)·(first block row) from the second block row. This replaces E_𝐁Ω' by
     E_𝐁Ω' − E_𝐁Ω'P^+P = Y := E_𝐁Ω'F_P and leaves 𝐁 unchanged.
   - col Y ⊆ range E_𝐁 = (col 𝐁)^⊥, so col Y ∩ col 𝐁 = 0.
   - If a row vector satisfies yP = zY, right-multiply by P^+P. Since F_PP^+P = 0 and PP^+P = P, this gives
     yP = 0. So row P ∩ row Y = 0.
   - Hence a column relation [0; 𝐁u] = −[Pv; Yv] forces Pv = 0 and 𝐁u = −Yv ∈ col 𝐁 ∩ col Y = 0. So
     rank [[0, P],[𝐁, Y]] = rB + rank [P; Y] = rB + rP + rank Y.
   This is the Marsaglia–Styan rank formula (Linear Multilinear Algebra 2 (1974) 269–292); the argument above is
   complete without it.
4. *Bound.*
   - Column side: for v ∈ 𝒞, 𝐁𝐁^+v ∈ col 𝐁 ⊆ 𝒞, so E_𝐁v ∈ 𝒞; and E_𝐁𝐁 = 0. So E_𝐁𝒞 is a subspace of dimension
     ≤ dim 𝒞 − rB. It contains col Y, because col Y ⊆ E_𝐁(col Ω') and col Ω' ⊆ 𝒞.
   - Row side: for a row vector y ∈ 𝒜, yP^+P ∈ row P ⊆ 𝒜, so yF_P ∈ 𝒜; and PF_P = 0. So 𝒜F_P has dimension
     ≤ dim 𝒜 − rP. It contains row Y, because row Y ⊆ (row Ω')F_P and row Ω' ⊆ 𝒜.
   - Hence rank Y ≤ min(dim 𝒜 − rP, dim 𝒞 − rB). ∎

## 2. Proposition G (dim A = 3 and dim C = 3) ⇒ rank ≤ 6

Gauge A = C = Sym. Rank Lemma (ii) applies with 𝒜 = vec A and 𝒞 = vec C, both 3-dimensional. The hypotheses hold:
- row P ⊆ vec A, since N_1, N_2 ∈ A and Q_1, Q_2 ∈ A (Lemma N1);
- n_0 = vec N_0 ∈ vec A;
- the rows vec Ω_ad of Ω lie in vec A (Lemma N1);
- col 𝐁 ⊆ vec C, since R_1, R_2 ∈ C and T_1, T_2 ∈ C (Lemma N1');
- x = vec R_0 ∈ vec C;
- the columns vec Ω^{(bc)} of Ω lie in vec C (Lemma N1').

So rank M ≤ 4 + min(rP, rB). Since ‖N_0‖ < 1, the 2×4 matrix
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
- (O4) and (O2) then give Σ_{a∈K}Q_a[b,c]w̄_c[a] = 0 and Σ_aQ_a[b,c]w̄_b[a] = 0 for all b,c ∈ K. Indeed, with
  R_c = ρ_cw_cw_c^T, (O4) reads Σ_c ρ̄_c(Σ_a Q_a[b,c]w̄_c[a]) w̄_c[d] = 0 for all d. Since w̄_1, w̄_2 are independent
  and ρ_c ≠ 0, each bracket vanishes. (O2) is the same with τ_b.
  - For b ≠ c, w̄_b and w̄_c span C², so Q_a[b,c] = 0.
  - For b = c, (Q_a[b,b])_a ∥ n^{(b)}_K.
  So every Q_a (a ∈ K) is diagonal, span{N_1,N_2,Q_1,Q_2} ⊆ Diag, and rP ≤ 2.
- Every column of the last row block lies in vec C, which is 3-dimensional: x = vec R_0 and vec R_c by definition,
  vec T_b and vec Ω^{(bc)} by Lemma N1'. Rank Lemma (i) gives rank M ≤ (1 + rP) + 3 ≤ 6.

dim A = 1 is impossible here: then p ∥ q, contradicting w_1 ∦ w_2.

## 4. Proposition B\* (all of dim A,B,C,D ≤ 2; ‖N_0‖, ‖R_0‖ < 1) ⇒ U 2-unitary or rank ≤ 5

Gauge A ⊆ Diag and C ⊆ Diag: N_d = diag(p_d,q_d) and R_c = diag(r_c,s_c), with all four of p_K, q_K, r_K, s_K
nonzero.
1. (O1) reads n^{(b)}_a·conj(ρ^{(a)}_b) = 0 (ρ^{(1)} = r, ρ^{(2)} = s), i.e. p_1r_1 = p_2s_1 = q_1r_2 = q_2s_2 = 0.
   With all four K-parts nonzero this forces one of two support patterns.
   - If p_1 ≠ 0: then r_1 = 0, so r_2 ≠ 0, so q_1 = 0, so q_2 ≠ 0, so s_2 = 0, so s_1 ≠ 0, so p_2 = 0. This gives the
     first pattern p_2 = q_1 = r_1 = s_2 = 0.
   - If p_1 = 0: then p_2 ≠ 0, so s_1 = 0, so s_2 ≠ 0, so q_2 = 0, so q_1 ≠ 0, so r_2 = 0. This gives the second
     pattern p_1 = q_2 = r_2 = s_1 = 0.
   - The simultaneous swap e_1 ↔ e_2 on parties 1 and 4 maps the second pattern to the first. It sends
     p_K ↦ (p_2,p_1) and q_K ↦ (q_2,q_1), swaps r and s, and keeps A, C ⊆ Diag.
   So, after this swap if needed, **p_2 = q_1 = r_1 = s_2 = 0**: N_1 = p_1E_11, N_2 = q_2E_22, R_1 = s_1E_22,
   R_2 = r_2E_11, with p_1, q_2, r_2, s_1 ≠ 0. In particular dim A = dim C = 2.
2. (O4) gives Q_1e_2 = 0 and Q_2e_1 = 0, so Q_1 = αE_11 + βE_21 and Q_2 = γE_12 + δE_22. (O3) gives T_1e_1 = 0
   and T_2e_2 = 0, so T_1 = x_1E_12 + y_1E_22 and T_2 = x_2E_11 + y_2E_21.
3. (U) for B: |α|²+|β|² = |α|²+|γ|² = |p_1|², |γ|²+|δ|² = |β|²+|δ|² = |q_2|², and αβ̄+γδ̄ = 0; so |β| = |γ|.
   (U) for D: |x_1|²+|x_2|² = |x_2|²+|y_2|² = |r_2|² and |y_1|²+|y_2|² = |x_1|²+|y_1|² = |s_1|².
4. (O2) gives βx_2 = αx_1 = δy_2 = γy_1 = 0.
5. If β = γ = 0: |α| = |p_1| and |δ| = |q_2| are nonzero, so x_1 = y_2 = 0, and all Q_a, T_b are diagonal.
   Entries (1,2) and (2,1) of (α) and (γ) in the diagonal gauge (using p_2 = q_1 = 0, p_1q_2 ≠ 0 and Q_a
   off-diagonal zero) make Ω_ad diagonal in (b,c). The mirrored argument (R, T diagonal, r_1 = s_2 = 0,
   r_2s_1 ≠ 0) makes Ω^{(bc)} diagonal in (a,d). So the rows of the last column block and the columns of the last
   row block all lie in Diag. For the columns these are x = vec R_0 (R_0 ∈ C ⊆ Diag), vec R_c, vec T_b and
   vec Ω^{(bc)}. Rank Lemma (i) with 𝒞 = vec Diag gives rank M ≤ (1 + rP) + 2 ≤ 1 + 2 + 2 = 5, where rP ≤ 2
   because N_1, N_2, Q_1, Q_2 ∈ Diag.
6. If β ≠ 0 (⇔ γ ≠ 0): x_2 = y_1 = 0, so |x_1| = |r_2| ≠ 0 and |y_2| = |s_1| ≠ 0, hence α = δ = 0.
   - B = span{diag(p_0,q_0), E_21, E_12} has dim ≤ 2 only if N_0 = 0; likewise D forces R_0 = 0. So
     |p_1| = |q_2| = |r_2| = |s_1| = |β| = |γ| = |x_1| = |y_2| = 1.
   - With N_0 = 0, (α) and (γ) give Ω_a1 = ω_aE_22 and Ω_a2 = ω'_aE_11. Then (δ) and (β) with Q_1 = βE_21,
     Q_2 = γE_12 give ω = ω' = 0, so Ω = 0.
   - Then M = [[1,0,0],[0,0,P],[0,𝐁,0]] with P and 𝐁 monomial unitaries (distinct matrix units with unimodular
     coefficients). So MM† = I: **U is 2-unitary**.

## 5. Assembly

Take any normal form of §0.2 (φ(0000) = 1) of a dual U. Since |U[(00),(00)]| ≤ 1, every such normal form has
maximal overlap; nothing changes relative to r3's wording.
- If ‖N_0‖ = 1 or ‖R_0‖ = 1: Lemma S.
- Else, if some sector has dimension 3: by the symmetries assume dim C = 3. The symmetries preserve the hypothesis
  that both corners are strict contractions. Then Proposition G (dim A = 3) or Proposition A\* (dim A ≤ 2)
  applies.
- Else all sector dimensions are ≤ 2: Proposition B\*.
In every case rank U^Γ ≤ 6 or U is 2-unitary. ∎

## W. Attaining gates (explicit, exact; R4)

Both matrices below are real. Tokens: s3 = √3, s6 = √6. Rows and columns are indexed by |ij⟩ ↔ 3i+j; row r is the
output basis state and column c the input basis state.

`code/witnesses_exact.py` (SHA-256 0d4295fe…56d7) builds both gates from their definitions, certifies them exactly,
and prints these tables → `evidence/witnesses_exact.json` (ba380fad…3c19). The command
`python -B code/witnesses_exact.py --check-doc <file>` re-parses the tables in a proof file and re-certifies the
parsed matrices. It passed on r3 after r3's freeze (evidence/LOG.md, 05:29:16). The tables below are byte-identical
to r3's (textual diff recorded in evidence/LOG.md); per the parent's no-new-numerics instruction for r4 it was not
re-run.

**W1. U_s(2π/3) := S·U(2π/3) ∈ M_9(Q(√3)).** U(θ) is thesis eq. (3.36), transcribed in `code/gates.py` (U36_ROWS).
Attainment is certified by the table itself, independently of this identification.

```
2Us[0] =    0    0    1   s3    0    0    0    0    0
2Us[1] =   s3    0    0    0    0    0    0    0    1
2Us[2] =    0    0    0    0    0    1    0   s3    0
2Us[3] =    0    2    0    0    0    0    0    0    0
2Us[4] =    0    0    0    0    0   s3    0   -1    0
2Us[5] =    0    0    0    0   -1    0  -s3    0    0
2Us[6] =   -1    0    0    0    0    0    0    0   s3
2Us[7] =    0    0    0    0   s3    0   -1    0    0
2Us[8] =    0    0   s3   -1    0    0    0    0    0
```

Certified exactly:
- U_sU_s† = I;
- U_s^R = U_s, so U_s is dual and self-dual;
- W := U_s^ΓU_s^Γ† satisfies W² = (3/2)W, tr W = 9 and tr W² = 27/2;
- rank W = rank U_s^Γ = 6, so U_s is not 2-unitary;
- e_p(U_s) = 15/16 from the survey formula, with E(S) = 8/9.

Earlier exact controls are in `evidence/controls_exact.json`. The parent reports an independent Q(√3) check.

**W2. H ∈ M_9(Q(√6)).** The normal-form data are from the Codex review note, lines 98–111. Take t = √6/4,
X = [[0,1],[1,0]], Z = diag(1,−1), and
- N_0 = R_0 = I/2;
- N_1 = Q_1 = R_1 = T_1 = tZ;
- N_2 = Q_2 = tX;
- R_2 = T_2 = −tX;
- Ω_ad = −(1/2)δ_ad I.

These are assembled with the conventions of §0.2 (φ(0000) = 1, all other entries 0):

```
4H[0] =    4    0    0    0    0    0    0    0    0
4H[1] =    0    0    0    2   s6    0    0    0  -s6
4H[2] =    0    0    0    0    0  -s6    2  -s6    0
4H[3] =    0    2    0    0   s6    0    0    0   s6
4H[4] =    0   s6    0   s6   -2    0    0    0    0
4H[5] =    0    0   s6    0    0    0  -s6   -2    0
4H[6] =    0    0    2    0    0  -s6    0   s6    0
4H[7] =    0    0  -s6    0    0   -2  -s6    0    0
4H[8] =    0   s6    0  -s6    0    0    0    0   -2
```

Certified exactly:
- HH† = I and H^R = H;
- H^ΓH^Γ† = (3/4)(I + S). Hence W² = (3/2)W, tr W = 9, tr W² = 27/2 and rank H^Γ = 6, so H is not 2-unitary;
- e_p(H) = 15/16.

Mutation controls, all rejected:
- t = 1/2: not unitary;
- R_2 = +tX: not both unitary and self-dual;
- Ω_ad = +(1/2)δ_ad I: not unitary;
- H^ΓH^Γ† = (3/4)(I − S): false;
- one entry of U_s changed from 1/2 to 1/3: not unitary.

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
- `code/witnesses_exact.py` (0d4295fe…56d7) → `evidence/witnesses_exact.json` (ba380fad…3c19): both attaining
  gates of §W, with 5 mutation controls rejected. Its `--check-doc` mode re-certifies the tables printed in this
  file. Earlier exact checks of U_s are in `evidence/controls_exact.json` (adafcff9…3281).
- The Rank Lemma (R3) and the T-dual transfer (R2) are hand proofs. They use only the identities already listed.
- Floating-point material is evidence only: the survey `evidence/search/nfcases_*.jsonl` (main stratum: case G
  only; rank-3/4: case S only; degenerate cases only at 2-unitaries) and `code/scratch/relations_check.py`.
- Reported by the parent, not re-run here: the byte-identical replay of the four exact scripts
  (`institute/…/review/qutrit-rank-exact-replay-v1/`), the exact relation re-derivation, the Q(√3) and Q(√6) gate
  checks, and the Codex review's 536 counterexample attempts. None of those attempts found a counterexample;
  failed runs establish nothing.
- Not done: formalisation. The r3 → r4 delta (E1–E12) is editorial and is reviewed by the parent.

## 7. Errata carried by r4

- v1 §0, Fact K parenthetical "(complement spanned by J^{-1}σ_m)" is wrong. The complement of the three-Pauli span
  is C·σ_m, and J^{-1}σ_m is the right multiplier (F1). The normal-form note's longer proof (v1 file
  LEMMA_R_NORMAL_FORM.v1.md, lines 48–51) was already correct.
- REDUCTION.v1.md lines 12–13 (and the same line in later REDUCTION.md revisions), "U^ΓU^Γ† ≅ 9ρ_14 (fixed index
  permutation)", is wrong in general. The correct identity is 9ρ_14 = MM† = (U^Γ†U^Γ)^T, with
  U^ΓU^Γ† = Π(M†M)^TΠ^T (F2). No argument in the lane depended on the wrong form: only rank, spectrum and purity
  were used.
- v1's status line ("computer checks are floating-point sanity checks") is superseded by §6.
- r2 §0.1, "Every statement about D transfers to T", is withdrawn. What transfers is rank V^R ≤ 6 and
  e_p(V) ≤ 15/16 for V = US (R2); V^Γ is unitary.
- r2's Theorem sentence "The same bound holds for T-dual unitaries" is made precise by the Theorem's T-dual form.
- Page reference: the parent's message cites the thesis conjecture as "p. 84". In the lane copy it is on the page
  with footer 85 (PDF page 17 of 07_chapter3.pdf); eq. (3.36) is on the page with footer 84.
- r3 §0.4, Fact K proof step 1: "Φ(w_0I + w·σ) = w_0I + (t + Tw)·σ" is wrong as written when w_0 ≠ 1 and t ≠ 0.
  The correct form is w_0I + (w_0t + Tw)·σ (E1). It was never used in its wrong form, because the same step
  imposes t = 0.
- r3 §0.2, "with one index equal to 0", does not describe the (a,d)-analogues. These are the {b}×{0} entries of (1)
  and (3) with both block indices in K (E11).
- r3 §5, "maximal-overlap normal form", was not defined in r3. It means any normal form of §0.2 (E8).
