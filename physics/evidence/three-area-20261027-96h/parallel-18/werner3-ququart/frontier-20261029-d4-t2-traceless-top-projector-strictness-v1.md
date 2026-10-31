# Strict T2 on the entire tracezero-top-projector class outside the weighted-cycle boundary

**Status: WRITTEN, UNREVIEWED additive corollary** of the self-contained `frontier-20261029-d4-t2-traceless-dual-strict-chiral-consolidated-v2.md` (SHA-256 b96fcf9f42e0762132d7b843149f424fcde28bd978439b144f3196e09e34efb5). It extends that packet's strict equality analysis from orthogonal **one**-singular-pair inputs to the full **top-two tracezero-projector** class. The source bytes and any frozen review scope are unchanged. No physical q/numerical instance, execution, held/ZERO material, source correctness or novelty claim is used.

## 1. Exact result

Let arbitrary traceless `A,B∈M4(C)` have tensor sum `X=A⊗I4+I4⊗B`, `L=||A||_F²+||B||_F²`, and `S2=σ1(X)²+σ2(X)²`. Assume **some** maximizing rank-two right-singular projector `P` satisfies `Tr(XP)=0`. The consolidated source proves `S2≤2L`. We prove the equality boundary:

**If `S2=2L>0`, then both A and B are supported on local reducing subspaces of dimension at most two.**  (1.1)

Each factor is therefore unitarily similar to a weighted 2-cycle plus zeros, and both local squares are normal. Consequently, on this entire original-pair class, **if either local square is nonnormal OR either factor is not unitarily similar to a weighted partial permutation, then `S2<2L`**. No chiral symmetry, orthogonality of an individual singular pair, local rank, irreducibility or magnitude assumption is imposed.

The original cases in which every top-two maximizing `P` has nonzero `Tr(XP)` remain open in this route. Whether any member of the tracezero-top class escapes the full f274 optimized `η≤2L` region remains unpaid. Neither a physical/η counterexample nor unrestricted T2, T3, Z2, q3 or novelty follows.

## 2. Equality in the tracezero rank-two dual bound

Set `R=XP`. Then `rank R≤2`, `Tr R=0`, `||R||_F²=S2=2L`, and

`S2=⟨Φ(R),(A,B)⟩_F≤||Φ(R)||_F√L≤√2||R||_F√L=2L`.

Because `S2=2L>0`, all inequalities are equalities. Frobenius Cauchy–Schwarz therefore gives

`Φ(R)=2(A,B)`, `||Φ(R)||_F=√2||R||_F`.  (2.1)

The consolidated source decomposes any traceless rank-at-most-two `R` into tracezero rank-one terms `R=r1+r2` such that

`||Φ(R)||_F≤||Φ(r1)||_F+||Φ(r2)||_F≤||r1||_F+||r2||_F=||R||_1≤√2||R||_F`.  (2.2)

Equality in the last inequality forces `rank R=2` with two equal positive singular values `s`. In the source's SVD/hollowing construction each `||r_i||_F=s`. Equality at the other steps of (2.2) gives

`||Φ(r_i)||_F=||r_i||_F=s`, `Φ(r1)=Φ(r2)`.  (2.3)

The second statement is equality in the triangle inequality in a complex Hilbert space: the two nonzero vectors must have the same phase, and their norms coincide. Combining (2.1) and (2.3) yields

`(A,B)=Φ(r1)=Φ(r2)`.  (2.4)

## 3. From the rank-one equality to local support

Normalize `r1=s|u⟩⟨v|` with `||u||=||v||=1`. Its trace is zero, so `u⊥v`. Equality `||Φ(r1)||_F=||r1||_F` in the rank-one local-swap identity forces

`(P_-^A⊗P_-^B)(u⊗v)=0`.

The consolidated source proves the following purely algebraic mixed-minor implication: if unit `u,v` are orthogonal and the displayed antisymmetric tensor vanishes, then **both** local partial traces of `|u⟩⟨v|` are supported on local reducing subspaces of dimension at most two. Briefly, Schmidt-diagonalizing `u` shows its Schmidt rank cannot exceed two; rank two forces `v` into the same 2×2 coefficient support, and rank one forces `v` into a first-row/first-column cross with vanishing intersection.

Equation (2.4) now gives the same local reducing-support property for `A,B`, proving (1.1). Each supported block is traceless; Cayley–Hamilton makes its square scalar, and the orthogonal complement contributes zero, so both full local squares are normal. Unitary hollowing of each traceless 2×2 block yields `[[0,p],[q,0]]` plus zeros, a weighted 2-cycle. The asserted strictness is the contrapositive, with the separately established `S2≤2L`.

## 4. Scope

This is an equality-boundary result and a strict nonnormal-square/non-weighted-factor corollary for the **whole** tracezero-top-projector class, not an assertion that all original pairs meet the trace condition. It is independent of the 2+2-reducing physical theorem and the 8×8 Schur-coupling chain. It does not settle optimized f274 membership, unrestricted T2/T3/Z2/q3, physical counterexamples, external-source correctness, execution, formal/kernel or stronger-family/human review, or novelty. Disjoint review must check the nuclear-decomposition equality phases and the referenced mixed-minor implication.
