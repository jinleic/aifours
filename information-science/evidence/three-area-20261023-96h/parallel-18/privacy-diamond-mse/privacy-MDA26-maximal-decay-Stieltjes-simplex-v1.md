# MDA26 maximal-decay class: explicit Stieltjes mixture, compact simplex, extreme points and finite-cost weak continuity

Owner **InfoResearch96h-2**, original info-1. Actual `/bin/date` BEFORE this write: **Mon Oct 26 07:24:14 PDT 2026**. **NEW AUTHOR-WRITTEN SOURCE-STRUCTURE CANDIDATE**, not reviewed or parent-adopted. Exact WRITTEN measure/geometry/algebra only; no scientific interpreter/eval/calculator/CAS/program/enumeration/replay/solver/CLI/nested agent, no machine check or new GO.

## 0. Exact delta and source attribution

Primary source: Melbourne–Diaz–Asoodeh, [*Optimality of Staircase Mechanisms for Vector Queries under Differential Privacy*, arXiv2601.14597v1](https://arxiv.org/html/2601.14597v1). Retained source reader `RUN/privacy-source-snapshot-MDA26-v1.txt`, SHA256 `d2c986cb8d53a000259a3b4587833002d703481ab5c72481ad1d4bc7f122dccb`,1999 rendered logical lines, NOT original PDF-byte identity. Current additional selected reads1586–1678 and1810–1845 include its Lemma8 comparison/Corollary1, full structural theorem statements and part of its extreme-point proof, not that entire printed proof or a fresh whole-publication/version audit.

The source's Theorem5/Theorems9–10 assert compact convex maximal-decay class with staircase extreme points. Its Corollary1 asserts weak continuity of the norm-cost functional if one class member has finite cost. Those are positively PRIOR statements, not discoveries of this lane.

The earlier237LF PER-COST proof and219LF universal weighted-decay proof explicitly left the extreme-point/compactness source edge separate. This NEW body supplies a direct alternative: an EXACT, UNIQUE Stieltjes barycentric representation in normalized staircase laws. It proves compactness/extremality and the actual unbounded-cost continuity without assuming Krein–Milman or the source's printed perturbation/weak-closure arguments.

**New WRITTEN scope:** the ACTUAL norm-radial, nonincreasing, lower-semicontinuous, maximally decaying class D. No LAW642, original all-law optimizer, registered Euclidean-MSE/diamond geometry, universal reduction theorem, new science/novelty or source-publication-wide certificate is a premise or conclusion. Original all-law reduction needs its separate proof/gate; it is NOT automatically accepted by this class-structure theorem.

## 1. Exact class and ordinary imports

Fix finite dimension d>=1, a genuine compact convex centrally symmetric norm unit ball K with interior, V=|K|>0, finite epsilon>0 and b=exp(-epsilon)∈(0,1). Write r(z)=||z||_K.

Let D be the set of probability LAWS with a radial density `p(z)=rho(r(z))`, where rho is nonincreasing, right-continuous on[0,infinity), and

    rho(s+1)=b rho(s) for EVERY s>=0,
    d V integral_0^infinity s^(d-1)rho(s)ds=1.              (MAX_CLASS)

The source uses a lower-semicontinuous nonincreasing radial profile; this is exactly the right-continuous convention. Finite positivity is automatic: rho(0)=0 would make the whole profile0; an infinite rho(0) would force rho(1)=infinity and infinite mass on[0,1]. Thus0<rho(0)<infinity, and `b rho(0)<=rho(s)<=rho(0)` on[0,1], making the profile positive everywhere by maximal decay. No moment/cost bound is assumed in defining D.

Every such law is actually private for EVERY h∈the FULL CLOSED K: if0<=s<=t<=s+1, monotonicity and maximal decay give `rho(s)>=rho(t)>=b rho(s)`. The norm triangle inequality yields `|r(z+h)-r(z)|<=1`, hence both density ratios and all-Borel event privacy. This is not merely a discrete radial recurrence.

**Ordinary classical imports:** finite Lebesgue–Stieltjes measures of monotone right-continuous functions; positive Tonelli; norm-ball volume/zero-boundary measure; dominated convergence; weak compactness of probability measures on a compact metric space; the elementary compact-to-Hausdorff continuous-bijection homeomorphism theorem. These are named standard facts, not formal libraries. All model-specific measures, normalization, uniqueness, topology and cost bounds are proved below.

Arbitrary positive sensitivity scale Delta is covered by replacing K with the scaled sensitivity ball and using dimensionless radius r=||z||/Delta. The profile's physical maximal-decay step is then Delta; no closed sensitivity boundary is removed.

## 2. Correct right-continuous staircase parameter and endpoint identity

For0<=t<=1 define

    psi_t(s)=b^(floor(s-t)+1), s>=0,
    Z(t)=integral_(R^d)psi_t(r(z))dz,
    q_t(z)=psi_t(r(z))/Z(t), Q_t=its probability law.        (STAIR_RC)

For0<t<=1 the profile equals1 on0<=s<t and b on t<=s<1, then repeats with exact factor b every unit interval. This is the RIGHT-CONTINUOUS version at every jump, so `psi_t(s+1)=b psi_t(s)` including s=0. It defines the same staircase LAWS as alternative null-boundary conventions, not an arbitrary inconsistent pointwise version.

Positive level slicing gives the actual normalizer

    Z(t)=(1-b)V sum_(i>=0)b^i(t+i)^d.                      (NORM)

The zero-radius level at t=0 is empty; its next layer still gives positive mass. This series is finite continuous on[0,1], with a strictly positive minimum Z_min, by uniform convergence of geometric-polynomial sums. Moreover

    psi_0=b psi_1 pointwise,
    Z(0)=b Z(1), Q_0=Q_1 as LAWS.                         (ENDPOINT)

There is no second distinct endpoint law. For different t in(0,1] the normalized radial laws are distinct: their interior first-period jump positions differ, with a nonzero density change because b<1.

## 3. EXPLICIT Stieltjes representation of EVERY class member

Take any rho in MAX_CLASS. Put M=rho(0)>0 and L=rho(1-). Monotonicity and exact decay give

    L>=rho(1)=bM.

Define the positive finite Stieltjes measure m on(0,1) by

    m((a,c])=rho(a)-rho(c), 0<=a<c<1.

Its total is `m((0,1))=M-L`; it places the actual downward jump of rho at its threshold. Define a new positive measure nu on(0,1] by

    nu restricted to(0,1)=m/(1-b),
    nu({1})=(L-bM)/(1-b)>=0.                              (NU)

Its total is EXACTLY

    nu((0,1])=(M-L+L-bM)/(1-b)=M.

For0<=s<1,

    nu((s,1])=(rho(s)-bM)/(1-b).

Since psi_t(s)=b+(1-b)1_(s<t) in that interval,

    integral_(0,1]psi_t(s)nu(dt)
        =bM+(1-b)nu((s,1])=rho(s).                       (PROFILE)

At s=1 every psi_t(1)=b, giving bM=rho(1). Exact unit decay of BOTH sides extends PROFILE to EVERY s>=0. This is a full pointwise right-continuous representation, not a step-function approximation or an unproved convex-hull closure.

Positive Tonelli and normalization give

    1=integral_(0,1]Z(t)nu(dt).

Therefore

    eta(dt)=Z(t)nu(dt)                                    (ETA)

is an ACTUAL probability measure on(0,1], and the original law is the normalized-staircase mixture

    P=integral_(0,1]Q_t eta(dt).                         (BARY)

All measures/weights are explicit and positive. They are not guessed from extreme-point names.

## 4. Uniqueness is at the LAW level, with endpoint identification

Two right-continuous radial profiles of one law must agree EVERYWHERE: a disagreement at one radius would, by right continuity of both, persist on a right interval. That interval has positive radial volume even if its left endpoint is0, contradicting equality a.e. of the densities. Thus the LAW determines rho, hence M,L and the Stieltjes measure m.

Formula NU determines nu uniquely, and ETA determines eta uniquely on the CANONICAL parameter space(0,1]. Conversely, given the mixture's probability measure eta, the unnormalized measure is exactly `nu(dt)=eta(dt)/Z(t)`. The Stieltjes representation therefore makes BARY UNIQUE once the duplicate endpoint0 is represented by1.

For compact topology use

    T=[0,1] with0 and1 IDENTIFIED,

a compact metric circle. A point of T other than the identified endpoint has its unique representative in(0,1); the endpoint has representative1. This identification is Borel, so the uniqueness just proved is exactly uniqueness of a Borel probability measure on T. No usual-topology compactness of the half-open interval(0,1] is asserted.

## 5. Actual compact convex class and an affine homeomorphism

First, t↦Q_t is weakly continuous on[0,1]. If t_n→t, then for every radius s except the countable set t+Z, `floor(s-t_n)=floor(s-t)` eventually. Thus the unnormalized densities converge a.e.z; the corresponding norm spheres are null. For all t∈[0,1],

    psi_t(s)<=b^(s-1),
    q_t(z)<=b^(r(z)-1)/Z_min.

This is an integrable radial exponential envelope. Dominated convergence proves weak continuity, and ENDPOINT makes the map well-defined and continuous on T.

For ANY probability measure eta on T, the mixture kernel is Borel measurable from the jointly measurable density in(t,z). The density

    rho_eta(s)=integral_T psi_t(s)/Z(t) eta(dt)

is finite positive, nonincreasing, right-continuous by dominated convergence on bounded radius intervals, has exact maximal decay at EVERY s, and integrates to1 by Tonelli. Hence it belongs to D. This verifies the converse inclusion, not merely representation of already known class members.

Define A:Prob(T)→D by eta↦P_eta. It is affine and surjective by §3 and injective by §4. For every bounded continuous f on R^d,

    integral f dP_eta=integral_T [integral f dQ_t]eta(dt),

and the bracket is bounded continuous in t. Thus A is continuous for weak topologies. Prob(T) is compact; the probability-law weak topology on R^d is Hausdorff. Therefore A is an AFFINE HOMEOMORPHISM and its image D is compact and convex.

This supplies the source's actual weak compactness/class closure. It does not infer compactness from a merely closed noncompact probability class, assume convergence of unbounded moments or silently import Krein–Milman.

## 6. Extreme points are EXACTLY the staircase laws

If eta is not a point mass on compact metric T, there is a Borel set B with0<eta(B)<1. Its two conditional probability measures on B and its complement are distinct and give a nontrivial convex decomposition of eta. The affine INJECTIVE map A turns this into a nontrivial decomposition of P_eta into TWO DISTINCT class laws. Hence P_eta is not extreme.

If eta=delta_t and `Q_t=lambda P1+(1-lambda)P2` with0<lambda<1 and P1,P2∈D, apply the affine inverse A^(-1). Then

    delta_t=lambda eta1+(1-lambda)eta2.

Nonnegativity forces both eta1,eta2 to put all mass at t, so P1=P2=Q_t. Thus Q_t is extreme.

Consequently

    Ext(D)={Q_t:t∈T},                                   (EXT)

with endpoints0/1 counted once. In first-period profile language, an extreme law has exactly TWO values on[0,1]: a positive height and b times that height, with a single right-continuous threshold in(0,1]. Conversely a nonincreasing right-continuous profile with only those two values and rho(1)=b rho(0) has precisely that threshold and is one Q_t. This is the source's exact structural characterization, including its terminal endpoint convention.

## 7. Finite cost at ONE member gives genuine weak cost continuity ON D

Let Phi(z)=phi(r(z)) with nonnegative nondecreasing phi, as in the source's actual Assumption1. Suppose some P_ref∈D has finite cost `F(P_ref)=integral Phi dP_ref` and radial profile rho_ref.

For s=k+u with integer k>=0,0<=u<1,

    rho_ref(s)=b^k rho_ref(u)>=b^(k+1)rho_ref(0),
    psi_t(s)<=b^k for EVERY0<=t<=1.

Hence the ACTUAL normalized staircase densities satisfy the UNIFORM bound

    q_t(z)<=C p_ref(z),
    C=1/(b rho_ref(0)Z_min)<infinity.                    (COST_DOM)

This is domination by ONE FIXED finite-cost law, not by a generic exponential whose phi-moment might be infinite.

The a.e. density continuity in §5 and COST_DOM allow dominated convergence after multiplication by Phi. Therefore

    C_phi(t)=F(Q_t)

is finite continuous on[0,1], equal at its two endpoints, hence continuous on compact T. Its finite maximum also shows F(P_eta)<infinity for EVERY eta by BARY/Tonelli.

For ANY sequence P_n→P weakly INSIDE D, the actual homeomorphism gives eta_n→eta weakly on T. Since C_phi is bounded continuous there,

    F(P_n)=integral_T C_phi(t)eta_n(dt)
         ->integral_T C_phi(t)eta(dt)=F(P).               (COST_CONT)

This reconstructs the source's precise finite-cost continuity Corollary1. It is NOT a claim that arbitrary unbounded measurable losses are weakly continuous on all probability laws, or that weak convergence generally implies moment convergence.

If no member has finite cost, F is identically infinity on D and no finite value is invented. In the finite case the explicit mixture also gives

    min_(P∈D)F(P)=min_(t∈T)C_phi(t),

with attainment because T is compact. This is a result ABOUT D. Applying it to unrestricted original laws needs the separately supplied universal-reduction theorem; this packet does not silently adopt another candidate or widen its class.

## 8. Exact source disposition and non-claims

At the named ordinary facts, this new body supplies the source's compactness/convexity/extreme-point/cost-continuity conclusions by an explicit positive UNIQUE Stieltjes mixture. It avoids certifying the printed finite-band perturbation or weak-closure proof merely because the conclusion is familiar. No source bytes, earlier219/237LF successor or parent records are edited or backdated.

The source's theoretical norm-matched claim remains POSITIVE PRIOR, not a new mechanism/method/discovery count. The complete source's other versions, regulated-density wording, samplers/grid searches/plots/experiments, original per-query sensitivity necessity and publication/PDF-glyph identity remain separate. No source-publication-wide correctness/falsity or public refutation is asserted.

The registered diamond sensitivity/squared-Euclidean MSE objective is NOT a function phi(||z||1), so this compact simplex structure does not replace LAW642's mixed geometry/value/ALL-law uniqueness. It also does not classify ALL optimizers among arbitrary original laws for plateau losses. No worldwide equivalence/non-equivalence, firstness, novelty or publication significance is inferred; priority remains UNCLEAR.

A fresh COMPLETE source/mathematics/dependency/application gate is REQUIRED for THIS entire new proof. The219LF universal reduction and237LF per-cost theorem have their own separate gates; their composition with this class theorem must be explicit rather than silently accepted from branch headlines.

## 9. Chronology, execution and unchanged round

The complete Stieltjes/endpoint/compactness/extremality/cost-continuity lead was saved BEFORE this body in checkpoint097. Every identity above is exact WRITTEN; no scientific execution or kernel check. All firstfive owner findings, SIXTH DISTINCT v111B written-exactness finding, SEPARATE077 continuation failure, v21 category correction, auxiliary214 UNADMITTED/strictSTOP and every parent/reviewer/source/import/N4UNKNOWN/exit/old-arithmetic qualification remain. No clean cognition/runtime/history or continuous-work census, stronger human/family/cross-vendor/formal/kernel/executable/novelty/publication assurance or new GO.

Exclusive own root only; frozen/source/ACK/parent/other-owner bytes unchanged. No auxiliary graph derivation, new model/slot/owner, publication or deadline reset. Same eighteen owners; science cutoff **2026-10-27T11:05:38-07:00**, delivery **2026-10-27T12:35:38-07:00**; active actual substantive checkpoints at most30minutes. This is not early final-park or round closeout; the authorized registered source/proof/priority residual continues.
