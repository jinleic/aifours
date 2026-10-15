# References and applicability audit

Read/retrieval date: 2026-10-14 PT. Only the public material and exact local
declarations actually inspected below are used. No unavailable theorem is
treated as an established premise. All source target/corpus/cache files were
read only. Mathematical results in `mathematical-progress.md` are independently
argued there; historical priority is not claimed.

## Existing target, inspected in this attempt

Root: `/Users/jinleic/jinleic-workspace/ai4s/m-estimator-sample-augmentation`.

| File | Actual use | SHA256 at inspection |
|---|---|---|
| README.md | Original quantifiers, unique-minimizer scope, status distinctions | `7243b98966666fe8555f1245840493777759795c62761a906222c4408a448da8` |
| proof.md | Full Theorem 9, sections 9--11; Theorems 4A, 5, 7, 8 and prior nested attack obstruction | `69067c247a410ce26fcfa96b73dce154173962c76a30dcd95322c99461b25991` |
| sources/reading-notes.md | Prior source access boundaries, precise preview limitations | `71c359818a9138756b4487a43e8d87fbdf106fcadb268dca7d211764bb070e82` |

Theorem 9's finite variance, global lower/upper curvature, same-law replicate,
population center theta_n, and degenerate-law case are preserved in the
progress report. Theorem 4A prevents a universal Gram necessity claim for
LAD with atoms. Theorem 7 is a checked Gaussian/finite-location-information
necessity reduction, not general convex-loss sufficiency. Theorem 8 is an
L1 necessity result, not sufficiency. The old triangular construction remains
excluded from the current target.

## Zhao--Rao--Chen (1993): incomplete primary access

