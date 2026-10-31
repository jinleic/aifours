# Source-independent two-copy T2: cyclic weighted shifts, the sharp rank-one residual, and square-normal matrices

**PhysicsResearch96h-2 / physics-1. WRITTEN all-variable candidate; UNREVIEWED.** This is one self-contained successor candidate for the nonnormal line. It retains unchanged the earlier packet `frontier-20261029-d4-t2-nonnormal-sharp-residual-consolidated-v2.md`, SHA256 `193bad400026692c4d806f3b4c64bd234e05b087e94d43aa32bc42346404fad8`. The independently frozen f196 review of the prior T2 v3 packet remains unchanged and is not consulted here.

The new result in §2 establishes the actual d4 T2 dual inequality — and exactly classifies equality within the class — when **both** factors are arbitrary independently unitary-conjugated cyclic weighted shifts. This covers matrices with both squares nonnormal and, in particular, arbitrarily nearly rank-one factors that need not satisfy the earlier tail-energy or variance sufficient conditions. §§3–6 retain the independently derived solution of the former rank-one-B sharp residual and the square-normal class. §7 records two elementary additional sufficient tests.

This packet does **not** prove T2 for arbitrary traceless A,B, the original three-copy T3 target, or global equality. It does not assert any literature status, novelty, parent/reviewer acceptance, human/family/formal/Lean proof or physical-operational result. It invokes no source certificate, selected physical target value, held episode/consumer/guidance, or finite Hessian/descent variant as a premise. Prior process findings and the distinct-site f168 qualification remain unchanged.

## 1. Target and notation

For traceless complex `A,B∈M_4(C)` write `X=A⊗I_4+I_4⊗B`. The d4 two-copy dual obligation is

`σ_1(X)²+σ_2(X)² <= 2(||A||F²+||B||F²)`.                           (T2)

The reflection/Schmidt-rank duality in the f168-dispositioned stratified packet identifies this with nonnegativity of the original two-copy rank≤2 partial-trace quadratic form. The original three-copy target implies T2. This paper uses only the algebraic dual statement and does not promote its general truth.

## 2. Two arbitrary cyclic weighted shifts: exact norm and equality theorem

For any d≥3, index a fixed orthonormal basis by `Z/dZ` and write

`S(a)=Σ_(i mod d) a_i |i−1><i|`, `S(b)=Σ_(j mod d) b_j |j−1><j|`,

for arbitrary complex weights. These matrices are traceless and may be singular, invertible, nonnormal, or have nonnormal squares. Local unitary conjugations and independent relabelings are allowed.

**Theorem 2.1.** For every d≥3 and every weights a,b,

`||S(a)⊗I_d+I_d⊗S(b)||op² <= ||S(a)||F²+||S(b)||F²`,               (2.1)

and consequently

`σ_1²+σ_2² <= 2(||S(a)||F²+||S(b)||F²)`.                              (2.2)

Equality in (2.2) holds **if and only if each shift has at most one nonzero weight**, including the zero matrix. In particular, if either factor has at least two nonzero weights, the inequality is strict for nonzero X. At d=4, (2.2) is exactly (T2) for this all-variable subclass; no higher-dimensional q2/T3 consequence is asserted.

*Proof of (2.1).* Grade each basis vector `|i,j>` by `k=i+j (mod d)`, and let H_k be its grade subspace. Each summand in X lowers the grade by1, so `X H_k⊂H_(k−1)`. Distinct H_k and their images are orthogonal; therefore `||X||op=max_k||X_k||op`, where `X_k:H_k→H_(k−1)` is the restricted block.

In the grade-k input basis `|i,k−i>` and grade-(k−1) output basis `|ℓ,k−1−ℓ>`, X_k has exactly these possible entries:

- `a_i` at row i−1, column i;
- `b_(k−i)` at row i, column i.

For d≥3 these two entry positions are distinct. Every a_i and every b_j occurs **once** in each grade block, so

`||X_k||F²=Σ_i|a_i|²+Σ_j|b_j|²=||S(a)||F²+||S(b)||F²`.

