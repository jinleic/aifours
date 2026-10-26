# No fixed finite order of factual outcome moments determines the sharp sign criterion

**Status: CANDIDATE / NOVELTY_UNCLEAR.** A written strengthening within the same frozen bounded-real strong-surrogate model, following the parent's direction to characterize information needed beyond the two examples. No scientific program, moment-fitting search, numerical experiment or new target is introduced. The result is a constructive nonidentification theorem for ordinary moment summaries, not a claim that every finite-dimensional statistic is inadequate: the already-defined scalar Gamma_* itself determines the strict-positive decision at fixed p,q.

## 1. Precise statement

Fix p_0=p_1=1/2 and q=3/4. For every integer k>=0, there exist two probability densities f and g on [0,1], both C-infinity, strictly positive and symmetric about 1/2, and a number gamma in (0,1/2), such that:

1. the factual law in each surrogate stratum is f in the first model and g in the second:

       mu_0^f=mu_1^f=(1/2)f(y)dy,
       mu_0^g=mu_1^g=(1/2)g(y)dy;

2. their conditional raw moments match through order k:

       integral_0^1 y^j f(y)dy = integral_0^1 y^j g(y)dy,
       j=0,1,...,k;

3. their external gamma and treated surrogate marginal q are identical and compatible;
4. in the f model, **every** compatible full law has delta>0, while in the g model, there is a compatible full law with delta<0.

Thus, even with positive smooth symmetric factual densities and fixed surrogate masses, no finite truncation of ordinary factual moments can reproduce the exact sharp sign decision uniformly over this model. This is an all-k argument with explicit smooth perturbations, not additional finite enumeration.

## 2. An exact symmetric-density threshold formula

Let F be any strictly positive continuous density distribution on [0,1], symmetric about 1/2, and use the same F in both factual surrogate strata. Write Q for its usual probability quantile. Then Q is continuous and strictly increasing, and symmetry gives

    Q(1-u)=1-Q(u),  0<=u<=1.                               (1)

The main theorem's data have g_min=-1/2, h=1/4 and I=[1/4,1/2]. Their combined upper tail is

    W(r)=(1/2) integral_(1-2r)^1 Q(v)dv
         +(1/2) integral_(1-2(r-1/4))^1 Q(v)dv.

The derivative of W(r)-r at interior r is

    Q(1-2r)+Q(3/2-2r)-1.                                  (2)

It is strictly decreasing. At r=3/8, its value is Q(1/4)+Q(3/4)-1=0 by (1). Therefore the unique maximizer is r=3/8, t=1/8.

Put

    A_F=integral_0^(1/4) Q(v)dv.                            (3)

Since the mean is 1/2, symmetry and (1) imply

    W(3/8)
      =(1/2)[integral_(1/4)^1 Q(v)dv
              +integral_(3/4)^1 Q(v)dv]
      =(1/2)[1/2-A_F+1/4-A_F]
      =3/8-A_F.

Consequently the exact sharp positive-effect threshold is

    Gamma_*(F)=-1/2+1-3/8+W(3/8)=1/2-A_F.                 (4)

Because F has positive density, A_F>0 and Gamma_*(F)<1/2. For the uniform density f=1, A_f=1/32 and Gamma_*(f)=15/32.

The combined W is not identically zero, so the main theorem's strict trichotomy applies at gamma>0: above Gamma_* every law has positive delta; below it the attained sharp lower bound is negative.

## 3. Smooth perturbations annihilating any finite moment order

Let alpha=1/4 and fix delta_0=1/16. Choose an even smooth cutoff chi on the real line, equal to 1 near 0 and supported in [-delta_0,delta_0]. For definiteness one may build it from theta(t)=0 for t<=0 and theta(t)=exp(-1/t) for t>0, by

    chi(v)=theta(delta_0^2-v^2) /
           [theta(delta_0^2-v^2)+theta(v^2-(delta_0/2)^2)].   (5)

The denominator never vanishes: the two theta arguments cannot both be nonpositive. This defines a C-infinity even cutoff, 1 for |v|<=delta_0/2 and 0 for |v|>=delta_0.

