# Registered full-diamond pure DP: finite joint-bin/product-geometric-tail recovery

Owner **InfoResearch96h-2**, original info-1. Actual `/bin/date` BEFORE this write: **Mon Oct 26 05:23:35 PDT 2026**. **NEW AUTHOR-WRITTEN CANDIDATE**, requiring a fresh complete source/proof/application gate. No independent reconstruction, parent adoption, formal/kernel/executable or novelty credit is claimed.

All work is exact WRITTEN symbolic analysis, not numerical parameter trials. There is no scientific interpreter, eval, calculator, CAS, program, enumeration/table, solver/replay, external-model CLI or nested agent. No mathematical identity was machine checked.

## 0. Prospective authority and exact contribution boundary

The actual v112-I RETURN preceded Main's explicit registered-primary permission, the whole-state checkpoint085, and the separate whole-primary ACK SHA256 `832d6f181a3e5a4a6dc3bb27061ceedb32ccaf38c50c1f7d02a1e058ccecdf5b`. That ACK was SENT before current primary/source reasoning. Complete preceding state, all held leads and findings remain preserved. New order-limit work is saved in checkpoint086; the FULL current recovery construction was saved in checkpoint087 before this body. No older freeze or ACK is retroactively made to contain these new leads.

The registered target stays **ALL additive Borel laws on R², EVERY shift in the FULL CLOSED unit-l1 diamond, squared Euclidean loss, EVERY finite epsilon>0**. Auxiliary214 remains UNADMITTED/strict STOP. No graph, cactus auxiliary, nonadditive/channel/model/slot cutover is involved.

**What this note adds:** an exact recovery sequence of finite-parameter JOINT square-bin densities with an exact product-geometric tail, maintaining the ORIGINAL epsilon privacy for EVERY continuous diamond shift and approaching the known all-law optimal MSE from above. This fills an existence/recovery-sequence edge of the registered prior-method comparison—not a numerical solver or an already-proved G25 theorem about planar joint laws.

**What it imports:** the already-adopted LAW642 value/unique law and its compact-core canonical density. This is an approximation/representation theorem for that SAME optimum, not a new optimum, independent lower bound or mechanism discovery. Mixtures, independent convolution, density max/order arguments, quantization and geometric-tail parameterization are PRIOR/basic methodology. No priority, novelty, major-contribution or publication claim follows.

The preceding233LF `privacy-renyi-infinity-full-diamond-bridge-v1.md`, SHA256 `03ccb06b95b5b3cdbf9b9e120293a6a68c3c8399ff2621c9ee77e1ccdd3df843`, remains an UNREVIEWED candidate at its own pin. The direct pure-DP recovery proof here does **not** require accepting its Rényi-order/minimum-interchange theorem. Its still-open family-recovery sentence is historical at that first snapshot; the present later proof supplies a precisely defined joint-family recovery, not a silent edit.

## 1. Named inputs and source-comparison evidence

**LAW642 (NAMED adopted mathematical input).** `privacy-all-law-optimum-self-contained-v1.md`,642LF, SHA256 `957cab2bcf3eff1860ff9f4b5a1e5838708aceaf894a97fdc2c5244c3e7d8e53`, at complete ordinary-WRITTEN parent `RUN/privacy-all-law-self-contained-parent-v1.md`, SHA256 `c08f6353f121ef9e35da0e9d5e8ec9c87b0da838be0d1adf38b807010a1cd979`.

Precisely used: for every finite epsilon>0 the original additive problem has finite positive value C=V(epsilon) and a UNIQUE optimal LAW mu_* with canonical density

    f_*(z)=Z_*^(-1) exp(-epsilon n_S(z)),
    n_S(z)=min{k>=0 integer:z in S+kD},

for a nonempty compact S and finite positive Z_*. This density is positive and full-D-private. No old578LF root/Galois/transcendence/numerical-table output is used. No fresh proof of LAW642's geometry or lower bound is claimed.

