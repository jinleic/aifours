# Bounded-real strong-surrogate bounds: integrated delivery v2

Before-creation clock observation: **2026-10-23T13:22:37-07:00**. This is the consolidated manuscript requested by the parent, not the end of the 96-hour round.

**Correctness status:** the five result packets below completed author, independent in-harness and parent written-reconstruction cycles; their scopes are **WRITTEN_CHECKED at the in-harness level**. This v2 integrates those unchanged mathematical claims and applies the explicit binary-domain clarification. The new integration has not itself had a fresh independent full-manuscript review. It is neither kernel/formal nor human/cross-vendor acceptance.

**Every result retains NOVELTY_UNCLEAR; the Kuroki 2013 full-theorem gate remains ACCESS_BLOCKED.** This manuscript does not claim scientific priority, publication readiness, a full solution of the book's causal-inference programme, statistical inference or clinical applicability.

## 1. Source, scope and result map

Book: *10000 Selected Problems in Sciences: Information Science*, Science Press 2011, ISBN 978-7-03-031911-1; article *Causal inference*, Zhi Geng, printed pp.596–599 / PDF pp.617–620. The actual printed p.597 image, `sources/book-causal-0618.png`, was opened. It describes positive treatment-to-surrogate and surrogate-to-outcome effects coexisting with a negative treatment-to-outcome effect. The modern model below is a precise scoped instantiation of that paragraph, not a literal list of parameters specified by the book.

