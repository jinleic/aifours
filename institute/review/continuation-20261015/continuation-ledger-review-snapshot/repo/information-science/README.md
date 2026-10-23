# Information-science volume

Source volume: 《10000个科学难题·信息科学卷》 (10000 Selected Problems in Sciences: Information
Science, Science Press, 2011, ISBN 978-7-03-031911-1). Local copy: [`books/`](../books/README.md),
not tracked by Git; 1139 PDF pages; the table of contents is on PDF pages 11–21; PDF page = book
page + 21.

Each target directory owns its own status, sources, evidence and claims. This index only routes.
Round-level selection reviews, screening reports and parent replays live in
[`evidence/`](evidence/). [Repository overview](../README.md).

## Information-science selection (2026-10-14)

Screened the full table of contents, then read about 40 candidate sections to identify precise questions. A problem was kept only if it

1. has a precise mathematical statement in the book,
2. showed no full solution in a quick literature pre-screen on 2026-10-14, and
3. has a bounded attack path (exact computation, counterexample search or proof) on this machine.

"Not too hard" is a provisional [INFERENCE], not a guarantee. A failed literature search does not
prove that a problem is open. An independent selection review flagged disturbance decoupling as a weak
choice because exact per-instance decision is older than the book; it is retained as a scoped
partial result, not counted as a confirmed easy open problem. Intake provenance, the review and parent
replays are under [`evidence/information-science-intake/`](evidence/information-science-intake/).

| # | Target | Book problem (authors) | Book pages (PDF pages) | Outcome after the 2026-10-14 continuation | Directory |
|---|---|---|---|---|---|
| 1 | Robust SPR synthesis for stable interval polynomial families of degree > 4 | 区间系统的鲁棒严格正实综合 (郁文生, 王龙) | 680–682 (701–703) | Partially solved. Degrees 5 and 6 have recent public claims with Lean sources; neither build was replayed. New all-order proofs reduce every failure to two explicit critical contact certificates and make the conjecture equivalent to nonzero closed feasibility on radial stability-boundary boxes. There is still no proof or counterexample for degree 7 or higher. | [`robust-spr-interval-synthesis/`](robust-spr-interval-synthesis/) |
| 2 | Stochastic H∞ preview control | 随机系统 H∞ 预演控制 (张焕水, 王宏霞) | 674–676 (695–697) | Partially solved. A candidate continuous-time theory covers the mean-square substitute. A new exact constant-matrix finite-horizon example is feasible at γ = 6 under the printed criterion for all adapted disturbances, while every controller has mean-square gain above 14, so the substitute is not equivalent. General synthesis under the printed criterion remains unsolved. The 2020 SIAM N&S result is confirmed from its author manuscript to be discrete-time and finite-horizon; priority remains unclear. | [`stochastic-hinf-preview-control/`](stochastic-hinf-preview-control/) |
| 3 | Disturbance decoupling by static output feedback | 静态输出反馈下的干扰解耦 (陈本美) | 631–632 (652–653) | Partially solved. Exact per-instance algebraic decision is prior work. All unstabilized gains are now synthesized explicitly when min(m, p) = 1 (an affine family) and when m = p = 2 (one real quadric), at every order and with all feedthrough terms. General real gain selection and stable selection remain open; the Grassmannian framework is classical. | [`ddp-static-output-feedback/`](ddp-static-output-feedback/) |
| 4 | Optimal pixel expansion and contrast of visual cryptography schemes | 视觉密码方案的最优化问题 (刘峰) | 409–410 (430–431) | Partially solved. All four basis and collection optima are now certified for every strong access structure on at most five participants. The five remaining collection cases were closed by full-distribution impossibility proofs and independently re-derived without the original code. The general access-structure problem remains open. | [`visual-cryptography-optimality/`](visual-cryptography-optimality/) |
| 5 | P-type iterative learning control under bounded initial errors, relative degree ≥ 1 | 相对阶不小于 1 的 P 型迭代学习控制系统 (孙明轩) | 712–715 (733–736) | Open. No stationary finite-memory linear pointwise P-type learner combines exact nominal tracking with robustness to arbitrary bounded starts, at any relative degree. An initial-error-rectified P-type law achieves both for the degree-one integrator with initial errors only. It fails under arbitrary measurement noise at every degree and under process noise at degree one. | [`p-type-ilc-initial-error/`](p-type-ilc-initial-error/) |

