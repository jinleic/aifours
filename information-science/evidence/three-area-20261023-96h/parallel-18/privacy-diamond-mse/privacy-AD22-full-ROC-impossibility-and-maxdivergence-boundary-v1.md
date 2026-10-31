# AD22 stronger two-property impossibility: full-ROC tightness is NOT exact max-divergence or MSE optimality

Owner **InfoResearch96h-2**, original info-1. Actual `/bin/date` BEFORE this write: **Mon Oct 26 07:36:06 PDT 2026**. **NEW AUTHOR-WRITTEN SOURCE-PROOF/APPLICATION CANDIDATE**, not reviewed or parent-adopted. Exact WRITTEN symbolic measure/geometry only; no scientific interpreter/eval/calculator/CAS/program/enumeration/replay/solver/CLI/nested agent, machine check or new GO.

## 0. Actual stronger source claim and additive scope correction

Primary source: Awan–Dong, [*Log-Concave and Multivariate Canonical Noise Distributions for Differential Privacy*, arXiv2206.04572v2](https://arxiv.org/html/2206.04572v2),5October2022. Reader artifact35066 SHA256 `e34f6b702c8b245a8e4e85ffa11598feb7e7a2deb6fb8d81a59c33b3797636d9`,178697bytes,1234 newline characters/1235 logical lines. Actual selected reads were1–300,321–342 and the COMPLETE1152–1227 Theorem4.8 proof through its ending. This is NOT a complete1235-line/publication/PDF-glyph or all-version audit.

The old `source-CND-interface-v1.json` listed all FOUR defining CND requirements and had only heading/interface coverage for Theorem4.8. The actual newly read theorem is STRONGER: in dimension>=2 it excludes properties1 AND2 ALONE—full norm-ball pure privacy together with equality of the ENTIRE pure-DP ROC at ONE admissible shift. It does NOT need the additional monotone-likelihood-ratio or symmetry requirements3/4. Any reading that makes the impossibility depend on those extra two requirements is too narrow. This is an ADDITIVE correction of scope/reading, not an edit or backdating of the old record.

This note supplies a direct all-Borel alternative proof at ordinary facts. It replaces unlicensed uncountable-null-union/high-level-set-boundedness/disjoint-ball/terminal-integer shortcuts rather than endorsing them from the retained reader. The theoretical two-property result is positively PRIOR. No source-publication-wide falsity, original-glyph authentication, public refutation, new mechanism/value/discovery or novelty claim follows.

**Exact new WRITTEN conclusions:**

- For any genuine full closed norm-ball sensitivity in dimension>=2 and finite epsilon>0, no private law has binary likelihood ratio {exp(-epsilon),exp(epsilon)} a.e. for ANY admissible nonzero shift.
- Thus EVERY fixed admissible shift has total variation STRICTLY below the pure-DP extremal value. For EACH fixed law, compactness of the shift ball makes this a uniform positive margin over all shifts.
- Consequently no admissible shift can attain the full pure-DP ROC, even without MLR or symmetry.

These do NOT preclude a finite-epsilon MSE optimizer or exact max-divergence epsilon. The registered LAW642/I233 optimum has those properties at its own imports; the ROC distinction is made precisely in §8.

## 1. Exact model, ordinary imports and testing convention

Let d>=2 be finite, K⊂R^d a compact convex centrally symmetric genuine norm ball with interior, finite epsilon>0 and b=exp(-epsilon)∈(0,1). Let mu be ANY Borel probability law satisfying

    mu(A)<=b^(-1)mu(A+h)
    for EVERY Borel A and EVERY h in FULL CLOSED K.           (DP_K)

No density, first/second moment, radiality, MLR, symmetry of mu or selected optimizer is assumed.

**Named classical facts:** RN; positive Tonelli/Fubini and translation invariance; Lebesgue differentiation; countable unions of null sets; elementary norm/Euclidean projection geometry; total variation in RN form; L1 density of C_c and continuity of translations; compact-interval/compact-set extrema. Every specialized privacy, binary-ratio, packing and ROC step is supplied below. No AD22 research theorem, CND construction or LAW642 is a premise of §§2–7.

To avoid any ambiguity of rendered testing notation, use the explicit operational SPECIFICITY convention

    T(P,Q)(alpha)=1-sup{E_Q phi:
                        0<=phi<=1, E_P phi<=1-alpha},
    alpha∈[0,1].                                          (TEST)

With this convention T(P,P)=identity. Its pure-DP lower envelope is

    f_epsilon(alpha)=max(0,b alpha,
                             1-b^(-1)+b^(-1)alpha).         (PURE_ROC)

This is the standard increasing tradeoff/specificity convention used for the displayed pure-DP envelope. No proof rests on blindly copying an inequality sign from the reader layout. The theorem below is operationally defined by TEST, not a glyph-level certification of every source definition.

## 2. Full privacy gives AC, positivity and ONE full set with ALL pairwise local bounds

Put V=|K|>0. Integrating DP_K over h∈K for a null Borel N gives

    V mu(N)<=b^(-1)integral_K mu(N+h)dh=0

by Tonelli/translation fibers. Thus mu has a Borel density p.

It is positive a.e. If a bounded positive-volume Borel Z had p=0 a.e., privacy iteration along finite K-steps would give mu(Z+h)=0 for EVERY h∈R^d. But positive Tonelli gives

    integral_(R^d)mu(Z+h)dh=|Z|>0,

contradiction. This avoids the false inference that an uncountable union of individually null translated events is null.

Let E be the full-Lebesgue-measure set of Lebesgue differentiation points of p where0<p<infinity. If x,y∈E and y-x∈K, privacy applies to their Euclidean balls of EVERY radius t>0:

    mu(B_t(x))<=b^(-1)mu(B_t(y)).

Divide by their equal positive volume and let t↓0. The two limits exist by the DEFINITION of E, giving

    b p(x)<=p(y)<=b^(-1)p(x)
    for EVERY x,y∈E with||x-y||_K<=1.                     (PAIR)

This is a single full set with an ALL-pairs conclusion obtained from actual BALL-event limits. It is NOT an intersection of uncountably many fixed-shift RN exception sets.

## 3. Binary likelihood at one shift yields an infinite transverse chain

Suppose for contradiction that some v∈K has

    p(x+v)/p(x)∈{b,b^(-1)} for a.e.x.                    (BINARY)

The case v=0 is immediately impossible because b<1; hence v≠0. Choose r>0 so the CLOSED Euclidean ball rB2 is contained in K. Since d>=2 choose a Euclidean unit vector e perpendicular to v, and put

    z=(r/4)e,
    w=z-v/2.

Then `||z||_K<=1/4`, `||v||_K<=1`, and the norm triangle inequality gives

    ||w||_K<=3/4<1,
    ||w+v||_K<=3/4<1.                                   (TWO_STEPS)

Their transverse projection along v-perpendicular is exactly z≠0.

Let G be a full-Lebesgue-measure set where BINARY holds. The lattice

    Gamma={k w+j v:k,j∈Z}

is COUNTABLE. Therefore

    E0=intersection_(gamma∈Gamma)[(E∩G)-gamma]

has full Lebesgue measure. Pick xi∈E0 and set a=p(xi)>0. Every point of xi+Gamma belongs to BOTH E and G. No boundedness or positive-volume thickness of a high-density level set is assumed.

Start at x0=xi. Suppose xk is a lattice point with p(xk)>=a. PAIR and TWO_STEPS imply

    p(xk+w)>=b p(xk),
    p(xk+w+v)>=b p(xk).

The ratio of these TWO values is b or b^(-1), because xk+w∈G. Whichever is the larger is at least p(xk): the smaller is at least b p(xk) and the larger is exactly b^(-1) times the smaller. Choose x_(k+1) as that larger-density point. Then

    xk=xi+k w+j_k v for some integer0<=j_k<=k,
    p(xk)>=a for EVERY k>=0,
    Proj_(v-perp)(xk)=Proj_(v-perp)(xi)+k z.              (CHAIN)

This is an exact mathematical induction, not a program/enumeration or a finite numerical witness. The transverse motion does not depend on the choices of j_k.

## 4. Actual disjoint neighborhoods have fixed positive mass

Let A_k be the open Euclidean ball of radius r/16 around xk. For distinct k,l,

    |xk-xl|2>=|Proj_(v-perp)(xk-xl)|2
              =|k-l|r/4>=r/4>2(r/16).

Thus the balls are ACTUALLY pairwise disjoint. The strict radius/separation inequality is supplied; center distance merely equal to one radius would not suffice.

For a.e.y∈A_k we have y∈E and `||y-xk||_K<=1/16<1`. Since xk∈E, PAIR and CHAIN give

    p(y)>=b p(xk)>=b a.

Consequently EVERY A_k has the SAME positive mass lower bound

    mu(A_k)>=b a |B2(0,r/16)|>0.

Countable additivity over infinitely many disjoint A_k contradicts mu(R^d)=1. No terminal finite integer bound, its reciprocal, unbounded-high-level-set argument or ignored tail is needed.

Therefore BINARY is impossible for EVERY v∈K. This proves the stronger density-ratio core of AD22Theorem4.8 in the ALL-Borel full-closed-ball class, with no MLR, symmetry or moment assumptions.

## 5. Exact total-variation endpoint and the full-ROC implication

Fix any h∈K and let P=mu,Q=tau_h mu. Mutual DP_K domination gives

    L=dP/dQ∈[b,b^(-1)] Q-a.e., E_Q L=1.

Put c=(1-b)/(1+b)>0. On that exact interval the chord inequality is

    |L-1|<=c(L+1),

with STRICT inequality at every interior L∈(b,b^(-1)). Indeed, for L<=1 the difference is `2(L-b)/(1+b)`; for L>=1 it is `2(1-bL)/(1+b)`. Hence

    TV(P,Q)=(1/2)E_Q|L-1|<=c,

and equality holds iff L takes ONLY the two endpoint values Q-a.e. Because p>0 a.e., this endpoint condition is precisely BINARY after a translation/sign change. Sections3–4 exclude it, so

    TV(mu,tau_h mu)<c for EVERY h∈K.                      (STRICT_TV)

At h=0 the strict inequality is automatic since TV=0. For nonzero h it is the new packing consequence.

From the operational definition TEST,

    TV(P,Q)=sup_(alpha∈[0,1])[alpha-T(P,Q)(alpha)].

For each admissible test phi take alpha=1-E_P phi to obtain one direction; conversely any test under the constraint has `E_Q phi-(1-alpha)<=E_Q phi-E_P phi<=TV`. This proves the identity directly, without a ROC-to-PLRV research import.

For PURE_ROC the maximum difference is EXACTLY c, attained at

    alpha*=1/(1+b), f_epsilon(alpha*)=b/(1+b).

The two affine pieces intersect there; their respective difference bounds are `(1-b)alpha` and `(1-b)(1-alpha)/b`, whose minimum is maximized at that intersection. Thus if the full tradeoff equaled f_epsilon for even the relevant central alpha*, its TV would be>=c, contradicting STRICT_TV. In particular full-ROC equality for ALL alpha cannot hold for ANY shift.

This proves the source's properties1+2 impossibility directly under TEST. Extra monotone likelihood ratios or symmetry are not used and must not be presented as necessary for the no-CND conclusion.

## 6. Uniform positive margin over shifts for EACH fixed law

The density p lies in L1. The map h↦tau_h p is L1-continuous: approximate p in L1 by a compactly supported continuous function, use translation invariance of the L1 approximation error and uniform continuity of the approximant on a common compact support neighborhood. Therefore

    h↦TV(mu,tau_h mu)=(1/2)||p-tau_h p||1

is continuous. Since K is compact and EVERY value is strictly below c by STRICT_TV, its maximum is attained and remains strictly below c. Hence for EACH fixed mu there is

    delta_mu=c-max_(h∈K)TV(mu,tau_h mu)>0.                (LAW_MARGIN)

It follows also that at alpha*,

    T(mu,tau_h mu)(alpha*)>=f_epsilon(alpha*)+delta_mu
    for EVERY h∈K.

This is a uniform shift margin for a FIXED law only. No positive constant uniform over all private laws, no evaluated delta, convergence rate or moment-bounded-family theorem is asserted.

## 7. Source-proof replacement and exact retained limitations

The complete1152–1227 reader proof was actually read. This new proof deliberately avoids the following unsupported steps if the retained text is taken as a full all-Borel argument:

- uncountable unions of individually null translates to prove positivity;
- asserting an unbounded high-density set must have infinite mass merely because its density is bounded below;
- calling balls disjoint from a center-separation lower bound smaller than two radii;
- a terminal integer inequality that does not explicitly supply the reciprocal threshold needed for total mass>1.

The replacements are respectively positive Tonelli/finite-step translation; a countable full-set lattice and arbitrary positive starting density; the explicit r/4 versus2(r/16) separation; and an INFINITE disjoint-mass contradiction. No corresponding original-PDF glyph/version authentication or public theorem-falsity finding is claimed. The theoretical source result has a complete alternative WRITTEN proof here; other AD22 theorems/constructions, composition/limit results and all-version details remain outside this reconstruction.

The explicit testing convention TEST also keeps our operational proof independent of possible reader-layout inequality ambiguities. No blanket correctness of every rendered definition or uninspected source version is inferred from the valid reconstructed statement.

## 8. Registered max-divergence/MSE boundary and named additional imports

For registered K=D in dimension2, the general theorem applies to EVERY original feasible additive law, without an optimum assumption. It proves that NONE can saturate the entire pure-DP ROC at an admissible shift, or meet even the central ROC equality, regardless of whether it minimizes MSE.

The separately adopted I233 theorem `privacy-renyi-infinity-full-diamond-bridge-v1.md`,233LF, SHA256 `03ccb06b95b5b3cdbf9b9e120293a6a68c3c8399ff2621c9ee77e1ccdd3df843`, at `RUN/privacy-order-infinity-and-joint-tail-recovery-entire-parent-v1.md`, supplies exact `F_infty(mu_epsilon)=epsilon` for the LAW642 optimizer, at its explicitly named compact-core/value/ALL-law uniqueness imports. This is a NAMED input ONLY for the following specialization, not part of §§2–7's generic impossibility proof.

Thus the registered optimizer can have exact worst-event/tail max-divergence epsilon while STILL having STRICT_TV and LAW_MARGIN, so it is not a CND. Exact max divergence means some event ratios attain or approach exp(epsilon); full-ROC equality requires the ENTIRE testing experiment to be the extremal binary likelihood experiment. They are logically different claims.

No contradiction with original attainment/uniqueness or source nonexistence arises. Conversely the no-CND theorem says NOTHING about the numerical value of the registered MSE infimum, its finite-epsilon core geometry or uniqueness. It must not be advertised as an absence theorem for optimizers, a substitute original lower bound, or a worldwide novelty/priority separator.

Positive PRIOR f-DP/ROC/CND and multivariate-impossibility contributions remain credited. Original priority remains UNCLEAR. A fresh COMPLETE source/mathematics/dependency/application gate is REQUIRED for this entire new body and for the specialization's explicit I233/LAW642 import union. The old four-requirement source summary is not silently rewritten or retrospectively broadened into a full proof read.

## 9. Chronology, execution and unchanged round

The stronger two-property statement and complete lattice/packing/ROC proof lead were saved BEFORE this body in checkpoint098. All arithmetic/proofs are exact WRITTEN; no scientific execution or machine check. All firstfive owner findings, SIXTH DISTINCT v111B written-exactness finding, SEPARATE077 continuation failure, v21 category correction, auxiliary214 UNADMITTED/strictSTOP and every parent/reviewer/source/import/N4UNKNOWN/exit/old-arithmetic qualification remain. No clean cognition/runtime/history or continuous-work census, stronger human/family/cross-vendor/formal/kernel/executable/novelty/publication assurance or new GO.

Exclusive own root only; frozen sources/ACKs/parents/other-owner bytes unchanged. No auxiliary graph derivation, new model/slot/owner, publication or deadline reset. Same eighteen owners; science cutoff **2026-10-27T11:05:38-07:00**, delivery **2026-10-27T12:35:38-07:00**; active actual substantive checkpoints at most30minutes. This is not early final-park or round closeout; the authorized registered source/proof/priority residual continues.
