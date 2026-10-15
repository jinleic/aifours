# ai4s — AI-assisted attacks on open problems

Source volume: 《10000个科学难题·信息科学卷》 (10000 Selected Problems in Sciences: Information
Science, Science Press, 2011), local copy
`/Users/jinleic/Documents/中文pdf/10000个科学难题·信息科学卷(10000个科学难题信息科学编委会).pdf`
(1139 PDF pages; the table of contents is on PDF pages 11–21).

Each target directory owns its own status, sources, evidence and claims. This index only routes.

Targets from the mathematics volume are indexed separately in [Mathematics volume](#mathematics-volume).

Targets from the physics volume are indexed separately in [Physics volume](#physics-volume).

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

## Mathematics volume

Source volume: 《10000个科学难题·数学卷》 (10000 Selected Problems in Sciences: Mathematics,
Science Press, 2009), local copy
`/Users/jinleic/Documents/中文pdf/10000个科学难题·数学卷(10000个科学难题数学编委会).pdf`
(568 PDF pages; the table of contents is on PDF pages 9–16; PDF page = book page + 16).

### Selection (2026-10-14)

Read the front table of contents (250 problem articles, excluding the afterword) and about 45
candidate sections, then assigned five research targets. This uses the opening contents pages,
not just the first five logic/set-theory articles.

The screen favors bounded setup and checkable progress, **not guaranteed low mathematical
difficulty**. A finite certificate may be easy to verify but extremely hard to discover. The
surviving formulations below remain research-risky; solved formulations and weaker variants
are separated in each target directory. Parent source checks and book provenance are in
[`evidence/mathematics-intake/parent-spot-checks.md`](evidence/mathematics-intake/parent-spot-checks.md).

| # | Target | Book problem (authors) | Book pages (PDF pages) | Outcome on 2026-10-14 (after the HMZ + Lean round) | Directory |
|---|---|---|---|---|---|
| 1 | Existence of LKTS(v) for every v ≡ 3 (mod 6); attack the two smallest open orders, 57 and 87 (a construction would be a new case, not the whole problem) | 柯克曼三元系大集的存在性问题 (常彦勋) | 428–429 (444–445) | Open. Verified a 17-system partial packing for order 57 (55 systems are needed), plus restricted-symmetry obstructions. No LKTS(57)/LKTS(87) certificate; 15 two-hour searches and one joint 480-second search ended UNKNOWN. Lean (25 theorems) checks the resolved-row encoding and the C19/C29 development criteria; the missing seed systems remain hypotheses. | [`kirkman-large-sets-57-87/`](kirkman-large-sets-57-87/) |
| 2 | Do the Serre relations define every non-symmetrizable Kac–Moody algebra (Gabber–Kac beyond the symmetrizable case)? | 非可对称化的卡茨–穆迪 (Kac-Moody) 代数的定义关系问题 (苏育才) | 226–227 (242–243) | Open. New for the `A(r,s)` family: equality whenever α₃ ≤ 3 (written proof whose level-3 step an HMZ review confirmed), and whenever α₃ ≤ 4 for r,s ≥ 4 (independent exact checker; not model-reviewed). Lean (8 theorems) covers sl₂-string and graded-ideal lemmas, not J = τ. General height-8 gaps unchanged. | [`kac-moody-serre-relations/`](kac-moody-serre-relations/) |
| 3 | Does weak consistency of a convex M-estimator survive repeating a nested deterministic design with fresh errors? | 样本量的增加能保持原估计的渐近性质吗? (崔恒建) | 408–409 (424–425) | **The broad no-moment formulation is false.** A written counterexample (p = 2, one nested design, a C² loss with 3/4 ≤ ρ'' ≤ 5/4, iid errors with E\|ε\| = ∞) keeps the original estimator consistent at every n, while the replicated-design estimator fails with probability at least e⁻²/2 along a subsequence. Independent referee: correct, minor fixes applied; not Lean-certified. Preservation proved in fixed finite dimension for a fixed nested eventually full-rank design, a fixed C² loss with 0 < m ≤ ρ'' ≤ M, iid finite-variance errors and independent same-law replicates. A separate transfer result covers centered nondegenerate Gaussian errors and even convex coercive Lipschitz losses including LAD/Huber, assuming a translation-equivariant original estimator (almost-sure uniqueness of original minimizers suffices); arbitrary consistent selectors on nonunique designs are not covered. The book's unspecified "regular" conditions for general convex losses remain open. | [`m-estimator-sample-augmentation/`](m-estimator-sample-augmentation/) |
| 4 | Gröbner–Shirshov bases for non-A finite-type Artin groups on the book's specified alphabets, distinct from known simple-element rewriting | 阿廷 (Artin) 群的 Gröbner-Shirshov 基 (L. Bokut, 陈裕群) | 30–34 (46–50) | Question (3) answered in writing for the fixed deg-lex reading: an explicit rational GS basis for every finite type, including all `B_n`; generally non-reduced; no novelty claim. Lean (82 theorems) proves conditional completeness and confluence of the exact rules, but is not instantiated for actual Artin groups. Reduced templates and the other six questions remain open. | [`artin-group-grobner-shirshov/`](artin-group-grobner-shirshov/) |
| 5 | Embed weakly E-unitary locally r-orthodox semigroups into a semidirect product of a seminormal band by a completely simple semigroup | 关于正则半群的两个嵌入问题 (郭聿琦) | 66–67 (82–83) | Open. Proved necessity, orthodox reduction, regular-band and two-D-class cases, plus 48 finite certificates. New written result: ξ is idempotent pure for every finite member, which rules out that finite counterexample route. Lean (29 theorems) covers necessity and the local characterizations. | [`regular-semigroup-embedding/`](regular-semigroup-embedding/) |

No book problem is fully solved. Target 3 settles only its broad formalization, negatively; Cui's
intended conditions are unspecified. Parent replays of the first round are in
[`evidence/mathematics-intake/parent-replays.json`](evidence/mathematics-intake/parent-replays.json).
Review findings and their dispositions are in
[`evidence/mathematics-intake/review-resolution.md`](evidence/mathematics-intake/review-resolution.md).

**HMZ + Lean round (2026-10-14).** Each target got one HMZ RLAR run (Codex gpt-6.1-sol actor,
Claude Opus 5.5 reviewer, 3,600 s). All five stopped at the budget without reviewer acceptance;
every completed review returned `done:false` because the full goal remained open. The parent
replayed every target's Lean file through Comparator: statements match derived challenge files,
only `propext`/`Classical.choice`/`Quot.sound` are used, and the kernel replay succeeds. Each
target's delivered checks were also replayed. Receipts:
[`evidence/mathematics-intake/hmz-lean-parent-verification.json`](evidence/mathematics-intake/hmz-lean-parent-verification.json),
harness and challenge files in
[`evidence/mathematics-intake/hmz-lean-verification/`](evidence/mathematics-intake/hmz-lean-verification/).
The local `math/` corpus was used as a source of proof techniques and Lean patterns; no OAI
theorem was imported as a premise.

Slot 2 was reassigned twice, using the same agent rather than launching more:

- 组合优化反问题的计算复杂性 (pp. 535–536): its binary, full-linear, known-feasible-start case
  is already covered by [Schulz's 2009 equivalence theorem](https://doi.org/10.1007/978-3-540-76796-1_19);
  broader readings need extra assumptions and were not certified as one precise open target.
  Dossier kept as evidence: [`inverse-optimization-complexity/`](inverse-optimization-complexity/).
- 西摩的二阶邻域猜想 (pp. 417–418): a [July 2026 paper](https://arxiv.org/abs/2607.18047) still
  calls it open, but the openai/math corpus (family 173, 2026-09-23) claims the full conjecture
  with a Lean formalization; not re-verified here. Intake kept:
  [`seymour-second-neighborhood/`](seymour-second-neighborhood/).

All five targets were also screened against the workspace's openai/math clone (`math/`, commit
adc7f1241, 2026-10-06) and the remote repository's newer families and preprints listed on
2026-10-14: none covers them. That corpus claims solutions to many other problems in this book
(for example Seymour, Hadwiger, Koebe, Brennan, Rokhlin's multiple mixing, Turing-degree
rigidity, circulant Hadamard, finitistic dimension and Auslander–Reiten).

### Second batch: four more exact questions (2026-10-14)

Asked to keep checking for full resolutions, we screened about 40 more articles: three
read-only scouts plus direct parent reading. We then pursued four exact numbered questions with
the same HMZ + Lean + `math/` method. Screening reports, parent source checks, Comparator
packages and replays are in
[`evidence/mathematics-more-20261014/`](evidence/mathematics-more-20261014/); the summary is
[`parent-verification.json`](evidence/mathematics-more-20261014/parent-verification.json).

| # | Exact question | Book problem (authors) | Book pages (PDF pages) | Outcome on 2026-10-14 | Directory |
|---|---|---|---|---|---|
| 6 | Questions 2 and 3: which left-divisible filters/semifilters L give exactly the regular languages, and when do two of them give the same class? | 关于半群上一类重要同余的一个系列推广模式 (郭聿琦, 王守峰) | 61–63 (77–79) | **Both questions answered in writing, for every finite alphabet.** R_L = Reg iff every member of L is regular; for filters, iff every member is cofinite, i.e. exactly the filters {A : A^c is a finite subset of U} with U suffix-closed. R_L1 = R_L2 iff the complements of each family's members have finite mod-2 expressions K + Σ P_i a_i B_i over the other family. Independent Opus referee: correct with minor fixes (applied). **HMZ accepted** (reviewer `done:true`, `how:"done"`, `ok:true`), the only acceptance in either round. Lean (4 roots, Comparator-accepted) covers the residual elimination and the series-level criteria; the translation from semifilters, the parity normal form and the filter classification are written proofs. **Not shown to be new:** full texts of Guo–Wang–Shum 2017, Wang 2021 and Guo–Liu–Wang 2024 were inaccessible. Questions 4–5 are not addressed. | [`prodinger-semifilter-languages/`](prodinger-semifilter-languages/) |
| 7 | Question 3: Gröbner–Shirshov bases of the free dendriform dialgebra and trialgebra | 一些代数的 Gröbner–Shirshov 基 (L. Bokut, 陈裕群) | 83 (99) | **Already solved by prior work.** Trialgebra: Bagherzadeh–Bremner–Madariaga, J. Algebra 486 (2017), Lemma 6.1 (parent read the primary text). Dialgebra: Chen–Wang 2010 and Madariaga. Reproduced with an all-arity written proof, all 15 critical pairs (Lean, Comparator-accepted, plus a parent reconstruction) and a Codex referee. No HMZ run. | [`dendriform-trialgebra-gs/`](dendriform-trialgebra-gs/) |
| 8 | Olson's ordered EGZ conjecture: every length-(2n−1) sequence in a group of order n has n terms, in their original order, with product 1 | 有限阿贝尔 (Abel) 群的 Davenport 常数 (孙智伟) | 141–142 (157–158) | Open. Known for all p-groups (Dimitrov 2004). Lean: the known one-short odd-dihedral bound, and the conjecture for every finite group restricted to words a^(n−1) c b^(n−1). No counterexample among words with at most three runs in two order-12 groups; unrestricted searches ended UNKNOWN. HMZ stopped (three `done:false` reviews). | [`olson-ordered-egz/`](olson-ordered-egz/) |
| 9 | Question 1: does Shor's 16-word code have a finite completion? | 关于有限码具有有限完备化的判定问题 (郭聿琦, 刘云) | 64–65 (80–81) | Open. Written proofs: a completion forces cyclic tilings for every t and a pure power a^n with 1320 \| n (the published minimum n ≥ 1320 is unchanged); n ≥ 19800 if Szabó 2006, Theorem 7 holds, which could not be authenticated. Lean covers the arithmetic only. HMZ stopped (two `done:false` reviews). | [`shor-code-finite-completion/`](shor-code-finite-completion/) |

So this batch gives one new candidate full answer (target 6), whose novelty is unresolved; one
question already answered in the literature (target 7); and two still-open problems with
partial results. The parent replayed every Lean root through fresh-module Comparator (10
roots in 6 configurations, all accepted); a one-definition mutation was rejected. Each
target's own checkers were replayed, and the HMZ journals were parsed directly.

The new screen also found more questions answered after publication. The parent read the
primary sources for: rational-SOS Question 2 (negative,
[Scheiderer 2016](https://doi.org/10.4171/JEMS/620)); osp characters
([Gruson–Serganova, arXiv:0906.0918](https://arxiv.org/abs/0906.0918)); and the Alekseevskii
conjecture inside 齐性爱因斯坦流形
([Böhm–Lafuente, arXiv:2107.04210](https://arxiv.org/abs/2107.04210)). Scout-reported, not
re-read by the parent: Hough's minimum-modulus theorem for coverings, Aut of Witt algebras
(Bavula), topological similarity of periodic matrices (Hambleton–Pedersen), Kawohl's hot-spots
conjecture (false in high dimension), Chvátal's conjecture (unrefereed 2026 preprints) and GS
Question 4. The openai/math titles also suggest overlaps not compared with the book statements:
hot spots for simply connected planar domains (369), the generalized Lax conjecture (095),
Penrose (260), Iitaka (033), Nagata (039), Griffiths (050), Arnold (347), surfaces in R⁴ (333),
Hilbert's 16th (143) and the Erdős reciprocal-sum conjecture (159).

### Screened out

Solved after the book was published:

- 极小塔问题 (p = t): [Malliaris–Shelah, arXiv:1208.5424](https://arxiv.org/abs/1208.5424),
  J. Amer. Math. Soc. 29 (2016).
- 关于奇数阶阿贝尔群的 Snevily 猜想: [Arsovski, Israel J. Math. 182 (2011)](https://doi.org/10.1007/s11856-011-0040-6).
- 凸多面体的 d-步猜想: false, via [Santos's Hirsch counterexample](https://arxiv.org/abs/1006.2814),
  Ann. of Math. 176 (2012).
- 旅行商问题性能比小于 1.5 (metric TSP): [Karlin–Klein–Oveis Gharan](https://arxiv.org/abs/2007.01409),
  STOC 2021; randomized approximation, not exact TSP.
- 紧闭包与局部化相交换: false, [Brenner–Monsky, Ann. of Math. 171 (2010)](https://doi.org/10.4007/annals.2010.171.571).
- 球面上的 g-猜想: [Adiprasito](https://arxiv.org/abs/1812.10454);
  [Papadakis–Petrotou](https://arxiv.org/abs/2012.09815), for simplicial spheres.
- LKTS(21), the book's smallest open order: Zhou–Chang (2010). The July 2026 literature
  statement lists 57 and 87 as the remaining admissible orders below 200
  ([Chen Wang, arXiv:2607.21521](https://arxiv.org/abs/2607.21521)).
- DFP 拟牛顿法的收敛性: false — a 2-D C² strongly convex counterexample under the strong Wolfe
  conditions, [Liu–Wang–Wen–Zhang–Yuan, arXiv:2608.21708](https://arxiv.org/abs/2608.21708)
  (August 2026 preprint).

Claimed in the openai/math corpus, not re-verified here. Lean families (numbers from
`math/lean/docs/`): Seymour's second-neighborhood conjecture (173), Koebe's circle-domain
conjecture (071), Brennan (072), Rokhlin's multiple mixing (145), rigidity of the Turing degrees
(241), circulant Hadamard (179), finitistic dimension (198) and Auslander–Reiten (199). Preprint
only: a counterexample to Hadwiger's conjecture (`math/preprints/`, September 2026).

An October 2026 search result claimed an n=5 Atiyah–Sutcliffe proof, but the record and API
returned HTTP 403. That claim was not verified and is **not counted as an established solution**.

Too hard for a bounded attempt: the remaining opening logic and set-theory problems (Vaught,
canonical inner models for supercompacts, CH, the singular cardinals problem); RH, Goldbach, BSD
and the Langlands program; union-closed sets, reconstruction and Ryser; Navier–Stokes and
Yang–Mills; large searches (Hadamard order 668, R(5,5), a projective plane of order 12,
Erdős–Szekeres f(7)); Smale's mean value conjecture; Valiron's common Borel direction problem; an
OPT + 1 bin-packing algorithm.

Not precisely posed: numerical-method programs, statistical-modelling directions and multiscale
modelling items.

## Physics volume

Source volume: 《10000个科学难题·物理学卷》 (10000 Selected Problems in Sciences: Physics,
Science Press, 2009, ISBN 978-7-03-024269-3), local copy
`/Users/jinleic/Documents/中文pdf/10000个科学难题·物理学卷(10000个科学难题物理编委会).pdf`
(876 PDF pages; the table of contents is on PDF pages 9–18; PDF page = book page + 33 for book
pages 183–579 and + 35 for 580–704).

### Current reselection (2026-10-14)

The user subsequently chose **“Re-select with explicit open statements.”** Five replacement
packages now contain complete classical arguments, source/SOTA screens, independent reviews and
passing parent replays; their exact outcomes are indexed in
[PHYSICS_RESELECTION.md](PHYSICS_RESELECTION.md). All are **Certification** results with
**uncertified novelty/priority**, not five priority-certified discoveries or full book-chapter
solutions. Three targets come from one Tevet paper, and the supersoliton result addresses only
the selected generic criterion. The five earlier proof packages below remain preserved but do
not count toward the replacement five; the already-solved SO(5) candidate is also excluded.

### Earlier narrowed intake (selection gate not passed)

The opening table of contents and about 40 candidate sections were screened. Five workers first
investigated cone packing, bilinear integrability, fractional parentage, optical invariance and
quantum codes. That first pass did **not** establish five easy, literature-open chapter problems.
The user then explicitly chose **“Choose precise open subproblems”** rather than keeping the
chapter-scale questions or restarting the full-volume screen.

The five focused proof obligations below come from **three book chapters**. Two distinct parity
branches concern the same integrability chapter; two different state families concern fractional
parentage. None was proved in the first-pass package. In the prior-art screen run on 2026-10-14,
none of the primary sources we could access settled the exact scoped statements. However, some
key primary texts could not be accessed (for example, the full Peng et al. (2008) paper), so their
openness and novelty remain **uncertified**. “Accessible” means that each target reduces to a finite
symbolic computation or a specific proof identity. It does not guarantee that the theorem is easy,
novel or previously unknown. Each directory records its own verdict and independent review.

**Still-unsolved selection gate: NOT PASSED (blocked on inaccessible primary sources).** All five
proofs are complete, independently reviewed and replayed, but none of the five statements is
certified as historically unsolved. Each was **previously unproved in this project**; no checked
primary source explicitly declares the exact statement open. Final comparisons are recorded in each
target's STATUS.md under “Openness gate (final, 2026-10-14)”. Inaccessible sources are listed there
and are not treated as negative evidence.

| # | Scoped proof target | Book chapter; book pages (PDF pages) | Openness gate | Directory |
|---|---|---|---|---|
| 1 | Spin-2 low-total-spin CFPs (L ≤ 5), all seniorities: 24 squared-coefficient formulas and two block weights | 母配分系数递推关系的破解 (鲍诚光); 348–349 (381–382) | No settling source among those checked; Kishimoto–Tamura 1971, Arima–Iachello 1976, Talmi 1993 pp. 763–771 and others inaccessible | [`phys-fractional-parentage-coefficients/`](phys-fractional-parentage-coefficients/) |
| 2 | General-spin near-stretched CFPs at deficit five: f ≥ 3, L = fv − 5, v → v−1 | Same chapter; 348–349 (381–382) | No settling source among those checked; Sun et al. 1989, Bayman–Lande 1966 tables, Kishimoto–Tamura 1971 and Talmi 1993 inaccessible | [`phys-parentage-deficit-five/`](phys-parentage-deficit-five/) |
| 3 | Odd-cubic two-function bilinear system: arbitrary-amplitude Pfaffian tau formula for all N | 关于得到高维可积模型的一个新猜想 (楼森岳, 李金花); 350–351 (383–384) | Partial overlap: equation and three-soliton structure in Hietarinta (1987/1997); Peng et al. 2008 reports Wronskian N-solitons (full text inaccessible) | [`phys-bilinear-higher-dim-integrability/`](phys-bilinear-higher-dim-integrability/) |
| 4 | Mixed-parity bilinear system (c₂ ≠ 0): all-N tau formula for arbitrary F/G seed patterns | Same chapter; 350–351 (383–384) | Partial overlap on both branches: c₃ ≠ 0 is gauge-equivalent to the odd-cubic pair; c₃ = 0 is Li–Lou model (ii); same inaccessible sources | [`phys-bilinear-mixed-parity/`](phys-bilinear-mixed-parity/) |
| 5 | Fresnel polarization-degree invariance for sector-diagonal sources in LG modes n = 0, 1, orders ±m | 光传播中的光谱不变性和偏振不变性 (赵道木); 333–334 (366–367) | No settling source among 24 checked; Li 2015, Zhao–Wolf 2008, Gori 2008 and others inaccessible | [`phys-spectral-polarization-invariance/`](phys-spectral-polarization-invariance/) |

### Screened out

Retained but rejected as active “not-too-hard” selections:

- [Cone/Fibonacci packing](phys-fibonacci-cone-spirals/): the fixed-golden-angle ansatz has a
  certified counterexample, but this does not settle every Fibonacci-contact configuration or the
  experimental elastic-energy problem. Its sharp number-theoretic packing-density law also has
  [2024 prior art](https://arxiv.org/html/2106.12333v8); it is not a fresh open target.
- [Small quantum codes](phys-quantum-code-construction/): the unrestricted rank-three/rank-five
  existence questions remain open in the checked tables, while the tested CWS classes were
  already excluded in stronger prior work. Reproductions are preserved but not counted as
  solutions or as evidence that the unrestricted problems are easy.

Already settled (some before, others after the book was published):

- 一维量子自旋链系统在任意边界磁场中的严格解: off-diagonal Bethe ansatz, Cao, Yang, Shi, Wang,
  Nucl. Phys. B 877, 152 (2013) (arXiv:1307.2023).
- 梯度方法能否用于求解 Dirac 方程?: yes; the inverse Hamiltonian method avoids variational collapse
  (e.g. Ren et al., Phys. Rev. C 95, 024313 (2017), Dirac equation on a 3D lattice).
- 五夸克态是否存在?: LHCb, Phys. Rev. Lett. 115, 072001 (2015).
- 介观环中的持续电流的实验观测值与理论值有较大差距的疑难: Bleszynski-Jayich et al., Science 326, 272
  (2009), measured currents agree with theory.
- 量子信道, additivity of the classical capacity: false, Hastings, Nature Phys. 5, 255 (2009).
- 用"瓦特天平"法实现量子质量基准 and 用基本物理常数建立国际单位制 SI 的基本单位: the 2019 SI
  redefinition fixed h, e, k and N_A.
- Yangian 表示论与求解非线性模型, Haldane–Shastry part: Haldane, Ha, Talstra, Bernard, Pasquier,
  Phys. Rev. Lett. 69, 2021 (1992).
- 能否利用随机共振机制提高弱信号接收的信噪比: largely settled for weak signals by Fisher-information
  bounds (Duan, Chapeau-Blondeau, Abbott, PLoS ONE 7, e34282 (2012)).

Too hard for a bounded attempt: exact solutions of 3D many-body models; the QMC sign problem; the
high-T_c pairing mechanism; a rigorous Fourier law and the 1D anomalous heat-conduction exponent;
turbulence; quantum capacities of general channels; exact solutions of quantum field theories; a
Yangian-only solution of the Hubbard spectrum; spin-liquid ground states of J1–J2 models.

Not precisely posed: most astrophysics, acoustics, nuclear-structure, materials and device items,
and conceptual questions such as 为什么严格的多体波函数计算不能给出超导态 (answered by off-diagonal
long-range order, Yang, Rev. Mod. Phys. 34, 694 (1962)).
