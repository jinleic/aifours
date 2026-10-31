# Unitary matrices with exactly three support entries above the row-degree floor

Owner **PhysicsAME46-2**. Native clock immediately before writing: `Wed Oct 28 19:09:02 PDT 2026`; not an exact completion time. **WRITTEN author candidate**, not independently reviewed or accepted. This standalone lemma imports the one-excess exclusion proved in `frontier-20261028-global-ame46-support-lower44-v1.md`, SHA-256 `89e2de23d4777697bd4e2b55e5925f3bd50f5f07c2e0e18aeb548ddd70052a30`: a square unitary with every row and column degree at least two cannot have exactly `2n+1` nonzeros.

## Statement

Let U be an n×n complex unitary whose every row and column has at least two nonzero entries. If U has exactly `2n+3` nonzero entries, then n is odd and, up to independent row and column permutations, U is the direct sum of one full 3×3 unitary block and `(n−3)/2` full 2×2 unitary blocks. Conversely such a matrix exists for every odd n≥3. In particular, no even-dimensional U has support `2n+3` under these hypotheses.

## 1. Reduce to one irreducible component

In a unitary, disconnected components of the bipartite support graph are square: after row and column permutations a rectangular component would have to possess both orthonormal rows and orthonormal columns, forcing equal dimensions. Every component has nonnegative row-degree excess `r=nnz−2m`. Excess zero means every row and column has degree two; row orthogonality forbids a unique intersection, so the component is a full 2×2 block. Excess one is impossible by the named one-excess lemma.

Total excess three therefore consists of **one** component of excess three and any number of full 2×2 components: two positive components would require excess at least 2+2>3. Let the exceptional component have size m≥3. Its support graph is connected.

## 2. Degree-two pairs in a connected component

Two distinct degree-two rows cannot have supports meeting in exactly one column, because their inner product would have exactly one nonzero term. If two degree-two rows have the **same** two-column support, their restrictions are orthonormal and span C². Orthogonality forces every other row to vanish in those columns; the two rows have no other entries, so they form a separate 2×2 component, contradicting connectedness. Thus the degree-two row supports are pairwise **disjoint** two-column sets.

Let s be the number of degree-two rows and b the number of higher-degree rows. The disjoint pairs use 2s columns, so `2s≤m=s+b`, equivalently `s≤b`. Total excess three gives `b≤3`. Hence `m≤2b≤6`.

Each degree-two row's column pair must be met by at least **two** higher-degree rows. Any row meeting only one column of that pair would have a unique overlap with the degree-two row, so all neighbors use both columns. If there were only one higher-degree neighbor, the two columns would be supported on exactly two rows and form a 2×2 unitary; that neighbor's norm would already be exhausted on the pair, yielding a separate component. This proves the claim.

## 3. Exclude m=4,5,6

For m=4, `s≤b≤3`. If b=2, then s=2 and the two degree-two pairs cover all four columns; the two higher degrees must be 3 and 4, but a higher row meets each pair in either zero or two columns and therefore cannot have degree 3. If b=3, then s=1 and all three higher rows have degree 3. Each must contain the one complete pair plus exactly one of the two unpaired columns, since avoiding the pair leaves only two columns. The two unpaired columns each have degree at least two, requiring at least four incidences from only three higher rows. Both cases are impossible.

For m=5, `s≤b≤3` forces b=3 and s=2. All three higher rows have degree 3, and the two degree-two pairs leave one unpaired column. Each higher row must use exactly one whole pair plus that unpaired column. But each pair needs at least two higher-row neighbors, requiring at least four pair incidences among only three rows. Impossible.

For m=6, b=3 and s=3. The three pairs cover all columns; each higher row must be a union of whole pairs and thus has even degree, contradicting its degree 3.

Consequently m=3. A 3×3 component with `2m+3=9` entries is full. The remaining components are 2×2, so n is odd. A 3×3 Fourier unitary, direct-summed with any full 2×2 unitaries, gives the converse. ∎

## 4. Exact controls

`frontier-20261028-unitary-three-excess-controls-v1.py`, SHA-256 `0a42e2ddc08f5887ebac7c61ac3b393eae50c1921d0309008712b8bd5d88caed`, exhausts the possible row-degree patterns for n=3,4,5, checking no unique row/column overlaps and the necessary square-component property. Receipt `frontier-20261028-unitary-three-excess-controls-v1.json`, SHA-256 `167ebc810557462e1c49c74d1f284fe8f47bee3d97abea90a20ee56de87f7105`, records 1, 0, and 100 surviving support patterns respectively; all survivors have the stated full 3×3 plus 2×2 structure. These bounded support checks neither prove the general lemma nor independently review it.
