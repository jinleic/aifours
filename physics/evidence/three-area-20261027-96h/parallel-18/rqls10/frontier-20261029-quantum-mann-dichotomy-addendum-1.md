# Addendum 1: f163 MINOR fixes (printed phase data, two proofs, notation)

**WRITTEN AUTHOR ADDENDUM, UNREVIEWED.** Native `/bin/date`: Thu Oct 29 08:38:05 PDT 2026.

This is additive. It does not edit the pinned packets:
- `frontier-20261029-quantum-mann-dichotomy-k333-k555-v1.md` (SHA-256 `9fba4852172abd8629d1695ad2ec05bc14563628880c377108b21f9fa31dde3c`);
- `frontier-20261029-half-resolved-maximal-qls10-and-m7-v1.md` (SHA-256 `e72f7c7db43eeb734ed18c199fb5ff84c0a9157b1bdcc714bbafeabd893791d1`).

It answers the three MINORs of review f163 (m1, m2, m3) as recorded in `dispositions/physics-5-quantum-mann-k333-no-k555-exact-core-parent-v1.md`. No mathematical claim changes.

## m1. Printed phase data

**Maximal QLS(10) with exactly five transversals.**
- Characters: T = [(0,0),(0,1),(1,0),(1,3),(2,2),(2,4),(3,1),(3,4),(4,2),(4,3)] ⊂ Z5².
- Vectors: for quadrant q ∈ {Q00, Q01, Q10, Q11} and x = (x1, x2) ∈ Z5², v_q(x)_j = ζ20^{4⟨c_j, x⟩ + PHI2[q][j]} / √10, for j = 0, …, 9.
- Phases:

```text
PHI2[Q00] = (-65, -40, -40, -25, -25, -15, -20, -10, -10, 0)
PHI2[Q01] = (-40, -30, -25, -15, -15,  -5, -20, -10, -10, 0)
PHI2[Q10] = (-25, -10, -15, -10, -10, -10,   0,   0,   0, 0)
PHI2[Q11] = (  0,   0,   0,   0,   0,   0,   0,   0,   0, 0)
```

- Placement:
  - Q00: x ↦ (row x1, column x2);
  - Q01: x ↦ (x1, 5 + x2);
  - Q10: x ↦ (5 + x1, x2);
  - Q11: x ↦ (5 + x1, 5 + x2).
- The transversal class T1(u), for u ∈ Z5, consists of the Q01 and Q10 cells with x1 + x2 = u.

**L(K7,7,7) in C^14.**
- Characters: T7 = [(0,0),(0,1),(1,0),(1,1),(2,3),(2,5),(3,5),(3,6),(4,2),(4,6),(5,2),(5,4),(6,3),(6,4)] ⊂ Z7².
- Vectors: ψ_q(x)_j = ζ28^{4⟨c_j, x⟩ + PH7[q][j]} / √14.
- Phases:

```text
PH7[AB] = (-63, -49, -14,   0, -84, -70, -56, -42, -42, -28, -28, -14, -14, 0)
PH7[AC] = (-49, -70, -14, -35, -56, -14, -14,   0, -14,   0, -14,   0,   0, 0)
PH7[BC] = (  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0, 0)
```

- Incidence: the AB-cell x = (s,t) is the edge A_s–B_t; the AC-cell x is A_s–C_{s+t}; the BC-cell x is B_t–C_{s+t} (indices mod 7).

**Provenance.** These literals are the ones in:
- the pinned producers `frontier-20261029-half-resolved-maximal-qls10-v1.py` (SHA `7800b9c9…7ae`, lines 15–19);
- `frontier-20261029-k777-exact-construction-v1.py` (SHA `0008dd52…6c0fe`, lines 11–14);
- the author replay read by f163.

They were checked again from these literals alone by the independent Galois-norm replay `frontier-20261029-norm-test-independent-replay-v1.py` (SHA `3a5627da…f7a6`), result `…json` (SHA `82b4d05a…8b4e`), status PASS. That replay found:
- QLS(10): rows, columns and T1 classes orthonormal; 1225 orthogonal pairs; exactly 5 orthogonal transversals; 100 non-parallel rays;
- K7,7,7: all 21 stars orthonormal; 147 non-parallel rays.

## m2. The two load-bearing lemmas

**Frame identity.** Take an orthonormal representation ψ of L(K_{m,m,m}) in C^{2m} with parts A, B, C. Define:
- P_a = Σ_{b∈B} |ψ_ab⟩⟨ψ_ab|;
- Q_b = Σ_{a∈A} |ψ_ab⟩⟨ψ_ab|;
- R_c = Σ_{a∈A} |ψ_ac⟩⟨ψ_ac|.

