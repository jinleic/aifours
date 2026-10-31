# The full T2 gap for every rank-two test projector with 2×2 local support

**Status: WRITTEN, self-contained owner candidate, UNREVIEWED.** This is an original-quantifier dual-domain theorem and strictness result; it does not assume a separable or PPT test projector, or any structural restriction on the original local matrices. It does not depend on earlier 2+2, separable, PPT, chiral, tracezero-dual or Schur-chain candidates. No numerical/physical-q sample, scientific program, external source, false f198 estimate, held/ZERO material or novelty claim is used.

## 1. Main theorem and exact remainder

Let `P` be a rank-two orthogonal projector on `C4⊗C4` whose two local support dimensions satisfy

`rank(Tr_A P)≤2`, `rank(Tr_B P)≤2`.  (1.1)

For every arbitrary traceless complex `A,B∈M4(C)`, with `X=A⊗I4+I4⊗B` and `L=||A||_F²+||B||_F²`,

**`Tr(PX†X)≤2L`.**  (1.2)

If **both `A²` and `B²` are nonnormal**, then the inequality is strict. Consequently, if some maximizing top-two right-singular projector meets (1.1), the original pair satisfies T2, strictly on the entire both-squares-nonnormal complement. The theorem includes NPT as well as PPT projectors; it imposes no separability, local-factor normality, 2+2 reducibility, numerical threshold or other restriction on `A,B`.

The exact remaining dual test domain in this route consists of rank-two projectors for which **at least one local marginal has rank at least three**. A projector in that domain is not claimed to be a counterexample. The theorem does not settle f274 optimized `η` membership, unrestricted T2/T3/Z2/q3, physical/η counterexamples, source correctness, stronger-family/human/formal review, execution or novelty.

## 2. Local supports and orthogonal leakage

Choose local rank-two projections `U_A,U_B` containing the supports of `Tr_B P` and `Tr_A P`, respectively. The projector is supported in `U_A⊗U_B`: for example,

`Tr[P((I−U_A)⊗I)]=Tr[(I−U_A)Tr_B P]=0`,

and positivity of `P` forces `(I−U_A)⊗I` to annihilate its range; similarly on B. The projections can be extended to rank two if a support has dimension one.

In local bases adapted to these projections write

`A=[[αI2+C,A12],[A21,A22]]`, `B=[[βI2+D,B12],[B21,B22]]`,

where `Tr C=Tr D=0`. On the 2⊗2 input support, the tensor sum's outputs in the three mutually orthogonal spaces

`U_A⊗U_B`, `U_A⊥⊗U_B`, `U_A⊗U_B⊥`

are, respectively,

`Y=(α+β)I4+C⊗I2+I2⊗D`, `A21⊗I2`, `I2⊗B21`.

Let `ρ=Tr_B P|U_A`, `τ=Tr_A P|U_B`. They are positive 2×2 matrices of trace two, so `ρ,τ≤2I2`. Orthogonality of the output spaces gives

`Tr(PX†X)=Tr(PY†Y)+Tr(ρ A21†A21)+Tr(τ B21†B21)`.  (2.1)

Here `P` in the first term is restricted to its 2⊗2 support. Since `0≤P≤I4`,

`Tr(PY†Y)≤||Y||_F²=4|α+β|²+2||C||_F²+2||D||_F²`

`≤8(|α|²+|β|²)+2||C||_F²+2||D||_F²`.  (2.2)

The cross terms in `||Y||_F²` vanish because `C,D` are traceless. Separate trace zero of `A,B` gives `Tr A22=−2α`, `Tr B22=−2β`; trace Cauchy on 2×2 matrices yields

`||A22||_F²≥2|α|²`, `||B22||_F²≥2|β|²`.  (2.3)

The leakage terms in (2.1) are at most `2||A21||_F²` and `2||B21||_F²`. Adding (2.2)–(2.3), together with the nonnegative `2||A12||²` and `2||B12||²` contributions in the source norm, proves (1.2) for every projector satisfying (1.1).

## 3. Equality when both local supports have dimension two

