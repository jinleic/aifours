# Registered mixed-norm privacy source edge: a quantitative UNIFORM ROC deficit by finite max-propagation

Owner **InfoResearch96h-2**, original info-1. Actual `/bin/date` returned BEFORE this write: **Mon Oct 26 08:01:35 PDT 2026**. **NEW AUTHOR-WRITTEN candidate**, NOT independently reviewed or parent-adopted. The complete new representation and theorem were first saved in checkpoint100, actual **07:58:55**, before this body. This is registered privacy source-equivalence/proof work, not auxiliary graph work, another matching-norm optimum, or a new mechanism.

**Exactness:** every argument below is symbolic/integer/rational analysis; square roots and exponentials remain exact mathematical expressions. No decimal magnitude gloss, numerical parameter trial, calculator, interpreter/Eval/CAS, enumeration program, solver, replay or machine-check occurred. This is WRITTEN, NOT WRITTEN-checked-in-kernel or formal/kernel verification.

## 0. Source question, named inputs and contribution ceiling

The earlier `privacy-AD22-full-ROC-impossibility-and-maxdivergence-boundary-v1.md` (212LF, SHA `5675d8a0ea1602bacfa5a11b0e757b4d1d463eb5ec6750eab07d9465a749a4a`) reconstructs the positive PRIOR AD22 impossibility of a multivariate pure-DP canonical noise distribution, and derives strict nonsaturation of binary testing for each individual full-ball-private law. The later `privacy-AR24-anticoncentration-strong-profile-and-AD22-typo-v1.md` (136LF, SHA `8244731152ee815e2f1015ea2345eafba578344c9d35cbd495c6c86868c3d53b`) records AR24's published footnote reporting the AD22 testing-sign typo, its TV anti-concentration tools and the difference between full reference-profile privacy and a single pure-epsilon constraint. Both are SOURCE CONTEXT, not mathematical premises of the new proof.

**The new theorem is stronger in one exact direction:** under an ACTUAL second-moment budget C, a completely explicit positive TV deficit is UNIFORM over ALL feasible laws and ALL shifts in the full norm ball. It replaces exact binary-LR equality and an infinite packing contradiction by a finite max-propagation/Markov argument. No source paper is claimed to contain, exclude, or certify novelty of this quantitative statement. Priority/novelty remain **UNCLEAR**.

Named ordinary inputs, with specialized bridges supplied below:

- Tonelli/Fubini and translation invariance of Lebesgue measure; Radon–Nikodym derivatives and density order for ordered measures.
- Markov's inequality for a nonnegative square-integrable norm, the triangle inequality for a genuine norm, and existence of a Euclidean unit vector perpendicular to one vector in dimension at least two.
- The total-variation identity `TV(p,q)=(1/2)integral|p-q|`; elementary maxima, finite sums and exact inequalities.
- Only in the LAST application identifying a particular geometric density as the registered optimizer: **LAW642**, `privacy-all-law-optimum-self-contained-v1.md`, SHA `957cab2bcf3eff1860ff9f4b5a1e5838708aceaf894a97fdc2c5244c3e7d8e53`, at the separate parent `privacy-all-law-self-contained-parent-v1.md`. That named research theorem is NOT needed for the quantitative theorem or the general geometric-index identity.

There is no MDA26/K25/EG/CND-construction/finite-family/uniqueness/attainment research premise in Sections1–7. All newly written claims carry the same ordinary-WRITTEN assurance ceiling.

## 1. FULL theorem and quantifiers

Let d>=2 be ANY finite integer. Let K be ANY compact convex centrally symmetric genuine norm unit ball in R^d with nonempty interior. Write `||.||_K` for its norm. Fix an ACTUAL r>0 such that the CLOSED Euclidean ball `B_2(0,r)` is contained in K.

Fix EVERY finite epsilon>0 and EVERY C>0. Set

    b=exp(-epsilon),  c=(1-b)/(1+b),  kappa=(1+b)/(2b),
    R=2 sqrt(C),      delta=r/4,
    n=ceil(max{1, 16 sqrt(C)/r, 512 C/r^2}),
    beta=b/[(1+b)n(n+1)].                                      (PARAM)

