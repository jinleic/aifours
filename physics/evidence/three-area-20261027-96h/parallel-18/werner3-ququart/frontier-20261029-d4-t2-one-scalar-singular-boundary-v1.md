# The one-scalar T2 residual when its trace-hyperplane form is singular

**Status: WRITTEN, UNREVIEWED additive theorem.** This packet establishes a full-source boundary case of the one-scalar original-T2 reduction, conditional on the separately UNREVIEWED written ingredients listed below. It supersedes the earlier owner checkpoint `frontier-20261029-2243-scalar-hyperplane-singular-boundary-v1.json`, which correctly withheld the full-source lift after considering only upper local offblocks. The present proof supplies the missing lift using **both-direction** chiral offblocks; no earlier bytes or frozen review scopes are changed.

## 1. Inputs and claim

The named written inputs are:

- the full-source scalar reduction `frontier-20261029-d4-t2-traceless-dual-one-scalar-residual-v1.md`, SHA-256 4cdf23c554641ae044fd4ed3934859beda4df6ea25547edf4bcff3ab835aa3a5;
- the independent traceless rank-two dual and mixed-minor support proof / chiral operator bound in `frontier-20261029-d4-t2-traceless-dual-strict-chiral-consolidated-v2.md`, SHA-256 b96fcf9f42e0762132d7b843149f424fcde28bd978439b144f3196e09e34efb5;
- the arbitrary separately 2+2-reducing physical T2 theorem `frontier-20261029-d4-t2-arbitrary-2plus2-blocks-v1.md`, SHA-256 bb09c6bf442b9d497241297c57f9da678b559b5d13ee56cc871de4a6fc7f1473;
- the 2+2 equality classification `frontier-20261029-d4-t2-schur-coupling-universal-kernel-v1.md`, SHA-256 4a17f5a24b509528d6b4238f5adf4e7ca546e53154ff697ca0b86957f7b18ff8;
- the direct original-source product-projector inequality in `frontier-20261029-d4-t2-schur-coupling-singular-boundary-v1.md`, SHA-256 76d6ea5ef50e93619454f4190781595884d435df54746f067965b81655d2438c.

All are UNREVIEWED; their exact scopes and process restrictions are not broadened here.

For a rank-two projector `P`, let `M_P=2I−T_P†T_P` on the **full 30-complex-dimensional** traceless-pair source, `ℓ_P(A,B)=Tr[(A⊗I+I⊗B)P]`, `h_P` the Frobenius Riesz vector, and `K_P` the compression of `M_P` to `ker ℓ_P`. The scalar reduction proves `K_P⪰0`. The present claim is:

**If `h_P≠0` and `K_P` is singular, then `M_P⪰0` on the entire 30-dimensional source.**  (1.1)

Together with the separately proved `h_P=0` case and the product-projector endpoint, the scalar residual only remains for `K_P>0` and `0<||h_P||²<4`. No assertion is made about the scalar sign there, and no continuity argument from the boundary is allowed.

## 2. A nonzero kernel pair has 2D local reducing support

Take `w=(A0,B0)≠0` in `ker K_P`; put `X0=A0⊗I+I⊗B0` and `R=X0P`. Since `w∈kerℓ_P`, `R` is traceless and has rank at most two. As in the scalar reduction, equality in the traceless dual/Cauchy bound gives

`||R||_F²=2||w||²`, `Φ(R)=2w`, `||Φ(R)||=√2||R||`.

In the consolidated dual proof, the tracezero `R` is a sum of two tracezero rank-one terms with total Frobenius norm `||R||_1≤√2||R||_F`. Equality throughout forces two equal positive singular values of `R`, equality in each rank-one swap bound, and proportional identical local-partial-trace pairs for the two rank-one terms. The consolidated mixed-minor argument then forces **both** components `A0,B0` to have support on local reducing subspaces of dimension at most two.

Independently rotate the local bases and extend those supports to two-dimensional first blocks. The pair `(A0,B0)` is now separately 2+2 block diagonal. Its fixed-projector value is `Tr(PX0†X0)=2||w||²`. The arbitrary 2+2 theorem gives `S2(X0)≤2||w||²`, so this value is the top-two maximum and `P` is a maximizing rank-two projector.

## 3. Classification of P and the full-source lift

The 2+2 equality classification gives two alternatives for the nonzero pair:

1. `σ2(X0)>σ3(X0)`, so the unique maximizing `P` commutes with all four 2+2 tensor-sector projections and hence with `Γ=(I2⊕−I2)⊗(I2⊕−I2)`;
2. up to swapping local factors, one of `A0,B0` is zero and the other is traceless rank one, so every maximizing `P` is a product projector `|v⟩⟨v|⊗Q` with `rank Q=2`, or its swap.

For alternative 2, the named product-projector proof bounds the full original quadratic form for **all** traceless local matrices, so `M_P⪰0` directly.

For alternative 1, take an **arbitrary** full-source traceless pair `(A,B)` in these fixed local bases and split each factor into its 2+2 block-diagonal and **both-direction** offdiagonal parts:

`A=Ad+Ao`, `B=Bd+Bo`.

The parts are Frobenius-orthogonal, and the diagonal parts are separately traceless. Write their tensor sums `Xd` and `Xo`. `Xd` commutes with `Γ`, whereas `Xo` anticommutes with `Γ`. Since `[P,Γ]=0`,

`Tr(P Xd†Xo)=0`.

The arbitrary 2+2 theorem gives `Tr(PXd†Xd)≤2(||Ad||²+||Bd||²)`. The both-direction offdiagonal factors are locally chiral; the consolidated chiral operator theorem gives `||Xo||_op²≤||Ao||²+||Bo||²`, hence `Tr(PXo†Xo)≤2(||Ao||²+||Bo||²)`. Adding the orthogonal pieces proves

`Tr[P(Xd+Xo)†(Xd+Xo)]≤2(||A||²+||B||²)`

for every full source. Thus `M_P⪰0` in alternative 1 as well. The essential step is the BOTH-direction offdiagonal class: a proof only for strictly upper offblocks would not by itself cover the full 30-dimensional source.

## 4. Exact remaining interior

For `h_P=0`, the tracezero dual theorem already proves `M_P⪰0`. Write `ρ=Tr_B P`, `τ=Tr_A P`. Their traces are two, so

`||h_P||²=Tr(ρ²)+Tr(τ²)−2`, `6−Tr(ρ²)−Tr(τ²)=4 Tr[(P⊗P)P_-^A P_-^B]≥0`.

The lower bound `||h_P||²≥0` is immediate. Equality at the upper bound `4` forces the local-antisymmetric projector to annihilate `u⊗u` for every vector `u` in the range of `P`; Schmidt decomposition then forces every such `u` to be a product vector. A two-dimensional linear subspace consisting wholly of product vectors has a common local factor: the sum of two product vectors has Schmidt rank one only when their first factors or their second factors are parallel. Hence `P` is a product rank-two projector, and the converse is immediate from its two marginal purities. These projectors are paid by the direct product-projector proof.

Combining those exact boundaries with (1.1), the one-scalar proof only needs to establish

`δ(P)=c_P−b_P†K_P⁻¹b_P≥0`

for all rank-two projectors with `K_P>0` and `0<||h_P||²<4`. The inverse is ordinary in this remaining case. This is the **unpaid interior scalar inequality**, not a proven strictness, numerical check or claim that the interior is empty.

There is no unrestricted T2/T3/Z2/q3, optimized-η failure, physical counterexample, chosen numerical/physical q, program, independent-family/human/formal review, source correctness or novelty claim. All STOP/HOLD/ZERO and already frozen review restrictions remain in force.
