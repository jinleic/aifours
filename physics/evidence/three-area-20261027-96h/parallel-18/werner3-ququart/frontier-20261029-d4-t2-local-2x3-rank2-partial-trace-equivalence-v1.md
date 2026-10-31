# The exact 2×3 local-support T2 residual is a 6×6 rank-two partial-trace inequality

**Status: WRITTEN, UNREVIEWED exact equivalence, not a proof of its unpaid inequality.** This packet continues the original full-pair dual quantifier immediately beyond the independently written 2×2-local-support theorem. The equivalence and partial paid subcases are derived below without an external theorem, numerical/physical-q sample, scientific program, false f198 estimate, held/ZERO input or novelty claim.

## 1. Exact equivalence and remaining premise

The following statements are equivalent:

**(A)** For every rank-two test projector `P` on `C4⊗C4` whose A-local support has dimension at most two and B-local support at most three, and every complex traceless original `A,B∈M4(C)`,

`Tr[P(A⊗I4+I4⊗B)†(A⊗I4+I4⊗B)]≤2(||A||_F²+||B||_F²)`.

**(B)** For every `R∈M(C2⊗C3)` with `rank R≤2`,

`||Tr_3 R||_F²+||Tr_2 R||_F²−|Tr R|²/2 ≤ 2||R||_F²`.  (1.1)

Exchanging local factors gives the exact `(3,2)` analogue. The full `(2,3)`/`(3,2)` claims are **not proved** here. Section 4 pays rank-one, tracezero rank-two and equal-range/corange rank-two cases of (1.1); the explicit remaining dual premise is **rank exactly two, nonzero trace, and `range R≠range R†`**.

This reduces the next original-support boundary to a 6×6 all-variable, rank-constrained partial-trace inequality, with a converse so no necessary physical directions are dropped. It does not establish any f274 `η>2L`, a physical/q counterexample, unrestricted T2/T3/Z2/q3, source correctness, stronger-family/human/formal review or novelty.

## 2. The 6×6 dual is exactly a weighted Ky Fan inequality

For `C∈M2(C)`, `D∈M3(C)` traceless and `t∈C`, define

`Y=tI6+C⊗I3+I2⊗D`.

Statement (B) is equivalent to

`σ1(Y)²+σ2(Y)² ≤ 6|t|²+2||C||_F²+2||D||_F²`  (2.1)

for all `t,C,D`. Indeed, Ky Fan/Frobenius duality says

`√S2(Y)=max_{rank R≤2, ||R||_F=1}|Tr(R†Y)|`.

For a fixed `R`, optimization over the weighted source norm on the right of (2.1) yields the squared dual norm

`|Tr R|²/6 + ||(Tr_3 R)_0||_F²/2 + ||(Tr_2 R)_0||_F²/2`.

Here `(Tr_3 R)_0=Tr_3 R−(Tr R)I2/2` and `(Tr_2 R)_0=Tr_2 R−(Tr R)I3/3`. Expanding gives exactly one half of the left side of (1.1). Thus (2.1), for all weighted sources, is equivalent to (1.1), for all rank-at-most-two dual operators.

## 3. Both directions of the original-support equivalence

For sufficiency, take any original traceless `A,B` and any rank-two `P` supported in 2⊗3 local subspaces. In adapted local bases write

`A=[[αI2+C,A12],[A21,A22]]`, `B=[[βI3+D,B12],[B21,B22]]`,

with `C,D` traceless. The inside-support tensor sum is

`Y=(α+β)I6+C⊗I3+I2⊗D`.

The inside, A-leakage and B-leakage output spaces are orthogonal. The leakage contributions are at most `2||A21||²` and `2||B21||²`, since the local marginals of rank-two `P` have trace two. By (2.1), the inside contribution is at most

`6|α+β|²+2||C||²+2||D||²`.

Trace zero forces `Tr A22=−2α` and scalar `B22=−3β`. Trace Cauchy therefore gives

`2(||A11||²+||A22||²)≥8|α|²+2||C||²`,

`2(||B11||²+||B22||²)=24|β|²+2||D||²`.

