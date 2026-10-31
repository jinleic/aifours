# Strict original T2 on separable top projectors for both-nonnormal pairs

**Status: WRITTEN, UNREVIEWED additive equality analysis.** The prerequisite is the independent all-separable rank-two projector proof `frontier-20261029-d4-t2-all-separable-rank2-projectors-v1.md` (SHA-256 8f86264caffb9bb3885ae63dfcb86586dcbef8d16c2dec1df4f2a988c477f42d). Its bytes and any already frozen review remain unchanged. No normal-factor physical class, magnitude threshold, selected physical q/numerical instance, program, held/ZERO input or novelty assertion is used.

## 1. Claim

Let `A,B∈M4(C)` be arbitrary traceless complex matrices, `X=A⊗I4+I4⊗B`, `L=||A||_F²+||B||_F²`, and let `P/2` be any separable rank-two projector. Then

**`Tr(PX†X)=2L  ⇒  A is normal OR B is normal`.**  (1.1)

Equivalently, if **both** local factors are nonnormal, the fixed-projector inequality is strict for every separable `P/2`. In particular this holds whenever both local squares are nonnormal. If some maximizing top-two right-singular projector is separable, then such a both-nonnormal pair satisfies **strict T2**.

This is not a statement about entangled projectors, or proof that any pair lies outside f274's optimized `η≤2L` region. The full T2/T3/Z2/q3, physical or optimized-certificate counterexamples, source correctness and novelty remain open.

## 2. Nonparallel second local rays

The prerequisite proves that every separable rank-two projector has an orthonormal product basis. Up to local unitaries and factor swap, write

`P=|e1⊗b⟩⟨e1⊗b|+|e2⊗d⟩⟨e2⊗d|`,

`e1⊥e2`, `||b||=||d||=1`, `r=|⟨b,d⟩|`.

For `0≤r<1`, let `z1=A11`, `z2=A22`, `s=z1+z2`, `q=z1−z2`, `S=|b⟩⟨b|+|d⟩⟨d|`, `W=2I−S>0`, `C=z1|b⟩⟨b|+z2|d⟩⟨d|`. The prerequisite proves the exact lower bound

`2L−Tr(PX†X) ≥ [4(1−r²)/(3−r²)]|s|²`.

Equality therefore forces `s=0`. Equality in its preceding A-side estimate forces all offdiagonal A entries to vanish: their gap coefficients are `1` in the first two columns and `2` in the other columns. It also forces the two complementary diagonal entries to equal `−s/2=0`. Thus

`A=t diag(1,−1,0,0)` for some `t∈C`,  (2.1)

and A is normal.

For completeness, equality also determines B. The scalar `λ` minimizing `||(C−λI)W^(−1/2)||²` in the prerequisite is zero when `s=0`; equality in its completed square gives

`B=CW⁻¹=t(P_b−P_d)W⁻¹`.  (2.2)

In the symmetric orthonormal basis for `b,d` used in the prerequisite, this has the form

`B=t [[0,√((1−r)/(1+r))],[√((1+r)/(1−r)),0]] ⊕ 0_2`.

Hence both `A²` and `B²` are normal on this nonparallel branch. This stronger observation is not needed for (1.1). If `t=0`, (2.1)–(2.2) give the zero pair.

## 3. Parallel endpoint

For `r=1`, the projector is `Q⊗|v⟩⟨v|` with `rank Q=2`. We state the equality calculation for the swapped equivalent `|v⟩⟨v|⊗Q`; the conclusion is symmetric under exchanging A and B.

Put `a=⟨v,Av⟩`, `b0=Tr(QB)`. The prerequisite's proof writes the gap as a sum of nonnegative terms:

`2(||A||²−||Av||²−|a|²/3)`

`+ (||BQ||²−|b0|²/2) + 2(||B(I−Q)||²−|b0|²/2)`

`+ (√(2/3)|a|−√(3/2)|b0|)² + 2(|ab0|−Re(conjugate(a)b0))`.

Equality makes every term zero. In particular, trace-Cauchy equality for both `Q` and `I−Q` forces B block diagonal with scalar blocks `b0 I2/2` and `−b0 I2/2`; hence **B is normal**. This remains true when `a=b0=0`. The symmetric orientation gives normal A. Therefore every separable P equality has at least one normal local factor, proving (1.1).

For reference, equality throughout gives `b0=2a/3`, `B=(a/3)(2Q−I4)` and `A=a|v⟩⟨v|−(a/3)(I−|v⟩⟨v|)+|u⟩⟨v|` with `u⊥v`; this is not assumed in the proof.

## 4. Boundaries

The statement `P/2 separable` concerns the rank-two **test projector**, not a claim that `A` or `B` is normal. The consequence for a pair requires a separable **maximizing** P. Entangled-projector cases, whether the physical class escapes f274's full optimized `η≤2L` region, unrestricted T2/T3/Z2/q3, a physical/q counterexample, source correctness, execution, formal/kernel or stronger-family/human review and novelty remain open. Disjoint review should reconstruct all equality implications, including complex phases and the parallel endpoint.
