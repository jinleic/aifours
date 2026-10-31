# Near-optimal mechanisms: two-sided KL stability and the Renyi order-one cutoff

**AUTHOR CANDIDATE — WRITTEN with exact rational mixture checks; NOT independently reviewed or parent-adopted.** Actual native pre-write clock: `Wed Oct 28 18:08:03 PDT 2026`.

## 1. Exact original target and claims

Fix EVERY finite epsilon>0. Let `b=e^(-epsilon)`, `D={h:||h||_1<=1}`, and F_epsilon be ALL Borel laws satisfying the epsilon privacy inequality for EVERY Borel event and EVERY h in the FULL CLOSED D. Let `J(mu)=E_mu|X|_2^2`, V its original all-law infimum, and mu_* its unique optimizer.

For every feasible near-optimal sequence `J(mu_n)->V`, this candidate proves, conditional on the named all-law TV-stability input,

    D_KL(mu_n || mu_*) -> 0,       D_KL(mu_* || mu_n) -> 0.             (1)

For EVERY fixed order `0<alpha<1`, Renyi divergence in BOTH directions tends to zero too. No convergence rate or uniform-in-epsilon assertion is made.

This cannot be extended to any fixed order alpha>1. For EVERY finite epsilon>0 there is ONE explicit sequence of genuinely feasible, exact-epsilon laws nu_R with the following properties; no density smoothness is assumed or claimed:

    J(nu_R)=V+1/R,    TV(nu_R,mu_*)<=R^(-3),
    W_2(nu_R,mu_*)<=R^(-1/2),    D_KL in BOTH directions ->0,
    D_alpha(nu_R || mu_*) -> infinity  for EVERY fixed alpha>1,           (2)

including order infinity. In fact for fixed alpha>1 the forward Renyi divergence is at least

    epsilon R - [3alpha/(alpha-1)]log R - O_epsilon,alpha(1).            (3)

In the REVERSE direction, all Renyi orders, including infinity, tend to zero for this sequence. This is an asymmetric exact order-one cutoff, not a contradiction of TV/W2/finite-Lp convergence and not a finite-epsilon privacy violation.

## 2. Precise named inputs and definitions

- Original all-law LAW642 parent `institute/runs/three-area-2026-10-23-96h/privacy-all-law-self-contained-parent-v1.md`, SHA `c08f6353f121ef9e35da0e9d5e8ec9c87b0da838be0d1adf38b807010a1cd979`, gives the unique optimizer with centered symmetric convex compact core S containing 0 in its interior, canonical density `p_*=Z^(-1)b^(n_S)`, `n_S(x)=min{k:x in S+kD}`, finite positive V and full-shift feasibility.
- My UNREVIEWED `frontier-20261028-all-law-tv-stability-v1.md`, SHA `3f6c2a61738cc92f615e375d88f6dfb10f96b553585b5c8468480a7ec9683f79`, proves all original feasible cost-near-minimizers converge to mu_* in TV and W2 at fixed epsilon. That candidate explicitly imports LAW642 plus the separately adopted v241 core classification. The universal KL conclusions are CONDITIONAL on that still-unreviewed input, not a new acceptance of it. The concrete translated-mixture counterexample in §§5–6 uses LAW642 only and proves its own TV/W2/KL properties directly.

For positive densities p,q and alpha>0, alpha!=1, use

    D_alpha(p||q)=(alpha-1)^(-1) log integral p^alpha q^(1-alpha) dx,

and take D_1 as relative entropy and D_infinity as the essential supremum log likelihood ratio. The all-law privacy property ensures absolute continuity; the construction below supplies strictly positive densities. No opaque divergence convention or finite-parameter endpoint epsilon=0/infinity is assumed.

## 3. Uniform exponential density bounds for near-optimal sequences

By the named TV stability, any near-optimal mu_n converges to mu_* in TV. For each law take the finite ball-average density representative. Integrating privacy over D gives a common finite bound

    0 <= p_n(x),p_*(x) <= C=1/(2b)     for every x,                       (4)

