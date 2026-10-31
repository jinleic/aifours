# Independent same-harness review: N=47 forces t=27

**Disposition: 0 FATAL / 0 MAJOR / 0 MINOR; INCONCLUSIVE items within the frozen claim: none.** The reduction is supported as a conditional written argument, importing only the stated adopted f113 bound. This does not independently prove that bound or establish an AME state of support 47, nor does it exclude one.

Native clock observed before composing this report: `2026-10-29T13:28:32-0700 PDT`. This is an observation before writing, not a file-creation timestamp.

## Frozen inputs, measurements, and actual sequence

1. The first research artifact opened was `manifest-v1.json` in this wave. Measured SHA-256: `f6854d6292f5c6295d94452c808529d724981c91f99b09da6aa9f134f8f62e0a`, matching the assigned `f6854d6292f5` prefix. The initial manifest display truncated its requirements line; I then displayed that line in full with a raw read.
2. Before opening either input body, I measured the SHA-256, bytes, and LF count of **both** declared inputs. Both matched the manifest:
   - `/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/dispositions/physics-6-maximal-coefficients29-parent-v1.md`: `86968ac972bf26f1f6cac6936bbccd23b27696487c96a9779be5ef0553723d9b`; 5,473 bytes; 28 LF.
   - `/Users/jinleic/repos/aifours/physics/evidence/three-area-20261027-96h/parallel-18/ame46-support/frontier-20261029-n47-to-t27-reduction-self-contained-v2.md`: `906975c6c9b1ff03d3553e72263ad7f1a448ea44f15b66673a6ffedbceac1ea6`; 8,048 bytes; 72 LF.
3. I displayed the disposition completely, first, in raw windows 1–7, 8–14, 15–21, and 22–28 (the last request was 22–29 and reached the end). I then displayed the candidate completely, in raw windows 1–12, 13–24, 25–36, 37–48, 49–60, and 61–72 (the last request was 61–75 and reached the end). Every window was at most 15 requested lines. No mathematical reconstruction or control preceded those complete reads. A mistyped path was tried immediately before the successful 25–36 read and returned not found; it displayed no content. The subsequent read used the exact declared target path.
4. Only after both bodies were displayed did I reconstruct the argument and create and run the reviewer-owned control below. Memory and procedural skill instructions were also consulted after the input reads; they were not used as mathematical evidence. No linked body, author script, author receipt, solver status, external source, sibling review, or author contact was used.

## Per-claim verdicts

`0F/0M/0m` denotes no fatal, major, or minor finding for that claim; it is conditional on the explicit import list below.

| Claim | Verdict | Basis |
|---|---|---|
| Each 2|2 flattening yields a 36×36 unitary; singleton maximal entries can be removed, leaving an n×n unitary with line degrees at least 2 | 0F/0M/0m | Reconstruction §1 |
| `N≥72−t`; for `N=47`, `25≤t≤29`, `n=36−t`, `e=t−25` | 0F/0M/0m | Reconstruction §1; upper end uses f113 only |
| F1: no two distinct rows or columns have exactly one common support position | 0F/0M/0m | §2.1 |
| F2: each support component is square and has nonnegative row excess | 0F/0M/0m | §2.1 |
| F3 / Lemma A: excess-zero components are 2×2 full blocks; `e=0` forces even `n` | 0F/0M/0m | §2.1–2.2 |
| F4: degree-2 rows in a component of size at least 3 have disjoint pairs | 0F/0M/0m | §2.1; uses column norms, not just the support graph |
| F5: each degree-2 pair has at least two higher-degree row neighbours | 0F/0M/0m | §2.1; uses column orthogonality and norm saturation |
| F6–F7: `s≤b≤r` and higher rows meet each degree-2 pair in 0 or 2 columns | 0F/0M/0m | §2.1 |
| Lemma B: no component of excess 1 | 0F/0M/0m | §2.2 |
| Lemma C: excess 2 forces an eight-entry 3×3 component | 0F/0M/0m | §2.2 |
| Lemma D: excess 3 forces a full 3×3 component | 0F/0M/0m | §2.2; all size/degree cases enumerated in writing |
| Lemma E: a 7×7 unitary of minimum line degree 2 cannot have 18 nonzeros | 0F/0M/0m | §2.3; all component allocations and size/degree cases |
| Final case split: `N=47` forces `t=27` | 0F/0M/0m | §3; `t≥30` excluded only by f113 |
| Scope: no exclusion of `N=47`, existence assertion, or global support result follows from this packet alone | 0F/0M/0m | §3–4 |

