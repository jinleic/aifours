# Explicit full-D privacy distance from the product of 1D optima

**AUTHOR CANDIDATE — WRITTEN; NOT independently reviewed or parent-adopted.** Native pre-write observation: `Wed Oct 28 20:07:45 PDT 2026`.

## 1. Finite-epsilon geometric result

Fix any epsilon>0, `b=e^(-epsilon)`, `m=b/(1-b)` and ANY gamma in (0,1]. Let nu_gamma be the actual symmetric 1D epsilon-private staircase density proportional to `b^(max(0,ceil(|x|-gamma)))`, and let `Q_gamma=nu_gamma tensor nu_gamma`. This product need not be private for the ORIGINAL 2D full l1 diamond. Put `d=min(gamma,1/2)`.

For EVERY 2D Borel law mu satisfying the original all-event FULL closed D privacy condition,

    TV(mu,Q_gamma) >= [b(1-b)/(1+b)] [d/(2(gamma+m))]^2 >0.           (1)

This is a source-independent, explicit finite-epsilon separation from a concrete NONPRIVATE product. It is not a claim that the true 2D optimum equals a product or that the product is a feasible mechanism.

Under the separately pinned UNREVIEWED exact 1D optimization candidate `frontier-20261028-exact-scalar-marginal-relaxation-v1.md`, SHA-256 `cde9bcc08bd4f87e635f1a2566fb2eaae6f1b289df5ebd4d36707229c8fc60ed`, take gamma to be its exact unique minimizing offset for any given mixed cost `Y^2+kappa|Y|`, kappa>=0, or for pure |Y|. Then (1) is an explicit TV gap from the product of the TWO individually optimal 1D laws. That optimizer interpretation is conditional on cde9; inequality (1) itself is not.

## 2. Short diagonal shift proves the bound

The exact 1D normalization is `Z1=2(gamma+m)`. Take `I=(gamma-d,gamma)`, `I+=(gamma,gamma+d)` and rectangle A=I x I. The density on I+ is exactly b times the density on I; thus

    Q_gamma(A)=[d/(2(gamma+m))]^2,
    Q_gamma(A+(d,d))=b^2 Q_gamma(A).                                      (2)

The diagonal displacement (d,d) is in D since 2d<=1. Any original-private mu obeys `mu(A+(d,d))>=b mu(A)`. Subtracting this inequality from the violated one for Q and using the definition of total variation gives

    b(1-b)Q_gamma(A)
       <= b|Q_gamma(A)-mu(A)|+|mu(A+(d,d))-Q_gamma(A+(d,d))|
       <=(1+b)TV(mu,Q_gamma),

which proves (1). This argument uses no density of mu, compactness, optimizer existence, selected numerical search or external source.

## 3. Concrete rational bound and high-privacy scale

At epsilon=ln 2, the cde9 1D squared-cost minimizing gamma is `3^(1/3)-1`. Since `(36/25)^3<3<(3/2)^3`, gamma is in (11/25,1/2) and d=gamma. With b=1/2 and m=1, monotonicity of gamma/(1+gamma) gives for every actual 2D private mu

    TV(mu,Q_gamma) >= gamma^2/[24(1+gamma)^2] >121/31104.                (3)

This instance's interpretation as the product of individually J-optimal marginals imports the unreviewed 1D theorem; (3)'s geometric inequality is otherwise unconditional.

The same 1D theorem's gamma tends to 1/2 as epsilon->0 UNIFORMLY for arbitrary kappa>=0, including kappa=kappa(epsilon): writing v=m(m+1), s=sqrt(v), t=[v(m+1/2)]^(1/3), one has s<t, the mixed cubic is increasing, and its root lies between the pure-mean root s-m and pure-square root t-m. Both endpoints tend to 1/2. Consequently the right-hand side of (1) is asymptotic to `epsilon^3/32` uniformly in kappa. This is a lower bound on the finite-epsilon privacy-violation distance; it is compatible with convergence of both actual 2D optima and the nonprivate product to product Laplace as epsilon->0.

## 4. Status

All geometric steps are WRITTEN and the selected numerical gamma interval is a rational cube comparison, not a floating confidence claim. The optimum interpretation and its high-privacy selector limit depend on the explicitly named unreviewed cde9 result. No formal, independent review, novelty, source-equivalence, or parent acceptance is claimed. Suggested review: normalization, diagonal-shift inequality and its TV factor 1+b.
