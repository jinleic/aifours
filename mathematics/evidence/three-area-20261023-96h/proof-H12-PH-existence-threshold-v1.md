# H_{1,2}: an exact all-parameter PH-existence threshold

Status: **CANDIDATE / NOVELTY_UNCLEAR**. This is a further written attack on the already frozen broad H_{1,2} target, not a new simultaneous target. No computation or numerical root-finding has been performed. The non-PH direction is elementary; the PH-existence direction imports O'Cinneide's characterization at the exact source boundary in §6. This does not determine the minimum order throughout the PH region.

## 1. Exact statement

For a>c>0 and b>0 define d=a-c, k=d/b and

    H(s)=c(a^2+b^2)^2 / [(s+c)((s+a)^2+b^2)^2].

Let xi be the unique root of tan x=x in (2pi,5pi/2). This is the second positive nonzero root of sin x-x cos x=0. Define, for k>=0 and x>0,

    P_k(x)=1+kx+(1+k^2)x^2/2,
    m_k(x)=exp(-kx) P_k(x)/sqrt(1+x^2).

There is a unique k_*>0 satisfying

    m_{k_*}(xi)=1.

**Candidate theorem E.** H is the Laplace transform of a finite continuous-time PH distribution if and only if k>k_*. Equivalently, with beta=b/d and beta_*=1/k_*, it is PH iff 0<beta<beta_*. At beta=beta_* its inverse transform is a nonnegative probability density with an isolated positive-time zero and is NOT PH. For beta>beta_* its inverse transform takes a negative value, so it is not even a probability-density transform.

This is an exact implicit constant definition, not a numerical approximation. In particular beta_*>1, as proved below. The earlier explicit minimum-order5/6 interval beta<=1/sqrt2 is strictly inside the PH-existence region.

## 2. Exact inverse transform and its derivative

Put Delta=d^2+b^2 and K=c(a^2+b^2)^2. Shifting the Laplace variable by c gives

    H(s)=K / [z((z+d)^2+b^2)^2], z=s+c.

The inverse transform of 1/((z+d)^2+b^2)^2 is

    exp(-dt)(sin(bt)-bt cos(bt))/(2b^3).

For example, differentiate the identity L[exp(-dt)sin(bt)/b]=1/((z+d)^2+b^2) with respect to b to obtain this formula; the differentiations are elementary and justified by exponential decay. Division by z then integrates from0 to t. Thus the unique inverse transform of H is

    f(t)=K exp(-ct) g(t),
    g(t)=integral_0^t exp(-du)(sin(bu)-bu cos(bu))/(2b^3) du.

Write x=bt, k=d/b. A closed form, checked by differentiating and evaluating at0, is

    g(t)=G_k(bt)/Delta^2,
    G_k(x)=1-exp(-kx)[(1-k(1+k^2)x/2) cos x
                     +(k(k^2+3)/2+(1+k^2)x/2) sin x].

Indeed G_k(0)=0 and

    G_k'(x)=((1+k^2)^2/2) exp(-kx)(sin x-x cos x).

The preceding integral and closed form therefore agree exactly. No evaluation at selected parameter values is used as a proof premise. As t tends to infinity, G_k(bt) tends to1, because k>0.

## 3. Every possible positive-time minimum

For x>0, put R(x)=sin x-x cos x. Its positive roots consist of exactly one root x_j in each interval

    (j pi,j pi+pi/2), j=1,2,... .

There is no root in the intervening intervals, where tan x is negative; on each displayed interval tan x-x rises from a negative number to infinity, with derivative tan^2 x and hence a unique root. Also R is positive near0. Its signs alternate at these roots. Consequently the x_j with j odd are local maxima of G_k, and the x_j with j even are local minima. The first minimum is xi=x_2.

At a critical point sin x=x cos x, the bracket in G simplifies exactly:

    (1-k(1+k^2)x/2)+(k(k^2+3)/2+(1+k^2)x/2)x
      =1+kx+(1+k^2)x^2/2=P_k(x).

For j even, cos x_j=+1/sqrt(1+x_j^2), and hence

    G_k(x_j)=1-m_k(x_j).

For j odd, cos x_j=-1/sqrt(1+x_j^2), so

    G_k(x_j)=1+m_k(x_j)>0.

Thus only the even critical points can obstruct positivity.

## 4. Unique threshold and why the first minimum suffices

For every fixed x>0,

    partial_k m_k(x)
      =-((1+k^2)x^3/2) exp(-kx)/sqrt(1+x^2) < 0.

At k=0,

    m_0(x)=(1+x^2/2)/sqrt(1+x^2)>1,

because (1+x^2/2)^2-(1+x^2)=x^4/4>0. As k tends to infinity, m_k(x) tends to0. Therefore m_k(xi)=1 has exactly one solution k_*>0, by continuity and strict decrease.

A useful exact bound is

    k_* xi > 1.

To prove it, evaluate at k=1/xi. With y=sqrt(1+xi^2),

    m_{1/xi}(xi)=exp(-1)(xi^2+5)/(2sqrt(1+xi^2))
               =exp(-1)(y/2+2/y)>1.

Here xi>2pi>6 gives y/2>3, whereas e<3. Since m decreases in k, the solution k_* must exceed1/xi.

Now differentiate m_k with respect to x. Since all omitted factors are strictly positive, the sign of partial_x m_k(x) is the sign of

    Q_k(x)=(1-k^2)x-k(3+k^2)-k(1+k^2)x^2.

More explicitly,

    (partial_x log m_k(x)) P_k(x)(1+x^2)
       =x^2 Q_k(x)/2.

