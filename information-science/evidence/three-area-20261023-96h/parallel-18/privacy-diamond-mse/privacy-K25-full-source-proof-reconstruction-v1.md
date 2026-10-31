# K25 SAME-norm theorem: full-law rearrangement, attainment and exact staircase classification

Owner **InfoResearch96h-2**, original info-1. Actual `/bin/date` BEFORE this write: **Mon Oct 26 05:56:44 PDT 2026**. **NEW AUTHOR-WRITTEN, UNREVIEWED joint-source-proof candidate.** This is the logical union of THIS body and `privacy-K25-weighted-cyclic-saturation-proof-v1.md`,208LF, SHA256 `3dff72bfd9984a8d7977fa089811337db963b3e1865666aa55139ea94754f2d7` (abbreviated **WS208**). Both are new candidates; neither inherits adoption from older source reviews.

## 0. Exact purpose, theorem and non-transfer boundary

The earlier WS208 proof replaced K25Lemma10's missing annular-weighted scalar-Step5 transfer AFTER explicitly NAMED K25 radial/nonincreasing-optimum inputs. This successor discharges BOTH inputs by an actual full-law Brunn–Minkowski/strict-bathtub argument and gives an independent tightness/LSC attainment proof. The new UNION therefore proves K25Theorem2's theoretical SAME-norm existence claim without using any K25 research lemma as a correctness premise. It does not certify every printed proof, algorithm, experiment or all-wording of that publication.

