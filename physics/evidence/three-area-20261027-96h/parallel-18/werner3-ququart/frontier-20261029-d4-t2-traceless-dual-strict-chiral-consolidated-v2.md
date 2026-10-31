# A traceless rank-two dual bound and strict T2 for the full nonnormal chiral class

**Status: WRITTEN, one self-contained owner candidate, UNREVIEWED.** This successor consolidates the previously pinned traceless-dual/chiral theorem, chiral operator-norm strengthening, mixed-minor strictness proof and equality-boundary corollaries. It does not edit or retroactively change any prior packet or already frozen review. No numerical/physical-q instance, scientific program, false f198 lemma, held/ZERO material, external source or novelty claim is used. Elementary inputs are finite-dimensional singular-value and unitary Schur decompositions, Frobenius duality, local swaps and Cayley–Hamilton; their needed applications are written out below.

## 1. Theorems and exact boundaries

Let `A,B∈M4(C)` be traceless, `X=A⊗I4+I4⊗B`, `L=||A||_F²+||B||_F²`, and `S2=σ1(X)²+σ2(X)²`. For any bipartite operator `R`, set

`Φ(R)=((Tr_B R)_0,(Tr_A R)_0)`, `G_0=G−(Tr G/4)I4`.

**A. Traceless rank-two dual.** For every `rank R≤2` with `Tr R=0`,

`||Φ(R)||_F²≤2||R||_F²`.  (1.1)

Therefore, for arbitrary original `A,B`, if **some** maximizing rank-two right-singular projector `P` of `X` has `Tr(XP)=0`, then `S2≤2L`.

**B. Orthogonal top singular pair.** If a top singular pair `Xv=σ1 u`, `||u||=||v||=1`, has `u⊥v`, then

`σ1²≤L` and `S2≤2L`.  (1.2)

For `X≠0`, equality `σ1²=L` forces **both** factors to be supported on local reducing subspaces of dimension at most two. Thus both local squares are normal; moreover, each factor is unitarily similar to a single weighted 2-cycle plus zero fixed points. In particular, if **either** local square is nonnormal, or either factor is not unitarily similar to a weighted partial permutation, then `σ1²<L` and `S2<2L`.

**C. The entire chiral physical class.** If local Hermitian unitary involutions obey `Z_A A Z_A=−A` and `Z_B B Z_B=−B`, the hypothesis of B holds. This includes **every** pair

`A=[[0,E],[F,0]]`, `B=[[0,G],[H,0]]`, `E,F,G,H∈M2(C)`,  (1.3)

with no rank, irreducibility, normality, magnitude, genericity or 2+2-**reducing** restriction. Every such pair with at least one nonnormal local square satisfies **strict** `σ1²<L` and strict T2. Section 7 supplies a symbolic family in (1.3) with both factors unitarily irreducible and both squares nonnormal.

These are written physical-class conclusions, not unrestricted T2, T3, Z2 or original q3. They do **not** establish that any member lies outside the entire f274 optimized `η≤2L` region or that a fixed-basis certificate failure is a physical counterexample. The exact unhandled route for A is that every maximizing top-two `P` has `Tr(XP)≠0`; failure of this route is not a counterexample. Novelty, source correctness and stronger-family/human/formal assurance are not claimed.

## 2. A rank-one swap identity

For `u,v∈C4⊗C4`, put `r=|u⟩⟨v|`. Let `F_A,F_B` swap the two copies of the A and B factors and `P_-^A=(I−F_A)/2`, `P_-^B=(I−F_B)/2`. Direct expansion gives

`||u||²||v||²+|⟨v,u⟩|²−||Tr_A r||_F²−||Tr_B r||_F²`

`=4 ⟨u⊗v,(P_-^A⊗P_-^B)(u⊗v)⟩ ≥0`.  (2.1)

The final operator is an orthogonal projector. If `Tr r=⟨v,u⟩=0`, each partial trace is itself traceless, and (2.1) gives

`||Φ(r)||_F≤||r||_F=||u||·||v||`.  (2.2)

