# Author candidate: complete six-character actual-output decomposition

**Status.** Written prospective GENERAL AUTHOR reconstruction, not an independent review or parent disposition. The construction below proves the stated assertions at the displayed parameter scope, subject to ordinary independent mathematical checking. It is not a global PPT44, unrestricted-filter, SN3-detector, novelty, human, independent-family or formal/kernel result. A negative residual is not evidence of Schmidt number 3. No executable or verifier was prepared or run.

## 1. Actual objects, quantifiers and result

Write `ij=|i>_A tensor |j>_B` and `[v]=v v†`. Let **every** finite real `s,r` satisfy `s>1`, `r>1`, `(s−1)(r−1)>=4`. Let **every** finite `alpha,beta,gamma` be complex, with `beta != 0`, and put

    w=(alpha,beta,gamma,0)^T,  K=[I_4 | w],
    a=|alpha|²,  y=|beta|²>0,  x=|gamma|²,
    kappa=r/(r+s),  eta=s/(r+s).

In particular `kappa,eta>0`, `kappa+eta=1`. The actual positive 4-by-5 parent and its actual unnormalized 4-by-4 output are

    Q=[00+11+22]+[01+12]+[10−21]
       +s([02+34]+[32]+[04])+r([20+33]+[23]+[30]),
    R=(I tensor K) Q (I tensor K)†.

Define the actual output kets

    A=00+11+22, B=01+12, D=10−21,
    F=02+3w, H=0w, G=32, P=30, J=20+33.

All kets are in the actual output bases; `3w=alpha 30+beta 31+gamma 32` and `0w=alpha 00+beta 01+gamma 02`. Consequently, without replacing the physical output by a surrogate,

    R=[A]+[B]+[D]+s[F]+s[H]+s[G]+r[P]+r[J]+r[23].       (1)

The theorem proved below is: for all these parameters, the four-by-four residual `M` in (5) has the exact explicit Hermitian PSD test (9)–(11). Whenever `M>=0`, (7) is a finite decomposition of **this actual `R`** into rank-at-most-two pure terms; the physical normalized output is PPT and has **exact** Schmidt number 2. A sufficient phase-unrestricted condition, including equality, is

    q=x/s+a/(r+s)
      +{[1+x+x²+a(1+x)]/s+a(x+a)/r}/y <= 1.               (2)

The test `M>=0` is exact for this particular six-character residual, not asserted necessary for the existence of a different Schmidt-rank-two decomposition. The general parameters satisfying it, and in particular those satisfying (2), include genuine mixed exterior points beyond the previously retained ellipsoid and coordinate lines. Section 5 proves the exact `alpha=0` residual region, all its finite boundaries, and the separate `beta=0` gamma axis without taking a prohibited limit.

## 2. Six characters and rank of each actual ket

With `beta != 0`, define the four actual kets

    X1=(H−gamma F+gamma² G+alpha gamma P)/beta,
    X2=gamma G+kappa alpha P,
    X3=alpha(F−gamma G−alpha P)/beta,
    X4=−eta alpha G.                                       (3)

There are no conjugates in these ket coefficients. Direct substitution of the actual `F,H,G,P` gives the nontrivial cancellations

    X1=(alpha/beta)00+01−gamma 31,
    X3=(alpha/beta)02+alpha 31.                            (4)

For every one of the **six** complex roots `z^6=1`, set

    V_z=A+z D+z^−1 X1+z^−2 X2+z^−3 X3+z^−4 X4.

Its coefficient matrix, with Alice rows and Bob columns indexed `0,1,2,3`, is exactly

    [1+(alpha/beta)z^−1, z^−1,             (alpha/beta)z^−3,             0]
    [z,                   1,                  0,                            0]
    [0,                  −z,                  1,                            0]
    [kappa alpha z^−2,   alpha z^−3−gamma z^−1,
                                             gamma z^−2−eta alpha z^−4, 0].

