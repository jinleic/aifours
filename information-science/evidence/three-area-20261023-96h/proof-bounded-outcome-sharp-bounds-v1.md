# Sharp strong-surrogate bounds for an arbitrary bounded real endpoint

**Status: CANDIDATE; NOVELTY_UNCLEAR.** Complete written derivation by the information-science lane, after `selection-v1.md`. No scientific program, independent mathematical check, finite verification, proof assistant or human review has been performed. Exploratory pre-freeze reasoning is disclosed in the selection. This manuscript does not solve the book's full causal-inference programme. Its theorem is a bounded-real extension of the model in Yin–Liu–Geng–Luo, not a claim to rediscover their binary theorem.

## 1. Model, supplied information and notation

Let S_0,S_1 take values in {0,1}. Let Y_0,Y_1 be arbitrary random variables in [0,1]. No restriction is imposed on their joint dependence. The subscript on Y denotes **intervention on the surrogate**, not treatment. Strong surrogacy means that treatment-specific primary outcomes are Y_(S_0) and Y_(S_1). A randomized treatment T, independent of all four potential variables, can be added at the end; observed outcomes are S=S_T, Y=Y_(S_T).

We are supplied with:

- the complete untreated joint law, represented by measures

      mu_s(A) = P(S_0=s, Y_s in A),  s=0,1,

  for Borel subsets A of [0,1];
- q=P(S_1=1);
- the external causal mean gamma=E[Y_1-Y_0].

The measures mu_s are nonnegative and their masses sum to one. Write

    p_s = mu_s([0,1]),   p = p_1,   p_0=1-p,
    m_s = integral y mu_s(dy),
    h = q-p,
    g_min = m_1-m_0-p,
    eta = gamma-g_min.

The quantity to identify is

    delta = E[Y_(S_1)-Y_(S_0)]
          = E[(S_1-S_0)(Y_1-Y_0)].                  (1)

This is population partial identification, not finite-sample inference. The information gamma is not claimed identified from (mu_0,mu_1,q). We allow atoms, zero-mass strata, hidden confounding, randomized latent assignments and arbitrary nonmonotone surrogate responses. No rank invariance or individual monotonicity is assumed.

A general fixed outcome interval [a,b], a<b, reduces to this model by (Y-a)/(b-a); gamma and delta scale by b-a. Unbounded outcomes, censoring and continuous surrogates are outside this theorem.

## 2. Tail-integral notation

For a finite measure mu_s of mass p_s, and 0<=x<=p_s, define

    ell_s(x) = inf { integral y a(y) mu_s(dy) :
                     0<=a<=1, integral a dmu_s=x },
    u_s(x)   = sup { integral y a(y) mu_s(dy) :
                     0<=a<=1, integral a dmu_s=x }.             (2)

The endpoint notation is deliberately lower-case: u_s is an upper **tail integral**, not a potential outcome.

Equivalently, if Q_s(v)=inf{y in [0,1]: mu_s([0,y])>=v} is the unnormalized quantile for 0<v<p_s,

    ell_s(x) = integral_0^x Q_s(v) dv,
    u_s(x)   = integral_(p_s-x)^p_s Q_s(v) dv.                  (3)

When p_s=0, both functions are defined only at 0 and equal 0. Quantile values at endpoints do not affect these integrals.

### Lemma 1: tail extrema and their attainment

Both extrema in (2) are attained. For the upper extremum, take all y above a cutoff, none below it, and an appropriate fraction at the cutoff; for the lower extremum take the lower tail instead. These selections are realizable by an auxiliary uniform random variable when an atom must be split. They preserve the original distribution of y.

**Proof.** Choose a cutoff c satisfying mu_s((c,1])<=x<=mu_s([c,1]), using c=0 or c=1 if needed. Let a_*(y) be 1 above c, 0 below c and a constant in [0,1] at c such that its mass is x. For any other feasible a,

    integral (y-c)(a_*(y)-a(y)) mu_s(dy) >= 0.