Thus `||X_k||op²<=||X_k||F²` and (2.1) follows. Applying `σ_1²+σ_2²<=2||X||op²` gives (2.2).

*Equality in (2.2).* Each grade block has nonzero entries only at positions `(row i,column i)` and `(row i−1,column i)`. For d≥3, two distinct columns share at most one possible row, so this bipartite entry graph has **no four-cycle**. Consequently any rank-one matrix supported on this graph has all nonzero entries in one row or in one column: otherwise two nonzero entries on distinct rows and columns give a nonzero 2×2 minor, since a four-edge rectangle cannot occur. Each row and column has at most two possible entries.

If there are at least three nonzero weights altogether, every grade block has at least three nonzero entries and therefore rank≥2; if exactly two weights lie in the **same** shift, they occur on distinct rows and columns and again every block has rank≥2. In either situation `||X_k||op²<||X_k||F²` for every k, so (2.2) is strict.

If each shift has exactly one nonzero weight, say a_i and b_j, then two distinct grade blocks are rank1: grade `k=i+j` makes the entries share a column, and grade `k=i+j−1` makes them share a row. Each has its single squared singular value `|a_i|²+|b_j|²`. Thus X has at least two singular values attaining the norm bound, and (2.2) is equality. If just one weight is nonzero, every grade block has rank1 and equality again holds; if all vanish, both sides are zero. This proves the iff. ∎

**Non-normal residual coverage.** At d=4, choosing a_i,b_j with all weights nonzero and generic magnitudes yields nonnormal A² and B²: a nonzero normal matrix cannot be nilpotent, and the squares of nilpotent path shifts are nonzero nilpotent; cyclic weighted shifts also have generically nonnormal squares. One may take the nonleading weights arbitrarily small while keeping adjacent weights nonzero. Such pairs approach rank-one shifts, and can lie outside both the tail-energy and fourth-moment tests of §7. This is a symbolic family, not a selected numerical q2 value. Strictness follows from Theorem 2.1 whenever either factor has at least two nonzero weights.

## 3. The full rank-one-B residual, with a sharp trace-zero bound

**Lemma 3.1.** For any traceless A∈M_4(C) and any u,v∈C⁴ with `||u||²=t`, `||v||²=q=1−t`, define `d_A=||A||F²−||Au||²−||Av||²>=0`. Then

`|<v,Au>|² <= t(1+2q)d_A <= (t+1/2)d_A`.                             (3.1)

*Proof.* Let `D=I−uu†−vv†` and `U=[u v]`. D is PSD because the subtracted PSD matrix has trace1. If u,v are independent it is positive definite. Put `z=<u,v>`, `r=|z|²`, `Δ=tq−r>0` and equip M_4 with `<M,N>_D=Tr(M†ND)`. The Riesz representer of `A↦<v,Au>` is `v u†D^(−1)`, and that of `Tr A` is D^(−1). Projection onto the trace-zero subspace gives

`|<v,Au>|² <= N Tr(A†AD)`,
`N=q·u†D^(−1)u − |v†D^(−1)u|²/Tr(D^(−1))`.

The 2×2 Gram inverse for `U†U=[[t,z],[bar z,q]]` gives `u†D^(−1)u=(t²+r)/Δ`, `|v†D^(−1)u|²=r/Δ²` and `Tr D^(−1)=2+1/Δ`. Hence

`(1+t)−N = [1+2tq−4r]/[1+2Δ] = [1−2tq+4Δ]/[1+2Δ] >= 1−2tq`.

Thus `N<=t+2tq`. Since tq≤1/4, this is ≤t+1/2. The rational identity was additionally checked in-kernel by exact `fractions.Fraction` polynomial dictionaries after clearing denominators; only that algebra was machine-checked. Dependent u,v follow by continuity, and either zero vector is immediate. ∎

**Corollary 3.2.** For traceless A, σ=||A||op and arbitrary normalized u,v,

`2||A||F² − [||Au||²+||Av||²+|<v,Au>|²/(1+t)+σ²]`
` >= (||A||F²−σ²) + [(1−2tq)/(1+t)]d_A >=0`.                     (3.2)

