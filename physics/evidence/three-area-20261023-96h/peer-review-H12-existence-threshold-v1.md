# Independent written reconstruction: H_{1,2} PH-existence threshold

Before-creation clock observed: **2026-10-23T13:07:01-07:00**. Reviewer: PhysicsResearch96h, ordinary in-harness peer. No author edit, root approximation, scientific program, solver, model CLI, test suite or formal verification was performed for this review.

## Snapshot and verdict

Assigned manuscript: `/Users/jinleic/repos/aifours/mathematics/evidence/three-area-20261023-96h/proof-H12-PH-existence-threshold-v1.md`, SHA-256 **`a35c865eaf977b065635e31ee13b4e101306d69f8b7562470b6bafc3a82a1a32`**. All 168 lines were read; the pin was observed by metadata hashing.

**0 FATAL / 0 MAJOR / 0 MINOR. No substantive defect found at the explicit theorem-import boundaries below.** The inverse-transform and positivity/nonpositivity classification reconstruct by written analysis. The positive-side finite PH existence conclusion remains conditional on the explicitly named classical characterization theorem. No minimum-order statement outside the earlier separately proved band is inferred.

This is independent in-harness written checking, not parent acceptance, worldwide novelty clearance, human peer review or a kernel proof.

## 1. Inverse transform and the closed G_k formula (lines 26–49)

For `d=a-c>0`, `b>0`, `k=d/b`, shifting by c gives the denominator `z((z+d)^2+b^2)^2`. Starting with

`L[exp(-dt)sin(bt)/b]=1/((z+d)^2+b^2)`,

applying `-(1/(2b)) partial_b` yields

`L[exp(-dt)(sin(bt)-bt cos(bt))/(2b^3)]=1/((z+d)^2+b^2)^2`.

Exponential decay justifies the parameter differentiation in the relevant Laplace half-plane. Dividing by z integrates from zero, and shifting back supplies exp(-ct). Thus the manuscript's integral inverse transform is correct.

With x=bt, differentiating that integral gives

`d g/dx=exp(-kx)(sin x-x cos x)/(2b^4)`.

Since `Delta^2=b^4(1+k^2)^2`, the normalization `g(t)=G_k(bt)/Delta^2` requires exactly

`G_k'=((1+k^2)^2/2) exp(-kx)(sin x-x cos x)`.

I independently differentiated the displayed closed form. Writing its cosine coefficient as `A=1-k(1+k^2)x/2` and sine coefficient as `B=k(k^2+3)/2+(1+k^2)x/2`, the derivative coefficients are

`kA-A'-B=-(1+k^2)^2 x/2`,

`kB+A-B'=(1+k^2)^2/2`.

Also G_k(0)=0, so the closed and integral forms agree exactly. For k>0 the exponential-polynomial remainder tends to zero and G tends to one.

## 2. All critical points and their signs (lines 51–72)

Let `R(x)=sin x-x cos x`; `R'(x)=x sin x` and `R(x)>0` near zero. Away from cosine zeros, a positive root is equivalent to `tan x=x`. There is one root in every `(j pi,j pi+pi/2)`, j>=1: tan x-x starts negative, tends to positive infinity, and has strictly increasing derivative tan^2 x on the interval. The alternating half intervals have tan x<0 and no positive solution. Cosine-zero endpoints and positive multiples of pi are not roots of R.

The signs alternate, with odd j yielding maxima and even j minima. At a root, substituting sin x=x cos x simplifies the bracket exactly to

`P_k(x)=1+kx+(1+k^2)x^2/2`.

For even j, cosine is positive and has magnitude `1/sqrt(1+x_j^2)`, giving `G=1-m_k`; for odd j, `G=1+m_k>0`. Thus every potentially negative local minimum has been covered, not just a sampled oscillation.

## 3. Both monotonicity derivatives and the exact threshold (lines 74–111)

For fixed x>0,

`partial_k [exp(-kx)P_k(x)] = exp(-kx)[x+kx^2-xP_k(x)]`

`= -((1+k^2)x^3/2) exp(-kx)`.

Dividing by sqrt(1+x^2) gives the displayed strictly negative derivative. At k=0, squaring positive quantities gives `m_0(x)>1` because the difference is x^4/4. As k tends to infinity, m tends to zero. Continuity and strict decrease give one and only one positive k_* at xi.

At k=1/xi,

`m=exp(-1)(xi^2+5)/(2sqrt(1+xi^2))=exp(-1)(y/2+2/y)`.