Choose an even integer n>k with n>=2, and define

    phi(x)=(x-alpha)^(n-2) chi(x-alpha),
    psi(x)=phi(x)+phi(1-x),
    H(x)=psi^(n)(x).                                       (6)

Here psi^(n) denotes the n-th ordinary derivative. The supports near alpha and 1-alpha are disjoint and lie strictly inside (0,1). The function psi is symmetric, and because n is even, H is symmetric as well. All derivatives of psi vanish at 0 and 1.

For every polynomial x^j of degree j<n, integration by parts n times gives

    integral_0^1 x^j H(x)dx=0.                              (7)

All boundary terms vanish; the n-th derivative of x^j is zero. This includes j=0, so H has mean mass zero. It is not identically zero: otherwise psi would be a polynomial of degree at most n-1 with compact support inside (0,1), forcing psi=0, contrary to (6).

Let M=max_[0,1]|H|>0, and for |epsilon|<1/(2M) define

    f_epsilon(x)=1+epsilon H(x).                            (8)

These are normalized, symmetric C-infinity densities, bounded below by 1/2. By (7), every moment through degree k agrees **exactly** with the uniform density. No approximate moment matching is involved.

## 4. The relevant trimmed moment actually changes

Let x_epsilon be the lower quartile of f_epsilon, that is

    integral_0^(x_epsilon) f_epsilon(x)dx=alpha.

Strict positivity makes the quartile unique. The implicit function theorem near epsilon=0 gives x_0=alpha and

    x'_0=-integral_0^alpha H(x)dx.                          (9)

The lower-quantile integral in (3) equals the lower-tail first moment, because the density is positive:

    A(epsilon)=integral_0^alpha Q_epsilon(v)dv
             =integral_0^(x_epsilon) x f_epsilon(x)dx.

Differentiating at 0 and using (9),

    A'(0)=integral_0^alpha (x-alpha)H(x)dx.                  (10)

Two integrations by parts in (10) give

    A'(0)=-psi^(n-2)(alpha).                                (11)

Indeed the term (x-alpha)psi^(n-1)(x) vanishes at alpha and at 0, and psi^(n-2)(0)=0. Near alpha, chi=1, while the reflected bump phi(1-x) vanishes. Hence

    psi^(n-2)(alpha)=(n-2)!,
    A'(0)=-(n-2)!<0.                                      (12)

It follows that for all sufficiently small positive epsilon,

    A(epsilon)<A(0)=1/32,
    Gamma_*(f_epsilon)>Gamma_*(f_0)=15/32.                 (13)

This is a strict analytic perturbation statement, not a numerical observation. Both thresholds remain below 1/2 by positivity of A(epsilon).

## 5. Same moments, opposite sharp conclusions

Choose any sufficiently small positive epsilon from (13), put f=f_0 and g=f_epsilon, and set

    gamma=[Gamma_*(f)+Gamma_*(g)]/2.

Then gamma is strictly between the thresholds, is positive and is less than 1/2. It is compatible with both models because g_min=-1/2 in each and compatibility is gamma in [-1/2,1/2]. Treatment's surrogate effect is h=1/4>0 in each.

For f, gamma>Gamma_*(f), so the complete identified interval has lower endpoint L_f>0. For g, gamma<Gamma_*(g), and W is nonzero, so L_g<0 and the main constructive theorem supplies a full compatible law attaining it. The entire factual moment vectors through degree k, p_s,q and the external gamma nevertheless agree.

This proves all four assertions in Section 1. QED.

## 6. Information and novelty boundary

The result rules out **finite ordinary-moment truncations**, even when exact and augmented by symmetry/smoothness/positivity. It does not rule out a single purpose-built functional such as Gamma_*, a suitably informative quantile functional, the full observed distribution, or a finite-dimensional parametric model imposed as an additional assumption. It does not concern finite-sample estimation error.

Smooth moment-annihilating perturbations and the distinction between moments and trimmed means are classical. The proposed contribution is their exact bridge to opposite **attainable sharp surrogate-sign conclusions** in the frozen model. This manuscript has not had a new independent written check; the main theorem's previous WRITTEN_CHECKED status must not be automatically extended to it. Kuroki 2013 remains ACCESS_BLOCKED and scientific priority remains unestablished.