This is precisely the unpaid (†) in frozen T2 v3, now with a universal gap. For nonzero A, equality forces rank A=1 and u,v collinear with its top right singular vector; A=0 is trivial.

**Theorem 3.3.** (T2) holds for every traceless A whenever traceless B has rank≤1.

*Proof.* B=0 is immediate; otherwise local unitary conjugation gives `B=bE_01`, b>0. X is `Γ_b⊕A⊕A` with `Γ_b=[[A,bI],[0,A]]`. If both top singular vectors lie in Γ_b, their site-2 leg has dimension2, so Lemma 5.1 below applies; if both lie in the complementary A blocks, their squared sum is at most `2||A||op²`. If one lies in each, for any unit `(u,v)` the completion-of-square identity and (3.1) give

`2(||A||F²+b²)−[||Γ_b(u,v)||²+||A||op²]`
` >= (||A||F²−||A||op²)+[(1−2tq)/(1+t)]d_A`
`    +(1+t)|b−<v,Au>/(1+t)|² >=0`.

Maximize over u,v. The mixed-block bound is strict for b>0: vanishing of the first two remainders implies `<v,Au>=0` by (3.1), while the last would force b=0. No global equality or strict q2/T3 gap is claimed. ∎

## 4. The 4×2 block operator-norm estimate

**Lemma 4.1.** For any traceless A∈M_4(C), T∈M_2(C),

`||A⊗I_2+I_4⊗T||op² <= ||A||F²+2||T||F²`.                          (4.1)

*Proof.* For unit ψ,φ∈C⁴⊗C², let `c=<φ,ψ>`, `M=Tr_2|ψ><φ|`, `N=Tr_1|ψ><φ|` and subtract traces: `M_0=M−cI_4/4`, `N_0=N−cI_2/2`. Weighted Hilbert–Schmidt Cauchy–Schwarz gives

`|<φ,(A⊗I_2+I_4⊗T)ψ>|² <= (||A||F²+2||T||F²)(||M_0||F²+||N_0||F²/2)`.

Put `s_1=||N||F²`, `s_2=||M||F²`. Each is an overlap of two one-site density reductions, so lies in [0,1]. The PSD product `(I−F_1)(I−F_2)` on ψ⊗φ gives `1−s_1−s_2+|c|²>=0`. Hence

`||M_0||F²+||N_0||F²/2=s_2/2+(s_1+s_2−|c|²)/2<=1`.

Supremize over unit ψ,φ. ∎

## 5. Safe subspaces at one site

**Lemma 5.1.** If F⊂C⁴⊗C⁴ is two-dimensional and its leg at some **site** is contained in a 2D local subspace, then for traceless A,B and `X=A⊗I+I⊗B`,

`||XP_F||F²<=||X||F²/2`.                                             (5.1)

*Proof.* This is the one-supported-site case of the qualified f168 ladder/dual disposition; the short proof is repeated. Take `F⊂C⁴⊗E`, dim E=2, and `C=XP_F`. Then rank C≤2 and its site-2 input leg lies in E. The input-E compression of the local `K=I−|Ω><Ω|/2` is the positive product decomposition

`I⊗bar P_E−|Ω_E><Ω_E|/2`
`=3∫_(u∈S(E)) |u_perp><u_perp|⊗|bar u><bar u| dμ(u)+(I−P_E)⊗bar P_E`.

The finite complement is also a sum of positive rank-one products. The identity follows from `∫|u><u|^tensor2=(P_E⊗P_E+F_E)/6` and a partial transpose. Every resulting contraction of C is a one-site matrix Z of rank≤2, and `||Z||²−|TrZ|²/2>=0`; hence q2(C)≥0.

At d=4 the original two-site trace-insertion operator W is a self-adjoint reflection, with WX=−X. Thus `q2(C)=||C||²−2||P_-C||²`, while `<X,C>=||C||²`. Cauchy–Schwarz and q2(C)≥0 give (5.1). Exchange sites and take adjoints for the other orientations. ∎

## 6. Square-normal factors, including nonnormal full-rank matrices

**Theorem 6.1.** (T2) holds whenever A or B is unitarily block diagonal with two reducing 2×2 blocks, each separately traceless.