The scalar difference is exactly

`8|α|²+24|β|²−6|α+β|²=2|α−3β|²≥0`.

The remaining source terms `2||A12||²`, `2||B12||²` are nonnegative. Thus (B) implies (A), without assuming a block-diagonal or normal original pair.

For necessity, embed arbitrary `t,C,D` as

`A=(3t I2/4+C) ⊕ (−3t I2/4)`,

`B=(t I3/4+D) ⊕ (−3t/4)`.

Both 4×4 factors are traceless, their active 2⊗3 block is exactly `Y`, there is no leakage, and

`2(||A||_F²+||B||_F²)=6|t|²+2||C||_F²+2||D||_F²`.

Applying (A) to every rank-two projector in the active space and maximizing proves (2.1), hence (B). The converse is exact; it is not merely a sufficient relaxation.

## 4. Dual subcases already paid

For vectors `u,v` on any bipartite space, local antisymmetric swaps give

`||Tr_A |u⟩⟨v|||_F²+||Tr_B |u⟩⟨v|||_F²≤||u||²||v||²+|⟨v,u⟩|²`.  (4.1)

For rank-one `R`, (4.1) directly gives the left side of (1.1) at most `3||R||²/2`, so all rank-one operators are paid.

If `rank R≤2` and `Tr R=0`, thin-SVD `R=UΣV†` and unitary-hollow the traceless 2×2 matrix `Σ^(1/2)V†UΣ^(1/2)`. The resulting two rank-one summands each have trace zero and total Frobenius/nuclear norm `||R||_1`. Applying (4.1) termwise gives

`||(Tr_3 R,Tr_2 R)||_F≤||R||_1≤√2||R||_F`.

Thus every traceless rank-two `R` is paid, in arbitrary local dimensions. The elementary 2×2 hollowing proof is: Schur the traceless matrix to `[[λ,z],[0,−λ]]` and choose a unit vector `(cosθ,e^{iφ}sinθ)` whose expectation `λ cos 2θ+(z e^{iφ}/2)sin 2θ` vanishes; its orthogonal complement has zero expectation as well.

Finally, any `R` of rank at most two with `range R=range R†` is paid. Its Hermitian parts `H=(R+R†)/2`, `K=(R−R†)/(2i)` are Hermitian and supported in the same at-most-2D subspace. For a Hermitian rank-two operator `H=λ|u⟩⟨u|+μ|v⟩⟨v|`, with `u⊥v`, define

`p_u=Tr(ρ_A(u)²)+Tr(ρ_B(u)²)≤2`, and analogously `p_v`,

`r=Tr[ρ_A(u)ρ_A(v)]+Tr[ρ_B(u)ρ_B(v)]∈[0,1]`.

The upper bound on `r` follows from the local antisymmetric-swap identity and `u⊥v`. The left side of (1.1) for `H` is

`λ²(p_u−1/2)+μ²(p_v−1/2)+2λμ(r−1/2)`

`≤(3/2)(λ²+μ²)+|λμ|≤2(λ²+μ²)=2||H||_F²`.

Partial traces of Hermitian operators remain Hermitian, so both the Frobenius norms and the trace modulus split into the sums of their H/K contributions for `R=H+iK`. This proves the equal-range/corange case. The remaining dual premise is thus genuinely **nonnormal/non-EP**, rank two and nonzero trace.

The rank condition in (1.1) cannot simply be discarded: for any nonzero traceless `C∈M2`, `R=C⊗I3` has rank at least three and gives left side `9||C||²` versus right side `6||C||²`. This is a symbolic false-stronger-premise observation, not a physical counterexample.

## 5. Scope

No proof is given for rank-two non-EP `R` with nonzero trace, and no original 2×3-support, unrestricted T2/T3/Z2/q3, f274 η-failure, physical counterexample, numerical/physical-q sample, executable, formal/kernel, stronger-family/human review, source correctness or novelty conclusion follows. The exact duality constants, tracezero complementary embedding, leakage bounds, and EP subcase require disjoint written review. Prior frozen scopes and STOP/HOLD/ZERO restrictions remain unchanged.
