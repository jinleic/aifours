# High-privacy density and one-sided Rényi topology

**AUTHOR CANDIDATE — WRITTEN; NOT independently reviewed or parent-adopted.** Native pre-write observation: `Wed Oct 28 19:43:47 PDT 2026`.

## 1. Exact scope and named import

Condition on the unreviewed all-law high-privacy rigidity candidate `frontier-20261028-sharp-high-privacy-universal-limit-v1.md`, SHA-256 `8615b71531aee0c55760796aad35dc6cb39002606b64b919017ed7a6e8b647d2`, especially its scaled total-variation and W1 convergence for arbitrary mixed nonnegative weights. Let epsilon->0, b=e^(-epsilon), kappa(epsilon)>=0 arbitrary, and X be any actual original full-D-private law satisfying

    E[|X|^2+kappa||X||_1]
      <= [4/epsilon^2+2kappa/epsilon][1+o(1)].                            (1)

Write Z=epsilon X, f_epsilon for its all-point private density representative, and `lambda(z)=(1/4)e^(-||z||_1)`. This note's written conclusions are

    ||f_epsilon-lambda||_p ->0   for EVERY p in [1,infinity],             (2)
    D_infinity(Lambda || Law(Z)) ->0,                                     (3)
    D_KL(Law(Z)||Lambda), D_KL(Lambda||Law(Z)) ->0.                      (4)

Here L-infinity is essential sup, and reverse D_infinity is log esssup(lambda/f_epsilon). Thus ALL fixed-order reverse Rényi divergences, including infinity, tend to zero; both directions tend to zero for orders 0<alpha<=1. In contrast, for EACH fixed alpha>1 there are actual original-J-nearopt laws with forward D_alpha->infinity and forward D_infinity->infinity, even though they converge in TV, W1 and W2 and both KLs tend to zero. This is a high-privacy asymptotic statement, not an assertion at fixed epsilon.

## 2. Uniform density convergence from full-shift privacy

Repeated privacy yields, for EVERY z,h,

    f_epsilon(z+h) <= exp(||h||_1+epsilon) f_epsilon(z),                 (5)

and the reverse direction. Integrating (5) over h in D gives the law-independent bound `||f_epsilon||_infinity<=e^(1+epsilon)/2`.

Take a compact smooth probability kernel rho_delta supported in delta D. By (5), uniformly over z,

    |(f_epsilon*rho_delta)(z)-f_epsilon(z)|
      <= [e^(delta+epsilon)-1] ||f_epsilon||_infinity.                   (6)

For fixed delta, the import's weak convergence plus tightness and uniform continuity of the fixed kernel imply `f_epsilon*rho_delta -> lambda*rho_delta` uniformly on all R^2: use a finite net on compact sets, and tightness for the tails. Then let epsilon->0 and delta->0; lambda is uniformly continuous. Equation (6) proves the L-infinity case of (2). The import already gives L1 convergence; interpolation `||f-lambda||_p^p<=||f-lambda||_infinity^(p-1)||f-lambda||_1` proves all finite p>=1.

## 3. Reverse infinity and both KLs

Taking z=0 in (5), with the inequality in the needed direction, gives the GLOBAL pointwise lower bound

    f_epsilon(z) >= f_epsilon(0)e^(-epsilon-||z||_1).

Consequently, with `c_epsilon=4 f_epsilon(0)e^(-epsilon)`,

    f_epsilon(z)>=c_epsilon lambda(z),
    D_infinity(Lambda||Law(Z)) <= -log c_epsilon ->0.                     (7)

Equation (2) makes `f_epsilon(0)->1/4`; normalization ensures c_epsilon<=1. Nonnegativity of divergences proves (3), and reverse KL and every fixed reverse Rényi order are bounded above by reverse infinity.

For forward KL, on any fixed ball the density ratio tends uniformly to 1 because lambda is bounded away from zero there. Globally, `f_epsilon<=K` for one fixed K and hence

    log(f_epsilon(z)/lambda(z)) <= log(4K)+||z||_1.

The import's W1 convergence gives uniform integrability of the first norm. The positive tail of the displayed log ratio therefore has uniformly vanishing f_epsilon integral outside large balls; the compact integral tends to zero. KL nonnegativity then forces the forward KL limit in (4). For 0<alpha<=1, Rényi monotonicity bounds each direction by its corresponding KL.

## 4. Exact forward-Rényi counterexample with W2 convergence

Choose any R=R(epsilon)->infinity, for example `R=log(1/epsilon)`, and `t=R^(-3)`. Let the scaled law be

    mu_epsilon=(1-t)Lambda+t tau_(R e1)Lambda.                             (8)

In original X coordinates this is a mixture of two translates of the actual epsilon-private product-Laplace law, hence remains fully private. Its scaled squared second moment is exactly `4+t R^2=4+1/R`; it is original-J first-order-nearopt by the source-independent marginal lower bound. The natural coupling gives TV<=t, W1<=tR=R^(-2) and W2<=sqrt(t)R=R^(-1/2).

On the whole half-plane z1>=R, the density ratio of the shifted Laplace to the unshifted one is exactly e^R, and Lambda gives this half-plane mass `(1/2)e^(-R)`. Therefore for EVERY fixed alpha>1,

    D_alpha(mu_epsilon||Lambda)
      >= [alpha log(1-t+t e^R)-R-log 2]/(alpha-1) ->infinity,
    D_infinity(mu_epsilon||Lambda)=log(1-t+t e^R)->infinity.              (9)

Equation (9) is an exact half-plane lower bound; the infinity equality follows from the triangle inequality giving shifted/unshifted ratio <=e^R everywhere. Reverse infinity remains <=-log(1-t)->0. This exhibits the stated direction/order cutoff without mistaking failure of a forward stronger divergence for failure of TV or W2.

## 5. Status

All original claims in §§2–4 are WRITTEN conditional on the pinned unreviewed 8615 rigidity result; the explicit mixture is directly checkable and still has no independent review. No numerical, formal, cross-model, novelty or parent-acceptance claim is made. Disjoint review should focus on the global density sup upgrade, the basepoint lower bound, uniform integrability for forward KL, and the half-plane Rényi calculation.