L. C. Zhao, C. Radhakrishna Rao, X. R. Chen, *A Note on the Consistency of
M-Estimates in Linear Models*, pp. 359--367 in *Stochastic Processes*.
[Primary publisher chapter](https://link.springer.com/chapter/10.1007/978-1-4615-7909-0_41).
DOI: 10.1007/978-1-4615-7909-0_41.

The publisher landing page and its two-page public preview were obtained.
The actual following theorem/proof pages were **not obtained**. A direct
full-PDF request returned HTTP 200 **HTML**, redirected to the access chapter
page; a 200 response is not evidence of PDF access. Its entire response,
redirect, content type, byte count, and hash are retained in
`evidence/source-fetch-20261014T192609.961451Z/`.

The fresh preview is `zhao-preview.pdf` in that directory, SHA256
`79e3e854f3ae52a581c0dec9e2e1924930ce1e952b29b52cd649364a24c740a5`.
The existing preview text and the actual page-360 image
`sources/zhao-rao-chen-1993-preview-page2.png` were independently opened.
The latter visually confirms:

- A1: a convex loss and a chosen subgradient between its one-sided derivatives;
- A2: centered score, local lower bound
  `|E psi(e+u)| >= c_0 |u|`, and locally bounded
  `E psi(e+u)^2 <= c_1` for `|u| < Delta`;
- A3: `S_n^{-1} -> 0`.

These are visible assumptions, not a reconstructed full theorem. The text
announces Gram-only weak sufficiency with regularity, but no exact theorem
statement, additional qualifications, proof, or application to the full
frozen goal is asserted. The current self-contained sufficiency argument
has the explicit additional vanishing-leverage assumption.

Exact-title, DOI, author/year, book-title, and full-PDF searches did not expose
an accessible complete chapter. OpenAlex was used only as a location finder;
its saved record lists no open repository full text. This does not prove
that no complete copy exists elsewhere. A web-tool screenshot request for
preview page 360 timed out; the local page image was then inspected directly.

## Bai--Wu (1997): metadata, no theorem pages

Z. D. Bai and Y. Wu, *On necessary conditions for the weak consistency of
minimum L1-norm estimates in linear models*, *Statistics & Probability
Letters* 34(2), 193--199, June 2, 1997.
[Primary publisher article](https://www.sciencedirect.com/science/article/pii/S0167715296001824).
DOI: 10.1016/S0167-7152(96)00182-4.

The public publisher article record/abstract was encountered, but the complete
article was **not obtained**. Direct `pdfft` retrieval returned HTTP 403 HTML.
The public article API returned HTTP 200 XML (1875 bytes), providing metadata
and no theorem text. These exact responses and hashes are preserved in the
same source-fetch directory. The OpenAlex record was inspected only for
public manuscript locations and supplied no open full text.

Search snippets mentioning an L1 design condition are not used as a theorem.
In particular, no median, tail, atom, symmetry, or density assumption of this
paper has been invented. The only L1 necessity argument referred to here is
the independently checked existing target Theorem 8, with its own explicit
two-sided-law hypothesis.

## Other public research screening

The primary publisher preview of Berlinet--Liese--Vajda (2000),
[DOI 10.1016/S0378-3758(99)00218-9](https://www.sciencedirect.com/science/article/pii/S0378375899002189),
was screened. Its visible introduction restricts regressors to a compact
set and allows triangular schemes; its advertised necessary/sufficient
theory is not substituted for arbitrary nested unbounded designs. No
unseen formula or theorem from this article is a proof dependency.

Google Books and exact-title/author searches were access/location searches,
not mathematical premises. Neither a search result count nor this source
access failure certifies that the frozen formulation is open worldwide.

## Local mathematics corpus: actual declarations and dependencies

Root: `/Users/jinleic/jinleic-workspace/math`. No corpus file was copied into
the cache or built, and **no OAI import** appears in `Formal.lean`.

| Inspected declaration | Actual hypotheses/dependencies | Applicability to this attempt |
|---|---|---|
| `OAI.FixedClauseThreshold.uniform_chebyshev`, Probability/RandomSAT/Concentration.lean, lines 94--104 | A finite nonempty uniform sample space; `uniformProbability`, `uniformMean`, `uniformVariance`; comparison of an indicator with a squared deviation | The indicator/second-moment-to-tail proof pattern helped choose the stochastic component. It is not a theorem for arbitrary iid errors. The final proof uses genuine probability measures and Mathlib Markov/variance results instead. |
| `OAI.NoiselessRegression.measurePreserving_pi_prefix`, Probability/GaussianRegression/Transfer.lean, lines 26--35 | A probability measure nu, finite product measures, t <= T; proves prefix marginalization using `Measure.ext_of_lintegral`, `lintegral_map`, and its imported `lintegral_pi_prefix` | A genuine finite-product marginalization pattern, useful for distinguishing same-law replication/prefixes. Not needed as an import. Its surrounding regression is random-design and noiseless and supplies no fixed-design M-estimator theorem. |
| `OAI.SK.Analytic.stronglyConvex_linear_variance_le`, Probability/SKBarriers/Calculus/StronglyConvexVariance.lean, lines 20--43 | A C2 potential, positive Hessian bound on a fiber, a linear functional, fiber invariance, integrability of exponential Gibbs density and its moments | Inapplicable to the sampling distribution of the estimator. No conversion from the likelihood criterion to a Gibbs law is made. |
| `OAI.SK.Analytic.hessian_comp_linear`, same file, lines 49--58 | C2 function and continuous linear map; chain rule for second Frechet derivatives | The chain-rule form matches the written finite-sample Hessian. No OAI calculus assertion is imported or used to hide differentiability assumptions. |
| `OAI.TruffetV4Counterexample.finite_execution_not_optimal`, Optimization/Tropical/TruffetCounterexample.lean, lines 126--143 | Explicit tropical states and their previously checked forced transitions, feasibility, and costs | Exact witness/control pattern only. It does not provide a statistical counterexample. The present finite negative control checks a necessary variance constant, without being presented as asymptotic evidence. |

The four files' actual contents and import lines were read, including the
finite variance proof's indicator argument and the Gibbs integrability
requirements. A targeted corpus search for Huber/M-estimation declarations
found no directly applicable theorem used here; this is not an exhaustive
coverage claim. The broad `import Mathlib` in the SK source is not copied.

## Direct Mathlib declarations used and inspected

Read-only cache root:
`/Users/jinleic/jinleic-workspace/scratch/rh-quasi-lean-2026-10-07/lean`.
Mathlib source subroot: `.lake/packages/mathlib/Mathlib/`.

- `Probability/Moments/Variance.lean`: `variance_eq_sub`,
  `variance_sub_const`, `variance_const_mul`,
  `ProbabilityTheory.IndepFun.variance_sum`, and the genuine Chebyshev
  variants. The final weighted second moment uses L2 integrability,
  centered variables, and pairwise independence; those assumptions are
  retained explicitly. A binary indicator's L2 membership is also derived.
- `Probability/Independence/Basic.lean`: `IndepFun.comp`, used for fixed
  affine transformations of independent observations. No independence
  between an observation's own curvature indicator and its score is assumed.
- `MeasureTheory/Integral/Bochner/Basic.lean`:
  `integral_finsetSum`, `integral_const_mul`,
  `mul_meas_ge_le_integral_of_nonneg`. The last is the real-probability
  Markov bound actually applied to the integrable Frobenius square.
- `MeasureTheory/Function/LpSeminorm/{Basic,TriangleInequality}.lean`:
  `MemLp.of_bound`, `memLp_finsetSum`, `memLp_finsetSum'`.
  These give integrability from bounded binary observations and Lipschitz
  contrasts, without imposing an L2 condition on epsilon itself.
- `MeasureTheory/Function/L2Space.lean`: `MemLp.integrable_sq`.
- `Analysis/Convex/Function.lean`: the full `ConvexOn` definition, used in
  the radial contraction proof locating every minimizer inside a positive
  criterion sphere. Positivity on the sphere is not a hypothesis of the
  original target; it is supplied by the separate written stochastic bound.
- `Topology/MetricSpace/Lipschitz.lean`: `LipschitzWith.dist_le_mul`, used
  to bound the loss contrast by L|t| under an arbitrary probability law.

The initial failed import `Mathlib.Tactic.Nlinarith` was corrected to the
actually present cached `Mathlib.Tactic.Linarith`; no dependencies were
updated or built. All failed and successful elaboration receipts are retained
under `evidence/lean-attempts/`.

## Claims and acceptance boundary

`claims.json` lists exact fully qualified formal declarations, assumptions,
scope, actual printed axioms, and negative-control details. Written mathematics
is separately labeled. Standard algebra, variance, convex localization, and
Huber inequalities are formalizations, not claims of historical novelty.
The smooth infimum-zero-curvature/infinite-error-variance case is a real
extension of this target's existing proved subclass, with explicit extra
design/score assumptions; it does not solve the full target.

The actor invokes neither Comparator nor nanoda nor another reviewer CLI.
Only the supplied runner may supply the independent reviewer verdict.
