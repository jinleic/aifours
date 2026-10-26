# Reference-ray bounds for the three-copy Werner endpoint

## Version and assurance boundary

**Version 2; written research manuscript, not a publication or full W4 solution.** Before-creation clock observed: **2026-10-23T13:31:39-07:00**. This consolidates immutable source manuscripts without changing their bytes:

- ME4 proof: `proof-GS4-maximally-entangled-reference-v1.md`, SHA `684ec10f7b7ab25bf0331fdbe9f660ffbfc195c37581addd36d14cf1228debb5`.
- GSd proof: `proof-GS4-maximally-entangled-reference-ADDENDUM-1-GSd.md`, SHA `c51a4c9d0665d37d91bd325b6e9771c4591207ffb44eac92beeeadbe7664ff4b`.
- Equality proof: `proof-GS4-maximally-entangled-reference-ADDENDUM-2-equality.md`, SHA `e6d88e639507904fc1d87fb2a515f5f02d9bbba6ff9e1e696583c74dd74e5202`.
- New embedded-reference proof: `proof-GS-Omega3-embedded-ququarts-v1.md`, SHA `89ea513a8c467b39d9e4509ddaf47469281ab8b5a89a60a153a4f32ada32ee8c`.
- New angle obstructions: `proof-reference-angle-obstructions-v1.md`, SHA `ccb579da080fcfba43c44dafbb7aa8511f989d33696c36193736ec5105abde84`.

At this freeze, the first three have ordinary independent in-harness written reconstructions with **0F/0M/0m**; the equality statement is conditional on the GSd matrices, as its review expressly states. The embedded Omega3 proof and angle obstructions are **CANDIDATE, pending independent reconstruction**. This newly assembled v2 has not itself received an integration review. No human review, kernel/formal verification or novelty clearance is claimed.

## Abstract

We study a structured part of the rank-two partial-trace inequality equivalent to three-copy Werner endpoint undistillability. An explicit co-Choi domination holds for a maximally entangled reference on two equal d-dimensional factors, for every integer d>=3. It supplies nonnegativity for every complex rank-at-most-two coefficient operator whose range or co-range contains a corresponding biseparable reference ray, without assuming factorization of the other ray. Within that family all nonzero equality cases are exactly an orthogonal rank-two projection on the first factor tensored with a rank-one operator having the reference as its range. A further written calculation treats the rank-three uniform reference embedded in two ququarts. Conversely, explicit rational co-Choi obstructions with Schmidt-rank-three and full-rank-four references show that Schmidt rank alone cannot characterize the same domination. These are structured-reference results, not a proof of unrestricted three-ququart nonnegativity or asymptotic NPT bound entanglement. Priority remains unresolved.

## 1. Problem, book relationship and prior scope

The physics-volume article *Quantum Channel* by Zhou Xiangfa and Guo Guangcan, book pp.591–592 / PDF pp.626–627, discusses the role of entanglement and auxiliary resources in quantum communication and the difficulty of regularized capacity questions. The retained unedited excerpt is `physics/evidence/physics-hard-20261015/sources/phys-p0591/excerpt.txt`; `books/README.md` identifies the copyrighted local PDF. The present finite-copy resource question is related to, **not equivalent to**, the full book article.

For finite-dimensional complex H1,H2,H3 set

`q3(C)=||C||_HS^2-(1/2)Σ_i||Tr_i C||_HS^2+(1/4)Σ_(i<j)||Tr_ij C||_HS^2-(1/8)|Tr C|^2`.

All partial traces are unnormalized, on the coefficient operator itself, not on CC†. For the Werner state

`rho_alpha^(d)=(I+alpha F)/(d^2+alpha d)`,

vectorization and expansion of `F^Gamma=|Omega_d><Omega_d|` give

`<vec C,((rho_alpha^(d))^Gamma)^(⊗3)vec C>=q3(alpha,C)/(d^2+alpha d)^3`.

