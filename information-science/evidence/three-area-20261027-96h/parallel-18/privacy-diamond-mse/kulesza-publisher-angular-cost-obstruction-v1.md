# Actual full-diamond laws: K25 angular averaging need not decrease squared-Euclidean cost

Owner **InfoResearch96h-2**, SAME info-1. Actual native clock immediately before writing: **Tue Oct 27 16:27:49 PDT 2026**. **AUTHOR-WRITTEN / UNREVIEWED** continuation inside the existing public-primary/written-comparison S1 scope. This is a precise SAME-INPUT source-method obstruction, not an optimality proof, printed-proof repair, novelty finding or new original-target completion.

## 1. Exact inputs and purpose

The only scientific source input is the already admitted exact publisher PDF: Kulesza–Suresh–Wang, PMLR258/AISTATS2025, native SHA256 `4e67a46d80e705df6b23a92e8fb88599a8b14c874af3f7b434a0ed217ca71df3`,1503464B/21pages. Its Section6.1 angular-averaging formula, Lemmas5–7 and all load-bearing operators were read visually on rendered PDF pages7–8 after the actual15:18:24 pre-body ACK. Those page-image pins are `ffe25143ade8a7b7cefe5bccc67c9d3daab4b448412e8cbea564494844edf45e` (page7) and `a3015edd05745b036537269a8da9a0823f1c1422ce080c269222522dacde608f` (page8).

The earlier complete source correspondence is `kulesza-publisher-correspondence-v1.md`, pin `de58e18705534388f4199ae194011cd3c8652d2a24c1d28975dcdee24a0f6e1d`. It identified the objective mismatch but did not assert any actual MSE sign for the averaging map. Here that exact next implication is decided on a universally quantified feasible family. No other paper, old K25 proof/review/reader, held source, old noise/control instance or private guide is used. Prior author/source exposure survives; no clean-cognition, blindness or independent-model claim.

Ordinary facts named and used: norm inequalities and triangle inequality; the elementary planar change-of-variables theorem and its displayed Jacobian; Tonelli for nonnegative integrals; integrability of polynomial times a decaying exponential; and the elementary two-copy covariance identity proved below. No scientific interpreter/Eval/calculator/CAS/program, numerical integral, selected epsilon/law/state/boundary trial, enumeration or replay was used.

The family is constructed directly from the ORIGINAL two norms and the source's averaging map for EVERY epsilon>0. It is a theorem-level actual-law obstruction, not a sanity test on an isolated parameter or a fixed experimental control. No normalizer or moment is evaluated numerically.

## 2. Exact registered class and the map, including its measure

Let `D={h in R^2:||h||_1<=1}`. For each arbitrary finite `epsilon>0`, let F_D(epsilon) be ALL Borel probability laws satisfying `P(E)<=exp(epsilon)P(E+h)` for every Borel event E and every h in the full CLOSED D. The objective is `integral ||x||_2^2 P(dx)`.

Parameterize the l1 unit sphere, apart from measure-zero edge endpoints, by

`theta_(sigma1,sigma2)(u)=(sigma1 u,sigma2(1-u))`, `0<u<1`, `sigma1,sigma2 in {+1,-1}`.

Give the four edges equal weights and u ordinary uniform measure: denote this probability measure by sigma. The map `(r,u) -> (sigma1 r u,sigma2 r(1-u))`, r>0, has absolute Jacobian r. Hence for every nonnegative measurable F,

`integral_(R^2) F(x)dx = 4 integral_0^infinity r E_sigma[F(r theta)] dr`.       (POL)

Axes/edge endpoints have planar measure zero and do not affect this identity. This proves the exact norm-polar measure used here without opening the source's external polar-coordinate citation.

The publisher's angular average becomes, for EVERY r>=0 and every l1-unit eta,

`A_D p(r eta)=E_sigma[p(r theta)]`.                                          (AVG)

At r=0 this is simply p(0) for the continuous family below. Thus the map is the same source-defined averaging operation, not an independently optimized radial law or a different rearrangement. It preserves the l1-radius marginal by (POL), but its angular coupling to squared-Euclidean cost is what must be checked.