None of the original five information-science targets was fully solved. The initial 2026-10-14 continuation produced the scoped
theorems and certificates above; parent replays and the independent re-derivation are under
[`evidence/information-science-push-20261014/`](evidence/information-science-push-20261014/). Four of
the five are control-theory problems: in this volume the control chapter holds most of the
precisely stated, tractable problems.

## Information-science screened out

Solved after the book was published:

- 基因组间的转位距离 (complexity of sorting by transpositions): NP-hard. Bulteau, Fertin, Rusu,
  "Sorting by Transpositions Is Difficult", ICALP 2011 / SIAM J. Discrete Math. 2012
  (doi:10.1137/110851390).
- 三维凸多面体相交检测 (O(log n) intersection test with linear-space preprocessing): Barba,
  Langerman, "Optimal detection of intersections between convex polyhedra", SODA 2015
  (doi:10.1137/1.9781611973730.109).

Too hard for a bounded attempt: existence of APN permutations for even n ≥ 8; tight nonlinearity
bounds for resilient Boolean functions (e.g. whether 8-variable balanced functions reach 118); the
P vs NP family; polynomial-time μ-calculus model checking; the Unique Games Conjecture; Tarski's
exponential-function problem; non-abelian hidden subgroups; lattice reduction; general decoding;
general characterizations for differential flatness and linear time-varying stability.

Not precisely posed (research directions or laboratory work rather than a checkable claim): most
engineering, optics, metrology and network items, and the popular-science section.

## Information-science expanded search (2026-10-14)

Checked **51 distinct candidate articles**, including targeted rereads, with three topic scouts;
then pursued seven proof dossiers. Exact book wording and current primary literature—not the
book's historical “open” label—determine each verdict. This round establishes **no new full
resolution of a previously open broad book problem**. It does completely answer the specific
mathematical readings and insufficiency claims below. Novelty is separate and remains
unestablished. Selection, direct source checks and parent replays:
[`evidence/information-science-more-20261014/`](evidence/information-science-more-20261014/).

| Target; book authors | Book pages (PDF pages) | Defensible outcome | Dossier |
|---|---|---|---|
| Geomagnetic Gauss uniqueness; 李玉和、杨建中 | 880–882 (901–903) | **Answered by classical prior work** for exact tangential+vertical continuum data on one source-free closed surface. Complete Green/Gauss separation proofs supplied; noisy, scalar-only and discrete data remain distinct. | [`geomagnetic-gauss-uniqueness/`](geomagnetic-gauss-uniqueness/) |
| Nonuniform spatial sampling / array aliases; 穆鹏程、殷勤业 | 446–448 (467–469) | **Answered by prior work** in the isotropic, noiseless, single-source model. Exact rational/algebraic decision and two counterexamples to published arbitrary-basis vertex shortcuts are certified. Arbitrary directional element gains are not silently included. | [`array-nonaliasing/`](array-nonaliasing/) |
| POMDP performance optimization; 汪德新、曹希仁 | 653–655 (674–676) | **Complete negative answer to universal expected-average optimizer existence:** a four-state blind model has supremum 1 but no maximizing policy, even with randomization/unbounded memory. The book omits an expectation symbol; other objectives and general optimization are not thereby solved. | [`average-reward-pomdp-nonattainment/`](average-reward-pomdp-nonattainment/) |
| Nonnegative, marginal-correct time–frequency distributions; 张建国、殷勤业 | 452–454 (473–475) | **Scoped sufficiency question fully refuted:** a genuine Schwartz Fourier pair passes both separate IF/GD density-feasibility tests and the covariance identity, but admits no joint nonnegative measure satisfying both. Rational dual + Arb interval certificate, independently reproduced. Broad “physical meaning” remains unspecified, not solved. | [`positive-tfd-marginals/`](positive-tfd-marginals/) |
| Piecewise-LTI approximation; 高静怀 | 467–469 (488–490) | **Partial:** complete known-kernel L¹ criterion, declared stochastic-metric characterizations, optimal segmentation and error bounds. Blind wavelet/reflectivity/Q identification needs extra assumptions; classical results are not called new discoveries. | [`piecewise-lti-approximation/`](piecewise-lti-approximation/) |
| Distributed scheduling under time-varying channels; 关新平、杨博 | 731–734 (752–755) | **Partial:** strong-stability theorem for arbitrary conflict graphs and finite-state Markov channels, but requires synchronized unbounded-rate control clocks. This does not satisfy the book's simple-policy intent. Prior rate stability is not confused with strong stability. | [`wireless-timevarying-strong-stability/`](wireless-timevarying-strong-stability/) |
| Adaptive large-population stochastic games; 李韬 | 635–637 (656–658) | **Partial:** all unknown A/B/Λ matrices identified, N-independent stability, mean-MSE and Nash-gap rates proved for a robustly stable, fully actuated homogeneous subclass with common/private pilots. General unknown stabilizable dynamics remain outside the theorem. | [`adaptive-mean-field-game/`](adaptive-mean-field-game/) |

