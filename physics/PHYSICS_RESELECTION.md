# Physics reselection: explicit published questions

Snapshot: 2026-10-14 (America/Los_Angeles).

The user chose **“Re-select with explicit open statements.”** This index tracks that replacement
research, not the earlier five certification-only targets. Those earlier results and their failed
historical-openness gates remain preserved in their original directories and in the Physics section
of [README.md](README.md#physics-volume).

## Selection rule

An eligible question must have an explicit primary-source open/conjectural/unproved statement,
a check of later citing work, and a bounded mathematical attack. A search miss is not evidence of
novelty. “No resolution identified in the checked sources” is a dated search result, not a guarantee
about all literature. Preprints, older empirical formulas, and established mathematical ingredients
are labeled separately in each target's `STATUS.md`.

The book connection is to two chapters in *10000 Selected Problems in Sciences: Physics*
(Science Press, 2009): higher-dimensional bilinear constructions (book pp. 350–351; PDF
383–384) and Fibonacci/cone arrangements (541–543; PDF 574–576). Four selected questions concern
phyllotaxis-related geometry, and one concerns a supersymmetric soliton criterion. The precise
questions occur in related primary papers; they are **not five separate questions quoted verbatim
from the 2009 book**, nor equivalent formulations of its full chapter goals.

## Completed replacement results

All five folders now contain complete classical arguments for their stated targets, source/SOTA
screens, exercised scientific checks and independent review dispositions. Their evidence label is
**Certification**; worldwide novelty/priority remains **NOVELTY-UNCLEAR**. Three distinct questions
come from the same Tevet paper; these are not five independent literature areas.

| # | Exact research target and package | Explicit primary question | Delivered result |
|---|---|---|---|
| 1 | [Spiral dense forest](phys-spiral-dense-forest/README.md): existence with exact radii sqrt(k) | Tevet (2025), Further Questions p. 12 conjectures existence, contrasting an earlier negative conjecture | A norm-ranked union of two rotated grids gives a spiral dense forest, with visibility uniform over all positions and orientations. The proof handles tied shells, the finite core and open rectangle boundaries. |
| 2 | [Fermat Chabauty classification](phys-fermat-chabauty-classification/README.md): translation-limit types and covolumes | Tevet (2025), Remark p. 4 and Further Questions p. 12 conjecture the non-badly-approximable limit types and ask about covolumes | Every nonempty limit is an affine line or a covolume-pi affine lattice; mixed continuous/discrete groups and the plane are excluded. Every fixed irrational non-BA angle has empty, line and lattice limits. |
| 3 | [Fermat lattice universality](phys-fermat-lattice-universality/README.md): realize each covolume-pi lattice | Tevet (2025), Further Questions p. 12 explicitly leaves universal realization open | For each target lattice, one fixed badly approximable angle realizes it and all its rotations and affine translates, using translations only. The angle may depend on the target lattice. |
| 4 | [Spiral Delone density](phys-spiral-delone-uniform-density/README.md): exact radii k^(1/n) and asymptotic density on every bounded Jordan set | Adiceam–Tsokanos (2021 preprint version), §6 pp. 22–23 explicitly leave existence with asymptotic density open | Norm-ranking the integer lattice yields global separation, covering, uniform directions and density 1/V_n in every fixed n >= 2, hence all requested n >= 3. |
| 5 | [Generic three-super-soliton obstruction](phys-supersoliton-degree-obstruction/README.md): the selected mixed-seed criterion for the paired system | Wang–Tang–Liang (2018), §4 propose the all-n hypothesis and suggest three-super-solitons as a test for n > 3; they do not specify the selected generic ansatz | For every n >= 4, an exact F–F–G body obstruction rules out the generic mixed-seed square-free-exponential family, even with nilpotent dressings. Restricted solutions and symmetry integrability are not excluded. |

Each target's `RESULTS.md` owns its complete statement, proof, evidence limits and review
dispositions; `STATUS.md` owns the exact source quotations and citation-screen coverage.

For target 5, failure of the generic soliton test is **not** a proof that no infinite generalized-symmetry
hierarchy exists. The source's symmetry-integrability hypothesis and its proposed soliton criterion
must remain distinct.

For target 4, the exact density normalization must be read from the original formula and the source's
counting definition. PDF text extraction can confuse V_n^(-1) with V_(n-1); the unit-ball count fixes
the normalization. Uniform direction distribution alone does not establish separation or covering.

## Verification and remaining limits

Parent replays passed for all five packages. Scripts that write receipts were replayed in copies
under [`evidence/physics-reselection-20261014/`](evidence/physics-reselection-20261014/), preserving
the canonical results. The universality smoke was run without its optional `--write` flag.

| Target | Exercised parent replay |
|---|---|
| Dense forest | 25,704 norm sanity checks; two enumerators at radii 8, 16, 32, 64; 6,400 direction pairs; 257 squared-radius thresholds; exact rational displacement bounds and negative controls. Both generated result files matched the delivered files byte-for-byte. |
| Chabauty classification | 42 interval cases; 29,368/29,067 local points; 66 absolute-Cartesian comparisons; 36 determinant cases; two Liouville witnesses; six controls; eight source hashes. |
| Lattice universality | Four quadratic fixtures; 12 convergent bases; 300 forward and 300 paired reverse patch checks; 36 phase windows; three negative-control families. |
| Delone density | Five PASS groups, including independent exact enumeration, tie, normalization and negative controls. |
| Supersoliton obstruction | Exact n=4/n=5 witnesses, n=2/n=3 boundary bodies, parameter projection and exterior-algebra controls, finite integer certificate and all-degree tail inequality. |

Finite checks supplement the written proofs; they do not establish the universal quantifiers.
The dense-forest sampled segments and the universality numerical patches are explicitly empirical.
The final read-only Codex integration audit returned **ready**, with no established defect in its
permitted review scope; its report is preserved at
[`final-codex-review.md`](evidence/physics-reselection-20261014/final-codex-review.md).

Historical openness and first priority remain uncertified: some journal bodies are subscription
blocked, citation indexes are incomplete, and a bounded search cannot establish absence of prior
solutions. No Lean/kernel verification or human peer review is claimed. The next scientific action
is specialist correctness/priority review, not another numerical search. The full book chapters,
cone-energy minimization, optimal visibility and unrestricted supersymmetric integrability remain
outside these results.

A later comparison with the current literature, including a significance calibration for each
target, is in [`evidence/physics-sota-audit-20261014/`](evidence/physics-sota-audit-20261014/README.md).
Verdict: no major contribution. Forest and universality are modest specialist answers to explicit
questions; density is a companion construction; classification is mostly a corollary of
Bacher (2014); the supersoliton result is a scoped no-go. Working files from the earlier physics
intake are in [`evidence/physics-intake/`](evidence/physics-intake/).


## Primary sources

- Caprio, Rowe and Welsh, *Construction of SO(5)⊃SO(3) spherical harmonics and Clebsch–Gordan
  coefficients*, CPC 180 (2009): [arXiv:0902.0020](https://arxiv.org/abs/0902.0020), §2.5 Eqs. (26)–(29).
- Welsh and Rowe, subsequent ACM implementation (2016):
  [arXiv:1408.3824v3](https://arxiv.org/html/1408.3824v3), §IV Eq. (45).
- Yohay Ailon Tevet, *Chabauty Limits of Fermat Spirals*, *Combinatorics and Number Theory*
  **14**(3–4), 239–249 (2025), DOI [10.2140/cnt.2025.14.239](https://doi.org/10.2140/cnt.2025.14.239).
  The audited text is [arXiv:2506.22863v2](https://arxiv.org/pdf/2506.22863v2);
  the subscription-blocked journal body was not compared.
- Faustin Adiceam and Ioannis Tsokanos, *Higher Dimensional Spiral Delone Sets*:
  [arXiv:2010.06428v3](https://arxiv.org/pdf/2010.06428v3), §6.
- Faustin Adiceam and Ioannis Tsokanos, *Visibility properties of spiral sets*, *Moscow Journal of
  Combinatorics and Number Theory* **11**(2), 149–159 (2022):
  [arXiv:2111.01843v1](https://arxiv.org/abs/2111.01843v1), introduction after Figure 1.
- Jian-Yong Wang, Xiao-Yan Tang and Zu-Feng Liang, *Constructing (2+1)-dimensional N=1
  supersymmetric integrable systems from the Hirota formalism in the superspace*, CPB 27 (2018)
  040203: [primary full text](https://cpb.iphy.ac.cn/en/article/pdf/preview/10.1088/1674-1056/27/4/040203.pdf).

## Rejected replacement leads

- Caprio–Rowe–Welsh's 2009 SO(5) reduced-matrix formula: despite the explicit “unproved”
  wording and later empirical descriptions, the exact content has an equivalent pre-2009
  class-one SO(n) 3j formula (Ališauskas 2005, referring to Junker 1993). The convention-matched
  proof is preserved at [phys-so5-reduced-matrix-conjecture](phys-so5-reduced-matrix-conjecture/README.md)
  as Certification/ALREADY-SOLVED, and is **not** counted toward the five replacements.

- Pan et al. (2014) polynomiality remark: the literal normalized coefficients already have square
  roots in the source's tables, while a charitable rational-squares formulation is elementary.
  A hedged, imprecise remark is not counted as an unresolved theorem.
- Lou's 2022 deformation conjecture: the Lax-integrability transfer has a later proof by
  Casati–Zhang (2023); its imprecise residual soliton directions are not counted.
- Akiyama's broad higher-dimensional existence question: Adiceam–Tsokanos already construct
  higher-dimensional Delone spirals. Only their additional **uniform-distribution/density** question
  is retained above.
- The 2025 electromagnetic cross-spectral-purity extension: its separability definition is ambiguous
  and a directly relevant 2026 paper is inaccessible. It does not earn a replacement slot.
