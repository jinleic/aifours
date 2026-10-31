# The full original T2 gap for every separable rank-two test projector

**Status: WRITTEN, self-contained owner candidate, UNREVIEWED.** This proves an all-variable part of the original rank-two-projector dual quantifier, not unrestricted T2. In particular it pays separable projectors which are **not** diagonal in any local product basis and may lie in the positive-definite interior of the Hermitian commutator reduction. No 2+2-reducing/chiral/tracezero-dual candidate, source certificate, false f198 estimate, numerical/physical-q sample, scientific program, held/ZERO material or novelty claim is used. Needed ingredients are elementary finite-dimensional linear algebra, Cauchy–Schwarz and the definition of separability.

## 1. Claim and precise remainder

For **every** traceless `A,B∈M4(C)`, `X=A⊗I4+I4⊗B`, `L=||A||_F²+||B||_F²`, and every rank-two orthogonal projector `P` such that `P/2` is separable,

**`Tr(PX†X)≤2L`.**  (1.1)

There is no normality, local-rank, block-reducibility, parameter-threshold or basis assumption on `A,B`. Ky Fan says unrestricted T2 requires (1.1) for *all* rank-two projectors; consequently only projectors with **entangled** `P/2` remain in this particular route. A separable projector is not presumed to be product-basis diagonal.

For context, the earlier commutator boundary packet only paid product-basis-diagonal projectors, a proper subfamily; that earlier packet is not a premise here. No claim about the entangled-projector interior, optimized f274 `η`, physical counterexamples, unrestricted T2/T3/Z2/q3, source correctness, stronger-family/human/formal review or novelty follows.

## 2. A separable rank-two projector has an orthonormal product basis

Let `P/2` be separable. In finite dimensions it has a finite positive decomposition into pure product projectors. Every product vector occurring in such a decomposition lies in `S=range P`: if `x⊥S`, then `0=⟨x,Px⟩` is a sum of nonnegative terms, forcing each overlap to vanish. As `rank P=2`, at least two independent product vectors occur.

If two independent product vectors in `S` share one local factor, their whole 2-dimensional span is a common-local-factor product subspace, which plainly has an orthonormal product basis. Otherwise choose independent products `a1⊗b1,a2⊗b2` with both local pairs linearly independent. Every nontrivial linear combination with both coefficients nonzero has Schmidt rank two: use the two independent local pairs as local coordinates, where its coefficient matrix is diagonal with two nonzero entries. Thus `S` contains exactly those two product rays.

In the latter case the positive separable decomposition of `P` uses only those two rays, so `P=α|u⟩⟨u|+β|v⟩⟨v|` for unit nonparallel products and `α,β>0`. Restricted to `S`, the two columns `√α u,√β v` form a square matrix with `TT†=I`; hence they are orthonormal and `α=β=1`. Thus `u,v` are orthonormal. In either case `P` is the sum of two orthonormal product projectors. Since their inner product factors, at least one of the two local pairs is orthogonal.

Exchange local factors if necessary. By a local unitary and harmless phases it suffices to consider

`P=|e1⊗b⟩⟨e1⊗b|+|e2⊗d⟩⟨e2⊗d|`,

where `e1⊥e2`, `||b||=||d||=1`, and `r=|⟨b,d⟩|∈[0,1]`. The case `r=1` is a product projector and is handled in Section 4; the core proof allows all `0≤r<1`.

## 3. Two orthogonal first factors, arbitrary second overlap

Write `z1=A11`, `z2=A22`, `s=z1+z2`, `q=z1−z2`. The fixed-projector expansion is

`Tr(PX†X)=||Ae1||²+||Ae2||²+||Bb||²+||Bd||²`

`+2 Re[conjugate(z1)⟨b,Bb⟩+conjugate(z2)⟨d,Bd⟩]`.  (3.1)

Because `Tr A=0`, its two remaining diagonal entries sum to `−s`. The offdiagonal A entries have nonnegative coefficients in the gap, so

`2||A||_F²−||Ae1||²−||Ae2||² ≥ |z1|²+|z2|²+|s|² = |q|²/2+3|s|²/2`.  (3.2)

Set