and the representative obeys `p_n(x+h)>=b p_n(x)` for ALL x and ALL h in D. Canonical p_* also satisfies this pointwise.

Take the fixed l1 unit ball D as an integration set. Since mu_*(D)>0 and TV convergence implies mu_n(D)->mu_*(D), choose eta>0 such that mu_n(D)>=eta for all sufficiently large n; also arrange mu_*(D)>=eta. For x in R^2 and y in D, a chain of at most `ceil(||x-y||_1)` closed-D shifts gives

    p_n(x)>=b^ceil(||x-y||_1) p_n(y)
           >=b^(||x||_1+2) p_n(y).

Integrate y over D, whose area is 2. The SAME positive constant applies to p_* and every sufficiently late p_n:

    c exp(-epsilon ||x||_1) <= p_n(x),p_*(x) <= C,                      (5)

with `c=eta*b^2/2>0`. This is a pointwise statement for the chosen representatives; the probability laws remain unchanged.

In particular there is a fixed A such that

    |log p_n(x)|+|log p_*(x)| <= A+2epsilon||x||_1.                     (6)

Every near-optimal sequence has J bounded eventually by V+1, hence `E||X||_1^2<=2(V+1)` uniformly. Therefore the p_n first-moment tails over `{||x||_1>R}` are uniformly O(1/R), and p_* has the same finite-tail property.

## 4. BOTH relative entropies and all alpha<1

On any compact diamond `||x||_1<=R`, (5) bounds both densities above and below by positive constants. The function `x log(x/y)` is uniformly Lipschitz in x on that compact density range, vanishing when x=y. Similarly `|log(p_*/p_n)|` is bounded by a fixed multiple of `|p_*-p_n|`. TV convergence therefore makes BOTH local relative-entropy integrals tend to 0.

On the complement, (6) bounds the absolute integrands of both `p_n log(p_n/p_*)` and `p_* log(p_*/p_n)` by the corresponding probability density times `A+2epsilon||x||_1`. Their tails are uniformly small by the bounded second moments just established. First take n->infinity on the compact diamond, then R->infinity. This proves (1). In particular both integrals are finite for all sufficiently late n; no invalid interchange of infinity-minus-infinity is used.

For every fixed 0<alpha<1, pointwise

    min(p_n,p_*) <= p_n^alpha p_*^(1-alpha),

while Holder bounds its integral by 1. The integral is therefore in `[1-TV(mu_n,mu_*),1]`, and its log tends to 0. This proves D_alpha(mu_n||mu_*)->0; swapping p_n,p_* proves the reverse direction. Fixed alpha=1 is (1). These conclusions are strictly stronger than TV alone and use the fixed-privacy density lower bounds and near-optimal moment control.

## 5. Actual near-optimal shifted-mixture sequence

For every integer R>=2, write tau_R mu_* for translation by `R e1`, `e1=(1,0)`, and put

    w_R=R^(-3),     nu_R=(1-w_R)mu_* + w_R tau_R mu_*.                  (7)

Every translate of a feasible noise law is feasible for the SAME every-event/full-D model, and convex mixtures remain feasible. Because the canonical optimal core/density is centrally symmetric, `E_mu_* X=0`; hence the actual squared-Euclidean cost is EXACTLY

    J(nu_R)=(1-w_R)V+w_R(V+R^2)=V+1/R.                                   (8)

The mixture representation gives `TV(nu_R,mu_*)<=w_R`. Couple X~mu_* to X+R e1 with probability w_R and to X otherwise; then `W2^2<=w_R R^2=1/R`. This proves the cost, TV and W2 statements in (2) without importing the new TV theorem.