The 2m edge vectors at each vertex form an orthonormal basis. Hence:
- I − P_a = Σ_c |ψ_ac⟩⟨ψ_ac|;
- I − Q_b = Σ_c |ψ_bc⟩⟨ψ_bc|;
- I − R_c = Σ_b |ψ_bc⟩⟨ψ_bc|.

Let S_XY denote the sum of |ψ_e⟩⟨ψ_e| over the X–Y edges. Then:
- S_AB = Σ_a P_a = Σ_b Q_b;
- S_AC = Σ_a (I − P_a) = mI − S_AB, and also S_AC = Σ_c R_c;
- S_BC = Σ_b (I − Q_b) = mI − S_AB, and also S_BC = Σ_c (I − R_c) = mI − S_AC = S_AB.

So S_AB = mI − S_AB, that is, **Σ_a P_a = Σ_b Q_b = Σ_c R_c = (m/2) I**. In particular each of the three edge classes is a tight frame with bound m/2. ∎

**Parity-core embedding lemma.** Let L be a Latin square of order 2m with a Z2 quotient:
- R = R0 ⊔ R1, C = C0 ⊔ C1, T = T0 ⊔ T1, all parts of size m;
- L(R_i × C_j) ⊆ T_{i+j}, indices mod 2.

Put A = R0, B = C0, C = T1. Define φ_L on the 3m² cells of R0×C0 ∪ R0×C1 ∪ R1×C0 by:
- (r,c) ∈ R0×C0 ↦ edge r–c;
- (r,c) ∈ R0×C1 ↦ edge r–L(r,c);
- (r,c) ∈ R1×C0 ↦ edge c–L(r,c).

Here L(r,c) ∈ T1 in the last two cases.

*Claim.*
1. φ_L is a bijection onto E(K_{m,m,m}).
2. It maps each row r ∈ R0 onto the star of r, each column c ∈ C0 onto the star of c, and each label class t ∈ T1 onto the star of t.

*Proof.*
- **R0×C0** is A×B.
- **R0×C1.** For fixed r ∈ R0, the m symbols of row r in the columns C1 lie in T1 and are distinct. Since |T1| = m, c ↦ L(r,c) is a bijection C1 → T1. So R0×C1 → A×C is bijective.
- **R1×C0.** For fixed c ∈ C0, r ↦ L(r,c) is a bijection R1 → T1. So R1×C0 → B×C is bijective.
- **Star of r ∈ R0.** Row r consists of exactly the cells (r, C0) ∪ (r, C1). They map to {r}×B ∪ {r}×C, which is the star of r.
- **Star of c ∈ C0.** Column c consists of (R0, c) ∪ (R1, c). They map to A×{c} ∪ {c}×C.
- **Star of t ∈ T1.**
  - The label class of t has one cell per row and per column.
  - In a row r ∈ R0, the symbol t ∈ T1 occurs only in a column of C1, giving the edge r–t; these give A×{t}.
  - In a row r ∈ R1, it occurs only in a column c ∈ C0, giving the edge c–t. These m cells lie in distinct columns of C0, so they give B×{t}. ∎

Consequently, in any 1-RQLS(2m) (of any cardinality) with resolution square L, the 3m rows/columns/classes R0 ∪ C0 ∪ T1 restricted to these cells form an orthonormal representation of L(K_{m,m,m}) in C^{2m}. This is the parity core used by Corollary A and by the Consequence of Theorem B.

## m3. Notation corrections

These apply to the dichotomy packet, Theorem A.
- **Lemma 1 proof.** Read the vectors "w_j = 4g_j/√3" as **h_j = 4g_j/√3**. The unitary is e1⊗e_j ↦ f_j, e2⊗e_j ↦ h_j.
- **Step 2.** The generic vector "w = f_+ ⊗ g + f_− ⊗ h" is renamed **z = f_+ ⊗ g + f_− ⊗ h**. Throughout, **ω := e^{2πi/3}**. With ξ_a = e^{−2i t_a} and t_a ∈ {0, π/3, 2π/3}, we get ξ = 1, ω², ω respectively. So {ξ_a} = {1, ω, ω²} holds **as a set**: t = π/3 gives ω² and t = 2π/3 gives ω.
- **Step 3.** "spectrum {1, w, w²}" means {1, ω, ω²}. The stars previously written "E_b, E_c" are renamed **St(b), St(c)**:
  - St(b) is the six vectors ψ_ab (a ∈ A) and ψ_bc (c ∈ C);
  - St(c) is defined analogously.

  The symbols E_{μ,λ} in Steps 4–5 denote only matrix units.

None of these changes affects correctness. That agrees with the review.

## Scope reminder

Per the f163 disposition:
- Theorem C, the m = 7 flat-diagonal completion searches, the floating discovery data and the K666 control are **not adopted**.
- The full-array form of Corollary A may already be covered by Ball–Simoens (arXiv:2603.02334). The 9-context statement (Theorem A) is the incremental content.
- The original 100-ray target remains OPEN.