At alpha=-1/2 the numerator is q3(C), and rank C is the Schmidt rank of vec C across the grouped output:input cut. The frozen primary W4 question is **q3(C)>=0 for every complex 64×64 operator of rank at most two**. It remains NOT PROVED here.

Wu–Zou [1] treats the normal rank-two sector, a local-support-overlap sector, fully product reference rays and additional closed nonnormal classes. Its Theorem7.3 explicitly requires a fully product ray. Its one-site switched-complement argument is prior art. ULAM's structured multicopy theorem [2] is stronger than operator tensor factorization: it handles two coherent rank-one terms with a common admissible block-product structure. Neither hypothesis covers a generic second ray paired with the entangled reference studied here. An October4 unrefereed public candidate [3] claims unrestricted three-copy **qutrit** nonnegativity and explicitly excludes unrestricted higher dimensions; its certificate has not been replayed here and its qutrit conclusion is not presented as our discovery.

## 2. Statements

Define `Lambda_V(X)=Tr(X)I_V-X/2` and the co-Choi convention

`Jhat(E)=Σ_(a,b)|b><a|⊗E(|a><b|)`.

For a nonzero two-site reference eta, set

`A_eta=(Lambda_2⊗Lambda_3)(|eta><eta|)`,

`L_i=(Lambda_2⊗Lambda_3)(|i><eta|)`,

`M_eta(|i><j|)=L_i A_eta^(-1)L_j†`,

`C_B=Jhat(Lambda_2⊗Lambda_3)`, `S_eta=Jhat(M_eta)`.

The inverse exists: the product swap matrix `R_B=⊗_(i=2,3)(I-F_i/2)` has minimum eigenvalue1/4, so its reference compression A_eta is at least `||eta||^2 I/4`.

### Theorem A: uniform full-rank co-Choi domination — WRITTEN_CHECKED components

For every integer d>=3, on two d-dimensional factors with `eta=Omega_d=Σ_a|aa>`,

`C_B-S_eta>=0`, `C_B+S_eta>0`,

`ker(C_B-S_eta)=span{Omega_d}_input⊗B_output`.

The proof below is written and dimension-universal. The earlier four-dimensional exact assay is not a premise for the quantifier over d.

### Theorem B: reference-ray endpoint inequality and equality cases

Let H1 be any finite-dimensional complex space. If rank C<=2 on `H1⊗C^d⊗C^d`, d>=3, and its range contains a ray `a⊗eta` with eta maximally entangled, then q3(C)>=0. It is strict unless the nonzero operator has the exact form

`C=P_E⊗|eta><w|`,

where P_E is an orthogonal rank-two projection on H1 and w is nonzero. These and only these are the nonzero zero cases within this range-reference family. The co-range version consists of the adjoints. No nonzero zero case exists if dim H1<2.

### Theorem C: rank-three uniform reference in two ququarts — CANDIDATE

For `eta=|00>+|11>+|22>` in `C^4⊗C^4`, the same two signs and exact kernel in Theorem A hold, with B_output the full16-dimensional space. Consequently Theorem B and its equality argument also apply to this embedded reference class. Equal nonzero Schmidt coefficients are essential to the stated theorem; arbitrary rank-three references are not included.

### Theorem D: rank alone is insufficient — CANDIDATE exact obstructions

For the fixed co-Choi vector `w=p2+2q2`, where

`p2=|0000>+|0011>+|1100>+|1111>`,

`q2=|0000>+|0110>+|1001>+|1111>`,

one has negative C_B+S_eta values

`-58384/54689` for `eta=(1,1,1/4,0)`,

`-74/289` for `eta=(1,1,1/4,1/4)`.

The tuples specify diagonal Schmidt coefficients before normalization. The same w at `eta=(1,1,0,0)` has value -2. Across input:output, w has coefficient rank four, so none of these is a negative rank-two Werner witness. The full-rank negative example and uniform Omega4 positive theorem rule out a rank-only characterization decisively.

## 3. The switched-complement bridge