Assume both marginals have rank two. Since each is positive with trace two, its largest eigenvalue is strictly less than two. If equality holds in (1.2), each nonnegative slack in Section 2 vanishes. In particular the inactive-column terms give `A12=B12=0`, and strict positivity of `2I−ρ`, `2I−τ` gives `A21=B21=0`. Equality in (2.3) gives

`A22=−α I2`, `B22=−β I2`,

and equality in `|α+β|²≤2(|α|²+|β|²)` gives `α=β`.

If this common scalar is zero, `A=C⊕0`, `B=D⊕0`; Cayley–Hamilton makes `A²,B²` scalar on their 2×2 blocks and zero outside, hence normal.

Suppose the common scalar is nonzero. Equality in `Tr(PY†Y)≤Tr(Y†Y)` forces `Y(I−P)=0` and therefore `rank Y≤2`. We use the following elementary rank fact:

> If `t≠0` and both traceless `C,D∈M2(C)` are nonnormal, then `rank(tI4+C⊗I2+I2⊗D)≥3`.

Let the eigenvalues of `C,D` be `±λ,±μ`. If `λμ≠0`, both blocks are diagonalizable; two zero values among `t±λ±μ` would force `λ=0`, `μ=0` or `t=0`. If exactly one local eigenvalue is zero, the corresponding nonnormal block is nonzero nilpotent rank one; diagonalizing the other block gives two 2×2 summands, at most one of which is rank one and the other invertible. If both vanish, the two commuting nilpotent tensor terms have nilpotent sum, so its nonzero scalar shift is invertible. The rank fact follows.

If both `A²,B²` were nonnormal after the block-diagonal equalities, then `C,D` would both be nonnormal, because

`(αI2+C)²=(α²−det C)I2+2αC`,

and similarly for `D`. With `t=2α≠0` the rank fact contradicts `rank Y≤2`. Thus equality cannot occur when both original local squares are nonnormal.

## 4. Rank-one local support

If one marginal of the rank-two projector has rank one, its support is a product subspace, so `P=|v⟩⟨v|⊗Q` or the swapped form, with `rank Q=2`. For the displayed orientation let `a=⟨v,Av⟩`, `b=Tr(QB)`. Directly,

`Tr(PX†X)=2||Av||²+||BQ||_F²+2 Re(conjugate(a)b)`.

Trace zero of `A` and Cauchy on the three complementary diagonal entries give `||A||²−||Av||²≥|a|²/3`. Trace zero of `B` and rank two of `Q,I−Q` give `||BQ||²≥|b|²/2` and `||B(I−Q)||²≥|b|²/2`. Therefore the full gap is at least

`(2/3)|a|²+(3/2)|b|²−2|ab|≥0`.

If equality holds, equality in both B trace bounds forces `B=(b/2)(2Q−I4)`, which is normal. In the swapped orientation the same reasoning forces A normal. Hence equality is impossible when both local squares are nonnormal. This completes the strictness proof for every support configuration in (1.1).

## 5. Coverage and review boundary

The test-domain theorem includes projectors with **entangled/NPT** `P/2` as well as separable ones; no entanglement assumption was used. For example, the 2D subspace spanned by `|00⟩` and `a|01⟩+b|10⟩` with arbitrary `ab≠0` has 2×2 local support. With the second vector normalized, its projector's partial transpose has on `span{|00⟩,|11⟩}` a principal block of determinant `−|ab|²/(|a|²+|b|²)²<0`. This is a symbolic proof that the paid domain includes NPT projectors, not a selected physical q or a counterexample.

The separate UNREVIEWED rank-two PPT-projector classification would additionally show that all PPT rank-two projectors satisfy (1.1), but it is **not a premise** of this theorem. The unpaid dual domain still includes projectors with a local marginal of rank three or four, including NPT cases. No f274-optimized η-failure, physical counterexample, unrestricted T2/T3/Z2/q3, source correctness, execution, formal/kernel or stronger-family/human review, or novelty is claimed. Disjoint written review should reconstruct the local-support leakage decomposition, all complex trace/equality conditions, the 2×2 rank fact, and the rank-one support endpoint. Existing frozen scopes and STOP/HOLD/ZERO restrictions remain unchanged.
