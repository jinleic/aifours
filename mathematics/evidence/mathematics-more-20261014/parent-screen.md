# Additional mathematics-volume screen

Date: 2026-10-14 PT. Goal: check additional exact questions from the same mathematics volume for full resolution, continuing the HMZ + Lean + read-only `math/` reference method. This round does not rework the original five targets. No claim of guaranteed tractability, current openness or novelty follows from a failed search.

## Selection and source checks

The original extracted full book text `/tmp/math10000_full.txt`, the preserved first-round contents `../mathematics-intake/book-contents.txt` and corpus title inventory `/tmp/oai_math_titles.tsv` were reused rather than re-extracted. Original PDF provenance remains in `../mathematics-intake/parent-spot-checks.md`. Book page + 16 = PDF page.

Three read-only scouts screened disjoint sections; their reports are retained verbatim in `algebra-screen.md`, `discrete-screen.md` and `analysis-screen.md`. They include their own primary-source access limitations and unreviewed proof suggestions, not accepted conclusions. The parent additionally read the rational-SOS, minimax-quadratic, phase-type, high-order FEM, optimal-tessellation, osp-character, Kac–Weisfeiler, homogeneous-Einstein, symplectic-Dirac and affine-flat articles. This is a targeted further screen, not a claim that every article has been fully read.

Four proof/counterexample investigations were selected:

| Target | Exact book question | Scope and acceptance |
|---|---|---|
| Dendriform trialgebra GS basis | Bokut–Chen Question 3, p. 83 (PDF 99) | Explicit GS basis for the free noncommutative trialgebra over a field, every arity and generator set; the dialgebra half is separately compared with known work. A finite rank table alone is insufficient. |
| Prodinger semifilter languages | Guo–Wang Questions 2 and 3, p. 62 (PDF 78) | Characterize other semifilters yielding precisely regular languages and give a non-tautological necessary-and-sufficient criterion for equality of their induced language classes. Exact original semifilter closure axioms apply. |
| Olson ordered EGZ | Sun p. 142 (PDF 158), the increasing-index conjecture | Every group of order n and every length-(2n−1) sequence must contain an order-preserving product-one n-subsequence. One explicit finite counterexample would refute it; unordered EGZ or small-group checks do not prove it. |
| Shor finite completion | Guo–Liu Question 1, p. 65 (PDF 81) | A finite complete/maximal code containing the book's explicit 16-word code, or a universal noncompletion proof. A necessary cyclic-factorization constraint or bounded search is not the full question. |

Parent rendered and directly inspected the actual statement pages for all four targets. This checks the seven trialgebra axioms, the complement-of-symmetric-difference semifilter operation, the increasing index requirement in Olson, and all exponents in Shor's code. Images are staged under `scratch/ai4s-math-more-20261014/source-images/`; workers retain their source excerpts in their dossiers.

## Directly checked primary sources and exclusions

1. **Rational SOS Question 2, pp. 475–476:** already answered negatively. [Scheiderer, JEMS 18 (2016), 1495–1513](https://ems.press/journals/jems/articles/13893), DOI [10.4171/JEMS/620](https://doi.org/10.4171/JEMS/620), explicitly constructs rational-coefficient homogeneous polynomials that are real SOS but not rational SOS. The parent read the publisher abstract and metadata. This does not settle the chapter's other three questions.
2. **osp characters, pp. 222–223:** [Gruson–Serganova, arXiv:0906.0918](https://arxiv.org/abs/0906.0918), DOI [10.1112/plms/pdq014](https://doi.org/10.1112/plms/pdq014), states that it computes the character of every finite-dimensional simple module over a basic classical Lie superalgebra. The parent read the primary abstract, which covers the general osp family. No independent replay of the paper's proof was performed.
3. **Alekseevskii question within homogeneous Einstein manifolds, pp. 238–240:** the parent read [Böhm–Lafuente, arXiv:2107.04210v2](https://arxiv.org/html/2107.04210v2), Theorem A and the following algebraic-structure paragraph. Theorem A gives a Euclidean-space diffeomorphism for homogeneous negative Einstein spaces; combining it with the cited BL22 gives the Einstein solvmanifold conclusion matching the book's stronger wording. The general classification of compact homogeneous Einstein spaces remains open. The chapter must not be called wholly solved.
4. **General phase-type minimum-order representation, pp. 544–545:** [Liu–Yao–Zhang, arXiv:2409.12673](https://arxiv.org/abs/2409.12673), primary abstract read, treats representations whose order equals the algebraic degree, not every minimal PH representation. Exact quantified real feasibility is an in-principle decidability route, but is not claimed as a new answer to the book's algorithmic research objective. Not selected because no sufficiently specific new missing obligation was established.
5. **High-order FEM, pp. 516–517:** later literature reports Chen–Hu's [Math. Comp. paper, DOI 10.1090/S0025-5718-2012-02653-6](https://doi.org/10.1090/S0025-5718-2012-02653-6) as a proof of the rectangular nodal 2k conjecture. The AMS primary page returned HTTP 403; the reported bound includes a logarithmic factor. This session does not promote that search result to a proof of every exact rate or of the chapter's triangular, fourth-order, hyperbolic and three-dimensional variants.
6. **Olson distinction:** [Zhao–Wang, arXiv:2603.21052](https://arxiv.org/abs/2603.21052), primary abstract read, explicitly permits the n factors to be reordered. It does not settle the ordered book conjecture. [DeVos's original problem page](https://openproblemgarden.org/op/olsons_conjecture), read directly, states precisely the increasing-index problem and the distinction from Olson's unordered theorem.
7. **Dendriform baseline:** [Madariaga, arXiv:1304.5184](https://arxiv.org/abs/1304.5184), primary abstract read, gives GS bases for dendriform algebras and quadri-algebras; the abstract does not itself provide the free trialgebra basis. Full trialgebra prior-art comparison is assigned to the worker, not assumed absent.

The broad minimax-quadratic criterion, rational-SOS Questions 1/3/4, optimal tessellation/Gersho, affine-flat Chern, remaining Kac–Weisfeiler and symplectic-Dirac programmes did not produce an exact bounded missing obligation worth another full-resolution attempt in this round. This is a resource-selection judgment, not evidence of impossibility.

## Reference corpus and environment

The read-only local `math/` clone was checked at commit `adc7f1241b42e322a6451854ab7e4b4c146bf78a` (2026-10-06), with 235 family docs and 722 preprint directories. Targeted optimization/Lie-topic searches produced no covering entry for the newly selected questions. Scout remote-screen claims remain in their own reports and are not independently certified here. The workers must record source-level applicability rather than importing unrelated OAI conclusions as premises.

The existing Mathlib-only project and existing Comparator control receipts from the preceding round are reused. No cache rebuild/clone is needed; disk availability was 13 GB (99% used) at the start of this round. HMZ pairing remains the live `scripts/hmz-tiers.json` authority. One finite run per viable question is allowed, only through `scripts/hmz-run.sh`, with frozen full-resolution acceptance criteria and no global/runtime edits.

## Correction to the previous result summary

The mathematics index's Gaussian-transfer summary was corrected to retain centered nondegenerate Gaussian errors and a translation-equivariant original estimator; almost-sure uniqueness of original minimizers suffices. Arbitrary consistent selectors on nonunique LAD designs are not covered. This agrees with `../../m-estimator-sample-augmentation/hmz-lean-20261014/regular-bounded-score-derivation.md:19-23`. The finite-variance uniformly-curved-loss summary also retains fixed dimension, a fixed nested eventually full-rank design and independent same-law replicates.