The mass constraint cancels the c term, proving optimality. The lower-tail statement is identical with the inequalities reversed. Integrating the corresponding quantile intervals gives (3), also with atoms. The auxiliary-randomization construction gives a literal joint distribution implementing every fractional selection. QED.

Consequently u_s is concave, ell_s is convex, both are continuous and 1-Lipschitz, and

    0<=ell_s(x)<=u_s(x)<=x.                                   (4)

## 3. Main identified-set theorem

Let

    I = [ max(0,h), min(p_0,q) ].                              (5)

This interval is always nonempty for p,q in [0,1]. For r in I, put t=r-h. Then 0<=r<=p_0, 0<=t<=p and r+t<=1.

For a real a, write a_+=max(a,0). Define

    F_eta(r) = (t-eta)_+ + (r+eta-1)_+
               -u_0(r)-u_1(t),                              (6)

    G_eta(r) = t+min(eta,r)-(t+eta-1)_+
               -ell_0(r)-ell_1(t).                           (7)

### Theorem 1

The supplied data are compatible with at least one joint law of (S_0,S_1,Y_0,Y_1) if and only if

    g_min <= gamma <= g_min+1,  equivalently 0<=eta<=1.         (8)

For compatible data, the complete attainable set of delta is the closed interval [L,U], where

    L = min_(r in I) F_eta(r),
    U = max_(r in I) G_eta(r).                                (9)

Both endpoints and every intermediate value are attained by actual laws preserving the entire measures mu_0,mu_1, not merely their means. The optimization for L is one-dimensional and convex; that for U is one-dimensional and concave.

### Proof, step 1: missing-outcome normalization

Put B=S_0 and y=Y_B, which is exactly the untreated observable. Define

    Z = Y_1       on B=0,
    Z = 1-Y_0     on B=1.

Then 0<=Z<=1, and pointwise

    Y_1-Y_0 = -y+Z        on B=0,
    Y_1-Y_0 = y-1+Z       on B=1.                             (10)

Taking expectations gives gamma=g_min+E[Z]. This proves necessity of (8). Conversely, for any eta in [0,1], sample (B,y) from the given measures, set Z=eta, recover the missing outcome using (10), and independently choose S_1 with probability q of being 1. This realizes all supplied information. Thus (8) is sufficient and no additional data-compatibility condition is missing.

### Step 2: the only switch-mass degree of freedom

For any compatible law, let

    C={B=0,S_1=1},  D={B=1,S_1=0},
    r=P(C),         t=P(D).

The treated surrogate marginal is q=p+r-t, so t=r-h. The elementary mass constraints are exactly r in I. Conversely any r in I can be implemented by selecting mass r from the B=0 stratum and mass t from the B=1 stratum. The remaining two nonswitch strata have masses p_0-r and p-t. There is no additional observable restriction on their coupling.

Let

    A_0=E[y 1_C],  A_1=E[y 1_D].

By (1) and (10),

    delta = t-A_0-A_1 + E[Z 1_C]-E[Z 1_D].                  (11)

In particular, for fixed r,t the observed-y term and the Z-allocation term can be optimized separately: assigning Z never changes y=Y_B.

### Step 3: exact allocation of the missing-outcome budget

For every Z in [0,1] with E[Z]=eta,

    -min(eta,t)+(eta-1+r)_+
       <= E[Z 1_C]-E[Z 1_D]
       <= min(eta,r)-(eta-1+t)_+.                           (12)

Both bounds are attainable for every fixed partition C,D and the nonswitch set.

To minimize, place the available Z-budget first on the coefficient -1 set D of mass t, then on the coefficient 0 nonswitch set of mass 1-r-t, and finally on the coefficient +1 set C of mass r. The resulting value is

    -eta                   if 0<=eta<=t,
    -t                     if t<=eta<=1-r,
    -t+(eta-1+r)           if 1-r<=eta<=1.

