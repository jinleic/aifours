# The original T2 gap on every separable rank-two test projector

**Status: WRITTEN, one self-contained owner candidate, UNREVIEWED.** This successor consolidates the previously pinned all-separable-projector proof and its both-nonnormal strictness analysis without changing their bytes or any frozen review. It uses only elementary finite-dimensional linear algebra, Cauchy–Schwarz and separability. No other owner candidate, source certificate, f198 false estimate, selected numerical/physical q, scientific program, held/ZERO material or novelty assertion is used.

## 1. Full all-variable result and exact remainder

For every traceless `A,B∈M4(C)`, `X=A⊗I4+I4⊗B`, `L=||A||_F²+||B||_F²`, and every rank-two orthogonal projector `P` with separable `P/2`,

**`Tr(PX†X)≤2L`, and equality forces `A` normal OR `B` normal.**  (1.1)

Thus, if both local factors are nonnormal—including the entire both-squares-nonnormal case—the fixed-projector gap is **strict** for every separable `P/2`. If some maximizing top-two right-singular projector is separable, strict T2 follows for that pair. There is no local-rank, reducibility, normality, magnitude or parameter-threshold assumption on the original factors.

Ky Fan requires (1.1) for **all** rank-two `P`; the exact unhandled test domain in this route consists of projectors with **entangled** `P/2`. Entanglement is not asserted to be sufficient for a counterexample. The statement does not decide whether any physical pair lies outside the entire f274 optimized `η≤2L` region, and it is not a proof of unrestricted T2/T3/Z2/q3, a physical or η counterexample, source correctness, formal/kernel or stronger-family/human review, or novelty.

## 2. Separable rank-two projectors and product bases

A finite-dimensional separable `P/2` admits a finite positive sum of pure product projectors. Every product vector in such a decomposition lies in `S=range P`: for `x⊥S`, the nonnegative summands in `0=⟨x,Px⟩` must each vanish. Since `rank P=2`, at least two independent product vectors occur.

If two independent product vectors share a local factor, their entire 2D span is a common-local-factor product subspace and has an orthonormal product basis. Otherwise choose products `a1⊗b1,a2⊗b2` whose two A factors and two B factors are each linearly independent. A combination with both coefficients nonzero has Schmidt rank two: use those independent local vectors as coordinates, yielding a 2×2 diagonal coefficient matrix with two nonzero diagonal entries. Thus the span contains exactly those two product rays.

The separable decomposition of `P` in the latter case uses only these rays, so `P=α|u⟩⟨u|+β|v⟩⟨v|` for unit nonparallel products and `α,β>0`. Restricted to `S`, the two columns `√α u,√β v` satisfy `TT†=I`; the square matrix `T` is therefore unitary. Hence `α=β=1` and `u⊥v`. In either case **P has an orthonormal product basis**. Its two product vectors are orthogonal because at least one pair of their local factors is orthogonal.

Exchange local factors if needed. Local unitaries and harmless vector phases reduce to

`P=|e1⊗b⟩⟨e1⊗b|+|e2⊗d⟩⟨e2⊗d|`,

`e1⊥e2`, `||b||=||d||=1`, `r=|⟨b,d⟩|∈[0,1]`.  (2.1)

No requirement that `b,d` be equal or orthogonal is imposed.

## 3. The nonparallel case and an exact weighted gap

Assume `0≤r<1`. Write `z1=A11`, `z2=A22`, `s=z1+z2`, `q=z1−z2`. The exact fixed-projector expansion is

`Tr(PX†X)=||Ae1||²+||Ae2||²+||Bb||²+||Bd||²`

`+2 Re[conjugate(z1)⟨b,Bb⟩+conjugate(z2)⟨d,Bd⟩]`.  (3.1)

The two remaining diagonal entries of `A` sum to `−s`. All A-offdiagonal gap coefficients are positive: one in the first two columns and two in the other columns. Cauchy–Schwarz therefore gives

`2||A||_F²−||Ae1||²−||Ae2||² ≥ |z1|²+|z2|²+|s|² = |q|²/2+3|s|²/2`.  (3.2)

Set

`S=|b⟩⟨b|+|d⟩⟨d|`, `W=2I4−S>0`, `C=z1|b⟩⟨b|+z2|d⟩⟨d|`.

The B contribution and cross term in (3.1) are `||BW^(1/2)||_F²−2 Re⟨C,B⟩_F`. Because `Tr B=0`, `C` may be replaced by `C−λI4` in the inner product. Completing a Frobenius square gives, for every `λ∈C`,

