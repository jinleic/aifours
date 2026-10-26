# All-reference obligation — physical reduction checkpoint001

Before-creation clock observed: **2026-10-23T15:45:51-07:00**. Owner: PhysicsResearch96h. This is an intermediate written research checkpoint, **not** a complete all-reference candidate or an isolated sector acceptance request. The frozen target remains EVERY nonzero eta in C4 tensor C4, including all zero/repeated Schmidt coefficients: `C_B-S_eta>=0` and `3C_B+S_eta>=0`, or an exact failure of that sufficient route. No scientific program/CAS/CLI/nested agent was used.

Exposure and operative scope were ACKed before this derivation in `all-reference-exposure-ack-v1.json`; parent disposition SHA `98b741bc28c9dcfdb802e0f4dfa56eee3e501d495376d627c2d2981d5bdcec2e`. The supported two-pair packet is immutable. These generic-reference formulas are newly written and unreviewed.

## 1. Full inverse and a crucial change from the paired calculation

Schmidt/unitary/scaling reduction permits

`eta=sum_i c_i|ii>`, `c_i>=0`, `x_i=c_i^2`, `sum_i x_i=1`.

For Schmidt rank at least two, define

`d_ij=1-(x_i+x_j)/2>0`, `q_i=x_i/(1-x_i)`,

`z=sum_i q_i`, `r=1/(4+z)`, `H=sum_i c_i/(1-x_i)|ii>`.

Direct expansion gives the FULL16-dimensional inverse

`A_eta=D+|eta><eta|/4`, `A_eta^-1=D^-1-r|H><H|`,

where D has diagonal d_ij. This is not an inverse on a reduced Schmidt subspace.

For every input pair,

`L_ab=delta_(ab)c_a I-(c_b E_ab tensor I+c_a I tensor E_ba)/2+|ab><eta|/4`,

`L_ab H=delta_(ab)c_a H+nu_ab|ab>`,

`nu_ab=z/4-(q_a+q_b)/2`.

**The paired proof's mixed-input cancellation no longer holds generically:** nu_ab need not vanish on off-diagonal inputs. Its rank-one inverse correction must be retained in every new phase block. Reusing the old nonzero-charge inverse truncation would be wrong.

At Schmidt rank one, D has one zero entry and this D^-1 formula is not used. A_eta itself remains invertible with `A_eta>=I/4`. Its physical matrix and S_eta depend continuously on eta. The rank-one reference is also the already-known product reference, whose one-site tensor factors give the asymmetric bounds directly. Boundary extensions below therefore refer to the actual continuous physical matrix, not divergent q_i substitutions.

## 2. Complete diagonal-phase reduction

Let each physical two-site space transform by `U tensor conjugate(U)`, U diagonal unitary. Eta is invariant. Reversed-co-Choi covariance puts the same representation on input and output, with positive slots1,3 and negative slots2,4. Thus every coordinate vector has weight

`e_(i1)+e_(i3)-e_(i2)-e_(i4)`.

The complete256-dimensional decomposition has the following blocks:

| Weight type | Number of blocks | Block dimension |
|---|---:|---:|
| `2e_a-2e_b`, a!=b |12|1|
| `e_a+e_b-2e_c`, all three distinct |12|2|
| `2e_c-e_a-e_b`, all three distinct |12|2|
| `e_a+e_b-e_c-e_d`, all four distinct |6|4|
| `e_a-e_b`, a!=b |12|12|
| zero |1|28|

The dimensions sum to256. These are reducing **coordinate** blocks with orthonormal computational bases, so there is no Gram correction. Zero or repeated Schmidt coefficients do not invalidate this subgroup decomposition.

The twelve12-dimensional blocks contain the persistent kernels `eta_input tensor |ab>_output`; the zero block contains the four diagonal-output reference kernels. This identifies known kernels only, not positivity or an exhaustive all-reference kernel classification.

## 3. Scalar blocks: explicit correction and both signs

For weight `2e_a-2e_b`, the unique coordinate vector is `|a,b,a,b>`. Both swaps fix it, so C_B=1/4. Put

`u=q_a+q_b`, `v=z-u`.

Its raw vector is

`L_ab†|ab>=-(c_a/2)|aa>-(c_b/2)|bb>+eta/4`.

The D-inverse norm squared is z/16 and its H inner product is `(v-u)/4`. Retaining the inverse correction gives

`S_scalar=z/16-r(v-u)^2/16=(z+uv)/[4(4+z)]`.

For any complementary pair of indices, **uv<=1**. If `T=x_a+x_b` is strictly between0 and1, then

`q_a+q_b<=T/(1-T)`,

`q_c+q_d<=(1-T)/T`,

because each individual denominator is at least the complementary pair mass. Multiplication proves the claim. At T=0 or1, one of the actual finite q sums is zero for Schmidt rank>=2.

Consequently

`C_B-S_scalar=(4-uv)/[4(4+z)]>0`,

and `S_scalar>=0` makes the lower asymmetric sign positive too. The actual rank-one endpoints follow by the physical continuity just specified. No matrix sampling is used.

## 4. Complete two-dimensional blocks and an all-parameter upper proof

Take distinct a,b,c and let d be the remaining label. For weight `e_a+e_b-2e_c` use

`v1=|a,c,b,c>`, `v2=|b,c,a,c>`.

The exact physical forms are

`C2=(1/2)[[1,-1/2],[-1/2,1]]`,