## 1. Reduction to support graphs

Write the four coefficient indices in a product basis. For a 2|2 bipartition, form the 36×36 matrix whose row and column indices are the two pairs. The normalized AME condition says the reduced density on either two-party side is `I_36/36`; thus `U=6ψ` obeys `UU*=I_36` and is a square unitary. Each entry has modulus at most 1. The three flattenings have the same multiset of coefficient moduli and support size.

Let `P` be the entries of modulus 1, `t=|P|`, and let `E` contain all other nonzero entries. In every flattening, any entry of modulus 1 uses the entire squared norm of its row and of its column. Hence two entries of `P` cannot share either line, and no other entry lies in any line through `P`. Permuting rows and columns places these entries in `t` singleton blocks and all of `E` in an `(36−t)×(36−t)` complementary block `V`; orthonormality makes `V` unitary. Put `n=36−t`. Every row and column of `V` has at least two nonzeros: one nonzero would have modulus 1 by its norm and so would belong to `P`, contrary to its removal. This also covers the vacuous `n=0` situation.

Counting by rows gives `|E|≥2n`, so

`N=t+|E|≥t+2(36−t)=72−t`.

For `N=47`, this yields `t≥25`. The adopted f113 statement gives `t≤29`. In any one of the three cuts, the row excess is

`e=|E|−2n=(47−t)−2(36−t)=t−25`.

The same number occurs for all three cuts because `t`, `|E|`, and `n` are common. The following necessary restrictions use only one cut.

## 2. Independent reconstruction of all unitary-support facts

### 2.1 Structural facts

Use a bipartite support graph: rows on one side, columns on the other, with an edge for each nonzero entry. All lines have degree at least 2.

**F1.** If two distinct rows meet in exactly one column, their Hermitian inner product is a single product of nonzero complex numbers and cannot vanish. Orthogonality forbids this. The identical argument applied to columns proves its transpose.

**F2.** For any connected component with `p` rows and `q` columns, its `p` rows are orthonormal vectors supported in those `q` columns, so `p≤q`. Its `q` columns are orthonormal vectors supported in those `p` rows, so `q≤p`. Thus `p=q=m`. Since every row has degree at least 2, its excess `r=#edges−2m=Σ_rows(degree−2)` is a nonnegative integer. Component excesses add to the whole-matrix excess.

**F3.** If a component has excess 0 then each row has degree 2. It has `2m` edges, and because each of its `m` columns has degree at least 2, every column also has degree 2. A finite connected 2-regular bipartite graph is a cycle. In a cycle with `m≥3`, two adjacent row vertices share exactly one column, contrary to F1. Thus `m=2`, and the component is the full 2×2 support. Conversely this support has excess 0. Consequently an entire excess-zero matrix has even size.

For the remaining facts let a component have `m≥3` rows. Let `s` be the number of degree-2 rows and `b=m−s` the number of rows of degree at least 3.

**F4.** Distinct degree-2 row pairs cannot intersect in exactly one column by F1. If two had the same pair `{c,c'}`, their two rows, supported only on these columns, would form a square 2×2 matrix with orthonormal rows. It is unitary, so both of its columns already have norm 1 within these two rows. No other entry can occur in those columns. The two rows and columns would therefore form their own 2×2 component, contradicting `m≥3`. Thus all `s` pairs are disjoint.

**F5.** Fix a degree-2 row `ρ` on `{c,c'}`. By F1 any other row meeting either column must contain both; by F4 no such row can itself have degree 2. There is at least one such row because column `c` has degree at least 2. If there were exactly one, `σ`, then columns `c,c'` would be supported only on `{ρ,σ}` and would form an orthonormal 2×2 column matrix. It is unitary, so the norm of `σ` would already be 1 on those two columns, forcing degree 2, a contradiction. Hence at least two higher-degree rows contain each pair.

**F6–F7.** The `s` disjoint pairs use `2s` distinct columns, so `2s≤m=s+b`, i.e. `s≤b`. Every higher row contributes at least 1 to `r`, so `b≤r`. Finally, F1 says a higher row intersects each degree-2 pair in either 0 or 2 columns, never exactly 1. These deductions do not assert that every graph meeting them is a unitary support.

### 2.2 Excess 0, 1, 2, and 3

**A, excess 0.** F3 gives only full 2×2 components and therefore even total size.