Put `R=⊗_(i=1)^3(I-F_i/2)`. For output rays u,x define

`A=(<u|⊗I)R(|u>⊗I)`, `L=(<u|⊗I)R(|x>⊗I)`, `D=(<x|⊗I)R(|x>⊗I)`.

The correctly polarized identity is

`q3(|u><v|+|x><y|)=<v,Av>+<y,Dy>+2 Re<y,Lv>`.

It follows by expanding each local swap; the eight contractions are exactly the eight partial traces. The required complement is **D-L A^-1 L†**, not the ordinary compression's D-L† A^-1 L.

For the first-site reference |0>, define `A0=I-|0><0|/2`, `ell_a=delta_(a0)I-|a><0|/2`, and `M0(E_ab)=ell_a A0^-1 ell_b†`. Let C0,S0 be their co-Choi matrices. On |00>, C0=S0=1/2; on each span{|0a>,|a0>},

`C0=[[1,-1/2],[-1/2,1]]`, `S0=[[1,-1/2],[-1/2,0]]`;

on Q⊗Q they are I-F_Q/2 and F_Q/2. Therefore C0-S0>=0 and C0+S0>0.

If a two-site reference has `-C_B<=S_eta<=C_B`, then both normalized matrices `T0=C0^-1/2 S0 C0^-1/2` and `TB=C_B^-1/2 S_eta C_B^-1/2` are Hermitian contractions. Hence `I-T0⊗TB>=0`. Positive congruence says `Lambda_1⊗Lambda_B-M0⊗M_eta` is completely copositive, and thus positive. Applying it to |x><x| is precisely the full switched complement for `u=|0>⊗eta` because the reference inverse factors. The square completion

`q3(C)=||A^(1/2)(v+A^-1 L†y)||^2+<y,(D-L A^-1 L†)y>`

proves nonnegativity. Arbitrary covectors v,y are allowed. Local-unitary covariance and adjoint invariance give the stated transports. No general tensorization of positive maps and no preservation of rank under partial trace is assumed.

## 4. Proof of Theorem A in every d>=3

### 4.1 Raw identity

Use four slots, with input pair1,2 and output pair3,4. Set

`A=F_13`, `B=F_24`, `F=A B`,

`C=(I-A/2)(I-B/2)`, `P=P_12`, `Q=P_14`, `Q'=P_23`,

where P_ij is the unnormalized Bell projector on slots i,j, tensored with identity elsewhere. Let `kappa=(d-1)(5d-4)`, `tau=(d-4)/4`. Directly

`A_eta=(d-1)I+|Omega><Omega|/4`,

`A_eta^-1=I/(d-1)-|Omega><Omega|/kappa`,

`L_ab=delta_(ab)I-(E_ab⊗I+I⊗E_ba)/2+|ab><Omega|/4`,

`L_ab Omega=delta_(ab)Omega+tau|ab>`.

For the co-Choi input reversal,

`S_((ab,cd),(ef,gh))=<L_ef†cd,A_eta^-1 L_ab†gh>`.

Expanding the four terms of each vector gives the exact identity

`H=CP+PC-P+(A+B)/4+(Q+Q')F/4+(d-8)F/16`,

`T=P_12 P_34+tau(FP+PF)+tau^2 F`,

**`S=H/(d-1)-T/kappa`.**

The four negative/Bell products contribute -F/2, while the Bell/Bell product contributes dF/16. The rank-one inverse term is T, from the displayed L_ab Omega identity. These observations independently expose the dimension-sensitive coefficients and the co-Choi convention.

### 4.2 Complete Bell-contraction decomposition

Let K be the sum of the four ranges P_12,P_34,P_14,P_23. The swaps permute these ranges, so K and K-perp reduce both matrices. For X in M_d(C) define

`J1(X)_(abcd)=X_ab delta_(cd)`,

`J2(X)_(abcd)=delta_(ab)X_cd`,

`J3(X)_(abcd)=X_ad delta_(bc)`,

`J4(X)_(abcd)=X_cb delta_(ad)`.

