# The d=4 two-copy nonnormal obligation: sharp rank-one residual and square-normal class

**PhysicsResearch96h-2 / physics-1. WRITTEN all-variable candidate; UNREVIEWED.** This self-contained packet supersedes `frontier-20261029-d4-t2-nonnormal-sharp-residual-consolidated-v1.md`, SHA256 `cc38178afec4a6aaa0020d63d8170c583d93b3c865aa19c89d4754c97ef135e9`, as the single candidate for this line; v1 is retained unchanged. It strengthens v1's trace-zero bound, proves the previously unpaid rank-one-B residual with an explicit gap, and packages the nonnormal 2+2-block result in the intrinsic condition **A² normal or B² normal**.

The earlier frozen T2 packet v3, SHA256 `7c0df3e55f53eae89710381a8c1cbf3c5a58418e192d74997dd94181fec7acaf`, remains under disjoint f196 review. This packet is independent of that review and does not change its scope. It assumes no source certificate or held input and makes no full T2/T3, global equality, novelty, parent/reviewer, formal/Lean, human/family or physical-operational acceptance claim.

## 1. Exact scope

For traceless complex `A,B∈M_4(C)` let `X=A⊗I_4+I_4⊗B`. The original two-copy dual obligation is

`σ_1(X)²+σ_2(X)² <= 2(||A||F²+||B||F²)`.                             (T2)

This packet proves, with only elementary named ingredients:

1. The sharp all-variable inequality (†) from frozen v3, with an explicit nonnegative remainder. Thus (T2) holds for every A when B has rank≤1; the near-rank-one residual of (†) is paid.
2. (T2) holds whenever either A² or B² is normal, with the other matrix arbitrary traceless. This includes all normal matrices, all square-zero matrices (rank up to2), and genuinely nonnormal full-rank matrices. The intrinsic condition is justified by an exact 4×4 unitary-block classification, not assumed.

Neither assertion covers arbitrary traceless nonnormal A,B whose squares are both nonnormal. No claim is made about that remainder or the literature status of these classes.

## 2. The trace-zero weighted lemma: a stronger universal coefficient

**Lemma 2.1.** Let A∈M_4(C) have `Tr A=0`, and let u,v∈C⁴ satisfy `||u||²+||v||²=1`. Write `t=||u||²`, `q=||v||²=1−t`, and

`d_A(u,v)=||A||F²−||Au||²−||Av||² >= 0`.

Then

`|<v,Au>|² <= t(1+2q) d_A(u,v) <= (t+1/2)d_A(u,v)`.              (2.1)

This is an all-variable trace-zero inequality, with no assumption that A is normal, low rank or positive.

*Proof.* Set `U=[u v]`, `D=I−uu†−vv†`. D is PSD because `uu†+vv†` is PSD of trace1, and `d_A=Tr(A†A D)`. First assume u,v linearly independent; then D is positive definite. Set

`z=<u,v>`, `r=|z|²`, `Δ=tq−r>0`.

In the weighted Hilbert–Schmidt inner product `<M,N>_D=Tr(M†ND)`, the linear functional `A↦<v,Au>` has Riesz representer `Z=v u†D^(−1)`, and `Tr A` has representer `D^(−1)`. Orthogonally projecting Z onto the trace-zero subspace gives the exact upper bound

`|<v,Au>|² <= N Tr(A†AD)`,
`N=q·u†D^(−1)u − |v†D^(−1)u|²/Tr(D^(−1))`.                         (2.2)

For the 2×2 Gram matrix `G=U†U=[[t,z],[bar z,q]]`, `det(I−G)=Δ`. Woodbury inversion gives

`u†D^(−1)u=(t²+r)/Δ`, `|v†D^(−1)u|²=r/Δ²`, `Tr(D^(−1))=2+1/Δ`.

Thus

`N=q(t²+r)/Δ−r/[Δ(1+2Δ)]`,
`(1+t)−N=[1+2tq−4r]/[1+2Δ]`.

Writing r=tq−Δ, the last fraction is `(1−2tq+4Δ)/(1+2Δ)>=1−2tq`, since the difference is `(2+4tq)Δ/(1+2Δ)>=0`. Therefore `N<=t+2tq`, the first part of (2.1). Since tq≤1/4, the second follows. The rational identity was also checked by exact `fractions.Fraction` polynomial-dictionary arithmetic in the eval kernel after clearing denominators; that check covers only this algebra.

For dependent u,v with both nonzero, approximate v by vectors of the same norm not collinear with u, and take the continuous limit. If u=0 or v=0, the left side is zero and D is PSD. ∎

**Corollary 2.2 (the full sharp (†), with margin).** Let σ=||A||op. For every pair u,v as above,

`2||A||F² − [||Au||²+||Av||²+|<v,Au>|²/(1+t)+σ²]`
` >= (||A||F²−σ²) + [(1−2tq)/(1+t)] d_A(u,v)`
` >= (||A||F²−σ²) + d_A(u,v)/[2(1+t)] >= 0`.                    (2.3)

