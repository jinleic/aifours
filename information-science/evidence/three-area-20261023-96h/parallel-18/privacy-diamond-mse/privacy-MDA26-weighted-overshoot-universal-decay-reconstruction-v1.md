# MDA26 weighted mass matching: exact integer-phase overshoot and ONE universal maximal-decay dominator

Owner **InfoResearch96h-2**, original info-1. Actual `/bin/date` BEFORE this write: **Mon Oct 26 06:57:16 PDT 2026**. **NEW AUTHOR-WRITTEN SOURCE-PROOF CANDIDATE**, not independently reviewed or parent-adopted. All mathematics is exact WRITTEN analysis. No scientific interpreter/eval/calculator/CAS/program/enumeration/replay/solver/CLI/nested agent, no machine-checked identity and no new GO.

## 0. Exact delta, source identity and independence

The preceding237LF `privacy-MDA26-norm-monotone-cost-direct-reconstruction-v1.md`, SHA256 `54cc4fd54fa74bad4c74d857ca7bca028cb0772bffe7771933857ebce52f164a`, gives a PER-COST alternative proof of the source's theoretical staircase-optimality conclusion. It expressly does NOT certify its stronger universal stochastic-dominator Lemma1 or weighted mass-matching Lemma7. That frozen scope remains unchanged.

This NEW body supplies those missing implications directly. Its new representation writes each INTEGER phase's ACTUAL weighted mass as a monotone expression in the amplitude sequence `a_k(u)=b^(-k)rho(k+u)`. Monotone convergence proves a genuine finite overshoot whenever unit decay has positive slack. It does not discard the tail or assume the modified profile agrees with the original on an initial interval.

