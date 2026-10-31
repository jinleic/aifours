# Exact 1D J/L frontier and finite 2D joint-budget relaxation

**AUTHOR CANDIDATE — WRITTEN; NOT independently reviewed or parent-adopted.** Native pre-write observation: `Wed Oct 28 19:59:15 PDT 2026`.

## 1. Scope, dependencies and exact scalar frontier

Condition on the unreviewed exact 1D mixed-cost result `frontier-20261028-exact-scalar-marginal-relaxation-v1.md`, SHA-256 `cde9bcc08bd4f87e635f1a2566fb2eaae6f1b289df5ebd4d36707229c8fc60ed`. Set b=e^(-epsilon), m=b/(1-b),

    v=m(m+1),    s=sqrt(v),    t=[v(m+1/2)]^(1/3),
    L_max=(t+v/t)/2.                                                      (1)

The exact one-dimensional all-law Pareto frontier between `L1=E|Y|` and `J1=E Y^2` under epsilon privacy for all shifts |h|<=1 is parameterized by

    L1(x)=(x+v/x)/2,
    J1(x)=v+x^2/3+2t^3/(3x),        x in [s,t].                         (2)

Every point is attained by the actual symmetric 1D staircase with gamma=x-m; all other finite attainable 1D pairs are dominated by a point (2). The associated exact single-coordinate squared-error optimum under a mean upper budget u is

    phi(u)=infeasible                                    if u<s,
           v+x(u)^2/3+2t^3/[3x(u)]                     if s<=u<L_max,
           v+t^2                                        if u>=L_max,
    x(u)=u+sqrt(u^2-v).                                                   (3)

The curve is strictly convex and strictly decreasing on (s,L_max), then constant. This exact 1D frontier is a conditional deduction from cde9, not a claim that product staircases meet the original 2D full-D privacy condition.

## 2. Derivation and selector separation

The cde9 actual 1D staircase with gamma and x=m+gamma has

    L1(x)=(x+v/x)/2,
    J1(x)=v+x^2/3+2t^3/(3x).                                             (4)

Both follow by algebraic expansion of its exact geometric-shell moments. Since `(m+1/2)^2>v`, one has `m<s<t<m+1`. The mean-minimizing x is s; the squared-minimizing x is t. Their strict noncoincidence gives exact cross-objective penalties

    J1(s)-J1(t)=(t-s)^2(s+2t)/(3s)>0,
    L1(t)-L1(s)=(t-s)^2/(2t)>0.                                          (5)

For s<x<t, the weight making x the UNIQUE global minimum of `J1+kappa L1` is

    kappa(x)=(4/3)(t^3-x^3)/(x^2-v)>0.                                   (6)

It decreases continuously from infinity to zero; this is precisely the translated cubic from cde9. Hence every point in (2) is globally attainable and supported by the original 1D all-law scalar optimum. Any 1D law must have L1>=s; for s<L1<L_max, use the unique support (6) at x(L1), proving J1>=phi(L1). For L1>=L_max, the unconstrained J optimum at t dominates. At L1=s the exact mean optimizer gives phi(s). This proves completeness and (3).

The formula `d phi/du=-kappa(x(u))` is strictly increasing from -infinity to 0, proving strict convexity on the active interval; the constant continuation preserves convexity.

## 3. Original 2D joint-budget implication

For any original 2D full-D-private law, both coordinate marginals are 1D private. If J<=j and L<=ell then, with `u_i=E|X_i|`,

    ell>=u_1+u_2>=2s,
    j>=E X_1^2+E X_2^2 >=phi(u_1)+phi(u_2)>=2phi(ell/2).               (7)

The last step is Jensen plus monotone decrease of phi. Thus `ell<2s` is impossible, while for ell>=2s the EXPLICIT necessary lower boundary is `j>=2phi(ell/2)`.

A stronger strict conclusion is CONDITIONAL on the additional unreviewed 2D diagonal-gap candidate `frontier-20261028-strict-marginal-privacy-gap-v1.md`, SHA-256 `13140214203a7988976cfe1e92dbd464f844e747384f38808a02a8bfeb104221`: ell=2s is also impossible, and for ell>2s the necessary inequality is STRICT, `j>2phi(ell/2)`. When ell/2<L_max, choose kappa from (6) and use its strict 2D scalar gap; for ell/2>=L_max use kappa=0. The separately pinned quantitative gap candidate 30d can add an explicit but small positive amount. These stricter statements are NOT claimed independently of their unreviewed diagonal-gap inputs.

## 4. Sanity identities and limits

At epsilon=ln 2, m=1, v=2, `s=sqrt(2)` and `t=3^(1/3)`. Thus 1D mean and square selectors are `sqrt(2)-1` and `3^(1/3)-1`, respectively, and the original 2D mean budget `ell<2sqrt(2)` is infeasible. The 1D J-only lower is `2(v+t^2)=4+2*3^(2/3)`, matching cde9's separately certified example. Evaluating t,s or (3) numerically is unnecessary for these identities.

This is a written conditional reconstruction using elementary algebra and supporting-plane convexity. No numerical, formal, independent review, novelty, priority, exact 2D frontier or parent adoption is claimed. Review should verify the exact algebra (4), attainment at u=s, endpoint derivative behavior, and the Jensen/direction of the 2D budget inequality.