This requires neither vector to be a product vector.

## 3. Traceless rank-two decomposition preserving nuclear norm

Let `rank R≤2` and `Tr R=0`. Rank one follows directly from (2.2). For rank two write the thin SVD

`R=UΣV†`, `Σ=diag(s1,s2)>0`, `U†U=V†V=I2`.

The 2×2 matrix `M=Σ^(1/2)V†UΣ^(1/2)` has trace zero. A 2×2 unitary `W` can make the diagonal of `W†MW` zero. To see this without an additional import, unitary-Schur `M` to `[[λ,z],[0,−λ]]`; the expectation on `(cosθ,e^{iφ}sinθ)` is `λ cos(2θ)+(z e^{iφ}/2)sin(2θ)`. Choose `φ` opposite the phase of `λ` and `θ∈[0,π/4]` so the two magnitudes agree. The cases `λ=0` or `z=0` are immediate. Complete the chosen vector orthogonally; the other diagonal expectation is also zero because the trace is zero.

Let `w1,w2` be the columns of `W`, define `a_i=UΣ^(1/2)w_i`, `b_i=VΣ^(1/2)w_i` and `R_i=|a_i⟩⟨b_i|`. Then

`R=R1+R2`, `Tr R_i=⟨b_i,a_i⟩=w_i†Mw_i=0`,

`||R_i||_F=||a_i||·||b_i||=w_i†Σw_i`, `Σ_i ||R_i||_F=TrΣ=||R||_1`.

By (2.2) and Frobenius triangle/Cauchy inequalities,

`||Φ(R)||_F≤||R||_1≤√2||R||_F`,

which proves (1.1). The rank-one summands need not be mutually orthogonal.

## 4. Physical consequences and chiral symmetry

If `P` is any maximizing top-two right-singular projector and `Tr(XP)=0`, then `R=XP` has rank at most two, trace zero and `||R||_F²=S2`. Since `A,B` are traceless,

`S2=Tr(R†X)=⟨(Tr_B R)_0,A⟩_F+⟨(Tr_A R)_0,B⟩_F≤√(2S2 L)`.

For `S2>0` this gives `S2≤2L`; zero is trivial.

If a top singular pair has `u⊥v`, the rank-one `r=|u⟩⟨v|` is traceless and has unit Frobenius norm. Thus

`σ1=|Tr(r†X)|≤||Φ(r)||_F√L≤√L`,

proving the stronger operator bound (1.2).

For the local chiral hypothesis set `Γ=Z_A⊗Z_B`. Then `ΓXΓ=−X` and `[Γ,X†X]=0`. Choose a top right singular vector `v` that is also a `Γ` eigenvector; its left partner `u=Xv/σ1` has the opposite parity and is orthogonal to `v`. This works at arbitrary top-eigenvalue degeneracy and proves (1.2) on the whole chiral class. The same simultaneous diagonalization provides a top-two projector commuting with `Γ`, so the trace condition in A also holds.

## 5. Exact operator-bound equality and mixed minors

Let `σ=σ1>0` and choose any orthogonal top singular pair. Put `r=|u⟩⟨v|`, `C=Tr_B r`, `D=Tr_A r` and `p=||(P_-^A⊗P_-^B)(u⊗v)||²`. Both partial traces are traceless. Equation (2.1) gives `||C||_F²+||D||_F²=1−4p`, while `⟨(C,D),(A,B)⟩_F=σ`. Therefore the **exact nonnegative slack** is

`L−σ² = ||(A,B)−σ(C,D)||_F²+4σ²p`.  (5.1)

Equality forces `p=0`, `A=σC`, `B=σD`. We now prove this forces both factors to have at-most-2D local reducing support.

Schmidt-diagonalize `u` by local unitaries, with coefficient matrix `U=diag(s1,…,sh,0,…)`, `s_i>0`, and let `V` be the coefficient matrix of `v` in those bases. Here `h` is the Schmidt rank. Vanishing `p` gives for all distinct row indices `i,k` and column indices `j,l` the mixed-minor identity

