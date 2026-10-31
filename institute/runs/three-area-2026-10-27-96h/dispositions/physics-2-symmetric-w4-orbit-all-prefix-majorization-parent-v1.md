# Four-qubit symmetric W orbit: exact full depolarizing majorization

**Disposition: same-harness written support with independently authored exact physical-channel and coefficient verification.** Native observation before composition: 2026-10-30T11:01:01-0700 PDT. f411 reports **0 FATAL / 0 MAJOR / 0 MINOR**. This is the equal-amplitude W4 orbit and its finite convex hull, not arbitrary W amplitudes, all biseparable states or unrestricted four-qubit majorization.

## Exact statement and genuinely larger state class

For |W4>=(|1000>+|0100>+|0010>+|0001>)/2, every local product unitary V, every physical 0<=p<=4/3, and every complex orthogonal rank-k projector Q, k=1,...,16,

Tr[Q Phi_p^tensor4(V|W4><W4|V†)] <= K_k(diag(a,b)^tensor4),

where Phi_p(X)=(1−p)X+(p/2)Tr(X)I2, t=|1−p|, a=(1+t)/2 and b=(1−t)/2. It extends by linearity for fixed Q to finite mixtures of such local-unitary images and to their convex hull together with the previously adopted [Class A/B hull](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/dispositions/physics-2-two-coefficient-and-paired-repetition-all-prefix-majorization-parent-v1.md). No input-independent postprocessing channel or common maximizer is asserted.

This addition is strictly outside the earlier hull. Across every paired physical cut, W4 has Schmidt rank2 and pair reduced support span{|00>,|01>+|10>}. A vector x|00>+y(|01>+|10>) has product-coordinate determinant −y²; thus the support contains exactly one product ray. A rank2 Class A pair support and a rank2 Class B repetition pair support each contain two independent product rays. All three pairings are equivalent for W; local physical unitaries preserve product rays. A positive mixture equal to a pure W density forces each positive-weight component to have W's one-dimensional support, so no Class A/B mixture can equal it.

## Actual output and exact coefficient proof

On p=1−t, the physical channel output is Hamming-weight block diagonal. For weights k=1,2,3 its block is d_k I+g_k A(J(4,k)), with

d_k=[k a^(5−k)b^(k−1)+(4−k)a^(3−k)b^(k+1)]/4,
g_k=t² a^(3−k)b^(k−1)/4.

The weight0 and4 eigenvalues are a³b and ab³. The graph eigenvalues are3,-1,-1,-1 for k=1 or3, and4,0,0,0,-2,-2 for k=2. This yields all16 actual eigenvalues, including multiplicities and endpoints.

Every candidate eigenvalue and ordered product-reference eigenvalue is a degree-four polynomial in t. Express them in the nonnegative Bernstein basis B_j^4=binom(4,j)t^j(1−t)^(4−j). For each j and k, subtract the sum of the k largest W coefficient positions from the coefficient of the reference k-prefix. The complete minimum-gap table (multiplied by192, k=0,...,16) is:

| j | Coefficientwise minimum gaps in ascending k |
|---|---|
| 0 | 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 |
| 1 | 0,6,9,12,15,18,18,18,18,18,18,18,15,12,9,6,0 |
| 2 | 0,24,24,28,36,44,36,32,28,24,20,20,12,8,4,0,0 |
| 3 | 0,36,24,24,36,48,36,24,12,0,0,0,0,0,0,0,0 |
| 4 | 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 |

Every entry is nonnegative. Hence the reference prefix dominates EVERY fixed subset of k eigenvalue positions coefficientwise, and therefore dominates the maximum over those subsets for every t. No fixed output eigenvalue order, common maximizing subset or numerical crossing argument is needed. For p>1, full transpose/spin-flip preserves the output spectrum; the consuming Q must be transported as Y^tensor4 Q^T Y^tensor4. Physical p=0,1,4/3 and degeneracies are included.

## Evidence, prior-public qualification and limits

[Parent author proof](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f410-parent-symmetric-four-qubit-w-channel-original-sector/author-candidate-v1.md) · [Disjoint written review](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f411-depolarizing-symmetric-w4-majorization-written-review/review-v1.md) · [Independent finite report](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f412-depolarizing-symmetric-w4-independent-exact-finite-verification/review-v1.md) · [Exact separately authored verifier](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f412-depolarizing-symmetric-w4-independent-exact-finite-verification/independent-w4-exact-physical-verifier-v1.py) · [Actual parent run](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f412-depolarizing-symmetric-w4-independent-exact-finite-verification/parent-independent-finite-run-v1-receipt.json). Parent displayed all101 author lines,596 written-review lines and943 finite-report/source lines. The independent verifier was parent-run once, exit0, checking all256 exact polynomial matrix entries, all three Johnson spectra, all85 Bernstein minimum gaps, exact complex negative-branch/projector controls and8 intended-invariant mutations. Parent's own separate scripts also produced exact physical matrices and all6144 multiplicity subset comparisons; their receipts remain linked from the candidate. These are mathematical and finite checks, not human/independent-family/formal-kernel assurance.

The [bounded public-source audit](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f413-depolarizing-w4-bounded-public-source-overlap-audit/review-v1.md) identifies stronger earlier printed tensor-product majorization claims in Amosov arXiv:2103.08515v6 and arXiv:2401.05104v1 whose formal scope may encompass this state class. Their proof validity and correspondence to the inaccessible subscription journal text are NOT certified by that audit; a separately frozen review investigates a specific ancillary-orbit step. Do not describe the present certificate as the first such result or infer that the older propositions are false merely from an unreviewed proof concern. Song–Wang–Tomamichel–Fang arXiv:2609.37240v1 states general exact majorization as a conjecture and proves a different exact log-determinant ordering and asymptotic approximate result. Neither source establishes novelty here.

Unrestricted high-polarization/all-density k3 and all-index majorization, all unequal-amplitude W states, 1|3 separable coverage and original-target closure remain open at this disposition. No external-model CLI, heavy/paid campaign or public communication was used.
