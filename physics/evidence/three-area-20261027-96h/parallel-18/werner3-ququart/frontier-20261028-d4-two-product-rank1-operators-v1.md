# Source-independent q3 positivity and equality for two product rank-one operators

**PhysicsResearch96h-2 / physics-1. WRITTEN all-variable proof; UNREVIEWED.** This source-independent theorem strictly subsumes the two-product-projector class in `frontier-20261028-d4-nonproduct-q3-equality-families-v2.md`, SHA256 `c1aade137e8274ace51fb2f7d1f0113d2fc09d5f78b0660f8d703672f28d7843`: the two summands may now be arbitrary complex non-Hermitian product rank-one operators, and their local ket and bra directions need not agree. It establishes original q3≥0 and a necessary-and-sufficient algebraic equality criterion on this entire specified class, not on every complex rank≤2 operator. It is not a source-conditional variant, novelty claim, whole-target proof, global equality classification, or parent/f62/f153/human/family/formal/operational acceptance.

## 1. Exact theorem

Let `H=(C⁴)^tensor3`. At each site i choose arbitrary nonzero complex rank-one operators `A_i,B_i` on C⁴, and set

`A=A_1⊗A_2⊗A_3`, `B=B_1⊗B_2⊗B_3`, `C=αA+βB`, with α,β∈C.

Both A,B have global operator rank1, so C has rank≤2. Define the local Hermitian form

`g_i(X,Y)=Tr(X†Y)−(1/2) conjugate(Tr X) Tr Y`,
`a_i=g_i(A_i,A_i)`, `b_i=g_i(B_i,B_i)`, `h_i=g_i(A_i,B_i)`.

For rank-one nonzero inputs `a_i,b_i>0`. Define `a=Π_i a_i`, `b=Π_i b_i`, `h=Π_i h_i`. Then the original unnormalized-trace functional has the exact form and bound

`q3(C) = a|α|²+b|β|²+2 Re(conjugate(α) β h)`
`      >= (sqrt(a)|α|−sqrt(b)|β|)² >= 0`.                             (1)

This holds for every complex local rank-one A_i,B_i and every complex α,β, with no source-certificate assumption and no selected numerical target state.

**Exact equality criterion in this class.** If `α=β=0`, C=0 and q3=0. Otherwise q3(C)=0 if and only if α≠0, each of the three local determinants vanishes,

`|h_i|²=a_i b_i  (i=1,2,3)`,

and

`β=−(a/h)α`.                                                         (2)

When the local determinants vanish, h is automatically nonzero, so (2) is well-defined. These conditions also include a possible cancellation C=0 when A and B are proportional. If a nonzero equality occurs, C has exact rank2, because rank1 is strictly positive as shown in §4. This criterion is complete for the two-product-rank-one class, not for arbitrary rank2 C.

## 2. Each local two-column Gram is positive

For every local matrix X of rank at most2,

`g_i(X,X)=||X||HS²−|Tr X|²/2 >= 0`.                                  (3)

Indeed, the absolute trace is at most the sum of the singular values, which is at most `sqrt(2)||X||HS`. The linear span of A_i,B_i consists entirely of matrices of rank at most2. Applying (3) to `s A_i+t B_i` for arbitrary complex s,t shows the 2×2 Hermitian matrix

`G_i = [[a_i,h_i],[conjugate(h_i),b_i]]`

is PSD. Hence `|h_i|²≤a_i b_i`. For nonzero rank1 X, the stronger rank-one trace inequality `|Tr X|²≤||X||HS²` gives `g_i(X,X)≥||X||HS²/2>0`, establishing a_i,b_i>0.

For two product operators, every original partial trace factorizes. Expanding the eight subsets,

`<A,W(B)>HS = Σ_S (−1/2)^|S| <Tr_S A,Tr_S B>HS`
`               = Π_i [Tr(A_i†B_i)−(1/2) conjugate(Tr A_i) Tr B_i] = h`,