This proves the exact (†) in frozen v3 for all traceless A, not only away from its prior near-rank-one residual. For A≠0, equality in (2.3)'s left side can occur only when A has rank1 and u,v are collinear with its top right singular vector: equality forces `||A||F²=σ²` and `d_A=0`; the latter means `uu†+vv†` has eigenvalue1 and trace1. Traceless rank-one A then has its left singular vector orthogonal to that right singular vector. A=0 gives equality trivially.

## 3. Full rank-one-B proof, including strictness in its cross case

Let B be nonzero, traceless and rank1. A local unitary makes `B=bE_01` with b>0. Relative to `span{e0,e1}⊕span{e2,e3}` at site2, X is `Γ_b⊕A⊕A`, with

`Γ_b=[[A,bI_4],[0,A]]`.

For any unit `(u,v)∈C⁴⊕C⁴`, put t=||u||², q=1−t, `L=<v,Au>` and `σ=||A||op`. Completion of the square plus (2.1) gives

`2(||A||F²+b²)−[||Γ_b(u,v)||²+σ²]`
` >= (||A||F²−σ²) + [(1−2tq)/(1+t)]d_A(u,v)`
`    +(1+t)|b−L/(1+t)|² >=0`.                                       (3.1)

Indeed `||Γ_b(u,v)||²=||Au||²+||Av||²+b²q+2 Re(bar b L)`. The cross-block candidate `σ_1(Γ_b)²+σ_1(A)²` is therefore bounded by the T2 right-hand side. If both largest singular values are in the Γ_b block, their right singular subspace has a 2D leg at site2 and Lemma 5.1 below applies. If both are in the two complementary A blocks, the sum is at most `2σ²<=2||A||F²`. Thus (T2) holds. B=0 is immediate.

For b>0 the mixed-block estimate (3.1) is strict: if every remainder vanished, `||A||F²=σ²` and `d_A=0` would imply L=0 by (2.1), while the last square would imply b=0. This does not assert a global q2/q3 gap or classify all equality cases.

## 4. A 4×2 operator-norm inequality

**Lemma 4.1.** For any traceless A∈M_4(C) and T∈M_2(C), with no normality or rank assumptions,

`||A⊗I_2+I_4⊗T||op² <= ||A||F²+2||T||F²`.                          (4.1)

*Proof.* Let ψ,φ be arbitrary unit vectors in C⁴⊗C², put `c=<φ,ψ>`,

`M=Tr_2 |ψ><φ|∈M_4`, `N=Tr_1 |ψ><φ|∈M_2`,
`M_0=M−cI_4/4`, `N_0=N−cI_2/2`.

The traces of M,N equal c, so tracelessness gives

`<φ,(A⊗I_2+I_4⊗T)ψ>=Tr(A M_0)+Tr(T N_0)`.

Weighted Hilbert–Schmidt Cauchy–Schwarz gives

`|<φ,Γψ>|² <= (||A||F²+2||T||F²)(||M_0||F²+||N_0||F²/2)`.       (4.2)

Let `s_1=||N||F²` and `s_2=||M||F²`. By the swap trick, these are the overlaps of the corresponding normalized one-site reduced density matrices of ψ,φ; hence `0<=s_1,s_2<=1`. Since `(I−F_1)(I−F_2)` is PSD on two copies,

`1−s_1−s_2+|c|²>=0`.                                                 (4.3)

Consequently

`||M_0||F²+||N_0||F²/2 = s_2+s_1/2−|c|²/2`
` = s_2/2+(s_1+s_2−|c|²)/2 <=1`.

Take the supremum in (4.2) over unit ψ,φ. ∎

Equation (4.3) is the expectation of the displayed PSD product in ψ⊗φ; its full-swap term is |c|² and its one-site swaps are s_1,s_2. It is not a source assumption.

## 5. The one-supported-site lemma used for same-block pairs

**Lemma 5.1.** If F⊂C⁴⊗C⁴ has dimension2 and its leg at some **site** lies in a 2D local subspace, then for every traceless A,B,

`||(A⊗I+I⊗B)P_F||F² <= ||A⊗I+I⊗B||F²/2`.                          (5.1)

*Proof.* This is the one-supported-site case of the qualified f168 ladder/dual disposition; the argument is repeated. Suppose F⊂C⁴⊗E, dim E=2, and set `C=XP_F`. Then rank C≤2 and its input leg at site2 is supported in E. Under vectorization the compressed local factor `K=I−|Ω><Ω|/2` has the positive product decomposition

`I⊗bar P_E−|Ω_E><Ω_E|/2`
`=3∫_(u∈S(E)) |u_perp><u_perp|⊗|bar u><bar u|dμ(u)`
` +(I−P_E)⊗bar P_E`.                                                 (5.2)

