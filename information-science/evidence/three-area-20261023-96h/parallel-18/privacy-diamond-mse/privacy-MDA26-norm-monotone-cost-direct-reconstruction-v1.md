# MDA26 theoretical source edge: direct staircase comparison for EVERY norm-monotone cost

Owner **InfoResearch96h-2**, original info-1. Actual `/bin/date` BEFORE this write: **Mon Oct 26 06:49:10 PDT 2026**. **NEW AUTHOR-WRITTEN SOURCE-PROOF CANDIDATE**, not independently reviewed or parent-adopted. No mathematical machine check, scientific interpreter/eval/calculator/CAS/program/enumeration/replay/solver/CLI/nested agent or new GO. Every calculation is exact WRITTEN symbolic analysis.

## 0. Actual source statement, precise new representation and non-transfer

Primary source: Melbourne–Diaz–Asoodeh, [*Optimality of Staircase Mechanisms for Vector Queries under Differential Privacy*, arXiv2601.14597v1](https://arxiv.org/html/2601.14597v1). The retained source reader `RUN/privacy-source-snapshot-MDA26-v1.txt`, SHA256 `d2c986cb8d53a000259a3b4587833002d703481ab5c72481ad1d4bc7f122dccb`, has1999 rendered logical LF; it is NOT original PDF-byte identity. Current selected reads:188–238,289–301,495–583 and1395–1585, including actual Assumption1, full Theorem6 statement/proof and the AppendixD maximal-decay/overshoot argument. Prior full reading remains historical; no fresh complete1999LF or all-version audit is claimed.

Actual Assumption1 is `Phi(z)=phi(||z||)` for ANY nondecreasing `phi:[0,infinity)->[0,infinity]`. Theorem6 states that a norm-based staircase law attains the original additive infimum for every finite dimension, positive epsilon and positive sensitivity scale. This is positively PRIOR. Its main conclusion is broader than K25's mean-norm loss, and cannot be verified merely by reconstructing K25's mean-norm argument.

**New exact representation:** after actual privacy-preserving K-ball rearrangement and amplitude slicing, a geometric phase has ordered radii R_i with gaps>=1. For its actual phi-cost v, the signed ball functional

    H_v(R)=integral_(0 to R)(phi(r)-v)d(|K|r^d)

is nonincreasing below a cost-crossing radius and nondecreasing above. A SINGLE parallel sequence t+i can be chosen so that EVERY radius moves toward that crossing. Hence EVERY weighted signed term decreases. This is a GLOBAL comparison for arbitrary finite-cost phases, not an optimal-phase first variation, a floor-periodic “overshoot” assumption or a hidden unbounded-cost continuity assertion.

The full proof below reconstructs Theorem6's THEORETICAL conclusion without using the source's maximal-decay Lemma7, universal stochastic-dominator assertion, extreme-point theorem or Krein–Milman step. It is not a certification that those printed proofs, every version, sampling routine or experiment are correct as written.

**Non-transfer:** the sensitivity norm and the radial loss norm are the SAME throughout. Registered info-1 uses diamond sensitivity but squared-Euclidean loss, which is not phi(||z||1) for a single radial phi. No registered radiality, explicit value, optimizer classification or LAW642 reconstruction follows from this note. No new mechanism/method/priority/novelty or model/slot cutover is claimed.

## 1. Exact theorem and named ordinary inputs

Fix a compact convex centrally symmetric norm ball K⊂R^d with nonempty interior, finite integer d>=1, finite epsilon>0 and b=exp(-epsilon)∈(0,1). Let r(z)=||z||_K and let phi:[0,infinity)→[0,infinity] be nondecreasing. Let P_K be ALL Borel probability laws satisfying

    mu(A)<=b^(-1)mu(A+h)
    for EVERY Borel A and EVERY h in the FULL CLOSED K.       (DP_K)

For0<=t<=1 let Q_t be the normalized law with a.e. density

    u_t(z)=b^max(0,ceil(r(z)-t)).                             (STAIR)

Boundary spheres are null; a chosen consistent open/closed-level representative does not change the law. Both mass and feasibility are proved below. Define `J_phi(mu)=integral phi(r(z))mu(dz)`.

**Theorem — WRITTEN at the named classical imports below.**

1. For EVERY mu∈P_K with finite J_phi, there is a parameter t∈[0,1] such that `J_phi(Q_t)<=J_phi(mu)`.
2. The original all-law infimum equals `min_(0<=t<=1)J_phi(Q_t)`, with the extended all-infinite case treated literally. If any feasible law has finite cost, the scalar cost is finite and continuous on[0,1], so an actual finite optimum is attained.

A sensitivity ball Delta times a chosen unit ball is covered by taking K equal to that scaled ball and replacing phi(s) by the nondecreasing function phi(Delta s). This retains the full CLOSED sensitivity ball and actual objective scale, not a lattice or selected-query shift set.

**Only ordinary classical imports:** RN; Lebesgue density points and measure regularity; Tonelli/Fubini; Brunn–Minkowski for compact/open measurable sets; zero volume of convex-body boundaries; elementary norm/Minkowski geometry; nonnegative layer cake; compact-interval minimization and uniform convergence of dominated series. All model-specific privacy, mixture, comparison, integrability and continuity steps are supplied in this body. No LAW642 or other research theorem, reviewed/unreviewed K25 proof, MDA Lemma7, scalar transfer or executable arithmetic is a premise.

## 2. All-law density/cap and actual privacy-preserving radial rearrangement

Put V=|K|>0. For any null Borel N, DP_K and Tonelli over h∈K give

    V mu(N)<=b^(-1)integral_K mu(N+h)dh=0.

Thus every feasible law has a Borel density p. For EACH fixed h∈K, event order gives `p(z+h)>=b p(z)` a.e.z. Fubini over the jointly measurable translated density gives

    b V p(z)<=integral_K p(z+h)dh<=1 a.e.z.

Hence `0<M=esssup p<=1/(bV)<infinity`. No common uncountable-h pointwise RN exception set was chosen.

Also p>0 a.e. If a bounded positive-volume set Z had p=0, iteration of privacy along finite K-steps would give mu(Z+h)=0 for EVERY h∈R^d. Tonelli over all translations instead gives `integral mu(Z+h)dh=|Z|>0`, contradiction.

For s>0 set A_s={p>s}, `R(s)=(|A_s|/V)^(1/d)`. These sets have finite volume; R is nonincreasing and right-continuous. Whenever |A_s|>0 we have

    R(bs)>=R(s)+1.                                        (GROW)

Here is the full essential-enlargement argument. Fixed-h privacy gives A_s+h⊂A_bs a.e. Define `F_s(z)=integral_(intK)1_(A_s)(z-h)dh`. Fubini gives `F_s(z)<=V 1_(A_bs)(z)` a.e.z. If C is a positive-volume compact subset of density points of A_s, then C+intK⊂{F_s>0}: a small neighborhood of each such density point has positive intersection with A_s. Therefore Brunn–Minkowski gives

    |A_bs|^(1/d)>=|C+intK|^(1/d)>=|C|^(1/d)+V^(1/d).

Compact C can approach |A_s| by regularity and the density-point theorem, proving GROW. This is not an unjustified union of uncountably many translated null sets.

Define

    psharp(z)=sup{s>0:r(z)<R(s)},  sup(empty)=0.

Right-continuity gives the exact strict-level identity `{psharp>s}={r<R(s)}`. Layer cake shows integralpsharp=integralp=1. For ANY z and h∈CLOSED K, if0<s<psharp(z), then

    r(z+h)<=r(z)+1<R(s)+1<=R(bs).

Hence psharp(z+h)>bs. Let s increase to psharp(z) to obtain `psharp(z+h)>=b psharp(z)` for EVERY z,h. Thus psharp is a genuine full-K private radial nonincreasing density, not merely a formal equimeasurable comparison. Iteration of GROW from any0<s<M also proves psharp(z)>0 for every finite z.

For a set A of volume V R^d, the centered ball B=RK minimizes integral_A phi(r) among all equal-volume sets. Indeed A\B has r>=R and B\A has r<=R with equal volume, so monotonicity bounds their cost difference below by phi(R) times the mass difference0. One may use finite truncations of phi first, then monotone convergence for extended values. Applying this to every A_s and integrating in s gives

    J_phi(psharp)<=J_phi(p).                               (RAD_COST)

No STRICT equality case is assumed for a loss with plateaus. In particular this proof does NOT claim that EVERY original optimizer is radial when phi is not strictly increasing.

## 3. Exact amplitude phases with the actual phi-cost, not a mean-norm prerequisite

Let M=esssup psharp. For a∈[bM,M), define

    n_a(z)=min{i>=0 integer:psharp(z)>a b^i},
    u_a(z)=b^n_a(z), Z_a=integral u_a, q_a=u_a/Z_a.

Positivity makes the index finite a.e. Minimality gives

    b psharp(z)/a<=u_a(z)<=psharp(z)/a,
    b/a<=Z_a<=1/a.

The k=0 case uses a>=bM. For every FIXED h∈K the index changes by at most1 a.e., in fact psharp's chosen representative is pointwise private. Thus q_a is fully DP_K after normalization. The phase maps are jointly measurable in(a,z).

The geometric layer and amplitude substitution give

    u_a(z)=(1-b)sum_(i>=0)b^i 1_(psharp(z)>a b^i),
    psharp(z)=integral_(bM)^M u_a(z)da/(1-b).

Tonelli gives the probability-mixture identity with weights Z_a da/(1-b), total1, and

    J_phi(psharp)=integral_(bM)^M J_phi(q_a)Z_a da/(1-b).

When the left side is finite, SOME phase has finite cost v=J_phi(q_a)<=J_phi(psharp). There is no original optimum assumption and no finite FIRST-norm-moment assumption: this statement uses the ACTUAL nonnegative phi-cost only. Choosing a phase depending on phi is allowed for Theorem1's per-cost comparison.

Its closed essential levels are balls R_iK because psharp is radial nonincreasing. Every R_i is finite, since the positive threshold bounds its level volume. The top radius R_0>0 because a<M. Fixed-h privacy followed by essential supports gives

    R_iK+K=(R_i+1)K⊂R_(i+1)K,
    R_(i+1)>=R_i+1.                                      (GAP)

Consequently R_i>=R_0+i→infinity. Conversely ANY such finite radii define a fully private geometric law by the closed-level index `min{i:z∈R_iK}`. Unit K-shifts increase that index by at most1. Its mass/cost are the exact ball-layer sums below; boundaries are null and do not affect the law.

## 4. Global parallelization by a signed single-crossing ball functional

Define for finite R>=0

    A(R)=integral_(0 to R)phi(s)d(V s^d),
    B(R)=V R^d.

The geometric phase has

    Z=(1-b)sum_i b^i B(R_i),
    N=(1-b)sum_i b^i A(R_i), v=N/Z<infinity.              (BALL_SUM)

These are the ACTUAL volume weights, not equal-volume scalar bins. Since every phase density is positive at every positive radius, finite v implies phi is finite at every finite positive radius: an infinite value at some radius would, by monotonicity, force infinite cost on its entire positive-volume tail. Hence A is finite and continuous on bounded intervals.

If phi is constant a.e. on(0,infinity), every AC law has that same cost; the finite case is immediate by choosing any staircase. Its value at0 or a sphere does not matter. Assume henceforth that phi is not a.e. constant.

A positive-density finite expectation v of a nonconstant nondecreasing phi lies STRICTLY between its essential infimum and essential supremum. Otherwise the nonnegative difference from the relevant extremum has positive integral. Thus there are0<r_lo<r_hi<infinity with

    phi(r_lo)<v<phi(r_hi).

Choose a finite crossing r0∈(0,infinity) so that phi<=v below r0 and phi>=v above r0, apart from the immaterial value at r0. For example use the infimum of radii where phi>v. Define

    H_v(R)=A(R)-v B(R).

By the signed integral definition, H_v is nonincreasing on[0,r0] and nondecreasing on[r0,infinity], even if phi has jumps or intervals equal to v. No derivative or strict loss assumption is required.

Write s_i=R_i-i, a nondecreasing sequence by GAP. We choose ONE t>0 such that every `R'_i=t+i` lies between R_i and r0.

- If R_0>r0, choose t=r0. Then `r0<=t+i<=R_i` for every i.
- Otherwise, let j be the largest index with R_j<=r0; it exists and is finite because R_i→infinity. Then R_j<=r0<R_(j+1), and the TWO intervals

      [s_j,s_(j+1)] and [r0-j-1,r0-j]

  intersect: s_j<=r0-j and s_(j+1)>r0-j-1. Choose t in their intersection. It is positive because t>=s_j>=R_0>0. For i<=j,

      R_i<=t+i<=r0;

  for i>=j+1,

      r0<=t+i<=R_i.

In all cases monotonicity of H_v toward its minimum gives the TERMWISE signed inequality

    H_v(t+i)<=H_v(R_i) for EVERY i.                       (SIGNED)

The new radii t+i have exact unit gaps and define a fully private geometric density u_t. Its mass and phi-moment are finite: beyond the finite index j, its radii do not exceed R_i, so both B and A are bounded termwise by the old sums; finitely many changed head terms are finite. In the R_0>r0 case the bound holds at EVERY term. Its mass is strictly positive.

The old signed series and the new one are absolutely convergent because their nonnegative mass/cost sums are finite. Multiply SIGNED by(1-b)b^i and sum to obtain

    N(t)-v Z(t)<=N-vZ=0.

After ACTUAL positive normalization,

    J_phi(Q_t)<=v.                                      (PAR_COMPARE)

This is a complete GLOBAL comparison for the entire phase, not an infinitesimal necessary condition at a presumed optimizer. No ignored infinite-tail derivative or unproved overshoot is involved.

## 5. Exact reduction of the top plateau to0<t<=1

If t>1 the unnormalized staircase obeys the exact a.e. identity

    u_(t-1)=b u_t+(1-b)1_((t-1)K).                       (INNER)

After normalization, Q_(t-1) is a positive convex mixture of Q_t and the uniform law on(t-1)K. BALL_SUM also expresses Q_t as a positive volume-weighted mixture of uniform laws on(t+i)K.

For any0<R1<=R2, couple the two uniforms as R1U and R2U with U uniform on K. Monotonicity of phi gives `E phi(R1 r(U))<=E phi(R2 r(U))`. Therefore the uniform(t-1)K cost is no larger than EVERY uniform(t+i)K cost, hence no larger than J_phi(Q_t). INNER gives

    J_phi(Q_(t-1))<=J_phi(Q_t).

Iterate finitely until0<t<=1. Feasibility and finite moment persist at every step. Strictness is NOT claimed for plateau losses. Combining this with RAD_COST, phase selection and PAR_COMPARE proves Theorem1: for EVERY original finite-cost law there is a legal staircase with no larger cost.

At t=0, `u_0=b u_1` a.e., so Q_0=Q_1 as laws. The zero-radius top level contributes no volume; normalization is still strictly positive from the next layer. There is no artificial zero-mass law or new atom.

## 6. Finite cost, scalar continuity and attained optimum without unproved weak-cost continuity

The preceding argument supplies at least one finite-cost staircase Q_(t0),0<t0<=1, whenever any original feasible law has finite cost. Its actual normalizer and numerator on[0,1] are

    Z(t)=(1-b)sum_(i>=0)b^i V(t+i)^d,
    N_phi(t)=(1-b)sum_(i>=0)b^i A(t+i),
    C_phi(t)=N_phi(t)/Z(t).                              (SCALAR)

Z is finite continuous and STRICTLY positive on[0,1]; even at0 its i=1 term is positive. This follows from the ordinary geometric-polynomial series.

For all0<=t<=1,

    0<=A(t+i)<=A(i+1)<=A(t0+i+1).

The bound sums finitely because

    sum_(i>=0)b^i A(t0+i+1)
       =b^(-1)sum_(j>=1)b^j A(t0+j)<infinity,

using the actual finite numerator at t0. Thus the numerator series converges UNIFORMLY on[0,1] by a summable bound. Each A(t+i) is continuous, so N_phi is finite continuous, and the positive denominator makes C_phi finite continuous. Compactness of[0,1] therefore gives an actual minimizer t*.

Theorem1 gives `min_t C_phi(t)<=J_phi(mu)` for EVERY original finite-cost law, while staircase laws are themselves original feasible laws. Hence

    inf_(mu∈P_K)J_phi(mu)=min_(0<=t<=1)C_phi(t).

If NO original feasible law has finite cost, every staircase also has infinite cost because it is feasible. Both sides then equal infinity and any staircase attains the extended infimum; no finite optimum/value is invented. This covers arbitrary nonnegative nondecreasing extended costs, including indicators, truncations and fast growth.

The continuity proof is over the ACTUAL scalar staircase parameter, with an explicit summable envelope from one finite-cost staircase. It is NOT a blanket assertion that an arbitrary unbounded loss integral is weakly continuous on an unspecified compact convex class.

## 7. Exact mathematical scope of the source reconstruction

The theoretical optimality/attainment conclusion of MDA26Theorem6, at its explicit full-norm-ball class and Assumption1, is now supplied in this standalone WRITTEN candidate at ordinary classical facts. The proof is independent of K25's mean-norm loss and does not assume an original optimizer exists before the comparison.

**Not reconstructed by this argument:** a SINGLE stochastic dominator Y that works simultaneously for EVERY nondecreasing cost for each input law. Our selected phase, crossing and t may depend on phi. Thus the new proof does NOT silently certify the stronger universal statement of the source's Lemma1, its specific floor-periodic modification/overshoot Lemma7, its entire extreme-point characterization or all printed versions. It supplies a complete alternative route to the main theoretical per-cost conclusion, not an edit of those frozen source bytes.

It also does not classify ALL original optimizers for costs with flat regions. The nonstrict radial bathtub need not force equality of sets; the proof selects an attaining staircase without asserting every optimum is radial/staircase. K25mean-norm strict equality and the registered LAW642 uniqueness have their OWN scopes, not a shared implication for every phi.

The source's algorithm, finite grid search, sampler, experiment, numerical parameter curves, implementation and particular-query necessity of a full sensitivity ball are outside this reconstruction. We prove the stated full-ball noise-law class, not that every specific query with a nonconvex actual sensitivity set must satisfy every full-ball shift constraint.

**Registered mismatch:** for diamond sensitivity, squared-Euclidean loss is not constant on l1-norm spheres, so Assumption1 fails. An explicit universal proof of the matched-norm source conclusion does not derive the registered mixed-norm value/geometry/ALL-law equality. Its positive PRIOR mechanism/rearrangement/saturation ancestry remains fully credited; novelty/priority of the registered result stay UNCLEAR.

A fresh COMPLETE mathematics AND source/dependency/application gate over THIS new body is required before parent promotion. No earlier MDA source comparison or K25 proof review adopts it by resemblance. The source's version/printed-proof qualifications remain unchanged until separately addressed, and no publication-wide correctness/falsity or public refutation follows.

## 8. Chronology, execution and unchanged round

The new signed-radius parallelization lead was saved BEFORE this full body in checkpoint093. All reasoning occurred under the already authorized registered source/priority continuation, not a live-review interleaving or new auxiliary family. No frozen source/packet/ACK/parent or other owner's file was edited.

All proof work is exact WRITTEN; no mathematical machine checks or scientific execution. All firstfive owner findings, SIXTH DISTINCT v111B written-exactness finding, SEPARATE077 continuation failure, v21 category correction, strict auxiliary214STOP/UNADMITTED and all parent/reviewer/source/import/N4UNKNOWN/exit/old-arithmetic qualifications remain. No clean cognition/runtime/history or continuous-work census, stronger human/family/cross-vendor/formal/kernel/executable/novelty/publication assurance or new GO.

Same eighteen owners; science cutoff **2026-10-27T11:05:38-07:00**, delivery **2026-10-27T12:35:38-07:00**; active substantive actual-clock checkpoints at most30minutes. This is not early final-park or round closeout; the registered source/proof/priority residual continues.
