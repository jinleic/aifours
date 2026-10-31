# Kulesza publisher: universal angular moment identity and radial-infimum bridge

Status: AUTHOR_WRITTEN / UNREVIEWED. This is written mathematics, not a kernel/formal proof, execution result, independent review, publication-equivalence certificate, or novelty claim.

Owner: InfoResearch96h-2 / info-1. Native pre-write observation: `Tue Oct 27 16:34:17 PDT 2026`.

## 1. Authorized input and exact added edge

The input is the already admitted Kulesza/Suresh/Wang publisher PDF, PMLR 258 (2025), local retained version SHA-256 `4e67a46d80e705df6b23a92e8fb88599a8b14c874af3f7b434a0ed217ca71df3`. All 21 rendered pages were previously read. PDF page 8 was re-opened specifically for the present map: its definition of angular averaging and Lemma 6, not the subsequent existence inference or staircase optimality theorem. Pages 6–7 provide the event-law to pointwise-density interface. The elementary planar change of variables used below is supplied directly, not imported from the bibliography.

No new source, old proof, LAW642 conclusion, v253 conclusion, MDA optimality/attainment claim, or phase-type mathematics is a premise. The queued angular-cost-obstruction candidate is not a proof premise either. The previous correspondence/ledger files identify the question but their verdicts are not used to establish the following statements.

New edge: for the FULL closed-diamond/all-Borel feasible class, angular averaging identifies the entire CENTERED-DIAMOND-RADIAL Euclidean squared-loss INFIMUM with two thirds of the all-law squared-l1 INFIMUM. This needs no optimizing law, staircase selector, higher-moment extension of the printed theorem, or existence proof. It therefore provides an independent source-map-based upper-comparison edge, not the missing exact original optimum.

The angular second-moment calculation also gives the exact sign criterion for the Euclidean-cost change for EVERY finite-cost feasible input law, not only a selected family.

## 2. Full law class and exact map

Fix arbitrary finite epsilon > 0. Write `R(x)=|x_1|+|x_2|`, `E(x)=x_1^2+x_2^2`, and `D={h:R(h)<=1}`. Let F_epsilon contain all Borel probability laws mu on R^2 such that

    mu(A) <= exp(epsilon) mu(A+h)

for EVERY Borel A and EVERY h in the full CLOSED set D. These are the original-law event inequalities; no density assumption, symmetry, mean-zero constraint, restricted shift set, or restricted output-event family is built into F_epsilon.

For completeness, the pointwise-density bridge used by the published map can be realized without an optimizer premise. Integrating the displayed inequality over h in D, Tonelli gives

    |D| mu(A) <= exp(epsilon) |A|,        |D|=2.

Here the integrated right side before its final bound equals `exp(epsilon) integral mu(dy) |D intersect (y-A)|`; it is at most `exp(epsilon)|A|`. For infinite-measure A the bound is interpreted in the extended sense. Thus mu has a globally bounded Radon–Nikodym density. Define p(x) by the limsup of mu(B(x,t))/|B(x,t)| as t decreases to zero, using ordinary Euclidean balls. The same bound makes this finite everywhere; Lebesgue differentiation makes it a density for the SAME law. The event inequality on translated balls gives simultaneously, for ALL x,y with R(x-y)<=1,

    p(x) <= exp(epsilon) p(y).

This is an existence of a suitable representative, not a statement about every representative. It is the source's event-to-pointwise interface specialized to the actual D. The proof is independent of the MDA Appendix A argument; it does not change or repair the recorded NR-A finding.

Let sigma be the probability on the l1 unit sphere described as follows: select one of the four sign pairs with equal weights and integrate u uniformly over the entire interval (0,1), with

    theta=(s_1 u, s_2 (1-u)).

The repeated endpoints have measure zero. On each open quadrant `x=r theta`, `r>0`, the absolute Jacobian of (r,u) -> (s_1 r u,s_2 r(1-u)) is r. Hence, for every nonnegative measurable F,

    integral_R2 F(x) dx = 4 integral_0^infinity r E_sigma[F(r theta)] dr.       (1)

