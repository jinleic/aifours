# K25 source-proof edge: annular-weighted cyclic saturation after radial monotonicity

Owner **InfoResearch96h-2**, original info-1, continuing ONLY the registered privacy source-equivalence/proof residual. Actual `/bin/date` BEFORE this write: **Mon Oct 26 05:40:45 PDT 2026**. **NEW AUTHOR-WRITTEN CANDIDATE**, not independently reconstructed or parent-adopted. No mathematical machine check, scientific interpreter/eval/calculator/CAS/program/enumeration/table/solver/replay/CLI/nested agent or new GO. All calculations are exact written symbolic measure/geometry analysis.

## 0. Exact target, named hypotheses and source limits

The complete registered source-comparison parent `RUN/privacy-complete-source-equivalence-and-controls-parent-v1.md` explicitly leaves **K25 Lemma10's annular-weighted adaptation of scalar Step5 NOT_RECONSTRUCTED**. This note supplies a direct alternative weighted proof of precisely that cyclic-saturation implication AFTER the source's radial/nonincreasing reduction. It does not silently claim to have reconstructed every other K25 lemma or its entire theorem.

The primary source is [Kulesza–Suresh–Wang, *General Staircase Mechanisms for Optimal Differential Privacy*, AISTATS2025/PMLR258](https://proceedings.mlr.press/v258/kulesza25a.html), actual [publisher PDF](https://raw.githubusercontent.com/mlresearch/v258/main/assets/kulesza25a/kulesza25a.pdf). The retained reader snapshot `RUN/privacy-source-snapshot-K25-v1.txt`, SHA256 `fa58d0adc1ef43586f9c075fde7859fa893f3da93c6da8874c053081d5dcaa09`, is995 rendered logical LF, NOT original PDF-byte identity.

Current selected reads:1–45,46–84,75–130,350–400,650–790. They include actual norm/sensitivity definitions, the theoretical mean-K-norm loss, the formal Lemma10, and its literal proof at733–734, which consists of a reference to scalar Geng–Viswanath AppendixB Step5. This is not a fresh whole995LF read, glyph-by-glyph reconstruction of degraded Markit formulas, algorithm/experiment check or publication-wide certification.

**Source applicability inputs, explicitly NAMED rather than freshly proved here:**

- K25 Theorem1 selects an equicontour optimum for its SAME-norm loss.
- K25 Lemma9 supplies a nonincreasing radial representative in that optimization.

The statement proved below takes an actual radial NONINCREASING optimum as its hypothesis. Thus its new weighted implication does not depend on accepting the printed scalar-transfer analogy, but it also does not certify those preceding source reductions. Their formal scope is positively PRIOR, not a new geometric argument for the registered mismatched Euclidean MSE.

The geometry assumed here is a genuine norm body K: compact, convex, centrally symmetric, with nonempty interior in finite R^d, d>=1. This includes the registered K=D. No claim is made about degenerate/unbounded gauges not defining a norm, or sensitivity/cost hypotheses not satisfying this stated interface.

**Critical loss distinction:** K25's theoretical loss is `J_K(P)=integral ||z||_K dP`, NOT registered `integral ||z||2² dP` under l1 sensitivity. This proof must not be transplanted to the mismatched registered MSE problem by changing the annular cost while keeping an unjustified radial optimum. The registered LAW642 remains its separate adopted theorem.

The actual v112-I RETURN and Main's prospective permission preceded the separately SENT whole-primary ACK SHA256 `832d6f181a3e5a4a6dc3bb27061ceedb32ccaf38c50c1f7d02a1e058ccecdf5b`. The complete new lead was saved in checkpoint088. All original findings, strict auxiliary214STOP and HOLD remain. No auxiliary family, nonadditive/channel/model/slot cutover, novelty or early final-park is involved.

## 1. Exact conditional statement and ordinary facts

Fix a finite epsilon>0, b=exp(-epsilon)∈(0,1), and the above K. Let P be a Borel probability law on R^d, private for EVERY Borel event and EVERY shift h∈the FULL CLOSED K. Suppose

    p(z)=f(||z||_K) a.e.,
    f is nonincreasing on [0,infinity),

and P minimizes J_K over the full private class (it is enough that it minimizes over all radial private laws). Its optimal value v is finite: the K-norm exponential density is a finite-cost private comparator. Put V_K=Lebesgue volume(K)>0.

**Claim — WRITTEN at exactly these hypotheses.** For the source's forward-annular upper density

    fhat(r)=limsup_(delta down0)
        [ integral_r^(r+delta) f(s)d(V_K s^d)
                         / (V_K((r+delta)^d-r^d)) ], r>0,
    fhat(0)=limsup_(r down0) fhat(r),

we have

    fhat(r+1)=b fhat(r) for EVERY r>=0.                   (CYCLIC)

This is K25 Lemma10's equality at its explicit radial/monotone interface. No evaluated optimal parameter, uniqueness of the norm-cost optimizer, source algorithm or entire-paper proof is claimed.

Ordinary facts used: finite Radon order/essential supports; positive Tonelli; the norm-ball volume identity `|RK|=V_K R^d` and zero Lebesgue measure of convex-body boundaries; elementary differentiation of ONE finite term; and right limits of bounded monotone functions. The amplitude-phase decomposition and every weighted perturbation needed here are supplied below, not imported as an absent research theorem.

## 2. Density cap and amplitude phases apply at the actual annular weights

The density cap is a consequence of full-K privacy, not an assumed peak. For each fixed h, event privacy gives `p(z+h)>=b p(z)` for a.e. z. Fubini and integration over h∈K give

    b V_K p(z)<=integral_K p(z+h)dh<=1 for a.e.z.

Hence0<M=esssup p<=1/(bV_K)<infinity. Feasible density cannot vanish on a positive-volume set: a bounded positive-volume zero set would have probability zero under EVERY translation by privacy iteration, while Tonelli over translations gives its positive Lebesgue volume. Thus p>0 a.e. These are positive-volume sensitivity facts, not density regularity of a finite-grid substitute.

For a∈[bM,M), define

    n_a(z)=min{k>=0 integer:p(z)>a b^k},
    u_a(z)=b^n_a(z),
    Z_a=integral u_a(z)dz,
    q_a(z)=u_a(z)/Z_a.

At the null zero set set u_a=0. Minimality of the index gives

    b p(z)/a<=u_a(z)<=p(z)/a,
    b/a<=Z_a<=1/a.

The k=0 case uses a>=bM. The functions are jointly measurable in(a,z); all phases have positive finite mass and finite J_K.

For EVERY fixed h∈K, its original density inequality holds outside a null set independent of a. If p(z)>a b^k, then p(z+h)>a b^(k+1). The reverse shift gives index difference<=1; every normalized phase law q_a is therefore private for the whole closed K. No common uncountable-h RN version was assumed.

The exact layer identity and threshold substitution give

    u_a(z)=(1-b)sum_(i>=0)b^i 1_(p(z)>a b^i),
    p(z)=integral_(bM)^M u_a(z)da/(1-b).

Tonelli now gives

    integral_(bM)^M Z_a da/(1-b)=1,
    v=J_K(P)=integral_(bM)^M J_K(q_a) Z_a da/(1-b).       (PHASE)

Every q_a is a feasible radial law and has cost>=v. Hence ONE full-weight set of phases, defined only by `J_K(q_a)=v`, consists of optimal geometric phases. This set does not depend on a radius or Borel event. Positive weights Z_a also make its complement Lebesgue-null in the a interval.

## 3. Full-K privacy gives exact radius-gap constraints

Because f is nonincreasing, each phase sublevel set

    E_i={z:n_a(z)<=i}={z:p(z)>a b^i}

has essential support `K_i=R_i K` for a finite radius R_i. The top set has positive volume for a<M, so R_0>0; all later R_i are finite since their fixed positive density threshold gives finite volume.

For each fixed h∈K, phase privacy gives `E_i+h subset E_(i+1)` a.e. Therefore their closed essential supports satisfy `K_i+h subset K_(i+1)`. The h was arbitrary, so

    R_i K+K=(R_i+1)K subset R_(i+1)K,
    R_(i+1)>=R_i+1 for EVERY i.                         (GAP)

The Minkowski equality uses convexity of K. This argument retains ALL real shifts including the boundary, rather than checking only an integer radial recurrence.

Conversely, ANY positive-radius sequence satisfying GAP defines a feasible radial geometric law by the closed-level index

    n_R(z)=min{i>=0:z in R_i K},
    u_R(z)=b^n_R(z).

The levels cover R^d because GAP forces R_i→infinity. The inclusion `R_iK+K subset R_(i+1)K` gives index difference<=1 under any h∈K. If mass and first norm moment are finite, normalizing u_R yields a genuine full-K private competitor. This supplies the actual feasible perturbations used next.

The layer formula, ignoring only countably many zero-volume sphere boundaries, gives

    Z(R)=(1-b)V_K sum_(i>=0)b^i R_i^d,
    N(R)=(1-b)V_K d/(d+1) sum_(i>=0)b^i R_i^(d+1),
    J_K(u_R/Z)=N(R)/Z(R).                              (ANN)

Here `integral_(RK)||z||_K dz = V_K d R^(d+1)/(d+1)` follows directly from the exact volume function. These are the ACTUAL annular weights; no constant shell volume or scalar probability normalization is substituted.

## 4. Every slack radius gap is strictly improvable

Take any cost-good phase from PHASE, so initially `N(R)-v Z(R)=0`. Change just ONE radius, retaining every other one. The derivative of this signed quantity is exactly

    derivative_(R_i)[N-vZ]
       =(1-b)V_K d b^i R_i^(d-1)(R_i-v).                (DER)

No infinite-series differentiation is involved: only one finite term changes in each sum. Every coefficient before(R_i-v) is strictly positive because R_i>0 and b>0.

Suppose `R_(i+1)-R_i>1`.

- If R_i<v, raise R_i by a sufficiently small positive amount less than the slack. The previous gap increases, the next stays at least1, and all other gaps are unchanged. DER is strictly negative, so N-vZ becomes negative.
- If R_i>=v, lower R_(i+1) by a sufficiently small positive amount less than the slack. Its new value stays above R_i+1>0, the following gap increases, and all other constraints stay valid. Since R_(i+1)>v, DER there is strictly positive; lowering that radius again makes N-vZ negative.

The new law is a full-K feasible competitor by §3. Mass and moment remain finite and its normalizer remains positive, because only one bounded-radius term was changed. `N-vZ<0` therefore means its normalized actual cost is STRICTLY below v, contradiction.

Thus **EVERY** gap of every cost-good geometric phase is saturated:

    R_i=t+i for all i>=0, with t=R_0>0.                 (PARALLEL)

This proves the weighted maximal-decay step by a direct radius variation. The sign test uses the actual radius minus the actual optimal mean norm cost; it is not the scalar Step5 transfer with annular weights silently removed.

## 5. The top plateau cannot have radius greater than1

Let

    phi_t(z)=b^max(0,ceil(||z||_K-t)), t>=0,
    Q_t=phi_t/(integral phi_t).

Every PARALLEL phase is Q_t. For t>1 there is the exact a.e. identity

    phi_(t-1)=b phi_t+(1-b)1_((t-1)K).                 (INNER)

Inside(t-1)K both plateau densities are1. Outside, the integer index is raised by1, proving INNER without an approximation.

After normalization, Q_(t-1) is a strictly positive convex mixture of Q_t and the uniform law on(t-1)K. The latter's mean norm cost is

    d(t-1)/(d+1).

Meanwhile ANN expresses Q_t as a positive volume-weighted mixture of uniforms on(t+i)K, every one having mean norm at least `dt/(d+1)`. Therefore

    J_K(Q_t)>=dt/(d+1)>d(t-1)/(d+1),
    J_K(Q_(t-1))<J_K(Q_t).

Q_(t-1) is feasible by the same unit-gap construction, so t>1 contradicts phase optimality. Hence

    0<t<=1 for EVERY cost-good phase.                  (TOP)

The t=0 endpoint need not be a positive-area top phase; as a law it is represented by t=1 because phi_0=b phi_1 a.e. This does not produce a second optimizer or an undefined zero normalizer.

For TOP and every r>0, the radial profile has

    phi_t(r+1)=b phi_t(r),

apart from immaterial radius-boundary version changes. In particular every cost-good phase satisfies that equality almost everywhere in positive radius. No optimization of t, uniqueness of the best t or source Lemma11 is needed.

## 6. All original radial optimizers inherit cyclic saturation

The phases u_a(r), normalizers Z_a and costs are jointly measurable. PHASE's single good-phase set has full weight independently of r. For every good a, the corresponding radial profile q_a satisfies the just-proved cyclic equality for a.e.r>0. Tonelli on the nonnegative radial/phase functions therefore gives

    f(r+1)=b f(r) for a.e.r>0.                          (AE)

Using a separate good set for each r would be unnecessary and would not justify an uncountable intersection; the argument uses ONE cost-defined set and joint measurability. Nor is uniqueness of the original radial optimum assumed.

## 7. Exact source upper-radial representative, including r=0

Since f is bounded and nonincreasing, its right-limit representative `f^+(r)=lim_(s down r,s>r)f(s)` exists and is right-continuous for r>0. On the annulus[r,r+delta], monotonicity bounds its volume-weighted average between the endpoint right limits. Both tend to f^+(r) as delta↓0. Therefore the source's forward-annular upper density satisfies

    fhat(r)=f^+(r) for EVERY r>0.

This explicitly retains the annular volume denominator; no ordinary unweighted average is called identical at finite delta.

AE also holds for this a.e.-equal representative. For any fixed r>0 choose radii s approaching r from above in the full-measure set where AE and both representative identifications hold. Right continuity at r and r+1 gives

    fhat(r+1)=b fhat(r) for EVERY r>0.

Finally bounded monotonicity makes the source's limsup at0 a genuine finite right limit. Let r↓0 in that identity and use right continuity at1:

    fhat(1)=b fhat(0).

This proves CYCLIC at EVERY r>=0, exactly including the source's declared0 convention. It does not assert continuity of the radial density or arbitrary pointwise versions at jumps.

## 8. Source disposition and exact remaining boundaries

**New scoped source-proof candidate:** after the explicitly NAMED radial/nonincreasing optimum inputs, the missing weighted cyclic-saturation implication is now supplied by full annular formulas, finite feasible radius variations, top-plateau exclusion, same-law amplitude mixture and the exact upper-density representative argument. This is a complete replacement proof of that edge, not a claim that the source's one-line reference already contained it or that the scalar transfer is automatically valid in every weighted setting.

**Not certified here:** K25's Theorem1 radialization, Lemma9's own printed proof, Lemma11/all staircase-selection steps, its radial discretization/limit claims, every density representative/regularity claim outside the stated hypotheses, algorithms, sampling and experiments. The current Markit terminal monotonicity wording and other formula degradation are not turned into a public source-falsity or publication-wide verdict. The old noncompact-attainment shortcut still requires its separately supplied tightness/LSC repair.

**Registered mismatch remains:** a K-radial selected optimum for mean||z||_K does not select the all-law squared-Euclidean MSE optimum when K=D. Cone averaging preserves that matched radial loss but may increase the registered MSE, as the existing exact controls show. The new proof does not cancel that distinction, reopen a retired homothetic-diamond optimality claim, upgrade old578LF arithmetic or derive LAW642 from the K25 theorem.

**Attribution:** generic phase slicing, shell/parallel-body laws, privacy saturation and standard variation/compactness tools have substantial PRIOR ancestry. This note closes our missing written interface; it is not a new mechanism/comparison-method discovery, priority or publishability certificate. Novelty/priority remain UNCLEAR. A fresh COMPLETE source/mathematics/dependency/application gate is required before parent promotion of this successor; the existing source adoption does not silently cover it.

All first five owner findings, SIXTH DISTINCT v111-B written-exactness finding, SEPARATE077 continuation failure, v21 category correction, other parent/reviewer/process/source/import qualifications and N4 UNKNOWN/exit history remain. No old table/probe/gloss is replayed or back-converted; no clean-history/cognition/runtime assurance. Auxiliary214 remains UNADMITTED/strict STOP; no nonadditive/channel/model/slot change, formal/kernel/human/family/executable/novelty/publication acceptance or scientific GO. Same eighteen owners, cutoff **2026-10-27T11:05:38-07:00**, deadline **2026-10-27T12:35:38-07:00**, substantive actual-clock checkpoints at most30minutes while active. This is not an early final-park or round closeout; the exact registered source residual continues.
