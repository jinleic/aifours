# Bounded source audit of the strict mixed-geometry comparison

Observed clock before creation: **2026-10-23T15:02:31-0700**. Scope: source/status gate for the mathematical candidate [proof-diamond-staircase-counterexample-v1.md](proof-diamond-staircase-counterexample-v1.md), SHA-256 `d2f7771852c05edb32905b2d99c42a0403faecb42c08a16a90e8df1662d8c148`. Mandatory companion: [prior-mechanism addendum](proof-diamond-staircase-counterexample-ADDENDUM-1-prior-mechanism.md), SHA-256 `a874807c869567cde7616ec670fbadada55bcff85e2a4c4d2503bda3685bef5e`.

**Disposition: the general mechanism class is PRIOR PUBLISHED; no earlier matched strict comparison was located within the sources and interfaces actually read below. NOVELTY_UNCLEAR remains operative.** This is not a worldwide exhaustive audit, a peer mathematical verdict, or permission to publish/contact authors.

## 1. What is already prior and what alone remains a possible delta

Soria-Comas–Domingo-Ferrer 2013, DOI [10.1016/j.ins.2013.07.004](https://doi.org/10.1016/j.ins.2013.07.004), Section 6's arbitrary coordinate-downward core and successive Minkowski reachability shells already contain our octagonal-core law. The exact institutional accepted manuscript was retrieved, its Theorem 13 image opened, and the whole Section 6, conclusion, Appendix theorem proof and reference list read. Source pins and the printed-index caveat are in the mandatory addendum. No theorem-level optimality assertion from that paper is used by our proof.

The only candidate delta is therefore the exact comparison

`J_known-class-octagonal-instance < (33/50)sqrt(b) < (333/500)sqrt(b) <= min_gamma J_diamond-staircase(gamma)`

for the **same** full continuous diamond sensitivity, squared-Euclidean loss, b=exp(-epsilon)<=10^-16. A new parameterization of a known mechanism, a comparison only with Laplace, or a numerically chosen gamma would not be that delta.

The old paper's Definition 5 is minimality under a concentration partial order, not a claim that every core minimizes every expected loss. Its actual multivariate example uses rectangular sensitivity and rectangular core and compares coordinate variances and confidence regions with Laplace. The exact optimized diamond-family comparison is absent from that read paper. Its reference list does not contain the later December 2, 2013 Geng–Viswanath manuscript.

## 2. Primary statement being addressed

[arXiv:1312.0655](https://arxiv.org/abs/1312.0655), Geng–Viswanath, **published December 2, 2013** according to the actual arXiv record. Section II imposes the full l1-sensitivity translation condition. Theorem 1 establishes the d=2 l1-cost case. The final Section III paragraph literally conjectures that the same correlated multidimensional f_gamma family is optimal for d=2 and `L(x)=||x||_2^2`, and warns that their l1-layer averaging does not prove it. The actual model, theorem, f_gamma and conjecture paragraph were read.

The conjecture here is that exact f_gamma family, not an assertion that every conceivable geometric staircase family is suboptimal. Our own density is in a broader already known staircase-shaped class.

## 3. Later strongest optimality interfaces actually checked

| Source | Actual read scope | Model/objective boundary relative to this comparison |
|---|---|---|
| [GKOV, IEEE JSTSP 2015](https://pramodv.ece.illinois.edu/pubs/GKOV.pdf), DOI10.1109/JSTSP.2015.2425831 | Abstract, model/theorem discussion and **actual printed p.1179 image** | Equation(9) uses l1 sensitivity; equation(10)/Theorem1 use l1 loss. Not the mixed squared-Euclidean comparison. The universal wording in the abstract is not substituted for its theorem. |
| [Kulesza–Suresh–Wang, AISTATS2025](https://proceedings.mlr.press/v258/kulesza25a.html) | Actual PDF Sections1–3, Definitions3/5, Theorems1/2; public code README | Theoretical utility and sensitivity use the **same K norm**. Other metrics are empirical comparisons, not the required global mixed-cost theorem. |
| [Melbourne–Diaz–Asoodeh, arXiv:2601.14597](https://arxiv.org/html/2601.14597), January21 2026 | Abstract/introduction, additive model, Assumption1, theorem/level-set interfaces, reference13 | Requires `Phi(x)=varphi(||x||)` for the **same sensitivity norm**. Squared Euclidean loss is not l1-radial. Theorem3 already treats geometric level-set expansion; that idea is not new. This paper expressly cites SCDF2013. |
| [Selvi–Liu–Wiesemann, Differential Privacy via Distributionally Robust Optimization](https://arxiv.org/html/2304.12681v3), accepted manuscript also [Imperial record](https://hdl.handle.net/10044/1/120024), DOI10.1287/opre.2023.0218 | Repository abstract and actual arXiv introduction/model interface; the introduction expressly says **scalar query `f:D -> R`** | Strong nonasymptotic optimization guarantees and converging primal/dual bounds for a scalar query. This is not a discovered planar diamond-staircase refutation. No claim of a full read of every appendix or application is made. |
| [Fernandes–McIver–Morgan, arXiv:2105.07176](https://arxiv.org/html/2105.07176), 2021 | Abstract and actual Definitions1/eq.(4), continuous-result scope in SectionII-G | Their continuous query result is on a scalar interval with **metric privacy proportional to Euclidean distance for every input pair** and Bayesian remapping utility. It is not the fixed factor for all shifts in a two-dimensional diamond. |
| [Koufogiannis–Han–Pappas, arXiv:1504.00065](https://arxiv.org/abs/1504.00065), 2015 | Actual abstract | Says **Lipschitz privacy**, a stronger variant, for Laplace MSE optimality. Abstract alone is not a complete hypothesis audit; it supplies no authenticated closure of the present fixed-neighborhood pure-DP conjecture. |
| [Alghamdi et al., Cactus Mechanisms, arXiv:2207.00420](https://arxiv.org/abs/2207.00420), 2022 | Actual abstract | Large-number-of-compositions objective is KL-divergence minimization subject to noise cost, not single-shot fixed-epsilon full-diamond MSE. |
| [Alghamdi et al., Optimal Multidimensional Differentially Private Mechanisms in the Large-Composition Regime](https://asu.elsevierpure.com/en/publications/optimal-multidimensional-differentially-private-mechanisms-in-the/), ISIT2023, DOI10.1109/ISIT54713.2023.10206658 | Actual university publication abstract | Explicitly spherically symmetric cost with **l2 sensitivity**, and an asymptotic composition/KL objective. Not the mixed planar single-shot model. |
| [Wei–Bienstock–Polychroniadou, ICML2026](https://proceedings.mlr.press/v306/wei26a.html) | Actual proceedings abstract | High-dimensional Gaussian asymptotics and spherical generalized-gamma alternatives. The abstract does not establish the frozen full-diamond pure-DP comparison. No full-text exclusion theorem is claimed from this abstract. |
| [Qin et al., arXiv:2203.10323](https://arxiv.org/abs/2203.10323), 2022 | Actual abstract | Discrete random noise and discretely distributed data, not all continuous shifts. |
| [Chen–Pal–Golubchik, IEEE SPW2016](https://qed.usc.edu/papers/ChenPG16.pdf) | Actual abstract/introduction/model | Exploratory scalar-output, side-information/Bayesian experiments and alternative utility assumptions; not a proof of the exact planar comparison. |
| [Wang et al., Minkowski Response / PIC, arXiv:2406.18145v3](https://changyudong.site/assets/pdf/usenix25.pdf), January30 2025 | Actual abstract/introduction and local/shuffle model | Important prior geometric randomizer, but bounded-input local DP with shuffle amplification, not a translation-independent law over the whole plane for the prescribed diamond. No claim to originate the term Minkowski mechanism is made. |

The primary source boundaries, not search-engine summaries saying “arbitrary norms,” determine overlap. In particular changing sensitivity from l1 to l2 or using a distance-proportional privacy requirement would change the problem.

## 4. Citation and public-claim coverage

A public [OpenAlex citing-work query](https://api.openalex.org/works?filter=cites:W2091913942&per-page=100&select=id,doi,title,publication_year,open_access) returned **75 indexed citing works** for SCDF2013. Their returned titles/DOIs/year/access routes were screened; the most directly relevant mechanism-optimality titles motivated the additional interfaces above. **Those 75 manuscripts were not all read.** Citation indexing may omit newer preprints and other relevant papers, so the count is not a completeness certificate. For example the actual January2026 paper's reference13 directly confirms its citation even apart from any index coverage.

The earlier selection screen also actually checked:

- the current EulerSolve full papers listing and canonical matched SOF source (no privacy/staircase listing match returned);
- retained remote/current-local openai/math catalogs, with their observed hashes and unrelated staircase matches recorded in the selection's linked screen;
- the public GoogleResearch generalized-staircase implementation README and current AIM problem inventory;
- targeted later-claim and repository queries for mixed norms, squared-Euclidean loss, Minkowski sums/level sets, nonradial noise, and named conjecture/counterexample terms.

Those searches found no additional **matched strict comparison** that was then authenticated. Many returned abstracts concern different geometries, scalar queries, local privacy, composition limits or stronger metric privacy; irrelevant hits were not treated as negative evidence. Search misses do not establish absence of prior art.

## 5. Current scientific and priority disposition

1. **Mechanism novelty: NO.** It is an instance of SCDF2013's published construction; geometric-level-set privacy has additional explicit prior treatment.
2. **Mathematical comparison:** still CANDIDATE at this audit's creation; exact independent and parent verdicts must be attached separately when actually returned/read.
3. **Comparison priority/novelty:** **NOVELTY_UNCLEAR**, with no matched earlier comparison found in the bounded read set. Not globally certified and not publishability assessed.
4. **Status of literal conjecture:** conditional on the comparison proof, false in every epsilon>=16log10. This is the mathematical consequence, not a source-search verdict.
5. **Execution:** no scientific code, sampling, solver, exact replay, syntax check or formal proof assistant was run. Native source extraction/rendering, metadata clocks/hashes and read-only web/repository access only.

A later matched primary comparison would retire the novelty claim without refuting our independent inequalities. The exact unrestricted V and any optimal-law characterization remain consequential scientific obligations within this same model, not new counted problems.
