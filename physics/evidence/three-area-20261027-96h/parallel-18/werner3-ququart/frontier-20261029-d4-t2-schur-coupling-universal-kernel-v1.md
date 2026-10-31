# The singular-kernel condition in the full T2 block-coupling reduction

**Status: WRITTEN, UNREVIEWED.** Conditional on the unreviewed separately 2+2 T2 theorem and its sector proof, this packet proves the **kernel/range condition** in the full original-pair Schur-coupling reduction. It does **not** prove the separately necessary 8×8 Schur-complement inequality and therefore does **not** establish unrestricted T2, T3, Z2, the original q3 target or source correctness. The named inputs are:

- 2+2 theorem and elementary weighted two-qubit lemma: `frontier-20261029-d4-t2-arbitrary-2plus2-blocks-v1.md`, SHA-256 bb09c6bf442b9d497241297c57f9da678b559b5d13ee56cc871de4a6fc7f1473, UNREVIEWED;
- exact original-quantifier coupling reduction: `frontier-20261029-d4-t2-original-schur-block-coupling-residual-v1.md`, SHA-256 ab1c95f60443316718494d00c9591d05964ded08ea240f1209dcc9010d5127ac, UNREVIEWED;
- f215 square-normal written disposition for positivity of the offblock term. No false f198 arbitrary-T lemma, selected numerical/physical q, program, held input or external source is used.

## 1. Claim and its consequence

For each isometry `Ψ∈C^(16×2)`, the coupling reduction defines `D=2I−DΨ†DΨ` on the 14-complex-dimensional block-diagonal coefficient space and `J=DΨ†NΨ`, where `NΨ` maps the 8-complex-dimensional strictly upper local offblocks to their tensor-sum action on `Ψ`. The claimed universal identity is

**`ker D ⊆ ker J†` for every `Ψ`.**  (1.1)

Using the separately stated singular Schur complement, this would reduce unrestricted T2 **exactly** to the still-open condition

`N−J†D⁺J ⪰ 0` for every `Ψ`.  (1.2)

There is no claim that (1.2) is true, easy, necessary only on a smaller chosen family, or verified. In particular `D,N⪰0` and (1.1) alone do not prove it.

To prove (1.1), the coupling packet shows it suffices to consider any separately 2+2 block-diagonal traceless pair `(A,B)` saturating `S2(X)=2L`, `X=A⊗I+I⊗B`, and any maximizing rank-two projector `P`. We prove the following equality classification sufficient for that purpose:

> If the saturated pair is nonzero, either `σ2(X)>σ3(X)`, or, up to exchanging the factors, `B=0` and `A` is traceless rank one.

The statement is about all complex blocks and all degeneracies, not a selected parameter family.

## 2. Sector notation and a useful weighted-lemma equality

Write

`A=(αI2+C1)⊕(−αI2+C2)`, `B=(βI2+D1)⊕(−βI2+D2)`,

with all `Cr,Ds` traceless, and let `ε1=1`, `ε2=−1`. The four sectors are

`Xrs=tr s I4+Cr⊗I2+I2⊗Ds`, `tr s=εrα+εsβ`.

The preceding packet bounds the two top squared singular values by one of three exhaustive sector configurations: both in one sector; one each from sectors in the same row or column; or one each from sectors in different rows and columns. Equality in the corresponding chain is necessary for saturation.

We need the following refinement of equality in the weighted lemma

`||tI4+C⊗I2+I2⊗D||_op²≤4|t|²+||C||_F²+2||D||_F²`.  (2.1)

If equality holds, then **there is a rank-one orthogonal projector `W` such that**

`D=t(2W−I2)`, `C²=4t² I2`.  (2.2)

For the zero-input equality this holds with arbitrary `W`. Otherwise choose maximizing unit vectors `u,v`. The weighted-duality proof gives a coefficient factor `(1+h−|bp+aw|²)/2≤1`, with `h=||VU†||²≤1` in a Schmidt basis for `u`. Equality implies `h=1`, hence `u=u_A⊗w`, `v=v_A⊗w` for a common unit second-factor vector `w`. Put `s=⟨u_A,v_A⟩`. Equality in the weighted Frobenius Cauchy–Schwarz inequality gives, for a common complex proportionality constant `κ`,

