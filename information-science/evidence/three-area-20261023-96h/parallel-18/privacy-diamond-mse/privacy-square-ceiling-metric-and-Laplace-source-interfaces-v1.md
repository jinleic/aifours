# Registered privacy source interfaces: exact square/ceiling metric, convex-budget reduction and two Laplace-optimality sources

Owner **InfoResearch96h-2**, original info-1. Actual `/bin/date` BEFORE this write: **Mon Oct 26 06:24:10 PDT 2026**. **NEW AUTHOR-WRITTEN source/application packet**, not an independent review, parent adoption, formal/kernel verification or novelty clearance. Exact symbolic/fraction mathematics only; no scientific interpreter/eval/calculator/CAS/program/enumeration/replay/solver/CLI/nested agent or new GO.

## 0. Registered model, scope and positive prior attribution

The registered model remains ALL Borel query-output-independent additive probability laws on R², EVERY shift of the FULL CLOSED unit-l1 diamond D, fixed finite epsilon>0 and squared-Euclidean loss. This packet changes its REPRESENTATION for a source comparison, not its optimization class or registered problem.

A prior search limited to “diamond” or “mismatched norm” language can miss equivalent statements. Sections1–2 therefore supply an exact square-sensitivity and ceiling-metric representation before examining two sources with apparently broad continuous-query optimality claims:

