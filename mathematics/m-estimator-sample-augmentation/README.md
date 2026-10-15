# M-estimator sample augmentation

**Outcome: broad formalization (c) refuted — written proof, parent-audited, independent Opus referee correct (minor fixes applied). Not Lean-certified; not HMZ-accepted.** The fixed nested p=2 construction has unique minimizers and one uniformly curved C^2 loss, but requires **E|epsilon|=infinity**, hence infinite variance. Cui's unspecified regular-error question and the finite-moment general-convex regime remain open beyond Theorems 9/10. Theorem 9's finite-variance, independent same-law result remains valid without score-centering; Theorem 10 supplies a written Gaussian bounded-score regime with an equivariant original estimator. Thirty Lean components compile, not the full asymptotic arguments. The actual 3600-second HMZ run ended `stopped` without its reviewer verdict; the separate no-tools Opus referee's **correct** verdict does not convert that run to RLAR acceptance. [Evidence, five fixes and both proof hashes](hmz-lean-20261014/independent-referee-resolution.json). All dates below are 2026-10-14 (PT).

## Source

* **Chinese title:** 样本量的增加能保持原估计的渐近性质吗?
* **English title:** Could Asymptotic Properties of Estimator Remain When Sample Size Increases?
* **Author:** 崔恒建 / Hengjian Cui, Beijing Normal University.
* **Book:** *10000 Selected Problems in Sciences: Mathematics* / 《10000个科学难题·数学卷》, Science Press, 2009; book pp. **408–409**, PDF pp. **424–425**.
* Original local PDF: `/Users/jinleic/Documents/中文pdf/10000个科学难题·数学卷(10000个科学难题数学编委会).pdf`.
* Extracted source: [sources/book-excerpt.txt](sources/book-excerpt.txt). The book itself leaves the error-law conditions unspecified and does not resolve nonunique minimizers or strong-consistency coupling.

## Problem

Fix p<infinity, a **single nested deterministic design sequence** x_i in R^p, one **fixed** finite convex coercive loss rho (not rho_n), and i.i.d. errors. In Y_i=x_i'beta_0+epsilon_i, let T_n be a specified measurable minimizer of sum rho(Y_i-x_i'beta). An eventual full-rank design guarantees existence for the examples here. Weak consistency means T_n->beta_0 in probability.

The intended question is whether weak consistency of the original estimator implies weak consistency of the estimator on the **2n-row array** (x_1,...,x_n,x_1,...,x_n) with independent i.i.d. errors. We seek a result with unique minimizers, or one robust to a fixed reasonable selection; a deliberately design-dependent tie preference is only a diagnostic, not a satisfactory resolution. When minimizers are not unique, our positive and triangular results explicitly state whether they control **every** selection.

Strong consistency additionally requires a coupling across n:

* **R (fixed replicate streams):** use independent infinite streams epsilon_i and epsilon_i', taking the first n of each.
* **S (sliding second block):** use one infinite stream, taking epsilon_1,...,epsilon_n and epsilon_{n+1},...,epsilon_{2n}, attaching the latter to x_1,...,x_n.
* **I (independent experiment vectors):** draw an independent 2n-vector at every n, its first n entries defining the original estimate. Different n use independent vectors. Under this coupling even the original estimator in Theorem 3 fails strong consistency; it is not a counterexample to a strong implication under I.

R, S, and I have exactly the same per-n experiment: **weak consistency is coupling-free**. Their almost-sure behavior can differ. The original design is nested; the *pooled arrays* need not be prefixes of any one design. In our S counterexample beta_0=0, so Y=epsilon throughout, and for every n all 2n errors are i.i.d. and the second half is independent of the first, exactly as required by the book's per-n experiment. Its unique-estimator formulas apply for **n>=4**. The fixed-stream positive result is proved for least squares by averaging and for p=1 with unique half minimizers by a sandwich argument, not for general convex M-estimation in p>=2.

A **triangular original design**, allowing x_{n,i} to change at old indices, is a different problem. It is clearly labeled throughout.

For the book's secondary **fully iid** formulation, if the same estimator rule T_k is consistent for every sample size k and N(n)->infinity is deterministic, weak consistency of T_{N(n)} is simply a subsequence statement. With one fixed iid infinite stream, the same is true almost surely. The repeated regression experiment **need not be iid** in its responses/design pairs and is not generally the original design's N(n)-prefix, which is why the specific question is not tautological.

