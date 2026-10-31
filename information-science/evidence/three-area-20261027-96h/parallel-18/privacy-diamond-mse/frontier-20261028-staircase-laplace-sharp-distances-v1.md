# Sharp high-privacy distances: diamond staircases versus product Laplace

**AUTHOR CANDIDATE — WRITTEN with separately disclosed Decimal diagnostics; NOT independently reviewed or parent-adopted.** Native pre-write observation: `Wed Oct 28 20:01:03 PDT 2026`.

## 1. Actual laws and exact max divergences

Fix epsilon>0, b=e^(-epsilon), m=b/(1-b), and any gamma in [0,1]. Let P_gamma be the ACTUAL full-D-private centered diamond staircase of offset gamma,

    p_gamma(x)=b^(max(0,ceil(||x||_1-gamma)))/Z_gamma,
    Z_gamma=2D_gamma,  D_gamma=gamma^2+2m gamma+m+2m^2,

and let Q be the ACTUAL full-D-private product Laplace with density `(epsilon^2/4)e^(-epsilon||x||_1)`. Set

    A=2/(epsilon^2 D_gamma).

Their exact directed max divergences are

    D_infinity(P_gamma||Q)=log A+epsilon gamma,
    D_infinity(Q||P_gamma)=-log A+epsilon(1-gamma),
    D_infinity(P_gamma||Q)+D_infinity(Q||P_gamma)=epsilon.               (1)

These identities hold for EVERY epsilon>0 and EVERY gamma in [0,1], not only an optimizer.

As epsilon->0, uniformly for ALL gamma(epsilon) in [0,1], the written asymptotics are

    D_infinity(P_gamma||Q)=epsilon/2-epsilon^2/24+O(epsilon^3),
    D_infinity(Q||P_gamma)=epsilon/2+epsilon^2/24+O(epsilon^3),
    TV(P_gamma,Q)=epsilon/8+O(epsilon^2),                                 (2)
    D_alpha(P_gamma||Q)=D_alpha(Q||P_gamma)
       =alpha epsilon^2/24+O_alpha(epsilon^3)  for every FIXED 0<alpha<infinity. (3)

In (3) the equality means both divergences have the displayed common expansion, not that they are exactly equal at finite epsilon. Alpha=1 means KL. The O_alpha constant may depend on alpha but is uniform in gamma.

The construction and claims (1)–(3) import NO optimizer theorem. If the separately pinned parent-v253 identification is accepted, then for sufficiently small epsilon they apply in particular to the actual original J optimizer; if the parent MDA alternative is accepted, they also apply to the actual first-norm optimizer. Those optimizer identifications are conditional additions only. This behavior does NOT extend to all first-order-nearopt laws: the separately pinned unreviewed `frontier-20261028-high-privacy-density-renyi-topology-v1.md`, SHA-256 `924c9048e94db579048847f5dda33a492cef81932936660eb9686fc69b438308`, constructs nearopt laws with unbounded forward alpha>1 divergences.

## 2. Exact density ratio and uniform local expansion

Write `r=||x||_1` and `n=max(0,ceil(r-gamma))`. The layer-cake identity gives exactly `Z_gamma=2D_gamma`, and

    p_gamma(x)/q(x) = A exp[epsilon(r-n)].                                (4)

The essential range of `r-n` is `[gamma-1,gamma]`, including gamma=0,1 up to null boundaries. Both extrema are realized on positive-measure shell portions. Taking logs gives (1).

Put `u=epsilon m`. Uniformly in gamma in [0,1], `u=1-epsilon/2+epsilon^2/12+O(epsilon^4)` and

    epsilon^2 D_gamma
       =2+(2gamma-1)epsilon+(1/3-gamma+gamma^2)epsilon^2+O(epsilon^3),
    log A=(1/2-gamma)epsilon-epsilon^2/24+O(epsilon^3).                   (5)

The gamma-dependent quadratic terms cancel EXACTLY in log A. Substitution into (1) proves the two uniform infinity expansions in (2).

## 3. Fractional-shell averaging, TV and finite-order Rényi

Under Q, the radius r has density `w_epsilon(r)=epsilon^2 r e^(-epsilon r)` on [0,infinity). For r>=gamma set

    v=ceil(r-gamma)-(r-gamma) in [0,1),
    p_gamma/q = exp[log A+epsilon gamma-epsilon v]
              =1+epsilon(1/2-v)+O(epsilon^2),                           (6)

uniformly in gamma and v. The initial region r<gamma has Q-mass O(epsilon^2) and ratio `1+O(epsilon)`, so contributes only O(epsilon^3) to the L1 difference.

For any bounded measurable function H on [0,1], periodizing w over shells shows

    E_Q[H(v) 1_(r>=gamma)] = integral_0^1 H(v)dv + O(||H||_infinity epsilon), (7)

uniformly in gamma: on each unit interval compare a point value of w with the integral over that interval; the total error is at most `integral_0^infinity |w'(r)|dr=2epsilon/e`, plus the O(epsilon^2) omitted initial mass. Thus the limiting v is uniform to a quantitative O(epsilon) error.

Since `integral_0^1 |1/2-v|dv=1/4`, (6)–(7) give the TV result in (2). Also `integral(1/2-v)^2 dv=1/12`, so

    E_Q[(p_gamma/q-1)^2]=epsilon^2/12+O(epsilon^3).                      (8)

Normalization gives `E_Q[p_gamma/q-1]=0`. Uniform boundedness of the ratio near 1 permits a Taylor expansion of `(p/q)^alpha` and `(p/q)^(1-alpha)` for any fixed alpha>0. Equation (8) gives both finite-order Rényi expansions (3), including the alpha=1 KL limit. No equalities of the forward and reverse divergences beyond this common leading expansion are claimed.

## 4. Actual checks and limits

A Python Decimal diagnostic used 70 digits and the APPROXIMATE offset `gamma=g-epsilon/12`, `g=(3+sqrt(3))/6`, and computed exact formula (1). For epsilon 0.1, 0.05, 0.01, the values of `[D_infinity(P||Q)-epsilon/2]/epsilon^2` were approximately -0.04245793, -0.04206498, -0.04174675, tending toward -1/24. These are point diagnostics, not interval enclosures or evaluations of an actual optimizer.

The finite identities, all-gamma error estimates and averaging arguments are WRITTEN; no formal, independent review, novelty, source-equivalence or parent-adoption claim is made. Disjoint review should check the density normalization, shell-phase range, uniform periodization error, and both Rényi Taylor expansions.