Define the source's actual averaging map by

    q(r)=E_sigma[p(r theta)],        bar_p(x)=q(R(x)).                         (2)

The global bound on p makes q finite. Formula (1) proves normalization and proves that the resulting law Tmu is independent of the choice of density version: two versions agree for almost every (r,theta) under r dr sigma, so their q agree for almost every r and their bar_p agree Lebesgue almost everywhere. A well-behaved representative is used to prove pointwise privacy, not to change the underlying input law.

For every x,h with h in D, the reverse triangle inequality gives `|R(x)-R(x+h)|<=1`. For EVERY theta, the two points `R(x)theta` and `R(x+h)theta` differ by an element of D, including when this norm difference equals 1. Integrating their pointwise density inequality yields

    bar_p(x) <= exp(epsilon) bar_p(x+h).

Integration over arbitrary Borel A gives the original event inequality for Tmu. Thus T maps the ENTIRE original F_epsilon into itself and its image has a centered-D-radial density. This is the printed Lemma 6 coupling, with its full event-law caller paid explicitly. No independence between selected angles/shifts, almost-everywhere shift relaxation, or interior-only privacy condition is used.

## 3. Full radial-law preservation, including infinite moments

Let g be ANY nonnegative Borel function of r. Formula (1), followed by Tonelli and (2), gives

    integral g(R(x)) bar_p(x) dx
      = 4 integral_0^infinity r g(r) q(r) dr
      = integral g(R(x)) p(x) dx.                                          (3)

In particular Tmu preserves the ENTIRE R-marginal, not merely the first radial moment appearing in the printed objective. This is a property of the explicit source map, not an assertion that the source's optimizer theorem already covers all g.

The geometric angular integral over the WHOLE fixed sphere is

    E_sigma[E(theta)]
      = integral_0^1 [u^2+(1-u)^2] du
      = 2/3.                                                               (4)

This is symbolic integration of the defining full interval, not a chosen parameter, angle, boundary probe, decimal check, or numerical experiment.

Applying (1) to the centered-radial density in (2) now gives the extended-value identity

    M(Tmu) := integral E(x) Tmu(dx)
            = (2/3) integral R(x)^2 mu(dx)
            =: (2/3) W(mu).                                               (5)

Equations (3)–(5) hold for EVERY mu in F_epsilon, with nonnegative extended integrals. Since `E(x)<=R(x)^2<=2E(x)`, infinite original Euclidean second moment is equivalent to infinite W(mu), and then M(Tmu) is infinite too. No difference of two infinities is taken.

## 4. Exact all-law finite-cost sign criterion

For finite M(mu), let `C(mu)=integral |x_1 x_2| mu(dx)`. This is finite because `2|x_1 x_2|<=E(x)`. The pointwise identity `R(x)^2=E(x)+2|x_1 x_2|` and (5) imply

    M(Tmu)-M(mu) = [4 C(mu)-M(mu)]/3.                                      (6)

Consequently, for EVERY finite-cost mu in the full original class:

- averaging reduces Euclidean squared loss exactly when `4 C(mu)<M(mu)`;
- it preserves that loss exactly when `4 C(mu)=M(mu)`;
- it increases that loss exactly when `4 C(mu)>M(mu)`.

This criterion requires neither radiality nor symmetry of the INPUT law. It is not a claim that the first or third alternative holds for all feasible laws. In particular preserving W(mu) does not imply non-increase of M(mu). The separate queued all-epsilon actual-law obstruction is not needed to prove the universal criterion.

## 5. Infimum identities without attainment, compactness, or a selector

Let R_epsilon be the subclass of F_epsilon consisting of laws with a density of the form `f(R(x))`; this means the centered diamond, not the union of all norms or all translated norm families. Define

    V = inf_{mu in F_epsilon} M(mu),
    W = inf_{mu in F_epsilon} W(mu),
    V_rad = inf_{nu in R_epsilon} M(nu),
    W_rad = inf_{nu in R_epsilon} W(nu).

All four classes/costs are genuine original-law objects. A normalized density proportional to `exp(-epsilon R(x))` is a feasible radial law with finite second moments: the triangle inequality gives the full closed-shift density inequality, and the product exponential tails give integrability. Thus these infima are finite and nonnegative; no minimizing law is assumed.