This is exactly the lower expression in (12). A fractional final group can be assigned a constant Z or split by an auxiliary uniform variable. Conversely, the exchange of Z-budget from a larger coefficient to a smaller coefficient never increases the objective, proving optimality; equivalently the two elementary bounds E[Z 1_D]<=min(eta,t) and E[Z 1_C]>=max(0,eta-(1-r)) prove the same lower bound directly, with the ordered fill showing simultaneous equality. Filling C, then the nonswitch set, then D gives the upper expression. This proof covers zero-mass groups without division by them.

### Step 4: exact selection of the observed outcomes

At fixed r,t, Lemma 1 gives

    ell_0(r)<=A_0<=u_0(r),
    ell_1(t)<=A_1<=u_1(t).                                  (13)

For the minimum of (11), choose the upper tails in both strata, so A_0=u_0(r), A_1=u_1(t), and use the minimum Z-allocation. Its value is

    t-u_0(r)-u_1(t)-min(eta,t)+(eta-1+r)_+
      = F_eta(r).

For the maximum, select lower tails in both strata and the maximum Z-allocation. This gives G_eta(r). All these choices are simultaneous literal constructions: first sample (B,y), use the tail selectors to choose S_1, and then allocate Z across the three coefficient groups. Finally set Y_1=Z when B=0 and Y_0=1-Z when B=1. The factual outcome Y_B remains y in each case. Thus no unattainable threshold-by-threshold optimization is being combined.

### Step 5: optimizing the masses and filling the interval

The interval I is compact. The continuous functions F_eta and G_eta attain their respective optima, so the preceding construction attains L and U. Every compatible law has some r in I and is bounded by (11)–(13), proving no value lies outside [L,U]. Mixtures of an attaining lower law and an attaining upper law preserve mu_0,mu_1,q and gamma, while varying delta linearly across [L,U]. A randomized T independent of the resulting potential variables completes a structural model with an arbitrary nontrivial randomization probability.

Finally, u_s is concave and ell_s convex. Equation (6) is a sum of convex hinges minus concave functions. For (7), use

    G_eta(r)=r+t-(r-eta)_+-(t+eta-1)_+-ell_0(r)-ell_1(t).

This is concave. Theorem 1 follows. QED.

## 4. A sharp positive-effect threshold

The two positive causal premises of the average surrogate paradox are h>0 and gamma>0. They do not suffice by themselves. Theorem 1 yields an explicit sharp extra threshold using the full untreated outcome distribution.

For r in I put

    W(r)=u_0(r)+u_1(r-h),
    B_* = max_(r in I) [1-r+W(r)],
    Gamma_* = g_min+B_*.                                    (14)

The maximand in B_* is concave and continuous. Importantly, the optimizer and Gamma_* do **not** depend on the supplied gamma.

### Theorem 2

Assume compatible data, h>0 and gamma>0. Then every compatible law has strictly positive delta if and only if

    gamma > Gamma_*.                                        (15)

At gamma=Gamma_* (if compatible), the sharp lower bound is zero. Below the threshold, positive delta is not guaranteed; this alone is not a claim that a strictly negative delta is always attainable in every degenerate data set.

If W is not identically zero on I, the stronger trichotomy holds:

    gamma<Gamma_*  implies L<0,
    gamma=Gamma_*  implies L=0,
    gamma>Gamma_*  implies L>0.                             (16)

If W is identically zero, L>=0 for every compatible gamma, while (15) remains the exact criterion for L>0.

### Proof

For any r in I, t=r-h and t<=1-r. Hence (6) is

    F_eta(r)=distance(eta,[t,1-r])-W(r).                     (17)

For fixed r the condition F_eta(r)<=0 is therefore exactly

    eta in J_r=[t-W(r), 1-r+W(r)].                           (18)

All J_r share a common point. Indeed, writing r_max for the upper endpoint of I, every interval [t,1-r] contains every point in [r_max-h,1-r_max]; this latter interval is nonempty because 2r_max-h=r_max+t_max<=1. The family J_r has continuous endpoints over a compact interval. Its union is the closed interval

    [ A_*, B_* ], where A_*=min_(r in I)[t-W(r)].             (19)