Thus n is an ACTUAL finite positive integer, defined symbolically; no finite table or root evaluation is involved. The defining bounds imply

    n delta>=2R,             n>=32 C/delta^2.                  (N)

Let mu be ANY Borel probability law on R^d satisfying BOTH

    mu(A)<=b^(-1)mu(A+h)
    for EVERY Borel A and EVERY real h in the FULL CLOSED K,   (PRIV)

    integral |x|_2^2 dmu(x)<=C.                               (MOM)

No density, symmetry, radiality, geometric level, mean-zero or optimizer assumption is imposed. Then

    TV(mu,tau_v mu)<=c-beta<c
    for EVERY v in the FULL CLOSED K,                        (GAP)

where `tau_v mu(A)=mu(A-v)`. The same beta works for ALL mu and ALL v at the displayed epsilon,C,K,r. The zero shift is included. If `c-beta<0`, the conclusion correctly says that this moment-constrained feasible class is EMPTY; it does not invent a negative TV or a feasible law.

This is a quantitative testing/profile obstruction, not an exact minimum-MSE calculation or a theorem about arbitrary nonadditive channels.

## 2. All Borel laws have densities: no uncountable exceptional-set assumption

Let A be Lebesgue-null. By Tonelli and translation invariance,

    integral_K mu(A+h) dh
      = integral [integral_K 1_(A+h)(x) dh] dmu(x)=0.

Since |K|>0, some h in K has mu(A+h)=0. Applying PRIV at THAT h gives mu(A)=0. Hence mu has a nonnegative integrable density p with integral p=1.

For EACH fixed h in K, PRIV and -h in K give the a.e. two-sided density inequalities

    b p(x)<=p(x+h)<=b^(-1)p(x).                               (FIXED)

This follows from the actual ordered measures, not an assumption about pointwise values of arbitrary density versions. We will use only THREE fixed shifts and their countable lattice translates for each fixed v. We NEVER intersect uncountably many exceptional sets. No everywhere-positive-density theorem, cap, first moment or common uncountable RN version is needed below.

## 3. EXACT two-variable testing deficit

Fix an ARBITRARY v in K. For a.e. y set

    D_v(y)=c[p(y)+p(y+v)]-|p(y+v)-p(y)|.

Write M=max{p(y),p(y+v)}, m=min{p(y),p(y+v)}. FIXED at v gives m>=bM. Direct algebra, with NO sign approximation, gives

    D_v=(c-1)M+(c+1)m
       =2(m-bM)/(1+b)>=0.                                  (DEF)

Consequently D_v is nonnegative and integrable. Translation invariance and the TV identity give

    integral D_v=2c-integral|p(y+v)-p(y)|
                =2[c-TV(mu,tau_v mu)].                       (INT)

The sign of v in the density formula is harmless: `integral|p(y+v)-p(y)|=integral|p(y-v)-p(y)|`. Define the NONNEGATIVE number

    eta_v=c-TV(mu,tau_v mu).

Then `integral D_v=2 eta_v`. The theorem will give a positive lower bound for eta_v; it does not assume exact binary testing equality.

## 4. Two legitimate privacy shifts with a transverse displacement

Choose a Euclidean unit vector e perpendicular to v. Such an e exists for EVERY v in dimension d>=2; for v=0 any unit vector is perpendicular. Put

    z=delta e,              w=z-v/2.

Since `|z|_2=r/4`, containment of the Euclidean radius-r ball gives `||z||_K<=1/4`. Since `||v||_K<=1`, the norm triangle inequality gives

    ||w||_K<=3/4,           ||w+v||_K<=3/4.

Both w and w+v lie in the ACTUAL sensitivity ball, not a replacement Euclidean sensitivity set. Moreover

    e.v=0,                 e.w=delta.                        (TRANS)

