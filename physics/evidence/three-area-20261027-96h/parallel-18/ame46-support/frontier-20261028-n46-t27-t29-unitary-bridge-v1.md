# N=46 residual bridge: exclude t=27,28,29 using complex unitarity

Owner **PhysicsAME46-2**. Native clock immediately before writing: `Wed Oct 28 20:45:09 PDT 2026`; not an exact completion time. **WRITTEN author candidate**, not independently accepted or formally verified. This is a direct original-target bridge, not a global lower-bound disposition. The proof of the three exclusions below is self-contained and uses no classical no-OLS(6) theorem.

## 1. Exact claim and relationship to t=26

For a normalized complex AME(4,6) state ψ in any product basis, let t count coefficients of modulus 1/6. If its support is exactly N=46, then t cannot be 27, 28, or 29.

The standard row count `N≥72−t` makes t≥26. **Only in combination with the separately recorded t≤29 structural result**, including that result's named no-OLS(6) and prior-t≤30 boundary, do the present exclusions force t=26. This packet does not itself establish t≤29, exclude N=46 for t≥30, prove a global ≥47 lower bound, or claim a 46-term witness. The named classical theorem is **not** used in the actual t=27/28/29 exclusions.

## 2. Exact unitary residual

For every 2|2 cut, `U=6ψ` is a 36×36 complex unitary because the associated two-party marginal is `I_36/36`. A coefficient of modulus 1/6 exhausts the squared norm of its row and column in ψ, so it is the unique nonzero of each. The t maximal coefficients occupy t disjoint singleton rows and columns. Deleting them leaves an `n×n` unitary V, where `n=36−t`. Every residual row and column has degree at least 2: a singleton of a unitary has modulus 1 and would have been one of the maximal coefficients. In each of the six coordinate-pair projections, the nonmaximal support E uses exactly n pair values and each has at least two E extensions.

For N=46 the cases are

| t | n | |E| | residual excess `|E|−2n` |
|---|---:|---:|---:|
| 27 | 9 | 19 | 1 |
| 28 | 8 | 18 | 2 |
| 29 | 7 | 17 | 3 |

We first prove the necessary unitary-support facts in full.

## 3. Complex-unitary support lemmas

Two distinct unitary rows cannot share exactly one nonzero column: their inner product would consist of one nonzero term. The analogous statement holds for columns. A disconnected component of the bipartite support graph must be square, since its submatrix has both orthonormal rows and orthonormal columns. Thus a unitary splits, after row/column permutations, into square support components.

A component of excess 0 has two nonzeros per row and per column. Its support is a union of even bipartite cycles; any cycle longer than four has two rows with exactly one common column. Hence a connected zero-excess component is a full 2×2 block.

Consider a connected component of size m≥3. The supports of its degree-two rows are pairwise disjoint 2-column sets. If two such rows share exactly one column they violate orthogonality. If they have the same two columns, their restrictions span C² and all other rows vanish there, so they would split off a separate 2×2 component. Let s be the number of degree-two rows and b the number of higher-degree rows. Then `2s≤m=s+b`, so `s≤b`. If the component's row-degree excess is r, then b≤r and m≤2r.

Each degree-two pair must be met by at least **two** higher-degree rows. Any row meeting only one of its two columns has a unique overlap with the degree-two row, so every neighbor uses both. If there were exactly one higher-degree neighbor, those two columns would be supported on only two rows and form a 2×2 unitary; that neighbor's norm would be exhausted, splitting off the pair. This contradicts connectedness.

### Excess one

A positive-excess connected component has m≥3. If r=1, then m≤2r=2, impossible. Therefore **no** square unitary with all row/column degrees at least two has exactly `2n+1` nonzeros.

### Excess two

A global excess of two has one connected positive-excess component (excess one is impossible), all other components being 2×2. That component has m≤4. If m=4, it has two degree-two rows whose disjoint pairs cover all columns, and its two higher rows each have degree 3; any higher row meets each pair in zero or two columns, so its degree would be even. Contradiction. The component is thus 3×3 with eight nonzeros, and the full unitary is that block plus 2×2 blocks. In particular its dimension n is **odd**. Hence even n cannot have support `2n+2`.

### Excess three

A global excess of three likewise has only one positive-excess component (two such components would each have excess at least two). Its size m is at most 6.

- m=4: if b=2, the two degree-two pairs cover four columns, so a higher degree-three row would have even degree. If b=3, there is one degree-two pair and two unpaired columns. All three higher rows have degree 3, must use the pair and exactly one unpaired column; the two unpaired columns each need at least two incidences, impossible with only three rows.
- m=5: b=3 and there are two degree-two pairs and one unpaired column. Each higher degree-three row uses one whole pair plus the unpaired column. Both pairs require at least two higher-row neighbors, demanding four pair incidences from three rows, impossible.
- m=6: b=3 and three degree-two pairs cover all columns; a higher degree-three row must be a union of whole pairs and hence has even degree, impossible.