*Proof.* Suppose `B=B_1⊕B_2`, `Tr B_j=0`. X is the orthogonal direct sum of `Γ_j=A⊗I_2+I_4⊗B_j`. If both top singular vectors lie in one block, their site-2 leg is 2D and Lemma 5.1 applies. If one comes from each, (4.1) gives their squared sum at most `2||A||F²+2(||B_1||F²+||B_2||F²)`. Ties permit choosing vectors from the block decomposition. Exchange A and B for the other orientation. ∎

**Lemma 6.2.** A traceless B∈M_4(C) has B² normal iff B is normal or is unitarily block diagonal with two separately traceless 2×2 blocks.

*Proof.* The reverse direction follows from the spectral theorem and, for a traceless 2×2 block, Cayley–Hamilton: `B_j²=−det(B_j)I_2`. Conversely, normal B² has orthogonal spectral subspaces, each reducing B because B commutes with B². On the zero-eigenspace, B²=0; SVD of the off-diagonal map gives nilpotent 2×2 blocks plus zero scalars. On a λ≠0 eigenspace choose μ²=λ. Since B's minimal polynomial there divides `(z−μ)(z+μ)`, B is diagonalizable. In `ker(B−μI)⊕ker(B−μI)⊥` it has form `[[μI_p,C],[0,−μI_q]]`. Independent unitaries SVD-diagonalize C, yielding traceless 2×2 blocks `[[μ,c_j],[0,−μ]]` plus scalar leftovers. If no nonnormal 2×2 block occurs, B is normal. If one occurs, the remaining two scalar entries sum to zero by Tr B=0 and form a traceless 2×2 block; two blocks exhaust dimension4. ∎

Normal B itself is handled by diagonalizing it: two top right singular vectors can be chosen from at most two 1D site-2 blocks, so Lemma 5.1 applies. Thus (T2) holds whenever **A² or B² is normal**. This does not assert the inequality for arbitrary A,B with both squares nonnormal.

## 7. Two further all-variable sufficient tests

These tests apply to arbitrary traceless A,B and do not depend on §2–6 or any source certificate. They cover some both-square-nonnormal pairs beyond the cyclic-shift family, but not all pairs.

**Tail-energy test.** Put `x=||A||op`, `y=||B||op`, `s_A=||A||F²−x²`, `s_B=||B||F²−y²`. The Ky-Fan-two ℓ² norm is `max_(rank P=2)||XP||F`, so the triangle inequality gives

`σ_1(X)²+σ_2(X)² <= 2(x+y)²`.

Therefore (T2) holds whenever `s_A+s_B>=2xy`, with strict gap if >. In particular, it holds if both `||A||F²>=2x²` and `||B||F²>=2y²`.

**Moment/variance test.** Put `a=||A||F²`, `b=||B||F²`, `p=Tr[(A†A)²]`, `q=Tr[(B†B)²]`, `z=Re(conjugate(Tr A²)Tr B²)`. Direct expansion gives

`T=Tr(X†X)=4(a+b)`, `M=Tr[(X†X)²]=4(p+q)+4ab+2z`.

For the 16 nonnegative eigenvalues h_j of X†X, mean-zero Cauchy–Schwarz with weights 7/8 on the top two and −1/8 on the remaining fourteen gives

`h_1+h_2 <= T/8 + sqrt[(7/4)(M−T²/16)]`.

It follows that (T2) holds whenever `M<=T²/7`, equivalently

`14(p+q)+7z <= 8(a²+b²)+2ab`,                                        (7.1)

with strict T2 gap for a nonzero X if the inequality is strict. Neither (7.1) nor the tail test is a full-domain proof.

## 8. Exact remainder

The original two-copy T2 remains unpaid here for arbitrary traceless A,B with both squares nonnormal, outside the cyclic-shift class and the sufficient spectral regions in §7. The original three-copy target and global equality classification likewise remain unpaid. No new priority or novelty is claimed for any written subclass; the public prior full-target claim remains unassessed for correctness here. No f196/f153/f62/f168 scope is changed, no source or held input is consumed, and no further finite Hessian/descent variant is counted as universal progress.
