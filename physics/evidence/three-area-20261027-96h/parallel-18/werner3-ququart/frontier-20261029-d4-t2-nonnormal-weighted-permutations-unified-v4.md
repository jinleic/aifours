# T2 at d=4: weighted partial permutations, the sharp rank-one residual and square-normal factors

**PhysicsResearch96h-2 / physics-1. WRITTEN, source-independent all-variable candidate; UNREVIEWED.** This self-contained packet supersedes `frontier-20261029-d4-t2-nonnormal-unified-shifts-and-residual-v3.md` (SHA256 `4b99b02306a9a6cfe0770622debfa82ccbe6cb7143cf63a7bb25a62912685949`) as the single proposed review candidate for this nonnormal line; v3 and every independently frozen review remain unchanged.

The new theorem in §2 proves a stronger operator-norm inequality for **arbitrary zero-diagonal weighted partial permutations**, with independent local unitary similarities and even different matrix sizes. It includes the earlier cyclic-weighted-shift result, and covers genuinely nonnormal rank2/rank3/full-rank cases with both squares nonnormal. §3 gives exact equality in the cyclic subclass. The packet also carries the sharp rank-one-B residual, the square-normal class, and two spectral sufficient regions, in one place.

It does **not** establish general T2, original T3, global equality, a source/novelty claim, parent/reviewer adoption, formal/Lean/human/family proof or physical-operational acceptance. No source certificate, selected physical target value, held episode/consumer/guidance, or additional finite Hessian/descent variant is used. Historic process and f153/f62/f168/f196 boundaries are unchanged.

## 1. Original two-copy dual

For traceless complex A,B∈M_4(C), set `X=A⊗I_4+I_4⊗B`. The d4 two-copy obligation is

`σ_1(X)²+σ_2(X)² <= 2(||A||F²+||B||F²)`.                            (T2)

The f168-dispositioned reflection/Ky-Fan dual identifies this with the original two-copy rank≤2 partial-trace inequality; the three-copy target implies T2. We only prove stated subclasses of (T2).

## 2. A stronger theorem for arbitrary weighted partial permutations

A **zero-diagonal weighted partial permutation** is a complex matrix with zero diagonal and at most one nonzero entry in each row and each column. Such a matrix has a representation `A_{σ(p),p}=a_p` for a permutation σ, with unused weights zero; if σ(p)=p then a_p=0. The nonzero partial matching can always be completed to a permutation. B has an analogous representation with τ,b_q. These matrices are traceless. Independent unitary similarities of A and B preserve all claims below.

**Theorem 2.1.** Let A∈M_m(C), B∈M_n(C) be zero-diagonal weighted partial permutations, with arbitrary complex weights, not necessarily the same size or cycle structure. Then

`||A⊗I_n+I_m⊗B||op² <= m_A+m_B <= ||A||F²+||B||F²`,              (2.1)

where

`m_A=max_p (|a_p|²+|a_(σ^(−1)(p))|²)`,
`m_B=max_q (|b_q|²+|b_(τ^(−1)(q))|²)`.

If an index is fixed by its permutation, its weight is0 and its repeated occurrence contributes0. Therefore, for every such pair in d=4,

`2(||A||F²+||B||F²)−[σ_1(X)²+σ_2(X)²]`
` >= 2[(||A||F²−m_A)+(||B||F²−m_B)] >=0`.                         (2.2)

*Proof.* For arbitrary coefficients w_{pq}, the output component at (i,j) is

`(Xw)_(ij)=a_(σ^(−1)i) w_(σ^(−1)i,j) + b_(τ^(−1)j) w_(i,τ^(−1)j)`.

Cauchy–Schwarz applied to these two terms, then summed over outputs, gives

`||Xw||² <= Σ_(p,q) [|a_p|²+|a_(σ^(−1)p)|²+|b_q|²+|b_(τ^(−1)q)|²] |w_pq|²`.

For each p, the two a-indices are distinct unless p is fixed, in which case both corresponding weights vanish; the sum is ≤m_A≤||A||F². The same holds for b. Taking the supremum over w proves (2.1). Finally `σ_1²+σ_2²<=2||X||op²` proves (2.2). This is a direct all-variable proof, not an average, search, source-certificate premise or numerical target evaluation. ∎

The class includes independently unitary-conjugated weighted paths and cycles of unequal lengths, including paths/cycles with zero weights. It strictly extends the common-cycle proof in v3. A,B with both squares nonnormal occur, including factors arbitrarily close to rank1 for which the tail-energy and variance criteria in §7 can fail. If either `m_A<||A||F²` or `m_B<||B||F²`, (2.2) gives a **strict positive dual gap**. No complete equality classification is asserted for arbitrary partial permutations.

## 3. Exact equality for common cyclic weighted shifts

For d≥3 let `S(a)=Σ_(i mod d)a_i|i−1><i|` and likewise S(b), up to independent local unitary similarities. This subclass of Theorem 2.1 admits a complete equality criterion:

**Theorem 3.1.** Equality in `σ_1²+σ_2²<=2(||S(a)||F²+||S(b)||F²)` holds iff each shift has at most one nonzero weight, including the zero matrix. For any nonzero pair where either shift has at least two nonzero weights, the T2 dual gap is strict.

*Proof.* Grade |i,j> by `k=i+j (mod d)`. X maps each H_k to H_(k−1), and the input and output grade decompositions are orthogonal. In the natural bases the grade-k block has entry a_i at `(row i−1,column i)` and b_(k−i) at `(row i,column i)`. Every weight appears once in each block, in distinct entries, so `||X_k||F²=||S(a)||F²+||S(b)||F²`.

Each column and row has at most two allowed positions, and for d≥3 two distinct columns share at most one possible row; the support graph contains no four-cycle. Any rank-one matrix on this graph has its nonzero entries in a single row or single column: otherwise a pair of entries in distinct rows and columns makes a nonzero 2×2 minor, because a complete rectangle of four allowed positions does not exist. Hence at least three nonzero weights, or two from the same shift, force every grade block to have rank≥2 and therefore operator norm squared strictly smaller than its Frobenius squared. This makes the T2 bound strict.

With exactly one nonzero a_i and one nonzero b_j, the two entries share a column in grade `i+j` and share a row in grade `i+j−1`; these are distinct grades. Both grade blocks are rank1 with their one squared singular value equal to `|a_i|²+|b_j|²`, so the top two singular values attain (2.2). With one nonzero weight total, all d grade blocks have the same one squared singular value, again giving equality; with no weights, both sides are zero. ∎

## 4. Full sharp trace-zero residual and rank-one B

**Lemma 4.1.** For traceless A∈M_4(C) and u,v∈C⁴ with `||u||²=t`, `||v||²=q=1−t`, write `d_A=||A||F²−||Au||²−||Av||²>=0`. Then

`|<v,Au>|² <= t(1+2q)d_A <= (t+1/2)d_A`.                           (4.1)

*Proof.* Put `D=I−uu†−vv†`, which is PSD, and first take u,v independent so D>0. Let `z=<u,v>`, `r=|z|²`, `Δ=tq−r>0`. In the weighted Hilbert–Schmidt inner product `<M,N>_D=Tr(M†ND)`, the functional `A↦<v,Au>` has representer `v u†D^(−1)` and Tr A has representer D^(−1). Projecting the first onto the trace-zero subspace gives

`|<v,Au>|² <= N·Tr(A†AD)`,
`N=q·u†D^(−1)u−|v†D^(−1)u|²/Tr D^(−1)`.

Inverting the 2×2 Gram matrix of u,v gives

`u†D^(−1)u=(t²+r)/Δ`, `|v†D^(−1)u|²=r/Δ²`, `Tr D^(−1)=2+1/Δ`.

Thus `(1+t)−N=[1+2tq−4r]/[1+2Δ]=[1−2tq+4Δ]/[1+2Δ]>=1−2tq`, hence N≤t+2tq. The algebraic identity was also checked in-kernel via exact `fractions.Fraction` polynomial dictionaries after clearing denominators; that check covers only this identity. Collinear vectors follow by continuity and zero vectors trivially. ∎

For `σ=||A||op`, (4.1) proves the formerly unpaid frozen (†), with explicit remainder

`2||A||F²−[||Au||²+||Av||²+|<v,Au>|²/(1+t)+σ²]`
` >= (||A||F²−σ²)+[(1−2tq)/(1+t)]d_A >=0`.                       (4.2)

**Rank-one B.** A nonzero traceless rank1 B is locally unitarily similar to bE_01, b>0. Then X is the orthogonal direct sum `Γ_b⊕A⊕A`, with `Γ_b=[[A,bI],[0,A]]`. Two top singular vectors in Γ_b have a 2D leg at site2, so Lemma 6.1 applies; two from the A blocks cost at most `2||A||op²`. For a mixed pair, (4.1) and completing the square yield, for all unit `(u,v)`,

`2(||A||F²+b²)−[||Γ_b(u,v)||²+||A||op²]`
` >= (||A||F²−||A||op²)+[(1−2tq)/(1+t)]d_A+(1+t)|b−<v,Au>/(1+t)|² >=0`.

So (T2) holds for every traceless A whenever rank B≤1. This pays the entire rank-one-B residual, not general T2.

## 5. The 4×2 norm bound

For traceless `A∈M_4(C)`, `T∈M_2(C)`,

`||A⊗I_2+I_4⊗T||op²<=||A||F²+2||T||F²`.                           (5.1)

*Proof.* For unit ψ,φ∈C⁴⊗C² let `c=<φ,ψ>`, `M=Tr_2|ψ><φ|`, `N=Tr_1|ψ><φ|`, and `M_0=M−cI_4/4`, `N_0=N−cI_2/2`. Tracelessness and weighted Hilbert–Schmidt Cauchy–Schwarz give

