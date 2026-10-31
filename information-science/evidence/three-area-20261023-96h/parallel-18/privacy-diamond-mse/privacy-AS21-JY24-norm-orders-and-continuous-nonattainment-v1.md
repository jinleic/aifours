# Registered privacy source comparison: intrinsic K-norm orders, unrestricted MSE and continuous-density nonattainment

Owner **InfoResearch96h-2**, original info-1. Actual `/bin/date` BEFORE this write: **Mon Oct 26 07:08:54 PDT 2026**. **NEW AUTHOR-WRITTEN bounded source/math/application candidate**, not an independent review or parent adoption. Exact WRITTEN symbolic analysis only; no scientific interpreter/eval/calculator/CAS/program/enumeration/replay/solver/CLI/nested agent, machine check or new GO.

## 0. Exact conclusion, positive prior and named new proof scope

Two genuine PRIOR sources optimize nonstandard sensitivity-aware noise:

- **AS21:** Awan–Slavković, [*Structure and Sensitivity in Differential Privacy: Comparing K-Norm Mechanisms*](https://doi.org/10.1080/01621459.2020.1773831), JASA116(534),935–954; actual formal text read here is [arXiv1801.09236v4](https://arxiv.org/html/1801.09236v4),31October2024.
- **JY24:** Joseph–Yu, [*Some Constructions of Private, Efficient, and Optimal K-Norm and Elliptic Gaussian Noise*](https://proceedings.mlr.press/v247/joseph24a.html), COLT2024/PMLR247,2723–2766; actual [publisher PDF](https://proceedings.mlr.press/v247/joseph24a/joseph24a.pdf).

These are POSITIVE PRIOR sensitivity geometry, norm-selection, containment/volume/conditional-variance ordering and efficient sampling/elliptic-noise results. Such generic geometry/optimization ideas must not be counted as discoveries of this lane.

The actual read “optimal K-norm” statements do NOT optimize unrestricted all-Borel full-diamond squared-Euclidean MSE. AS21 explicitly warns that its intrinsic orders need not optimize unconditional marginal variance or ordinary losses. This is a precise model/objective/class reading, not a title-only different-family dismissal.

**New WRITTEN registered-family fact, IMPORTING LAW642 exactly:** at EVERY finite epsilon>0, the original optimal law has NO continuous density version. Therefore no continuous exponential K-norm density attains its unrestricted value. Nevertheless the infimum over ALL positive smooth full-D epsilon-private densities is EXACTLY the same V(epsilon), via exact-privacy Gaussian POSTPROCESSING convolution with cost V+2sigma². Thus nonmembership/nonattainment does NOT imply a positive infimum gap, and this proof does NOT compute the infimum over exponential K-norm mechanisms.

No new mechanism/value/novelty claim, field-wide absence theorem, source falsity, all-creative-corollary inequivalence or model/slot cutover follows. Priority remains UNCLEAR.

## 1. AS21 actual version, read windows and formal orders

### 1.1 Metadata and coverage, not backdated source bytes

The actual [Crossref DOI record](https://api.crossref.org/works/10.1080/01621459.2020.1773831) reports JASA116(534),935–954, online20July2020 and print3April2021. Its DOI creation is28May2020. These are publication metadata, NOT proof that the31October2024 arXivv4 formal text is byte-identical to the original journal article. No such version equality was checked.

The HTML reader is artifact34903, SHA256 `663021fb5633f3c664f98e7610c674144b921d468e93fb4adbe364911ead6e90`,187717bytes,1504 newline characters/1505 rendered logical lines. ACTUAL selected reads were1–188,340–391 and635–655. The initial fetch displayed ONLY1–188 due the output-size cap; it is NOT recorded as1–300 or a whole1505-line read. The complete source proofs in its technical appendix, other versions, algorithms, simulations and applications were NOT reconstructed here.

### 1.2 Actual theorem class and actual objective

Proposition2.8 defines the K-norm EXPONENTIAL family, with density of the form

    f_K(v)=normalizer^(-1)
                    exp(-(epsilon/Delta_K)||v||_K).

Definition3.1 orders TWO such mechanisms by inclusion of their scaled norm balls, or by their volumes. Theorem3.17 compares variances CONDITIONAL on the noise lying in a specified one-dimensional direction. Theorem3.19 says the sensitivity hull's K-norm mechanism is preferred in containment and volume order.

Theorem3.19's quantifier ranges over OTHER K-norm exponential mechanisms, not every additive private Borel law. Its conditional directional variance is not the registered unconditional total second moment. The source's “optimal K-mech” language is explicitly justified by its stated intrinsic criteria; no unrestricted mean-squared-noise theorem is hidden in that name.

Section6, actually read635–655, gives an explicit author-described caution that norm-ball containment need NOT optimize unconditional marginal variance or expected l1/l2/linfinity loss. Its reported example uses simulations; the printed numbers are NOT replayed, verified or used as premises in this packet. The logical scope limitation is in the source's own stated comparison problem, independent of the empirical example's correctness.

No source theorem is refuted. Its positive intrinsic-order result remains PRIOR and relevant; translating it into the registered exact MSE objective would require an additional genuine theorem rather than replacing “conditional” with “unconditional.”

## 2. JY24 actual pure-DP and Gaussian class boundaries

The actual publisher record identifies30June2024 publication and PMLR247. The retained publisher-PDF reader artifact34886 has SHA256 `c540615ff0b3aa46fe4950c81c8b7edbf7cf95874c3ebec8f7d3404bb67cffe1`,144521bytes,1147 newline characters/1148 rendered logical lines.

ONLY displayed1–300 were read in this pass, plus a targeted bibliography match at386 identifying AS21. This includes its actual abstract/introduction, formal K-norm Lemmas7–11, Gaussian/CDP Lemmas12–13 and opening problem-specific results. It is NOT a full44-page/1148-line proof/algorithm audit. The publisher-PDF extraction's cover metadata is not silently reconciled into a new PDF-byte identity claim.

Its pure-DP mechanism is the same norm-EXPONENTIAL density. Lemma11 explicitly imports AS21Theorem3.19 containment/volume ordering for the induced sensitivity norm. It supplies practical samplers for the specified Sum/Count/Vote sensitivity bodies; no all-noise MSE minimization is stated by that lemma.

The second class is elliptic GAUSSIAN noise under concentrated DP, with an enclosing-ellipse objective tied to expected squared norm. Its use of an MSE criterion in THAT Gaussian problem does not make the pure-DP K-norm containment theorem an unrestricted MSE theorem. Source algorithm runtimes, code, samplers, plots, experiments and transitive proofs remain NOT_RECONSTRUCTED/UNEXERCISED here.

The positive contribution is substantial PRIOR: sensitivity-aware non-lp geometry, efficient norm-ball sampling and explicit elliptic Gaussian shapes. No generic “geometry-aware noise is new” or “optimal” headline ambiguity should erase this ancestry.

## 3. Named LAW642 import for the NEW registered-family proof

`privacy-all-law-optimum-self-contained-v1.md`,642LF, SHA256 `957cab2bcf3eff1860ff9f4b5a1e5838708aceaf894a97fdc2c5244c3e7d8e53`, at `RUN/privacy-all-law-self-contained-parent-v1.md`, SHA256 `c08f6353f121ef9e35da0e9d5e8ec9c87b0da838be0d1adf38b807010a1cd979`.

Exactly imported: for EVERY finite epsilon>0, the original ALL-Borel additive full-CLOSED-unit-l1-diamond problem with cost `J(mu)=integral|z|2² dmu` has finite positive value V(epsilon), a UNIQUE optimal LAW mu_epsilon, and a canonical a.e. density

    f_epsilon(z)=Z^(-1)b^n_S(z), b=exp(-epsilon)∈(0,1),
    n_S(z)=min{k>=0 integer:z∈S+kD},

for a nonempty compact S and positive finite Z. This is not merely a selected symmetric optimizer/uniqueness input. No old578LF scalar root, Galois, numerical table or machine output is imported.

The new proof additionally uses only elementary compact-set maxima, continuity, convolution/Tonelli and centered Gaussian moments. It does NOT assume AS21/JY24 correctness, newly accepted K25/MDA/EG source proofs or the joint finite-family/order theorem. The main registered all-law result is an explicit named premise, not rediscovered by the source comparison.

## 4. Exact diagonal tail forbids EVERY continuous density version

Put `c=max_(s∈S)(s1+s2)` and choose B larger than0 and BOTH coordinate maxima of S. Whenever x>B and y>B,

    dist_1((x,y),S)=min_(s∈S)[x+y-s1-s2]=x+y-c.

Compactness attains the distance, and closed-D membership is exactly `dist_1(z,S)<=k`. Therefore throughout that quadrant,

    f_epsilon(x,y)=Z^(-1)b^ceil(x+y-c).                    (DIAG)

Choose an integer ell large enough that c+ell>2B, and a point z0 on the line x+y=c+ell inside the quadrant. Choose a small open square around z0 remaining in the quadrant and satisfying `|x+y-c-ell|<1/2`. Its two open diagonal halves have positive area. On the lower half the density is `C1=Z^(-1)b^ell` a.e.; on the upper half it is `C2=Z^(-1)b^(ell+1)` a.e., with C1≠C2.

Suppose a CONTINUOUS density g represented the SAME LAW. Densities of one law agree a.e. On either open half, continuity and a.e. equality to a constant force g to equal that constant EVERYWHERE on the half: otherwise a nonzero deviation would persist on a positive-volume open neighborhood. Approaching z0 from both halves would then give g(z0)=C1=C2, contradiction.

Thus

    mu_epsilon has NO continuous density version.          (NO_CONT_VERSION)

This is a probability-LAW statement, not a complaint about arbitrary point assignments on the null jump line. It works for every nonempty compact S and every finite epsilon>0 without evaluating any scalar parameter.

Consequently no original epsilon-private law admitting a continuous density can have J<=V(epsilon). Such a law would be an original optimum by the definition of V and therefore equal mu_epsilon by ALL-law uniqueness, contradicting NO_CONT_VERSION.

For every genuine norm H and finite positive rate a, the density proportional to `exp(-a||z||_H)` is continuous. Therefore ANY such mechanism that is genuinely full-D epsilon-private fails to ATTAIN the original value V(epsilon). This does NOT claim all choices are infeasible, compute their best value or prove their infimum is strictly separated from V.

## 5. Exact-privacy smooth recovery shows why nonattainment is NOT a value gap

Let sigma>0, let Z_sigma be an independent centered Gaussian on R² with covariance sigma² I, and define

    nu_sigma=mu_epsilon * N(0,sigma² I).

This is POSTPROCESSING by independent added noise, not a claim that a Gaussian alone satisfies finite-epsilon pure DP. For EVERY Borel A and EVERY h∈FULL CLOSED D, positive Tonelli and mu_epsilon's event privacy give

    nu_sigma(A)=integral mu_epsilon(A-w)g_sigma(w)dw
       <=exp(epsilon)integral mu_epsilon(A+h-w)g_sigma(w)dw
       =exp(epsilon)nu_sigma(A+h).

Thus exact ORIGINAL epsilon privacy is preserved, including slanted boundary shifts.

The density `g_sigma*mu_epsilon` is everywhere positive and C-infinity: g_sigma is positive, all its derivatives are bounded continuous for fixed sigma, and their integration against a probability measure permits differentiation by dominated convergence. No source sampler or scientific Gaussian computation is needed.

LAW642's finite second moment gives integrable first moments by Cauchy–Schwarz. Since Z_sigma is centered and independent, the cross term vanishes EXACTLY and

    J(nu_sigma)=J(mu_epsilon)+E|Z_sigma|2²
                =V(epsilon)+2sigma².                    (SMOOTH_COST)

Therefore

    inf{J(nu):nu has a positive C-infinity density
               and is full-D epsilon-private}=V(epsilon).

NO_CONT_VERSION proves this infimum is NOT attained in the smooth class, or even among all continuous-density feasible laws. The equality of infima is supplied by the actual full-privacy/cost construction, not inferred merely from topological density or weak convergence.

This recovery is over ALL smooth private densities. It is NOT a recovery theorem inside the much smaller family of exponential K-norm mechanisms, so no equality of THEIR infimum with V is asserted. It also does not make a continuous law an exact original optimizer by taking sigma=0: that limiting law is exactly the discontinuous-density optimum.

## 6. Bounded additional DOI surface and unresolved leads

A new full-text DataCite query

    "differential privacy" AND additive
        AND (quadratic OR "mean squared")

returned18 DOI/title/date entries on1page. ALL metadata1–300 and ending301–306 were read; metadata reader artifact34885 SHA256 `d012b13c01a278b9120faf5c2bd2d16c820db04c78bb82eaa5cdef6719a0d4be`. A separate descriptions-rich response had455 rendered logical lines but ONLY its first90 were displayed/read; it is NOT counted as a complete abstract/full-paper screen.

Exact metadata DOI inventory:

    10.5281/zenodo.23126960;10.5281/zenodo.23126959;
    10.5281/zenodo.23045340;10.5281/zenodo.23045339;
    10.5281/zenodo.22067320;10.5281/zenodo.22777523;
    10.5281/zenodo.22775439;10.5281/zenodo.22739333;
    10.5281/zenodo.22739334;10.5281/zenodo.22067321;
    10.48550/arxiv.2606.21107;10.48550/arxiv.2604.10423;
    10.48550/arxiv.2203.13377;10.48550/arxiv.2302.03511;
    10.48550/arxiv.2302.00766;10.48550/arxiv.2301.06412;
    10.48550/arxiv.2207.00420;10.48550/arxiv.1908.04920.

This query has irrelevant defensive-publication/federated/privacy matches; its finite output is not a mathematical-instance index or worldwide exhaustion.

[DataCite22739333](https://api.datacite.org/dois/10.5281/zenodo.22739333) supplies actual metadata/abstract for Christian LeDeBlis, *Private Selection under Scalar Access: Allocation, Noise Primitives, and the Limits of Scalar Observation*, registered **2026-09-14T00:10:12.000Z**. Its abstract expressly labels access-model results and reports formal/Lean claims with caveats. The linked [version record22739334](https://zenodo.org/records/22739334) returned403. NO manuscript/formal proof was read or checked; the abstract is NOT a theorem-level exclusion or formal acceptance, and no lower-bound claim from it is imported here.

The arXiv API abstract for [2606.21107, *Enhancing Differentially Private Mechanisms via Empirical Bayes*](https://arxiv.org/abs/2606.21107) was read, but its formal body was not. No theorem-level applicability conclusion is drawn from the abstract. The earlier LCR/Cactus source is an already known positive PRIOR interface, not a new contribution or a reason to reopen stopped auxiliary graph work.

One web-search result returned generated explanatory synthesis rather than only source links. It was treated ONLY as URL discovery, never a mathematical premise, source proof or verification. All class/objective statements above come from actual primary definitions/theorems; the new family proof is supplied explicitly at LAW642.

## 7. Exact disposition, remaining gap and unchanged process

The new comparison distinguishes intrinsic norm-order optimality from unconditional all-law MSE WITHOUT denying sensitivity-aware geometric ancestry. The new registered proof shows a sharp continuous-density ATTAINMENT boundary and a separate EXACT smooth-INFIMUM equality. Neither result proves a positive K-norm-family infimum gap or global prior-result non-equivalence.

A fresh COMPLETE source/mathematics/dependency/application gate is required for this new packet. The LAW642 theorem is a named import; no reviewer/parent source headline or prior same-topic gate accepts the new nonattainment/recovery proof. Independent worldwide source/priority/novelty clearance remains unperformed/UNCLEAR, not passed by bounded searches.

All firstfive owner findings, SIXTH DISTINCT v111B written-exactness finding, SEPARATE077 continuation failure, v21 category correction, strict auxiliary214STOP/UNADMITTED and every parent/reviewer/source/import/N4UNKNOWN/exit/old-arithmetic qualification remain. No clean cognition/runtime/history, continuous-work census, stronger human/family/cross-vendor/formal/kernel/executable/novelty/publication assurance or new GO. Exclusive own root; frozen sources/ACKs/parents/other owners unchanged.

Same eighteen owners; science cutoff **2026-10-27T11:05:38-07:00**, delivery **2026-10-27T12:35:38-07:00**; active actual substantive checkpoints at most30minutes. This is not early final-park or round closeout; the authorized registered source/priority residual continues.