`S2=[[x_a/(4d_ab), beta],[beta,x_b/(4d_ab)]]`,

`beta=[(q_c+q_d+q_c q_d)-(q_a+q_b+q_a q_b)]/[4(4+z)]`.

For a direct check of the off-diagonal, its D-inverse part is `(q_c+q_d-q_a-q_b)/16`. Its correction is `-r nu_ac nu_bc`, where

`16nu_ac nu_bc=(q_d-q_c)^2-(q_a-q_b)^2`.

Combining them yields the displayed beta. Thus generic mixed-input inverse terms have not been dropped. The opposite weight is obtained by simultaneous physical-factor interchange.

### Rational probability coordinates

Put

`T=x_a+x_b`, `m=x_a x_b`, `n=x_c x_d`.

Direct cancellation of the q denominators gives

`beta=N/(4W)`,

`N=1-2T+m-n`,

`W=1+2T(1-T)+(1+T)m+(2-T)n>0`.

These expressions remain regular at rank-one probability vertices; the derivation there is interpreted by continuity of S_eta.

For fixed T,m,

`partial beta/partial n=-3(1-T+m)/(4W^2)<=0`.

Also each q_i q_j<=1 because x_i+x_j<=1; therefore `|beta|<=1/4` (strict before a rank-one limit). The two upper diagonals are nonnegative, and the off-diagonal of C2-S2 is `-1/4-beta<=0`. Hence the determinant is smallest when n=0. This is a worst-case parameter comparison, not restriction of the original reference to rank three.

### Positive polynomial certificate for that worst case

Let `v=1-T`, `A0=1+2v-2v^2`, `B0=2-v`, `d0=1+v`, `e0=3-v`. At n=0, W=A0+B0m and W+N=2vB0+e0m. After multiplying the upper determinant by its positive denominator, its numerator is

`F=4(A0+B0m)^2(2v d0+m)-d0^2(2v B0+e0m)^2`.

Its coefficients as a polynomial in m are

`F0=4v d0(1-v)(2+6v+6v^2-7v^3)`,

`F1=4[A0^2+v d0 B0(1-v)(1+7v)]`,

`F2=7+44v-46v^2-4v^3+7v^4`,

`F3=4B0^2`.

All are nonnegative for0<=v<=1. For F0, the last factor is at least `2+6v-v^2>0`. F1,F3 are plainly positive. An explicit nonnegative Bernstein expansion of F2 is

`F2=7(1-v)^4+72v(1-v)^3+128v^2(1-v)^2+64v^3(1-v)+8v^4`.

Thus F>=0 for every allowed m>=0, proving C2-S2>=0 for the **entire** two-dimensional phase family. No roots or finite evaluations substitute for this coefficient identity.

For the symmetric plus form the two diagonals are at least1/2 and its off-diagonal `-1/4+beta` has absolute value at most1/2. Diagonal dominance gives C2+S2>=0. Hence3C2+S2>=2C2>=I/2. These statements include all physical zero/repeated coefficients by the regular formulas and physical endpoint limit.

## 5. Exact four-dimensional raw form, sign still unresolved

For four distinct labels a,b,c,d, take positive labels a,b and negative labels c,d and use

`P1=|a,c,b,d>`, `P2=|b,d,a,c>`,

`P3=|a,d,b,c>`, `P4=|b,c,a,d>`.

C4 is the same swap matrix as in the earlier product-adjoint calculation:

`[[1,1/4,-1/2,-1/2],[1/4,1,-1/2,-1/2],[-1/2,-1/2,1,1/4],[-1/2,-1/2,1/4,1]]`.

For a pair i,j define

`u_ij=q_i+q_j`, `E_ij=[z+u_ij(z-u_ij)]/[4(4+z)]`.

The full raw S4 is

`[[0,-E_ac,x_a/(4d_ab),x_c/(4d_cd)],`

` [-E_ac,0,x_d/(4d_cd),x_b/(4d_ab)],`

` [x_a/(4d_ab),x_d/(4d_cd),0,-E_ad],`

` [x_c/(4d_cd),x_b/(4d_ab),-E_ad,0]]`.

The two F13F24 D-inverse edges are -z/16. Their full corrections are respectively `+r nu_ac^2` and `+r nu_ad^2`, since complementary pairs have opposite nu. These become -E_ac and -E_ad; the four single-swap edges come directly from the negative matrix-unit terms. In the old paired case some of these nu vanish, but no such cancellation is assumed here.

This table is a new generic raw identity; **neither full sign on this4x4 form is proved by this checkpoint**. Bounds on its entries or positive selected compressions do not close its Schur complement.

## 6. Literal residual and next scientific decision boundary

The generic physical reduction is now explicit for all scalar/two-dimensional blocks and for the raw four-dimensional blocks. The unresolved sufficient-route obligations remain:

- both required signs on the generic four-dimensional forms above;
- full raw derivation and both signs on every12-dimensional `e_a-e_b` block, with the persistent reference kernel retained;
- full raw derivation and both signs on the28-dimensional zero block, again retaining its four reference kernels.

No conclusion for arbitrary eta is yet claimed. No exact route-failure vector has been found in written work. This remains the SAME all-reference target, not a small region or equal-pair replacement. If a separately admitted exact falsification assay is proposed, it must reconstruct the physical full inverse and name its finite scope; a positive finite assay cannot settle these universal residuals, and a negative co-Choi form would refute this route only, not W4 itself.
