# Traceless rank-two duals and a full chiral both-squares-nonnormal T2 class

**Status: WRITTEN, self-contained owner candidate, UNREVIEWED.** This packet does not depend on the earlier 2+2 theorem, Schur-coupling residual, f198's false bound, held/ZERO material, source certificates, or numerical/physical-q examples. It uses finite-dimensional SVD, Frobenius duality, elementary 2×2 unitary Schur form and the local swap identity proved below. It is not a formal proof, stronger-family/human review or novelty claim.

## 1. Main claims and limits

For every operator `R` on `C4⊗C4` with `rank R≤2` and `Tr R=0`, put

`Φ(R)=((Tr_B R)_0,(Tr_A R)_0)`, `G_0=G−(Tr G/4)I4`.

Then

**`||Φ(R)||_F² ≤ 2||R||_F²`.**  (1.1)

Consequently, for **arbitrary** traceless `A,B∈M4(C)`, with `X=A⊗I4+I4⊗B`, `L=||A||_F²+||B||_F²`, if **some** maximizing rank-two right-singular projector `P` satisfies `Tr(XP)=0`, then

**`σ1(X)²+σ2(X)²≤2L`.**  (1.2)

In particular this holds for every pair admitting local Hermitian unitary involutions `Z_A,Z_B` such that `Z_A A Z_A=−A`, `Z_B B Z_B=−B`. Relative to their eigenspace decompositions this is the complete arbitrary off-diagonal-block class, including all 2+2 choices

`A=[[0,E],[F,0]]`, `B=[[0,G],[H,0]]`, `E,F,G,H∈M2(C)`,  (1.3)

with no normality, magnitude, genericity, rank, block-reducibility or other restriction. Section 6 exhibits a fully symbolic subfamily in (1.3) for which both factors are unitarily irreducible and both squares are nonnormal. Thus this is not a normal-class or 2+2-**reducing** theorem.

**Exact original residual:** pairs for which every maximizing rank-two right-singular projector has `Tr(XP)≠0` are not decided by (1.2). No claim is made that (1.3), or the Section 6 example, contains a point outside the entire f274 optimized `η≤2L` region; the all-bases comparison is unpaid. Neither a physical counterexample, unrestricted T2, T3, Z2, q3, any source proof, nor novelty follows.

## 2. Rank-one tracezero bound from local antisymmetry

For vectors `u,v∈C4⊗C4`, let `r=|u⟩⟨v|`. We first prove

`||Tr_A r||_F²+||Tr_B r||_F² ≤ ||u||²||v||²+|⟨v,u⟩|²`.  (2.1)

Let `F_A,F_B` swap the two copies of the A and B factors, respectively, and let `P_-^A=(I−F_A)/2`, `P_-^B=(I−F_B)/2`. A direct swap expansion gives

`||u||²||v||²+|⟨v,u⟩|²−||Tr_A r||_F²−||Tr_B r||_F²`

`=4 ⟨u⊗v,(P_-^A⊗P_-^B)(u⊗v)⟩ ≥0`.

The final operator is an orthogonal projector. In particular, if `Tr r=⟨v,u⟩=0`, then removing the scalar parts of the partial traces can only reduce their squared norms, so

`||Φ(r)||_F ≤ ||r||_F=||u||·||v||`.  (2.2)

This is valid for arbitrary complex vectors, not merely product vectors.

## 3. Nuclear-norm-preserving traceless rank-one decomposition

Let `R` be nonzero, rank at most two, and traceless. If `rank R=1`, (2.2) already proves (1.1). Otherwise take an SVD

`R=U Σ V†`, `Σ=diag(s1,s2)>0`, `U†U=V†V=I2`.

Define the complex 2×2 matrix `M=Σ^(1/2) V† U Σ^(1/2)`. Its trace is `Tr R=0`. There exists a 2×2 unitary `W` such that the diagonal of `W† M W` is zero. For completeness: unitary-Schur `M` to `[[λ,z],[0,−λ]]`; for a unit vector `(cosθ,e^{iφ}sinθ)`, its expectation is `λ cos(2θ)+(z e^{iφ}/2)sin(2θ)`. Choose `φ` opposite the phase of `λ`, then choose `θ∈[0,π/4]` so the two nonnegative magnitudes agree. The cases `λ=0` or `z=0` are immediate. Complete that unit vector orthogonally; because the trace is zero, the other diagonal expectation is zero as well.

Let `w1,w2` be the columns of `W`, and define

`a_i=U Σ^(1/2) w_i`, `b_i=V Σ^(1/2) w_i`, `R_i=|a_i⟩⟨b_i|`.

Then