## Status as of 2026-10-14

### (a) Verbatim book statement

> 则有：若 β̂n 是 β 的相合估计, 则 β̂N 也是.

Faithful English: “Then: if beta_hat_n is a consistent estimator of beta, beta_hat_N is also.” This is the exact extracted sentence on book p. 408, [source line 46](sources/book-excerpt.txt). Its preceding definition uses convex rho with rho(±infinity)=infinity, N=2n, and x_{n+j}=x_j; it says the iid error distribution “satisfies certain conditions” without listing them.

### (c) Fully quantified statement attacked

**For every fixed integer p>=1, every single deterministic design sequence (x_i) whose first n_0 rows span R^p for some fixed n_0, every fixed finite convex coercive rho:R->R, every fixed error law F on R giving an identifiable location-regression family, and every beta_0 in R^p, if the original and repeated-design criteria both have almost-surely unique minimizers for every n>=n_0, then original weak consistency beta_hat_n -> beta_0 in probability implies repeated-design weak consistency beta_tilde_{2n} -> beta_0 in probability.**

Here the two criteria are F_n and F_n+F_n' defined in [proof.md §1](proof.md#1-definitions-three-error-couplings-and-design-indexing), with two independent F-distributed n-vectors at each n. Identifiability means different beta values induce different observation laws for a full-rank prefix. **No moment, density, or population-loss/Fisher-identification condition is imposed in this broad attacked formulation**; in particular, we do not assume that E[rho(epsilon-t)-rho(epsilon)] exists or has a unique minimum at zero. This is an explicit formalization of the otherwise unspecified error-law clause, not a claim that Cui intended every such law. Original and pooled *sample* minimizers are both required unique in the main target; side results about all selections or artificial selections are labeled separately. p and rho never vary with n.

### (b) Dated status search and subsequent local result

