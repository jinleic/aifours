# Independent review: unitary three-excess classification

Native clock immediately before this report write: `2026-10-28T19:18:18-0700 PDT`; this is not a completion timestamp.

## Verdict and scope

**No FATAL, MAJOR, or MINOR defect found in the all-n `2n+3` unitary lemma.** I independently reconstruct its necessity and converse below using complex row and column orthogonality, not merely graph conditions. I also reconstruct the lower-excess results for `2n`, `2n+1`, and `2n+2`. The separately computed finite controls extend through `n=6`; they are not the all-n proof.

This slice does **not** accept or prove the global AME lower bound. The proposed `≥46` remains conditional on the separately reviewed `≥45` candidate, its dependencies and the explicitly named classical no-OLS(6) import, and on the remaining residual/active-count reasoning outside this slice. No-OLS(6) is not needed for the standalone unitary lemma. This is a same-harness review, not human, independent-family, formal/kernel, or novelty verification.

## Input binding and reading

I read the binding manifest and all ten listed inputs completely, in the prescribed order; the two author programs and two author receipts were read for scope only and were **not** imported or executed. The manifest SHA-256 is `725e7c0d12bb013128ac9d11b15aba6355292578070b71b65c25f9c2c5d709a4`. For every input below, the computed whole-file SHA-256, byte count, and LF count all match the manifest. There were no pin mismatches. Basenames are under `/Users/jinleic/repos/aifours/physics/evidence/three-area-20261027-96h/parallel-18/ame46-support/`.

| Order | Input basename | Verified whole SHA-256 |
|---:|---|---|
| 1 | `frontier-20261028-global-ame46-lower42-review-packet-v2.md` | `50e97ebd0a30f2bcb1999fa85896f88bf4590d89fd897c60d9de53fe5775bedf` |
| 2 | `frontier-20261028-global-ame46-support-lower44-v1.md` | `89e2de23d4777697bd4e2b55e5925f3bd50f5f07c2e0e18aeb548ddd70052a30` |
| 3 | `frontier-20261028-unitary-two-excess-classification-v1.md` | `4a6d012d39ae8ae3acd0bb2ba04d0f79c824a9002633a0d2a45d91038119bec0` |
| 4 | `frontier-20261028-global-ame46-support-lower45-v1.md` | `26a4115ff62f56320af2647c550072255d0ab7c6c90de49ef83025d9219a1121` |
| 5 | `frontier-20261028-unitary-three-excess-classification-v1.md` | `a37a958ab0fca716ddeddd527a5e0cc4e8e35938c628f42e264f815488742bc2` |
| 6 | `frontier-20261028-global-ame46-support-lower46-v1.md` | `36586d04dd9e6cdc2bdf11e1bfcb2f85c07890cbf902386fef264260876b73eb` |
| 7 | `frontier-20261028-unitary-three-excess-controls-v1.py` | `0a42e2ddc08f5887ebac7c61ac3b393eae50c1921d0309008712b8bd5d88caed` |
| 8 | `frontier-20261028-unitary-three-excess-controls-v1.json` | `167ebc810557462e1c49c74d1f284fe8f47bee3d97abea90a20ee56de87f7105` |
| 9 | `frontier-20261028-active-count-control-v1.py` | `dccb5f9afa3ccefbb096f1c4dfe5992cd72644410eeb0e293ec30009a69e84b4` |
| 10 | `frontier-20261028-active-count-control-v1.json` | `c49c56b773400248fb7ee2c11e3bb42bdd78c824d2bf68a6bf3d55a5bceee7b6` |

## All-n reconstruction

Let `U` be a complex `n × n` unitary, with at least two nonzero entries in every row and column, and let its bipartite support graph have a component with `m` rows, `k` columns, and `e` edges.

**Square components and excess zero.** Entries between different components vanish. The component submatrix has orthonormal rows and orthonormal columns, since the other entries in its rows and columns are zero. Thus `m ≤ k` and `k ≤ m`, hence `m=k`; the component itself is unitary. Its row and column degrees remain at least two, so `r=e−2m ≥ 0`. If `r=0`, all row and column degrees equal two. A connected 2-regular bipartite graph is an even cycle; in any cycle longer than four, two rows have exactly one common nonzero column. Their Hermitian inner product would consist of a single nonzero product, impossible. Consequently each zero-excess component is a full `2 × 2` block.