Only m=3 remains, and its `2m+3=9` entries fill the 3×3 block. The rest are 2×2 blocks. Thus a `2n+3` unitary has odd n and is a direct sum of one full 3×3 block and 2×2 blocks. In particular, **every row and column has degree at most 3**.

These arguments use actual complex row and column orthogonality and norms, not merely support-graph no-unique-overlap tests. The earlier numerical-control correction is retained: 100 n=5 quadrangular two-excess patterns split into rectangular 2×3/3×2 support components and are not unitaries; they are not counted as valid unitary blocks.

## 4. Exclude t=27 and t=28

For t=27, the n=9 residual has `2n+1=19` nonzeros, impossible by the excess-one lemma. For t=28, the n=8 residual has `2n+2=18` nonzeros, impossible because the excess-two lemma requires n odd.

## 5. Exclude t=29

For t=29, the n=7 residual has `2n+3=17` nonzeros. The excess-three lemma makes every residual row and column degree at most 3. Thus every one of the six E coordinate-pair projections has seven values and every value has between two and three E extensions.

Fix any coordinate with r residual symbols. Every nonempty symbol fiber must vary in at least two other coordinates: if it varied in none or only one, some occurring pair would have only one extension. For another coordinate j, the total excess number of j-values across fibers is `7−r`, so at most that many fibers vary in j. Counting the three other coordinates gives `2r≤3(7−r)` and r≤4.

If r=4, each of the four fibers contains at least four E words: it varies in some j and each of two distinct `(symbol,j)` pairs has at least two extensions. If any other coordinate were constant on one of these fibers, the corresponding pair would have at least four E extensions, contrary to the degree-at-most-three bound. Hence every other coordinate varies in every fiber, giving at least `4·2=8` projected pair values, not seven. Thus every residual alphabet has size at most 3. Since each pair projection has seven values, no coordinate can have fewer than 3 values; otherwise its pair product with any size-at-most-3 alphabet has size at most 6. All four alphabets have size exactly 3.

Call a coordinate of a maximal P word active if its symbol occurs in the corresponding E alphabet. For any fixed party i, the 18 pairs with an active i symbol split into seven E pair values and 11 distinct P pair values. Thus exactly 11 P words are active at i. For any party pair ij, the nine active/active pairs split into seven E values and two distinct P values. Thus exactly two P words are active at both i,j.

If k(x) is the active-coordinate count of a P word x, these counts give

`Σ_{x∈P} k(x)=44`,  `Σ_{x∈P} C(k(x),2)=12`.

But `k−C(k,2)` equals `0,1,1,0,−2` for k=0,1,2,3,4 and is at most 1. Therefore

`32=Σ_{x∈P}[k(x)−C(k(x),2)]≤|P|=29`,

contradiction. This excludes t=29 and completes the direct bridge.

## 6. Exact controls and review limits

The written support lemmas are separately pinned in `frontier-20261028-unitary-two-excess-classification-v1.md`, SHA-256 `4a6d012d39ae8ae3acd0bb2ba04d0f79c824a9002633a0d2a45d91038119bec0`, and `frontier-20261028-unitary-three-excess-classification-v1.md`, SHA-256 `a37a958ab0fca716ddeddd527a5e0cc4e8e35938c628f42e264f815488742bc2`. Their exact small-graph control sources have SHA-256 `e8a2d9adbdeb11e4a42bd5a9326a41ae3100b479a345b5790c3a54b9dddf31d7` and `0a42e2ddc08f5887ebac7c61ac3b393eae50c1921d0309008712b8bd5d88caed`; corresponding receipts have SHA-256 `724018a563d3667860ba614fda117abf5c23729f1616961bc0a277048c77bf04` and `167ebc810557462e1c49c74d1f284fe8f47bee3d97abea90a20ee56de87f7105`.

The active-count arithmetic control `frontier-20261028-active-count-control-v1.py` has SHA-256 `dccb5f9afa3ccefbb096f1c4dfe5992cd72644410eeb0e293ec30009a69e84b4`; its receipt has SHA-256 `c49c56b773400248fb7ee2c11e3bb42bdd78c824d2bf68a6bf3d55a5bceee7b6`. The bounded graph and arithmetic controls do not prove the general unitary statements and do not constitute independent scientific review.

The original N=46 question remains open in the t=26 alphabet cases unless their separate, conditional candidates survive review; no statement about them or t≥30 is adopted here.
