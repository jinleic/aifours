# The original T2 gap whenever either test-projector marginal has rank at most two

**Status: WRITTEN, one self-contained owner candidate, UNREVIEWED.** This pays the complete one-qubit-local-support test domain, including arbitrary entangled/NPT projectors, and proves strictness when both original local squares are nonnormal. It uses only finite-dimensional SVD, 2×2 unitary Schur/hollowing, Ky Fan/Frobenius duality and elementary rank algebra, all reconstructed below. No earlier owner candidate, external source, numerical/physical-q sample, scientific program, false f198 estimate, held/ZERO input or novelty claim is used.

## 1. Theorems and precise original remainder

**Rank-two partial-trace inequality.** For every `n≥1` and every operator `R∈M(C2⊗Cn)` with `rank R≤2`,

`||Tr_n R||_F²+||Tr_2 R||_F²−|Tr R|²/2 ≤ 2||R||_F²`.  (1.1)

**Original-pair consequence.** For every rank-two projector `P` on `C4⊗C4` with **either** local marginal of rank at most two, and every arbitrary complex traceless `A,B∈M4(C)`, setting `X=A⊗I4+I4⊗B` and `L=||A||_F²+||B||_F²`,

`Tr(PX†X)≤2L`.  (1.2)

If **both `A²` and `B²` are nonnormal**, (1.2) is strict. Consequently a pair with a maximizing top-two right-singular projector of either local rank at most two satisfies T2, strictly on the both-squares-nonnormal complement.

The exact still-unhandled test domain in this route has **both local marginal ranks at least three**. Other independently proved special cases may lie there; no such projector is asserted to be a counterexample. This packet does not settle f274 optimized `η` membership, unrestricted T2/T3/Z2/q3, a physical or η counterexample, source correctness, independent-family/human/formal review or novelty.

## 2. A dimension-free 2×n rank-two partial-trace proof

An elementary lemma: every traceless complex 2×2 matrix can be made zero-diagonal by a unitary similarity. Indeed Schur it to `[[λ,z],[0,−λ]]`. The expectation on a unit vector `(cosθ,e^{iφ}sinθ)` is `λ cos(2θ)+(z e^{iφ}/2)sin(2θ)`. Choose `φ` opposite the phase of `λ` and `θ∈[0,π/4]` to cancel the magnitudes; the cases `λ=0` or `z=0` are immediate. The orthogonal complement also has zero expectation because the trace is zero.

Apply such a local unitary to the traceless part of `Tr_n R`. Local unitary conjugation preserves `rank R`, `||R||_F`, `Tr R`, and both partial-trace Frobenius norms. In the resulting qubit basis write

`R=[[P,Q],[T,S]]`, with `P,Q,T,S∈Mn(C)` and `Tr(P−S)=0`.  (2.1)

Direct expansion gives the **exact identity**

`2||R||_F²−[||Tr_n R||_F²+||Tr_2 R||_F²−|Tr R|²/2]`

`= ||P−S||_F²−|Tr(P−S)|²/2`

`  +2||Q||_F²−|Tr Q|² +2||T||_F²−|Tr T|²`.  (2.2)

The first trace term is zero by (2.1). `Q,T` are submatrices of the original rank-at-most-two operator, so each has rank at most two. For any matrix `Z`,

`|Tr Z|²≤||Z||_1²≤rank(Z)||Z||_F²`.

Consequently both remaining bracketed terms in (2.2) are nonnegative, proving (1.1) for every complex `R` and every `n`.

The rank restriction is essential: for nonzero traceless `C∈M2`, `R=C⊗I3` has rank at least three and gives left side `9||C||²` versus right side `6||C||²`. This is a symbolic observation about a false stronger premise, not a physical counterexample.

## 3. Weighted Ky Fan form and full original-source lift

For traceless `C∈M2(C)`, `D∈Mn(C)` and `t∈C`, set

`Y=tI_(2n)+C⊗In+I2⊗D`.

Ky Fan/Frobenius duality gives

`√S2(Y)=max_{rank R≤2, ||R||_F=1}|Tr(R†Y)|`.

The squared dual norm of the weighted source `2n|t|²+2||C||²+2||D||²` is

`|Tr R|²/(2n)+||(Tr_n R)_0||_F²/2+||(Tr_2 R)_0||_F²/2`,

which expands to one half of the left side of (1.1). Hence (1.1) is exactly equivalent to the **all-variable** weighted Ky Fan bound

`S2(Y)≤2n|t|²+2||C||_F²+2||D||_F²`.  (3.1)

Now let a rank-two original `P` have A-local marginal rank at most two. Choose a two-dimensional A support containing it and write

`A=[[αI2+C,A12],[A21,A22]]`, `Tr C=0`; the B factor remains completely arbitrary and traceless. The inside-support tensor sum is

`Y=α I8+C⊗I4+I2⊗B`.

