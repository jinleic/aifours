# GI24 source comparison and the registered canonical law's EXACT all-shift three-point testing profile

Owner **InfoResearch96h-2**, original info-1. Actual `/bin/date` returned BEFORE this write: **Mon Oct 26 08:16:23 PDT 2026**. **NEW AUTHOR-WRITTEN complete source/math/application candidate**, requiring its OWN complete gate. Neither a source search, prior260LF submission nor a source-impossibility verdict adopts it. The initial three-point/profile lead was saved in checkpoint101, actual08:12:43, before this body; the worst-shift/erasure consequences below are subsequent written derivations.

**Assurance/exactness:** ordinary WRITTEN symbolic/fraction/integer-product reasoning only. No decimal trials, scientific calculator/interpreter/Eval/CAS, enumeration program, solver/replay, model CLI or machine-check. No formal/kernel/configured-family/human/cross-vendor/novelty acceptance.

## 0. ACTUAL primary source and positive PRIOR attribution

**Elena Ghazi and Ibrahim Issa, *Total Variation Meets Differential Privacy*, arXiv2311.01553v2, 29Apr2024**, [actual version](https://arxiv.org/html/2311.01553v2). Its text reports partial presentation at ISIT June2023. The retained source-reader artifact is `artifact://35312`, SHA256 `7a2e4951b3decd21b26022bcdca0a48d8e6f4912048032cefaad73aaf69e2cd3`, physical1036LF/135378bytes; the tool labels the extracted body1037logical lines. These are reader-text bytes, NOT original HTML/PDF/publisher-glyph authentication.

Actual completed source reads: raw1–300, including definitions/Corollary1/the ternary dominating experiment Eq(7); raw405–446, the COMPLETE main VI-A/B/C mechanism formulas; raw909–944, COMPLETE AppendixK1/K2 through endings. This is NOT an entire1037logical-line/full-composition-proof reading. No stronger coverage is inferred from the cached whole SHA.

**Genuinely positive PRIOR:** combining DP with a TV constraint, the resulting three-line exact testing region, the ternary dominating pair, its erasure-like neutral component, and the scalar staircase's exact TV/profile relationship. These are NOT new framework/mechanism contributions here. The elementary generic TRADE consequence in the frozen260LF `privacy-quantitative-finite-propagation-ROC-gap-v1.md` is within this PRIOR formalism. That earlier packet's separately proposed new mathematical item is its explicit finite-moment UNIFORM quantitative TV deficit, not invention of DP+TV privacy.

**New supplied exact application, not a novelty claim:** for EVERY shift of a geometric private density, prove an actual ternary sufficient experiment and identify its parameter as same-level probability; derive an EXACT entire full-ball testing profile from ONE worst-shift parameter and explicit pairwise erasure/reconstruction; specialize conditionally to the registered canonical optimizer. Priority/novelty of this application remain UNCLEAR; a creative corollary of positive prior tools is not automatically a new mechanism or independent discovery.

## 1. Scope, model and named imports

Fix b=exp(-epsilon) with EVERY finite epsilon>0, and c=(1-b)/(1+b). Let K be a genuine norm unit ball in R^d. For Sections2–6, d>=1 is ANY finite integer. Let n:R^d→Z be a measurable FINITE integer-valued function, modulo null versions, with

    |n(x+h)-n(x)|<=1 a.e. in x, for EACH h in FULL CLOSED K.   (STEP)

Suppose `p(x)=Z^(-1)b^n(x)` has finite positive integral normalized to1. No symmetry, convexity, radiality or optimizing premise is assumed. Each fixed-shift a.e. ratio bound integrates to event privacy for EVERY Borel event; no common uncountable exceptional-set intersection is assumed.

For fixed h let P have density p(x), and let Q_h have density q_h(x)=p(x+h), that is, Q_h=tau_(-h)P. Define the INCREASING testing tradeoff

    T_h(u)=inf{E_(Q_h) phi : measurable0<=phi<=1,E_P phi>=u},
    0<=u<=1.

GI24 instead uses decreasing ROC with type-I upper budget t; the exact conversion is `f_GI(t)=T_h(1-t)`. Mixing up these conventions would reverse the visible curve; all formulas below use T_h.

Named ordinary inputs: normalization and ordered-measure integration; nonnegative density/TV identities; exact finite-state randomized tests; conditional probabilities on a FINITE measurable partition; L1-translation continuity (proved from compactly supported approximation below); compactness/continuity; elementary geometric series.

Two additional research inputs are sharply separated:

- **GAP260**: `privacy-quantitative-finite-propagation-ROC-gap-v1.md`, 260LF, SHA `63826c7daca15d7a482873b13167c28ed63da6831b27c0ed1666b23a157a5633`, is at this write an AUTHOR-WRITTEN separately ungated candidate. ONLY the explicit UNIFORM positive same-level bound in Section6 uses its theorem. Sections2–5/source algebra do NOT depend on GAP260. A new union audit is needed before jointly promoting them.
- **LAW642**: `privacy-all-law-optimum-self-contained-v1.md`, SHA `957cab2bcf3eff1860ff9f4b5a1e5838708aceaf894a97fdc2c5244c3e7d8e53`, separately adopted at `privacy-all-law-self-contained-parent-v1.md`. ONLY Section8's identification with the ACTUAL registered optimum imports its canonical-form/finite-cost outputs. No fresh proof of its geometry, uniqueness or value is inferred here.

The source GI24 is positive PRIOR comparison, not an opaque premise of the explicit calculations/proofs below. No Blackwell theorem, scalar MSE optimum, MDA26/K25/CND theorem or finite-family approximation is required for Sections2–7.

## 2. Normalization FORCES the entire ternary experiment

For a FIXED h, partition R^d, up to a null set, into

    G_+= {n(x+h)-n(x)=1},    q_h/p=b;
    G_0= {n(x+h)-n(x)=0},    q_h/p=1;
    G_-= {n(x+h)-n(x)=-1},   q_h/p=b^(-1).

Write `a=P(G_+)`, `m=P(G_0)`, `d=P(G_-)`. Both p and q_h integrate to1, so

    a+m+d=1,               ba+m+b^(-1)d=1.

Subtracting and multiplying by b gives

    (1-b)(d-ba)=0.

Since 0<b<1, `d=ba`. Therefore

    a=(1-m)/(1+b),
    P_3=(a,m,ba),          Q_3=(ba,m,a).                     (TERNARY)

All three masses, including zero-group cases m=0 or m=1, are determined by the ACTUAL same-level probability m, not an independently selected parameter or a scalar analogy.

The statistic sigma_h(x)=the label of G_+,G_0,G_- sends (P,Q_h) EXACTLY to (P_3,Q_3). Conversely, for every group with positive P mass define the probability kernel

    R_h(j,A)=P(A intersect G_j)/P(G_j).

Because q_h/p is CONSTANT on that group, its conditional probability under Q_h is the SAME R_h(j,.). If a group has zero P mass, it also has zero Q_h mass; define R_h(j,.)=P(.) to complete the kernel, whose value on this unused group has no effect. Thus, for EVERY Borel A,

    P(A)=sum_j P_3(j)R_h(j,A),
    Q_h(A)=sum_j Q_3(j)R_h(j,A).                            (REVERSE)

This is an explicit TWO-WAY simulation of the BINARY experiment, not just a moment/likelihood-ratio comparison. It uses the full actual continuous laws. The kernel depends on h; it is NOT claimed that one h-independent postprocessor realizes the whole translation family from three noise atoms.

In GI24 Eq(7), the neutral parameter denoted alpha is exactly m: rewrite exp(epsilon)=1/b to obtain precisely TERNARY. The ternary experiment and generic privacy region are therefore explicitly positive PRIOR.

## 3. EXACT profile, including all breakpoints and degeneracies

Among randomized tests with a fixed P-acceptance requirement, minimizing Q-acceptance means filling likelihood ratios in increasing order: b first, then1, then b^(-1). This follows directly by exchanging acceptance mass from a larger-ratio group to a smaller-ratio group; the P mass is unchanged and the Q mass cannot increase. Randomization within a group supplies every intermediate acceptance exactly.

With a=(1-m)/(1+b), the exact minimum is

    T_h(u)= b u,                         0<=u<=a;
            u-(1-b)a,                   a<=u<=a+m;
            1-b^(-1)+b^(-1)u,           a+m<=u<=1.          (PIECES)

At the two breakpoints the adjacent expressions coincide. The slopes b,1,b^(-1) are nondecreasing, and normalization gives the final affine intercept exactly: `[(b-b^(-1))a+(1-b^(-1))m]=1-b^(-1)`.

Set eta_h=(1-b)a=c(1-m). Equivalently,

    T_h(u)=max{0,b u,u-eta_h,1-b^(-1)+b^(-1)u}.              (PROFILE)

This is an EXACT curve, not merely a lower bound. If m=0, the middle interval has zero length and PROFILE is exactly pure-epsilon DP's two-line envelope. If m=1, a=0 and PROFILE is the identity u; both extreme groups have zero mass. These cases are not excluded by division by1-m.

Also, direct summation of absolute mass differences gives

    TV(P,Q_h)=(1-b)a=c(1-m).                                (TV)

Hence the same-level probability m is an EXACT sufficient parameter for the entire pairwise ROC, not only its TV. No level-set areas or scalar roots have been evaluated.

## 4. Shift signs, continuity, and exact nonzero-shift max-divergence

Define m_h=P[n(X+h)=n(X)]. On the same-level event p(x+h)=p(x). Changing variables y=x+h therefore gives

    m_(-h)=integral p(y)1_{n(y-h)=n(y)}dy
          =integral p(x+h)1_{n(x)=n(x+h)}dx=m_h.             (EVEN)

Thus PROFILE for Q_h=tau_(-h)P is ALSO the exact profile for the requested pair (P,tau_hP); no symmetry of p itself was needed.

L1-translation continuity gives eta_h=TV(P,tau_hP) continuous in h. Here is the needed ordinary bridge: approximate p in L1 by a continuous compactly supported g. Translation is an L1 isometry, so

    ||p(.+h)-p||_1<=2||p-g||_1+||g(.+h)-g||_1.

Uniform continuity and a fixed finite-volume compact neighborhood of supp(g) make the last term tend to0 as h→0. The first term can be arbitrarily small. This proves continuity at0; translation invariance and the triangle inequality give continuity at every h. By TV, m_h=1-eta_h/c is also continuous and m_0=1.

For ANY nonzero h, eta_h>0. Otherwise p(.+h)=p a.e. and P is invariant under that translation. Some bounded ball B_R has positive mass. Choose an integer N with N|h|_2>2R; the balls B_R+kNh, k=0,1,..., are pairwise disjoint and all have the SAME positive P mass, contradicting total probability1. This uses no moment assumption.

Therefore m_h<1 for nonzero h, so a>0. TERNARY then has BOTH extreme likelihood-ratio groups of positive mass, which gives

    D_infinity(P||tau_hP)=D_infinity(tau_hP||P)=epsilon
    for EVERY nonzero h in FULL CLOSED K.                   (ACTIVE)

This conclusion is for the displayed GEOMETRIC class, not all private laws. It is compatible with `TV(P,tau_hP)→0` as h→0: exact max-divergence jumps at0 for this discontinuous geometric-density model, whereas TV and the ROC remain continuous. No smaller pure-epsilon parameter follows from an improved TV/privacy curve.

## 5. ONE ACTUAL worst shift attains the ENTIRE full-ball profile

Because K is compact and m_h is continuous, an ACTUAL minimizer h_* in K exists. Set

    m_*=min_(h in K)m_h,       eta_*=c(1-m_*).

K contains nonzero vectors, so Section4 gives eta_*>0 and h_* can be chosen nonzero. For every u, PROFILE is NONDECREASING in m. Consequently

    inf_(h in K)T_h(u)
       =max{0,b u,u-eta_*,1-b^(-1)+b^(-1)u},                (WHOLE)

and the SAME actual h_* attains this equality for EVERY u simultaneously. This is not an unjustified interchange of an infimum over h with another optimization: monotonicity in the single scalar m gives the lower bound and the actual minimizer supplies equality. No claim identifies h_* as axial, diagonal or boundary, or evaluates m_*.

One can even supply the pairwise domination explicitly, without importing Blackwell's theorem. For a target shift with m_h>=m_*, let

    t_h=(1-m_h)/(1-m_*) in [0,1].

From the ternary experiment with parameter m_*, keep an extreme label with probability t_h; otherwise erase it to the neutral label. Always keep an already neutral label neutral. Under BOTH hypotheses the output masses become TERNARY with parameter m_h, since the new neutral mass is `1-t_h(1-m_*)=m_h`. Composing this explicit erasure with R_h from REVERSE reproduces the ACTUAL pair (P,tau_(-h)P). Again the kernels may depend on h; no one global finite-output additive channel or h-independent input-family equivalence is asserted.

WHOLE is an exact full-continuous-shift privacy-profile characterization in terms of the actual geometric overlap parameter. It does not evaluate an MSE optimum or make a new ternary-mechanism claim.

## 6. The NEW260LF quantitative theorem gives a strict all-shift overlap bound

This section explicitly imports **GAP260**, pending its own fresh full audit at this write. Suppose d>=2, `B_2(0,r) subseteq K`, and the ACTUAL J=E|X|_2^2<=C<infinity. Its theorem gives, with

    N=ceil(max{1,16sqrt(C)/r,512C/r^2}),
    beta=b/[(1+b)N(N+1)],

that `c-TV(P,tau_hP)>=beta` for EVERY h in K. By TV,

    m_h>=beta/c=b/[(1-b)N(N+1)]>0,
    m_*>=beta/c>0,          eta_*<=c-beta<c.                 (UNIFORM)

At `u*=1/(1+b)`, the pure-epsilon envelope equals b/(1+b), and u* lies between a and a+m for EVERY m in[0,1]. Thus the EXACT pairwise and full-ball improvements are

    T_h(u*)=b/(1+b)+c m_h,
    inf_hT_h(u*)=b/(1+b)+c m_*>=b/(1+b)+beta.                (CENTER)

The exact formulas in Sections2–5 are independently proved; ONLY the quantitative positivity is imported from GAP260. Joint promotion of the new union is NOT automatic. It also does not apply to finite-alpha Renyi approximants lacking actual pure-epsilon privacy.

## 7. Complete scalar source-formula control and why dimension>=2 is essential

To reconstruct the GI24 staircase calculation exactly, take scalar sensitivity Delta=1. For EVERY gamma>=0 define the ACTUAL geometric-core density by

    n_gamma(x)=max{0,ceil(|x|-gamma)},
    p_gamma(x)=a_gamma b^n_gamma(x).

The top interval has length2gamma; each later level has length2. Positive geometric summation gives

    Z_gamma=2gamma+2sum_(k>=1)b^k
           =2[b+(1-b)gamma]/(1-b),
    a_gamma=(1-b)/[2(b+(1-b)gamma)].                         (NORM)

This is normalized, has finite moments of every fixed order by its geometric tails, and STEP holds for EVERY scalar shift |h|<=1. For0<=gamma<=1 it is exactly the usual scalar staircase law in the source, up to null endpoints. For gamma>1, the formula above EXPLICITLY defines the wider flat-core continuation matching the printed normalizer/TV branch; this is a stated interpretation, not a claim to have resolved overlapping cases in the source's displayed recursive definition.

For Q(x)=p_gamma(x-1), direct level comparison gives the COMPLETE same-level event, up to null endpoints:

- If0<=gamma<=1/2: x in(gamma,1-gamma), with p_gamma(x)=a_gamma b, so `m=a_gamma b(1-2gamma)`.
- Ifgamma>=1/2: x in(1-gamma,gamma), with p_gamma(x)=a_gamma, so `m=a_gamma(2gamma-1)`.

Outside these intervals the integer index changes by exactly one in either direction. Insert these ACTUAL m values into TV. Writing D=b+(1-b)gamma:

    gamma<=1/2:
    2D-b(1-b)(1-2gamma)
       =(1+b)[b+2gamma(1-b)],
    eta=(1-b)[b+2gamma(1-b)]/(2D);

    gamma>=1/2:
    2D-(1-b)(2gamma-1)=1+b,
    eta=(1-b)/(2D)=a_gamma.                                (BOTH)

These reproduce BOTH printed GI24 VI-C/AppendixK1 TV formulas algebraically, and Sections2–3 reproduce its AppendixK2 EXACT privacy region without merely inspecting a figure or appealing to an unreconstructed test.

**Dimension control:** at gamma=1/2, m=0 and eta=c EXACTLY, despite the scalar law having finite second moment and full continuous sensitivity privacy. Thus the d>=2 hypothesis of GAP260 is ESSENTIAL. This is the known scalar Tulap/half-core staircase control, not a new counterexample to a published theorem or a claim of scalar superiority in the registered planar problem.

**Printed inference qualification:** the selected source-reader AppendixK1 second bullet displays a putative positive area `a(gamma)2gamma Delta[1-exp(+epsilon)]`, which is NEGATIVE for epsilon>0 and gamma>0. Direct subtraction of the high and low densities gives the positive factor `1-b=1-exp(-epsilon)`, consistent with the source's main/final BOTH formulas. The needed conclusion is supported by the exact reconstruction above; this does NOT pass that displayed sign as written. No original-PDF glyph/version-family audit or publication-wide false-theorem claim is made.

## 8. CONDITIONAL application to the ACTUAL registered planar optimizer

The registered original problem has FULL CLOSED unit-l1 diamond D sensitivity, ALL Borel additive laws and squared-Euclidean cost. **LAW642** supplies an ACTUAL finite-cost optimizer with density

    p_epsilon(x)=Z^(-1)b^n_S(x),
    n_S(x)=min{k>=0:x in S+kD},

where S is its nonempty compact canonical core. If x in S+kD and h in D, then x+h in S+(k+1)D. Reversing h gives the reverse inequality, hence `|n_S(x+h)-n_S(x)|<=1` for EVERY x,h with the canonical closed-level convention. Thus the FULL scope of Sections2–5 applies, not only an axial family.

Define the EXACT overlap parameter

    m_h=Z^(-1)sum_(k>=0)b^k |E_k intersect(E_k-h)|,
    E_k={x:n_S(x)=k},       m_*=min_(h in D)m_h.

The identity follows by positive Tonelli; no overlap area/tail is numerically evaluated. Sections2–5 give the optimizer's exact EVERY-shift ROC, exact full-diamond WHOLE curve, one simultaneous worst shift, and ACTIVE pure-epsilon max-divergence for EVERY nonzero diamond shift. These conclusions import LAW642's canonical-form/existence/finite-value identification, not its proof or an evaluated scalar root.

With C=V(epsilon)>0, the Euclidean ball radius r=1/sqrt(2) lies in D. CONDITIONAL on the additional pending GAP260 theorem, Section6 strengthens the description with

    N_D=ceil(max{1,16sqrt(2V(epsilon)),1024V(epsilon)}),
    m_*>=b/[(1-b)N_D(N_D+1)]>0,
    0<eta_*=c(1-m_*)<=c-beta_D<c.

Even without newly certifying this quantitative union, the exact ternary/profile calculations in this body stand at their displayed geometric-index hypotheses. No new V computation, elementary inverse, finite table, old Galois/arithmetic replay, all-channel theorem or new mechanism follows.

## 9. Exact source/acceptance residual and permanent boundaries

This successor adds a genuinely relevant POSITIVE prior source after the260LF freeze; it does not edit or backdate that packet. The generic DP+TV/ternary formalism and scalar staircase profile must be credited to GI24 and its cited earlier testing/composition work. This packet does NOT reconstruct GI24's entire adaptive composition theorem, subsampling, SGD analysis, local-privacy contraction results or all1037logicalsource lines. Those are not needed for the precise comparison/application proved here and are not silently marked passed.

Pending scientific acceptance is the OWN complete mathematics AND dependency/application audit of this body, and, for UNIFORM/CENTER quantitative conclusions, the explicit union with GAP260. The original registered model/value/source-priority problem is not replaced by the scalar control or a finite-output toy. Novelty/worldwide priority/publishability and a whole-book/nonadditive solution remain UNCLEAR/unmet.

All earlier source packets, parents, reviews, ACKs and park bytes stay frozen. FirstFIVEindividuallycategorized owner findings, SIXTH DISTINCTv111Bexactness, SEPARATE077continuationfailure/categoryv21 and all source/old-arithmetic/N4UNKNOWN/exit-unestablished histories remain permanent, not renamed/cured. Withdrawn private glosses/old computation have ZERO credit and are not replayed/back-converted. Auxiliary214 remains UNADMITTED under strict STOP; no graph derivation has resumed.

No scientific execution/newGO/CLI/nestedagent/Git/publication/shared-root write. Same18 owners, original full registered model, global HOLD and actual substantive checkpoints at most30minutes. Original new-science cutoff **2026-10-27T11:05:38-07:00**, delivery **2026-10-27T12:35:38-07:00**. This is NOT early final-park, round closeout, continuous-activity assurance or a private-history census; the registered source/proof/priority residual continues.