These embeddings span K. On traceless X,Y their Gram matrix is

`G=[[d,0,1,1],[0,d,1,1],[1,1,d,0],[1,1,0,d]] Tr(X†Y)`.

The orthogonal coefficient vectors

`h0=(1,1,1,1)`, `h1=(1,1,-1,-1)`,

`h2=(1,-1,1,-1)`, `h3=(1,-1,-1,1)`

have Gram eigenvalues `d+2,d-2,d,d`. Identity components give p,p,q,q, with `p=Omega12 Omega34`, `q=Omega14 Omega23`, Gram `[[d^2,d],[d,d^2]]`. They are orthogonal to the traceless components. Thus K consists of one two-dimensional identity block and d^2-1 independent four-dimensional traceless blocks, dimension4d^2-2; nothing is omitted.

### 4.3 K-perp and the identity block

On K-perp,

`S=(A+B)/(4(d-1))+(d^2-9d+4)F/(4kappa)`.

The joint swap sectors yield:

| (A,B) | C-S | C+S |
|---|---|---|
| (+,+) | `(2d^2-5d+4)/(2kappa)` | `d(3d-4)/(2kappa)` |
| (+,-),(-,+) | `(4d^2-9d+4)/kappa` | `(7d^2-9d+4)/(2kappa)` |
| (-,-) | `(22d^2-31d+12)/(2kappa)` | `(23d^2-50d+24)/(2kappa)` |

All are positive for d>=3, as seen by shifting d=x+3.

In p,q coordinates the minus form is

`[d(d+1)(7d-4)/(2(5d-4))]|beta|^2`.

The plus form is

`[d(5d-4)/2]|alpha+[(5-4d)/(5d-4)]beta|^2`

`+[d(d+1)(2d-5)/(2(5d-4))]|beta|^2`.

Both signs therefore have the asserted positivity; the minus kernel here is exactly p. At d=2 the second plus coefficient is negative, producing Theorem D's limiting obstruction rather than a hidden extension to d=2.

### 4.4 Traceless blocks: complete certificates

Normalize J(h_i) by `2sqrt(d+2),2sqrt(d-2),2sqrt(d),2sqrt(d)` to obtain orthonormal f0,f1,f2,f3, and set f_plus=(f2+f3)/sqrt2, f_minus=(f2-f3)/sqrt2. C is diagonal with entries1/4,9/4,3/4,3/4. The minus quadratic form is exactly

`[(d-2)(9d-4)/(8kappa)]|z0-sqrt((d+2)/(d-2))z1|^2`

`+[(d-2)/(2(d-1))]|z_plus+sqrt(2d/(d-2))z1|^2`

`+[(21d^2-40d+16)/(4kappa)]|z_minus|^2`.

Every coefficient is positive. Its sole kernel direction is J2(X).

For the plus sign, the f_minus scalar is `(9d^2-14d+8)/(4kappa)>0`. On f0,f1,f_plus the matrix is

`[[A0/(8kappa),sqrt(d^2-4)(9d-4)/(8kappa),0],`

` [sqrt(d^2-4)(9d-4)/(8kappa),B0/(8kappa),-sqrt(2d(d-2))/(2(d-1))],`

` [0,-sqrt(2d(d-2))/(2(d-1)),E0/(2kappa)]]`,

with `A0=11d^2-14d+8`, `B0=131d^2-306d+152`, `E0=10d^2-13d+4`. Its leading determinants are

`Delta1=A0/(8kappa)`, `Delta2=p(d)/(8kappa^2)`, `Delta3=r(d)/(16kappa^3)`,

`p(d)=170d^4-641d^3+914d^2-608d+160`,

`r(d)=p(d)E0-A0 d(d-2)(5d-4)^2`.

Their positive polynomial certificates, for d=x+3, are

`A0=11x^2+52x+65`,

`p=170x^4+1399x^3+4325x^2+5929x+3025`,