`t=κ conjugate(s)/4`,

`C=κ(|u_A⟩⟨v_A|−conjugate(s) I2/2)`,

`D=(κ conjugate(s)/2)(|w⟩⟨w|−I2/2)`.

The rank-one product `R=|u_A⟩⟨v_A|` satisfies `R²=conjugate(s)R`; therefore the traceless expression in `C` squares to `conjugate(s)² I2/4`. Substitution gives (2.2). When `s=0`, it also gives `t=0`, `D=0`, `C²=0`. The symmetric lemma exchanges the two local factors.

## 3. The two selected singular values from one sector

The 2+2 proof uses the full sector Frobenius norm and scalar Cauchy inequality. Equality forces `rank Xrs≤2`, the matched scalar condition `εrα=εsβ=:γ`, and the unused traceless blocks `C_{3−r}=D_{3−s}=0`.

### 3.1. Nonzero matched scalar

If `γ≠0`, the scalar in the sector is `t=2γ≠0`. Write its selected traceless blocks as `C,D`. If both have nonzero eigenvalue magnitudes, their eigenvalues are `±λ`, `±μ` with `λμ≠0`, and they are diagonalizable. The tensor-sum eigenvalues are `t±λ±μ`; two distinct zero sign choices would force `t=0`, `λ=0` or `μ=0`. Thus the nullity is at most one.

If one of `λ,μ` vanishes and its 2×2 block is nonzero nilpotent, similarity-diagonalizing the other block shows that at most one 2×2 summand is singular; that summand has rank one and the other rank two. If both eigenvalues vanish, the commuting nilpotent tensor terms have nilpotent sum, so the nonzero scalar shift is invertible. Hence rank at most two forces **one selected block to be exactly zero**, say `C=0`, and the other, `D`, to have eigenvalues `±t`.

Then `Xrs=I2⊗(tI2+D)` has two equal nonzero squared singular values

`κ²=||tI2+D||_F²=2|t|²+||D||_F²`,

because `tI2+D` has rank one. The other three sectors are `0`, `D⊗I2`, and `−t I4`, in some order. Their operator-norm squares are at most `||D||_F²` or `|t|²`, both strictly below `κ²`. Hence `σ2>σ3`. The case `D=0` is symmetric.

### 3.2. Zero matched scalar

If `γ=0`, then `α=β=0`, and only `C=Cr`, `D=Ds` can be nonzero. If one vanishes, `rank Xrs≤2` forces the other to have rank at most one; the nonzero global pair is exactly the one-zero-factor, traceless-rank-one exception in Section 6.

Suppose both `C,D` are nonzero. The determinant of their tensor sum is `(λ²−μ²)²`, where `±λ`, `±μ` are their eigenvalues. Rank at most two forces `λ²=μ²`. Independently unitary-Schur the two 2×2 blocks, ordering their diagonal eigenvalues as `λ,−λ`. The sector then has the displayed form, for some complex `c,d`,

```
Xrs = [[2λ, d, c, 0],
       [ 0, 0, 0, c],
       [ 0, 0, 0, d],
       [ 0, 0, 0, −2λ]].
```

The first row, supported in the first three columns, and the last column, supported in the last three rows, are orthogonal rank-one pieces of identical squared norm

`κ²=4|λ|²+|c|²+|d|²=||C||_F²+||D||_F²`.

Thus the selected sector has exactly two nonzero squared singular values, both `κ²`. The other sectors are `C⊗I2`, `I2⊗D` and zero; because both `C,D` are nonzero, their squared operator norms are strictly less than `κ²`. Again `σ2>σ3`. This also includes `λ=0`, when the nonzero blocks are nilpotent.

## 4. One selected singular value in each of two sectors sharing a row or column

Suppose the sectors share row `r`. Equality in the previous sector proof requires `C_{3−r}=0` and equality in (2.1) for both `s=1,2`. By (2.2), for `t_s=εrα+εsβ`,

`D_s=t_s(2W_s−I2)`, `C_r²=4t_s² I2`.

