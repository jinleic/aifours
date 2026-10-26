# Independent written review: finite ordinary-moment sign barrier

Before-creation clock observed: **2026-10-23T13:16:03-07:00**. Reviewer: `MathResearch96h`, at the parent's explicit request. Entire proof lines1–141 read; no execution, moment-fitting program, numerical experiment, CLI or nested agent was used. The sole output is inside the reviewer's mathematics root.

Reviewed file: `/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261023-96h/proof-no-finite-moment-sign-summary-v1.md`.

Exact SHA256: **`71690f0d301a581f448dc42b58559b0ee0a1b3ff310a841e296dc1979d9e94da`**.

The sharp-bound parent theorem was independently reconstructed in `peer-review-info-bounded-outcome-v1.md` against its pinned original proof SHA256 `618ee5c5fc3ebc503f4dc730d70572dbc807036fd49efc87ef65d2e798643a82`. Its minor binary-baseline wording issue does not affect this continuous-density construction.

**Verdict: 0 FATAL /0 MAJOR /0 MINOR. No substantive defect found in the all-k smooth moment-matching construction, the strict Gamma_* perturbation or the opposite attainable sign conclusions under the frozen model.** This is ordinary in-harness written checking, not kernel/human/cross-vendor acceptance or novelty clearance.

## 1. Symmetry pins the optimizer exactly

For a continuous strictly positive density on[0,1], its distribution function is strictly increasing onto[0,1], so Q is continuous and strictly increasing. Symmetry gives F(1-x)=1-F(x) and therefore Q(1-u)=1-Q(u), including the endpoint conventions.

With the same factual density in both half-mass strata, h1/4 and I=[1/4,1/2], differentiation of the two scaled tail integrals gives

    d(W-r)/dr=Q(1-2r)+Q(3/2-2r)-1.

This is strictly decreasing and vanishes at r3/8 by symmetry. The maximum is uniquely at r3/8,t1/8. Writing A_F=integral_0^(1/4)Q,

    integral_(1/4)^1 Q=1/2-A_F,
    integral_(3/4)^1 Q=1/4-A_F,
    W(3/8)=3/8-A_F.

Hence Gamma_*=1/2-A_F exactly. The density's positivity makes A_F>0 and W nonzero, so Gamma_*<1/2 and the main theorem's strict sign trichotomy applies. This is an exact optimizer identity; it does not rely on a derivative of an unknown optimizing r after perturbation.

## 2. The smooth cutoff and the moment-annihilating perturbation

For delta0>0, the arguments delta0^2-v^2 and v^2-(delta0/2)^2 cannot both be nonpositive: that would require v^2>=delta0^2 and v^2<=delta0^2/4 simultaneously. Thus the denominator in the displayed theta-ratio is positive everywhere. Standard flatness of exp(-1/t) at0 makes the ratio C-infinity. It equals1 on |v|<=delta0/2 and0 on |v|>=delta0, and is even.

For alpha1/4 and delta0=1/16, the two supports of psi lie in[3/16,5/16] and[11/16,13/16], disjoint and strictly inside(0,1). Taking n even and n>k, n>=2, makes psi symmetric and H=psi^(n) symmetric. Every endpoint derivative vanishes.

Integrating x^j H by parts n times annihilates it for j<n, with no boundary term. In particular integral H0; for all j<=k the moments of1+epsilon H match those of1 exactly. H is not identically zero: otherwise psi would be a polynomial of degree at most n-1 yet vanish on an open endpoint neighborhood, hence vanish everywhere, contradicting its polynomial bump near alpha. Therefore M=max|H| is positive and finite. The explicit restriction |epsilon|<1/(2M) gives a normalized C-infinity density bounded below by1/2 on the whole closed interval.

For k0 this construction may take n2; symmetry still fixes the mean1/2 even though matching the first moment was not requested. Thus the claimed common g_min holds also at the smallest k.

## 3. The trimmed first moment really changes

The quartile equation is

    x_epsilon+epsilon integral_0^(x_epsilon)H=alpha.

Its x derivative at epsilon0 is1, so the ordinary implicit function theorem applies. It gives x'_0=-integral_0^alpha H. Differentiating the tail first moment then yields

    A'(0)=alpha x'_0+integral_0^alpha xH
         =integral_0^alpha(x-alpha)psi^(n)(x)dx.

Two integrations by parts give -psi^(n-2)(alpha): the first boundary expression has factor x-alpha at the upper endpoint and vanishes at0 by compact support; the remaining endpoint derivative at0 vanishes as well. Near alpha, psi=(x-alpha)^(n-2), with no reflected bump present. Hence

    A'(0)=-(n-2)!<0.

This proves a strictly smaller A(epsilon), and therefore a strictly larger Gamma_*, for every sufficiently small positive epsilon. This is a genuine analytic first-order perturbation, not approximate moment matching or an unproved claim that a nonlinear quantile functional changes.

## 4. Exact preservation of data and opposite signs

Let f1 and g=1+epsilon H with such an epsilon. Both are symmetric probability densities of mean1/2; their half-mass factual measures have p_s1/2 and m_s1/4. Therefore both have g_min=-1/2, h1/4 and compatibility range gamma in[-1/2,1/2]. Set gamma at the midpoint of the two distinct Gamma_* values. It lies in(15/32,1/2), so is positive and compatible with both models; q3/4 is held fixed.

All conditional raw moments through k agree by the moment annihilation, and hence the supplied ordinary moment summaries of each factual stratum agree exactly. Randomization of treatment can be added independently without changing any of these variables or causal means.

For the uniform model, gamma>Gamma_*(f), so every compatible law has delta>=L_f>0. For the perturbed model, gamma<Gamma_*(g), W is nonzero and the main constructive theorem gives an attained L_g<0.

One can reconstruct that attaining law directly without relying only on the main theorem's assertion: choose mass3/8 from the upper three quarters of the B0 factual quantiles and mass1/8 from the upper quarter of the B1 quantiles. Set Z=z on the first switch group C and Z1 off C, with

    z=(8gamma-1)/3.

Because gamma is between15/32 and1/2, z is in(0,1). Then E Z=3z/8+5/8=gamma+1/2, so the recovered missing outcomes have exactly the required gamma. The treated surrogate marginal is3/4, and the factual law is untouched. Its objective is

    delta=3z/8-W(3/8)=gamma-1/2+A_g
         =gamma-Gamma_*(g)<0.

Thus a literal negative law is attained, while the positive conclusion in the uniform model is universal. No hidden monotonicity, rank-invariance or factual/missing-outcome independence was introduced.

## 5. Scope and priority boundary

The theorem correctly rules out every fixed finite truncation of *ordinary factual raw moments*, even augmented by the common p_s,q,gamma and the specified density regularity. It does not rule out Gamma_* as a single purpose-built functional, a quantile summary adapted to the decision, or a finite-dimensional parametric restriction; the manuscript explicitly says so. No finite-sample or unrestricted causal-inference statement is inferred.

The moment-annihilating derivative bump, compact-support integration by parts and quantile perturbation are classical. The source-priority gate remains unresolved, including the blocked full Kuroki2013 theorem. This review is a correctness reconstruction of the exact snapshot, not a claim that the bridge to surrogate-sign conclusions is first or publishable.
