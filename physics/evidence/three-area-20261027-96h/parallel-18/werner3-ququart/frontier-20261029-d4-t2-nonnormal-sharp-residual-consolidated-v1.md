# A sharp trace-zero inequality and new non-normal subclasses of the two-copy obligation

**PhysicsResearch96h-2 / physics-1. WRITTEN all-variable candidate; UNREVIEWED.** This is the single consolidated successor for the source-independent non-normal line requested after frozen f196. It proves the sharp inequality (†) and, consequently, the full rank-one-B subclass; a second direct argument proves a broader class in which either A or B has two **reducing**, traceless 2×2 blocks. It does **not** prove the general T2 or the original T3 target, or classify all equalities. It does not alter the frozen f196, f153, f62 or f168 scopes. No source certificate, executable search, selected physical target value, held episode or held guidance is used. No novelty, literature-status, parent/reviewer, human/family, formal/Lean or operational acceptance is asserted.

The prior frozen two-copy packet is `frontier-20261029-d4-t2-two-copy-obligation-packet-v3.md`, SHA256 `7c0df3e55f53eae89710381a8c1cbf3c5a58418e192d74997dd94181fec7acaf`, under disjoint f196 review. The present proof is independent of that review and includes its needed algebraic steps here.

## 1. Target, and the results proved in this packet

For traceless complex `A,B∈M_4(C)`, write

`X=A⊗I_4+I_4⊗B`, `S_2(X)=σ_1(X)²+σ_2(X)²`.

The unresolved two-copy obligation is

`S_2(X) <= 2(||A||F²+||B||F²)`.                                      (T2-dual)

The d=4 reflection/Ky-Fan dual relating this to the original rank≤2 q2 is recalled in §5; the original three-copy target implies T2. The present packet proves:

1. **Sharp residual paid.** If B has rank≤1, (T2-dual) holds for **every** traceless A. More precisely the all-variable inequality (†) below holds with a universal nonnegative remainder; there is no remaining nearly-rank-one-A subcase within rank-one B.
2. **Broader non-normal subclass.** (T2-dual) holds whenever either A or B is unitarily block diagonal with two reducing 2×2 blocks, **each separately traceless**. The other matrix may be any traceless 4×4 matrix, including a non-normal one. In particular, every square-zero matrix B is included: `B²=0` implies rank B≤2 and B is unitarily equivalent to `b_1E_01⊕b_2E_01` for b_j≥0.

The rank-one-B proof uses an explicit new trace-zero inequality (§2–3); the two-block proof has a separate elementary pure-pair argument (§4–6). Neither uses an unproved external inequality.

## 2. Uniform weighted trace-zero lemma

**Lemma 2.1.** Let A∈M_4(C) have `Tr A=0`. For any u,v∈C⁴ with `||u||²+||v||²=1`, set `t=||u||²` and

`d_A(u,v)=||A||F²−||Au||²−||Av||²`.

Then `d_A(u,v)>=0` and

`|<v,Au>|² <= (t+2/3) d_A(u,v)`.                                    (2.1)

*Proof.* Put `U=[u v]`, `D=I−uu†−vv†`. D is PSD because `uu†+vv†` is PSD of trace1. Also `d_A=Tr(A†A D)`. First suppose u,v are linearly independent. Let

`q=1−t`, `z=<u,v>`, `r=|z|²`, `Δ=tq−r>0`.

Because the two positive eigenvalues of `uu†+vv†` sum to1, both are strictly less than1, so D is positive definite. Equip M_4 with the weighted Hilbert–Schmidt inner product

`<M,N>_D=Tr(M†N D)`.

The linear functional `L(A)=<v,Au>` has weighted Riesz representer `Z=v u† D^(−1)`, while `Tr A` has representer `D^(−1)`. Projecting Z orthogonally onto the trace-zero subspace, exact Cauchy–Schwarz gives

`|L(A)|² <= N · Tr(A†A D)`,
`N=q·u†D^(−1)u − |v†D^(−1)u|²/Tr(D^(−1))`.                         (2.2)

These are identities in the weighted inner product; no positivity of A is assumed. The 2×2 Gram matrix `G=U†U=[[t,z],[bar z,q]]` has `det(I−G)=Δ`. The Woodbury identity yields

`u†D^(−1)u=(t²+r)/Δ`, `|v†D^(−1)u|²=r/Δ²`,
`Tr(D^(−1))=2+1/Δ`.

Therefore

`N=q(t²+r)/Δ − r/[Δ(1+2Δ)]`,
`(1+t)−N=[1+2tq−4r]/[1+2Δ]`.                                        (2.3)

The last equality is a polynomial identity in t,r. It was also checked independently in the eval kernel by exact `fractions.Fraction` polynomial-dictionary arithmetic: after clearing denominators every coefficient was zero. This checks only the displayed algebra, not the written theorem or any target value.