One can also prove the union assertion directly: a family of intervals with a common point covers every point between its smallest left endpoint and its largest right endpoint. Here those extrema are attained.

Since h>0, r_min=h and t=0 there, so A_*<=-W(h)<=0. Also g_min<=0 by 0<=m_1<=p and m_0>=0. Since gamma>0, eta=gamma-g_min>0. Thus eta cannot lie strictly below A_*. Equations (17)–(19) imply

    L>0 iff eta>B_* iff gamma>Gamma_*.

At eta=B_* all F_eta(r)>=0, with equality at a maximizer of 1-r+W(r), proving L=0.

For the strict-negative statement, if W(r)>0 then F_eta(r)<0 precisely on the open interval with the same endpoints as J_r. These open intervals also share a common point. If W is nonzero and I has positive length, concavity and nonnegativity of W imply W>0 throughout the interior of I. Thus the endpoints obtained using only W>0 have the same infimum/supremum A_*,B_* as in (19), by continuity. If I is a singleton with W>0, the assertion is immediate. Consequently the union of the strict-negative intervals is (A_*,B_*). Since eta>0>=A_*, eta<B_* gives L<0. If W is identically zero, (17) instead shows F_eta>=0 everywhere. QED.

### Corollary 2.1: high-gamma linear branch

For any compatible data, if

    eta >= 1-r_min,

then eta>=t for every r in I, and r+eta-1>=0 for every r in I. Therefore

    L=eta-B_*=gamma-Gamma_*.                                (20)

The implication eta>=t follows from t<=1-r<=1-r_min. This corollary is useful for exact analytic examples; it is not an approximation.

## 5. Analytic real-outcome example and a distributional delta

Take

    mu_0=(1/2) Uniform[0,1],
    mu_1=(1/2) Uniform[0,1],
    q=3/4.

Then p=1/2, h=1/4, m_0=m_1=1/4, g_min=-1/2, eta=gamma+1/2 and I=[1/4,1/2]. Compatibility is -1/2<=gamma<=1/2. Direct integration gives, for x in [0,1/2],

    ell_s(x)=x^2,  u_s(x)=x-x^2.

Consequently, with t=r-1/4,

    1-r+W(r)=1+t-r^2-t^2.

This concave quadratic is uniquely maximized at r=3/8, t=1/8. Its value is 31/32. Thus

    Gamma_* = 15/32.                                       (21)

For every gamma in [1/4,1/2], Corollary 2.1 applies, and

    L=gamma-15/32.                                         (22)

This supplies both exact negative and positive regimes with smooth **factual** outcome distributions. For example gamma=2/5 gives L=-11/160, while gamma=49/100 gives L=17/800>0. These are analytic identities, not numerical experiment outputs.

### An explicit law attaining (22)

For gamma in [1/4,1/2], sample B uniformly from {0,1} and y uniformly from [0,1], independently. Put

- if B=0, set S_1=1 exactly when y>=1/4;
- if B=1, set S_1=0 exactly when y>=3/4.

Thus C has mass 3/8 and D mass 1/8, and P(S_1=1)=3/4. Let

    c=(8 gamma-1)/3,
    Z=c on C,  Z=1 off C.

Here 1/3<=c<=1. On B=0 set Y_0=y,Y_1=Z; on B=1 set Y_1=y,Y_0=1-Z=0. This realizes the prescribed mu_s and

    E[Y_1-Y_0]=(3/8)c+1/8=gamma.

The selected upper-tail factual integrals are

    u_0(3/8)=15/64,  u_1(1/8)=7/64.

Therefore

    delta=(3/8)c-15/64-7/64=gamma-15/32.

All properties are explicit and can be reconstructed without a solver. The unobserved counterfactual marginal may have atoms; no claim that every potential-outcome marginal is absolutely continuous is made.

### Why the complete observed distribution matters

Replace both conditional factual Uniform[0,1] distributions by Bernoulli(1/2), retaining the same p_s,m_s,q and gamma. Thus the masses of the four (S_0,Y_(S_0)) binary cells are all 1/4. Then

    u_s(x)=min(x,1/4).