**Earlier 2026-10-14 literature search: no resolution found; not proof of openness.** The later HMZ attempt produced the nested counterexample in [Theorem 11](proof.md#13-full-scope-written-counterexample-to-the-broad-no-moment-formulation). The broad no-moment formulation (c) is **refuted by written proof, parent-audited, independent Opus referee correct, with five minor presentation fixes applied**. It needs E|epsilon|=infinity and is not fully Lean-certified or HMZ-accepted. Cui's unspecified regular-error question and finite-moment general-convex regimes remain open beyond Theorems 9/10; “OPEN” means unresolved here, not certified worldwide openness.

The dated English/Chinese search log and access limits are in [sources/reading-notes.md](sources/reading-notes.md): exact book-title phrases, Cui/Chen/Zhao/Wu/Drygas, necessary/sufficient conditions, and replication/doubling. Citing-work checks included **Lai–Robbins–Wei (1978)**, whose primary p. 3034 cites Drygas and proves nested LSE strong consistency; **Zhao (2002)**, whose opened primary references include Zhao–Rao–Chen (1993); and **Wang–Hu (2015/2016)**, which explicitly improves Zhao's strong M-consistency theorem. These works establish results described below, not a resolution of the exact book implication. Older necessity papers and a 2023 dependent-error paper were screened with their access limitations recorded.

**Parent-reported OpenAI/math corpus screen:** no family for this topic was found in local clone **adc7f1241** or the remote listing checked **2026-10-14**. This worker did not rerun that screen; it is corpus coverage evidence only, not a proof of openness. The parent's independent scope review is [mathematics/evidence/mathematics-intake/independent-review.json](../evidence/mathematics-intake/independent-review.json).

| Formulation | Finding | Evidence |
|---|---|---|
| Broad formulation (c): nested design, unique minimizers, arbitrary fixed convex loss and identifiable iid law with no moment restriction | **Refuted: written proof, parent-audited, independent Opus referee correct; minor fixes applied** | [Theorem 11](proof.md#13-full-scope-written-counterexample-to-the-broad-no-moment-formulation); [clarified proof](hmz-lean-20261014/counterexample.md); requires infinite first absolute moment; not full Lean/HMZ acceptance |
| Nested design, any fixed p, C^2 loss with 0<m<=rho''<=M, iid finite-variance errors | **Weak preservation proved**, without density or score-centering assumptions | Self-contained Theorem 9 in [proof.md §9](proof.md#9-full-weak-preservation-theorem-for-uniformly-curved-losses) |
| Nested design, centered nondegenerate Gaussian errors, fixed even convex coercive Lipschitz loss, translation-equivariant original estimator | **Weak preservation proved in a written, parent-audited argument**, including LAD/Huber; not a complete Lean proof | Theorem 10 in [proof.md §12](proof.md#12-regular-bounded-score-extension-and-gaussian-ladhuber-transfer); [full derivation](hmz-lean-20261014/regular-bounded-score-derivation.md) |
| Scalar unique half minimizers, weak consistency; strong consistency under R | Preservation holds | Self-contained Theorem 1 in [proof.md](proof.md) |
| Least squares in any fixed dimension, weak consistency; strong consistency under R | Preservation holds by exact averaging | Theorem 2; classical background [Drygas 1976, DOI 10.1007/BF00535679](https://doi.org/10.1007/BF00535679) |
| Strong consistency under S | **False already for unique scalar least squares** | Theorem 3: original ->0 a.s.; pooled limsup/liminf are +1/2 and -1/2 a.s. |
| Triangular original designs, weak consistency | **False for p=4**, even when every original minimizer is consistent and every pooled selection is inconsistent | Theorem 5; not a solution of the nested question |
| Literal “arbitrary measurable argmin selection” | False through an explicit artificial tie rule | Theorem 6; diagnostic only |

The book's 2009 “no progress beyond LSE” statement must not be turned into “no later M-consistency results.” Wang–Hu [arXiv:1505.07178](https://arxiv.org/abs/1505.07178), published as [DOI 10.1007/s00184-015-0554-8](https://doi.org/10.1007/s00184-015-0554-8), gives a later strong-consistency sufficient theorem, not the desired implication from consistency alone. Exact source scope and access failures are in [sources/reading-notes.md](sources/reading-notes.md).

## State of the art

This is the strongest **directly checked** relevant theory found, not a claim to a globally exhaustive/latest bibliography.

| Estimator/regime | Directly checked result | Primary source |
|---|---|---|
| LSE, fixed nested full-rank design, i.i.d. mean-zero errors with finite nonzero variance | Weak consistency iff lambda_min(S_n)->infinity | [Drygas (1976), Theorem 3.1](https://doi.org/10.1007/BF00535679); complete PDF saved |
| LSE, independent mean-zero errors with uniformly bounded second moments | S_n^(-1)->0 implies strong consistency for the nested design | [Lai–Robbins–Wei (1978), Theorem 1, p. 3034](https://doi.org/10.1073/pnas.75.7.3034); primary scanned theorem page saved |
| LAD, i.i.d. median-zero errors with continuous positive density near zero | With V_n^2=S_n>0 and max_i ||V_n^(-1)x_i||->0, 2f(0)V_n(T_n-beta_0) converges to N(0,I); this implies weak consistency for nested rows | [Pollard (1991), Theorem 1, p. 189](https://doi.org/10.1017/S0266466600004394); author PDF and four page renders saved |
| Convex M, additional loss/error regularity | Weak consistency under S_n^(-1)->0 is announced; displayed A2 requires centered score, local linear identification, and locally uniformly bounded score second moment | [Zhao–Rao–Chen (1993)](https://doi.org/10.1007/978-1-4615-7909-0_41); abstract and preview p. 360 opened; formulas recovered visually, but the following formal theorem/proof pages remain inaccessible |
| Convex M, explicit score-identification conditions and diffuse design | Strong consistency when d_n=max_i x_i'S_n^(-1)x_i=O(1/n), bounded local score increments, E psi(epsilon)=0, and |E psi(epsilon+u)|>=C|u| near zero | [Wang–Hu, arXiv:1505.07178, Theorem 1](https://arxiv.org/abs/1505.07178); no additional q>1 moment, but the displayed expectation still requires ordinary integrability |
| General error laws, atoms, flat-bottom losses | The LSE eigenvalue criterion is **not universally necessary**: LAD can recover exactly eventually with x_i=1/i and errors {-1,0,1}; a uniform-error flat-bottom example also has every minimizer strongly consistent while S_n<2 | Self-contained Theorems 4A/4B, not attributed to an unverified source |

**Necessary conditions and literature gaps.** Bai–Wu (1997), [DOI 10.1016/S0167-7152(96)00182-4](https://doi.org/10.1016/S0167-7152(96)00182-4), and Berlinet–Liese–Vajda (2000), [DOI 10.1016/S0378-3758(99)00218-9](https://doi.org/10.1016/S0378-3758(99)00218-9), explicitly concern necessity or necessary/sufficient conditions. Their primary metadata was opened, but their complete theorem hypotheses were not accessible; no formula is guessed from their titles. Chen–Wu (1988), [DOI 10.1016/0047-259X(88)90120-0](https://doi.org/10.1016/0047-259X(88)90120-0), is similarly recorded without inventing its assumptions.

**A proved reduction for the actual nested problem:** Theorem 7 shows that if sqrt(f) belongs to H^1 with finite location information, weak consistency of a translation-equivariant estimator forces lambda_min(S_n)->infinity. Unique M-minimizers are equivariant. Its product-affinity proof covers Gaussian errors and precisely explains why the atomic/bounded-support examples do not justify a universal necessity claim. A suitable M-estimation *sufficiency* theorem would finish the transfer in a matching regular class, since replication doubles S_n. It does not establish sufficiency for every convex rho.

**A second necessary condition, including atomic LAD:** Theorem 8 proves directly that for a spanning fixed design and an error law with positive probability on both sides of zero, consistency of even one LAD minimizing selection requires inf_{||u||=1} sum_{i<=n}|x_i'u|->infinity. No density, moments, uniqueness, or equivariance is needed. A positive-probability finite-prefix event dominates any finite-L1 tail and excludes all minimizers near the truth. Replication doubles this quantity. Sufficiency is not claimed; the result is not attributed to the inaccessible Bai–Wu theorem.

**Focused-round positive result for the actual nested target:** Theorem 9 proves weak replication preservation whenever rho is C^2 with 0<m<=rho''<=M and errors have finite variance, in every fixed dimension; the replicate error vector is independent of the original vector and iid with the **same law**. For every n>=n_0 with S_{n_0}>0, beta_hat_n, theta_n, and beta_tilde_{2n} are the unique original, population, and pooled minimizers. For all such n, E||beta_hat_n-theta_n||^2<=M^2 sigma^2 p/(m^2 lambda_min(S_n)), while pooling shares theta_n and halves this bound; all limits are along n>=n_0. For a nondegenerate law, consistency forces Gram divergence through a fixed-row influence bound uniform over n>=n_0. Thus **for nondegenerate laws in this subclass**, original consistency is equivalent to Gram divergence plus theta_n->beta_0. For degenerate errors, almost surely the pooled criterion equals 2F_n and beta_tilde_{2n}=beta_hat_n a.s.; Gram divergence need not hold. The nonquadratic cyclic example rho(r)=r^2/2+log(cosh r) now includes the between-cycle bound |theta_n-beta_0|<=|E psi(epsilon)|/(2k+1) at n=4k+1 or 4k+3; n=4k and 4k+2 are balanced. This is a self-contained derivation, not a claim of priority.

## Attack

1. **Separate weak/strong, selection, and coupling first.** This produced the scalar bracket proof, the exact least-squares averaging identity, and a genuine strong S counterexample. The latter uses x_i=1 only at i=4^k and Rademacher errors. The original estimate averages the first j informative errors. Within each exponentially long interval of n with the same j, a greedy packing supplies many disjoint sliding windows; both all-plus and all-minus windows occur eventually in every interval. A summable probability bound proves the almost-sure oscillation. No simulation supplies this proof.
2. **Test convexity plus exchangeability.** It is insufficient even for i.i.d. random convex functions. For delta>0, H_s=[[1,s delta],[s delta,delta^2+delta^4]], a_s=(s delta,0), and f_s(z)=(z-a_s)'H_s(z-a_s), each minimum tends to zero. For opposite signs, the sum's minimizer is (0,1/(1+delta^2)). These quadratics do not themselves have the required nested regression representation; they rule out a tempting abstract argument. Rational checks are in [evidence/exact-checks.json](evidence/exact-checks.json).
3. **Realize the obstruction with one fixed regression loss.** Theorem 5 constructs six low-leverage hinge groups and two high rows, with rho(r)=10|r|+(r-1)_+ and Rademacher errors. It proves compact-uniform objective limits, coercivity, and convergence of all minimizers. The original fourth coefficient tends to zero; after replication it tends to -1,0,+1 with probabilities 1/4,1/2,1/4. This is a substantive triangular-design counterexample, not a nested one.
4. **Attempt nesting rather than silently changing the target.** Freezing and concatenating stages retains old penalties. In the limiting old coordinates, G(0,0,0,v)=4v_+ + (-v)_+/2. Thus old stages penalize every nonzero weak-coordinate displacement; they cannot be discarded. Raising new-stage weights eventually breaks the bounded high-row pinning. Staggered high-row updates also need consistency at every intermediate prefix, not merely completed blocks. A one-sided-flat variant was explored to eliminate old penalties, but finite empirical groups retain random linear slopes in the unpenalized direction; no iid, fixed-loss construction controlling those slopes and preserving original consistency was obtained. These are failed constructions, **not impossibility theorems**.
5. **Attack necessity in the genuine nested setting.** Theorem 7 extracts a fixed finite-energy direction if Gram divergence fails, then uses positive product Hellinger affinity to rule out consistency at two distinct parameters. Equivariance supplies the two-parameter requirement. Theorem 8 separately handles LAD with two-sided, possibly atomic errors by a finite-prefix directional-derivative obstruction. These give genuine necessary-condition reductions in the nested problem, but neither proves pooled consistency from necessity alone.
6. **Check atoms/support rather than assuming LSE conditions.** Theorems 4A/4B give complete bounded-Gram examples, including eventual unique LAD recovery and shrinking nonunique intervals. Theorem 6 records why an arbitrary argmin selector makes the literal statement vacuous; it is not counted as settling the intended problem.

### Focused nested-design round

The requested scale-separation route was tested before changing approach. For any L-Lipschitz loss, the effect of rescaling retained strong coordinates is bounded by (LR/A) sum ||a_i|| on ||z||<=R. Taking A super-exponential does not remove the retained weak-coordinate criterion. In the constructed candidate, the exact residual barrier remains G(0,0,0,v)=4v_++(-v)_+/2; at scale ratios through 2^(-64), the old penalty at v=-1 is still exactly 1/2. The isolated intermediate-prefix geometry has v=r-1->-1 when only one high coordinate is updated. These calculations block that candidate, not every possible counterexample.

The fallback attack succeeded for uniformly curved losses: a persistent fixed-row leverage gives an own-response fitted-value derivative bounded below by (m/M) times that leverage. A nondegenerate error law therefore prevents concentration unless S_n^(-1)->0. Concentration around the deterministic population minimizer then proves replication preservation. This directly addresses the nested implication rather than replacing it by a triangular problem. The proof stops at LAD/Huber because their global lower curvature is zero; the influence and sample-gradient bounds fail, and Theorem 4A shows that Gram divergence cannot be universally necessary there.

### Exercised computational evidence

* [work/check_algebra.py](work/check_algebra.py): independent, standard-library rational arithmetic, no imports from the simulation and no optimizer. **PASS:** 83,521 geometry grid checks, 68 local-loss identities, 1,088 pooled-coordinate checks, all 16 high-error configurations, and disjoint-window packings for j=1,...,6. These finite checks do not prove an asymptotic theorem.
* [work/illustrate.py](work/illustrate.py): seeded Monte Carlo, seed **20261014**, NumPy **2.5.4**, SciPy **1.18.1**, one computational thread. It solves the **full finite loss**, not just the limiting objective, by exact aggregation of equal row/error types. Numerical primal/dual residuals are checked on every LP. SciPy warns that `threads=1` is passed verbatim to HiGHS; this is intentional and was not suppressed.
* At m=1,000,000 (n=6,000,002), 200 triangular trials: original fourth-coordinate error exceeding 1/2 occurred in **0/200**, pooled in **98/200**; the same-draw limiting configuration also predicts 98/200. Maximum LP residual was about **8.53e-14**. Smaller m had genuine large outliers: their full results are retained, including mean errors exceeding 1,000. They are not hidden or interpreted as contradicting the asymptotic proof.
* A single sliding path scanned every n **from 4 through 1,048,575**; each tested block j=1,...,9 contained both extreme second-block averages. This illustrates the oscillation mechanism, not convergence of the finite prefix path to zero. Separate 20,000-trial pointwise experiments show MSE approximately 1/j before and 1/(2j) after pooling, consistent with weak preservation.
* Full outputs: [evidence/monte-carlo.json](evidence/monte-carlo.json), [evidence/exact-checks.json](evidence/exact-checks.json). No global packages were installed; `uv --with` supplies temporary environments. All work stays in this target directory; no campaign or git operation was run.
* Focused exact checks: [work/check_curvature_round.py](work/check_curvature_round.py) passed **120** retained-row Lipschitz checks, **675** Hessian comparisons, **2,025** influence inequalities, **16,875** normalized-gradient inequalities, and **50** trace identities. Scale profiles and intermediate-prefix displacements are in [evidence/curvature-exact-checks.json](evidence/curvature-exact-checks.json).
* New nonquadratic illustration: rho(r)=r^2/2+log(cosh r), curvature [1,2], errors 0/2 with equal probability, balanced cyclic design, seed **20261015**, 400 trials per size. At n=1024, MSE around the population minimizer was **0.00334025** originally and **0.00177668** pooled, against proved upper bounds **0.015625** and **0.0078125**. The score mean at truth is approximately **1.48201**, so no centered-score assumption is hidden. [Output](evidence/curvature-monte-carlo.json).
* The first generic Newton illustration hit its iteration cap; [the failure is preserved](evidence/curvature-illustration-first-attempt.txt). It was replaced by coordinate monotone-score bisection using the actual separable design, without relaxing the final gradient criterion. The corrected run completed with maximum normalized gradient **6.87e-13** and at most **41** bisection iterations. This numerical correction does not alter the theorem.

Reproduce from this directory:

```sh
python3 work/check_algebra.py
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 \
  uv run --with numpy==2.5.4 --with scipy==1.18.1 python work/illustrate.py
python3 work/check_curvature_round.py
uv run --with numpy==2.5.4 python work/illustrate_curvature.py
```

## Claims

| Claim | Status | Evidence path |
|---|---|---|
| Scalar unique-half weak preservation, and strong R preservation | PROVED | `proof.md`, Theorem 1 |
| Least-squares pooled estimator is the mean of the two half estimates | PROVED | `proof.md`, Theorem 2 |
| Universal strong S preservation | REFUTED | `proof.md`, Theorem 3; `evidence/proof-review.md` |
| Sparse LSE example has pooled a.s. limsup/liminf ±1/2 while its original is strongly consistent | PROVED | `proof.md`, Theorem 3 |
| Gram divergence is necessary for all convex M-estimators/error laws | REFUTED | `proof.md`, Theorems 4A/4B |
| Triangular-design weak preservation even for every selection | REFUTED | `proof.md`, Theorem 5; `evidence/proof-review.md` |
| Unrestricted arbitrary measurable-selection formulation | REFUTED | `proof.md`, Theorem 6; diagnostic only |
| Regular finite-location-information + equivariance forces Gram divergence for nested designs | PROVED | `proof.md`, Theorem 7; `evidence/proof-review-2.md` |
| Two-sided errors and a spanning nested design force L1 design divergence for consistent LAD | PROVED | `proof.md`, Theorem 8; `evidence/proof-review-3.md` |
| Nested weak preservation in all fixed dimensions for globally bounded positive curvature and finite error variance | PROVED | `proof.md`, Theorem 9; `evidence/proof-review-4.md` |
| Gaussian LAD/Huber and even bounded-score convex losses, nested design, equivariant original estimator | WRITTEN PROOF + PARENT AUDIT; not full Lean formalization | `proof.md`, Theorem 10; `hmz-lean-20261014/regular-bounded-score-derivation.md`; `written-proof-parent-audit.json` |
| Scale-separation diagnostic and finite curvature inequalities | COMPUTED+VERIFIED | `evidence/curvature-exact-checks.json`; mathematical argument in `proof.md §10` |
| Nonquadratic, non-centered-score numerical illustration | COMPUTED+VERIFIED | `evidence/curvature-monte-carlo.json` |
| Finite rational identities and seeded numerical illustrations | COMPUTED+VERIFIED | `evidence/exact-checks.json`; `evidence/monte-carlo.json` |
| Broad no-moment nested-design weak implication, formulation (c) | REFUTED: written proof, parent-audited, independent Opus referee correct; minor fixes applied | `proof.md`, Theorem 11; `hmz-lean-20261014/independent-referee-resolution.json` |
| Cui's intended regular-error formulation, beyond Theorems 9/10 | OPEN / hypotheses unspecified | The new counterexample has infinite first absolute moment; it does not settle centered/finite-moment-score regimes |
| General strong R implication beyond proved sufficient regimes | OPEN | `proof.md §11` |

## Independent review

Codex CLI **gpt-6.1-sol**, effort **max**, read-only sandbox, ephemeral session, restricted by prompt to this target; no further delegation or web use. First audit: **READY-WITH-FIXES**, with no invalidating error in Theorems 1–6. It explicitly confirms both the strong sliding-block and triangular-design counterexamples and the unresolved nested weak scope.

All Codex objections are resolved. Review 1 requested two minor fixes: only low groups 3,4,6 have changing fourth components, and the bounded-Gram examples needed a direct strong-S argument. Review 2 returned **READY**, accepting those fixes and Theorem 7. Review 3 returned **READY-WITH-FIXES**, accepting Theorem 8 and the numerical evidence; its two wording fixes are applied: repeated regression **need not** be iid, and the sliding scan begins at **n=4**. The parent’s independent Claude review additionally requested the explicit book quotation, quantified target, uncertified-open status, citing-work log, and third strong coupling I; all are incorporated. The I-coupling observation has its short proof in Theorem 3's scope paragraph.

The fourth focused Codex audit returned **READY-WITH-FIXES**, explicitly confirming that Theorem 9 proves the requested nested weak implication in its subclass, with no substantive proof gap. Its one qualification is applied in both proof and report: the **equivalence characterization** requires nondegenerate errors; the **replication implication** includes degenerate errors. The reviewer also accepted the scale-separation and intermediate-prefix diagnostics at their stated limited strength. All review processes have exited.

The parent's independent **Claude opus-5-5, max** audit also found no logical error in Theorem 9: [curvature-review.json](../evidence/mathematics-intake/curvature-review.json), verdict **READY-WITH-FIXES**. Its qualifications are applied: independent **same-law** replication; definitions, bounds, and uniform influence statements restricted to **n>=n_0**; an **almost-sure** identity in the degenerate case; and the optional between-cycle calculation for the nonquadratic example. These clarify the existing theorem without changing its scope.

Earlier artifacts: `evidence/proof-review.prompt.txt`, `evidence/proof-review.md`, `evidence/proof-review.run.json`, plus corresponding `proof-review-2.*`, `proof-review-3.*`, and `proof-review-4.*` files. The later [HMZ/Lean attempt](hmz-lean-20261014/README.md) has component-level Lean acceptance and a stopped HMZ run without its reviewer verdict. The separate parent-owned **Claude Opus 5.5/max, no-tools** referee returned **correct**, checking 44 written claims, every-prefix original consistency, pooled inconsistency and target hypotheses. Its five minor presentation findings were applied only to the integrated proof; [receipt and both hashes](hmz-lean-20261014/independent-referee-resolution.json). It did not inspect/use Lean. No historical novelty, full-kernel-proof or HMZ-acceptance claim is made.

## Next steps

**Exact remaining mathematical scope:** the broad no-moment implication is refuted by Theorem 11's written nested counterexample, but the book leaves error conditions unspecified. Its intended regular-error version remains unresolved beyond the finite-variance uniformly curved Theorem 9 and the Gaussian even-Lipschitz-loss Theorem 10. In particular, the new construction has E|epsilon|=infinity and cannot be presented as settling centered/finite-moment-score versions. General LAD/Huber behavior for singular/atomic or non-centered laws is not classified. Theorem 4A still prevents a universal Gram-divergence necessity claim.

**Exact remaining certification:** fully formalize Theorem 11's fixed infinite law/design, every-prefix convergence and positive limiting pooled-error probability; its written proof has passed parent and independent Opus review, but Lean covers components only. The stopped HMZ run cannot be relabeled accepted. Theorem 10's stochastic compactness and argmin steps are also written only. Complete Zhao--Rao--Chen and Bai--Wu theorem text remains inaccessible in the recorded source check; unseen qualifications were not assumed away.