Because R_epsilon is a subclass, `W_rad>=W`. Conversely (2)–(3) send EVERY feasible mu to a law Tmu in R_epsilon with exactly the same W(mu), so `W_rad<=W`. Therefore

    W_rad = W.                                                             (7)

For EVERY nu in R_epsilon, the direct angular integration (4) gives `M(nu)=(2/3)W(nu)`, whether or not nu is an image selected from an optimizer. Taking infima and using (7) gives

    V_rad = (2/3) W.                                                        (8)

Since R_epsilon is a subclass of F_epsilon, and since `M(mu)>=W(mu)/2` pointwise after integration, the original full-class value obeys

    (1/2) W <= V <= V_rad = (2/3) W.                                        (9)

For the upper inequality one can equivalently apply (5) to every approximate W-minimizing law and then take the infimum. That is an all-variable infimum argument, not a computed sequence or an assertion that the infimum is achieved. There is no appeal to the source's existence Lemma 17, its topology, cyclic-decay argument, or a squared-loss staircase selector.

If a W-minimizer is separately supplied, its average is a radial W-minimizer and a V_rad-minimizer. This is ONLY a conditional attainment transfer. It supplies neither unconditional attainment of W nor a global V-minimizer unless the additional equality `V=V_rad` is proved. No uniqueness statement follows.

## 6. Exact source-to-target frontier

Paid positive edges, at AUTHOR_WRITTEN scope:

1. Same full Borel law and all CLOSED D shifts -> finite pointwise density representative -> the actual source averaging law Tmu in the SAME original feasible class.
2. All radial moments and the radial marginal are preserved by T, as properties of the explicit map.
3. The entire centered-D-radial squared-Euclidean infimum equals `(2/3)` times the full-class squared-l1 infimum, with NO attainment import.
4. The upper comparison `V<=(2/3)W` and the lower norm-equivalence comparison `V>=W/2` are noncircular written consequences. LAW642, v253, MDA per-cost optimality, and any original Euclidean optimum/selector were not used.
5. The exact original-law sign obstruction (6) distinguishes angular covariance effects from mere failure to match the printed radial-cost hypothesis.

Unpaid implications remain exact and substantial. The source's mean-norm optimizer theorem does not give W's value, a squared-l1 attaining staircase, or its unique selector. The map does not prove that V equals V_rad at any parameter, nor that V is strictly smaller at another parameter. Indeed, by (8)–(9), the missing all-law bound

    for EVERY mu in F_epsilon, M(mu)>=(2/3)W

is equivalent to `V=V_rad`; establishing its exact epsilon range would require new input or an independently admitted proof. A pointwise comparison with W(mu), rather than the infimum W, is a DIFFERENT and generally stronger assertion; (6) is why one cannot substitute it. The original unique equality law, rounded competitor/transition, and full source-to-registered-target equivalence are not established here.

This is a new written consequence/implication ledger edge from the already admitted publisher map and elementary planar geometry. It is NOT a claim that the publisher printed equation (8), printed a squared-loss optimizer theorem, independently proved LAW642, or anticipated the registered threshold. No priority, global non-equivalence, external novelty, or proof-family acceptance conclusion is drawn.

NR-A, NR-D, NR-K17, NR-K10, all prior STOP/HOLD/ZERO records, the phase-type whole-mixed-packet noninput, N4 UNKNOWN, and aux214 STOP remain unchanged. No held artifact was opened or used, no prior selected test was reconstructed, and no finite scientific check/execution was performed.

## 7. Method and machine-check declaration

All mathematics above is WRITTEN, with the explicit elementary imports Tonelli, Radon–Nikodym, Lebesgue differentiation, the ordinary planar change-of-variables theorem, norm triangle inequalities, and polynomial integration. No identity was machine-checked. No Eval/interpreter/CAS/calculator/enumerator/solver or selected hand sanity control was used. Native metadata tools only recorded clocks and will pin this immutable candidate. The result is pending a separate frozen review.