Row 0 is `(z^−1+(alpha/beta)z^−2)` times row 1 plus `(alpha/beta)z^−3` times row 2. Row 3 is `kappa alpha z^−3` times row 1 plus `(gamma z^−2−eta alpha z^−4)` times row 2. The latter identity uses `kappa+eta=1`. Rows 1 and 2 are independent, so in fact **each `V_z` has matrix/Schmidt rank exactly 2**, for every complex parameter and every root, including `z=1`.

The exponents `0,1,−1,−2,−3,−4` are respectively `0,1,5,4,3,2` modulo 6, hence all distinct. As `conjugate(z^e)=z^(−e)`, exact character orthogonality yields

    (1/6) sum_(z^6=1) [V_z]
       =[A]+[D]+[X1]+[X2]+[X3]+[X4].                     (4a)

No numerical choice or approximation of roots is involved.

## 3. Exact actual residual and explicit Hermitian PSD test

Let `C:C^4 -> C^4 tensor C^4` have the ordered actual columns `(F,H,G,P)`. Put

    t1=(−gamma,1,gamma²,alpha gamma)^T/beta,
    t2=(0,0,gamma,kappa alpha)^T,
    t3=(alpha/beta)(1,0,−gamma,−alpha)^T,
    t4=(0,0,−eta alpha,0)^T,
    Lambda=diag(s,s,s,r),    M=Lambda−sum_(j=1)^4 t_j t_j†. (5)

Equation (3) is exactly `Xj=C t_j`. All outer products are Hermitian, `t_j t_j†`, **not** `t_j t_j^T`; neither the filter phases nor `kappa,eta` may be silently conjugated or changed. Using (1) and (4a) gives the actual-object identity

    R=(1/6) sum_(z^6=1)[V_z]+[B]+r[J]+r[23]+C M C†.       (6)

Moreover `C` is injective here: the `01` coefficient first forces the coefficient of `H` to vanish because `beta!=0`, then the `02` coefficient forces that of `F` to vanish, and the remaining `32` and `30` coefficients force those of `G,P` to vanish. Thus `M>=0` is **equivalent** to PSD of this displayed actual residual `C M C†`: `C†` is onto. Failure of this residual test has no implication for other decompositions.

If `M>=0`, its unique positive square root gives four actual kets `Psi_i=C M^(1/2)e_i`, `i=1,...,4`, and the fully positive finite identity

    R=(1/6) sum_(z^6=1)[V_z]+[B]+r[J]+r[23]
       +sum_(i=1)^4[Psi_i].                                (7)

Every `Psi_i` is supported on Alice rows 0 and 3 and hence has rank at most 2, including when the square root is singular. `B` and `J` have rank 2 and `23` rank 1. The six `V_z` have rank 2 by Section 2; every scalar weight in (7) is nonnegative.

For a fully explicit four-by-four PSD matrix, put `W=Lambda^(−1/2)[t1 t2 t3 t4]`, `G0=W†W`, and define

    L=(1+x)/s+a/r,  K0=x/s+kappa a/r.

The complete entries of the Hermitian matrix `G0=(g_ij)` are

    g11=([(1+x+x²)/s]+a x/r)/y,
    g22=x/s+kappa² a/r,    g33=a L/y,    g44=eta² a/s,
    g12=(conj(gamma)/conj(beta)) K0,
    g13=−(alpha conj(gamma)/y) L,
    g14=−eta alpha conj(gamma)²/(s conj(beta)),
    g23=−(alpha/beta) K0,
    g24=−eta alpha conj(gamma)/s,
    g34=eta a conj(gamma)/(s conj(beta)),
    gji=conj(gij) for i<j.                                  (8)

Then the complete test matrix and equivalences are

          [1−g11   −g12    −g13    −g14 ]
    E  =  [−g21    1−g22   −g23    −g24 ]
          [−g31    −g32    1−g33   −g34 ]
          [−g41    −g42    −g43    1−g44 ],                (9)

    M>=0  iff I−W W†>=0  iff E=I−W†W>=0.                 (10)

The first equivalence is congruence by the positive `Lambda^(1/2)`; the second says both matrices are PSD exactly when the largest singular value of `W` is at most one. Equivalently all 15 principal minors of the explicitly displayed Hermitian `E` are nonnegative. This is a finite exact necessary-and-sufficient test for the selected residual, also on its singular boundary.