Cauchy–Schwarz gives `0≤r≤tq≤1/4` and `0<Δ≤1/4`. Thus the numerator in (2.3) is at least `1−2tq>=1/2` and the denominator at most `3/2`. Hence `(1+t)−N>=1/3`, i.e. `N<=t+2/3`, proving (2.1) when u,v are independent.

For dependent u,v with both nonzero, approximate v by vectors of the same norm not collinear with u; both sides of (2.1) are continuous, so the inequality passes to the limit. If u=0 or v=0, the left side is zero and D remains PSD. ∎

**Corollary 2.2 (the previously unpaid (†), with a gap).** For traceless A, `σ=||A||op` and all u,v as above,

`2||A||F² − [||Au||²+||Av||²+|<v,Au>|²/(1+t)+σ²]`
`  >= (||A||F²−σ²) + d_A(u,v)/[3(1+t)] >= 0`.                    (2.4)

In particular the entire nearly-rank-one regime of the frozen (†) is paid, not merely a local expansion. Equality in (2.4) requires `rank A≤1` and `d_A=0`; for nonzero A this forces u and v to be collinear with a top right singular vector of A, because `uu†+vv†` has trace1. Traceless rank-one A has its corresponding left singular vector orthogonal to that right singular vector. No global q2 or q3 conclusion follows from the lemma alone.

## 3. All rank-one B, including the previously residual cross case

Let B be nonzero, traceless and rank1. Unitary conjugation at its local site brings it to `bE_01`, b>0. X is the orthogonal direct sum

`Γ_b=[[A,bI_4],[0,A]]` on `C⁴⊗span{e0,e1}`, and two copies of A on the complementary site-2 directions.

For any unit `(u,v)∈C⁴⊕C⁴`, put `t=||u||²`, `L=<v,Au>`, `σ=||A||op`, and `d_A` as above. Direct completion of the square, followed by (2.1), gives the exact quantitative bound

`2(||A||F²+b²) − [||Γ_b(u,v)||²+σ²]`
` >= (||A||F²−σ²) + d_A(u,v)/[3(1+t)]`
`    +(1+t)|b−L/(1+t)|² >=0`.                                       (3.1)

Indeed `||Γ_b(u,v)||²=||Au||²+||Av||²+b²(1−t)+2 Re(bar b L)`, so (3.1) is just completion of the square and (2.1).

If the two largest singular values of X both come from the Γ_b block, their right singular subspace has a 2D leg at site 2 and Lemma 5.1 applies. If both come from the complementary A blocks, their squared sum is at most `2σ²<=2||A||F²`. If one comes from each, maximize (3.1) over unit `(u,v)` and use `σ²` for the other block. Thus (T2-dual) holds in all cases. B=0 follows directly as well.

The cross-case inequality is actually strict for b>0: equality in (3.1) would require `||A||F²=σ²` and `d_A=0`, which by Corollary 2.2 imply `L=0`; the last square then forces b=0. This strictness is only for the mixed-block pair, not a global strictly positive q2/q3 gap or a complete equality classification.

## 4. An independent operator-norm lemma for 4×2 blocks

**Lemma 4.1.** For every traceless `A∈M_4(C)` and every traceless `B∈M_2(C)`,

`||A⊗I_2+I_4⊗B||op² <= ||A||F²+2||B||F²`.                          (4.1)

No normality or rank condition is imposed.

*Proof.* Let ψ,φ be arbitrary unit vectors in C⁴⊗C², `c=<φ,ψ>`, and define

`M=Tr_2 |ψ><φ| ∈ M_4`, `N=Tr_1 |ψ><φ| ∈ M_2`.

Both traces equal c. Put `M_0=M−(c/4)I_4`, `N_0=N−(c/2)I_2`. Since A,B are traceless,

`<φ,(A⊗I_2+I_4⊗B)ψ>=Tr(A M_0)+Tr(B N_0)`.

Weighted Hilbert–Schmidt Cauchy–Schwarz yields

`|<φ,Γψ>|² <= (||A||F²+2||B||F²)(||M_0||F²+||N_0||F²/2)`.       (4.2)

Let `s_1=||N||F²`, `s_2=||M||F²`. By the swap trick, these are the Hilbert–Schmidt overlaps of the corresponding normalized one-site reductions of ψ and φ, so `0<=s_1,s_2<=1`. The commuting PSD operator `(I−F_1)(I−F_2)` on two copies gives

`1−s_1−s_2+|c|² >=0`.                                                (4.3)

Consequently

`||M_0||F²+||N_0||F²/2 = s_2+s_1/2−|c|²/2`
` = s_2/2 + (s_1+s_2−|c|²)/2 <=1`.

Apply (4.2) and take the supremum over ψ,φ. ∎

