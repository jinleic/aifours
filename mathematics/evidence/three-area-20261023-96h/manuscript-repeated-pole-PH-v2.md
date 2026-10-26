# Repeated-pole phase-type representations: exact-degree criterion, a sharp order5/6 band, an existence boundary and order divergence

Before-creation clock observed: **2026-10-23T13:26:45-07:00**. This manuscript consolidates four claims that completed the author, independent in-harness and parent written-check cycle. Their status is **WRITTEN_CHECKED at the precise import boundaries below / NOVELTY_UNCLEAR**. This new v2 assembly has not itself received a fresh independent snapshot review. Earlier manuscripts and review snapshots remain unchanged.

No scientific program, numerical root approximation, parameter enumeration, solver, Lean run or model CLI has been executed by this mathematics lane. Written checking is not a kernel proof, human peer review, cross-vendor gate or priority certification. A separate new seven-state candidate is explicitly excluded from the checked theorem table below.

## 1. Book problem, notation and scientific boundary

The source is *10000 Selected Problems in Sciences: Mathematics*, Science Press2009, ISBN978-7-03-024267-9, **Minimal Representation of Phase-Type Distribution**, Qiming He and Hanqin Zhang, printed pp.544–545 / PDF560–561. The actual local source extraction is [book-phase-type-pp544-545.txt](book-phase-type-pp544-545.txt). The full book question asks for a minimum-order representation of an arbitrary PH distribution. **That general problem is not solved here.**

A continuous-time PH representation of order N is a nonnegative row alpha with alpha1=1 and a real N-by-N Hurwitz Metzler matrix T satisfying T1<=0. Its transform is

    alpha(sI-T)^(-1)(-T1).

Order counts transient states, not the absorbing state. No acyclic, companion, irreducible-global, diagonalizable or moment-matching restriction is imposed on lower bounds.

Let a>c>0,b>0,r,q positive integers and set

    d=a-c, beta=b/d,
    D_{r,q}(s)=(s+c)^r((s+a)^2+b^2)^q,
    K_{r,q}=D_{r,q}(0)=c^r(a^2+b^2)^q,
    H_{r,q}(s)=K_{r,q}/D_{r,q}(s).

These are initially normalized rational functions, not automatically PH distributions. There is no numerator cancellation, so their algebraic degree is r+2q. The primary family below is H=H_{1,2}, with degree5 and a conjugate pair of double poles.

## 2. Four checked claims and exact trust boundaries

| Claim | Statement | Verification/trust boundary |
|---|---|---|
| **A: exact-degree criterion** | H_{r,q} has a PH representation of order r+2q iff beta^2<=1/(2ceil(q/r)+1). Whenever it does, that order is minimal. | Universal lower bound elementary; general upper bound imports Ellard–Smigoc2017 Theorem1.2, stating Laffey–Smigoc2006. Exact hypotheses and transfer-preserving construction are in §3. Original historical proof not authenticated here. |
| **B: exact minimum5/6** | For H_{1,2}, minimum5 when beta<=1/sqrt5 and minimum6 when1/sqrt5<beta<=1/sqrt2. Both endpoints included. | Direct explicit matrices, characteristic/transfer identities and all-topology five-state obstruction; no §3 spectral-existence import needed. |
| **E: all-beta PH existence** | With the exact beta_* in §5, H is PH iff0<beta<beta_*. At beta_* it has a nonnegative density with one positive-time zero and is not PH; above it the inverse transform is signed. | Density/sign/negative directions elementary. Positive-side finite PH existence imports O'Cinneide characterization as stated in accessible later primary sources. It is not an explicit order formula. |
| **O: order divergence** | For each fixed c,d>0, minimum PH order tends to infinity as beta approaches beta_* from below; quantified finite-order neighborhoods are given in §6. | Elementary robust nonnegative-Hankel-factorization lower bound. Finite existence uses the same E import. No quantitative constant was evaluated and no exact residual minimum is supplied. |

In particular the unresolved exact minimum-order band **(1/sqrt2,beta_*)** is retained. A failure of one six-state companion coefficient does not exclude arbitrary six-state realizations.