Matched baseline: [Yin–Liu–Geng–Luo, arXiv:1607.05454v1, Theorem 1](https://arxiv.org/html/1607.05454v1), published as [doi:10.1111/sjos.12398](https://doi.org/10.1111/sjos.12398), supplies sharp bounds in the all-binary model and explicitly leaves continuous primary outcomes to future work in its Discussion. Those binary bounds remain prior art. Recent [Hsiao–Tian–Parast 2025](https://arxiv.org/html/2506.12194v1) and [their empirical-assumption paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC12382359/) have different sufficient-assumption/cross-study sensitivity interfaces. No dominance over those frameworks is claimed.

| Packet | Exact result integrated here | Verification/novelty boundary |
|---|---|---|
| A | Complete compatible delta interval for arbitrary [0,1] factual laws, atomic simultaneous attainment, and sharp strict-positive threshold | WRITTEN_CHECKED in-harness; NOVELTY_UNCLEAR; Kuroki ACCESS_BLOCKED |
| B | Two data-only quantile optimizers and explicit median/clamp selectors for every gamma | WRITTEN_CHECKED in-harness; NOVELTY_UNCLEAR; Kuroki ACCESS_BLOCKED |
| C | For every finite raw-moment order k, smooth positive symmetric factual laws match those moments but have opposite sharp sign conclusions | WRITTEN_CHECKED in-harness; NOVELTY_UNCLEAR; Kuroki ACCESS_BLOCKED |
| D | Two least nondecreasing 1-Lipschitz tail majorants are a complete invariant for the entire bound curve at fixed p,q,g_min | WRITTEN_CHECKED in-harness; NOVELTY_UNCLEAR; Kuroki ACCESS_BLOCKED |
| E | Under positive h and gamma, U>=0, with a complete U>0/U=0 classification including ceiling exceptions | WRITTEN_CHECKED in-harness; NOVELTY_UNCLEAR; Kuroki ACCESS_BLOCKED |

Packets A–E depend only on the probability model, elementary tail rearrangement, real convexity/calculus and the constructions below. There is no numerical or external causal-theorem import in their proofs. The prior binary theorem is used for comparison, not as a premise. The reserve SOF source correction is separate and is not part of this five-result stack.

## 2. Model and unnormalized tail integrals

Let S_0,S_1 be binary and let Y_0,Y_1 be arbitrary random variables in [0,1], with unrestricted joint dependence. A subscript on Y means intervention on the **surrogate**, not treatment. Strong surrogacy means the primary outcome under treatment t is Y_(S_t). Randomized treatment T can be generated independently of the whole latent tuple; observed S=S_T and Y=Y_(S_T).

Inputs are the full untreated joint law

    mu_s(A)=P(S_0=s,Y_s in A), s=0,1,

for every Borel set A, the treated surrogate marginal q=P(S_1=1), and the externally supplied causal mean gamma=E[Y_1-Y_0]. Gamma is not asserted identified from mu_0,mu_1,q. No individual monotonicity, rank invariance, parametric outcome family or hidden-confounder independence is assumed. Atoms and zero-mass strata are included.

Write

    p_s=mu_s([0,1]), p=p_1, p_0=1-p,
    m_s=integral y mu_s(dy),
    h=q-p, g_min=m_1-m_0-p, eta=gamma-g_min,
    delta=E[Y_(S_1)-Y_(S_0)]
         =E[(S_1-S_0)(Y_1-Y_0)].                           (1)

For 0<=x<=p_s define the lower and upper tail integrals

    ell_s(x)=inf { integral y a(y)mu_s(dy):
                    0<=a<=1, integral a dmu_s=x },
    u_s(x)=sup { integral y a(y)mu_s(dy):
                    0<=a<=1, integral a dmu_s=x }.           (2)

If Q_s(v)=inf{y:mu_s([0,y])>=v}, 0<v<p_s, then

    ell_s(x)=integral_0^x Q_s(v)dv,
    u_s(x)=integral_(p_s-x)^p_s Q_s(v)dv.                   (3)

For p_s=0 these functions are defined at x=0 and equal zero. Both extrema are attained by taking a lower/upper tail and splitting a possible cutoff atom using an independent uniform variable. For example, if a_* selects an upper tail of mass x at cutoff c, then for every other selector of mass x,

    integral (y-c)(a_*(y)-a(y))mu_s(dy)>=0.

The equal masses cancel the c term, proving optimality; lower-tail optimality is analogous. This proves (3) as well. Both tails are nondecreasing, continuous and 1-Lipschitz; ell_s is convex and u_s concave. In particular 0<=ell_s(x)<=u_s(x)<=x. The splitting changes no observed outcome value.

A fixed outcome interval [a,b], a<b, reduces to [0,1] by an affine transformation, with gamma/delta scaled by b-a. Unbounded outcomes, continuous surrogates, censoring and non-strong surrogacy are not covered.

## 3. Packet A: complete sharp interval and attainment

**Status: WRITTEN_CHECKED in-harness; NOVELTY_UNCLEAR; Kuroki ACCESS_BLOCKED.**

Let

    I=[max(0,h),min(p_0,q)],
    t=r-h for r in I,
    F_eta(r)=(t-eta)_+ +(r+eta-1)_+-u_0(r)-u_1(t),
    G_eta(r)=t+min(eta,r)-(t+eta-1)_+-ell_0(r)-ell_1(t).     (4)

I is nonempty for p,q in [0,1]. Its r,t satisfy 0<=r<=p_0, 0<=t<=p and r+t<=1.

### Theorem A1

The data are compatible if and only if

    g_min<=gamma<=g_min+1, equivalently 0<=eta<=1.           (5)

For compatible data, the exact attainable set of delta is [L,U], where

    L=min_(r in I) F_eta(r),
    U=max_(r in I) G_eta(r).                               (6)

Both endpoints and every intermediate value are attained by full laws preserving the complete mu_s, q and gamma. F_eta is convex and G_eta concave on I.

### Proof

Put B=S_0 and y=Y_B. Define the missing-outcome budget

    Z=Y_1 on B=0,  Z=1-Y_0 on B=1.

Then Z is in [0,1] and

    Y_1-Y_0=-y+Z on B=0,
    Y_1-Y_0=y-1+Z on B=1.

Thus gamma=g_min+E[Z], proving necessity of (5). Conversely sample (B,y) from the mu_s, put Z=eta, recover the missing outcome as above, and independently choose S_1 with probability q. This constructs a compatible law for every eta in [0,1], so there is no additional compatibility restriction.

Let C={B=0,S_1=1}, D={B=1,S_1=0}, with masses r,t. The treated marginal gives q=p+r-t, and the two stratum mass constraints give exactly I. Conversely every r in I is implemented by selecting mass r from stratum 0 and mass t from stratum 1. Put A_0=E[y 1_C], A_1=E[y 1_D]. Then

    delta=t-A_0-A_1+E[Z1_C]-E[Z1_D].                       (7)

At fixed switch partition the sharp budget bounds are

    -min(eta,t)+(eta-1+r)_+
      <=E[Z1_C]-E[Z1_D]
      <=min(eta,r)-(eta-1+t)_+.                            (8)

For the lower bound fill the coefficient -1 group D first, then the nonswitch group of coefficient 0, then C of coefficient +1. Their masses are t,1-r-t,r. This produces -eta up to eta=t, then -t up to eta=1-r, then -t+eta-1+r. The displayed lower formula is exactly these cases. It also follows directly from E[Z1_D]<=min(eta,t) and E[Z1_C]>=(eta-(1-r))_+. Filling C first, then nonswitch positions, then D proves and attains the upper bound. A fractional last group is split or assigned a constant Z; zero-mass groups need no division.

At fixed r,t, select upper factual tails for the minimum, giving A_0=u_0(r), A_1=u_1(t), and lower tails for the maximum. These choices and (8) are **simultaneous**: after choosing the observed-y selectors, Z changes only the missing potential outcome and never the factual y. Substitution into (7) gives exactly F_eta and G_eta. Thus each value in (4) is attained by a literal law, even with cutoff atoms.

Continuity on compact I attains the global extrema. Every compatible law is bounded by those same steps. Mixing complete endpoint laws preserves both entire factual measures, q and gamma and interpolates delta across [L,U]. Finally F_eta is a sum of convex hinges minus concave tails, and

    G_eta=r+t-(r-eta)_+-(t+eta-1)_+-ell_0(r)-ell_1(t)

is concave. QED.

### Theorem A2: sharp positive-effect threshold

Set

    W(r)=u_0(r)+u_1(r-h),
    B_*=max_(r in I)[1-r+W(r)],
    Gamma_*=g_min+B_*.                                    (9)

For compatible data with h>0 and gamma>0, every law has strictly positive delta if and only if gamma>Gamma_*. At gamma=Gamma_* the lower bound is zero. If W is not identically zero, gamma<Gamma_* implies an attained L<0. If W is identically zero, L>=0 for all compatible gamma, but gamma>Gamma_* is still the exact criterion for L>0.

**Proof.** Since t<=1-r,

    F_eta(r)=distance(eta,[t,1-r])-W(r).

Hence F_eta(r)<=0 exactly when eta lies in J_r=[t-W(r),1-r+W(r)]. If r_max is the upper endpoint of I, all base intervals [t,1-r] contain [r_max-h,1-r_max], nonempty because r_max+t_max<=1. The J_r therefore have a common point, and their union is the compact interval [A_*,B_*], with A_*=min(t-W). For h>0, r_min=h,t=0, so A_*<=0. Also g_min<=0; gamma>0 gives eta>0. Thus L>0 iff eta>B_*, proving the threshold. At equality a maximizer in (9) gives F=0 and all other F are nonnegative.

When W>0 somewhere, its concavity/nonnegativity make it positive at every interior point of nondegenerate I. The open intervals giving F<0 have the same limiting endpoint extrema A_*,B_* and a common point, so their union is (A_*,B_*). Since eta>0>=A_*, eta<B_* gives L<0. Singleton I with W>0 is immediate. If W is identically zero, F is a distance and cannot be negative. QED.

If eta>=1-r_min, every first hinge in F is zero and every second hinge is active; therefore

    L=eta-B_*=gamma-Gamma_*.                               (10)

This high-gamma branch is exact, not an approximation.

### Analytic example with explicit attaining law

Let mu_0=mu_1=(1/2)Uniform[0,1], q=3/4. Then p=1/2, h=1/4, g_min=-1/2, I=[1/4,1/2], ell_s(x)=x^2 and u_s(x)=x-x^2. The function 1-r+W(r)=1+t-r^2-t^2 is maximized at r=3/8,t=1/8, giving B_*=31/32 and Gamma_*=15/32. For gamma in [1/4,1/2],

    L=gamma-15/32.                                        (11)

To attain it, sample B uniform binary and y uniform [0,1]. For B=0 set S_1=1 iff y>=1/4; for B=1 set S_1=0 iff y>=3/4. On C set Z=(8gamma-1)/3 and off C set Z=1; recover missing outcomes as above. Then q=3/4, E[Z]=gamma+1/2 and

    u_0(3/8)=15/64, u_1(1/8)=7/64,
    delta=(3/8)(8gamma-1)/3-22/64=gamma-15/32.

Thus gamma=2/5 admits delta=-11/160, while gamma=49/100 forces delta>=17/800>0. The factual laws are smooth; missing potential-outcome marginals may have atoms, as allowed.

Replacing the two conditional uniforms by Bernoulli(1/2) preserves p_s,m_s,q and gamma but gives u_s(x)=min(x,1/4) and L=gamma-1/2 on the same gamma band. At gamma=49/100 a negative law with delta=-1/100 is then attained. This explains why merely substituting means into a binary formula loses information; it does not contradict the prior binary theorem.

## 4. Packet B: two fixed optimizers for every gamma

**Status: WRITTEN_CHECKED in-harness; NOVELTY_UNCLEAR; Kuroki ACCESS_BLOCKED.**

Define

    Wbar(r)=r+(r-h)-ell_0(r)-ell_1(r-h),
    r_minus in argmax_I[W(r)-r],
    r_plus in argmax_I[Wbar(r)-r].                          (12)

Wbar is the combined upper tail for reflected outcomes y'=1-y and has the same nonnegative, nondecreasing, concave, 2-Lipschitz properties as W. These optimizers depend only on the factual data and q, not gamma.

Let clamp_I denote projection to I and med the middle of three real numbers. Exact optimizing masses are

    r_L(eta)=clamp_I(med(h+eta,1-eta,r_minus)),
    r_U(eta)=clamp_I(med(h+1-eta,eta,r_plus)).                (13)

Thus L=F_eta(r_L), U=G_eta(r_U) for every compatible eta, including ties, atoms, endpoint maxima and singleton I.

**Proof.** For a concave W with increments in [0,2 times the argument increment], f(r)=(r-a)_++(r-b)_+-W(r) is nonincreasing below min(a,b), nondecreasing above max(a,b), and equals r-min(a,b)-W(r) between them. On that middle interval it is minimized by projecting any global minimizer of r-W(r) onto that interval intersected with I. If the intersection is empty, the appropriate endpoint of I is optimal. In all cases the result is clamp_I(med(a,b,r_0)). Take a=h+eta,b=1-eta for L. Reflecting both potential outcomes changes delta to -delta and eta to 1-eta, because g_min changes to -1-g_min. Direct substitution gives -F_ref_(1-eta)=G_eta. Apply the same lemma with Wbar for U. QED.

At differentiability points the two data-only crossings are

    Q_0(p_0-r)+Q_1(p-(r-h))=1,
    Q_0(r)+Q_1(r-h)=1,                                    (14)

respectively, with the appropriate endpoint/subgradient conditions in general. No differentiability or uniqueness is an assumption in (12)–(13).

## 5. Packet D: exact lossless envelopes for the entire curve

**Status: WRITTEN_CHECKED in-harness; NOVELTY_UNCLEAR; Kuroki ACCESS_BLOCKED.**

For every real m define

    E_W(m)=max_(r in I)[W(r)-(r-m)_+].                      (15)

Restricted to I, this is the least nondecreasing 1-Lipschitz majorant of W, and it is concave. If r_0 maximizes W-r and K=max_I(W-r), then

    E_W(m)=m+K       for m<=r_0,
           W(m)     for r_0<=m<=u,
           W(u)     for m>=u,                              (16)

where u is the upper endpoint of I. Any choice in a flat argmax gives the same function.

**Proof.** Each fixed-r expression in (15) is nondecreasing and 1-Lipschitz in m; its maximum has those properties and majorizes W on I by choosing r=m. Every nondecreasing 1-Lipschitz majorant g satisfies g(m)>=g(r)-(r-m)_+>=W(r)-(r-m)_+, proving leastness. Joint concavity in (r,m), mixing maximizing r values in convex I, proves concavity. Split (15) into r<=m and r>=m. The first part maximizes W at the largest allowed r; the second maximizes m+(W-r). Concavity of W-r gives (16). If it has a flat maximum, W(r)=r+K there, so the cases agree for every optimizer choice. QED.

Every feasible r satisfies 2r-h=r+t<=1. The two lower hinge locations sum to 1+h, so their larger value is >=(1+h)/2>=r and its hinge is zero. Therefore the complete endpoint curves are

    L(gamma)=-E_W(min(h+eta,1-eta)),
    U(gamma)= E_Wbar(min(h+1-eta,eta)).                    (17)

In particular (13) simplifies on the actual feasible domain to

    r_L=clamp_I(max(r_minus,min(h+eta,1-eta))),
    r_U=clamp_I(max(r_plus,min(h+1-eta,eta))).               (18)

This is exactly the earlier median convention, not a changed optimizer.

The summary is necessary as well as sufficient. Fix p,q and g_min. For any m in I, eta=m-h is a feasible t and 2m-h<=1 gives min(h+eta,1-eta)=m. Taking eta=m similarly gives min(h+1-eta,eta)=m. Consequently

    E_W(m)=-L(g_min+m-h),
    E_Wbar(m)=U(g_min+m),  m in I.                         (19)

Their restrictions to I also determine the outside extensions: K=E_W(l)-l at I's lower endpoint l, the extension below l is m+K and above u is constant E_W(u). Thus two factual-law pairs with the same p,q,g_min have identical complete sharp-bound curves iff their two envelope restrictions agree. This is a complete **population identified-interval invariant**, not recovery of the factual laws or finite-sample statistical sufficiency. The sign threshold is the single functional

    Gamma_*=g_min+1+E_W(l)-l.                              (20)

## 6. Packet C: no finite ordinary-moment order determines the sign

**Status: WRITTEN_CHECKED in-harness; NOVELTY_UNCLEAR; Kuroki ACCESS_BLOCKED.**

### Theorem C

For every integer k>=0 there are two C-infinity strictly positive symmetric densities f,g on [0,1], with exactly matching raw moments through degree k, such that mu_0=mu_1=(1/2)f(y)dy versus (1/2)g(y)dy, the same q=3/4 and the same compatible gamma>0 yield opposite sharp conclusions: every law in the f model has delta>0, while the g model admits delta<0.

This rules out a fixed finite truncation of ordinary moments, not arbitrary finite summaries: Gamma_* itself is a purpose-built scalar for the sign decision.

### Proof

For a strictly positive continuous symmetric density F, its quantile Q is continuous, strictly increasing and Q(1-u)=1-Q(u). Using the same F in both half-mass strata fixes g_min=-1/2,h=1/4,I=[1/4,1/2]. The derivative of W(r)-r is

    Q(1-2r)+Q(3/2-2r)-1,

strictly decreasing and zero at r=3/8. Writing A_F=integral_0^(1/4)Q(v)dv, symmetry gives W(3/8)=3/8-A_F and hence

    Gamma_*(F)=1/2-A_F.                                   (21)

For uniform f=1, A_f=1/32 and Gamma_*(f)=15/32.

Put alpha=1/4 and delta_0=1/16. Choose an even smooth cutoff chi, equal to 1 near zero and supported in [-delta_0,delta_0]. One explicit choice is

    theta(t)=0 for t<=0, exp(-1/t) for t>0,
    chi(v)=theta(delta_0^2-v^2)/
       [theta(delta_0^2-v^2)+theta(v^2-(delta_0/2)^2)].       (22)

The denominator is positive because the two theta arguments cannot both be nonpositive. Flatness of theta at zero makes chi C-infinity, even, 1 on |v|<=delta_0/2 and 0 on |v|>=delta_0.

Choose n even, n>k, n>=2, and define

    phi(x)=(x-alpha)^(n-2)chi(x-alpha),
    psi(x)=phi(x)+phi(1-x), H(x)=psi^(n)(x).                (23)

The two supports lie in [3/16,5/16] and [11/16,13/16], strictly inside (0,1). H is symmetric, and all endpoint derivatives of psi vanish. Integrating by parts n times proves

    integral_0^1 x^j H(x)dx=0, j<n.                        (24)

H is not zero: otherwise psi would be a polynomial of degree<n with compact support in (0,1), contradicting its nonzero local polynomial bump. If M=max|H|>0, then f_epsilon=1+epsilon H is a normalized symmetric C-infinity density bounded below by 1/2 for |epsilon|<1/(2M), with every raw moment through k equal exactly to the uniform's.

Let x_epsilon be its lower quartile. The implicit equation integral_0^(x_epsilon)f_epsilon=alpha has x_0=alpha and x'_0=-integral_0^alpha H. Since A(epsilon)=integral_0^(x_epsilon)x f_epsilon(x)dx,

    A'(0)=integral_0^alpha(x-alpha)H(x)dx
         =-psi^(n-2)(alpha)=-(n-2)!<0.                    (25)

The second equality uses two integrations by parts; the endpoint terms at zero vanish and the factor x-alpha vanishes at alpha. Near alpha only the unreflected polynomial bump remains, giving the factorial.

Thus for sufficiently small positive epsilon, Gamma_*(f_epsilon)>15/32, while both thresholds remain <1/2 because A_F>0. Take g=f_epsilon and gamma the midpoint of their two thresholds. Both factual models have p_s=1/2,m_s=1/4,q=3/4 and g_min=-1/2, so gamma is positive and compatible with both. Their raw moments through k agree exactly. Theorem A2 gives L_f>0 and L_g<0 with attained endpoints. For an explicit negative law in the g model, select upper factual quantile masses 3/8 and 1/8, put Z=(8gamma-1)/3 on C and Z=1 off C; its value is gamma-Gamma_*(g)<0. QED.

The proof remains valid for k=0 because symmetry already fixes the common mean. Smooth moment-annihilating perturbations are classical; the separate priority gate remains open.

## 7. Packet E: exact sign of the upper endpoint

**Status: WRITTEN_CHECKED in-harness; NOVELTY_UNCLEAR; Kuroki ACCESS_BLOCKED.**

### Theorem E

For compatible data with h>0,gamma>0, U>=0. Moreover U>0 iff either

- mu_0([0,1))>0; or
- mu_0 is concentrated at 1 and q<1, mu_1([0,1))>0, gamma<m_1 all hold.

Every other compatible case under these premises has U=0.

### Proof

For positive selected mass x, ell_s(x)<x iff the corresponding measure has positive mass below 1: select some of that mass and complete the selection arbitrarily. Otherwise concentration at 1 gives ell_s(x)=x. Also ell_s(x)<=m_s.

Since eta=gamma+m_0+p-m_1>m_0, the feasible monotone switch choice r=h,t=0 gives

    G_eta(h)=min(eta,h)-ell_0(h)>=0.

If mu_0 has mass below 1, both eta and h strictly exceed ell_0(h), giving U>0.

In the remaining case m_0=p_0,ell_0(r)=r. Compatibility gives gamma<=m_1; set kappa=m_1-gamma>=0. Then eta=1-kappa>p_0>=r, and the exact entire upper optimization becomes

    U=max_(0<=t<=min(p,1-q))[min(t,kappa)-ell_1(t)].         (26)

If q=1, or kappa=0, or mu_1 is concentrated at 1, the objective is <=0 everywhere and zero at t=0. Conversely if none holds, compatibility and gamma>0 imply p>0; choose 0<t<=min(p,1-q,kappa). Then ell_1(t)<t and (26) is positive. QED.

U>=0 guarantees at least one compatible nonharmful law, not absence of the paradox. A negative L may coexist. In the binary specialization, writing a,b,c,d below, U>0 iff c>0 or [c=0,q<1,d>0,gamma<b]; the complementary ceiling cases have U=0. This is consistent with the existing binary theorem.

## 8. Exact recovery of the prior binary baseline

This appendix is not a new binary result. It corrects a distinction in the original v1 comparison and supplies a complete direct algebraic reduction.

### 8.1 Binary factual versus binary potential outcomes

The bounded-real model with binary factual y=Y_B still permits nonbinary missing outcomes; its full feasible-law set is not literally Yin's all-binary set. Retain B,y,S_1,Z and adjoin independent uniform V. Let Z'=1{V<=Z}, so E[Z'|B,y,S_1,Z]=Z. On B=0 set Y'_0=y,Y'_1=Z'; on B=1 set Y'_1=y,Y'_0=1-Z'. Both potential outcomes are binary, while mu_s and q remain exactly unchanged. Equations gamma=g_min+E[Z] and (7), affine in Z, show gamma and delta remain unchanged by conditional expectation. Conversely binary laws are already bounded-real laws. Therefore the two models have exactly the same attainable **gamma/delta projections**, not the same full law sets.

### 8.2 Four-hinge reduction and both endpoint lists

Write a=mu_0({1}), b=mu_1({1}), c=mu_0({0}), d=mu_1({0}), so a+b+c+d=1. Then g_min=-a-d, eta=gamma+a+d, h=q-b-d, u_0(r)=min(r,a),u_1(t)=min(t,b). Hence

    F(r)=sum_(j=1)^4(r-beta_j)_+-2r+h,
    (beta_1,beta_2,beta_3,beta_4)
       =(h+eta,1-eta,a,h+b).                               (27)

The unconstrained minimizer interval is between the second and third ordered beta values; its minimum is max_(i<j)(h-beta_i-beta_j). The six pair values are -1, -gamma-2a-d, -gamma-q-a, gamma+q-b-1, gamma-2b-c and -a-b. The -1 term is redundant.

Lower-domain clipping cannot remove all unconstrained minimizers: beta_1,beta_4>=h and beta_2,beta_3>=0 imply the third ordered beta>=max(0,h). If the middle interval lies above u=min(a+c,q), exactly one beta can be <=u. When u=a+c it must be beta_3=a and F(u)=q-1-a; when u=q it must be beta_4=q-d and F(u)=-b-q. If the two upper endpoints coincide, two anchors are <=u and this clipped case cannot occur. Both extra expressions bound every feasible F from below because F>=-a-t>=-a-(1-q) and F>=-r-b>=-q-b. Thus in all cases

    L=max{
       -a-(1-q), -a-b, -b-q,
       -gamma-q-a, -gamma-d-2a,
        gamma-2b-c, gamma-(1-q)-b }.                        (28)

Complement both potential outcomes. This invertibly maps (a,b,c,d,gamma,delta) to (c,d,a,b,-gamma,-delta), so

    U=min{
        c+(1-q), c+d, d+q,
        gamma+a+2d, gamma+d+(1-q),
       -gamma+2c+b, -gamma+c+q }.                           (29)

These are exactly the seven lower and seven upper pieces actually read in Yin et al.'s Theorem 1. The calculation is independent of importing its elimination/sharpness proof; the Bernoulliization establishes the exact domain bridge. The all-binary result remains prior art.

## 9. Dependency and verification receipts

Original files remain immutable. SHA-256 identities (metadata pins, not proof authentication):

| Source packet | SHA-256 |
|---|---|
| `proof-bounded-outcome-sharp-bounds-v1.md` | `618ee5c5fc3ebc503f4dc730d70572dbc807036fd49efc87ef65d2e798643a82` |
| operative `proof-bounded-outcome-sharp-bounds-ADDENDUM-1.md` | `e0ea69c9d4a4848f09aeb1f742038c8c5371a1ceceda8f298b61d771f2dddf9b` |
| `proof-binary-reduction-v1.md` | `f69c07b271985742025d95d827df565683536d02286d11c4aedd17f9eee96408` |
| `proof-gamma-independent-selectors-v1.md` | `52b33a6766c6d4cfd0a76638801a39747b82761f86ac54fd868a4601f239c429` |
| `proof-no-finite-moment-sign-summary-v1.md` | `71690f0d301a581f448dc42b58559b0ee0a1b3ff310a841e296dc1979d9e94da` |
| `proof-tail-envelope-characterization-v1.md` | `ddad3ac40668af6363a9e69fa489bfc67406c17f96abe7e9db79569338859ce5` |
| `proof-upper-endpoint-sign-v1.md` | `35fa16a6570a91c1f8722e1f49ed29a6b43c980f08cb82c4a0d2e720b6a57306` |

Read the actual peer returns and parent records, not an inferred blanket approval:

- Math lane `peer-review-info-bounded-outcome-v1.md`: `a1e5ed5b231c92ce2a2261342bcee756fc1b5ba9398c4121651d11ab8216ddc6`; **0F/0M/1MINOR**, binary feasible-law wording repaired explicitly above. That historical count is not rewritten as a clean original pass.
- Math lane `peer-review-info-moment-barrier-v1.md`: `5e28383d23fcd4ad5502fbeb6bb2aeecb6a825a2ffff60708cd9aa8c16990868`; **0F/0M/0m**.
- Physics lane `peer-review-info-gamma-selectors-v1.md`: `dea3c0daeadcc2a38035eded4c8afb56512f4092594fd50777a5f451fe611413`; **0F/0M/0m**.
- Physics lane `peer-review-info-tail-envelope-v1.md`: `d1cb2adeadafdf18b074f87c1006f73fa60f21da12a78f1fffa341992828d6fb`; **0F/0M/0m**.
- Physics lane `peer-review-info-upper-endpoint-sign-v1.md`: `0d5594b593eeb80b045d6aa92d3c28fbbd80b9d7dcdd2539a5a01db45bd40e55`; **0F/0M/0m**.
- Parent `institute/runs/three-area-2026-10-23-96h/information-parent-check-v1.md`: `93c6eaf1809933bae8194808c097aacb62d0605f9be9f4c5787971aaae0ee500`.
- Parent completed-wave receipt `checkpoints/007-wave-complete-v1.json`: `d0a37960c7355bdda238b0206f71c9fb3734d1e888663218c1b54cfb02ee22d7`, plus `006-envelope-sign-v1.json` for the two latest conclusions. These paths are relative to the new institute round. Their verdicts are cited by identity, not adopted as this lane's clock observations.

The first source exploration preceded `selection-v1.md`; that chronology departure remains disclosed. This lane ran no scientific program, solver, enumeration or proof assistant. Source extraction, ordinary public retrieval and hashes are not scientific verification. Parent verification specifics are owned by the parent records, not retroactively described as this lane's actions. All independent checks here are ordinary in-harness written checks, not a specific unavailable vendor gate.

## 10. Prior-art gate and final scientific boundary

`primary-source-comparison-v1.md` records the actual comparison and access failures. Kuroki, *Sharp bounds on causal effects using a surrogate endpoint*, Statistics in Medicine 32(25):4338–4347 (2013), [doi:10.1002/sim.5873](https://doi.org/10.1002/sim.5873), has an authenticated publisher/NCBI abstract claiming closed-form sharp surrogate bounds under various assumptions. The complete theorem's outcome domain, the regime of its P(S,Y), its use of an external ACE(S->Y) input, and its monotonicity hypotheses remain **UNKNOWN**.

Static publisher full/epdf/pdf routes returned 403; the deposited TDM route returned 400; a normal browser encountered a security-verification page and was closed without bypass. OpenAlex, Semantic Scholar, Europe PMC, CiNii and OpenAIRE provide abstract/closed-location metadata, not a full authenticated theorem. Author/institutional routes found so far have not supplied it. These observations are not proof of global unavailability or nonoverlap.

Therefore every packet A–E remains **NOVELTY_UNCLEAR / Kuroki ACCESS_BLOCKED** even though the local mathematical arguments are written-checked. Neither “first continuous-outcome sharp surrogate bound” nor its denial is established. Rearrangement, trimmed means, convex envelopes, moment-annihilating bumps and latent Bernoulliization are classical ingredients; no new general causal framework is claimed.

The bounded obligations of the frozen model are delivered at their stated scope. The book's unrestricted causal-inference programme, continuous-surrogate and unbounded/survival extensions, observational identification of gamma, statistical uncertainty, clinical validation, formal proof and scientific priority are not resolved by this manuscript. The parent authorized transition to the separately frozen SOF reserve; no automatic runtime or scientific-execution authority follows from that transition.

### Operative timestamp overlay

All affected parent records cited here must be read with `institute/runs/three-area-2026-10-23-96h/parent-timestamp-erratum-v1.md`. Its ten listed parent timestamp labels were estimates rather than observations; the operative bounds and immutable originals are preserved there. This manuscript uses their path/hash verdict interfaces only and does not adopt any of those labels as a lane-observed clock. The overlay changes no mathematical statement or review count.