## 3. The all-variable actual-law family

For EVERY epsilon>0 define

`Z_epsilon=integral_(R^2) exp(-epsilon||x||_2)dx`, `a_epsilon=1/Z_epsilon`,

`p_epsilon(x)=a_epsilon exp(-epsilon||x||_2)`.

This is an exact definition of a probability density; `0<Z_epsilon<infinity` follows from the usual exponential tail, not a computed normalizer. Let

`V=||theta||_2`, with theta distributed by the exact sigma above.

On every edge, `V^2=u^2+(1-u)^2`, so `1/sqrt(2)<=V<=1`. V is NOT sigma-almost-surely constant: the displayed continuous polynomial is nonconstant on the entire edge interval, and every nonempty open subinterval has positive sigma measure. No particular direction or u-value is selected or evaluated.

The source's ACTUAL averaged density is therefore

`pbar_epsilon(x)=a_epsilon E_sigma[exp(-epsilon ||x||_1 V)]`.                 (FAM)

It is finite, positive and continuous for all x, including the origin. Using (POL),

`integral pbar_epsilon dx = 4a_epsilon integral_0^infinity r E_sigma[e^(-epsilon r V)]dr`

`= integral p_epsilon dx =1`.

Both second moments are finite: `e^(-epsilon r V)<=e^(-epsilon r/sqrt(2))`, so their polar moment integrals are bounded by a fixed positive multiple of `integral_0^infinity r^3 e^(-epsilon r/sqrt(2))dr`, which is finite for every permitted epsilon. All following differences therefore subtract finite quantities; no infinity-minus-infinity step occurs.

## 4. BOTH laws satisfy the ORIGINAL full closed-shift/event constraints

For any x and ANY h in D, reverse triangle inequality and `||h||_2<=||h||_1<=1` give

`p_epsilon(x)/p_epsilon(x+h)=exp(epsilon(||x+h||_2-||x||_2))<=exp(epsilon)`.

Integrating over any Borel event proves the original measure inequality. No density ansatz is imposed on other feasible laws; this merely supplies one actual feasible law for every epsilon.

For the averaged density put `r=||x||_1`, `s=||x+h||_1`; then `|r-s|<=1`. For EVERY angular V in its support,

`exp(-epsilon r V)<=exp(epsilon |r-s| V) exp(-epsilon s V)`

`<=exp(epsilon)exp(-epsilon s V)`.

Averaging this SAME inequality over sigma proves `pbar_epsilon(x)<=exp(epsilon)pbar_epsilon(x+h)`. Integration again gives the full Borel/event inequality. These statements include the CLOSED boundary `||h||_1=1`, both directions of a shift, unbounded events and all original x. They use no marginal inverse, sampled angle or appeal to an unreconstructed optimum theorem.

Thus `P_epsilon` AND its actual source average `A_D(P_epsilon)` lie in the SAME F_D(epsilon), with normalization and finite original objective proved. This is not comparison of incompatible sensitivity geometries.

## 5. Exact cost-change identity and strict sign

For the actual original density, (POL) gives

`M_epsilon := E_(P_epsilon)||X||_2^2`

`=4a_epsilon integral_0^infinity r^3 E_sigma[V^2 e^(-epsilon r V)]dr`.

For its actual average, the radial value no longer depends on the output angle eta, while squared-Euclidean cost is `r^2||eta||_2^2`. Hence

`Mbar_epsilon := E_(A_D(P_epsilon))||X||_2^2`

`=4a_epsilon integral_0^infinity r^3 E_sigma[V^2] E_sigma[e^(-epsilon r V)]dr`.

Their difference is the exact SAME-LAW/SAME-MAP coupling

`Mbar_epsilon-M_epsilon = -4a_epsilon integral_0^infinity r^3 Cov_sigma(V^2,e^(-epsilon r V))dr`.       (COV)

For independent copies V,Vprime with this fixed angular distribution, elementary expansion proves

`2 Cov(f(V),g(V)) = E[(f(V)-f(Vprime))(g(V)-g(Vprime))]`.