The exact epsilon is also attained. Choose B greater than every coordinate of S, and c=max_S(x1+x2). In the positive quadrant x1,x2>B, `n_S(x)=ceil(x1+x2-c)`. For x1>B+R and x2>B, BOTH the original and translated canonical densities drop by exactly b under h=e1. Their positive mixture does too. Integrating over any nonempty bounded open rectangle in that quadrant gives an actual event equality `nu_R(E)=b^(-1)nu_R(E+e1)`. Therefore the minimal privacy parameter of nu_R is exactly epsilon.

Convexity of relative entropy in its first argument and the R-fold full-D privacy bound `d(tau_R mu_*)/dmu_*<=e^(epsilon R)` give

    D_KL(nu_R||mu_*) <= w_R D_KL(tau_R mu_*||mu_*)
                      <= epsilon/R^2 -> 0.

Also `nu_R >= (1-w_R)mu_*` as measures, so

    D_infinity(mu_*||nu_R) <= -log(1-w_R) -> 0.                          (9)

Every reverse Renyi divergence, in particular reverse KL, is bounded by this quantity. This confirms the KL/convergence part of (2) directly, independently of the unreviewed TV-stability input.

## 6. Forward Renyi divergence actually diverges for alpha>1

Because S has nonempty interior, choose an actual Euclidean ball A centered at 0 contained in int S, with `c0=mu_*(A)>0`. Let `E_R=R e1+A`. Under the shifted component, `nu_R(E_R)>=w_R c0`.

Compactness of S gives an l1 radius M with S subset M D. If x lies in E_R then `||x||_1>=R-O(1)`; since `x in S+n_S(x)D` implies `||x||_1<=M+n_S(x)`, the original canonical density satisfies `p_*(x)<=C0 exp(-epsilon R)` there. Thus for a fixed C1>0,

    mu_*(E_R)<=C1 exp(-epsilon R).                                       (10)

For every fixed alpha>1, Jensen/Holder on E_R gives

    integral p_(nu_R)^alpha p_*^(1-alpha) dx
      >= nu_R(E_R)^alpha / mu_*(E_R)^(alpha-1)
      >= c0^alpha R^(-3alpha) C1^(1-alpha) exp((alpha-1)epsilon R).

Taking `(alpha-1)^(-1)` times the logarithm proves (3), and hence forward D_alpha->infinity for EVERY fixed alpha>1. The same event lower-bounds the essential likelihood ratio and gives the order-infinity divergence. For each fixed R these divergences are finite: iterating the original DP bound R times gives `tau_R mu_* <= e^(epsilon R)mu_*`, so the mixture likelihood ratio is bounded above, while (9) bounds it below.

The SAME sequence works for all fixed alpha>1, but no uniformity in alpha near 1 is claimed. The reverse divergence for every alpha is <=D_infinity(mu_*||nu_R), which tends to 0 by (9).

## 7. Actual exact arithmetic and scientific scope

A local `fractions.Fraction` check used R=8 only as a diagnostic of the mixture factors:

```text
R= 8 mixture_weight= 1/512 exact_cost_excess= 1/8 forward_KL_upper_in_units_of_epsilon= 1/64 reverse_likelihood_ratio_upper= 512/511
alpha= 2 exponential lower-bound factor at epsilon=log2: 1/1024
alpha= 3 exponential lower-bound factor at epsilon=log2: 1/2048
```

The last two numbers omit the fixed positive core/area constants in the rigorous lower bound; they are arithmetic diagnostics, not evidence that divergence is already large at R=8. The all-variable exponential proof is §6. No floating-point run, solver, external model or source-priority search was used.

The two-sided KL/alpha<1 theorem requires the explicitly UNREVIEWED full-law TV-stability candidate. The translated-mixture alpha>1 counterexample is independently written from the named LAW642 canonical law and applies even if that candidate remains unreviewed. Request disjoint review of the pointwise lower bound, uniform entropy tails, actual shifted-event privacy equality and Renyi event estimate. No formal/kernel, human/configured-family, independent-model or novelty acceptance is claimed; historical held outcomes are not accepted premises.