`r=1425x^6+18370x^5+98812x^4+283834x^3+459127x^2+396484x+142780`.

Thus the square-completion pivots Delta1,Delta2/Delta1,Delta3/Delta2 are positive. This proves Theorem A and strict positivity of C+S. The minus kernel is p plus J2(X) for all traceless X, exactly `Omega_input⊗B_output`.

## 5. Strictness and all equality cases

Because the plus signs for the first-site and two-site pairs are strictly positive, their normalized contractions have spectra in (-1,1]. A tensor-product eigenvalue can equal one only when both factors equal one. Undoing the congruence gives

`ker(C0⊗C_B-S0⊗S_eta)=ker(C0-S0)⊗ker(C_B-S_eta)`.

Every vector there has its two-site input component in span{eta}. For any linear map E with the co-Choi convention,

`<z,E(|x><x|)z>=<x⊗z,Jhat(E)(x⊗z)>`.

Consequently the switched defect is positive definite for every x outside `H1⊗eta`, since x⊗z cannot enter that kernel for nonzero z. The square completion in Section3 proves strict q3>0 whenever the reference-ray range is not wholly contained in that common-reference subspace. Rank-one nonzero cases are strict by the product-swap lower bound `q3(C)>=||C||^2/8`.

For the remaining common-reference range, choose a first-site output basis a0,a1 and write

`C=Σ_(alpha=0)^1 |a_alpha⊗eta><v_alpha|`, `v_alpha=Σ_i |a_i>⊗v_(alpha,i)`.

With `A_eta=Lambda_B(|eta><eta|)>0` and `||v||_A^2=<v,A_eta v>`, the exact first-slot block trace identity is

`q3(C)=Σ_(alpha,i)||v_(alpha,i)||_A^2-(1/2)||v_(0,0)+v_(1,1)||_A^2`

`=(1/2)||v_(0,0)-v_(1,1)||_A^2+Σ_off-diagonal||v_(alpha,i)||_A^2`.

Thus equality forces exactly one common diagonal vector w and all off-diagonal vectors zero, giving P_E⊗|eta><w|. Conversely its first-site factor has `q1(P_E)=2-4/2=0`, so every such operator is zero. This proves both directions of Theorem B. The argument also applies verbatim to any other reference for which the same strict plus sign and exact minus kernel are proved.

## 6. Proof of the embedded Omega3 statement

This section consolidates the new candidate calculation. Use the inside subspace P=span{0,1,2}, outside label o=3 and eta=Omega3. The exact inverse is

`A_eta^-1=I/2-|Omega3><Omega3|/22` on P⊗P,

`A_eta^-1=2I/5` on P⊗o and o⊗P,

`A_eta^-1=1/3` on o⊗o.

For i,j inside,

`L_ij=delta_(ij)I-(E_ij⊗I+I⊗E_ji)/2+|ij><Omega3|/4`,

`L_oi=-E_oi⊗I/2+|oi><Omega3|/4`,

`L_io=-I⊗E_oi/2+|io><Omega3|/4`, `L_oo=|oo><Omega3|/4`.

Covariance under independent outside-level phases gives nine orthogonal sectors, according to outside counts among slots1,3 and slots2,4. Their dimensions are81;54,54;9,9;36;6,6;1, totaling256. Physical factor interchange identifies the paired sectors.

### 6.1 Sectors with zero, three or four outside labels, or a whole outside pair

The all-inside 81-dimensional sector is exactly Theorem A at d=3. The all-outside scalar is C=1/4,S=3/44, giving minus/plus2/11,7/22.

When a whole first-site pair is outside and the second pair is inside, with T the inside swap,

`C=I/2-T/4`, `S=I/8-3T/88`.

The minus/plus eigenvalues are7/44,15/44 for T=+1 and13/22,10/11 for T=-1. For a three-outside sector, basis `|o,o,o,i>,|o,i,o,o>`,

`C=[[1/2,-1/4],[-1/4,1/2]]`, `S=[[0,1/44],[1/44,1/10]]`.