**B, excess 1.** A component of size 1 is impossible under minimum degree 2; one of size 2 has exactly four edges and excess 0. For `m≥3`, F6 gives `b≤1` and `s≤b`. But `m=s+b≥3`, impossible. Thus no component has excess 1, and consequently no whole matrix has total excess 1.

**C, excess 2.** For `m≥3`, `s≤b≤2` gives `m≤4`. If `m=4`, then `s=b=2`: the two disjoint pairs cover every column. Each higher row intersects both pairs in 0 or 2 positions, hence has even degree, but the two higher rows together have excess 2 and therefore both have degree 3. Contradiction. The remaining size is `m=3`, where the number of edges is `2m+2=8`.

**D, excess 3.** The cases `m≤2` are impossible and F6 gives `m≤6`.

- `m=3`: `2m+3=9` edges, so the component is full.
- `m=4`, `(s,b)=(2,2)`: the degree-2 pairs cover all columns. Higher degrees must be even, but their positive excesses sum to 3, giving degrees 3 and 4. Contradiction.
- `m=4`, `(s,b)=(1,3)`: all three higher rows have degree 3. Let `X` be the pair and `u,v` the other columns. A higher row cannot avoid `X`, since only two other columns exist; by F7 it is `X∪{u}` or `X∪{v}`. This gives only three incidences in `u,v`, while their degrees must total at least four.
- `m=5`: necessarily `(s,b)=(2,3)` and all three higher rows have degree 3. Two pairs `X,Y` and one other column `u` account for all columns, so each higher row contains one pair plus `u`. This yields only three pair incidences; F5 requires at least two for each pair, i.e. four.
- `m=6`: necessarily `(s,b)=(3,3)`. The three pairs cover all columns, so F7 makes every higher degree even; all three higher degrees would be 3. Contradiction.

Hence the full 3×3 component is the only possibility for excess 3.

### 2.3 The 7×7, 18-entry case (excess 4)

Suppose such a unitary exists. Its component excesses are nonnegative, sum to 4, and none equals 1. The positive-excess allocation is therefore either `{2,2}` or `{4}`; other components have excess 0.

For `{2,2}`, Lemma C gives two size-3 components. The remaining one row cannot be filled by excess-zero components, each of which has size 2. This allocation is impossible.

For `{4}`, let its unique positive-excess component be `K`. The other components have size 2, so its size `m` must be odd. Size 1 is impossible, and a size-3 component has at most 9 entries and hence excess at most 3. Thus `m=5` or `7`, with `s≤b≤4`.

- `m=7`: necessarily `(s,b)=(3,4)`. The three pairs and one unpaired column `u` cover the columns; all four higher rows have degree 3, each consisting of one pair plus `u`. There are four pair incidences, whereas F5 requires at least six.
- `m=5`, `(s,b)=(2,3)`: the two pairs `X,Y` and one unpaired column `u` cover the columns. The higher degrees are 3, 3, and 4. By F7, a degree-3 row is one pair plus `u`, and the degree-4 row is `X∪Y`. F5 requires each pair to occur in at least two higher rows, so the two degree-3 rows must use different pairs. Those two rows meet exactly at `u`, contradicting F1.
- `m=5`, `(s,b)=(1,4)`: the four higher rows all have degree 3. Write the pair as `X` and the other columns as `u,v,w`. A higher row avoiding `X` is exactly `{u,v,w}`; by F5 some higher row contains `X` and is `X∪{x}` for one of `u,v,w`, which would meet `{u,v,w}` in exactly one column. Thus every higher row contains `X` and exactly one of `u,v,w`. The four resulting incidences cannot give all three of those columns degree at least 2, which would require six.

All cases contradict a necessary property of unitary support. This proves the claimed 7×7 exclusion; it does not claim that excess 4 is impossible at other sizes.

## 3. Final case split and precise scope

With `N=47`, the possible `t` and corresponding `(n,e)` are:

| `t` | `(n,e)` | Reason |
|---:|---|---|
| `≤24` | — | `N≥72−t` would give `N≥48` |
| 25 | `(11,0)` | Lemma A requires even `n` |
| 26 | `(10,1)` | no component can have excess 1 |
| 27 | `(9,2)` | not excluded by this reduction |
| 28 | `(8,3)` | the single positive component is full 3×3, all others have size 2, forcing odd `n` |
| 29 | `(7,4)` | Lemma E |
| `≥30` | — | imported f113 bound `t≤29` |