**Excess one.** In a square component with `r=1`, exactly one row has degree three and all others degree two. Call its columns `{a,b,c}`. Every column has another incident row. A degree-two row meeting the exceptional row must use two of `{a,b,c}`, since a unique overlap cannot cancel. Two distinct 2-subsets of a 3-set meet in exactly one column, so all such neighbors must use the same pair. The remaining one of `{a,b,c}` would then have column degree one, a contradiction. Therefore excess one is impossible, independently of the author citation.

**Disjoint-pair and two-neighbor lemmas, including actual unitarity.** In any connected component other than a full `2 × 2` block, degree-two rows have disjoint column supports. A one-column intersection is impossible by row orthogonality. If two such rows have the same two columns, their restrictions are orthonormal and span `C²`; every other row must vanish on those columns. Since the two rows have no other entries, they form a separate full `2 × 2` component, contradicting connectedness. Thus no two degree-two supports meet.

For any one of those two-column supports `P`, a row meeting it must use both columns, again by row orthogonality. There is at least one other neighbor because column degrees are at least two, and it must have degree greater than two by disjointness. If it were the *only* other neighbor, the two columns would be supported on just these two rows. Their column orthonormality makes the resulting `2 × 2` matrix unitary, so that neighbor already has squared norm one on `P` and cannot have any other nonzero entry. This contradicts its higher degree. Therefore **at least two higher-degree rows meet each degree-two pair**.

If `s` rows have degree two and `b` rows have higher degree, disjointness gives `2s ≤ m=s+b`, hence `s ≤ b`. Also `b ≤ r`, since each higher-degree row uses at least one unit of row excess.

**Excess two, independently checked.** There is one positive component, with `r=2`, because `r=1` is impossible; the other components are full `2 × 2` blocks. In the positive component `b≤2`, so `m≤2b≤4`. It cannot have `m=2`, since a `2 × 2` matrix has at most four entries. If `m=4`, then `b=s=2`, both higher rows have degree three, and the two disjoint degree-two pairs cover all four columns. Every higher row must meet each pair in zero or two columns, forcing even degree, a contradiction. Thus `m=3`; the inequalities force `b=2,s=1`, and the higher rows each have degree three. The component is a `3 × 3` unitary with exactly one zero. Hence `2n+2` is possible only for odd `n`, with one such component and full `2 × 2` blocks. The rational eight-entry matrix in the bounded-controls section proves the converse for every odd `n≥3` by direct sum. In particular, all residual row and column degrees are at most three in this case.

**Excess three: component reduction.** With total excess three, there is exactly one positive component, of excess three: two positive components would have total at least `2+2`, and excess one is impossible. All others are full `2 × 2` blocks. For this connected exceptional component, `b≤3`, `s≤b`, so `m≤6`. The case `m≤2` is impossible because `2m+3>m²`. The remaining cases are exhaustive:

* `m=3`: `2m+3=9`, so the component is full.
* `m=4`: either `(b,s)=(2,2)` or `(3,1)`. In the first case the high degrees are three and four, while the two disjoint pairs cover all columns, forcing every high degree even. In the second case the three high rows all have degree three. Each must use the single whole two-column pair and exactly one of the two other columns. Those two other columns each have degree at least two, demanding at least four incidences, but the three high rows provide only three.
* `m=5`: necessarily `(b,s)=(3,2)`, and all high rows have degree three. Each must use exactly one of the two whole pairs and the sole unpaired column. The two-neighbor lemma demands at least four pair incidences, while the three high rows provide only three.
* `m=6`: necessarily `(b,s)=(3,3)`; the three pairs cover all columns. Each degree-three high row would be a union of whole pairs, hence have even degree, a contradiction.

Thus the exceptional component is a full `3 × 3` unitary and every other component a full `2 × 2` unitary, so `n` is odd. Conversely, the following rational real orthogonal matrices are particular complex unitaries with full support:

`H₂ = (1/5) [[3,4],[-4,3]]`, and `H₃ = (1/3) [[1,-2,-2],[-2,1,-2],[-2,-2,1]] = I−(2/3)J`.

Their direct sum `H₃ ⊕ H₂^⊕((n−3)/2)` has exactly `9+4(n−3)/2=2n+3` entries for every odd `n≥3`. Independent row and column permutations give every support pattern in the classification. This completes the all-n written reconstruction; the finite calculations below are controls, not a replacement for it.

For the excess-two converse used above, one exact eight-entry real orthogonal matrix is

`[[3/5, 4/13, 48/65], [-4/5, 3/13, 36/65], [0, -12/13, 5/13]]`.

It and its direct sums with `H₂` are checked by exact rational Gram arithmetic.

## Independent finite controls