where W is the self-adjoint original trace-insertion operator. Likewise `q3(A)=a`, `q3(B)=b`. This proves the equality in (1). Multiplying the three local determinant inequalities gives `|h|²≤ab`; inserting this and `Re(conjugate(α)βh)≥−|α||β||h|` gives the bound in (1). Equivalently, the global 2×2 Gram is the Hadamard product `G_1∘G_2∘G_3`, PSD; the displayed scalar proof needs no imported Schur-product theorem.

For q3=0 with nonzero (α,β), the global PSD 2×2 Gram must have determinant zero. Because each `a_i b_i>0` and each `|h_i|²/(a_i b_i)≤1`, equality in the product occurs exactly when every local determinant is zero. The first null-vector equation is `aα+hβ=0`, giving (2). Conversely, (2) and the local equalities make the global 2×2 Gram singular with (α,β) in its nullspace. If either α or β alone vanishes, strict positivity of a,b shows q3>0 unless both are zero.

## 3. Local determinant degeneracy is an exact two-dimensional condition

The local equality in (2) has a concrete equivalent description. For fixed nonzero rank-one local A_i,B_i,

`|h_i|²=a_i b_i`

if and only if either A_i,B_i are linearly dependent, or their complex linear span contains a nonzero scalar multiple of an orthogonal rank2 projection. In the dependent case a nonzero coefficient pair gives the zero matrix, hence the Gram is singular. In the independent case, singularity gives a nonzero `X=s A_i+t B_i` with rank≤2 and `g_i(X,X)=0`; conversely any such X makes the PSD Gram singular.

To characterize that equality, let the positive singular values of a nonzero rank≤2 X be σ1,σ2. The chain

`|Tr X| <= σ1+σ2 <= sqrt(2)||X||HS`

is equality exactly when X has rank2, σ1=σ2=σ>0, and the left/right singular vectors coincide up to one common complex phase. In detail, writing `X=σ Σ_(j=1)^2 |p_j><q_j|`, equality in `|Σ_j <q_j,p_j>|≤2` forces each `p_j=e^(iθ) q_j` with the same θ. Hence `X=σ e^(iθ) P` for an orthogonal rank2 projection P. No normality, positivity or product assumption is made on A_i,B_i themselves.

## 4. Strict positivity for nonzero global rank-one C

For any global rank-one `C=x y†`, partial-trace contractions give

`q3(C)=<x⊗y, Π_i(I−F_i/2)(x⊗y)>`.

The site swaps F_i commute and every factor is at least I/2, so `q3(C)≥||C||HS²/8>0`. Thus a nonzero q3=0 matrix in §1 must have rank2, even if A and B themselves are linearly dependent on some sites. This standard swap proof is source-independent and does not assert global rank2 positivity outside the class in §1.

## 5. Nonproduct equalities and prior two-projector result

Set `A_i=|u_i><u_i|`, `B_i=|v_i><v_i|` for arbitrary local unit vectors and let `t_i=|<u_i,v_i>|²`. Then `a_i=b_i=1/2` and `h_i=t_i−1/2`; the local determinant condition is `t_i∈{0,1}`. If k local overlaps vanish, (2) gives α=β for odd k and α=−β for even k. For k=2 or k=3, α≠0, these are genuine nonproduct rank2 equalities: across an orthogonal site whose complement has another orthogonal site, the two local operator factors and the two complementary factors are respectively independent. For k=0 the resulting cancellation is C=0. Thus product-operator equalities do not exhaust the original equality set, while the separate f153 product-family review is not contradicted or extended.

## 6. Scope and provenance

The only mathematical inputs are the original q3 partial-trace definition, trace/singular-value inequalities, elementary 2×2 PSD algebra and finite tensor products. This proof does not use the source identity/PSD certificate, the conditional antisymmetry packet, any selected target q3 value, or the elected HELD/ZERO/NONINPUT episode or its guidance. The prior public full-target Werner claim retires new-discovery status; no literature-exhaustiveness or novelty claim is made. All historic process/held findings and frozen f153/f62 boundaries remain unchanged.