The minus/plus determinants are76/605 and601/2420, with positive first pivots. All these sectors are strictly positive in both signs.

### 6.2 One outside label at each physical site

For internal i,j inside, use four orientations

`A_ij=|o,o,i,j>`, `B_ij=|o,j,i,o>`, `C_ij=|i,o,o,j>`, `D_ij=|i,j,o,o>`.

The orientation C_B matrix is

`[[1,-1/2,-1/2,1/4],[-1/2,1,1/4,-1/2],[-1/2,1/4,1,-1/2],[1/4,-1/2,-1/2,1]]`.

Let Pi=|Omega3><Omega3| on the internal pair. The exact co-Choi contractions give

`S=[[0,0,0,Pi/11-I/44],`

`   [0,0,Pi/8-3I/88,I/10-Pi/5],`

`   [0,Pi/8-3I/88,0,I/10-Pi/5],`

`   [Pi/11-I/44,I/10-Pi/5,I/10-Pi/5,Pi/3]]`.

On Pi=3, the B-C antisymmetric minus/plus scalars are12/11,9/22. The minus remaining block has one zero D direction and the positive matrix `[[1,-1/sqrt2],[-1/sqrt2,10/11]]`, determinant9/22. For the plus remaining block

`[[1,-1/sqrt2,1/2],[-1/sqrt2,35/22,-sqrt2],[1/2,-sqrt2,2]]`,

the first Schur complement has diagonals12/11,7/4, off-diagonal -3/(2sqrt2), determinant69/88.

On each Pi=0 internal direction the antisymmetric scalars are63/88,69/88. The remaining minus/plus matrices are

`[[1,-1/sqrt2,3/11],[-1/sqrt2,113/88,-3sqrt2/5],[3/11,-3sqrt2/5,1]]`,

`[[1,-1/sqrt2,5/22],[-1/sqrt2,107/88,-2sqrt2/5],[5/22,-2sqrt2/5,1]]`.

After the first pivot their Schur diagonals/off-diagonals are respectively `(69/88,112/121,-51sqrt2/110)` and `(63/88,459/484,-63sqrt2/220)`. Determinants19689/66550 and548289/1064800 are positive. This covers all36 dimensions.

### 6.3 One outside label only

Use orientations `X_ijk=|o,j,i,k>`, `Y_ijk=|i,j,o,k>`. Let T swap internal j,k and J exchange orientations. Then C=(I-J/2)(I-T/2). On the27-dimensional internal space define

`U1(v)=Σ_a|a,a,v>`, `U2(v)=Σ_a|a,v,a>`,

`P1=U1U1†`, `K12=U1U2†`, `K21=U2U1†`.

The exact blocks are

`S_XX=0`,

`S_YY=(2/5)[P1-(K12+K21)/2+T/4]`,

`S_XY=I/8-P1/4+K12/8+5K21/44-T/11`, `S_YX=S_XY†`.

For clarity, the inside inverse sends `-|jn>/2+delta_(jn)Omega3/4` to `-|jn>/4+(5/44)delta_(jn)Omega3`, giving the X-Y block; the Y-Y block uses the distinct inverse2/5.

The two U ranges have Gram `[[3,1],[1,3]]⊗I3` and dimension6. On their21-dimensional complement, each T eigenvalue epsilon gives orientation matrices

`C=(1-epsilon/2)[[1,-1/2],[-1/2,1]]`,

`S=[[0,1/8-epsilon/11],[1/8-epsilon/11,epsilon/10]]`.

The four sign/epsilon determinants are4619/38720,9811/38720,56803/38720,70267/38720, all with positive pivots.

On each of the three U-range blocks, the **quadratic-form** matrices in XU1,XU2,YU1,YU2 coordinates are

`Minus=[[5/2,-1/2,0,-1/11],[-1/2,5/2,0,-2],[0,0,0,0],[-1/11,-2,0,16/5]]`,

