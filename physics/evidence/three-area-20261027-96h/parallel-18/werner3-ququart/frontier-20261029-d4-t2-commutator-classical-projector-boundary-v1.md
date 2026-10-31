# The exact singular boundary of the full T2 commutator residual

**Status: WRITTEN, UNREVIEWED additive theorem.** This refines the full-original-quantifier Hermitian commutator reduction `frontier-20261029-d4-t2-hermitian-commutator-residual-v1.md` (SHA-256 bf6057bb7184bba6ef399986cbcdc0367ba672c02c38783035980fa43f6e44c9). It reconstructs its only prerequisite—the normal eigenvalue evaluation Gram—below. It does not need the separately UNREVIEWED 2+2, tracezero-dual, chiral, product-boundary or Schur-chain packets. No numerical/physical-q instance, program, external source, false f198 lemma, held/ZERO input or novelty claim is used.

## 1. Exact singularity classification

For rank-two `P` on `C4⊗C4`, let `K_P` be the real symmetric form on pairs of traceless Hermitian local matrices defined in the named commutator reduction:

`K_P(H,H)=2(||A_H||_F²+||B_H||_F²)−Tr[P(A_H⊗I+I⊗B_H)²]`.

Call `P` **product-basis diagonal** if there are local orthonormal bases in which it is the sum of projectors onto two distinct product-basis vectors. Then

**`K_P` is singular iff `P` is product-basis diagonal.**  (1.1)

In addition, for **every** product-basis-diagonal `P`, the full original complex-source T2 gap is nonnegative. Thus, after paying this exact boundary, the original nonnormal commutator inequality needs checking only for projectors that are not product-basis diagonal, where `K_P` is positive definite. This is not a proof of the interior inequality.

## 2. Normal evaluation and equality

For a tracezero Hermitian pair `H=(A_H,B_H)`, independently diagonalize the local factors, with real eigenvalue vectors `a,b∈R4`, each summing to zero. For two distinct tensor positions `(i,j),(k,l)`, the evaluation map sends `(a,b)` to `(a_i+b_j,a_k+b_l)` and has Gram matrix

`[[3/2,κ],[κ,3/2]]`, `κ=δik+δjl−1/2∈{−1/2,+1/2}`.  (2.1)

Its largest eigenvalue is `2`, so the two largest squared eigenvalue magnitudes of `X_H` sum to at most `2(||A_H||²+||B_H||²)`. Consequently `K_P⪰0` for every `P`.

If `K_P` is singular, take `H≠0` with zero form. The fixed-projector value and top-two maximum must both equal the upper bound. Equality in (2.1) selects its simple top eigendirection:

- if both tensor indices differ: `a=t(e_i−e_k)`, `b=t(e_j−e_l)`;
- if only the A index is shared: `a=t(2e_i−(1/2)1)`, `b=t(e_j+e_l−(1/2)1)`;
- if only the B index is shared, exchange the two factors.

Here `t≠0` is real. In every case exactly two tensor-sum eigenvalues have magnitude `2|t|`, and all others have magnitude at most `|t|`. Thus the maximizing rank-two projector is **unique** and is the projector onto those two product eigenvectors. This proves the forward direction of (1.1), including degeneracy of the two top magnitudes.

Conversely, for any two distinct product-basis positions, choose nonzero traceless real diagonal `a,b` in the top eigendirection of (2.1). The displayed pair `H` has zero `K_P` form. Hence `K_P` is singular, proving the reverse direction. The classification concerns diagonalizability in a product basis; it does not assert that every separable rank-two projector has that property.

## 3. The full complex-source inequality on this boundary

In the product basis from (1.1), let

`P=|ij⟩⟨ij|+|kl⟩⟨kl|`, `X=A⊗I4+I4⊗B`,

where `A,B` are now **arbitrary complex traceless matrices**. Directly,

`Tr(PX†X)= Σ_{(p,q)∈{(i,j),(k,l)}} [||A e_p||²+||B e_q||²+2 Re(conjugate(A_pp) B_qq)]`.

Separate local diagonal entries `a_p=A_pp`, `b_q=B_qq` from offdiagonal entries. Each offdiagonal entry in an A column appears with multiplicity `m_p∈{0,1,2}` among the two positions; the coefficient of its squared modulus in the gap `2(||A||²+||B||²)−Tr(PX†X)` is therefore `2−m_p≥0`. The same holds for B columns.

The diagonal contribution is exactly

`2(||a||²+||b||²)−(|a_i+b_j|²+|a_k+b_l|²)≥0`

by the complex version of Gram bound (2.1). Thus the **entire full-source gap is nonnegative** for every product-basis-diagonal `P`, irrespective of normality of `A,B`. No appeal to a limiting argument is made.

## 4. What remains

For every non-product-basis-diagonal `P`, (1.1) gives `K_P>0`. The full original T2 obligation is therefore exactly the still-unproved ordinary weighted-commutator inequality

`||K_P^(−1/2) J_P K_P^(−1/2)||_op≤1`

for every such `P`, with `J_P` the marginal commutator operator defined in the named reduction. The unweighted bound `||J_P||≤1` does not pay it. This packet does not settle the interior, imply that all separable projectors are paid, or prove unrestricted T2/T3/Z2/q3, an f274 η failure, a physical counterexample, execution, formal/kernel or stronger-family/human review, external-source correctness or novelty. The equality classification and offdiagonal multiplicity argument require disjoint written review.
