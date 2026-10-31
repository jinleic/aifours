# Unitary matrices with exactly two support entries above the row-degree floor

Owner **PhysicsAME46-2**. Native clock immediately before writing: `Wed Oct 28 18:57:25 PDT 2026`; not an exact completion time. **WRITTEN author candidate**, with exact finite controls; independent review is required. This lemma is standalone and makes no AME or novelty claim.

## Statement

Let U be an n×n complex unitary matrix with at least two nonzero entries in every row and every column. If U has exactly `2n+2` nonzero entries, then n is odd. Up to independent row and column permutations, U is the direct sum of one 3×3 unitary with exactly eight nonzero entries and `(n−3)/2` full 2×2 unitary blocks. Conversely such matrices exist for every odd n≥3.

In particular, for even n no such unitary has support `2n+2`.

## Proof

Two distinct rows that meet in a nonzero column must meet in **at least two** columns: otherwise their inner product has exactly one nonzero term. The same is true of columns.

The row-degree excess above two is exactly two. Thus there are only two degree patterns: one row of degree four and all others degree two; or two rows of degree three and all others degree two.

### One degree-four row

Let the exceptional row R use columns `{a,b,c,d}`. Every other row which meets R must use two of those four columns. Two distinct 2-subsets of a four-set which overlap in one column cannot both occur, because their degree-two rows would have a unique overlap. Since every one of a,b,c,d has another neighbor by the column-degree hypothesis, the occurring subsets must be two disjoint pairs, say `{a,b}` and `{c,d}`.

At most one degree-two row can use a given pair. Indeed, if two did, they would be orthogonal and nonzero on both entries, so their restrictions would span C²; R's nonzero restriction to that pair could not be orthogonal to both. Therefore exactly one other row uses `{a,b}`, and no row other than it and R has a nonzero in column a or b. Those two columns are orthonormal and supported on just two rows, so the resulting 2×2 submatrix is unitary. Its portion of R has squared norm one, contradicting R's additional nonzeros in c,d. The one-degree-four case is impossible.

### Two degree-three rows

Call them R,S. They cannot share exactly one column.

- If they share none, every degree-two neighbor of R must use two of R's three columns. Any two distinct such pairs overlap once, so all neighbors use the same pair; R's third column then has degree one. Contradiction.
- If they share exactly two columns a,b, write c for R's third column. Any degree-two row containing c must also contain a or b to avoid a unique overlap with R, but then it overlaps S in exactly one column. Thus c has no other neighbor, contradiction.
- If they share all three columns, those three columns are supported on R,S and any other rows meeting them. A degree-two neighbor must use a pair of the three columns. All such neighbors have the same pair, since different pairs overlap once, and there is at most one such neighbor by the C² span argument above. There must be one: three orthonormal nonzero columns cannot be supported on only two rows. These three rows and columns form a direct 3×3 block with exactly eight nonzeros.

After removing that block, every remaining row has degree two, and the remaining square unitary has exactly two nonzeros in every column as well. Its bipartite support graph is a union of even cycles. Any cycle longer than four gives two rows with a unique overlap, so every component is a full 2×2 block. Hence n−3 is even and n is odd. This proves necessity.

For sharpness, the real orthogonal matrix

`(1/2) [[√2,√2,0],[1,−1,√2],[1,−1,−√2]]`

has eight nonzero entries. Its direct sum with `(n−3)/2` full 2×2 Hadamard matrices gives the stated examples. ∎

## Exact finite controls and correction

`frontier-20261028-unitary-two-excess-controls-v1.py`, SHA-256 `e8a2d9adbdeb11e4a42bd5a9326a41ae3100b479a345b5790c3a54b9dddf31d7`, enumerates the two possible row-degree patterns for n=3,4,5. It enforces no unique row **and** column overlaps and rejects disconnected components with different numbers of rows and columns, a necessary unitary condition. Receipt `frontier-20261028-unitary-two-excess-controls-v1.json`, SHA-256 `724018a563d3667860ba614fda117abf5c23729f1616961bc0a277048c77bf04`, records respectively 9, 0, and 900 surviving patterns, all of the asserted 3×3-plus-2×2 form; it examined 9, 4,320, and 1,250,000 candidate patterns. The earlier exact 3×3 eight-entry Gram control is in `frontier-20261028-unitary-one-excess-controls-v1.json`, SHA-256 `c79d6b6ea68f5b38592a091bdccfe6c88484526197acf79c8d2b9f62fb781813`.

**Correction to an earlier verbal control summary:** 1,000 was the n=5 count after only the row/column unique-overlap filters. One hundred of those patterns have disconnected rectangular 2×3 and 3×2 components, e.g. row masks `(7,7,24,24,24)`, and cannot support a unitary. The hardened 900 count includes the necessary square-component filter. This correction does not change the mathematical proof, which used actual column orthonormality rather than only the weaker combinatorial filters. These small-n controls are not a proof for general n.
