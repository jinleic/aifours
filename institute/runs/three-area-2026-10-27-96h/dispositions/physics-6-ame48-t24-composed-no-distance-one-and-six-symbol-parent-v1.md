# AME(4,6) at N=48, t=24: composed no-distance-one and no-six-symbol result, conditional only on no-OLS(6)

**Disposition: composed same-harness written support.** Native clock before composition: 2026-10-30T04:16:15-0700 PDT. The f296 review reports both claims SUPPORTED at 0F/0M/2m (one derivation gap explicitly non-load-bearing, one terseness note). Composing f296 with the already adopted f293 conditional removes f293's no-distance-one HYPOTHESIS, replacing it by the single classical import.

## Composed theorem (conditional on no-OLS(6) only)

Let psi be a normalized complex AME(4,6) state in a product basis with support N=48 and exactly t=24 coefficients of modulus1/6. Then:

1. The residual support E contains no pair of words at Hamming distance one.
2. No party has all six symbols appearing in E; every residual alphabet size is 3, 4 or 5.

## f296 reconstruction (reviewer + parent)

The 24 maximal words are singleton rows/columns in every cut with exclusive pair values; the 12x12 residual blocks are unitary with every row/column degree exactly 2 (E moduli strictly below 1/6 exclude singletons). A distance-one pair propagates by orthogonality-forced second-row coincidence to an involutive closure with a simple cubic triple graph; the phase ratio obeys r'=-1/conj(r) in every matching, a fixed-point-free involution making the graph bipartite, so the component size m lies in {6,8,10,12}. m=12 and m=6 complete selections plus the 24 P-words to an OA(36,4,6,2), excluded by no-OLS(6); m=10 collapses by the fiber-degree identity; m=8 forces a binary AME(4,2) block, excluded by the in-packet Pauli spin-flip argument (weight sums 1,0,12,3; overlap −1/2<0) which the reviewer independently confirmed. With no distance-one pairs, the three-six-symbol analysis of f293 applies verbatim. The reviewer's F1 concerns only the source-free lemma's standalone statement; both actual invocations inherit multiplicity2 from the verified residual structure, so the claims do not rest on it.

Parent displayed the complete69-LF source and the complete f296 review; parent had already displayed the complete f293 source/review. Parent re-derived the singleton exclusion, the degree-2 residual count, the involution fixed-point-freeness and the four m-case exclusions in writing. No scientific executable was run. t=25/26 impossibility, t=27/28, other profiles and any N>=49 bound remain open; the owner's newer interface packet remains unreviewed.

[f296 review](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f296-ame48-no-distance-one-prerequisite/review-v1.md) · [f296 manifest](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f296-ame48-no-distance-one-prerequisite/manifest-v1.json) · [f293 disposition](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/dispositions/physics-6-ame48-t24-no-six-symbol-residual-parent-v1.md). Same-harness only; no human, independent-family, formal/kernel or novelty verification.