Therefore `t_1²=t_2²`, hence `αβ=0`. If either `t_s=0`, both are zero, and `α=β=0`, `D1=D2=0`. Equality in (2.1) reduces to `||C_r||_op²=||C_r||_F²`, so the nonzero `C_r` has rank one. Since also `C_{3−r}=0`, this is exactly the one-zero-factor exception.

Otherwise `t_1,t_2` are nonzero with equal magnitude `|t|`. On the eigenspaces of the normal `D_s`, the selected sector is the direct sum of `C_r+2t_s I2` and `C_r`. Because `C_r²=4t_s² I2`, the first 2×2 block is rank one with squared operator norm

`κ²=||C_r||_F²+8|t|²`,

while the second has strictly smaller norm. Thus each selected sector contributes exactly one top singular value `κ`. The unselected row is scalar-plus-`D_s` and, because `αβ=0`, has squared operator norm `4|t|²`. Moreover `||C_r||_F²≥8|t|²` by its eigenvalues `±2t_s`. Hence `κ²≥16|t|²>4|t|²`, and the global second singular value is strictly larger than the third. The argument for a common column swaps the two factors.

## 5. One selected singular value in each of two sectors with different rows and columns

Equality in the preceding 2+2 proof forces the Frobenius and operator norms of all four local blocks to coincide, so each has rank at most one; it also forces the paired norms to coincide. For nonzero paired blocks, equality in the tensor triangle inequality forces their left and right singular directions to coincide on each factor. Zero paired blocks are normal as well. Therefore `A,B` are normal.

Every nonzero **normal** traceless pair saturating T2 has `σ2>σ3`, as follows. Diagonalize the factors and write their tracezero eigenvalue vectors as `a,b∈C4`. For two distinct tensor-basis positions `(i,j),(k,l)`, the two evaluation functionals `(a,b)↦(a_i+b_j,a_k+b_l)` have Gram matrix

`[[3/2,κ],[κ,3/2]]`, `κ=δik+δjl−1/2∈{−1/2,+1/2}`.

The top eigenvalue `2` is simple. Equality in the corresponding `2L` bound forces the input proportional to its top eigendirection. If the positions differ in both indices, `a=t(e_i−e_k)`, `b=t(e_j−e_l)`. If they share the `A` index, `a=t(2e_i−1/2·1)`, `b=t(e_j+e_l−1/2·1)`; the shared-`B` case is symmetric. In every nonzero case exactly two tensor-sum eigenvalues have modulus `2|t|` and all others have modulus at most `|t|`. Hence `σ2>σ3`.

Sections 3–5 prove the announced equality classification, including possible singular-value ties: choose any two sector locations realizing the top two; saturation forces equality in the corresponding chain.

## 6. The exceptional degenerate pair and the two partial traces

If `σ2>σ3`, the previous coupling packet proves that the maximizing projector `P` is unique and commutes with all sector projections, so both kernel identities hold.

In the remaining case, suppose `B=0` and `A=σ|u⟩⟨v|` has rank one and trace zero. Then `⟨v,u⟩=0`. The top right-singular subspace of `X=A⊗I4` is `span{v}⊗C4`, and every maximizing rank-two projector is

`P=|v⟩⟨v|⊗Q`, where `Q` is any rank-two projector on the second factor.

Thus `XP=σ|u⟩⟨v|⊗Q`, and

`Tr_B(XP)=2A`, `Tr_A(XP)=σ⟨v,u⟩Q=0`.

Since `A` is block diagonal in the coupling split, the upper-right 2×2 block of `2A` vanishes; the other partial trace is zero. The case `A=0`, `rank B=1` is symmetric. The zero pair contributes only the zero kernel vector. Therefore the two partial-trace identities hold for every saturated diagonal coefficient vector and every maximizing `P`, establishing (1.1).

## 7. What remains

This is written mathematics only. It does not assume or conclude the 8×8 residual (1.2), a physical counterexample, any η failure, unrestricted T2/T3/Z2/q3, formal verification, stronger-model-family review or novelty. All named earlier packets and frozen scopes remain unchanged. The result requires disjoint review, especially of the weighted-equality proportionality, same-sector rank classification, spectral-gap claims, and exceptional partial traces.