`Plus =[[5/2,-1/2,-5/2,13/22],[-1/2,5/2,1/2,-1/2],[-5/2,1/2,5,-1],[13/22,-1/2,-1,9/5]]`.

The upper-left block has inverse `[[5/12,1/12],[1/12,5/12]]`. The minus residual is one zero YU1 direction and positive scalar3629/2420. The plus residual is `[[5/2,-9/22],[-9/22,3871/2420]]`, determinant3709/968. This covers each54-dimensional one-outside sector completely.

The only minus kernels are dimensions9,3,3,1 in the all-inside, one-outside and two-outside-output sectors. They are exactly eta_input⊗B_output. Every plus sector is strictly positive. This completes Theorem C by written algebra, not by citing assay positivity as a proof.

## 7. Exact Schmidt-angle obstructions

Consider `eta=|00>+|11>+t|22>+u|33>`, t,u>=0. Put

`a=1+t^2+u^2`, `z=2/a+t^2/(2+u^2)+u^2/(2+t^2)`.

Writing the reference compression as `A_eta=D+|eta><eta|/4`, where `D_(ab)=2+t^2+u^2-(c_a^2+c_b^2)/2`, c=(1,1,t,u), gives

`A_eta^-1=D^-1-|D^-1 eta><D^-1 eta|/(4+z)`.

On the two vectors p2,q2 in Theorem D, direct contractions yield

`<p2,S p2>=[z+(16+2z)/a-4/a^2]/(4+z)`,

`<p2,S q2>=[z/2-(4+2z)/a-2/a^2]/(4+z)`,

`<q2,S q2>=[z-(8+z)/a-4/a^2]/(4+z)`.

The C_B quadratic-form matrix there is `[[3,-3/2],[-3/2,3]]`. Therefore

**`<p2+2q2,(C_B+S)(p2+2q2)>=[36+16z-(32+10z)/a-28/a^2]/(4+z)`.**

The coefficients are derived using the full inverse, including the outside reference components, not by truncating the physical Hilbert space.

For u=0,s=t^2, this value is

`2(8s^3+47s^2+75s-12)/[(s+1)(s^2+9s+12)]`.

At s=1/16 it is -58384/54689. The numerator is strictly increasing for s>=0, so its unique positive root is an exact threshold for this one witness only.

For t=u,s=t^2, the value is

`(2/3)(34s^3+65s^2+36s-3)/[(1+2s)(1+s)^2]`.

At s=1/16 it is -74/289, whereas at s=1 it is22/3 for the uniform Omega4 reference. Again the numerator is strictly increasing. These scalar necessary conditions are **not sufficient** for complete GS; other co-Choi directions may impose further restrictions.

The coefficient matrix of w=p2+2q2 is `|Omega2><Omega2|+2F2`, eigenvalues4,2,2,-2, hence rank4. This explicitly prevents conflating a co-Choi-route failure with a rank-two distillation witness. Continuity also shows failure occurs on open angular regions near the rank-two balanced reference; positivity cannot depend only on nonzero-coefficient counts.

## 8. Strict coverage beyond the named source sectors

Let

`u=|0>⊗Phi4`, `x=(|100>+|211>+|322>)/sqrt3`,

`v=|1>⊗Phi4`, `y=(|200>+|311>+|022>)/sqrt3`,

`C=|u><v|+|x><y|`.

Both pairs are orthonormal and the range/co-range planes differ, so C is rank2 and nonnormal. Every one-site support on each side is C^4. Neither plane contains a fully product ray: across1:23 every combination with a nonzero x (or y) coefficient has Schmidt rank at least3, while the remaining reference ray is entangled on2:3. No local partial trace vanishes.

The eight squared partial-trace norms, ordered by empty,1,2,3,12,13,23,123, are

`2, 2/9, 7/12, 7/12, 0, 0, 4/3, 0`,

giving q3=59/36. This is calibration, not a new negative witness.