`S=|b⟩⟨b|+|d⟩⟨d|`, `W=2I4−S`, `C=z1|b⟩⟨b|+z2|d⟩⟨d|`.

For `r<1`, `W>0`. The B part of the gap and the cross term in (3.1) are

`||B W^(1/2)||_F²−2 Re⟨C,B⟩_F`.

Since `Tr B=0`, `⟨C,B⟩=⟨C−λI4,B⟩` for any `λ∈C`. Weighted Cauchy–Schwarz gives the exact lower bound

`||B W^(1/2)||_F²−2 Re⟨C,B⟩_F ≥ −||(C−λI4)W^(−1/2)||_F²`.  (3.3)

Choose `λ` minimizing the right-hand norm. We now compute that minimum for **all** `r<1`.

After changing the phase of `d`, assume `⟨b,d⟩=r≥0`. On their two-dimensional span choose an orthonormal basis so that

`b=√((1+r)/2)e_+ + √((1−r)/2)e_-`,

`d=√((1+r)/2)e_+ − √((1−r)/2)e_-`.

Then, with zero C on the two-dimensional orthogonal complement,

`W=diag(1−r,1+r,2,2)`,

`C|span=(1/2)[[(1+r)s, √(1−r²)q],[√(1−r²)q,(1−r)s]]`.

The minimizing scalar is `λ=Tr(W⁻¹C)/Tr(W⁻¹)`. Direct expansion gives

`min_λ ||(C−λI4)W^(−1/2)||_F²`

`= |q|²/2 + [(1+5r²)/(2(3−r²))]|s|²`.  (3.4)

For example, before minimization the coefficient of `|s|²` is `(1+3r²)/(2(1−r²))`, while `Tr(W⁻¹C)=s(1+r²)/(1−r²)` and `Tr(W⁻¹)=(3−r²)/(1−r²)`; subtracting the corresponding scalar projection yields (3.4). This computation is an exact symbolic identity, not a selected case.

Subtracting (3.4) from (3.2) yields the nonnegative explicit bound

`2L−Tr(PX†X) ≥ [4(1−r²)/(3−r²)] |s|² ≥ 0`  (3.5)

for every original traceless `A,B` and every `0≤r<1`. The omitted A offdiagonal slack and B weighted square in (3.2)–(3.3) are also nonnegative. No equality or strictness is inferred when `s=0`.

## 4. The parallel endpoint

If `r=1`, the second local rays coincide and `P=Q⊗|v⟩⟨v|` with `rank Q=2`. For completeness, the following symmetric product-projector argument pays it directly, without treating a singular `W⁻¹`.

For arbitrary unit `v`, rank-two `Q` and traceless `A,B`, set `a=⟨v,Av⟩`, `b=Tr(QB)`. For `P′=|v⟩⟨v|⊗Q`,

`Tr(P′X†X)=2||Av||²+||BQ||_F²+2 Re(conjugate(a)b)`.

Trace zero of `A` and Cauchy on the three complementary diagonal entries give `||A||²−||Av||²≥|a|²/3`. Trace zero of `B` and rank two of both `Q,I−Q` give `||BQ||²≥|b|²/2`, `||B(I−Q)||²≥|b|²/2`. Hence the full gap is at least

`(2/3)|a|²+(3/2)|b|²−2|ab|≥0`.

Swapping local factors gives the required form `Q⊗|v⟩⟨v|`. This proves (1.1) at `r=1` and completes the full separable-projector proof.

## 5. Scope and remaining task

No separable rank-two projector is a counterexample to the original dual inequality, including non-product-basis-diagonal separable projectors. A failure of unrestricted T2, if one exists, must use an **entangled** rank-two projector `P/2` together with suitable traceless `A,B`. This is an exact necessary condition, not a claim that entanglement is sufficient or that any example exists.

The f274-optimized certificate comparison, the full original entangled-projector inequality, the 8×8 and scalar residuals, T3/Z2/original q3, source correctness, Lean/kernel or stronger-family/human review, execution and novelty remain open. Disjoint review must reconstruct the separable-projector classification, weighted scalar minimization, phase/endpoint handling and full complex-source quantifiers. All prior frozen packet bytes and STOP/HOLD/ZERO restrictions remain unchanged.