For a.e. x, FIXED at those TWO shifts yields

    A=p(x+w)>=bp(x),        B=p(x+w+v)>=bp(x).

For this pair, DEF at y=x+w says

    min(A,B)=b max(A,B)+(1+b)D_v(x+w)/2.

Since the left side is at least bp(x), division by b>0 gives

    max{p(x+w),p(x+w+v)}
      >=p(x)-kappa D_v(x+w).                                (ONE)

This approximate propagation inequality is the central new representation. It keeps the ACTUAL deficit from binary testing instead of pretending that one of the two values equals a larger exact level.

## 5. Finite max-propagation: all branches and all errors retained

For a measurable real function f define

    Tf(x)=max{f(x+w),f(x+w+v)}.

This operator is monotone, positively homogeneous for nonnegative scalars, and satisfies, for kappa>=0 and g>=0,

    T(f-kappa g)>=Tf-kappa Tg.                               (MAX)

Indeed each subtracted value is at most kappa times the larger g value, so the branch attaining Tf supplies the inequality. Let `E(x)=D_v(x+w)>=0`. ONE is `Tp>=p-kappa E`.

Induction using monotonicity and MAX gives, for EVERY positive integer m,

    T^m p>=p-kappa sum_(k=0)^(m-1) T^k E.                    (ITER)

For completeness: it holds at m=1. If it holds at m, applying T and MAX to the finite nonnegative sum gives

    T^(m+1)p >= Tp-kappa T(sum_(k=0)^(m-1)T^k E)
              >= p-kappa E-kappa sum_(k=0)^(m-1)T^(k+1)E.

The SECOND inequality uses `T(sum g_k)<=sum Tg_k`, valid because the maximum of sums is at most the sum of maxima, and Tp>=p-kappa E. This is exactly ITER at m+1. No branch/error is dropped.

Because the two translations commute,

    T^m p(x)=max_(0<=j<=m)p(x+mw+jv),
    T^k E(x)=max_(0<=j<=k)D_v(x+(k+1)w+jv).

All the latter terms are nonnegative, so

    T^n p(x)>=p(x)-kappa sum_(k=0)^(n-1) sum_(j=0)^k
                               D_v(x+(k+1)w+jv).            (FINITE)

These a.e. statements are legitimate simultaneously as follows. For the fixed v,w, take the full-measure sets on which FIXED for v,w,w+v and DEF/ONE hold, and intersect their translates over the COUNTABLE additive group `{aw+jv:a,j in Z}`. Translation preserves null sets. On the resulting full-measure invariant set every finitely iterated inequality is valid. The null set may depend on v, which is allowed; the FINAL numerical bound will not depend on it. This is not an uncountable intersection or an assumption of simultaneous density privacy for all shifts.

## 6. The ACTUAL moment budget forces a UNIFORM positive deficit

Integrate FINITE over the CLOSED Euclidean ball B_R. By MOM and Markov,

    integral_(B_R)p=mu(B_R)>=1-C/R^2=3/4.                    (START)

The finite double sum has exactly `n(n+1)/2` terms. Each translated nonnegative D_v integral over B_R is at most its integral over ALL R^d, namely 2 eta_v. Thus

    integral_(B_R)T^n p>=3/4-kappa n(n+1) eta_v.              (LOW)

For x in B_R and 0<=j<=n, TRANS gives

    e.(x+nw+jv)>=-R+n delta.

Therefore the ACTUAL translated ball `B_R+nw+jv` lies in the halfspace `e.y>=n delta-R`. By N this threshold is positive. Markov and `|e.y|<=|y|_2` give

    integral_(B_R)p(x+nw+jv)dx
      =mu(B_R+nw+jv)<=C/(n delta-R)^2.

Using `max<=sum` for the n+1 nonnegative endpoint densities gives

    integral_(B_R)T^n p
      <=(n+1)C/(n delta-R)^2
      <=4(n+1)C/(n^2 delta^2)
      <=8C/(n delta^2)
      <=1/4.                                                (UP)

