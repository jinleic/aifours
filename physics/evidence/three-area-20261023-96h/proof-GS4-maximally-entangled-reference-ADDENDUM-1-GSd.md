# Addendum 1 — a dimension-universal maximally entangled reference theorem

Before-creation clock last observed: **2026-10-23T13:07:01-07:00**. This is new **CANDIDATE written mathematics**, not an amendment to the frozen bytes or an independent acceptance of `proof-GS4-maximally-entangled-reference-v1.md`. No additional scientific program has been executed. The one earlier assay did not test every dimension.

## 1. Stronger exact statement

For every integer **d>=3**, define `Lambda_d(X)=Tr(X)I_d-X/2`, `Lambda_B=Lambda_d⊗Lambda_d`, and `Omega_d=Σ_(a=0)^(d-1)|aa>`. Set

`A_d=Lambda_B(|Omega_d><Omega_d|)`,

`L_ab=Lambda_B(|ab><Omega_d|)`,

`M_d(|ab><ef|)=L_ab A_d^(-1)L_ef†`,

`C_d=Jhat(Lambda_B)`, `S_d=Jhat(M_d)`.

**Theorem GSd (candidate):** `-C_d<=S_d<=C_d` for every d>=3.

The d=4 written theorem is a special case. The same switched-complement bridge then proves: for every finite-dimensional H1 and every rank-at-most-two complex C on `H1⊗C^d⊗C^d`, if the range or co-range contains a ray `a⊗eta` with eta maximally entangled on the two d-dimensional factors, then `q_3(C)>=0`.

The stronger co-Choi statement is **false at d=2**, with an explicit six-term vector given in Section 7. That failure does not refute the corresponding rank-two Werner statement. Arbitrary non-maximally-entangled reference vectors and unrestricted W4 remain outside this theorem.

## 2. Exact raw identity in arbitrary dimension

On four copies of C^d, retain the notation from the d=4 proof:

`A=F_13`, `B=F_24`, `F=A B`,

`C_d=(I-A/2)(I-B/2)`,

`P=P_12`, `Q=P_14`, `Qprime=P_23`,

where all Bell projectors P_ij are unnormalized. Put

`kappa=(d-1)(5d-4)`, `tau=(d-4)/4`.

Direct contraction gives

`A_d=(d-1)I+|Omega_d><Omega_d|/4`,

`A_d^(-1)=I/(d-1)-|Omega_d><Omega_d|/kappa`,

`L_ab=delta_(ab)I-(E_ab⊗I+I⊗E_ba)/2+|ab><Omega_d|/4`,

`L_ab Omega_d=delta_(ab)Omega_d+tau|ab>`.

Expanding the same matrix-unit co-Choi entries as in the frozen proof gives

`H_d=C_d P+P C_d-P+(A+B)/4+(Q+Qprime)F/4+(d-8)F/16`,

`T_d=P_12 P_34+tau(FP+PF)+tau^2 F`,

**`S_d=H_d/(d-1)-T_d/kappa`.**

To check the dimension-dependent coefficient, the four cross terms between the `-E/2` and `|ab><Omega|/4` parts contribute `-F/2`, while the final product contributes `dF/16`. Their sum is `(d-8)F/16`. The `T_d` identity follows by expanding the outer product of `L_ab Omega_d`; its two mixed terms are exactly FP and PF. At d=4, tau=0 and this reduces to the earlier raw identity.

## 3. Complete orthogonal decomposition

Let K be the sum of the four Bell-contraction ranges P_12,P_34,P_14,P_23. The four embeddings Ji(X) from the frozen proof apply with indices in `{0,...,d-1}`. On the traceless matrix space their Gram matrix is

`G_d=[[d,0,1,1],[0,d,1,1],[1,1,d,0],[1,1,0,d]]`.

The same h0,h1,h2,h3 vectors have eigenvalues `d+2,d-2,d,d`, all positive for d>=3. Thus K is the orthogonal sum of a two-dimensional identity block `span{p,q}` and `d^2-1` identical four-dimensional traceless blocks, where

`p=Omega_12⊗Omega_34`, `q=Omega_14⊗Omega_23`,

`||p||^2=||q||^2=d^2`, `<p,q>=d`.

Its dimension is `2+4(d^2-1)=4d^2-2`. All remaining `d^4-(4d^2-2)` dimensions are K-perp. The swaps permute the Bell ranges; every term of the raw identity preserves K. Thus the following three calculations cover the full space.

## 4. Complement K-perp

On K-perp the Bell terms vanish. With `N=d^2-9d+4`,

`S_d=(A+B)/(4(d-1))+N F/(4 kappa)`.

For the four joint eigenvalue sectors of the commuting involutions A,B, the two desired signs are:

| (a,b) | C_d-S_d | C_d+S_d |
|---|---|---|
| (+1,+1) | `(2d^2-5d+4)/(2 kappa)` | `d(3d-4)/(2 kappa)` |
| (+1,-1) or (-1,+1) | `(4d^2-9d+4)/kappa` | `(7d^2-9d+4)/(2 kappa)` |
| (-1,-1) | `(22d^2-31d+12)/(2 kappa)` | `(23d^2-50d+24)/(2 kappa)` |

Every denominator is positive. On putting d=x+3, x>=0, every numerator has positive coefficients, so both signs are strictly positive.

## 5. Identity block — exact sums of squares and the dimension threshold

In p,q coordinates the Gram matrix is `[[d^2,d],[d,d^2]]`. Substituting the elementary swap/Bell actions into the raw identity yields

`Form(C_d-S_d)=diag(0, d(d+1)(7d-4)/(2(5d-4)))`.

For C_d+S_d the Hermitian quadratic-form matrix is