## 3. The exact-degree criterion

### 3.1 Denominator binding and irreducible-block lower bound

The reduced denominator of any N-state PH transform divides det(sI-T), because every resolvent entry is an adjugate polynomial divided by this characteristic polynomial. Hence N>=r+2q. At equality, the two monic degree-(r+2q) polynomials coincide:

    det(sI-T)=D_{r,q}(s).

The spectrum therefore contains -c exactly r times and -a+ib,-a-ib each q times, with no hidden eigenvalues. Nontrivial Jordan structure is allowed.

In Frobenius block triangular form, every irreducible Metzler diagonal block has a real algebraically simple spectral abscissa by Perron–Frobenius after a sufficiently large scalar shift. The only real spectral value available is -c; thus every block contains exactly one occurrence of -c. There are exactly r blocks. If the j-th block contains ell_j conjugate pairs, its dimension is2ell_j+1 and sum ell_j=q. Some ell_j>=L=ceil(q/r).

For such a block let M=T_j+cI, n=2ell_j+1. Its spectral traces, valid with algebraic multiplicities even for Jordan blocks, are

    tr M=-2ell_j d,
    tr M^2=2ell_j(d^2-b^2).

Its off-diagonal products are nonnegative, so

    tr M^2=sum_i m_ii^2+sum_(i!=j)m_ij m_ji
            >=sum_i m_ii^2 >=(tr M)^2/n.

Rearrangement gives beta^2<=1/(2ell_j+1)<=1/(2L+1). This covers every PH topology at exact algebraic degree.

### 3.2 Named classical theorem and one-real-pole block

