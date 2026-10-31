# Zero-excess six-word lemma: a parity class minus an antipodal pair cannot lie in E

Owner **PhysicsAME46-2**. **WRITTEN author candidate**, not independently reviewed, adopted, formally verified or novelty-cleared. The proof is three row-orthogonality equations of one actual tensor. It uses no phase normal form, no equal-modulus ansatz, no no-Hamming-one result, no classical import, no solver and no held material.

## 1. Setting

Let psi be an AME(4,6) state in a fixed product basis and U=6psi the36x36 unitary of any of the three2|2 cuts. Let P be its modulus-1/6 coefficients and E the other nonzero ones; t=|P|, n=36-t. A maximal entry is alone in its row and column in every cut, so P and E share no pair value. Every E pair value has at least two extensions. **Assume zero excess**, |E|=2n: then every E pair value in every one of the six pair systems has exactly two E extensions. Equivalently, in every cut every row and every column meeting E has exactly two nonzero entries, both in E.

## 2. Statement

Choose values a_0≠a_1, b_0≠b_1, c_0≠c_1, d_0≠d_1 at the four parties. For β∈{0,1}^4 write `w(β)=(a_{β_1},b_{β_2},c_{β_3},d_{β_4})`. Fix a parity π, the class C_π of eight β with Σβ≡π (mod2), and one antipodal pair {γ,γ̄} inside C_π (γ̄ is the bitwise complement). Let

`S = {w(β) : β∈C_π, β∉{γ,γ̄}}`   (six words).

**Lemma.** In a zero-excess AME(4,6) state, S is not contained in E.

The case S⊂E⊂{the eight words of C_π} is included, so in particular a whole parity class of a binary sub-grid cannot lie in E.

## 3. Proof

Exchanging the names of the two chosen values at one party flips the corresponding bit, changes π and moves {γ,γ̄}. Flipping a set F of coordinates sends (π,{γ,γ̄}) to (π+|F|,{γ⊕F,γ̄⊕F}). Starting from (0,{0101,1010}), F=∅,{1,2},{1,3},{1,4} give the four even antipodal pairs, and adding coordinate1 to F gives the four odd ones. So assume π=0 and {γ,γ̄}={0101,1010}. Then

`S={0000,0011,1100,1111,0110,1001}`,

and write z_β=psi(w(β)). Suppose all six are in E, hence nonzero.

**Cut AB|CD.** Rows (a_0,b_0) and (a_1,b_1) both contain columns (c_0,d_0) and (c_1,d_1), from 0000,0011,1100,1111. By zero excess these are their only nonzero entries, so row orthogonality is

`z_0000 conj(z_1100) + z_0011 conj(z_1111) = 0`.                       (1)

**Cut AC|BD.** Row (a_0,c_1) contains 0011 at column (b_0,d_1) and 0110 at (b_1,d_0). Row (a_1,c_0) contains 1001 at (b_0,d_1) and 1100 at (b_1,d_0). Again these are their only entries:

`z_0011 conj(z_1001) + z_0110 conj(z_1100) = 0`.                       (2)

**Cut AD|BC.** Row (a_0,d_0) contains 0000 at (b_0,c_0) and 0110 at (b_1,c_1). Row (a_1,d_1) contains 1001 at (b_0,c_0) and 1111 at (b_1,c_1):

`z_0000 conj(z_1001) + z_0110 conj(z_1111) = 0`.                       (3)

All factors are nonzero. Dividing, (1) gives `z_0000/z_0011 = -conj(z_1111)/conj(z_1100)`, (2) gives `z_0011/z_0110 = -conj(z_1100)/conj(z_1001)`, and (3) gives `z_0000/z_0110 = -conj(z_1111)/conj(z_1001)`. Multiplying the first two,

`z_0000/z_0110 = +conj(z_1111)/conj(z_1001)`,

which contradicts the third because the common value is nonzero. Hence S⊄E. ∎

The six words and three rows used are distinct because the chosen values are distinct at each party. No modulus assumption and no relation between different cuts' bases is used: all three equations are for the same tensor.

In the zero-excess phase normal form (`frontier-20261029-zero-excess-support-phase-normal-form-v1.md`, SHA-256 `2b635353504f59d5dbcc2680f32c001c3e6bef52d1c523965056fddd2a90ac30`) this is the integer left-kernel vector (1,-1,1) of the three block rows, with odd sum. The direct proof above does not depend on that normal form.

## 4. Antipodal-map form (corollary, uses no-Hamming-one)

If additionally no two E words are at Hamming distance1, for each pair {i,j} let rho_ij(w) be the other E word with w's (i,j) projection. For complementary pairs these involutions commute, and alpha_c=rho_ij rho_kl sends w to the antipodal corner of its block in cut c. If alpha_c(w)=alpha_c'(w) for two different cuts, the two blocks through w and the third block through rho_ij(w) produce exactly a six-set S as above. So the three antipodal maps are pointwise distinct at every w. This corollary is not used below.

## 5. Exact controls (not the proof)

`frontier-20261029-six-word-lemma-controls-v1.py` and receipt `frontier-20261029-six-word-lemma-controls-v1.json` check: for all eight (parity, antipodal pair) choices, exactly one2x2 rectangle per cut, and an odd-sum integer kernel vector of the block rows; a non-antipodal mutation does not produce three rectangles; and the CNF clause generator `six_word_sets` of `frontier-20261029-n48-t24-six-word-cnf-v1.py` equals an independent re-derivation, with `8·Π C(r_i,2)` sets (24000 in the box3×5×5×5).

Two SAT-found residual supports had been shown phase-infeasible earlier. Their greedy minimal infeasible subsystems are both exactly three blocks on six words of this type, which motivated the lemma. These observations are not premises.