The inside output and the `A21` leakage output occupy orthogonal local A subspaces. With `ρ=Tr_B P` restricted to the chosen 2D A support, `ρ⪰0`, `Trρ=2`,

`Tr(PX†X)=Tr(PY†Y)+Tr(ρ A21†A21)`.

Equation (3.1) with `n=4` gives `Tr(PY†Y)≤S2(Y)≤8|α|²+2||C||²+2||B||²`. Trace zero gives `Tr A22=−2α`, hence `||A22||²≥2|α|²`; also `ρ≤2I2`. The resulting exact decomposition of the gap into nonnegative terms is

`2L−Tr(PX†X)`

`= 2||A12||² + Tr[(2I2−ρ)A21†A21] + 2(||A22||²−2|α|²)`

`  + [8|α|²+2||C||²+2||B||²−Tr(PY†Y)] ≥0`.  (3.2)

This proves (1.2) for an A-local rank at most two. Exchanging tensor factors proves the B-local case. No assumption is imposed on the other marginal rank, separability or PPT status.

## 4. Equality forces a normal local square

If one local marginal has rank one, the projector is `|v⟩⟨v|⊗Q` or its swap with `rank Q=2`. For the first orientation set `a=⟨v,Av⟩`, `b=Tr(QB)`. Trace zero and elementary Cauchy yield

`||A||²−||Av||²≥|a|²/3`, `||BQ||²,||B(I−Q)||²≥|b|²/2`.

The full gap is at least `(2/3)|a|²+(3/2)|b|²−2|ab|≥0`. Equality in the two B trace inequalities forces `B=(b/2)(2Q−I4)`, which is normal. Thus one original square is normal.

Assume now the A marginal has rank exactly two. Its two positive eigenvalues sum to two, so `2I2−ρ>0`. If equality holds in (3.2), then

`A12=A21=0`, `A22=−α I2`,

and the inside Ky Fan/weighted bound is saturated. Put `R=YP`, regarded as an operator on `C2⊗C4`. Equality in weighted Frobenius duality and (1.1) forces equality in (1.1) for this `R`, and fixes the original source by

`C=(Tr_4 R)_0/2`, `B=(Tr_2 R)_0/2`.  (4.1)

The common proportionality constant is exactly one because both weighted source norm squared and `||R||_F²` equal `Tr(PY†Y)>0`, and their dual pairing is that same positive number. The zero-source case is trivial.

Locally hollow `(Tr_4 R)_0` as in Section 2. Equality in (2.2) gives

`R=[[G,Q],[T,G]]`,

where each of `Q,T` is either zero or a complex scalar times a rank-two **orthogonal projection**. The latter equality claim follows from `|Tr Z|≤||Z||_1≤√2||Z||_F`: equality for nonzero rank≤2 `Z` forces its two singular values equal and its left and right singular directions equal up to a common phase, so `Z=λΠ`.

If `Q=T=0`, then `(Tr_4 R)_0=0`; (4.1) gives `C=0`, and the already-established block form makes `A` normal.

Otherwise, assume `Q=λΠ≠0`; the case `T≠0,Q=0` is symmetric. Swapping the two block columns gives `[[λΠ,G],[G,T]]`, still of rank at most two. Its top-left block has rank two, so equality of the full rank with this pivot rank forces

`G=ΠGΠ`, `T=λ⁻¹G²`.  (4.2)

If `T=0`, then `G²=0`. If `T=μΠ′≠0`, its support is contained in `Π`; both are rank-two orthogonal projections, so `Π′=Π` and `G²=λμΠ`.

By (4.1), `B=G−(Tr G/4)I4`. If `G²=0`, `Tr G=0`, so `B²=0` is normal. If `G²=κΠ` with `κ≠0`, the polynomial `z²−κ` has distinct roots on the two-dimensional support of `Π`. Either the two eigenvalues are opposite, giving `Tr G=0` and `B²=κΠ`, or they coincide, forcing `G` to be scalar on `Π` and making `B` normal. Thus **B² is normal in every nonzero-Q/T equality case**.

Therefore equality in (1.2) always forces `A²` or `B²` normal. The contrapositive proves strictness when both original squares are nonnormal. This argument does not assume the original factors are block diagonal before equality forces it.

## 5. Scope and review

The theorem pays all rank-two test projectors with **either** local marginal rank≤2; it strictly extends the both-marginals≤2 test-domain statement and includes NPT projectors. No claim is made for all projectors with both local ranks≥3, for f274 `η>2L`, a physical counterexample, unrestricted T2/T3/Z2/q3, execution, external-source correctness, formal/kernel or stronger-family/human review, or novelty. Disjoint review should independently reconstruct the qubit hollowing identity, Ky Fan constants, arbitrary-source leakage, equality in the trace bound, rank-two pivot with singular projections and all complex phase cases. Earlier frozen packets and STOP/HOLD/ZERO restrictions remain unchanged.