The successive inequalities use, respectively: N's `n delta>=2R`; `n+1<=2n` for n>=1; and N's `n>=32 C/delta^2`. They are exact, not asymptotic estimates, head-only packing, a numerical search or an ignored infinite tail.

Combine LOW and UP:

    kappa n(n+1) eta_v>=1/2,
    eta_v>=1/[2kappa n(n+1)]
         =b/[(1+b)n(n+1)]=beta>0.

This proves GAP for the arbitrary v. The same n and beta depended ONLY on epsilon,C,r, not v or mu. Hence the quantifiers in Section1 follow in full, including v=0 and the full closed sensitivity boundary. QED, ordinary **WRITTEN**.

## 7. Exact specialization to the REGISTERED diamond and a stronger tradeoff guarantee

For the planar CLOSED unit-l1 diamond D, the Euclidean radius `r=1/sqrt(2)` ball is contained in D, by `|x1|+|x2|<=sqrt(2)|x|_2`. The theorem therefore holds for EVERY finite epsilon>0, EVERY C>0, ALL original Borel additive laws with J<=C, and EVERY h in D, with the fully explicit symbolic choice

    n_D(C)=ceil(max{1,16sqrt(2C),1024C}),
    beta_D(epsilon,C)=exp(-epsilon)/
       [(1+exp(-epsilon))n_D(C)(n_D(C)+1)].                   (DIAMOND)

No original optimizer or LAW642 premise is needed for this specialization. This is directly a mixed-norm statement: sensitivity is l1; the ACTUAL budget is squared Euclidean moment. It is NOT a matching-norm radialization result.

To state the testing consequence, use the convention that T(P,Q)(alpha) is the infimum Q-acceptance probability over randomized tests with P-acceptance at least alpha. For EVERY such test, the TV bound gives

    E_Q phi>=E_P phi-TV(P,Q)>=alpha-(c-beta).

Pure epsilon-DP itself gives the standard symmetric lower tradeoff

    f_eps(alpha)=max{0,b alpha,1-b^(-1)+b^(-1)alpha}.

Thus every pair from the full-ball model satisfies the COMMON stronger lower bound

    T(mu,tau_hmu)(alpha)>=max{f_eps(alpha),alpha-c+beta}.       (TRADE)

For a nonempty moment-constrained feasible class, GAP at the zero shift ensures beta<=c, so this is a valid nonnegative TV improvement, never a curve exceeding the identity for a genuinely feasible pair. At `alpha*=1/(1+b)`, the two pure-epsilon affine pieces meet and

    f_eps(alpha*)=b/(1+b)=alpha*-c.

TRADE improves that specific pure-epsilon lower value by at least beta, uniformly in EVERY h and EVERY law obeying the ACTUAL budget. No complete f-curve equality, CND, new pure-epsilon' reduction, or elementary minimizer follows. The actual max-divergence can still equal epsilon; a TV/profile improvement is NOT the same as a smaller pure-DP parameter.

## 8. A precise geometric-density application, with research imports separated

Let n(x) be ANY measurable integer-valued index such that `|n(x+h)-n(x)|<=1` a.e. for EACH h in D, and suppose `p(x)=Z^(-1)b^n(x)` is a probability density with finite ACTUAL squared-Euclidean moment J<=C. These are explicit hypotheses, not a claim that all original laws are geometric.

For fixed h, the density ratio is one of b,1,b^(-1). In particular the pointwise a.e. ratio bounds integrate to PRIV for EVERY Borel event and EACH h in the full closed D, so the preceding theorem applies. On points where the index changes by either sign, DEF is ZERO. On points where `n(x+h)=n(x)`, DEF equals `2c p(x)`. Hence, writing

    A_h=P[n(X+h)=n(X)],

INT gives the EXACT identity

    c-TV(mu,tau_hmu)=c A_h,
    TV(mu,tau_hmu)=c(1-A_h).                                (PLATEAU)