For gamma in [1/4,1/2], every r in I gives

    F_eta(r)=gamma-1/2,

so L=gamma-1/2. In particular at gamma=49/100 this compatible binary-factual model attains delta=-1/100, although the full uniform-factual law forces delta>=17/800. Any guarantee using only p_s,m_s,q and gamma must allow the binary-factual law, and therefore cannot reproduce the uniform-law positive conclusion.

This is a matched information comparison, not a claim that the binary theorem was wrong: that theorem has different observed laws. It shows that the real-endpoint result uses genuinely distributional information rather than merely substituting real means into a binary formula.

## 6. Boundary and baseline comparisons

### 6.1 Degenerate masses

The definitions require no division by p_s. For p=0, I={q}, t=0, and (9) becomes

    L=(eta-1+q)_+-u_0(q),
    U=min(eta,q)-ell_0(q).

For p=1, I={0}, t=1-q, and

    L=(t-eta)_+-u_1(t),
    U=t-(t+eta-1)_+-ell_1(t).

These follow by direct substitution and retain arbitrary factual laws in the sole observed stratum. At eta=0 or eta=1, the allocation proof remains valid without a limiting argument.

### 6.2 Relation to the existing binary theorem

For factual outcomes in {0,1}, let a=mu_0({1}), b=mu_1({1}), c=mu_0({0}), d=mu_1({0}). Then

    g_min=-a-d,   eta=gamma+a+d,
    u_0(r)=min(r,a),  u_1(t)=min(t,b),
    ell_0(r)=(r-c)_+, ell_1(t)=(t-d)_+.

Inserting these into (6)–(9) gives an exact scalar piecewise-linear formula for the same identified set as Yin et al., Theorem 1. The present proof independently proves sharpness in that case. Conditional on the source theorem's stated sharpness, equality with its seven-piece expression follows from uniqueness of the minimum and maximum of the same feasible set. This is **not** a separate authentication/replay of the source's 16-type elimination or proof. A coefficientwise expansion or an independently reconstructed finite-support LP is an appropriate parent check, not an already-exercised check.

The binary example in Section 5 does expand directly and agrees with the source lower bound gamma-1/2 on the stated range. Binary-outcome optimality remains prior work.

### 6.3 Computational interpretation, not an executed computation

For finite-support measures, the tail functions are piecewise linear. F_eta and G_eta are piecewise linear on I, so extrema occur at endpoints or breakpoints: the tail cumulative masses, their shifts by h, and hinge locations h+eta and 1-eta for F_eta (with the corresponding G_eta locations). Exact rational data can therefore be evaluated by finite rational arithmetic without a nonlinear solver. This observation is a consequence of the formulas, not a new enumeration result. No such implementation has been executed in this round.

For atomless laws, the maximum in (14) has the usual quantile crossing description: at an interior differentiability point,

    Q_0(p_0-r)+Q_1(p-t)=1,

with endpoint inequalities/subgradients when the crossing is absent or nonunique. Equations (2)–(3) and the compact one-dimensional optimization remain the definitions when quantiles jump.

## 7. Scientific claim and remaining gates

**Proposed delta:** a complete, constructive sharp identified interval and sharp positive-effect threshold for every bounded real factual endpoint distribution under the fixed-gamma strong-surrogate model. The distributional example proves why a mere mean substitution into a binary theorem loses information.

**Not claimed:** a full book resolution; continuous-surrogate or unbounded/survival theory; statistical estimation/inference; weaker exclusion restriction; clinical validity; publication priority; a new optimal-transport principle; independent/formal verification.

The proof uses only elementary conditioning, mass allocation, tail selection and mixture. These are classical ingredients. Novelty must be assessed against general treatment-effect partial identification and trimmed-mean/optimal-transport work, including the unread full Kuroki 2013 theorem. The current manuscript is a CANDIDATE until parent and independent in-harness written checks are returned. No model CLI or historical verification gate has been satisfied by creating this document.
