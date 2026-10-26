# Prior-art addendum 1 — dimension-universal candidate and structured multicopy baseline

This adds a further primary-source comparison to immutable `ME4-prior-art-screen-v1.md`; it does not change that screen's **NOVELTY_UNCLEAR** verdict. The new candidate compared here is `proof-GS4-maximally-entangled-reference-ADDENDUM-1-GSd.md`, SHA `c51a4c9d0665d37d91bd325b6e9771c4591207ffb44eac92beeeadbe7664ff4b`. No new scientific execution occurred.

## 1. Additional source actually recovered

The public ULAM archive reader initially exposed only a 59-paper header. Reading its actual HTML and searching the embedded records, rather than interpreting the shell as an empty archive, recovered three Werner records:

1. [*Obstructions to Werner Distillation*](https://www.ulam.ai/archive/obstructions_to_werner_distillation.pdf), archive publication date 31 July 2026; already compared.
2. [*Structured Multicopy Werner Bounds*](https://www.ulam.ai/archive/structured_multicopy_werner_bounds.pdf), archive publication date **29 July 2026**.
3. [*A Spectral Gap for Two-Copy Werner States*](https://www.ulam.ai/archive/werner_spectral_gap.pdf), archive publication date **28 July 2026**.

Both newly reached primary PDFs were directly read. Their archive labels describe one-pass model verification; these are source-provided claims, not independent authentication or journal/human acceptance.

The structured paper's Theorem 1.2 proves a shifted-gap tensorization for a coherent sum of two rank-one terms that factor over a common partition into blocks of at most two copy slots, with larger common-range/common-corange padding blocks. Its Corollary 3.4 explicitly requires all four singular vectors to be product across one common 2+1 cut. It also gives an exact orthogonal-compression identity and a qubit extension principle, and explicitly does not settle unrestricted three-ququart nonnegativity. This is more general than tensor-factorized **operators**, and must not be misdescribed as merely the latter.

The spectral-gap paper proves the two-copy refinement and threshold, with no three-copy claim. The source mechanism is the balanced rank-two decomposition and crossed trace identities, not the grouped maximally-entangled co-Choi contraction used in the present candidate.

## 2. The strict-coverage example also escapes the stronger coherent block-product class

Use E=span{u,x} from checkpoint 001:

`u=|0>⊗Phi_4`, `x=(|100>+|211>+|322>)/sqrt(3)`.

Across the cut 1:23, every `alpha u+beta x` with beta nonzero has Schmidt rank at least three, because the first-site components at labels 1,2,3 contain the independent vectors |00>,|11>,|22>. Hence u is the **only** biseparable ray of E across that cut. E cannot have a two-vector basis whose members are both product across that cut.

Across cuts 2:13 and 3:12, u has Schmidt rank four. If E were spanned by two vectors product across either chosen cut, every vector of E would have Schmidt rank at most two there. This contradicts u's rank four. Thus no common 2+1 cut permits two product output rays spanning E.

This argument covers **every** two-term rank-one decomposition whose output rays span E, not only one chosen SVD. In particular equal singular values cannot be rotated to repair the common-cut condition. A singleton partition would require fully product rays, which E does not contain. A single three-slot padding block with equal ranges or equal co-ranges would make the whole operator rank at most one, contrary to the explicit rank two. Therefore the example is outside the structured theorem even under its more general coherent block-product convention.

This is a strict comparison of hypotheses, not proof of worldwide novelty. The example's directly calculable positive q3 value is still only calibration; the universal new candidate is the map/SOS theorem.

## 3. Refresh for the all-d statement

Additional public queries for Werner/maximally-entangled-reference, co-Choi/entangled-reference, three-copy/biseparable/Werner, and Werner-distillation/maximally/rank-two found no exact matched source beyond the inspected baseline papers and the already excluded qutrit release. The current archive's embedded records contain the three Werner entries above; no matched reference-ray theorem was found there. These are bounded catalogue/query screens, not a proof of absence.

For d=3, a general three-qutrit conclusion is already claimed by the anonymous October 4 candidate. The present all-d claim must therefore not portray its d=3 consequence as a new unrestricted qutrit result. Its stated family permits an arbitrary-dimensional first factor and, for every d>=3, a maximally entangled reference across the other two factors. The full W4 problem still contains generic two-planes not covered by this condition.

**Disposition:** no matched equivalent located in the primary sources read, but global priority and human specialist assessment remain open. Neither ME4 nor GSd should be called first, established novel, publication-ready, or a solution of NPT bound entanglement on this evidence.