Primary source: Melbourne–Diaz–Asoodeh, [*Optimality of Staircase Mechanisms for Vector Queries under Differential Privacy*, arXiv2601.14597v1](https://arxiv.org/html/2601.14597v1). Snapshot `RUN/privacy-source-snapshot-MDA26-v1.txt`, SHA256 `d2c986cb8d53a000259a3b4587833002d703481ab5c72481ad1d4bc7f122dccb`,1999 rendered logical LF. Current exact selected source reads188–238,289–301,495–583,1395–1585 cover the formal class, main theorem and full maximal-decay/mass-matching Lemma7 proof through the universal Lemma1 application. This is reader-text identity, not original PDF bytes, a newly complete1999LF read or all-version/publication certification.

**WRITTEN result:** for EVERY full-closed-norm-ball private Borel law, there is ONE fully private, radial nonincreasing lower-semicontinuous law with exact maximal unit decay whose norm is first-order stochastically no larger. The SAME selected law works for EVERY nonnegative nondecreasing norm-cost, including extended infinite expectations. No first-moment, initially optimal law, chosen loss or LAW642 premise is used.

The result and general rearrangement/maximal-decay methodology are positively PRIOR. This closes a source-proof interface, not a new mechanism/method discovery, registered optimum, novelty or public refutation. It is standalone at ordinary facts below, not a composition that assumes the unreviewed237LF proof.

## 1. Exact radial weighted lemma and named imports

Fix finite epsilon>0, b=exp(-epsilon)∈(0,1), and finite integer d>=1. Let rho:[0,infinity)→(0,infinity) be bounded, nonincreasing and right-continuous, with

    rho(r+1)>=b rho(r) for EVERY r>=0,
    I=integral_(0 to infinity)r^(d-1)rho(r)dr in(0,infinity).

For y>=0 define EXACTLY the source's unit-width periodic continuation

    rho_y(r)=b^floor(r-y) rho(r-floor(r-y)), r>=0,
    psi(y)=integral_(0 to infinity)r^(d-1)rho_y(r)dr.       (PHASE)

The argument of rho belongs to[y,y+1), hence is nonnegative. Negative floors for r<y are deliberate and valid, not omitted indices.

**Radial claim — WRITTEN:** there exists y>=0 with psi(y)=I. Every rho_y is finite, positive, nonincreasing, right-continuous and satisfies exact maximal decay `rho_y(r+1)=b rho_y(r)`. The matching y gives equal total weighted mass and a single crossing:

    rho_y(r)>=rho(r) for0<=r<=y,
    rho_y(r)<=rho(r) for r>=y.                            (CROSS)

The interval[y,y+1) is actually equality, so there is no sign ambiguity in the overlap.

**Ordinary classical imports:** nonnegative Tonelli/monotone convergence; dominated convergence; intermediate value theorem; elementary monotone-function right limits; Lebesgue density points/regularity/RN; norm-ball volume and zero sphere measure; Brunn–Minkowski; the CDF characterization of first-order stochastic domination. All problem-specific identities, finite overshoot, normalization and full-shift extension are supplied below. No source research lemma, numerical scout or other author packet is a correctness premise.

## 2. Feasibility and both-sided comparison of every periodic phase

Put k=floor(r-y) and s=r-k∈[y,y+1). Exact unit iteration gives

    rho(r+1)>=b rho(r).

If k>=0, then r=s+k and `rho(r)>=b^k rho(s)=rho_y(r)`. This covers r>=y. If k<0, then s=r+(-k) and `rho(s)>=b^(-k)rho(r)`, so `rho_y(r)=b^k rho(s)>=rho(r)`. This covers r<y. At k=0 the two profiles agree. Thus CROSS holds pointwise.

The floor identity gives for EVERY r>=0

    rho_y(r+1)=b rho_y(r).                               (EXACT)

Within each translated unit interval, rho_y is nonincreasing because rho is. At a junction r=y+k that lies in[0,infinity), the left limit is

    b^(k-1)rho((y+1)-),

whereas the right value/limit is b^k rho(y). The original lower-decay inequality gives `rho(y+1)>=b rho(y)` and monotonicity gives `rho((y+1)-)>=rho(y+1)`. Therefore the left limit is at least the right value. Right-continuity of rho supplies right-continuity at the junction. Hence rho_y is globally nonincreasing and right-continuous, including the right-domain limit at0. These properties imply lower semicontinuity at its downward jumps.

For0<=r<=s<=r+1, monotonicity and EXACT give

    rho_y(r)>=rho_y(s)>=rho_y(r+1)=b rho_y(r).

Thus the radial profile obeys the full unit-distance density ratio in BOTH directions, not merely the discrete recurrence at integer radii. The norm triangle inequality will turn it into full CLOSED-ball privacy in §7.

Every psi(y) is finite. Since floor(r-y)>=r-y-1 and rho<=rho(0),

    0<rho_y(r)<=rho(0)b^(r-y-1).

The right side times r^(d-1) is integrable. Real powers here mean the exact exponential expression; no float or numerical integration is used.

## 3. Exact integer-phase representation at the actual annular weights

Write r=k+u with integer k>=0 and0<=u<1. Define

    a_k(u)=b^(-k)rho(k+u),
    w_k(u)=(k+u)^(d-1)b^k,
    W(u)=sum_(k>=0)w_k(u).

Unit lower decay makes `a_(k+1)(u)>=a_k(u)` for EVERY u. Let `a_infty(u)=lim_(k->infinity)a_k(u)`, possibly infinity. W is finite and positive for0<u<1, by a geometrically weighted polynomial sum.

The ORIGINAL weighted mass is EXACTLY

    I=integral_(0 to1)sum_(k>=0)w_k(u)a_k(u)du.           (ORIG)

For an INTEGER phase y=m>=0,

    floor(k+u-m)=k-m,
    rho_m(k+u)=b^(k-m)rho(m+u)=b^k a_m(u).

Therefore its actual weighted mass is

    psi(m)=integral_(0 to1)W(u)a_m(u)du.                 (INT_PHASE)

All equalities follow by partition into half-open unit intervals and positive Tonelli; no Riemann-sum approximation or equal-shell-volume assumption is present.

Since a_m increases pointwise, INT_PHASE gives a MONOTONE integer sequence and monotone convergence gives

    psi(m) increases to Psi
      =integral_(0 to1)W(u)a_infty(u)du.                 (LIMIT)

ORIG and a_infty>=a_k give Psi>=I. The comparison includes the entire infinite tail with its true factor(k+u)^(d-1).

## 4. A genuine finite overshoot whenever decay is not already exact

If `rho(r+1)=b rho(r)` for EVERY r>=0, unit forward/backward iteration makes rho_y=rho for every y. Then psi(y)=I and there is nothing to find.

Otherwise take a finite r*=k*+u*, k*>=0 integer,0<=u*<1, with

    rho(r*+1)>b rho(r*).

Both rho(r+1) and rho(r) are right-continuous. Therefore the strict inequality persists on a sufficiently small RIGHT interval[r*,r*+eta), with eta>0 chosen so u*+eta<1. There is a positive-length interval U⊂(0,1) with

    a_(k*+1)(u)>a_(k*)(u) for EVERY u∈U.

If u*=0, take its positive open subinterval; no zero-radius weight is used. Since w_(k*)>0 on U and the difference is a nonnegative measurable function positive at every point of U, the exact integral

    Delta=integral_U w_(k*)(u)
                     [a_(k*+1)(u)-a_(k*)(u)]du

is STRICTLY positive and finite. Finiteness follows from bounded rho and fixed finite k* on the bounded interval.

Using a_infty>=a_(k*+1), the pointwise nonnegative sum difference in ORIG/LIMIT gives

    Psi>=I+Delta>I.                                     (STRICT_LIMIT)

If Psi=infinity the same inequality is interpreted in extended values. Positive Tonelli justifies this comparison; I is finite, so no infinity-minus-infinity expression is needed.

By monotone convergence of the ACTUAL finite values psi(m) to a limit STRICTLY above I, SOME FINITE integer m has

    psi(m)>I.                                          (OVERSHOOT)

This is the missing weighted overshoot argument. It does NOT assume rho_m agrees with rho on the initial interval, infer total-mass improvement by looking only at a positive local excess, or drop a possibly adverse tail. The full integer-phase mass formula proves the statement directly.

Also CROSS for y=0 gives rho_0<=rho, hence

    psi(0)<=I.                                         (START)

## 5. Continuous mass matching, including jumps and negative floors

Fix a finite bound M_y>=0 and any sequence y_j→y in[0,M_y]. For each fixed r NOT in the countable set `y+Z`, the number r-y is not an integer. Hence `floor(r-y_j)=floor(r-y)` for all sufficiently large j. The arguments of rho in PHASE then coincide EXACTLY, so

    rho_(y_j)(r)=rho_y(r) eventually.

This a.e. pointwise convergence does not require continuity of rho at its sampled argument and does not ignore changing negative floors.

The common bound from §2 is

    r^(d-1)rho_(y_j)(r)
        <=rho(0)b^(-M_y-1)r^(d-1)b^r,

an integrable function independent of j. Dominated convergence therefore proves psi(y_j)→psi(y). Thus psi is continuous on EVERY bounded y interval.

If exact decay holds, choose y=0. Otherwise START and OVERSHOOT put I between psi(0) and psi(m) for a finite m. The intermediate value theorem gives a finite y∈[0,m] with

    psi(y)=I.                                          (MATCH)

No monotonicity of psi at NONINTEGER y, numerical root, evaluated inverse, mass renormalization or maximum-attainment assumption is required. MATCH is the source's exact weighted-mass claim.

For arbitrary source sensitivity scale Delta_s>0, apply the unit proof to `rho_tilde(s)=rho(Delta_s s)`. Its weighted integral is I/Delta_s^d; the selected physical anchor is Delta_s y. Substitution gives exactly `rho_y(r)=b^floor((r-y)/Delta_s)rho(r-Delta_s floor((r-y)/Delta_s))` and the original weighted mass. Thus the scale is not silently fixed in the conclusion.

## 6. ONE cost-independent stochastic dominator for every radial law

Let K be any genuine norm unit ball in R^d, V=|K|, and let f(z)=rho(r(z)), r=||z||_K, be a probability density meeting §1's hypotheses. The radial volume formula gives `d V I=1`. MATCH therefore makes

    f_Y(z)=rho_y(r(z))

an ACTUAL probability density with NO new normalizing factor. By §2 it is radial, nonincreasing, right-continuous/lower-semicontinuous and maximally decaying at every radius.

Its radial CDF difference from the original is

    P(r(Y)<=R)-P(r(X)<=R)
       =d V integral_(0 toR)s^(d-1)[rho_y(s)-rho(s)]ds.

For R<=y the integral is nonnegative by CROSS. For R>=y, equality of the TOTAL weighted mass makes that integral the NEGATIVE of the tail integral from R to infinity, which is nonpositive by CROSS. Hence it is again nonnegative. Therefore

    r(Y) is first-order stochastically no larger than r(X).

The chosen y depends ONLY on rho,b,d, not on any loss function. Thus the SAME Y has no larger expectation for EVERY nonnegative nondecreasing phi, with extended infinite expectations allowed. This is the universal assertion that the earlier PER-COST237LF proof intentionally did not claim.

## 7. Full all-Borel norm-ball extension, with the geometry supplied

For completeness take ANY Borel probability law mu private under EVERY shift h∈the FULL CLOSED K. No density, radiality or moment is assumed initially.

As in the elementary Fubini argument, integrate privacy over K for null sets to get AC, and then integrate fixed-h density inequalities to get `p<=1/(bV)` a.e. A bounded positive-volume zero set would be null under EVERY translate by privacy iteration, contradicting Tonelli over all translations. Thus p>0 a.e. and has a positive finite essential supremum.

For a>0 let A_a={p>a} and `R(a)=(|A_a|/V)^(1/d)`. The sets have finite volume and R is nonincreasing/right-continuous. Fixed-h privacy implies the essential enlargement bound `R(ba)>=R(a)+1` when |A_a|>0: define `F_a(z)=integral_(intK)1_(A_a)(z-h)dh`, apply Fubini to get F_a<=V1_(A_ba) a.e., and put compact subsets C of density points of A_a into `{F_a>0}` by C+intK. Brunn–Minkowski gives `|A_ba|^(1/d)>=|C|^(1/d)+V^(1/d)`; regularity lets |C| approach |A_a|. This supplies the enlargement without an uncountable-null-set union.

Define

    psharp(z)=sup{a>0:r(z)<R(a)}, sup(empty)=0.

Right-continuity gives `{psharp>a}={r<R(a)}`. Layer cake gives integralpsharp=1. For EVERY z∈R^d and EVERY h∈the CLOSED K, `r(z+h)<=r(z)+1` together with the enlargement gives `psharp(z+h)>=b psharp(z)`. Its chosen radial profile rho is therefore positive, bounded, nonincreasing and satisfies `rho(r+1)>=b rho(r)` for EVERY r>=0.

The profile is right-continuous: if rho(r0) exceeded its right limit, a threshold between them would make the strict set `{rho>a}` contain r0 but no points immediately to its right, contradicting its open-ball form. The norm-ball volume identity gives the positive finite weighted integral I=1/(dV), so ALL hypotheses of the radial lemma hold.

This rearrangement is a stochastic improvement independently of cost. For every R>=0 and every threshold a,

    |{psharp>a}∩RK|=min(|A_a|,V R^d)>=|A_a∩RK|.

Integrate in a by Tonelli to get `P(r(Xsharp)<=R)>=P(r(X)<=R)` for EVERY R. Boundaries are null by AC.

Apply §6 to Xsharp and compose the TWO radial CDF orders. The resulting SINGLE law Y has maximal unit decay and stochastically no larger norm than the ORIGINAL arbitrary Borel law. For any real h∈CLOSED K, the norm triangle inequality gives `|r(z+h)-r(z)|<=1`; §2's BOTH-sided radial ratio proves actual event privacy for Y, including the slanted/closed boundary and all Borel events.

This completes the full universal source Lemma1 conclusion at ordinary facts. No research radialization/maximal-decay theorem, selected cost, initial optimum, finite first moment, LAW642 or hidden new approximation family was assumed.

## 8. Exact source scope and surviving non-claims

This new body supplies the precise weighted Lemma7 mass-matching implication and universal cost-independent maximal-decay reduction in the full closed norm-ball law class. Its selected y is a written existence result, NOT an evaluated scalar root or algorithm. The new proof replaces the source's disputed overshoot reasoning; it does not silently endorse every intermediate sentence of the frozen source or edit any source bytes.

The earlier237LF body remains a separate PER-COST alternative main-theorem proof. Its earlier explicit universal-domination nonclaim is historically correct for THAT body and is not rewritten. THIS later body provides the stronger universal implication in a new proof, requiring its OWN complete source/mathematics/dependency/application gate.

Still outside scope: the full source's extreme-point/weak-compactness characterization, every version's exact formulations, printed samplers/grid search/experiments, original per-query sensitivity necessity beyond the full-ball noise-law class, and all-original-optimizer classification for flat losses. No theorem about the registered mixed-norm Euclidean MSE is inferred from norm-cost domination.

Positive PRIOR attribution to MDA26 and older rearrangement/saturation tools remains. No new mechanism/value discovery, worldwide firstness, all-creative-corollary non-equivalence, novelty/publication significance or publication-wide correctness/falsity claim. Source/priority remains bounded and UNCLEAR; no prior acceptance transfers automatically to this new proof.

## 9. Permanent process and original round

The new integer-phase/weighted-overshoot lead was saved in checkpoint094 BEFORE this full body. All mathematics is exact WRITTEN; no scientific execution or kernel check. All firstfive owner findings, SIXTH DISTINCT v111B written-exactness finding, SEPARATE077 continuation failure, v21 category correction, auxiliary214 UNADMITTED/strictSTOP and all parent/reviewer/source/import/N4UNKNOWN/exit/old-arithmetic qualifications remain. No clean cognition/runtime/history or continuous-work census, stronger human/family/cross-vendor/formal/kernel/executable/novelty/publication assurance or new GO.

Exclusive own root only; pinned/source/ACK/parent/other-owner bytes unchanged. No auxiliary graph derivation, new model/slot, publication or deadline reset. Same eighteen owners, science cutoff **2026-10-27T11:05:38-07:00**, delivery **2026-10-27T12:35:38-07:00**; active substantive actual-clock checkpoints at most30minutes. This is not early final-park or round closeout; the registered source/proof/priority residual continues.