The example also escapes the stronger common block-product theorem [2] under **any** two-term rank-one decomposition. Across1:23 its range has only one biseparable ray; across2:13 or3:12 the reference has Schmidt rank4, impossible in a span of two cut-product vectors. Thus rotating a degenerate SVD cannot supply the missing common-cut output basis. The larger locally orthogonal product-code envelope is likewise impossible: in such a code, a vector product across1:23 must use one code ray and therefore be fully product, contrary to |0>⊗Phi4. These are strict hypothesis comparisons, not worldwide novelty certificates.

## 9. Exact assay, review coverage and remaining obligations

One scientific program ran under the named parent GO `physics-gs4-exact-001-GO-v1.json`: fixed d=4, reference ranks1,2,3,4, exact rational arithmetic, 55 torus blocks per sign, internal180-second bound. It exited0 in about2.13 seconds of program time. PID=PGID6412 and its absence after wait are recorded in lane-local launch/settlement receipts. Its source SHA is `171171107cf9922d949c29353198b0f8589289aecc49bdcb361ce5683cee72a9`; receipt SHA is `e46c79184dcf1652b1be17034d23fd1059e70fe3b5fb27fc8a22c5da57f236ec`.

The assay gives r1,r3,r4 PSD in both signs; r2 C+S has a rational negative vector of value-6/17. It is one encoding/checker and not an independent physical-model reconstruction. There has been no scientific retry, additional probe, CLI review, formal run or all-d computation.

Independent written reviews are in the mathematics lane: `peer-review-physics-ME4-v1.md`, `peer-review-physics-GSd-addendum-v1.md`, and `peer-review-physics-GSd-equality-v1.md`. Their reviewed source pins and bounded findings remain operative. The parent's ME4 written-check verdict is cited by path/content, not by its estimated timestamp; `parent-timestamp-erratum-v1.md` corrects the affected parent-authored clock labels. This paper's own observation above is separate.

New obligations are exact and not silently weakened:

1. independently reconstruct this consolidated v2, especially the new embedded-Omega3 sectors and nonuniform obstructions;
2. characterize the Schmidt coefficient regions satisfying the **full** co-Choi domination, not only the scalar witness inequalities;
3. distinguish any failure of that route from the underlying rank-two endpoint inequality;
4. return to unrestricted W4 with a genuinely new input, since generic two-planes need not contain any of the reference rays treated here;
5. complete a matched primary-art/priority audit before claiming novelty or publication readiness.

## References and provenance

[1] Wu–Zou, *Sharp Plucker Geometry for Three-Copy Werner Distillation*, [arXiv:2608.02647v1](https://arxiv.org/html/2608.02647v1), 31 July2026. Retained full source text SHA `14c6b3a89eceab623fa7af079b930e4045695f7a0c73bd43380d5a87e099db99`.

[2] ULAM.AI, [*Structured Multicopy Werner Bounds*](https://www.ulam.ai/archive/structured_multicopy_werner_bounds.pdf), archive date29 July2026; and [*Obstructions to Werner Distillation*](https://www.ulam.ai/archive/obstructions_to_werner_distillation.pdf), 31 July2026. Directly read primary manuscripts; their model-review labels are not human authentication. The two-copy spectral-gap note is also prior work, not the present contribution.

[3] Anonymous, [*Three-copy qutrit Werner undistillability*](https://raw.githubusercontent.com/ipitchford/three-copy-werner-undistillability/main/paper.md), version1.1.0-candidate, 4 October2026; statement and setup read, no certificate replay or acceptance here.

[4] Bharti–Gajjala–Haug, [arXiv:2607.24479v1](https://arxiv.org/html/2607.24479v1), two-copy theorem and finite-copy formulations. The present argument does not infer unrestricted three copies by partial-trace induction.

The two lane-local prior-art screens document actual arXiv, INSPIRE, public archive, EulerSolve and openai/math contents checks, their read scopes and access limits. They support **NOVELTY_UNCLEAR**, not absence of prior art. No full-book solution, every-alpha threshold, all-copy NPT result, human review, kernel proof or first-priority claim is made.