`||BW^(1/2)||_F²−2 Re⟨C,B⟩_F ≥ −||(C−λI4)W^(−1/2)||_F²`.  (3.3)

Change the phase of `d` so `⟨b,d⟩=r≥0`, and use an orthonormal basis of their span with

`b=√((1+r)/2)e_+ + √((1−r)/2)e_-`,

`d=√((1+r)/2)e_+ − √((1−r)/2)e_-`.

Then

`W=diag(1−r,1+r,2,2)`,

`C|span=(1/2)[[(1+r)s, √(1−r²)q],[√(1−r²)q,(1−r)s]]`,

and `C` is zero on the two-dimensional orthogonal complement. The minimizing scalar in (3.3) is `λ=Tr(W⁻¹C)/Tr(W⁻¹)`. Direct expansion gives

`min_λ ||(C−λI4)W^(−1/2)||_F² = |q|²/2+[(1+5r²)/(2(3−r²))]|s|²`.  (3.4)

Indeed the coefficient of `|s|²` before minimization is `(1+3r²)/(2(1−r²))`, and

`Tr(W⁻¹C)=s(1+r²)/(1−r²)`, `Tr(W⁻¹)=(3−r²)/(1−r²)`.

Combining (3.2)–(3.4), for every original pair and all `0≤r<1`,

`2L−Tr(PX†X) ≥ [4(1−r²)/(3−r²)]|s|² ≥ 0`.  (3.5)

The difference also contains the discarded nonnegative A-offdiagonal and B-square terms. This proves (1.1)'s inequality in the nonparallel case.

### Equality for `r<1`

If the full gap is zero, (3.5) forces `s=0`. Equality in the A estimate forces all A offdiagonal entries to vanish and the two complementary diagonal entries to equal `−s/2=0`. Hence

`A=t diag(1,−1,0,0)`

for some `t∈C`, so **A is normal**. The minimizing `λ` is then zero; equality in the completed square also gives

`B=CW⁻¹=t [[0,√((1−r)/(1+r))],[√((1+r)/(1−r)),0]] ⊕ 0_2`.

Thus in this branch both local squares are normal; `t=0` gives the zero pair. The stronger squared-normal observation is not needed for (1.1).

## 4. The parallel endpoint and its equality

If `r=1`, the projector is `Q⊗|v⟩⟨v|` for a rank-two `Q`. Prove the symmetric orientation `P′=|v⟩⟨v|⊗Q`; exchanging A/B gives the desired endpoint. Put `a=⟨v,Av⟩`, `b0=Tr(QB)`. Directly,

`Tr(P′X†X)=2||Av||²+||BQ||_F²+2 Re(conjugate(a)b0)`.

Trace zero of `A` and Cauchy on its three complementary diagonal entries give `||A||²−||Av||²≥|a|²/3`. Trace zero of `B` and rank two of `Q,I−Q` give `||BQ||²≥|b0|²/2`, `||B(I−Q)||²≥|b0|²/2`. Hence

`2L−Tr(P′X†X) ≥ (2/3)|a|²+(3/2)|b0|²−2|a b0| ≥0`.

If equality holds, both B trace-Cauchy inequalities are equalities. The first forces `QBQ=(b0/2)Q` and `(I−Q)BQ=0`; the second forces `(I−Q)B(I−Q)=−(b0/2)(I−Q)` and `QB(I−Q)=0`. Thus `B=(b0/2)(2Q−I4)` is normal, including `b0=0`. After swapping the local factors the corresponding conclusion is that A is normal. This proves both the inequality and equality implication of (1.1) for `r=1`.

## 5. Nonclaims and review boundary

The theorem concerns the **test projector**; the original factors may both be nonnormal. It pays all separable `P/2`, including non-product-basis-diagonal projectors where the earlier real commutator variance is positive definite. If a T2 failure exists, its test projector must be entangled, but the converse is not asserted. No conclusion is made about any member of the f274 optimized-certificate complement, entangled-projector T2, T3/Z2/original q3, physical/η counterexamples, external-source correctness, computation, independent-family/human/formal verification or novelty. Disjoint written review must reconstruct the rank-two separability classification, the weighted scalar minimization, complex phases, endpoint equality and all source quantifiers. Earlier frozen inputs and STOP/HOLD/ZERO restrictions remain unchanged.
