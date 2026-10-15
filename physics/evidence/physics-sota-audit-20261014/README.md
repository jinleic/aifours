# Physics reselection vs. state of the art

Snapshot: 2026-10-14 (America/Los_Angeles). Question: compared with the current literature, are
the five [physics reselection](../../PHYSICS_RESELECTION.md) results major contributions?

**No major contribution.** Major would mean a new method, a long-standing or prominent problem, a
quantitative gain over the state of the art, or a physical result; none of the five qualifies.
They answer recent, explicitly posed questions in a small specialist literature, mostly with known
tools. Conditional on human review and priority checks: forest and universality are modest
specialist results, density is a companion construction, classification is mostly a corollary of
Bacher (2014), and the supersoliton result is a narrow no-go.

## Comparison

| Result | State of the art before us | What we add | Calibrated value |
|---|---|---|---|
| [Spiral dense forest](../../phys-spiral-dense-forest/README.md) | Open. Adiceam–Tsokanos ([arXiv:2111.01843v2](https://arxiv.org/abs/2111.01843), 2022) conjectured that **no** spiral dense forest exists. Tevet ([arXiv:2506.22863v2](https://arxiv.org/abs/2506.22863), 2025) conjectured that one does; his Cor. 7 shows no Fermat spiral is one. Kashkan's 2025 Toronto PhD [thesis](https://utoronto.scholaris.ca/server/api/core/bitstreams/55a695f1-6642-433d-b023-ffcc9f69ce52/content) (p. 21) calls existence unknown. Lattice-union forests are known ([Shirandami 2023](https://arxiv.org/abs/2303.14719)). | An explicit example: a norm-ranked union of two rotated lattices with exact radii √k. No earlier equivalent was located in the bounded screen. Settles the planar question and refutes the 2022 conjecture. | Strongest of the five, but short: Tevet's Prop. 6 and his suggested Chabauty route make the transfer routine. No explicit visibility rate; not uniformly discrete. Modest specialist result. |
| [Lattice universality](../../phys-fermat-lattice-universality/README.md) | Tevet characterized the limits for one fixed badly approximable angle and asked whether every covolume-π lattice occurs. Local lattices and area π: [Bacher 2014](https://www.numdam.org/item/10.5802/cml.10.pdf). Winning sets: [McMullen](https://abel.math.harvard.edu/~ctm/papers/home/text/papers/winning/winning.pdf). | Yes: each target lattice, with all rotations and translates, arises from one angle with bounded continued-fraction digits. Target dependence of the angle is provably necessary. | Complete answer to an explicit question, using one non-elementary published input. A dynamics specialist may read it as known bounded-geodesic facts translated through Bacher's picture [INFERENCE]. |
| [Higher-dimensional spiral density](../../phys-spiral-delone-uniform-density/README.md) | Adiceam–Tsokanos ([arXiv:2010.06428](https://arxiv.org/abs/2010.06428) v1/v3) asked whether, for n ≥ 3, a spiral Delone set can have asymptotic density. No later restatement or resolution was found in the checked sources; n = 2 was known. | Yes for every n ≥ 2: norm-ranking ℤⁿ gives a Delone spiral with #(S∩RX)/Rⁿ → λ(X)/V_n for every bounded Jordan-measurable X. Origin-centred ball counts are automatic and are not the content. | Answers the literal question with classical ingredients: Landau–Hlawka counts, the [“well known”](https://arxiv.org/abs/0706.4395) equidistribution of lattice directions, density under bounded displacement. Corollary-level; same mechanism as the forest. |
| [Fermat limit classification](../../phys-fermat-chabauty-classification/README.md) | Tevet (p. 4) conjectured that for angles that are not badly approximable the nonempty limits are ℝ, ℤ² and ℤ×ℝ, “in particular the limit cannot be R²”. On p. 12 he added that computation suggests all listed types occur, and asked whether the lattices have covolume π. Bacher 2014, absent from Tevet's arXiv-v2 bibliography, already gives local lattices of area π. | Nonempty limits are only affine lines and covolume-π affine lattices; every irrational non-BA angle has empty, line and lattice limits. Excluding ℝ² **confirms** Tevet's conjecture. Excluding ℤ×ℝ contradicts only his computational suggestion that every listed type occurs, not the containment conjecture. | Mostly a corollary of Bacher (2014); a supporting proposition. |
| [Supersoliton obstruction](../../phys-supersoliton-degree-obstruction/README.md) | [Wang–Tang–Liang 2018](https://cpb.iphy.ac.cn/en/article/pdf/preview/10.1088/1674-1056/27/4/040203.pdf) hypothesized integrability for all n and suggested a three-super-soliton test without fixing an ansatz. Delisle–Jaouadi ([arXiv:2609.14372v1](https://arxiv.org/abs/2609.14372), 2026 preprint) classify single-tau equations only. | For every n ≥ 4: no generic F–F–G family with square-free bodies, even with arbitrary nilpotent dressings. | Narrow and interpretation-dependent. The super part is the earlier bosonic result plus the standard fermionic-limit reduction used by the 2018 paper. Odd-n polarized sectors, including F = G, are not excluded; constrained bosonic n = 5 families were known (2024). Symmetry integrability is untouched. |

Scope:

- The forest and density constructions use arbitrary directions with exact radii. They meet the
  sources' deliberately broad spiral-set definitions; they are not phyllotactic or dynamical
  spirals. The forest set is not uniformly discrete. The density set repeats directions and is not
  the orbit of a map.
- Visibility benchmark: for general finite-density planar forests the best bound is
  O(ε⁻¹ log ε⁻¹) ([Kashkan](https://arxiv.org/abs/2407.01633)); O(ε⁻¹) is equivalent to the planar
  Danzer problem. The forest result is existence only.
- None of this addresses the book's physics question (least-energy Fibonacci patterns on cones).
  Physical work there is numerical ground-state and defect modeling, e.g.
  [Ansell–Tomlinson–Wilkin 2020](https://www.nature.com/articles/s41598-020-74158-x).

Framing: (A) norm-ranking spiral constructions (forest + density), one mechanism and one shared
priority risk; (B) translation limits of Fermat spirals (universality, with classification as a
proposition crediting Bacher first); (C) a scoped supersoliton no-go.

## Stronger directions

Whether any of these would be major depends on the method and quantitative gain achieved.

- A spiral dense forest with an explicit near-optimal visibility rate, or a Danzer spiral set
  (Tevet's follow-up questions).
- A Delone spiral dense forest with an explicit rate. [INFERENCE: this mechanism plus an existing
  lattice-union forest may give a polynomial rate, far from the frontier.]
- Akiyama's question: a Delone spiral generated as the orbit of a map; asymptotic density would be
  a further requirement.
- A classification of supersymmetric mKdV-type bilinear equations, left open by Delisle–Jaouadi.

## Next steps

1. Forest and density: human specialist review plus one shared priority check (Adiceam's 2023 HDR,
   the journal text of the density paper, Berestovskii 2005, and
   [MathOverflow 24850](https://mathoverflow.net/questions/24850), a 2010 suggestion to number
   lattice shells, with no radius rescaling and no proof). [INFERENCE, unproved: the same method
   likely gives spiral dense forests in every dimension.]
2. Universality: ask a homogeneous-dynamics specialist whether the key step (a bounded geodesic
   through any point plus continued-fraction concatenation) is folklore; read the 2025
   *Mathematical Phyllotaxis* book and Tevet's journal version (paywalled).
3. Fold classification into the universality write-up. Keep the soliton note scoped, and check
   Hietarinta's 1990 chapter, which may already cover n = 5.

## Evidence

| Path | Content |
|---|---|
| [`parent-evidence.json`](parent-evidence.json), [`physical-context.json`](physical-context.json) | Primary sources read directly by the parent, with read scope and limits |
| [`evidence/`](evidence/) | Literature audits: `ForestSota.md`, `DensitySota.md`, `SolitonSota.md` (verified quotes, URLs, `unverified_or_dropped`) |
| [`assessment-draft.json`](assessment-draft.json); `review-prompt.txt`, `review-result.json`, `review-receipt.json`, `claude-*` | Provisional assessment and its read-only Claude `claude-opus-5-5` review (ready-with-fixes) |
| [`review-snapshot/`](review-snapshot/) (`manifest.json`); `codex-final-*` | Pinned 23-file snapshot and the read-only Codex `gpt-6.1-sol` review of the answer draft (ready-with-fixes) |

This file is the corrected final comparison. It supersedes `review-snapshot/final-answer-draft.md`,
which is preserved unchanged as the reviewed input. After both reviews, one more error was found:
the draft credited the exclusion of ℝ² as a correction of Tevet, whereas it confirms his p. 4
conjecture (see [classification STATUS](../../phys-fermat-chabauty-classification/STATUS.md)
§1).

Limits: only AI models have checked the proofs (two vendors for forest and universality, one for
the others); there is no human review. Publisher texts of Tevet and both Adiceam–Tsokanos papers
are paywalled. A failed search does not establish priority.