There is no hidden phase restriction even in the sharper test. If `alpha=sqrt(a)e^(i phi)`, `beta=sqrt(y)e^(i chi)`, `gamma=sqrt(x)e^(i psi)`, choosing arbitrary phases for zero coordinates, set

    U=diag(1,e^(i(chi−psi)),e^(i(phi−psi)),
             e^(i(phi−2psi+chi))).

Entry by entry (8) gives `G0=U† G_real U`, where `G_real` is obtained from (8) by replacing `(alpha,beta,gamma)` by their nonnegative moduli. Thus the exact PSD outcome depends only on `(a,x,y,s,r)`, although (6)–(9) retain all complex phases and conjugations.

## 4. The scalar `q` region, equality and genuine exterior

The squared Frobenius norm of `W` is

    tr G0=sum_j ||Lambda^(−1/2)t_j||²
      =x/s+a(kappa²/r+eta²/s)
       +{[1+x+x²+a(1+x)]/s+a(x+a)/r}/y
      =q,                                                   (11)

where `kappa²/r+eta²/s=1/(r+s)`. For every complex vector `v`, Cauchy–Schwarz gives

    v†M v >= (1−q) v†Lambda v.                             (12)

Consequently `q<1` makes `M` positive definite and `q=1` still makes it PSD. More precisely, at `q=1` it is singular exactly when `alpha=gamma=0`: if either is nonzero, `t2` is nonzero and independent of `t1` (whose H coordinate is `1/beta`), so `W` has at least two positive squared singular values summing to 1, each strictly less than 1. In the remaining case `q=1` means `y=1/s` and `M=diag(s,0,s,r)`.

This also records the full finite equality/boundary description of the scalar certificate. Put

    d=1−x/s−a/(r+s),
    H0=[1+x+x²+a(1+x)]/s+a(x+a)/r > 0.

For `y>0`, `q<=1` **iff** `d>0` and `y>=H0/d`; equality `q=1` is exactly `y=H0/d`. If `d<=0`, no finite positive `y` satisfies the scalar certificate. No conclusion about other decompositions follows from this failure.

The retained ellipsoid is `y/s+x/(s−1)<=1`. Impose in addition `x>0` and `y/s+x/(s−1)>1`; then both `beta,gamma` are nonzero and these are genuine mixed exterior filters, outside both coordinate lines. For every admissible `s,r` and every complex `alpha` with `a<r+s`, choose any nonzero complex `gamma` with `x/s+a/(r+s)<1`; for **every** sufficiently large finite `y` and any beta phase, (2) and the strict exterior inequality hold simultaneously. For instance it suffices that

    y>max{H0/d, s[1−x/(s−1)], 0}.

Thus the result is genuinely nonempty and open in the mixed exterior for every source-region pair, without claiming every exterior point.

## 5. Exact `alpha=0` Schur region and every relevant boundary

Set `alpha=0`, retain `beta!=0`, and allow arbitrary complex `gamma`. Then `t3=t4=0` and `t2=(0,0,gamma,0)^T`. If `0<=x<s`, first subtracting `t2 t2†` leaves the positive diagonal `D0=diag(s,s,s−x,r)`. The rank-one criterion

    D0−t1 t1† >=0  iff  t1† D0^−1 t1<=1

is immediate by positive diagonal congruence. Substituting the literal `t1` gives the **exact** residual criterion

    M>=0 iff y>=Y_S(x):=(1+x)/s+x²/(s−x),   0<=x<s.       (13)

At equality `y=Y_S(x)`, `M` has rank exactly 3; for strict `y>Y_S(x)`, it is positive definite. This includes `x=0`, where `Y_S(0)=1/s`, the equality point is `y=1/s`, and the square root in (7) remains valid. For **every** finite `y>0` and `x>=s`, the G-coordinate diagonal is `s−x−x²/y<0`, including the boundary `x=s`, so this `M` is not PSD. As `x` approaches `s` from below, `Y_S(x)` diverges; there is no finite-y point silently added at `x=s`. None of these failures implies a negative Schmidt-number conclusion.