`[[d(5d-4)/2, d(5-4d)/2],`

` [d(5-4d)/2, d(18d^2-43d+20)/(2(5d-4))]]`.

Its determinant is

`d^2(d+1)(2d-5)/4`.

Equivalently its form on coefficients alpha,beta is exactly

`[d(5d-4)/2] |alpha+[(5-4d)/(5d-4)] beta|^2`

` +[d(d+1)(2d-5)/(2(5d-4))] |beta|^2`.

Both signs are PSD for every d>=3. The second coefficient is negative at d=2, explaining why that dimension is excluded from GSd rather than hidden in a limiting argument.

For a direct check of the substitution, the co-Choi action has `S_d p=C_d p` and

`(S_d)_(qq action)=(11d^2-37d+20)/(4 kappa)`;

the off-diagonal action is fixed by self-adjointness in the displayed Gram metric. These determine the two forms above.

## 6. Traceless blocks

For a unit Hilbert–Schmidt traceless X, normalize the h0,h1,h2,h3 combinations of Ji(X) by `2sqrt(d+2),2sqrt(d-2),2sqrt(d),2sqrt(d)`. Replace the last two orthonormal vectors by their symmetric/antisymmetric combinations, called f_plus and f_minus. C_d is diagonal with entries `1/4,9/4,3/4,3/4`.

### 6.1 The minus sign

The form of C_d-S_d on coordinates z0,z1,z_plus,z_minus is exactly

`[(d-2)(9d-4)/(8 kappa)] |z0-sqrt((d+2)/(d-2)) z1|^2`

` +[(d-2)/(2(d-1))] |z_plus+sqrt(2d/(d-2)) z1|^2`

` +[(21d^2-40d+16)/(4 kappa)] |z_minus|^2`.

Every coefficient is positive for d>=3. The kernel is the expected reference contraction Ji=J2 component, rather than an unexplained numerical zero.

### 6.2 The plus sign

The f_minus scalar is

`(9d^2-14d+8)/(4 kappa)>0`.

On f0,f1,f_plus the Hermitian matrix is

`[[A0/(8 kappa), sqrt(d^2-4)(9d-4)/(8 kappa), 0],`

` [sqrt(d^2-4)(9d-4)/(8 kappa), B0/(8 kappa), -sqrt(2d(d-2))/(2(d-1))],`

` [0, -sqrt(2d(d-2))/(2(d-1)), E0/(2 kappa)]]`,

where

`A0=11d^2-14d+8`,

`B0=131d^2-306d+152`,

`E0=10d^2-13d+4`.

Its three leading principal determinants are

`Delta1=A0/(8 kappa)`,

`Delta2=p(d)/(8 kappa^2)`,

`Delta3=r(d)/(16 kappa^3)`,

with

`p(d)=170d^4-641d^3+914d^2-608d+160`,

`r(d)=p(d)(10d^2-13d+4)-(11d^2-14d+8)d(d-2)(5d-4)^2`.

Here Delta2 follows by expanding the top-left 2×2 determinant; Delta3 is Delta2 times the last diagonal entry minus the first diagonal entry times the square of the remaining off-diagonal entry. These identities expose every normalization factor.

All determinants are positive for d>=3. A0 is positive, and setting d=x+3 gives

`p(x+3)=170x^4+1399x^3+4325x^2+5929x+3025`,

`r(x+3)=1425x^6+18370x^5+98812x^4+283834x^3`

`        +459127x^2+396484x+142780`.

All coefficients are positive and x>=0. Positive square-completion pivots `Delta1,Delta2/Delta1,Delta3/Delta2` therefore prove strict positive definiteness. This is exact written polynomial algebra, not an empirical check of a finite dimension range.

Sections 4–6 prove GSd for every integer d>=3. Applying the one-site contraction and switched-complement argument from Sections 3 and 8 of the frozen d=4 proof gives the stated dimension-universal maximally-entangled-reference rank-two theorem.

## 7. Exact d=2 obstruction, separate from Werner rank two

Use the two-dimensional Bell-pair vectors

`p2=|0000>+|0011>+|1100>+|1111>`,

`q2=|0000>+|0110>+|1001>+|1111>`.

The C_2+S_2 form on their span is `[[6,-3],[-3,1]]`. Consequently the explicit vector

`w=p2+2q2`

has

**`<w,(C_2+S_2)w>=-2`.**

It has coefficients 3,1,2,2,1,3 on basis states 0000,0011,0110,1001,1100,1111, respectively. This also embeds unchanged in the r=2 two-ququart reference assay, because all its input/output indices lie in the two-dimensional reference support and the inverse restriction agrees.

This is a cleaner written obstruction to the same stronger route detected by the admitted assay's different LDL vector of value -6/17. No replay of the new w has been performed. Across the two-site input:output cut, w has coefficient matrix `|Omega_2><Omega_2|+2F_2`, of rank **four**, not at most two. It is not an admissible rank-two Werner witness. The d=2 failure therefore cannot be announced as a counterexample to W4, biseparable nonnegativity, or the published local-qubit exclusion.

## 8. Status and novelty boundary

This generalization is **CANDIDATE**, with no new independent reconstruction, finite all-d verification, kernel check or source-priority gate. Its mathematical premises are the displayed raw co-Choi identity, complete Bell-contraction decomposition, explicit sums of squares and positive polynomials. The earlier r=4 exact assay is only corroboration of that one dimension, not evidence for the universal quantifier.

The primary W4 statement for every complex 64×64 rank-at-most-two operator is unchanged and NOT PROVED. These results concern a structured reference ray. The existing ME4 prior-art screen must be refreshed/matched to this dimension-universal formulation before any novelty claim; source search misses still do not establish priority.
