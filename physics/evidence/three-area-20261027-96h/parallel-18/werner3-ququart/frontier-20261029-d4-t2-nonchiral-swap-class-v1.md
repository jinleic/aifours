# A nonchiral swap-antisymmetric original T2 class

**Status: WRITTEN, UNREVIEWED.** This is a direct corollary of the orthogonal-top-singular-pair theorem and its mixed-minor equality proof in `frontier-20261029-d4-t2-traceless-dual-strict-chiral-consolidated-v2.md` (SHA-256 b96fcf9f42e0762132d7b843149f424fcde28bd978439b144f3196e09e34efb5). It is not a local-chiral class, a normal-factor theorem, a small-parameter estimate, an optimized-certificate counterexample or a novelty claim. No numerical/physical q, scientific program, false f198 estimate or held/ZERO input is used.

## 1. All-variable statement

For any traceless `A,B∈M4(C)` such that `B=−W A W†` for some unitary `W`, put `X=A⊗I4+I4⊗B`, `L=||A||_F²+||B||_F²`. Then

`||X||_op²≤L`, hence `σ1(X)²+σ2(X)²≤2L`.  (1.1)

If `A²` is nonnormal, then `B²` is also nonnormal and **both inequalities are strict**. More generally strictness follows if `A` is not unitarily similar to a weighted partial permutation. No other assumption on `A` or `W` is made.

To prove this, conjugate the second local factor by `W†`, which preserves all singular values and `L`, and reduce to `B=−A`. Let `S` be the global tensor-swap involution: `S(x⊗y)=y⊗x`. Then

`SXS=−X`, `[S,X†X]=0`.

Choose a top right singular vector `v` that is also an eigenvector of `S`. If `σ1>0`, its left partner `u=Xv/σ1` has the opposite swap parity, so `u⊥v`. The named consolidated theorem proves `σ1²≤L` from exactly this condition, and proves equality forces both `A²,B²` normal and both factors supported weighted 2-cycles. This proves (1.1) and its strictness conclusions. If `X=0`, the conclusion is immediate.

The involution here acts on the **whole 16-dimensional tensor product**, not necessarily as a tensor product of local involutions. Thus this class is not contained in the previously studied local-chiral class merely by this argument.

## 2. Symbolic irreducible, both-squares-nonnormal, nonchiral family

Choose arbitrary pairwise distinct `s,t,u>0` and arbitrary nonzero complex `z1,z2,z3`. Set

`Λ=diag(s,t,u,−s−t−u)`,

`T=I4+(z1e1+z2e2+z3e3)e4ᵀ`, `A=TΛT⁻¹`, `B=−A`.  (2.1)

These are free symbolic conditions, not numerical q or selected physical instances. Since the vector added to `e4` has zero fourth component, `T` is invertible and `A` is traceless. Its eigenvectors are `e1,e2,e3` and `v4=e4+z1e1+z2e2+z3e3`, with distinct real eigenvalues `s,t,u,−s−t−u`.

Every orthogonal projection commuting with `A` must assign each of these one-dimensional eigenspaces eigenvalue zero or one. Because each `⟨e_i,v4⟩=z_i` is nonzero, they cannot belong to opposite eigenspaces of a Hermitian projection. The nonorthogonality graph is connected, so only the zero and identity projections commute with `A`: it is unitarily irreducible. The same holds for `B=−A`.

The eigenvalues of `A²` are pairwise distinct (the positive `s,t,u` are distinct and `s+t+u` is larger than each), with the same nonorthogonal eigenvectors. A normal matrix's eigenvectors at distinct eigenvalues must be orthogonal, so `A²` and `B²` are nonnormal. The spectrum is not invariant under sign, so no local unitary can conjugate either factor to its negative; neither factor admits a local chiral involution. They are invertible and unitarily irreducible, hence not in the rank-one, normal/square-normal, or separately 2+2-reducing structural classes. An invertible irreducible weighted partial permutation would be a single weighted 4-cycle, whose eigenvalues cannot all be real, whereas all four eigenvalues here are real; thus neither factor is in that weighted class.

According to Section 1 these symbolic pairs satisfy `||X||_op²<L` and strict T2. This is a structural separation from the named earlier classes and from local chiral symmetry, **not** proof that any such pair lies outside f274's optimized `η≤2L` region or outside every other sufficient test.

## 3. Exact open comparison

The global-swap argument yields no local product basis in which the f274 modulus compound necessarily fails. It leaves open, for the whole swap class and family (2.1), whether `η≤2L` always holds or whether some member has `η>2L` after minimizing over **all** local unitaries. A one-basis comparison cannot answer that question. This packet does not establish unrestricted T2/T3/Z2/q3, a physical counterexample, source correctness, executable/Lean/human/independent-family validation, or novelty. The named source and this corollary require disjoint written review; prior frozen scopes and all process/STOP/HOLD/ZERO restrictions remain unchanged.