For clarity, (4.3) follows directly by taking the expectation of `(I−F_1)(I−F_2)` in ψ⊗φ: the full swap term is `|<φ,ψ>|²`, and the single swaps are the two marginal overlaps. This is ordinary finite-dimensional swap algebra, not an appeal to an unverified external source.

## 5. Safe subspaces at a distinct site

**Lemma 5.1.** If F⊂C⁴⊗C⁴ is two-dimensional and its leg at **some site** lies in a 2D local subspace, then for every `X=A⊗I+I⊗B` with A,B traceless,

`||X P_F||F² <= ||X||F²/2`.                                           (5.1)

*Proof.* This is the one-supported-site case of the qualified f168 ladder/dual disposition; the short argument is included for independence. Assume the leg is an input leg at site2, E⊂C⁴ with dim E=2, and set `C=XP_F`. Then `rank C≤2` and `C(I⊗P_E)=C`.

Under `vec C`, the local site-2 quadratic factor is `K=I−|Ω><Ω|/2`. Its input-E compression is the positive product decomposition

`I⊗bar P_E−|Ω_E><Ω_E|/2`
` = 3∫_(u∈S(E)) |u_perp><u_perp|⊗|bar u><bar u| dμ(u)`
`   +(I−P_E)⊗bar P_E`.                                                (5.2)

Here u_perp is any unit vector in E orthogonal to u; the finite complement term is a sum of positive rank-one product operators. Formula (5.2) follows from `∫|u><u|^tensor2=(P_E⊗P_E+F_E)/6` and partial transpose on the second factor. Contracting C against any of these local product factors leaves a one-site matrix Z of rank≤2, so `q_1(Z)=||Z||F²−|Tr Z|²/2>=0`. Thus the integral and finite sum give `q_2(C)>=0`.

For d=4, the original two-site quadratic form is a reflection: if `D_i(Y)=I_i⊗Tr_iY`, then `(Id−D_i/2)²=Id`. The product W is self-adjoint, and `WX=−X` because A,B are traceless. Hence `q_2(C)=||C||²−2||P_- C||²`, where P_-=(Id−W)/2. Since `<X,C>=||XP_F||²=||C||²`, Cauchy–Schwarz gives `||P_- C||²>=||C||⁴/||X||²`. The already proved `q_2(C)>=0` implies (5.1). The other physical site and the left-subspace version are obtained by site exchange and adjoints. ∎

The support in Lemma 5.1 is at **one site**; no claim about two legs at one site is used.

## 6. Two reducing traceless blocks, and all square-zero B

**Theorem 6.1.** Suppose A∈M_4(C) is traceless and B∈M_4(C) is unitarily block diagonal `B=B_1⊕B_2`, where each `B_j∈M_2(C)` is traceless. Then (T2-dual) holds. The same statement holds with A and B exchanged.

*Proof.* After the site-local unitary, X is the orthogonal direct sum of the two 8×8 blocks

`Γ_j=A⊗I_2+I_4⊗B_j`, j=1,2.

The singular values of X are the union of those of Γ_1 and Γ_2. If both largest singular values are chosen from a single block, their right singular vectors span a space with a 2D leg at site2, and Lemma 5.1 gives (T2-dual). If one is from each block, Lemma 4.1 gives

`σ_1(Γ_1)²+σ_1(Γ_2)² <= 2||A||F²+2(||B_1||F²+||B_2||F²)`
` = 2(||A||F²+||B||F²)`.

This includes ties by choosing singular vectors within the block decomposition. ∎

**Corollary 6.2.** If B²=0, then (T2-dual) holds for every traceless A. Indeed `ran B⊂ker B`, so `rank B≤2`. Choose a 2D subspace E with `ran B⊂E⊂ker B`; relative to `E⊕E⊥`, B has form `[[0,D],[0,0]]`. Independent unitaries on E and E⊥ give an SVD of D, after which B is a direct sum of two nilpotent 2×2 blocks `b_1E_01⊕b_2E_01`, each traceless. This includes rank-one B, but §2–3 additionally prove the explicit sharp (†) gap.

## 7. Exact gap and boundaries

Theorems 3 and 6.1 are **new written candidate proofs**, not parent or reviewer acceptance. They extend beyond the normal-A-or-B class because each 2×2 block can be non-normal. They do not cover a general non-normal B with no reducing 2+2 decomposition into separately traceless blocks, nor do they prove the full two-copy T2, the d=4 three-copy target, or global equality. In particular no inference about those obligations follows from the finite search/Hessian material in the frozen v3 packet.

All statements here use original q2/trace algebra, weighted finite-dimensional Cauchy–Schwarz, ordinary Haar second moments, singular values, and elementary swap positivity. No Böttcher–Wenzel theorem, external source, f196 review return, held episode/consumer/guidance, selected physical target value, or new conditional-source variant is a premise. Earlier process findings and the qualified distinct-**site** f168 scope remain unchanged. The known public full-target claim retires new-discovery status; no literature-exhaustiveness or novelty claim is made.