`U_ij V_kl−U_il V_kj−U_kj V_il+U_kl V_ij=0`.  (5.2)

If `h≥3`, for any offdiagonal pair `(k,l)` choose an active diagonal index `i` distinct from both; (5.2) forces `V_kl=0`. The diagonal equations `s_i V_kk+s_k V_ii=0` on three active indices force all active diagonal entries zero, then force inactive diagonals zero. Thus `V=0`, impossible. Hence `h≤2`.

If `h=2`, the same offdiagonal argument forces every entry of `V` outside the identical active 2×2 coefficient block to vanish; the diagonal equations also vanish outside it. Hence `C=UV†` and `D=Uᵀ conjugate(V)` are supported on the corresponding local 2D subspaces.

If `h=1`, (5.2) forces `V` to be supported on the first row and column. Orthogonality `u⊥v` gives `V11=0`. Then `C=UV†` and `D=Uᵀ conjugate(V)` each have rank at most one, range in the first Schmidt direction, and initial vector perpendicular to that direction. Each is supported on the span of at most two local vectors. By (5.1) the same reducing-support statements hold for `A,B`.

Each supported local block is traceless, so its square is scalar by Cayley–Hamilton; the zero complement makes the full local square normal. Independently, a traceless 2×2 block may be unitarily hollowed by the elementary argument of Section 3, giving `[[0,p],[q,0]]` on its support and zeros elsewhere. This is a weighted partial permutation with a single possible 2-cycle. Thus all equality and strictness statements in B and C follow. `X=0` cannot meet a nonnormal-square or non-weighted-factor strictness hypothesis: taking local partial traces forces `A=B=0`.

## 6. Exact separation from the named old structural classes

For free symbolic `a,d>0`, `b∈C\{0}`, with `(a²−1)(ad−1)(d²−1)≠0`, let

`T=[[a,b],[0,d]]`, `A=[[0,I2],[T,0]]`, `B=A`.  (6.1)

The pair is chiral, invertible, and both squares are `diag(T,T)`, nonnormal because `b≠0`. To prove `A` unitarily irreducible, let an orthogonal reducing projector have block form `P=[[H,K],[K†,L]]`. Commutation with `A` gives

`L=H`, `HT=TH`, `KT=K†=TK`.

A non-scalar Hermitian `H` commuting with `T` would unitarily diagonalize `T`, contradicting nonnormality; hence `H=hI2`. From `K†=KT` and its adjoint, `K=T†KT`. Its component equations successively give `(1−a²)k11=0`, `(1−ad)k12=(1−ad)k21=0` once `k11=0`, and `(1−d²)k22=0` once those entries vanish. Thus `K=0`; projection forces `h=0` or `1`. Both factors are unitarily irreducible.

An invertible weighted partial permutation decomposes into weighted cycles. Irreducibility would require one 4-cycle, whose nonzero eigenvalues are related by multiplication by `i` and cannot all be real. But the characteristic polynomial in (6.1) is `(z²−a)(z²−d)`, with all-real roots. The example is therefore outside the named f215 weighted-partial-permutation, rank-one and square-normal classes, outside the f281 normal-factor class, and outside the earlier separately 2+2-reducing theorem. By C, its norm and T2 bounds are **strict**. No claim is made that it escapes f274's full optimized certificate or any other independently supported test.

## 7. Remaining work and review boundary

The arbitrary-pair cases in which no top-two maximizing projector has trace-zero `XP` remain open in this route. This consolidated candidate does not prove f274 `η>2L` anywhere, does not settle unrestricted T2/T3/Z2/q3, and makes no physical-counterexample, source, computational, Lean/kernel, independent-family/human review or novelty claim. Disjoint review should reconstruct the swap identity, 2×2 hollow nuclear decomposition, full mixed-minor equality argument, unitary irreducibility, and all stated applicability boundaries. All prior process/STOP/HOLD/ZERO and frozen-review restrictions remain binding.