- **MS25:** Goel–Jiang–Korolova–Munagala–Sarmasarkar, [*Differential Privacy Under Multiple Selections*](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.FORC.2025.8), FORC2025, Article8,1–25; actual [publisher PDF](https://drops.dagstuhl.de/storage/00lipics/lipics-vol329-forc2025/LIPIcs.FORC.2025.8/LIPIcs.FORC.2025.8.pdf).
- **FMM21:** Fernandes–McIver–Morgan, [*The Laplace Mechanism has optimal utility for differential privacy over continuous queries*](https://arxiv.org/html/2105.07176v2), LICS2021,1–12; DOI [10.1109/LICS52264.2021.9470718](https://doi.org/10.1109/LICS52264.2021.9470718).

Both supply substantive PRIOR optimality/continuous-channel/duality/approximation machinery. This lane does not claim any of those generic methods as new. Their exact read theorems do not automatically give the registered closure, for the precise budget/class reasons below. **No worldwide absence, impossibility of every creative adaptation, publication-wide correctness or source falsity conclusion is drawn. Priority/novelty remain UNCLEAR.**

All new claims carry WRITTEN scope. Imports are elementary invertible linear changes of variables, finite event-inequality chaining, limits of real exponentials, and convex-function secant inequalities. No research theorem is needed to prove the representation or convex-budget lemma.

## 1. Exact full-law square representation, WRITTEN

Let

    T(x,y)=(u,v)=(x+y,x-y),
    T^(-1)(u,v)=((u+v)/2,(u-v)/2).

For all real x,y,

    max(|x+y|,|x-y|)=|x|+|y|,
    u²+v²=2(x²+y²).

The first identity follows by separating the same-sign and opposite-sign cases for x,y; the second by expanding the two squares. Therefore T maps the ENTIRE CLOSED diamond D bijectively onto the ENTIRE CLOSED square C=[-1,1]².

For any Borel probability law mu, let nu=T_#mu. The invertible linear map and its inverse are Borel, and

    nu(B+h)=mu(T^(-1)B+T^(-1)h)

for every Borel B and h. Thus

    mu is epsilon-private for every shift in D
      iff nu is epsilon-private for every shift in C.        (SQUARE_DP)

This is an all-Borel-law equivalence, not an assumption that a density exists. If p is a density of mu, then nu's density is

    q(u,v)=(1/2)p((u+v)/2,(u-v)/2),
    p(x,y)=2q(x+y,x-y),

because |detT|=2. The objective transforms exactly:

    integral (x²+y²)mu(dxdy)
       =(1/2)integral (u²+v²)nu(dudv).                       (SQUARE_COST)

Consequently if V_C denotes the all-law squared-Euclidean infimum at full CLOSED-square sensitivity, `V_D=V_C/2`, and optimizers correspond bijectively under T. This is an equivalent-source search route, not a new optimum proof, changed sensitivity radius, independence assumption or source acceptance.

In particular the square problem is still coupled: requiring privacy for EVERY shift(|h1|,|h2|<=1) simultaneously is not merely imposing two separate unit-axis constraints. No product-mechanism optimality follows from separability of the written cost.

## 2. Full continuous step sensitivity is exactly a ceiling metric, WRITTEN

For any norm unit ball K in a finite-dimensional real vector space define

    delta_K(x,y)=ceil(||x-y||_K),

with ceil(0)=0. It is a genuine metric: positivity and symmetry are immediate, and the norm triangle inequality together with `ceil(a+b)<=ceil(a)+ceil(b)` gives its triangle inequality. Every two distinct points have delta_K>=1; its metric topology is discrete even though the underlying query space and Borel events in this model remain Euclidean. “Continuous input domain” therefore does NOT by itself force a distance-proportional budget at tiny displacements.

For an additive Borel law mu the following are equivalent:

    mu(A)<=exp(epsilon)mu(A+h)
       for EVERY Borel A and EVERY h in K,                   (STEP_K)

    mu(A)<=exp(epsilon ceil(||h||_K))mu(A+h)
       for EVERY Borel A and EVERY h in the whole space.     (CEIL_K)

For STEP_K=>CEIL_K, take nonzero h and the exact integer N=ceil(||h||_K). Then h/N∈the CLOSED K. Chain the N event inequalities along the same translated event. When h=0 the inequality is equality. Conversely ||h||_K<=1 makes the exponent either0 or epsilon and immediately recovers STEP_K. No uncountable-null-set synchronization or density derivative is required.

For an arbitrary full-space channel x↦P_x, imposing the step budget for every pair with||x-y||_K<=1 gives the same ceiling-metric bound by the same finite straight-line chaining. This is a formal-class comparison, not a claim that arbitrary nonadditive channels share the additive optimum.

A direct isometric substitution of this metric into an ordinary real-line Euclidean theorem is impossible even on three points: in the diamond take0,(1/2,0),(0,1/2). All three pairwise ceiling distances equal1. Three distinct points on the real line cannot all have pairwise Euclidean distance1, because the two adjacent intervals add to the outer interval. This rules out THAT direct distance-preserving one-dimensional substitution, not every possible reduction/corollary.

## 3. Convex differentiable privacy budgets collapse to their tangent budget, WRITTEN

### 3.1 Full event-kernel statement

Let X be a convex subset of a normed real vector space. Let x↦P_x be ANY family of probability laws on the same measurable output space. Let g:[0,infinity)→[0,infinity] be convex, g(0)=0, finite in a neighborhood of0, and right-differentiable at0 with finite derivative a=g'_+(0). Assume

    P_x(A)<=exp(g(||x-y||))P_y(A)
    for EVERY x,y in X and EVERY measurable A.               (G_DP)

Then it is EQUIVALENT to

    P_x(A)<=exp(a||x-y||)P_y(A)
    for EVERY x,y,A.                                        (TAN_DP)

The proof needs neither a density, derivative of a mechanism, boundedness of X nor a claimed optimizer. This is an exact original-class probability inequality.

### 3.2 Proof with every subdivision and direction retained

Fix x,y,A, write r=||x-y||, and for every positive integer n subdivide the straight segment into n points with each successive distance r/n. Convexity of X keeps all the intermediate inputs in X. Finite application of G_DP gives

    P_x(A)<=exp(n g(r/n))P_y(A).

Since g is right-differentiable at0 and g(0)=0,

    n g(r/n)=r [g(r/n)/(r/n)] ->a r

for r>0, with the r=0 case immediate. Passing to the real scalar limit proves TAN_DP. This step remains valid if P_y(A)=0; every preceding inequality already forces P_x(A)=0. Reversing x,y gives both ordered directions.

Conversely convexity gives `g(s)/s>=a` for every s>0 at which g is finite, by monotonicity of secant slopes from0. If g(s)=infinity, the corresponding G_DP inequality is automatic. Thus `g(s)>=a s` and TAN_DP implies G_DP. This proves the full equivalence.

The forward implication actually requires only the finite tangent limit, not convexity; convexity is used for the converse. A positive finite cutoff beyond which g=infinity is compatible with the proof if its neighborhood-of0 assumptions hold. This is why the phrase “privacy only below a threshold” alone does not identify the fixed-EPSILON step model.

### 3.3 The registered ceiling budget fails the stated hypothesis exactly

For the registered model the natural radial budget is

    g_step(0)=0,
    g_step(r)=epsilon ceil(r) for r>0.

For0<r<=1, g_step(r)=epsilon. Therefore its quotient g_step(r)/r tends to infinity as r↓0, not to a finite a. It is also NOT convex: `g_step(1/2)=epsilon>(1/2)g_step(1)+(1/2)g_step(0)=epsilon/2`.

Thus the full constant-EPSILON neighbor budget cannot be slipped into a theorem that requires g convex and differentiable at0 with finite nonzero derivative. The fact that a theorem separately permits g=infinity above a positive cutoff does not remove its finite-tangent requirement BELOW that cutoff.

A corresponding stricter metric-private additive law would be STEP_K-feasible, so its optimum on a genuinely matched class could give an UPPER bound for the step-class infimum. A lower bound proved only on that stricter subclass is not a lower bound on every STEP_K law. No new numerical bound is claimed here.

## 4. MS25: actual optimality theorem, generalized-g assumptions and limits

### 4.1 Actual complete rendered-text coverage

The publisher-PDF reader is artifact34508, SHA256 `86926bd5318242354a5856965952fb1fb93a08fa93eedcbda7a5fd07d16b9e01`,86626bytes,643 literal LF/644 rendered logical lines. Actual reads:1–300 from fetch, raw301–500 and501–644 including the last AppendixB recurrence and publication ending. This is complete RENDERED-TEXT reading, not PDF-byte/glyph certification or execution.

The source repeatedly defers full proofs to [arXiv2407.14641](https://arxiv.org/abs/2407.14641), including its exact weak-duality theorem, density approximation, derivative equivalence and several server-action claims. Those full-version proofs were NOT fetched in this pass and remain **NOT_RECONSTRUCTED** here. The publisher's sketches and references are positively prior statements/methods, not a complete correctness audit of every imported proof.

### 4.2 Actual privacy and utility quantifiers

Definition2 imposes geographic/metric privacy with factor `exp(epsilon |u1-u2|)` for EVERY input pair on the real line and EVERY measurable output event. The mechanism is a triplet of user signal space/distributions and server distribution over k returned results. Eq6 uses worst-case user expected MINIMUM disutility among that set of results, measured through an increasing function h of the input–result distance. This is not registered planar additive MSE.

Its Theorem5/Theorem19 supplies the Laplace-optimal user action in that actual privacy/architecture, with a server response selected to suit the disutility. Its Section1.3.5 and Theorem14 introduce an infinite-dimensional differential/integral LP weak-duality route. These are substantial positive PRIOR constructions, not dismissed because the system architecture is unfamiliar.

AppendixA's higher-dimensional discussion states a bound under further assumptions with Gaussian features and dimensional reduction, and defers its details to the full version. It is NOT an exact two-dimensional full-step-square/diamond all-law value/equality theorem in the displayed source.

### 4.3 Exact generalized-g interface

AppendixA.1's **Assumption20** requires g increasing, convex, g(0)=0 and differentiable at0 with g'(0)≠0. Definition21 uses `exp(g(|u1-u2|))`. Theorem22 gives Laplace density with rate g'(0); Lemma23 states a mechanism-derivative equivalence at that rate. The same section says g may be infinite above a threshold.

Our §§3.1–3.2 provides a direct all-event kernel explanation of that tangent budget on the source's real-line domain, without assuming its NOT_RECONSTRUCTED mechanism-derivative proof. Its convexity/finite derivative conditions leave the feasible class metric-private at rate g'(0); they do not include g_step. Section3.3 proves the exact hypothesis failure, not just a mismatch in names.

**Conclusion — WRITTEN source applicability, not source falsity:** MS25's generalized-threshold language cannot by itself be cited as solving the registered constant-budget continuous-neighbor problem. Reconstructing its missing transitive proofs would still not remove that explicit premise. No claim that every creative extension of its duality method fails is made.

## 5. FMM21: actual Euclidean metric, prior/remapping loss and bounded interval

### 5.1 Source identity and actual coverage

Primary [arXiv2105.07176v2](https://arxiv.org/html/2105.07176v2) identifies26July2021. The actual [Crossref DOI record](https://api.crossref.org/works/10.1109/LICS52264.2021.9470718) identifies the LICS2021 publication,1–12, printed29June2021 and DOI creation7July2021. Those DOI dates are publication metadata, not dates of our read or a mathematical proof certificate.

The HTML reader is artifact34552, SHA256 `d2b88bb2d9bbeacf6087521bc95212d0e5d782a694c7c3b36745dae5ddec49d4`,123900bytes,835 literal LF/836 rendered logical lines. Actual reads:1–300 from fetch, raw301–500,501–700 and701–836 including all references/end. These are the full conference-style HTML body, NOT its separately linked [full-version appendices](http://www.cse.unsw.edu.au/~carrollm/LiCS2021-210420.pdf). Several key refinement/approximation details are explicitly deferred there and remain **NOT_RECONSTRUCTED** here. No source correctness verdict is inferred from complete main-body reading.

### 5.2 Precise theorem, not the abstract's broad sentence

Definition1 makes the channel epsilon-Lipschitz from the CHOSEN input metric d to max-divergence of output distributions. SectionII-G then EXPLICITLY fixes the continuous raw-query input space to[0,1] and d to Euclidean absolute difference; it says the main theorem requires that metric.

Definition2 measures expected loss by integrating over observations the infimum over guesses of posterior expected loss, with a continuous PRIOR on[0,1]. Thus an observer may remap its observation. Definition4 uses the Laplace mechanism CLAMPED to[0,1], including endpoint atoms. Theorem5's quantifiers are continuous epsilon-DP mechanisms with input/output both[0,1], every continuous prior and every Lipschitz-continuous legal loss function.

This is a genuine broad PRIOR Bayesian/remapping optimality theorem in its exact class. It is not a theorem that an unclamped query-independent additive Laplace law minimizes squared noise over R² at the constant step-D budget. The source's RelatedWork explicitly distinguishes KHP2015 metric-privacy/non-Bayesian results and leaves Bayesian R^n extension to future work. That context is consistent with the precise metric/dimensional interfaces rather than replacing them.

### 5.3 Why the general channel definition does not silently widen Theorem5

The general Definition1 CAN describe other metrics. But Theorem5 as stated uses the source's explicitly fixed Euclidean metric on a real interval and the approximation proof uses privacy factors exp(epsilon/N) at interval width1/N. Section2's equivalent registered delta_K budget instead stays epsilon across every distinct arbitrarily close pair. Substituting delta_K into Definition1 would change Theorem5's proof premises and tiny-distance bounds; the general definition is not a theorem for all metrics.

Section2's three-equidistant-point obstruction also blocks an immediate distance-preserving substitution of the registered metric into that one-dimensional Euclidean theorem. No proof that arbitrary encodings/reductions are impossible is claimed. The displayed source has not supplied the needed multi-dimensional/step-metric/additivity/remapping-to-noise-cost bridge.

## 6. Exact disposition and remaining gap

This packet supplies three new exact source-interface facts in full WRITTEN scope:

1. Every original full-diamond Borel additive law corresponds bijectively to a full-square law, with precisely half the transformed squared loss.
2. The full continuous unit-neighbor constant budget is exactly epsilon times the CEILING-norm metric, not epsilon times the original norm.
3. Convex finite-differentiable-at0 distance budgets on a convex domain are exactly their tangent metric budgets at the probability-law/event level. The registered ceiling budget fails BOTH convexity and finite-tangent premises.

Those facts delimit the actual read MS25/FMM21 theorem scopes without denying their positive PRIOR machinery. They do not prove worldwide result novelty or source non-equivalence in all possible corollary senses. All-source priority remains **UNCLEAR**, and any candidate claiming the registered closure from these sources must supply the missing transformation of BOTH privacy budget and objective/class, not merely cite “continuous optimal Laplace”.

The registered LAW642, BRANCH-OLD578, new unreviewed Renyi/finite-family recovery/K25 proof-union packets and the Q26/DA26 comparison retain their own separate gates. No old review, metadata list or this owner-written comparison accepts any other successor. A fresh complete source/math/dependency/application review is required for this packet before parent use as an adopted comparison fact.

## 7. Process and original deadline

All mathematics is exact WRITTEN; no kernel check or scientific execution. Public source decimals were read as source text only, never evaluated or used as private proof glosses. All firstfive owner findings, SIXTH DISTINCT v111B written-exactness finding, SEPARATE077 continuation failure, v21 category correction, strict auxiliary214STOP/UNADMITTED and all parent/reviewer/source/import/N4 UNKNOWN/exit/old-arithmetic qualifications remain. No clean cognition/runtime/history or continuous-work assurance.

Only this exclusive owner root was written. No pinned/frozen/source/other-owner/parent file change, model/slot cutover, auxiliary graph work, nested/external model, publication or new GO. Same eighteen owners, science cutoff **2026-10-27T11:05:38-07:00**, delivery **2026-10-27T12:35:38-07:00**; actual substantive checkpoints at most30minutes while active. This is not early final-park or round closeout; the registered source/proof/priority residual continues.