If kx>=1, then

    Q_k(x) <= x-kx^2-k(3+k^2) < 0.

For k>=k_* and x>=xi, we have kx>=k_*xi>1. Thus m_k(x) is strictly decreasing on [xi,infinity). Every later local minimum has smaller m_k than the first one. This is the substantive step preventing an unjustified inference from checking only a single oscillation.

It follows that:

* If k>k_*, the first minimum satisfies G_k(xi)>0 and every later minimum is strictly positive. All maxima are positive. G_k rises from0 before its first maximum, is monotone between successive critical points, and tends to1; hence G_k(x)>0 for every x>0.
* If k=k_*, the first minimum is exactly0; every other positive local minimum is strictly positive. Thus G_k(x)>=0 for x>=0, with precisely one positive-time zero x=xi.
* If 0<k<k_*, then G_k(xi)<0. Consequently f(xi/b)<0.

This proves the complete positivity/nonpositivity classification of the inverse transform.

For a further exact bound, m_1(xi)<1: since xi>6, the exponential series gives

    exp(xi)>1+xi+xi^2/2+xi^3/6>1+xi+xi^2=P_1(xi),

and sqrt(1+xi^2)>1. Thus k_*<1 and beta_*>1. No decimal root value has been computed.

## 5. The threshold density is a probability density but cannot be PH

For k>=k_*, f(t)>=0 and is integrable: its closed form is a finite sum of polynomial-exponential-trigonometric terms with strictly negative real decay rates. Its integral is H(0)=1, by the exact Laplace-transform identity. Therefore it is a probability density on [0,infinity).

Every nontrivial finite PH density is strictly positive at every t>0. An elementary proof avoids relying on the wording of a characterization theorem: write w=-T1>=0 and choose lambda large enough that B=T+lambda I is entrywise nonnegative. Since alpha(sI-T)^(-1)w has total mass1, there is a path from some positive initial state to some positive exit state. For a path of length m, alpha B^m w>0. Then for all t>0,

    alpha exp(Tt)w=exp(-lambda t) sum_{j>=0} t^j alpha B^j w/j! > 0.

If no such path existed every term would vanish and total absorption mass would be0, contradicting the probability representation. This argument works with reducible matrices and permits zero density at t=0.

At k=k_* the exact density f has the positive-time zero t=xi/b, so it cannot be PH. For k<k_* a negative density value already rules out any probability or PH interpretation. These non-PH statements require no computational or external existence theorem.

## 6. Classical theorem used for the positive side

For k>k_*, the density just proved strictly positive has a rational Laplace transform and a unique pole of maximal real part, namely -c, since a>c and the other two poles -a+ib,-a-ib have order2. Its integral is1 and it is not concentrated at0.

**Named import:** O'Cinneide1990, *Characterization of phase-type distributions*, as stated in Commault–Mocanu2003 Theorem1, and in the opening of §2 of Liu–Yao–Zhang arXiv:2409.12673v2 (15 Feb2025). The latter states the version with a continuous positive density on (0,infinity), so zero density at0 is allowed. A probability distribution with a rational transform and a unique pole of maximal real part, whose density is positive on (0,infinity), is PH.

Sources actually opened:

* [Commault–Mocanu2003 primary PDF, §2.2](https://people.smp.uq.edu.au/YoniNazarathy/AMSIschool2016/CommaultMocanu_forAssignment.pdf), Theorem1; its reader text renders a closed interval at0, so this manuscript does not adopt that endpoint literally.
* [Liu–Yao–Zhang2025 official HTML, §2](https://arxiv.org/html/2409.12673v2#S2), explicitly using (0,infinity) and allowing general rational denominator multiplicities. Introduction also cites the underlying characterization literature.

Every substantive hypothesis has been checked above. At this theorem-level import boundary, H is therefore PH for k>k_*. The conclusion is existence of SOME finite PH representation, not its minimum order and not an explicit formula in the remaining band. The long original characterization proof has not been independently authenticated or formalized here.

## 7. What this changes and what remains open

Together with `proof-repeated-pole-PH-v1.md`, this candidate divides the primary H_{1,2} parameter space into:

1. beta<=1/sqrt5: exact minimum5, explicit parameters;
2. 1/sqrt5<beta<=1/sqrt2: exact minimum6, explicit parameters;
3. 1/sqrt2<beta<beta_*: PH existence from the named characterization theorem; exact minimum NOT determined;
4. beta=beta_*: nonnegative density with one positive-time zero, no finite PH representation;
5. beta>beta_*: a signed inverse transform, hence not PH.

Because beta_*>1, the unresolved minimum-order band is nonempty; it is not hidden by the existence theorem. No claim is made that order6 fails immediately above1/sqrt2. The displayed six-state coefficient changing sign was only an ansatz obstruction.

The original minimal-representation book problem remains open. Correctness and novelty are separate: the candidate is an elementary density/oscillation analysis assembled with a classical characterization theorem and may have an earlier equivalent in positivity/positive-realization literature. Searches for repeated complex PH poles and fifth-order external positivity located no exact comparison in the sources opened, but that bounded failure is NOT novelty clearance. No external contact or publication occurred.

## 8. Independent written check requested

Reconstruct the inverse transform; verify G_k' and both partial derivatives of m_k; prove all critical points and signs are covered; check the k_*xi>1 argument and the strict/excluded boundary; confirm the exact (0,infinity) hypotheses of the characterization source. No root approximation or parameter enumeration is needed. Written checking is not kernel acceptance.