**G25 (positive PRIOR motivation, NOT an approximation theorem imported here).** [Gilani et al., *Optimizing Noise Distributions for Differential Privacy*, ICML2025/PMLR267](https://proceedings.mlr.press/v267/gilani25a.html), with selected [arXiv2504.14730v2](https://arxiv.org/html/2504.14730v2) formal source read1–300, reader artifact34113 SHA256 `32e84fbe5ddd0ea2d3ff2f6c12a65764ce42acae5332da80e0f7af1fbd8da78d` (reader-log hash, NOT PDF identity). The earlier complete publisher786LF intake remains SHA256 `e5149e125a375d083d35ab98647dbd8a2cfcc37accfb98c0f62158c8f7e6c1be`; the current complete parent comparison is SHA256 `d25565ecce127f8347eb34075cc41cc9fc1851e49457722ca0352db1519934ed`.

The source expressly motivates the pure-DP alpha→infinity endpoint and optimizes scalar noise laws, with finite bin/geometric-tail families. Its scalar finite-family reformulation and full scalar-shift overlap control are genuine PRIOR overlap. Its general PDF-approximation wording does not itself establish a planar correlated/full-diamond divergence recovery sequence. This note proves its own specified joint analogue instead of asserting that the source already stated it. No source algorithm/accountant/experiment or printed numerical result is exercised or credited.

**Ordinary STANDARD facts:** nonnegative Tonelli; Lebesgue translation; elementary triangle/log/exponential inequalities; convolution of probability laws and centered product-Laplace moments; regular Borel integration; conditional kernels on countable cell partitions; Cauchy–Schwarz; weak compactness/Portmanteau and all-shift Radon measure order. Every problem-specific privacy, tail, normalization, cost and parameter-selection step is supplied below. No weighted K25 Step5, EG infimum assertion, source CLT, opaque CAL input or substantial external approximation theorem is assumed.

## 2. Explicit finite-parameter joint family

Choose integers M>=1,N>=1, set delta=1/M, and choose0<r<1. Centered square cells are

    C_k = product_(i=1,2)[(k_i-1/2)delta,(k_i+1/2)delta),
    k=(k1,k2) in Z².

They form an actual half-open Borel partition. Define the symmetric scalar PMF

    pi_r(0)=1-sqrt(r),
    pi_r(j)=sqrt(r)(1-r) r^(|j|-1)/2, j!=0.

Its sum is1, since its two-sided nonzero mass is sqrt(r). Let H_N={k:max(|k1|,|k2|)<=N}. For freely chosen head masses a_k>=0, k∈H_N, and theta>=0 put

    p_k=a_k,                                k in H_N,
    p_k=theta pi_r(k1)pi_r(k2),              k outside H_N,
    q(z)=p_k/delta² for z in C_k.                         (FAM)

Write

    S_N=sum_(|j|<=N)pi_r(j)=1-r^(N+1/2).

The exact normalization condition is the FINITE affine equation

    sum_(k in H_N)a_k + theta(1-S_N²)=1.                 (NORM)

For fixed M,N,r this is a finite-dimensional distribution family, with a genuinely JOINT head—not a coordinatewise-independent head. The tail is an EXACT product-geometric formula outside one finite square. Correlations inside that square are unrestricted. No fixed single M,N,r family is claimed exhaustive.

All second moments are finite. More explicitly,

    L2(r)=sum_j j²pi_r(j)=sqrt(r)(1+r)/(1-r)²,
    J(q)=delta²/6
        +delta²[sum_(k in H_N)(k1²+k2²)a_k
           +theta(2L2(r)
              -sum_(k in H_N)(k1²+k2²)pi_r(k1)pi_r(k2))]. (COST)

The cell-uniform second moment contributes delta²/12 in each coordinate. The formula for L2 uses `sum_(j>=1) j²r^(j-1)=(1+r)/(1-r)^3`, an exact geometric-series identity, not a machine computation. Thus COST is a finite affine expression in the head/tail masses when M,N,r are fixed.

Let G be the union of these families over all stated parameters. Privacy is ALWAYS the original event inequality for EVERY h∈D. Finite-dimensional **parameterization** is not here mislabeled a verified finite privacy-constraint list, scalar-bin alignment algorithm, gradient-convergence theorem or executable assay.

## 3. The full uniform claim

**Theorem R — WRITTEN at LAW642 and the ordinary facts named above.** For EVERY finite epsilon>0 and EVERY eta>0, there is q∈G satisfying the original full-CLOSED-diamond epsilon-privacy and

    V(epsilon)<=J(q)<=V(epsilon)+eta.                    (REC)

In particular

    inf{J(q):q in G, q is full-D epsilon-private}
       =V(epsilon).                                     (VALUE)

No density/independence/family ansatz was imposed in defining V. The recovery theorem uses the already-proved all-law optimum as an input and shows that its value is captured by this union of finite joint families.

**Law/equality corollary — WRITTEN at the same inputs.** Any sequence of full-D epsilon-private laws from G with costs approaching V(epsilon) converges weakly to the unique LAW642 optimizer, and its costs converge to that value. This asserts no total-variation/density-uniform rate, single fixed family, finite-order uniqueness, rational certificate or solver convergence.

## 4. Strict privacy slack without a discontinuity/plateau assumption

The compact core gives a GLOBAL exponential bound. Put

    R_S=max_(s in S)|s|1,
    A=Z_*^(-1) exp(epsilon R_S).

Since n_S(z)>=dist_1(z,S)>=|z|1-R_S,

    0<f_*(z)<=A exp(-epsilon|z|1) for every z.             (ENV0)

Fix a SYMBOLIC0<a<epsilon (for example a=epsilon/2), and take the normalized product-Laplace density

    nu_a(z)=a² exp(-a|z|1)/4,
    J(nu_a)=4/a².

It is a-private for all h∈D, and ENV0 implies

    nu_a(z)>=c0 f_*(z), c0=a²/(4A)>0.                   (DOM)

In fact c0<=1 by integration. For0<lambda<1 put

    g_lambda=(1-lambda)f_*+lambda nu_a,
    d_lambda=lambda c0/(1-lambda+lambda c0),
    b=exp(-epsilon),
    b_lambda=b+(exp(-a)-b)d_lambda,
    epsilon_lambda=-log(b_lambda).

Here0<d_lambda<1, so `a<epsilon_lambda<epsilon`. For EVERY h∈D,

    g_lambda(z+h)
      >=b(1-lambda)f_*(z)+exp(-a)lambda nu_a(z)
      =b g_lambda(z)+(exp(-a)-b)lambda nu_a(z).

DOM gives `lambda nu_a/g_lambda>=d_lambda`, hence

    g_lambda(z+h)>=b_lambda g_lambda(z).                 (SLACK)

The original law privacy can equivalently be used a.e. for each fixed h; DOM then yields the same measure inequality without an uncountable-h RN choice. The canonical LAW642 version also has the needed pointwise bound directly from its level index. Thus SLACK proves strict **uniform privacy slack**, not merely cost-convexity of a mixture. A generic mixture of two equally-private laws would not justify this strict claim; DOM is the missing quantitative ingredient.

The cost is exactly `(1-lambda)V(epsilon)+lambda(4/a²)` and is at most `V(epsilon)+lambda(4/a²)`. It approaches V(epsilon) as lambda→0. No left-continuity of V or assumption that rescaling a one-step-private density improves its epsilon proportionally was used.

## 5. Smoothing: exact privacy, moment and global relative regularity

Choose a SYMBOLIC sigma>0 with a sigma<1, and let K_sigma be the centered product-Laplace probability density

    K_sigma(w)=exp(-|w|1/sigma)/(4sigma²).

Set f_sigma=g_lambda*K_sigma. Independent centered addition preserves the whole event privacy condition, so f_sigma is epsilon_lambda-private for ALL shifts. More precisely, for any z,h, integrate the nonnegative kernel test against the event domination of g_lambda to obtain the pointwise canonical inequality for f_sigma. Thus there is no need to select one a.e. density version over an uncountable shift family.

The kernel ratio bound gives for EVERY z,z'

    exp(-|z-z'|1/sigma) f_sigma(z')
       <=f_sigma(z)<=exp(|z-z'|1/sigma)f_sigma(z').        (LOG-LIP)

The density is positive and continuous; its log is globally1/sigma-Lipschitz in l1. Also

    J(f_sigma)=J(g_lambda)+4sigma².                      (MOM-S)

The cross term vanishes because K_sigma is centered and both first moments are integrable, a consequence of their finite second moments. No symmetry or source identity is silently added to that calculation.

For the tail, let A_lambda=(1-lambda)A+lambda a²/4. Then `g_lambda(z)<=A_lambda exp(-a|z|1)`. The triangle inequality gives

    f_sigma(z)<=A_lambda exp(-a|z|1)
                      integral exp(a|w|1)K_sigma(w)dw
               =A_sigma exp(-a|z|1),
    A_sigma=A_lambda/(1-a sigma)².                       (ENV1)

Each one-dimensional integral is1/(1-a sigma), so ENV1 is exact. The requirement a sigma<1 is essential and explicitly retained.

## 6. Exact finite-tail replacement without losing privacy

Fix a SYMBOLIC0<t<a, and c>0. Because t<a<epsilon_lambda, the unnormalized density `c exp(-t|z|1)` is also epsilon_lambda-private. Define

    H_c(z)=max(f_sigma(z),c exp(-t|z|1)),
    Z_c=integral H_c,
    f_c=H_c/Z_c.

Max preserves the two required pointwise order inequalities: if both functions at z+h are at least exp(-epsilon_lambda) times their values at z, their max has the same property. Normalization does not change it. Thus f_c remains epsilon_lambda-private. Both functions also obey LOG-LIP with constant1/sigma, since t<a<1/sigma. Their max and its normalized density obey the same relative bound.

ENV1 proves that for

    R=max(0,log(A_sigma/c)/(a-t)),

we have `H_c(z)=c exp(-t|z|1)` whenever |z|1>=R. This is an EXACT tail outside a finite radius, not only an asymptotic comparison. Since `f_sigma<=H_c<=f_sigma+c exp(-t|z|1)`,

    1<=Z_c<=1+4c/t²,
    J(f_c)<=J(f_sigma)+16c/t^4.                          (MOM-T)

Here `integral exp(-t|z|1)=4/t²` and `integral ||z||2²exp(-t|z|1)=16/t^4`, from the two product integrals. These ensure finite normalization and second moment; no arbitrary renormalization is assumed to preserve a fixed cost budget. The explicit cost change is accounted for in §8.

## 7. Square-cell averaging controls EVERY real diamond shift

For delta=1/M and the actual centered partition C_k, let

    p_k=integral_(C_k)f_c(z)dz,
    q_delta(z)=p_k/delta² on C_k.

For any two points of one cell their l1 distance is at most2delta. LOG-LIP therefore gives, for EVERY z,

    exp(-2delta/sigma) f_c(z)
        <=q_delta(z)<=exp(2delta/sigma) f_c(z).

Consequently for EVERY h∈the FULL CLOSED D,

    q_delta(z)
       <=exp(epsilon_lambda+4delta/sigma)q_delta(z+h).   (PRIV-BIN)

Choose `4delta/sigma<=epsilon-epsilon_lambda`. The averaged density is then EXACTLY epsilon-private at the original sensitivity, not epsilon-plus-an-unspecified-rounding-error and not only at grid alignments. The construction uses one canonical cell version; the resulting event inequality follows by integration. The half-open partition includes all boundaries, and changing null-set values would not create another law.

For the moment bound, use the purely mathematical coupling: X has density f_c and, conditional on its cell, Y is uniform in the same cell. Then Y has density q_delta and `||Y-X||2<=sqrt(2)delta`. Cauchy–Schwarz gives

    J(q_delta)<=J(f_c)
        +2sqrt(2)delta sqrt(J(f_c))+2delta².              (MOM-BIN)

This is a probability-kernel argument, NOT an executed sample or numerical quantizer. Tonelli verifies the cell masses sum to1.

Now choose an integer N with Ndelta>R. If k is outside H_N, every point of C_k has |z|1>R. Therefore

    p_k=(c/Z_c) product_(i=1,2)
                     integral_((k_i-1/2)delta)^((k_i+1/2)delta)
                                  exp(-t|x|)dx.

Put r=exp(-t delta). The one-dimensional cell integrals are EXACTLY `(2/t)pi_r(j)`:

- j=0: `2(1-exp(-t delta/2))/t=(2/t)(1-sqrt(r))`;
- |j|>=1: `exp(-t delta/2)(1-r)r^(|j|-1)/t=(2/t)pi_r(j)`.

Thus every outside cell has mass

    p_k=theta pi_r(k1)pi_r(k2),
    theta=(4c/t²)/Z_c.

The inner finitely many masses are precisely the free joint a_k. NORM holds by actual integration, not a separate asserted adjustment. Hence q_delta belongs to the explicit G family. All tails are infinite and present; nothing was silently truncated or treated as zero.

This proof deliberately does **not** carry over the scalar statement that the worst continuous shift lies at bin alignments to the planar diamond. Bilinear overlap functions on grid rectangles can restrict to quadratics on slanted diamond edges. PRIV-BIN supplies full continuous-shift privacy directly, so no unproved endpoint-only reduction is needed.

## 8. Uniform parameter selection proves REC and VALUE

Fix arbitrary finite epsilon>0 and arbitrary eta>0; write C=V(epsilon). All choices below are SYMBOLIC and uniform, not a numerical viability search.

1. Fix0<a<epsilon and then0<t<a. Choose0<lambda<1 so `lambda(4/a²)<eta/4`. This fixes a strictly positive privacy margin epsilon-epsilon_lambda by §4.
2. Choose sigma>0 with a sigma<1 and `4sigma²<eta/4`.
3. Choose c>0 so `16c/t^4<eta/4`. It fixes a finite R and positive finite Z_c.
4. Choose integer M sufficiently large so delta=1/M satisfies BOTH

       4delta/sigma<=epsilon-epsilon_lambda,
       2sqrt(2)delta sqrt(C+3eta/4)+2delta²<eta/4.

   Such an M exists because the privacy margin is strictly positive and the second left side tends to0. This is the Archimedean property, not an evaluated mesh bound or enumeration.
5. Choose integer N with Ndelta>R.

Combining the actual bounds gives

    J(g_lambda)<=C+eta/4,
    J(f_sigma)<=C+eta/2,
    J(f_c)<=C+3eta/4,
    J(q_delta)<=C+eta.

PRIV-BIN makes q_delta fully epsilon-private. By definition of the ORIGINAL all-law optimum, `J(q_delta)>=V(epsilon)=C`, proving REC. Since G is a subclass of the ORIGINAL additive Borel-law class, its epsilon-private infimum cannot be below V. The constructed candidate for EVERY eta>0 proves the opposite inequality, hence VALUE.

All parameter domains remain honest: M,N are finite but unbounded as accuracy increases; r∈(0,1); tails have positive geometric decay; the head is joint; the privacy parameter is the exact original epsilon. No one fixed finite family or universal finite precision is asserted adequate.

## 9. ALL near-optimal law choices and exact logical limits

Let q_n∈G be ANY full-D epsilon-private sequence with J(q_n)→V(epsilon). Its moments are eventually bounded by V(epsilon)+1, giving tightness. For ANY fixed h∈D and nonnegative bounded continuous compactly-supported test phi, the event inequality gives

    integral phi dq_n <=exp(epsilon)integral phi(z-h)dq_n(z).

It passes through the SAME weak subsequence. Radon measure order recovers the all-Borel inequality for each arbitrary fixed h, including the boundary, without an h-dependent subsequence or an uncountable RN intersection. Portmanteau gives limit cost<=V(epsilon); the definition of V gives equality, and LAW642 uniqueness identifies the limit law as mu_*.

Every cluster point is that law. Weak compactness/metrizability forces the whole sequence to converge weakly to mu_*. Its costs converge by hypothesis and REC supplies such sequences. No total-variation, uniform-density, finite-order or algorithmic convergence claim is hidden in this statement.

The REC/VALUE theorem is independent of the first new packet's alpha→infinity optimization interchange. Combining the two new candidates, once EACH receives its actual gate and a proper composition if needed, can connect finite joint families to the registered Rényi/pure endpoint. Neither candidate is adopted merely because this logical composition is available.

## 10. Exact source-equivalence/priority consequence and remaining work

**A proved candidate bridge, not a title comparison:** a concrete correlated joint finite-head/geometric-tail analogue CAN recover the all-law registered pure-DP value, with EVERY continuous diamond shift controlled and exact epsilon retained. It is therefore inappropriate to claim that geometric tails or finite-dimensional parameterization are inherently incompatible with the clipped-core optimum, or to use the objective/family labels alone as a worldwide non-equivalence argument. G25 and its earlier scalar-tail ancestry remain positive PRIOR methodology.

**What is NOT proved:** G25's ACTUAL scalar theorem is not being relabeled a planar theorem; this note explicitly extends the representation. No published claim is refuted. The closed form of V, angular/core selection, independent lower bound and all-law uniqueness remain imported from LAW642—not derived from solving the source's finite program. No fixed N/r/Delta theorem, quantitative mesh/complexity rate, verified finite list of diamond-shift constraints, solver/accountant convergence, public algorithm run or executable certificate is supplied.

**Priority:** convex mixing, convolution, max-order closure, envelope tails and cell averaging are standard/prior tools. This proof is an exact missing interface in our bounded comparison, not proof of a new mechanism, methodological priority, publishability or major contribution. The limited source read/search is not fieldwide exhaustion, and no assertion is made that every creative prior adaptation is inequivalent to the registered theorem. Novelty/priority remain UNCLEAR and stronger acceptance unperformed.

The remaining registered work is exact primary-source/overlap assessment and explicitly authorized stronger acceptance, with the unreconstructed K25 weighted-Step5, EG general-infimum and MDA/version/source qualifications still separately named. The new recovery representation is a genuine mathematical successor, not an invitation to repeat an inconsequential enumeration or reopen stopped auxiliary work.

## 11. Permanent process and delivery boundary

All first five individually recorded owner findings, SIXTH DISTINCT v111-B written-exactness finding, SEPARATE077 continuation-control failure and parent v21's additive compressed-category correction remain. No retroapproval, withdrawn-gloss/probe backconversion, unadmitted arithmetic/table credit or clean-cognition/runtime assurance follows. No source, prior packet, ACK, parent or review byte was edited.

No nonadditive/channel/full-book/model/slot cutover, auxiliary214 activity, formal/kernel/human/configured-family/cross-vendor/executable/novelty certification, publication or scientific GO. This complete author proof requires its OWN fresh source/mathematics/dependency/application gate. Same original eighteen owners, cutoff **2026-10-27T11:05:38-07:00**, deadline **2026-10-27T12:35:38-07:00**, substantive actual-clock checkpoints at most30minutes while active. This increment is **not an early final-park or round closeout**; registered research continues at the exact stated residual.
