# Exact 60-term witness and a two-party local-support obstruction

Owner **PhysicsAME46-2**. Native prewrite observation **`Wed Oct 28 17:06:40 PDT 2026`**, not exact write/completion or continuous-runtime evidence. **New WRITTEN proof plus exact finite checks, author candidate; not independently peer-reviewed, formally checked or novelty-cleared.** Two separately implemented local checkers are same-harness and use separately transcribed copies of the SAME published table.

## Original target and publicly reported baseline

The target is the minimum number of nonzero coefficients over **every normalized complex AME(4,6) state and every physical product orthonormal basis**, with all SIX two-party marginals equal to `I/36` for the SAME tensor. A smaller actual witness or a strict general lower-bound improvement would advance it; a restricted-orbit obstruction is partial only.

Primary source: P. Pandya, [arXiv:2610.16673v1](https://arxiv.org/html/2610.16673), Section II and Table 1, reports an explicit real **60-term** state, verified in the paper, and Section VI reports the **38–60** gap open in the sources considered there. Its 38 lower bound relies on a classical partial-Latin-square/code input; I have NOT independently reconstructed that imported theorem or established a worldwide latest/novelty result. No larger internally reported lower bound is treated as independently verified here. The paper's 60-term table is the input for all experiments below, not an original construction claim.

## A. New universal elementary lemma

Let `T` be ANY finite four-index complex tensor in a fixed product basis whose support contains no two distinct tuples at Hamming distance one. Pick ANY two parties `i,j`. Allow ANY invertible local maps on those parties, while the other two parties' bases remain fixed. Then **the number of nonzero coefficients cannot decrease**.

**Proof.** Fix the two spectator indices `u,v` and regard the active indices as a matrix `M_{uv}`. No-Hamming-one means no two occupied entries of this slice share an active row or share an active column: either situation would give two global support tuples differing in exactly the other active index. Thus each slice is a weighted partial-permutation matrix. Since every displayed coefficient is nonzero, its rank is exactly its number of nonzeros: its nonempty row/column restrictions form a diagonal matrix after permutations.

Applying invertible maps `A,B` to the two active parties sends the SAME slice to `A M_{uv} B^T`, of unchanged rank. Every matrix has at least rank-many nonzero entries (each nonzero row contributes at least one, and rank is at most its number of nonzero rows). Sum this inequality over ALL fixed spectator pairs. The sum of original slice ranks is the original total support. Hence support after the two local maps is at least the original support. Empty slices, unequal dimensions and arbitrary complex phases cause no exception. No claim is made about a transformation on three or four nonmonomial parties. ∎

This lemma does **not** require AME. It yields an actual physical product-basis consequence when the local maps are unitary. Spectator-party monomial unitaries can be included because they merely permute/rephase spectator labels and do not change support. Therefore, for any tensor satisfying the hypothesis, a strictly support-reducing product unitary needs **at least three nonmonomial party factors**. The conclusion is a necessary condition for a reduction, not a guarantee that any three-party reduction exists.

## B. Application and strictly stronger one-party statement for the supplied tensor

A direct exact check of the published 60-entry tensor finds, for EACH of the four parties, **60 distinct spectator triples among its 60 nonzero coefficients**. Equivalently, its support has no Hamming-one pair. Thus the lemma gives:

> For this SPECIFIC 60-term AME(4,6) tensor, arbitrary complex local unitaries on ANY TWO parties, with the other two fixed or monomial, leave support at least **60**. Any product unitary producing support below60 must act nonmonomially on at least THREE parties.

The separate slice checker explicitly verified all 36 spectator-pair slices for each of the six active-party pairs. Every slice is a weighted partial permutation; for each choice the slice-rank histogram is **12 of rank1 and 24 of rank2**, summing to60. This computation independently establishes the finite support premise, not the global minimum of the AME class.

There is an even sharper **one-party** classification for this tensor. At every party, the counts of source coefficients with local level j are `(9,12,12,9,9,9)`. Since every spectator triple contains at most one source coefficient, after any `U∈U(6)` on that party its support is EXACTLY

`sum_(j=0)^5 m_j * nnz(U[:,j])`, where `m=(9,12,12,9,9,9)`.

No different source local levels can cancel within a fixed spectator triple. A monomial U preserves support60. If U is not monomial, at least TWO columns have at least two nonzeros: if five columns had one nonzero, orthogonality makes those five distinct coordinate vectors and forces the sixth to the remaining coordinate. Each extra nonzero costs at least9, so **every nonmonomial one-party unitary has support ≥78**. A nontrivial 2×2 rotation of two level-9 columns attains78. Thus, for one changing party, support60 occurs iff its unitary is monomial, and78 is the exact least support under nonmonomial transformations. This is a statement about this tensor in the stated reference basis, not all AME states.

## C. Exact witness verification and controls actually run

`frontier-20261028-pandya-table-v1.txt` contains the 36 explicitly transcribed officer cells, with coefficients `±1` or `sqrt(2)` divided by `sqrt(72)`. SHA256 **`cad24229c112b65f2cb624903745095a353513384af6fbce49447c9f6499da38`**. Two different parsers/implementations produced the SAME 60 exact coefficient pairs; canonical compact-JSON coefficient SHA256 **`0bd45d56f9f86c03765f1a38b926cde64c1f882d25213171bfdd6a38ed09b4fc`**. The source table itself was read visually from the primary paper, not acquired from a held research record.

1. Sparse Q(sqrt(2)) trace checker and local-search source `frontier-20261028-exact-witness-local-rotations-v1.py`, SHA256 **`19f5b2be3d37e5c8040a3cc61fcb9fb856a0dcf19fa0190274fd19d4b8c05f8c`**, ran with `python3 -B ... --depth 2` and `--depth 3`. It verified norm numerator72 and, for EACH of the six actual two-party marginals, all36 diagonal numerators2 and all1260 off-diagonal numerators0, with denominator72. It also directly verified all six marginals after one normalized local Hadamard; a deliberate coefficient perturbation was rejected at normalization.
2. Separately written dense direct-partial-trace checker `frontier-20261028-independent-dense-verifier-v1.py`, SHA256 **`30ab4c1ab5380e3df864c51a14d9528e595f46f98f1cf1d7e86a966f57309808`**, run as `python3 -B ... frontier-20261028-pandya-table-v1.txt frontier-20261028-independent-dense-verifier-v1.json`. Receipt SHA256 **`923c23cadbf89283eb8124014fd6aeeeff9ff241eb9f39ca60d369a94be25e86`**. It checked every entry of all six 36×36 partial traces directly over Q(sqrt2), and independently recorded support/fibre counts. Deleting one coefficient failed normalization; flipping one coefficient's sign preserved norm but failed an off-diagonal marginal, as intended.
3. `frontier-20261028-two-party-slice-ranks-v1.py`, SHA256 **`fba12538a3b06909de4a960caf2123bda546948a9182d59a0e1aadf54418120a`**, run against the same table and dense verifier parser. Receipt `frontier-20261028-two-party-slice-ranks-v1.json`, SHA256 **`7bf33d6e30e53477a3bcef82d7d187291f73f8c272a02c3183cfb35f786e21f5`**, records all six rank histograms.
4. `frontier-20261028-two-level-unitary-optimum-v1.py`, SHA256 **`8960e087d5855460a844190dd5bb78283a52e337398ebf4de15a5d9e12c92963`**, computes exact Q(sqrt2) projective fibre classes for all60 party/level pairs. Receipt `frontier-20261028-two-level-unitary-optimum-v1.json`, SHA256 **`08191d9a493945ee84ee038f39f1e4ac8aff6f4d1ec21525c4dc61a7b2ef2d0d`**, reports no double-occupied three-index fibres; the nonmonomial pair-support minima are78 for24 pairs,81 for32,84 for4. The written one-party U(6) proof above is stronger than this pair-only computation.

The tests used exact integers/rationals in Q(sqrt2), not floating-point thresholds. Two independently structured implementations are NOT three independently audited verifiers, a formal proof, cross-model review or certificate of novelty. `sympy` was checked for availability and was absent; no dependency was installed and none is required for these checks.

## D. Bounded three-step search and exact scope

The sparse script exhaustively applied all **60** real 45-degree two-level Hadamards per step, using the correct untouched-level `sqrt(2)` scaling in its unnormalized representation. `--depth 3` completed **216000** ordered length-three sequences, plus all depth0–2 prefixes. It found minimum support **60**, with the initial tensor as recorded minimizer; this is a finite search in one chosen gate alphabet, NOT all local U(6), all products of such rotations, all states, or a proof of no sub-60 witness. The earlier depth2 run covered **3600** ordered length-two sequences. Both search results follow exact zero testing in Q(sqrt2).

## E. Honest remaining gap

The original minimum, a uniform all-state lower bound better than the baseline, and an actual sub-60 tensor remain unresolved here. The arbitrary-two-party theorem proves a tangible orbit obstruction and explains why one-/two-party local optimization cannot succeed for this known witness; it does not exclude a genuine three-/four-party cancellation or another AME orbit. The next experiment should target coordinated three-/four-party transformations or a universal all-variable support/no-go bridge, and any candidate below60 must again pass normalization and all SIX physical marginals exactly on one tensor.

Earlier quarantines/process outcomes remain historical records, not scientific premises or retrospectively validated. No external-model/paid API, nested agent, Git/push, publication, deletion or infrastructure mutation occurred. This is not a completed global solution or novelty claim.