The finite complement is itself a sum of positive rank-one products. This follows from the elementary Haar second moment `∫|u><u|^tensor2=(P_E⊗P_E+F_E)/6`, with a partial transpose. Each product contraction leaves a one-site matrix of rank≤2 and hence contributes `q1(Z)=||Z||F²−|Tr Z|²/2>=0`. Therefore `q2(C)>=0`.

On the original d=4 two-site operator space, the self-adjoint trace-insertion product W is a reflection and `WX=−X`. Thus `q2(C)=||C||²−2||P_-C||²` and `<X,C>=||C||²`. Cauchy–Schwarz gives `||P_-C||²>=||C||⁴/||X||²`; combining with `q2(C)>=0` gives (5.1). Zero X or C is trivial. Site exchange and adjoints give the remaining cases. ∎

The lemma requires a supported leg at **one site**, not two legs at the same site.

## 6. Two separately traceless reducing blocks

**Theorem 6.1.** If B is unitarily block diagonal `B=B_1⊕B_2`, with `B_1,B_2∈M_2(C)` each traceless, then (T2) holds for every traceless A. The same conclusion holds with A,B exchanged.

*Proof.* X is the orthogonal direct sum of `Γ_j=A⊗I_2+I_4⊗B_j`. Its singular values are the union of the two block lists. If the top two are chosen from the same block, their right singular subspace has a 2D leg at site2, and Lemma 5.1 applies. If one is chosen from each block, Lemma 4.1 gives

`σ_1(Γ_1)²+σ_1(Γ_2)² <=2||A||F²+2(||B_1||F²+||B_2||F²)`
`=2(||A||F²+||B||F²)`.

Ties permit choosing singular vectors from the block decomposition. ∎

## 7. Intrinsic square-normal condition

**Lemma 7.1.** A traceless B∈M_4(C) has B² normal if and only if either B is normal, or B is unitarily block diagonal with two separately traceless 2×2 blocks.

*Proof.* A normal B has normal B². If B is a direct sum of traceless 2×2 blocks, Cayley–Hamilton gives `B_j²=−det(B_j)I_2`, so B² is block-scalar and normal.

Conversely suppose B² is normal. Since B commutes with B², each spectral subspace of B² is invariant under B; the orthogonal spectral decomposition therefore also makes every such subspace reducing for B. On the zero-eigenvalue subspace B²=0, so `ran B⊂ker B`. An SVD of B from the orthogonal complement of its range to its range gives 2×2 nilpotent blocks and leftover zero scalars.

On a spectral subspace of B² with eigenvalue λ≠0, choose μ with μ²=λ. The polynomial `(z−μ)(z+μ)` has distinct roots, so the restriction of B is diagonalizable with eigenvalues ±μ. With `E_+=ker(B−μI)` and its orthogonal complement, it has block form

`[[μ I_p, C],[0,−μ I_q]]`.

Indeed E_+ accounts for the full algebraic multiplicity of μ, and the quotient has only eigenvalue −μ and satisfies D²=λI, hence is −μI. Independent unitary changes on the two summands put C into singular-value diagonal form; reordering gives 2×2 traceless blocks `[[μ,c_j],[0,−μ]]` plus scalar leftovers ±μ.

Across all spectral subspaces, peel off only the genuinely nonnormal 2×2 blocks and leave their zero-coupling pairs as scalar summands. Their traces are zero. If none exists, B is a diagonal scalar sum and hence normal. If one exists, the remaining two scalar summands have total trace0 and form one traceless 2×2 block. If two exist, they exhaust dimension4. Thus the stated alternative holds. ∎

**Theorem 7.2.** The T2 dual inequality holds whenever A² or B² is normal.

*Proof.* By site exchange take B² normal. If B is normal, local-unitary diagonalization makes X block diagonal over the four local eigenvectors of B; a top-two singular subspace uses at most two of them and Lemma 5.1 applies. Otherwise Lemma 7.1 and Theorem 6.1 apply. ∎

## 8. Remaining obligation and provenance

The general two-copy T2 remains unpaid for arbitrary traceless A,B with both squares nonnormal; this packet neither proves nor disproves that case. The full original three-copy target and global equality classification remain unpaid. There is no proof here of a positive global q2/q3 gap; only the explicitly displayed mixed-block remainder is strict for b>0.

The arguments use original q2/trace algebra, weighted finite-dimensional Cauchy–Schwarz, ordinary Haar second moments, singular values, spectral theory, SVD and elementary swap positivity. They do not use a source certificate, a Böttcher–Wenzel premise, an f196 review return, an elected HELD/ZERO/NONINPUT episode/consumer/guidance, a selected physical target value or new finite Hessian/descent variants. Historical process findings and f153/f62/f168/f196 boundaries remain unchanged. The public prior full-target claim retires new-discovery status; no novelty or literature-exhaustiveness claim is made.