Since xi>2pi>6, y/2>3>e. Therefore this m exceeds one, and strict decrease in k proves `k_*xi>1` without a numerical root estimate.

For the x derivative I separately expanded

`-kP_k(x)(1+x^2)+P_k'(x)(1+x^2)-xP_k(x)`.

It equals

`(x^2/2)[(1-k^2)x-k(3+k^2)-k(1+k^2)x^2]`.

Thus the sign polynomial Q_k and the log-derivative identity in lines 98–105 are correct. If kx>=1,

`Q_k(x)<=x-kx^2-k(3+k^2)<0`.

For k>=k_* and x>=xi this condition follows from `k_*xi>1`. Hence every later local minimum has strictly smaller m than the first one. This is the essential uniform tail argument.

Finally, at k=1 and xi>6, the exponential series gives `exp(xi)>1+xi+xi^2/2+xi^3/6>1+xi+xi^2=P_1(xi)`. Therefore m_1(xi)<1, k_*<1 and beta_*>1. No decimal evaluation was needed.

## 4. Positivity classification and the excluded boundary (lines 113–137)

For k>k_*, the first minimum has G>0, every later minimum is larger than zero, all maxima are positive, and the initial segment rises from zero. Monotonicity between successive critical points covers every finite positive x. Thus the density is strictly positive on (0,infinity).

At k=k_*, the first minimum alone is zero, while every later minimum and every maximum is positive. Consequently there is exactly one positive-time zero, at t=xi/b. Analyticity/nonzero derivative between extrema excludes a zero interval. For k<k_*, the exact first-minimum value is negative.

For k>=k_*, the inverse is nonnegative, integrable because all decay rates are strictly negative, and has integral H(0)=1. It is therefore a probability density, including at the threshold.

For any nontrivial finite PH representation, take a subgenerator T, initial row alpha and exit vector w=-T1>=0. Choose lambda so `B=T+lambda I` is entrywise nonnegative. Accessibility of an exit from an initially positive state supplies m with `alpha B^m w>0`; otherwise every absorption path and hence the total absorption probability would vanish. For every positive t, the corresponding term of

`alpha exp(Tt)w=exp(-lambda t)Σ_(j>=0) t^j alpha B^j w/j!`

is strictly positive and all other terms are nonnegative. This works for reducible T and permits density zero at t=0. The manuscript correctly excludes the threshold density from finite PH without relying on a questionable closed-interval positivity convention. For k<k_*, Laplace-transform uniqueness and the negative inverse exclude a probability-density transform.

## 5. O'Cinneide import and all checked hypotheses (lines 139–150)

I directly read the current official [Liu–Yao–Zhang arXiv:2409.12673v2, Section 2](https://arxiv.org/html/2409.12673v2#S2), not merely the abstract. Its opening assumes a probability law on [0,infinity) with continuous **positive density on (0,infinity)** and gives the sufficient characterization when the rational LST has real coefficients, coprime numerator/denominator, value one at zero, and a unique pole of maximal real part. It then allows general pole multiplicities; there is no simple-complex-pole restriction on this characterization.

For the present H when k>k_*:

- f is a continuous strictly positive density on (0,infinity), as reconstructed above;
- H is rational with real coefficients;
- its constant numerator is positive, so it has no common root with the denominator;
- H(0)=1 and H tends to zero at positive infinity, so there is no atom at zero;
- its poles are -c (simple) and -a±ib (each double), with a>c>0 and b>0;
- therefore -c is the unique pole of greatest real part and the distribution is not concentrated at zero.

I also directly read [Commault–Mocanu's survey PDF, Section 2.2, Theorem 1](https://people.smp.uq.edu.au/YoniNazarathy/AMSIschool2016/CommaultMocanu_forAssignment.pdf). Its reader text uses a closed-at-zero positivity interval. The reviewed manuscript explicitly flags that rendering/convention and instead cites the modern open-interval statement, consistent with Erlang-type densities. Hence no zero-at-zero defect remains.

At the declared import boundary, the positive-side conclusion follows. The original long O'Cinneide 1990 proof was not reconstructed or formally authenticated by this review; the manuscript correctly states that limitation. This is an existence theorem, not an explicit PH construction or a minimum-order result on the remaining interval.

## Boundaries

The broad minimal-representation book question, exact minimum above the separately treated beta<=1/sqrt2 band, original-source proof authentication and novelty remain outside this review. The complete implicit threshold is supported as written, conditional only on the named characterization import for its PH-existence direction. The negative-density and positive-time-zero obstructions are elementary and do not depend on that import.