I wrote the two checkers below without importing author code. They enumerate column-labeled row-mask **multisets**, use the degree-excess partitions, reject within-degree unique overlaps before forming Cartesian products, and weight each remaining multiset by the exact number of distinct row labelings. Thus the large `all` counts are exact counts of labeled candidates represented by pruning and weights, **not** a claim that a billion matrices were individually visited. `graph` means all row and column degrees are at least two and neither two rows nor two columns have a unique overlap; `square` adds the component-square condition. The final necessary filters implement the twin-pair and two-neighbor unitarity consequences; every survivor is explicitly realized with rational entries and both exact row and column Gram matrices checked. Its row permutations preserve that realization. A graph survivor is not generally claimed to be realizable.

### Target excess `3`, exactly `2n+3` entries

| n | All row-minimum-two labeled candidates | Graph survivors | Square survivors | Exactly realized labeled supports |
|---:|---:|---:|---:|---:|
| 3 | 1 | 1 | 1 | 1 |
| 4 | 3,264 | 0 | 0 | 0 |
| 5 | 2,050,000 | 100 | 100 | 100 |
| 6 | 1,022,962,500 | 0 | 0 | 0 |

For `n=3,4,5,6`, respectively, the counts of multisets actually considered after within-degree pruning were `1, 156, 4,555, 101,010`; for `n=6`, 382,560 weighted candidates passed the full row-overlap test, 7,200 also had all column degrees at least two, and none also passed the column-overlap test. The 100 positive `n=5` labeled patterns correspond to 10 explicitly realized row multisets; `n=3` has one. The exact classifications agree with the all-n argument, but this finite agreement is not used to infer it.

### Lower excess `0,1,2` controls

Entries in the table are `all / graph / square / exactly realized`, using the definitions above.

| n | excess 0 | excess 1 | excess 2 |
|---:|---|---|---|
| 3 | 27 / 0 / 0 / 0 | 27 / 0 / 0 / 0 | 9 / 9 / 9 / 9 |
| 4 | 1,296 / 18 / 18 / 18 | 3,456 / 0 / 0 / 0 | 4,320 / 0 / 0 / 0 |
| 5 | 100,000 / 0 / 0 / 0 | 500,000 / 0 / 0 / 0 | 1,250,000 / 1,000 / 900 / 900 |
| 6 | 11,390,625 / 1,350 / 1,350 / 1,350 | 91,125,000 / 0 / 0 / 0 | 372,093,750 / 0 / 0 / 0 |

The `n=5`, excess-two graph filter admits **100 rectangular-component patterns** that the square-component filter correctly rejects. One example has row masks `(7,7,24,24,24)` and components of dimensions `2 × 3` and `3 × 2`; it satisfies both no-unique-overlap tests and all degree minima, but cannot be a unitary. This control is deliberately at excess two, not falsely counted as a `2n+3` example.

A second, deliberately off-target control has row masks `(3,3,3,31,31)`. It is a connected square `5 × 5` support passing the degree and row/column overlap filters, yet three rows would be orthonormal vectors in the same two-dimensional coordinate subspace. It therefore cannot support any complex unitary. This shows why these graph filters and component square-ness are only necessary, not sufficient in general. The checker also rejects a unique-overlap mutation and exactly checks the full `2 × 2`, full `3 × 3`, and eight-entry `3 × 3` positive matrices.

## Reproducibility and receipt binding

All artifacts below are in this review directory. The checkers use the Python standard library and the lower-excess checker imports only my own `excess-check-v1.py`, whose hash it records. Receipts are created exclusively and refuse overwrite. The actual bounded runs were:

* `python3 -B excess-check-v1.py excess-receipt-v1.json` (Python `3.14.3`; receipt clock immediately before creation `2026-10-28T19:16:42-07:00`).
* `python3 -B excess-lower-check-v1.py excess-lower-receipt-v1.json` (receipt clock immediately before creation `2026-10-28T19:17:52-07:00`).

| Own artifact | Whole SHA-256 |
|---|---|
| `excess-check-v1.py` | `5fd3c71f0fa411114c6deea69aaf27ec343517cd43f8d58616a13ebed54ff1e1` |
| `excess-receipt-v1.json` | `bc715d82b1a9c33b942a21e2d4e2e6ef9b07118fd680d9791e7762f070af48d4` |
| `excess-lower-check-v1.py` | `c03c470ea21f6bc9a2ed4c12899378d8eec92a0ffa3786229d4aec584cba1bb8` |
| `excess-lower-receipt-v1.json` | `1e4181408322860cfa8b49857e07cb1252dc67ce7436dbf253d35cf93af7aee0` |