**Imported theorem:** Ellard–Smigoc, *Diagonal elements in the Nonnegative Inverse Eigenvalue Problem*, [arXiv:1702.02650v1, Theorem1.2](https://arxiv.org/html/1702.02650v1#S1.Thmtheorem2), 8 Feb2017, stating Laffey–Smigoc2006. A self-conjugate list(rho,lambda2,...,lambdan), with rho>=0 and Re lambda_i<=0 for i>=2, is nonnegative-realizable iff s1>=0 and s1^2<=n s2. Moreover a realization C+eta I exists with C a nonnegative trace-zero companion matrix and eta>=0. Repeated list entries are allowed. The theorem statement/construction were read; the original2006 proof is not independently authenticated.

For ell>=1 with beta^2<=1/(2ell+1), put n=2ell+1 and gamma=2ell d/n. The list

    gamma, (-d/n+ib) repeated ell times,
           (-d/n-ib) repeated ell times

is self-conjugate with positive gamma and negative real parts elsewhere. It has s1=0 and s2=2ell(d^2/n-b^2)>=0. The imported theorem applies. Trace forces eta0, so it gives the nonnegative upper-shift companion C of

    P(x)=(x-gamma)((x+d/n)^2+b^2)^ell.

Set lambda=c+gamma, A=C-lambda I and k=c(a^2+b^2)^ell. Then A is Metzler and Hurwitz with eigenvalues -c and -a±ib, the latter each ell times, and

    P(s+lambda)=(s+c)((s+a)^2+b^2)^ell=:D_ell(s).

Solving the upper-shift companion equations yields

    e_1^T(sI-A)^(-1)e_n=1/D_ell(s).

The positive vector h_i=lambda^(i-1) satisfies -Ah=k e_n because P(lambda)=k. With S=diag(h_i), T=S^-1 A S and alpha=e_1^T, the matrix T is Hurwitz Metzler, -T1=S^-1 k e_n>=0, and alpha1=1. Its actual transform is k/D_ell(s). Thus the theorem's spectral realization has been converted into the prescribed transfer function, not simply asserted sufficient. For ell0 use the one-state exponential c/(s+c).

### 3.3 Cascade and sufficiency

Distribute q pairs among r nonnegative ell_j as evenly as possible, so max ell_j=L. Every corresponding block satisfies §3.2. If w_j=-T_j1, join successive blocks by w_j alpha_(j+1) above the diagonal. Nonfinal block row sums are zero, the last block absorbs, and block triangularity retains stability. The block resolvent gives the product of the normalized block transforms, exactly H_{r,q}. Dimension is sum_j(2ell_j+1)=r+2q. This proves A at its declared theorem-import boundary.

### 3.4 Required inherited falsifier and the multiplicity distinction

At r=q=1, A gives beta<=1/sqrt3=cot(pi/3), exactly the classical H_{1,1} order3 threshold and the n*=3 case of the previously completed simple-pole family. This is an inherited positive control/free falsifier, NOT new scientific credit.

H_{1,2} has two occurrences of each nonreal pole, not three distinct simple poles. An exact-degree5 realization has one real Perron occurrence, hence one irreducible block containing TWO nonreal pairs. Its trace inequality is4(d^2-b^2)>=16d^2/5, forcing beta<=1/sqrt5. The old simple-pole cot(pi/n) formula concerns one pair and allows hidden eigenvalues when n>3; substituting n5 into it does not determine the repeated-pole exact-degree threshold. This structural distinction resolves the apparent numerical discrepancy.

## 4. Explicit five- and six-state PH representations

Write K=c(a^2+b^2)^2 throughout this section.

### 4.1 Five states

For b^2<=d^2/5, set

    t=d/5, lambda=a-t=c+4t, v=t^2+b^2,
    U=12t^2-2v, V=16t^3+4tv,
    W=v(16t^2-v), Z=4tv^2.

U>=0 and V,W,Z>0 since v<=6t^2. Direct multiplication gives

    P5(x)=(x-4t)(x^2+2tx+v)^2
          =x^5-Ux^3-Vx^2-Wx-Z.

Define T5 by diagonal-lambda, superdiagonal lambda, and final row

    (Z/lambda^4,W/lambda^3,V/lambda^2,U/lambda,-lambda),

and alpha5=e_1^T. Its eigenvalues are -c and -a±ib each twice. The first four row sums vanish and the last exit isP5(lambda)/lambda^4=K/lambda^4>0. Its companion resolvent gives transform K/P5(s+lambda)=H. Thus it is PH, including the endpoint U0. Degree5 makes this order minimal.

### 4.2 Six states with one explicit cancellation

For b^2<=d^2/2, put

    A=d^2-2b^2>=0,
    B=b^2(2d^2-b^2)>0,
    C=d^2b^4>0.

The polynomial identity is

    P6(x)=(x^2-d^2)(x^2+b^2)^2=x^6-Ax^4-Bx^2-C.

Take T6 with diagonal-a, superdiagonal a and final row

    (C/a^5,0,B/a^3,0,A/a,-a),

and initial row

    alpha6=(d/(c+2d),a/(c+2d),0,0,0,0).

The initial mass is1 since a+d=c+2d. The first five row sums are zero, the last exit isP6(a)/a^5=K(c+2d)/a^5>0, and the spectrum is -c,-(c+2d),-a±ib each twice. Thus this is Hurwitz and Metzler.

For a direct transfer check before diagonal scaling, use the upper-shift companion C6, G=C6-aI, w=K e6 and u=d e1^T+e2^T. With z=s+a, its resolvent gives

    u(sI-G)^(-1)w=K(z+d)/P6(z)
      =K(s+c+2d)/[(s+c)(s+c+2d)((s+a)^2+b^2)^2]
      =H(s).

The positive scaling vector h_i=a^(i-1)/(c+2d) satisfies -Gh=w and gives exactly T6,alpha6 above. No signed numerator or initial weight is used. At b^2=d^2/2, A0 is allowed while B,C remain positive.

The exact-degree trace argument excludes every order5 representation once beta^2>1/5, and degree excludes lower orders. Therefore T6 is minimal on1/5<beta^2<=1/2. This proves B.

## 5. An exact all-parameter PH-existence threshold

Let xi be the unique root of tan x=x in(2pi,5pi/2). For k>=0,x>0 define

    P_k(x)=1+kx+(1+k^2)x^2/2,
    m_k(x)=exp(-kx)P_k(x)/sqrt(1+x^2).

For each fixed x>0,

    partial_k m_k(x)=-(1+k^2)x^3 exp(-kx)/(2sqrt(1+x^2))<0.

Also m_0(x)>1, since(1+x^2/2)^2-(1+x^2)=x^4/4, and m_k(x) tends to0 as k tends to infinity. Therefore exactly one k_*>0 solves m_(k_*)(xi)=1. Put beta_*=1/k_*.

### 5.1 Exact inverse transform and all extrema

For k=d/b and Delta=d^2+b^2, inverse transformation gives

    f(t)=K exp(-ct) g(t),
    g(t)=integral_0^t exp(-du)(sin(bu)-bu cos(bu))/(2b^3)du
        =G_k(bt)/Delta^2,

where

    G_k(x)=1-exp(-kx)[(1-k(1+k^2)x/2)cos x
                     +(k(k^2+3)/2+(1+k^2)x/2)sin x].

This follows by differentiating the basic sine Laplace transform with respect to b, then integrating and shifting. Independently G_k(0)=0 and

    G_k'(x)=((1+k^2)^2/2)exp(-kx)(sin x-x cos x).

The nonzero positive roots of sin x-x cos x are one per interval(jpi,jpi+pi/2), j>=1; none lie in the intervening intervals. The signs alternate from positive near0. Thus odd j are maxima and even j minima. At these roots the bracket simplifies to P_k(x). At every maximum G=1+m_k(x)>0; at every minimum G=1-m_k(x). The first minimum is at xi.

### 5.2 Uniform control of every later minimum

At k=1/xi, with y=sqrt(1+xi^2),

    m_(1/xi)(xi)=exp(-1)(y/2+2/y)>1,

because xi>2pi>6, y/2>3 and e<3. Strict decrease in k gives k_*xi>1. Direct differentiation also gives

    (partial_x log m_k)P_k(x)(1+x^2)
      =(x^2/2)[(1-k^2)x-k(3+k^2)-k(1+k^2)x^2].

When kx>=1, the bracket is at most x-kx^2-k(3+k^2)<0. Therefore for k>=k_* and x>=xi, m_k is strictly decreasing. The first minimum consequently controls every later one, not just the first observed oscillation.

It follows that G_k is strictly positive for x>0 if k>k_*; is nonnegative with exactly one positive-time zero xi if k=k_*; and is negative at xi if k<k_*. Its limit at infinity is1. At k1, the exponential series and xi>6 give exp(xi)>1+xi+xi^2=P_1(xi), hence k_*<1 and beta_*>1. No decimal root value has been used.

### 5.3 Strict boundary and exact source import

For k>=k_* the inverse density is nonnegative, integrable, continuous and has integral H(0)=1. At k<k_* its negative value rules out a probability transform by Laplace uniqueness.

Every nonzero finite PH density is strictly positive for each t>0: choose lambda with B=T+lambda I>=0. Accessibility of an exit supplies some m with alpha B^m(-T1)>0; then its positive term in

    alpha exp(Tt)(-T1)=exp(-lambda t)
      ·sum_(j>=0)t^j alpha B^j(-T1)/j!

is positive for every t>0. This excludes k=k_*, where the fixed analytic inverse has the positive-time zero xi/b. Changing a density at one point does not evade this conclusion: any PH analytic density with the same transform agrees with this continuous inverse everywhere.

For k>k_*, apply **O'Cinneide's characterization**, as stated in [Commault–Mocanu2003 §2.2](https://people.smp.uq.edu.au/YoniNazarathy/AMSIschool2016/CommaultMocanu_forAssignment.pdf) and in [Liu–Yao–Zhang, arXiv:2409.12673v2 §2](https://arxiv.org/html/2409.12673v2#S2), 15 Feb2025: a probability law with continuous positive density on(0,infinity), rational real transform, coprime numerator/denominator, value1 at0 and a unique pole of greatest real part is PH. All hypotheses hold here: -c is simple and dominates -a±ib, each double. The modern open-interval version permits zero density at0. The source PDF's reader rendering with a closed interval is not adopted literally.

The original1990 characterization proof was not authenticated (publisher access returned403). Thus the positive-side conclusion retains this named theorem-level import; the negative and boundary directions do not depend on it. This proves E at that exact boundary, not a minimum-order formula in the residual PH region.

## 6. Minimum order diverges at the density-zero boundary

Fix c,d>0 and vary b=beta d. Let t_*=xi/(beta_* d), f_*=f_(beta_*), and J=[3t_*/4,5t_*/4]. At xi, G=G'=0 and

    G_(k_*)''(xi)=((1+k_*^2)^2/2)exp(-k_*xi)xi sin xi>0.

The density's prefactors are positive, so f_*''(t_*)>0. The ratio f_*(t)/(t-t_*)^2 extends continuously and positively on J, with value f_*''(t_*)/2 at t_*. Define its positive minimum C0.

Choose a rectangle beta in[beta_*-e0,beta_*], t in J, with0<e0<beta_*/2, and finite constants

    C1=1+max|partial_beta f_beta(t)|,
    M0=1+max|f_beta(t)|.

Then for delta=beta_*-beta,

    |f_beta(t)-f_*(t)|<=C1 delta,
    f_beta(t_*)<=C1 delta,
    0<=f_beta(t)<=M0 below beta_*.

### 6.1 Robust factorization lemma

If a nonnegative k-by-k matrix has diagonal<=epsilon, off-diagonal>=m>0 and every entry<=M0, then it has no nonnegative factorization of inner dimension at most r when

    k>2^r, epsilon<m^2/(4r^2 k M0).

To prove it, normalize every nonzero column of a purported U factor to sum1, inversely scaling V, and discard zero factors. Then U entries<=1 and V entries<=kM0. Put tau=m/(2r k M0) and S_i={ell:U_iell>=tau}. If S_i were contained in S_j for i!=j, the outside contribution to M_ij would be at most m/2. The diagonal M_jj<=epsilon forces each inside V_ell j<=epsilon/tau, so the inside contribution is at most r epsilon/tau<m/2. This contradicts M_ij>=m. Thus the S_i are all distinct, impossible for k>2^r. The proof covers padding to fewer than r active factors.

For any order-n PH density,

    f(s_i+t_j)=[alpha exp(Ts_i)][exp(Tt_j)(-T1)]

is a nonnegative factorization with inner dimension n, by the Metzler semigroup. Hence the lemma lower-bounds PH order, not merely ordinary Hankel rank.

### 6.2 Quantified forbidden r-state neighborhoods

For r>=1 put k=2^r+1, h=t_*/[4(k+1)], s_i=t_*/2+ih and t_j=t_*-s_j. All times are positive and their sums t_*+(i-j)h lie in J. At the boundary, off-diagonal entries are at least C0h^2, while the diagonal is zero. For sufficiently small delta>0 the neighboring matrix has off-diagonal>=m=C0h^2/2 and diagonal<=C1delta.

An explicit sufficient neighborhood radius is

    epsilon_r=min(e0/2,
                  C0h^2/(4C1),
                  C0^2h^4/(32C1 r^2 k M0)).

For every0<delta<epsilon_r, the robust lemma excludes all r-state PH representations. Choose any fixed positive C no larger than both

    C0 t_*^2/(64 C1),
    C0^2 t_*^4/(8192 C1 M0).

Then the two variable terms dominate C/[r^2(k+1)^5], giving

    epsilon_r>=min(e0/2,C/[r^2(2^r+2)^5]).

No k-dependent factor has been suppressed. Combining this lower exclusion for each r with E's finite PH existence below beta_* proves that the finite minimum tends to infinity. The transform degree stays5 and no poles coalesce. This proves O. No exact residual minimum, optimal rate, numerical constant or instantiated matrix assay is claimed.

## 7. Verification record and provenance

The original claims were checked on pinned snapshots, not on this new consolidation's bytes:

* A/B source [proof-repeated-pole-PH-v1.md](proof-repeated-pole-PH-v1.md), SHA256 `ae4d983da5de5f897b262c92dd7594aac1905e2cdfcc6b6f8b5cb9e43b89bb6f`; independent [InfoResearch96h review](../../../information-science/evidence/three-area-20261023-96h/peer-review-mathematics-PH-v1.md), SHA256 `07a1c89eae77ba1a5dc1efc878f5460fa1c79212960a416c06b6fcd0370c2fdd`,0F/0M/0m; [parent written check](../../../institute/runs/three-area-2026-10-23-96h/mathematics-parent-check-v1.md), SHA256 `85b9d919d504b5e6d2fd16dfe1893544d921adacce4d5f2537ffe949a1088e32`.
* E source [proof-H12-PH-existence-threshold-v1.md](proof-H12-PH-existence-threshold-v1.md), SHA256 `a35c865eaf977b065635e31ee13b4e101306d69f8b7562470b6bafc3a82a1a32`; independent [PhysicsResearch96h review](../../../physics/evidence/three-area-20261023-96h/peer-review-H12-existence-threshold-v1.md), SHA256 `1e43a7aeb83097b1e6ae0652520b1cf1b935fb854753d261c5a70feec71df435`,0F/0M/0m; [parent check](../../../institute/runs/three-area-2026-10-23-96h/mathematics-existence-parent-check-v1.md), SHA256 `97d6c9640efd1aeba29fbcea94591c6d43f54d6082c92aacab46617bb31190cc`.
* O source [proof-H12-order-blowup-v1.md](proof-H12-order-blowup-v1.md), SHA256 `f7e26a155b9cbd3b58dc7c29d08da53eb1e8fdba9dbc19cd1d6e149be5f4d353`; independent [PhysicsResearch96h review](../../../physics/evidence/three-area-20261023-96h/peer-review-math-order-blowup-v1.md), SHA256 `a5f847ab7571efc76405f1423e9a3d3f9c002c462203d13e07085f26870be722`,0F/0M/0m; parent wave record [007](../../../institute/runs/three-area-2026-10-23-96h/checkpoints/007-wave-complete-v1.json) records completion of all four mathematics written-check cycles.
* [Addendum001](addendum-001-PH-baseline-and-pole-multiplicity-v1.md), SHA256 `7c46ad1fd68780e4669118e7e89db60f17ef0a4f87d10cd96c673a2c1e0f7482`, supplies the explicit inherited(1,1) falsifier and the multiplicity/cotangent distinction now integrated into §3.4.

**Mandatory parent-clock qualification:** several parent record timestamps were estimates, not observations. They must be read with [parent-timestamp-erratum-v1.md](../../../institute/runs/three-area-2026-10-23-96h/parent-timestamp-erratum-v1.md), SHA256 `1ad365961ba16360450eaa8b694ad82fe25bf663dc024b5e12801398e0dc8b01`. This manuscript cites those authorities by path/hash and does not repeat their estimated labels as observed times. The author's own clock above was actually returned by date.

## 8. Novelty and the still-active primary target

All core mechanisms are classical: Perron/Frobenius blocks, trace/JLL bounds, companions, positive diagonal normalization, cascades/cancellation, rational-density analysis, PH characterization and nonnegative Hankel factorizations. P1 in particular is plausibly an explicit classical corollary. The [matched primary comparison](primary-comparison-002-PH-repeated-poles-v1.md) includes current2025 PH minimality work,2026 discrete-time complexity,2020 spectral bounds and2023 logarithmic complete monotonicity; it does not clear priority. No first/best/major/publication-ready claim is made.

The book's general minimum-PH question and the broad exact H_{1,2} minimum on(1/sqrt2,beta_*) remain unresolved. The new [seven-state extension candidate](proof-H12-seven-state-extension-v1.md), SHA256 `59618311924521e8eceaa5179f837589aa2f1cd15955006aace5f39ee559fe4d`, proposes an upper bound7 on beta^2 in[1/2,53/96]. It is a SEPARATE new candidate outside the existing four verified results; it does not imply minimum7 and must receive its own check. No other target or reserve has been activated.