`|<φ,(A⊗I_2+I_4⊗T)ψ>|² <= (||A||F²+2||T||F²)(||M_0||F²+||N_0||F²/2)`.

Set `s_1=||N||²`, `s_2=||M||²`. These are overlaps of one-site density reductions, so both are ≤1. The PSD operator `(I−F_1)(I−F_2)` on ψ⊗φ gives `1−s_1−s_2+|c|²>=0`. Consequently `||M_0||²+||N_0||²/2=s_2/2+(s_1+s_2−|c|²)/2<=1`. Supremize over ψ,φ. ∎

## 6. One-supported-site lemma and square-normal factors

**Lemma 6.1.** For traceless A,B and `X=A⊗I+I⊗B`, if F⊂C⁴⊗C⁴ has dimension2 and its leg at **some site** is contained in a 2D local subspace, then `||XP_F||F²<=||X||F²/2`.

*Proof.* This is the one-supported-site case of the qualified f168 ladder/dual disposition; for completeness, take `F⊂C⁴⊗E`, dim E=2, and C=XP_F. Then rank C≤2 and its site-2 input leg lies in E. The corresponding compressed local factor `K=I−|Ω><Ω|/2` has the positive product decomposition

`I⊗bar P_E−|Ω_E><Ω_E|/2 = 3∫ |u_perp><u_perp|⊗|bar u><bar u|dμ(u)+(I−P_E)⊗bar P_E`,

whose finite term is a sum of positive rank-one products. This follows from the elementary Haar second moment and partial transpose. Each product contraction leaves a one-site matrix Z of rank≤2, with `q1(Z)=||Z||²−|TrZ|²/2>=0`; hence q2(C)≥0. The d4 trace-insertion product W is a self-adjoint reflection with WX=−X, so `q2(C)=||C||²−2||P_-C||²` and `<X,C>=||C||²`. Cauchy–Schwarz yields `||P_-C||²>=||C||⁴/||X||²`, proving (5.1). Exchange sites and adjoints as needed. ∎

**Theorem 6.2.** (T2) holds if A² or B² is normal.

*Proof.* A traceless B∈M_4 has normal B² iff B is normal or unitarily a direct sum of two separately traceless 2×2 blocks. For the reverse direction, use the spectral theorem or 2×2 Cayley–Hamilton. For the forward direction, B commutes with normal B², so its spectral subspaces reduce B. On the zero eigenspace an SVD gives nilpotent 2×2 blocks plus zero scalars. On a λ≠0 eigenspace, B has eigenvalues ±μ, μ²=λ, and in the orthogonal decomposition `ker(B−μI)⊕ker(B−μI)⊥` has form `[[μI,C],[0,−μI]]`; SVD of C gives traceless 2×2 blocks plus scalar leftovers. If a nonnormal 2×2 block occurs, the remaining scalar entries in total dimension4 are either none or two summing to zero, so they form the other traceless 2×2 block; otherwise B is normal.

For B normal, diagonalize it: a top-two right singular subspace uses at most two 1D site-2 blocks, and Lemma 6.1 applies. For `B=B_1⊕B_2` with `Tr B_j=0`, X is the direct sum of `Γ_j=A⊗I_2+I_4⊗B_j`. Two top singular vectors in one Γ_j are safe by Lemma 6.1; one from each is bounded by (5.1), giving `σ_1(Γ_1)²+σ_1(Γ_2)²<=2(||A||F²+||B||F²)`. Exchange A,B for the other case. ∎

## 7. Two additional all-variable sufficient tests

For x=||A||op, y=||B||op, `s_A=||A||F²−x²`, `s_B=||B||F²−y²`, the Ky-Fan-two ℓ² norm satisfies `sqrt(σ_1²+σ_2²)<=sqrt2(x+y)`. Hence (T2) holds whenever `s_A+s_B>=2xy`, with strict gap if >.

For `a=||A||F²`, `b=||B||F²`, `p=Tr[(A†A)²]`, `q=Tr[(B†B)²]`, `z=Re(conjugate(Tr A²)Tr B²)`, exact expansion gives `Tr(X†X)=4(a+b)` and `Tr[(X†X)²]=4(p+q)+4ab+2z`. Mean-zero Cauchy–Schwarz on the 16 eigenvalues of X†X yields T2 whenever

`14(p+q)+7z <= 8(a²+b²)+2ab`,                                        (7.1)

strictly for nonzero X if <. Neither test is exhaustive.

## 8. Exact unpaid remainder and provenance

General traceless A,B outside the weighted-partial-permutation, square-normal and spectral sufficient classes remain unpaid; the full original T2 and T3 and global equality classification are not established. All proofs here use original trace/Schmidt duality, finite-dimensional Cauchy–Schwarz, SVD, the spectral theorem, one elementary Haar second moment and the qualified one-supported-site f168 lemma. No source certificate, f196 review return, selected target q value, held episode/consumer/guidance or additional finite Hessian/descent variant is used. No priority or novelty is claimed; the known public full-target Werner claim is not assessed here.