At ANY r>0 and epsilon>0, `f(v)=v^2` is strictly increasing on the positive V-range while `g(v)=exp(-epsilon r v)` is strictly decreasing. The displayed product is nonpositive everywhere and strictly negative wherever `V!=Vprime`. Since V is nonconstant, that event has positive product measure. Therefore

`Cov_sigma(V^2,e^(-epsilon r V))<0` for EVERY r>0 and epsilon>0.

The integrand in the negative of (COV) is strictly positive at every positive r; its integral is finite by §3. Consequently

**`E_(A_D(P_epsilon))||X||_2^2 > E_(P_epsilon)||X||_2^2` for EVERY epsilon>0.**    (OBSTRUCTION)

No numerical epsilon, moment, angular value or gap is supplied. The sign is universal for this complete family and follows from the exact covariance identity, not from finitely many checks. No epsilon-uniform positive lower gap or asymptotic rate is claimed.

## 6. The exact source implication invalidated — and the ones not invalidated

This proves the precise theorem-level statement:

For every finite positive epsilon, there is an actual positive full-support finite-second-moment law in the registered full-diamond class whose ACTUAL K25 angular average remains in that SAME class but strictly INCREASES the registered squared-Euclidean objective.

Thus the proposed step “the source angular averaging preserves matching-norm utility, therefore it cannot increase squared-Euclidean error under diamond sensitivity” is false, not merely unproved, on these actual original objects. This is stronger than just observing that the cost is not a pointwise function of the l1 radius.

It is NOT a contradiction to the publication's actual theory. The paper's printed theoretical objective is the FIRST-power matching K-norm; its displayed averaging map preserves the entire K-radius marginal. Indeed (POL)/(AVG) here preserve every nonnegative l1-radial moment, including the squared-l1 moment, even while changing the different angularly weighted squared-Euclidean objective. No mean-norm theorem or empirical claim is refuted by (OBSTRUCTION).

Nor does the result:

- compare P_epsilon against the ENTIRE optimized staircase family or an all-law optimum;
- prove a new diamond/rounded transition or equality/unique optimizer;
- show the averaged exponential profile is an optimized source staircase;
- prove general impossibility of some other argument/source combination establishing the registered target;
- repair MDA NR-A/NR-D, publisher NR-K17/NR-K10, the source's attainment proof or a squared-cost global-optimality extension;
- establish source priority, worldwide absence, novelty or a major scientific contribution.

It is a precise actual-law METHOD-APPLICATION obstruction at the presently admitted source-comparison gate. The adopted original optimum remains at its earlier status/import cut and is not used as a premise. In particular a better law than this ONE averaged profile is not a new refutation of universal optimality of the BEST diamond-staircase family.

## 7. Controls and continuation boundary

All mathematics here is exact ordinary WRITTEN analysis from the admitted publisher formula and original two norms, with every actual normalization/privacy/moment/coupling implication displayed. It is not an executable/kernel/formal/human/configured-family certificate. No primary outside the packet, old K25 body, selected input/control, stopped review, PH mixed artifact/helper or ZERO guide was opened or used. No historical noninfluence or clean-cognition certificate.

All prior STOP/HOLD/ZERO/findings, N4 UNKNOWN/historical exit UNESTABLISHED and auxiliary214 STOP remain. The actual31m23s gap observed at16:26:09 is recorded separately in `checkpoint-003-actual-gap-and-angular-comparison-frontier-v1.json` (`4df58f81039f5d299c31f7d73f5358b5576fee0d07c516c92939b84671bcae6b`); this theorem does not backdate, excuse or hide it. No native scientific calculation, calculator/interpreter/Eval/CAS, enumeration/solver/replay/build/test/typechecker, nested agent/modelCLI/newGO, selected numeric/state/boundary probe, Git/delete/contact/infrastructure action. New deadline remains2026-10-31T21:23:27.000Z.

**END COMPLETE ANGULAR-COST OBSTRUCTION CANDIDATE — source-application gate only, actual full-D laws/all epsilon, UNREVIEWED.**