Primary source attribution remains [Kulesza–Suresh–Wang2025, *General Staircase Mechanisms for Optimal Differential Privacy*](https://proceedings.mlr.press/v258/kulesza25a.html), actual [publisher PDF](https://raw.githubusercontent.com/mlresearch/v258/main/assets/kulesza25a/kulesza25a.pdf). Its theorem is positively PRIOR, not discovered by this reconstruction. The retained reader snapshot is `RUN/privacy-source-snapshot-K25-v1.txt`, SHA256 `fa58d0adc1ef43586f9c075fde7859fa893f3da93c6da8874c053081d5dcaa09`; a reader-snapshot hash is NOT original-PDF identity.

**Theorem — WRITTEN at named classical imports and WS208.** Let d>=1 be a finite integer, K⊂R^d a compact convex centrally symmetric norm unit ball with nonempty interior, r(z)=||z||_K, finite epsilon>0 and b=exp(-epsilon)∈(0,1). Among ALL Borel probability laws satisfying

    mu(A)<=b^(-1)mu(A+h)
    for EVERY Borel A and EVERY h in the FULL CLOSED K,         (DP_K)

minimize the SAME-norm loss

    J_K(mu)=integral r(z)mu(dz),    v_K=inf J_K(mu).

Then:

1. A finite-cost optimum exists; every optimal law has a bounded positive density equal a.e. to a K-radial nonincreasing representative.
2. Some optimum has density proportional to

       phi_t(z)=b^max(0,ceil(r(z)-t)),   0<t<=1.                (STAIR_K)

3. Every optimal law is a convex mixture of the optimal STAIR_K laws. In fact an explicit finite candidate set of at most2d+2 scalar parameters suffices; the precise full convex class is given in §7. No uniqueness or irreducibility of that scalar selector is assumed.
4. Every radial optimal law's forward-annular upper density obeys `fhat(r+1)=b fhat(r)` for EVERY r>=0, including its prescribed0 limit.

**This is NOT the registered mismatched MSE theorem.** Registered info-1 uses sensitivity K=D (unit l1 diamond) but loss||z||2². The radial rearrangement below decreases SAME-norm mean cost, and need NOT decrease squared-Euclidean cost for that diamond. LAW642 remains the separate adopted registered result. No scalar root/value of the registered MSE problem, old578LF arithmetic, nonadditive mechanism or new model/slot is supplied or upgraded here.

## 1. Named imports and proof interfaces

Only the following ordinary classical facts are imported:

- Radon–Nikodym for finite Borel measures on Euclidean space; Lebesgue inner regularity/density-point theorem; positive Tonelli/Fubini and monotone convergence.
- A finite Radon-measure order follows from all nonnegative continuous compactly supported test functions.
- Tight probability sequences in finite Euclidean space have weakly convergent subsequences (Prokhorov); nonnegative lower-semicontinuous costs obey Portmanteau's liminf bound.
- **Brunn–Minkowski**, in the exact form `|C+U|^(1/d)>=|C|^(1/d)+|U|^(1/d)` for compact positive-volume C and bounded open positive-volume U in R^d.
- Norm triangle inequality, norm-ball volume `|RK|=|K|R^d`, zero volume of convex-body boundaries, elementary differentiation, compact-interval minimization and uniformly convergent geometrically weighted polynomial series.

The model-specific privacy-preserving rearrangement, equality case, all-law attainment and full optimizer-class deduction are proved below. **WS208 §§2–5** supplies the complete amplitude-phase and annular-radius variation argument; **WS208 §§6–7** supplies the all-radius upper-density completion. Those are new written proof imports in this UNION, not already reviewed facts. Its K25 radialization/Lemma9 hypotheses are discharged by §§2–5 below, so no circular research import remains.

Standard K-ball rearrangement, shell laws, phase slicing, saturation, finite scalar selection and compactness have substantial PRIOR ancestry. This is a source-proof repair/reconstruction, not mechanism/method novelty or a new scientific discovery count.

## 2. Actual all-Borel laws have capped densities

Write V_K=|K|>0. If N is Lebesgue-null, integrate DP_K's inequality over h∈K. Tonelli gives

    V_K mu(N)<=b^(-1)integral_K mu(N+h)dh=0.

Indeed, for each fixed z, `{h:z in N+h}` is a translate/reflection of N and is null. Thus mu is absolutely continuous. Choose a nonnegative Borel RN density p.

For EACH fixed h∈K, the event inequalities give `p(z+h)>=b p(z)` for a.e.z. Their exceptional set need not be chosen uniformly over h. Joint measurability and Fubini nevertheless give for a.e.z

    b V_K p(z)<=integral_K p(z+h)dh<=1.

Consequently `0<M=esssup p<=1/(bV_K)<infinity`.

For completeness p>0 a.e. If a bounded measurable positive-volume Z had p=0 on it, then mu(Z)=0. Privacy iterates to EVERY h∈R^d, by writing h as a finite sum of vectors in K, and gives mu(Z+h)=0 for every h. But

    integral_(R^d) mu(Z+h)dh=|Z|>0,

contradiction. Any positive-volume zero set contains such a bounded subset. This argument is for full continuous shifts, not a coordinate/grid privacy substitute.

## 3. Full-K privacy forces a volume-radius growth inequality

For t>0 define

    A_t={z:p(z)>t},
    R(t)=(|A_t|/V_K)^(1/d).

These are finite-volume sets since `t|A_t|<=1`. The radius function is nonincreasing, measurable and right-continuous: if u decreases to t from above, the sets A_u increase to A_t. For t<M its radius is strictly positive.

**Claim — WRITTEN from DP_K, density points and Brunn–Minkowski.** Whenever |A_t|>0,

    R(bt)>=R(t)+1.                                      (R_GROW)

For a fixed h∈K, density privacy gives `A_t+h subset A_bt` a.e. Define the essential-enlargement convolution

    F_t(z)=integral_(int K) 1_(A_t)(z-h)dh.

Fubini, for this FIXED t, gives

    F_t(z)<=V_K 1_(A_bt)(z) for a.e.z.                  (ESS_ENLARGE)

This is not a false literal inclusion for an uncountable union of exceptional null sets.

Let C be any compact subset of the Lebesgue-density points of A_t with positive volume. If z=c+h0 with c∈C and h0∈intK, then z-intK contains a neighborhood of c. Since c is a density point, this neighborhood meets A_t in positive volume. Therefore F_t(z)>0, pointwise. Thus

    C+intK subset {F_t>0},
    |A_bt|>=|C+intK|.

Brunn–Minkowski and `|intK|=V_K` yield

    |A_bt|^(1/d)>=|C|^(1/d)+V_K^(1/d).

By inner regularity, compact C inside A_t's density-point set can have volume arbitrarily close to |A_t|. This proves R_GROW. The zero-volume case is deliberately NOT assigned a false growth bound. It is unnecessary in every later use.

The proof applies to each t>0 as a mathematical implication; no common uncountable-t exceptional set is used. Its conclusion is a numeric volume inequality, not an a.e. density statement needing synchronization.

## 4. Equal-volume K-ball rearrangement is actually fully private

Define, for every z∈R^d,

    psharp(z)=sup{t>0:r(z)<R(t)},   sup(empty)=0.         (REARR_K)

Right-continuity of R gives the EXACT strict-level identity

    {z:psharp(z)>t}={z:r(z)<R(t)} for EVERY t>0.         (LEVEL_K)

To see the nontrivial direction, if r<R(t), right-continuity supplies u>t with r<R(u), so the supremum exceeds t. Conversely a supremum>t supplies such a u>t and monotonicity gives R(t)>=R(u)>r.

Hence psharp is a measurable K-radial nonincreasing density with cap M. Layer cake gives

    integral psharp dz=integral_(t>0)V_K R(t)^d dt
                     =integral_(t>0)|A_t|dt=1.          (MASS_K)

Fix ANY z and ANY h∈the full CLOSED K. If0<t<psharp(z), LEVEL_K gives `r(z)<R(t)`, so R(t)>0 and R_GROW applies. The norm triangle inequality gives

    r(z+h)<=r(z)+1<R(t)+1<=R(bt).

LEVEL_K gives `psharp(z+h)>bt`. Let t increase to psharp(z) to obtain

    psharp(z+h)>=b psharp(z) for EVERY z,h∈K.           (POINT_DP_K)

The notation means every z∈R^d and h∈K, not z restricted to K. If psharp(z)=0, the inequality is automatic. Applying it also to -h and integrating over any Borel event proves actual DP_K of its probability law. Thus both the normalization and full-shift feasibility are supplied; rearrangement is not merely a formal lower bound on costs.

Iterating R_GROW from any0<t0<M also shows R(b^n t0)>=R(t0)+n. Therefore psharp(z)>0 for every finite z. No zero-support boundary or finite radius cutoff is inserted.

## 5. Strict same-norm bathtub equality forces ALL optimal laws to be radial

Fix t>0 and let `B_t={r<R(t)}`, the equal-volume open K-ball from LEVEL_K. Put R=R(t). Its mean-norm integral is finite. Since |A_t|=|B_t|, the exact signed difference is

    D(t)=integral_(A_t)r dz-integral_(B_t)r dz
        =integral_(A_t\B_t)(r-R)dz
          +integral_(B_t\A_t)(R-r)dz>=0.              (BAT_K)

The difference is well-defined even when the first integral is infinite, because the ball integral is finite. For R>0, both integrands are strictly positive away from the zero-volume sphere r=R. Thus equality holds iff `|A_t symmetricdifference B_t|=0`. For R=0 both sets are null and the same equality conclusion holds.

Positive Tonelli and LEVEL_K now give

    J_K(psharp)<=J_K(p).                               (COST_K)

When p is an optimal finite-cost law, §4 makes psharp a genuine feasible competitor. Therefore equality must hold in COST_K. The nonnegative measurable deficit D(t) has integral zero, so D(t)=0 for a.e.t. Its strict equality case and Tonelli give

    integral |p-psharp|dz
      =integral_(t>0)|A_t symmetricdifference B_t|dt=0.

Consequently **EVERY** original optimal law already equals its K-radial nonincreasing rearrangement as a probability law. This is not an averaging argument or the mere selection of some different symmetric optimum.

**Exact limitation:** BAT_K compares `integral ||z||_K`, with its own equal-volume K-balls. Replacing that integrand by||z||2² while keeping a diamond K destroys the sign argument. The existing registered mismatch controls are not contradicted, and no registered MSE radiality is inferred.

## 6. Attainment is tightness plus closed privacy plus LSC, not a closed-set shortcut

The density proportional to `exp(-epsilon r(z))` is DP_K by the norm triangle inequality. Its mass and first norm moment are finite from the exact volume formula; in polar volume they are integrals of a polynomial times the decreasing exponential. Thus `v_K<infinity`.

Choose a minimizing sequence mu_n with uniformly bounded J_K. Markov bounds the mass outside RK by a constant divided by R, so the sequence is tight because norm balls are compact. Prokhorov gives ONE weakly convergent subsequence, with probability limit mu.

For each fixed h∈K and each nonnegative continuous compactly supported test function psi,

    integral psi(z)mu_n(dz)
       <=b^(-1)integral psi(z-h)mu_n(dz).

Both test functions are bounded continuous, so the SAME weak convergence passes this inequality to mu. Finite Radon order then gives the event inequality for every Borel event. The subsequence was not chosen as a function of h; h was arbitrary, so mu satisfies DP_K for EVERY h∈the full closed K.

The nonnegative continuous norm cost is lower semicontinuous under weak limits:

    J_K(mu)<=liminf J_K(mu_n)=v_K.

By feasibility it equals v_K. This is actual attainment. It does NOT assert that an arbitrary continuous linear functional attains its infimum on a merely closed noncompact set of probability measures. The earlier source shortcut is replaced, not silently endorsed.

By §§2–5 this attained law has an actual bounded positive radial nonincreasing density, so every hypothesis of WS208's new annular argument is now discharged without using a K25 correctness premise.

## 7. Exact full optimizer class and finite scalar selector

### 7.1 Logical use of the complete WS208 proof

Apply WS208 §§2–5 to any optimizer established above. Its same-law amplitude mixture has ONE full-weight cost-good phase set. Every good phase is a normalized geometric radial law with positive radii R_i and the full-K constraints `R_(i+1)>=R_i+1`.

WS208's actual annular formulas and ONE-radius signed derivative show every gap is1: any larger gap permits either raising its lower radius below v_K or lowering its upper radius above v_K, strictly reducing normalized actual cost. Its exact INNER mixture excludes top radius>1. Therefore every cost-good phase is precisely Q_t, the normalized STAIR_K law, with0<t<=1.

This immediately proves existence of an optimal generalized staircase. There is no need to invoke K25Lemma11, pass an unproved radial discretization limit, choose a numerical grid or assume a scalar root is unique.

WS208 §§6–7 also now applies to every original radial optimum and gives its exact upper-annular cyclic equality for EVERYr>=0. That representative conclusion uses monotone right limits and the actual annular denominator, not an arbitrary pointwise version of a density at a jump.

### 7.2 Actual norm-cost function, not the registered MSE selector

For0<=t<=1 let Q_t be normalized phi_t. Its cost from WS208's annular formula is

    C_d(t)=d/(d+1) * M_(d+1)(t)/M_d(t),
    M_j(t)=(1-b)sum_(i>=0)b^i(t+i)^j.                   (SCALAR_K)

The factors V_K cancel. At t=0 the i=0 denominator term is zero but the i=1 term is strictly positive; there is no zero normalizer. Moreover `phi_0=b phi_1` a.e., so Q_0=Q_1 and C_d(0)=C_d(1). The single origin value is immaterial.

Each M_j is a degree-j monic polynomial in t:

    M_j(t)=sum_(k=0)^j binom(j,k)t^(j-k)g_k(b),
    g_0(b)=1,
    g_k(b)=(1-b)(b d/db)^k[1/(1-b)] for k>=1.           (GEOM_K)

This is an exact rational-function formula over Q(b), obtained from the ordinary geometric series. It is not a symbolic-program output, minimal-polynomial claim or numeric root evaluation.

Uniform convergence of the geometrically weighted polynomial sums gives continuity of C_d on[0,1], and M_d(t)>0 throughout. The preceding existence proof and phase selection imply

    v_K=min_(0<=t<=1) C_d(t).                          (VALUE_K)

Let

    E_d(t)=(d+1)M_d(t)^2
                -d M_(d+1)(t)M_(d-1)(t),
    A_b={0,1} union {t in(0,1):E_d(t)=0},
    T_b={t in A_b:C_d(t)<=C_d(s) for EVERY s in A_b}.   (SELECT_K)

The derivative of C_d has the sign of E_d. Its leading coefficient is(d+1)-d=1, so E_d is a NONZERO degree2d polynomial. Consequently A_b has at most2d+2 elements, T_b is nonempty, and VALUE_K's full minimizer set is exactly T_b. This supplies a finite exact algebraic selection rule, not just an unspecified grid search. E_d is a stationarity polynomial, NOT claimed irreducible or minimal.

### 7.3 Every and only optimizer is in this finite convex class

**Full class — WRITTEN at the preceding proofs:**

    Opt_K=conv{Q_t:t in T_b}.                          (ALL_K)

One direction is immediate but substantive: each Q_t is fully DP_K by WS208's level inclusions, and has cost v_K by SELECT_K. Any convex mixture stays private and has that same cost.

For the other direction take any optimal law with its same-law radial representative p. The amplitude-phase mixture in WS208 has weights `Z_a da/(1-b)` on a∈[bM,M), total1, and one cost-good set of full weight. Its top phase radius is

    t(a)=(|{p>a}|/V_K)^(1/d).

This is a measurable function of a; on the good set, WS208 proves0<t(a)<=1 and the phase law is Q_(t(a)). Its cost is v_K, so t(a)∈T_b. Push the phase probability measure forward by this measurable radius. This gives an ACTUAL probability mixture supported on T_b and equal to the original optimal law by the exact amplitude identity. Since T_b is finite, this is the finite convex class ALL_K, not an unverified closure or an uncountable-convex-hull assertion.

The endpoints0 and1 name the same law and may be identified. Whether the other candidate parameters collapse to a single law is NOT assumed or proved. The explicit finite full class makes an unnecessary uniqueness claim avoidable.

## 8. Source/proof applicability and precise remaining assurance

The UNION of this body and WS208 now supplies a complete alternative WRITTEN proof of the SAME-norm theoretical generalized-staircase existence theorem at its explicit norm-body hypotheses. It also supplies full-law radiality, the correct upper-density cyclic property and the finite convex optimizer class, each with the actual model-specific bridges above. The previously missing radial/monotonicity inputs are no longer opaque research premises in this UNION.

This does **not** certify that the source's printed angular averaging, discretization, one-line Step5 analogy, compactness prose or all-optimal-profile Lemma11 are individually correct as written. The replacements are logically sufficient for the named theoretical conclusion; algorithms, sampling, plots, empirical other-metric comparisons and publication-wide claims remain outside this reconstruction. No field-wide absence, source falsity, public refutation or novelty/publishability verdict follows.

The original registered full-diamond squared-Euclidean MSE theorem, LAW642, its separately scoped BRANCH-OLD578 parameter algebra and every source/priority/control disposition remain unchanged. In particular this SAME-norm C_d is NOT substituted for the registered clipped-core scalar system. Stronger original-model/whole-book/channel assertions remain unclaimed.

A fresh COMPLETE joint-source/mathematics/dependency/application gate over BOTH new bodies is required before parent promotion. Earlier source reviews or review of WS208 alone cannot silently accept this enlarged import union. Neither exact written mathematics nor source repair supplies formal/kernel/human/configured-family/cross-vendor/executable/finite-witness-triple/novelty/publication acceptance.

## 9. Execution, chronology and unchanged process record

All mathematics above is exact WRITTEN symbolic measure/geometry/algebra. **No scientific interpreter, eval cell, calculator, CAS, enumeration, generated checker, solver, replay, external CLI or nested agent was used. No kernel machine check is claimed.** Metadata clocks/hashes/LF and public source reads do not back-convert the old unadmitted arithmetic, probes or private approximate glosses into credit.

The new Brunn–Minkowski lead was saved in checkpoint089 before this full body. Registered primary resumption authority remains Main's prospective post-v112 instruction followed by the separately SENT whole-primary ACK SHA256 `832d6f181a3e5a4a6dc3bb27061ceedb32ccaf38c50c1f7d02a1e058ccecdf5b`. There is no live-review interleaving or auxiliary derivation here.

Retain all firstfive owner findings, SIXTH DISTINCT v111B written-exactness finding, SEPARATE077 continuation failure, v21 category correction, strict auxiliary214STOP/UNADMITTED, every parent/reviewer/source/import qualification and N4 UNKNOWN/exit history. No clean-thought/runtime/history or continuous-work census is asserted. No new science GO, slot/model cutover, publication, deadline reset or early final-park. Same eighteen owners; science cutoff **2026-10-27T11:05:38-07:00**, delivery **2026-10-27T12:35:38-07:00**; actual substantive checkpoints at most30minutes while active. The registered source/proof/priority residual continues.