**Strongest additional certificate:** the time–frequency example has both one-sided constraints
separately feasible with densities, yet its full-plane nonnegative dual has forced expectation
`−0.0057637133335289…`. This settles the proposed joint-sufficiency claim negatively, not the
complete classification of physically meaningful distributions. Parent replayed the 256-bit Arb
checker and independently reconstructed the Fourier identities, exact corner/Sturm checks and
60-digit Gaussian integrals with different code. No Lean/kernel or human-journal certification
is claimed.

Additional status findings, not new solutions by this project:

- The finite-domain **CSP dichotomy** mentioned in 约束求解与优化 was proved independently in
  2017; [Zhuk's primary theorem](https://arxiv.org/abs/1704.01914) was checked. This does not settle
  every constraint-optimization or random-phase-transition question in the article.
- The **binary surrogate-paradox** question within 因果推断 has sharp observed-data criteria
  ([Yin–Liu–Geng–Luo](https://arxiv.org/abs/1607.05454)); general causal inference is not solved.
- Network-coding **exact solvability** is undecidable
  ([Li, arXiv:2205.11461](https://arxiv.org/abs/2205.11461)); this is not a theorem computing the
  general asymptotic capacity region.
- The sensor article's displayed **Mathieu equation**, not Duffing, has classical analytic
  fundamental solutions ([DLMF §28.2](https://dlmf.nist.gov/28.2)); the wider physical sensor-design
  programme has no single specified mathematical acceptance condition.

No workspace/infrastructure audit, Git mutation, external contact or publication was performed.

## Difficult-problem visit (2026-10-15)

The owner requested one difficult information-science problem with a six-hour total ceiling, alongside
mathematics and physics. The [hard-problem catalog](evidence/information-science-hard-20261015/catalog.md)
records candidates, status sources, budget classes, probes and parent-review restrictions.

Selected `info-p0403`, **弹性布尔函数的非线性度的紧上界** (张卫国, 肖国镇, book pp. 403–405; PDF
pp. 424–426): existence of a balanced nine-variable Boolean function with nonlinearity at least 242.
An explicit truth table can settle this instance without assuming the unrefereed 2026 upper-bound
claim. Local-neighborhood or symmetry-class exclusions remain partial; timeout and heuristic failure
establish no nonexistence.

The [institute run](../institute/runs/hard-2026-10-15/README.md) first timed out during 10-minute
identification. With owner approval it restarted at 12:02 PT with a fresh six-hour allocation and a
30-minute selected-question identification stage. Authority for those engine visits:
[`record.json`](../institute/runs/hard-2026-10-15/problems/info-p0403/record.json).
Its batch 03 continuation closed **unverified** (accept-with-fixes) at 15:37 PT with partial results.
An elementary proof shows that the balanced nine-variable maximum is 240 or 242. Any balanced 242 function
must have degree exactly eight and nonzero support XOR. Restricted exhaustive exclusions were also replayed.
Existence remains open. See the [outcome ledger](../institute/review/hard-2026-10-15-outcomes.md).
The screening worker's one read-only Git-command deviation is recorded in the
[parent source checks](../institute/review/parent-source-checks.md).

### Authorized continuation (2026-10-16)

All **252** remaining fixed-half classes in the pinned restricted corpus are now excluded;
this is not global nonexistence. A universal odd-half residue argument gives distance at least
112. Its [zero-geometry continuation](evidence/hard-continuation-20261015/quadratic-distance/zero-geometry/README.md)
then excludes the entire balanced quadratic residue type **(polar rank4,weight128)** by an
explicit zero-flat/next-bit/character-projection proof. Fresh Codex review returned **ACCEPT**,
with a separate Opus review of its imported lemmas and independently replayed finite certificates.
Seven large residue-type families remain.

A separate corollary proves that a nine-variable function with exactly one, two or three Walsh zeros
has nonlinearity at most 240; attainment and priority are not claimed. The methods build on
Wang–Lou–Wang and Lou–Xu–Wang. Neither result is Lean-verified or human peer reviewed.
Balanced NL242 existence remains open. See the
[continuation ledger](../institute/review/continuation-20261015/outcomes.md). Three later attempts
on the remaining seven types produced only unreviewed sub-case conditions; none excluded another type.