For `0<x<s`, the scalar `q<=1` specializes to `y>=Y_q(x):=(1+x+x²)/(s−x)`, and

    Y_q(x)−Y_S(x)=x(1+x)/[s(s−x)]>0.                      (14)

Thus the exact PSD test is genuinely sharper: `Y_S<=y<Y_q` has `M>=0` but `q>1`; the left endpoint is included. The exact genuinely mixed exterior part of this alpha-zero residual region is

    0<x<s,  y>=Y_S(x),  y>s[1−x/(s−1)].                    (15)

The last inequality is strict only because 'exterior' excludes the ellipsoid boundary; equality there remains covered by (13) whenever its other inequalities hold. For `x>=s−1`, the last bound is nonpositive and is automatically satisfied by `y>=Y_S>0`. The source boundary `(s−1)(r−1)=4` is included throughout; `s=1` or `r=1` is not in the quantified domain.

The character formula divides by beta, so `y=0` is **not** claimed by continuity. At `alpha=beta=0`, however, every finite complex gamma, including `x=s` and `x>s`, has a separate direct rank-two proof. For `z^5=1`, define

    T_z=z A+B−z² D+z^−1 02.

Its column 2 is `z^−1` times column 1 and column 3 is zero, so it has rank at most 2. The four used characters `1,0,2,−1` are distinct modulo 5, giving `mean_z[T_z]=[A]+[B]+[D]+[02]`. In the actual output the residual on `span{02,32}` is

    N_gamma=s[02+gamma 32]+s x[02]+s[32]−[02]
      <-> [[s(1+x)−1, s conj(gamma)],
           [s gamma,    s(1+x)]].                           (16)

Its leading diagonal is positive and its determinant is

    s[(s−1)(1+x)+s x²]>0.

Hence it is positive definite for every `x>=0`; its two square-root columns are actual product kets supported on Bob level 2. Therefore

    R=mean_z[T_z]+N_gamma+r[P]+r[J]+r[23]                  (17)

is a separate valid finite rank-at-most-two decomposition, including the origin and every `y=0` gamma-axis point. This does not extend the beta-dividing formula itself to `beta=0`.

For the other zero-coordinate boundary, `alpha=gamma=0` and every finite complex beta, the six-character Schur proof covers `y>=1/s`. The remaining interval `0<=y<=s`, including `y=0`, has a direct complementary fifth-character identity. Put `F_beta=02+beta31` and

    U_z=z A+B−z² D+z^−1 F_beta+beta z^−2 32,  z^5=1.

Column 2 is `z^−1` times column 1 and column 3 is zero; the five characters `1,0,2,−1,−2` are distinct modulo 5. Hence

    R=mean_z[U_z]+(s−1)[F_beta]+s y[01]+(s−y)[32]
       +r[P]+r[J]+r[23].                                   (18)

All weights are nonnegative on `0<=y<=s`; since `s>1`, this overlaps `y>=1/s` and proves the complete beta line including both endpoints and zero. Other `beta=0, alpha!=0` filters are not covered by the six-character formula or asserted by this axis argument.

## 6. PPT, physical normalization and exact Schmidt number

The PPT assertion follows from the actual displayed parent, not an unopened source link. Partial transpose on Bob decomposes `Q^Gamma` into scalar blocks `1,1,s,r` on `00,22,34,33`; all-ones 2-by-2 blocks with respective coefficients `1,1,s,r` on `(01,10)`, `(12,21)`, `(04,32)`, `(23,30)`; the zero block on `03,13,14,24,31`; and, in basis `(11,02,20)`,

    N=[[1,1,−1],[1,s,1],[−1,1,r]].

The Schur complement of its leading 1 is `[[s−1,2],[2,r−1]]`, PSD exactly under the displayed source inequalities. Thus `Q^Gamma>=0`, including determinant equality. The complex-filter identity is

    R^Gamma=(I tensor conj(K)) Q^Gamma (I tensor conj(K))† >=0,

not the generally incorrect unconjugated-`K` expression.

