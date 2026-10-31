# A sharp operator-norm strengthening for the chiral T2 class

**Status: WRITTEN, UNREVIEWED additive strengthening** of `frontier-20261029-d4-t2-traceless-rank2-dual-and-chiral-class-v1.md` (SHA-256 da483d5e3b24c798fc9ac0384a10a5b869d417c511ac3efd900ccec1b982919b). That packet is unchanged. This note uses its rank-one tracezero swap inequality only, and no 2+2-reducing result, false f198 lemma, held material, source certificate, numerical instance, physical q, or execution.

## 1. Full all-variable operator bound

For arbitrary traceless `A,B∈M4(C)`, let `X=A⊗I4+I4⊗B` and `L=||A||_F²+||B||_F²`. Suppose a top singular pair `Xv=σ1(X)u`, with `||u||=||v||=1`, can be chosen with `⟨v,u⟩=0`. Then

**`||X||_op² ≤ L`, hence `σ1(X)²+σ2(X)²≤2L`.**  (1.1)

Indeed `R=|u⟩⟨v|` has rank one, trace zero and Frobenius norm one. The explicitly proved rank-one swap identity in the named source yields `||((Tr_B R)_0,(Tr_A R)_0)||_F≤1`. Because both local factors are traceless,

`σ1(X)=|Tr(R†X)| ≤ √L`.

No condition on the second singular pair or any spectral gap is needed; if `X=0`, (1.1) is immediate.

## 2. Chiral pairs and the exact nonclaim

If local Hermitian unitary involutions obey `Z_A A Z_A=−A`, `Z_B B Z_B=−B`, then `Γ=Z_A⊗Z_B` anticommutes with `X` and commutes with `X†X`. A top right-singular vector `v` may be chosen as a `Γ` eigenvector even in a degenerate top eigenspace; for `σ1>0`, `u=Xv/σ1` has the opposite `Γ` eigenvalue and is orthogonal to `v`. Therefore (1.1) holds for **every** chiral pair, in particular every arbitrary off-diagonal-block pair `A=[[0,E],[F,0]]`, `B=[[0,G],[H,0]]` in the balanced 2+2 decompositions.

This sharpens that packet's T2 conclusion to the global operator-norm inequality on the same full, no-threshold class; it includes the symbolic unitarily irreducible both-squares-nonnormal example already given there. It does not establish that any member lies outside f274's optimized `η≤2L` region. Nor does it resolve pairs without such a top orthogonal singular pair, unrestricted T2/T3/Z2/q3, physical counterexamples, source correctness or novelty. Review of the named rank-one identity and this argument remains required.