Combining with DIAMOND gives the uniform positive same-level probability

    A_h>=beta_D/c
       =b/[(1-b)n_D(C)(n_D(C)+1)]>0
    for EVERY h in the FULL CLOSED D.                      (OVERLAP)

Equivalently, if E_k={n=k}, then positive Tonelli gives

    A_h=Z^(-1)sum_k b^k |E_k intersect(E_k-h)|.

No overlap area has been numerically evaluated, no tail is truncated, and no normalizer is estimated. This exact identity and inequality require ONLY the displayed geometric-index hypotheses plus Sections1–7, not an optimizing premise.

**Conditional application to the registered optimizer:** LAW642 supplies an actual finite-cost optimizer with canonical index `n_S(x)=min{k>=0:x in S+kD}` for its nonempty compact core S. That index satisfies the displayed step bound by the norm triangle inequality in BOTH directions. Taking C=V(epsilon)>0 therefore specializes PLATEAU/OVERLAP to that ACTUAL optimizer. This last identification explicitly imports the named LAW642 existence/finite-value/canonical-form outputs; neither their proof, all-law uniqueness, scalar-root evaluation, nor novelty is silently re-proved here. No fresh exact area/value table or old arithmetic/Galois certification is claimed.

## 9. Relationship to other live source work and exact limits

The two AD22/AR24 source packets are separately ungated context. The new proof has NO dependency on their proof bodies or on the arbitrary infinitely divisible-family-to-CND profile identification left NOT_RECONSTRUCTED in the AR24 note. A fresh full mathematics AND dependency/application gate is required for THIS entire new quantified theorem, not a transfer of a source-impossibility verdict.

Parent's complete `privacy-MDA26-entire-norm-cost-and-weighted-decay-parent-v1.md` was ACTUALLY read through END before this write, SHA `75614a6fc5cb66d9b26f13e64e58935fe6ea52121948e7a56592b91611576ac3`: its TWO distinct PRIOR matching-norm/per-cost/universal-dominator conclusions remain separate, not duplicate progress on the registered optimum.

Parent's complete `privacy-exact-budget-joint-order-family-and-nonattainment-parent-v1.md` was also ACTUALLY read through END before this write, SHA `3952c39b4918bb30b29e4ceb11a0f9f0c5918cff969a97c774e9d54000bbbcc4`. Its exact-cost-margin/cofinal-order/ALL-near-minimizer/nonattainment composition is at its stated I233+II280+LAW642 union. This quantitative pure-DP theorem does NOT silently apply to finite-alpha family approximants, which need not satisfy Finfinity<=epsilon. Nor does it prove a fixed-family positive infimum gap or any rate in that joint-limit theorem.

**Not established:** an improved or independently re-evaluated V; all original optimizers without LAW642; exact finite-family privacy/accountant certification; lower bound for arbitrary channels; complete ROC equality; CND existence; optimal TV constant; source-theorem falsity; absence of earlier quantitative corollaries; worldwide priority, publishability or novelty; formal/kernel/human/configured-family/cross-vendor/executable acceptance.

## 10. Permanent process and continuation

No scientific execution or new GO. Metadata `/bin/date`, source reads, hashes, own-root text writes only. Every frozen source/review/ACK/parent/earlier park retains its bytes. All five originally individually categorized owner findings, SIXTH DISTINCT v111B exactness finding and SEPARATE077 continuation-control failure/categoryv21 remain permanent; they are not collectively renamed six exactness occurrences. All withdrawn private glosses/old arithmetic receive ZERO credit and are not replayed or back-converted. The auxiliary214 graph body remains UNADMITTED under strict STOP; no graph derivation has resumed.

Same original18 owners, full registered model, global HOLD, N4UNKNOWN/exit-unestablished and all source/model/chronology qualifications remain. The active cadence is actual substantive checkpoints at most30minutes, not a runtime/private-thought census. Original new-science cutoff **2026-10-27T11:05:38-07:00**, delivery deadline **2026-10-27T12:35:38-07:00**. This is NOT early final-park or round closeout; the registered source/proof/priority residual continues.