`R=R1+R2`, `Tr R_i=⟨b_i,a_i⟩=w_i†M w_i=0`,

`||R_i||_F=||a_i||·||b_i||=w_i†Σw_i`,

`Σ_i ||R_i||_F=Tr Σ=||R||_1`.

Applying (2.2), the triangle inequality in the direct-sum Frobenius norm, and `||R||_1≤√2||R||_F` yields

`||Φ(R)||_F≤||R1||_F+||R2||_F=||R||_1≤√2||R||_F`.

Squaring proves (1.1). The decomposition may use nonorthogonal rank-one summands; neither their orthogonality nor an executable construction is assumed.

## 4. From a traceless top-two dual to physical T2

Let `P` be a maximizing rank-two right-singular projector for `X`: `Tr(PX†X)=S2:=σ1(X)²+σ2(X)²`. Such a projector exists, including when the cutoff is degenerate. If `Tr(XP)=0`, then `R=XP` has rank at most two, trace zero, and

`||R||_F²=Tr(PX†X)=S2`.

Because `A,B` are traceless,

`S2 = Tr(R†X) = ⟨(Tr_B R)_0,A⟩_F+⟨(Tr_A R)_0,B⟩_F`.

Cauchy–Schwarz and (1.1) give `S2≤√(2S2 L)`. If `S2>0`, division and squaring yield `S2≤2L`; if `S2=0` it is immediate. This establishes (1.2) with all original local traceless-pair quantifiers and no appeal to the previous 2+2 proof.

## 5. Chiral symmetry gives the required projector

Let `Γ=Z_A⊗Z_B`. The assumed local anticommutation gives `ΓXΓ=−X`, while `Γ` commutes with `X†X`. Simultaneously diagonalize the Hermitian operators `Γ` and `X†X`, and choose any two eigenvectors with the largest Gram eigenvalues; even at a degenerate cutoff their rank-two projector `P` commutes with `Γ`. Therefore

`Tr(XP)=Tr(ΓXPΓ)=Tr((−X)P)=0`.

Section 4 proves T2. In particular arbitrary off-diagonal local blocks (1.3) satisfy the hypothesis with `Z_A=Z_B=diag(I2,−I2)`. The involutions may also have other eigenspace multiplicities; (1.3) is the explicitly relevant 4×4 balanced case.

## 6. A symbolic class with BOTH factors irreducible and BOTH squares nonnormal

Let

`T=[[a,b],[0,d]]`, `A=[[0,I2],[T,0]]`, `B=A`,

with `a,d>0`, `b∈C\{0}`, and `(a²−1)(ad−1)(d²−1)≠0`. These are free symbolic conditions, not a selected numerical instance. Both factors have the chiral form (1.3) and are invertible. Their squares are `diag(T,T)`, which is nonnormal because `b≠0`. We now prove `A` has no nontrivial orthogonal reducing subspace.

Let a Hermitian projection commuting with `A` have block form `P=[[H,K],[K†,L]]`. Comparing `PA=AP` gives

`L=H`, `HT=TH`, `KT=K†=TK`.

Because `T` is nonnormal, any 2×2 Hermitian matrix commuting with `T` must be scalar: otherwise its two eigenspaces would unitarily diagonalize `T`. Thus `H=hI2`. The relation `K†=KT` and its adjoint give `K=T† K T`. Writing `K=(k_ij)`, the `(1,1)`, `(1,2)`, `(2,1)`, `(2,2)` equations successively force `k11=k12=k21=k22=0` because `a²`, `ad`, `d²` are not one. Hence `P=hI4`, and the projection equation gives `h=0` or `h=1`. So `A` is unitarily irreducible, and so is `B`.

An invertible weighted partial permutation decomposes into weighted cycles. If it is unitarily irreducible, there is just one 4-cycle, whose four nonzero eigenvalues are related by multiplication by `i` and cannot all be real. But the characteristic polynomial of this `A` is `(z²−a)(z²−d)`, so all eigenvalues are real. Hence the factors are not weighted partial permutations. They are not normal, not rank one, not square-normal, and not separately 2+2 unitarily reducing. This separates the class from the named f215/f281 structural cases and from the earlier 2+2 theorem, but **does not** establish failure of f274's optimized certificate or exclusion by every other sufficient test.

## 7. Boundaries and review

This packet is a new all-variable written proof and requires disjoint review of the swap identity, the hollow nuclear decomposition, the Ky Fan dual step, and the irreducibility example. It gives no executable check, Lean/kernel or independent-family/human validation, no unrestricted T2/T3/Z2/q3, no η-failure, and no novelty clearance. Earlier frozen packets and all process, HOLD and ZERO restrictions remain unchanged.