Thus any normalized complex AME(4,6) state with exactly 47 nonzero coefficients has exactly 27 maximal coefficients. The `t=27` line is a necessary-condition remainder, not a claim that such an AME state exists. As a sharp illustration of the one-cut limitation, the exact orthogonal 3×3 eight-entry positive-control matrix below, three copies of the 2×2 positive control, and 27 singleton blocks form a 36×36 orthogonal matrix with 47 nonzeros and exactly 27 modulus-one entries. This establishes a one-flattening example only: no simultaneous AME reshuffling is asserted. Composition with a separate `N=47,t=27` exclusion is outside this review.

## 4. Reviewer-owned exact control and receipt

I wrote `reviewer-support-control.py` in this wave without reading, importing, compiling, or running author code. SHA-256 measured before execution: `edd47f9748ff93df3499cb619a7fc97f4f5c55dda8273b61075d8c366dbd34a3`. Command: `python3 -B reviewer-support-control.py`; run capped at 120 seconds. Native-clock observations: start `2026-10-29T13:28:03-0700 PDT`, end `2026-10-29T13:28:03-0700 PDT`; exit code `0`; output ended `control_complete`. A cap or timeout would have meant UNKNOWN; neither occurred.

The independent finite control fixes the degree-2 pairs by column relabeling and enumerates all nondecreasing multisets of higher-row supports for connected square components of sizes 2 through 7 and excesses 0 through 4. It filters by minimum row/column degree, no unique row/column overlap, connectedness, pair disjointness, and the at-least-two-higher-neighbours condition. The latter two are necessary for unitaries by F4–F5 proved above, not merely graph-theoretic assumptions. Higher-row repetitions are allowed. It then composes component sizes/excesses to check total `(n,e)=(7,4)`. The count is of these canonicalized labeled support representatives, **not** a count of unitaries or of isomorphism classes; absence is conditional on the proved necessary conditions. The proof of A–D above covers arbitrary component size; this bounded control is supplementary.

| Component excess | Counts for `m=2,3,4,5,6,7`, respectively |
|---:|---|
| 0 | `1,0,0,0,0,0` |
| 1 | `0,0,0,0,0,0` |
| 2 | `0,1,0,0,0,0` |
| 3 | `0,1,0,0,0,0` |
| 4 | `0,0,8,0,0,0` |

The composition control found `0` possible seven-row, total-excess-four combinations. Predicate-level intended-reason negatives separately produced: row-overlap pair `(0,1)` sharing one column; column-overlap pair `(0,1)` sharing one row; a column of degree 1; disconnected two-2×2 support; and a degree-2 pair with only one higher neighbour. These are deliberately defective local inputs, not counterexamples to the theorem.

Positive checks used exact rational arithmetic for real orthogonal matrices with supports `(n,e)=(2,0),(3,2),(3,3),(4,4)`; all passed their inner-product identities and the relevant necessary-support filters. In particular, the 3×3 excess-2 matrix and the 2×2 matrix are

```
[ 3/5    4/5     0  ]       [ 3/5   4/5 ]
[12/25  -9/25   4/5 ]       [ 4/5  -3/5 ]
[16/25 -12/25  -3/5 ]
```

The nonzero `(4,4)` positive control prevents misreading the special seven-row exclusion as an exclusion of every excess-4 unitary.

## 5. Imports, remaining gap, and deviations

**Explicit mathematical import:** the pinned f113 disposition's stated result that every normalized complex AME(4,6) state in every product basis has at most 29 coefficients of modulus `1/6`. The disposition records its own reliance on the classical no-OLS(6) theorem and on a prior `t≤30` boundary. Those are inherited provenance of this sole adopted statement, not separately reproved or separately imported results in this reconstruction. Standard definitions of AME and elementary finite-dimensional complex linear algebra/arithmetic are used. No other adopted result is assumed.

**Remaining gap:** f113 itself and its classical import were not independently reproved here. This review establishes neither existence nor nonexistence at support 47, does not establish a global support bound, and does not check the separate downstream `t=27` exclusion. The finite control is not a formal proof certificate or an enumeration of complex amplitudes.

**Deviations:** no substantive deviation from the frozen review contract. The failed, non-content-returning mistyped-path read and the subsequent correct read are disclosed in the sequence above.

Same-harness review is not human review, independent-model-family review, formal/kernel verification, or novelty verification.