The actual trace and physical contraction are

    T=tr Q=7+4(s+r),       n=a+y+x,
    Z=tr R=7+2s(1+n)+4r,
    K_phys=K/sqrt(1+n),    rho=R/Z,
    p_success=Z/[(1+n)T].

Here `K K†=I+ww†`, so `K_phys` is a contraction. Moreover `(1+n)T−Z=2s+(7+2s+4r)n>0`, and `0<p_success<1`. Dividing (7), (17), or (18), as applicable, by `Z` gives the physical normalized positive decomposition. Both local supports have dimension 4: `[A]` supplies levels 0,1,2, while `[J]` supplies the missing level 3 on each side.

The lower bound is independent of `M`. Every vector in `range R` has a coefficient matrix of the form

    [u+alpha h, b+beta h, c+gamma h, 0]
    [d,         u,        b,         0]
    [e,        −d,        u,         k]
    [f+alpha c, beta c,   g+gamma c, e]

for complex `u,b,c,d,e,f,g,h,k`, since these are exactly the spans of the actual kets in (1). If this matrix has rank one, its minors `m1=u²+bd`, `m2=ud−be`, `m3=ue` vanish, but

    u² m1−u b m2−b² m3=u^4.

Thus every product vector in the range has `u=0`, hence zero `11` coefficient. Yet `R_(11,11)=1`. In any positive separable decomposition, each pure summand lies in `range R` because it is orthogonal to `ker R`; therefore `R` is not separable. The positive rank-at-most-two upper decomposition and this lower bound prove **exact Schmidt number 2** at every point covered by (7), (17), or (18). No claim of SN3 is made from the range argument.

The packet mentions that the original 4-by-5 parent has SN3, but its load-bearing underlying linked source bodies were not listed or opened here. A description as an SN3-to-SN2 transition therefore has the explicitly **conditional import** 'the original parent's SN3 proof and published-source identification hold at the linked prior-source boundary'; it is unnecessary for the actual-output theorem above. The exact current claims concern the displayed `Q` and `R` only.

## 7. Source coverage, process and limits

* Before body access or mathematical reasoning I read the complete manifest, freeze receipt, final pre-dispatch binding, parent live metadata, actual dispatch receipt, and all 22 manifest-listed controls as status/permissions only. Initial administratively elided displays were recovered by complete raw reads. I exclusively wrote `prebody-ack-v1.md` and then sent a direct prebody ACK to Main before opening the packet. No mathematical body or held episode/consumer was read before that ACK. Administrative hashes/roundtrip matches are parent-supplied metadata, not independent provenance or correctness certification.
* I read the sole `literal-packet-part-01-v1.md` completely and in order in raw windows `1–20`, `21–40`, `41–60`, `61–80`, `81–100`, `101–120`, `121–140`, `141–160`, `161–180`, `181–200`, `201–220`, `221–240`, `241–250`, including the terminal line. Each individual display was under 30,000 bytes: the entire parent-supplied part size is 25,182 bytes. No packet display was clipped, so no body recovery was needed. It includes complete S1 logical lines 1–191 and S2 logical lines 1–49, both terminal LF. Parent-supplied packet SHA-256 `113313a395f04d445919344cebf5da0ef74e7005bef656445a5bcd1d514f6101`; S1 `c5843b30d17031648d961d78c3da96f5c8fbf4509cdc7b8ca58bf9b97db4d352`; S2 `3f15a273f2c1d64aa1b54ff296c24133fb4c0b7245ec456e484f765f164eccf3`. I did not independently compute those hashes or open source links.
* All genuine held episodes and every proof/method/selection/planning/verification/reporting/confidence/downstream consumer remained NONINPUT; the controls were not mathematical premises. Generic memory summary and the written-math protocol were procedural inputs only. No scientific execution, tests, solvers, compilation, network, external model, child subprocess or child agent was used. No code was prepared, so there is no code hash. No new process deviation is known; no cognitive-isolation certification is claimed.
* This is an author candidate. Parent disposition and independent verification are separate. No unrestricted 4-by-4 PPT theorem, all-filter classification, assertion outside the displayed sufficient regions, arbitrary fourth-component filter, global SN3 claim, or novelty claim follows.
