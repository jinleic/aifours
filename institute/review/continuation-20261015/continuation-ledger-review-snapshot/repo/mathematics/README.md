# Mathematics volume

Source volume: 《10000个科学难题·数学卷》 (10000 Selected Problems in Sciences: Mathematics,
Science Press, 2009, ISBN 978-7-03-024267-9). Local copy: [`books/`](../books/README.md), not
tracked by Git; 568 PDF pages; the table of contents is on PDF pages 9–16; PDF page = book page + 16.

Each target directory owns its own status, sources, evidence and claims. This index only routes.
Round-level screening, parent checks, HMZ/Lean replays and review dispositions live in
[`evidence/`](evidence/). [Repository overview](../README.md).

## Selection (2026-10-14)

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
The workspace's openai/math corpus (`/Users/jinleic/jinleic-workspace/math/`) was used as a source of proof techniques and Lean patterns; no OAI
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

All five targets were also screened against the workspace's openai/math clone (`/Users/jinleic/jinleic-workspace/math/`, commit
adc7f1241, 2026-10-06) and the remote repository's newer families and preprints listed on
2026-10-14: none covers them. That corpus claims solutions to many other problems in this book
(for example Seymour, Hadwiger, Koebe, Brennan, Rokhlin's multiple mixing, Turing-degree
rigidity, circulant Hadamard, finitistic dimension and Auslander–Reiten).

## Second batch: four more exact questions (2026-10-14)

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

## Screened out

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
`/Users/jinleic/jinleic-workspace/math/lean/docs/`): Seymour's second-neighborhood conjecture (173), Koebe's circle-domain
conjecture (071), Brennan (072), Rokhlin's multiple mixing (145), rigidity of the Turing degrees
(241), circulant Hadamard (179), finitistic dimension (198) and Auslander–Reiten (199). Preprint
only: a counterexample to Hadwiger's conjecture (`/Users/jinleic/jinleic-workspace/math/preprints/`, September 2026).

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

## Difficult-problem visit (2026-10-15)

The owner requested one difficult mathematics problem with a six-hour total ceiling, alongside one
information-science and one physics visit. The [hard-problem catalog](evidence/mathematics-hard-20261015/catalog.md)
records candidates, status sources, budget classes, feasibility probes and parent-review restrictions.

Selected `math-p0039`, **凯莱 (Cayley) 图和相关的问题** (李才恒, book pp. 39–40; PDF pp. 55–56):
the geometric nonexistence of non-Desarguesian flag-transitive projective planes explicitly discussed
in the article. The printed diameter-two graph claim and its unspecified-generator equivalence are
inconsistent; the target is instead formalized using Kantor and Thas–Zagier, with those premises declared.
A finite range extension remains partial, and sampled independent checks do not certify the whole range.

The [institute run](../institute/runs/hard-2026-10-15/README.md) first ran at 04:03 PT and closed
**unverified**: its key production logs were absent from the replay snapshot. With owner approval it
resumed at 12:02 PT from the attack stage with a fresh six-hour allocation and the recovered logs.
Authority for those engine visits: [`record.json`](../institute/runs/hard-2026-10-15/problems/math-p0039/record.json).
Its batch 03 continuation closed **unverified** (accept-with-fixes) at 17:35 PT with a partial,
conditional result. Assuming the Kantor, Thas–Zagier and Feit premises, a sandbox-replayed exact
recomputation then excluded orders `n < 251,539,607,552`; the larger C-run ranges were empirical reports.
The all-orders conjecture remains open. See the [outcome ledger](../institute/review/hard-2026-10-15-outcomes.md).

### Authorized continuation (2026-10-16)

The [new exact replay](evidence/hard-continuation-20261015/README.md) reaches
**n < 2,582,236,504,064**, under the same Kantor/CFSG, Thas–Zagier reduction and valid Feit
premises. It recomputed `[8,2e11)` from scratch, removing dependence on Thas–Zagier's unreplayed
low-range search; the earlier exact Python prefix is imported through pinned records.
The new segments cover 105,445,704,021 progression members. Every rejection has a checked proper
factor, a full non-one modular residue, or an explicit difference collision. Libmpdec cross-checks
and parent GMP samples are separate evidence; samples do not certify the whole interval.

A reviewed Sidon theorem shows why forced-subgroup difference-collision searches cannot exclude
power-of-two orders; it does not prescribe every possible successful method. No novelty is asserted
for that observation. The all-orders conjecture remains open. See the
[continuation ledger](../institute/review/continuation-20261015/outcomes.md) for coverage, premises,
review limits and attribution. The original engine record is unchanged.

