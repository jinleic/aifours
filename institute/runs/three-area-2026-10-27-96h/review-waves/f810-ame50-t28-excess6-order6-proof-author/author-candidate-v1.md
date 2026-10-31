# Actual-unitary excess-six components of orders six and eight

**Status: nonblind GENERAL AUTHOR written candidate, not an automatic disposition.** In view of the complete frozen packet, I reconstruct the proposed order-six and order-eight exclusions for connected supports of actual complex unitary matrices, including every low-row case and its transpose dependency. The proof below is self-contained from the actual-unitary interface stated in §1. It yields the two stated necessary local alternatives at `N=50,t=28`; it neither rules out that branch nor establishes compatibility or a choice of phases for the three cuts of one tensor. This is a proposed mathematical argument requiring a separate complete check.

## 1. Scope and basic actual-unitary facts

Let a connected component of the bipartite support graph of a finite square unitary have order `m` on each side, no singleton line, and excess `e = E − 2m`, where `E` is its number of nonzero entries. A connected block is square: its rows are orthonormal, giving rows ≤ columns, while its columns are orthonormal, giving columns ≤ rows. The submatrix on that component is itself unitary. Distinct rows cannot have exactly one common nonzero column, since their inner product would contain one nonzero term; the analogous statement holds for columns. Call a degree-two row or column **low**, and a line of degree at least three **high**.

The following isolation fact is stronger than the no-one-overlap support rule. If a low row `r` meets columns `a,b`, every other row meets `a,b` in either both positions or neither, so `a,b` have identical row neighborhoods and degrees; call them twins. Their common degree is at least three in a component of order greater than two. Indeed, if their common neighborhood were exactly `{r,s}`, the two orthonormal columns restricted to those two rows would form a 2×2 unitary. Orthogonality to that column basis would force every other column to vanish in rows `r,s`, isolating that 2×2 block, contrary to connectedness. Likewise, two low rows cannot meet once, and if they have the same pair of columns, their two orthonormal row restrictions form a 2×2 unitary; every other row then vanishes on those columns and the block is isolated. Therefore, in a connected component of order greater than two, **the twin pairs of distinct low rows are disjoint**. All these statements transpose, including disjointness of neighborhoods of distinct low columns.

If `k` rows are low, at least `m−e` are low because each high row uses at least one of the `e` row-excess units. The `2k` columns in their disjoint twin pairs are high, and the number of high columns is at most `e`. Thus

`m − e ≤ k ≤ floor(e/2)`, and consequently `m ≤ e + floor(e/2)` for `m>2`.

The same bounds hold after transposition. A component of order two with minimum degree two is the full 2×2 block and has excess zero. A one-row component cannot have minimum degree two.

The asserted excess-six theorem below concerns any such connected component of a genuine unitary, regardless of its embedding in an AME flattening. It does not assume an arbitrary graph mask is unitarily realizable; in particular it explicitly uses the isolation step just proved.

## 2. Exclusion at order six: all four low-row counts

Assume `m=e=6`, so there are 18 nonzero entries. The twin bound gives `k∈{0,1,2,3}`. Row-degree bookkeeping, before contradictions, is:

| low rows `k` | possible sorted row degrees |
|---|---|
| 0 | `3,3,3,3,3,3` |
| 1 | `2,3,3,3,3,4` |
| 2 | `2,2,3,3,3,5` or `2,2,3,3,4,4` |
| 3 | `2,2,2,4,4,4` |

For `k=3`, the last row of the table also uses the twin property: the three twin pairs cover all six columns, so every high row has even degree; each high row has degree at least four and their degree sum is 12. We now eliminate the cases in an order that makes every use of transposition noncircular.

### 2.1. Three low rows

The six disjoint twin columns all have degree at least three and account for all six column-excess units, hence each has degree three. The two columns of a pair meet their own low row and a two-subset of the three high rows. Two such subsets belonging to different low rows intersect, and a one-point intersection would make the corresponding columns overlap exactly once. Hence the three subsets are equal. The remaining high row then has no neighbor, contradicting its degree. Thus `k=3` is impossible.

### 2.2. Two low rows

The four twin columns form two pairs, each pair having equal degree at least three. Since total column excess is six, their pair-degrees, up to exchange, are either `(3,3)` or `(4,3)`, where each number denotes the degree of each column in that pair. The two remaining columns avoid both low rows.

* **Pair-degrees `(3,3)`.** Each pair has one low-row neighbor and two high-row neighbors. Let those two-subsets of the four high rows be `A,B`. Their intersection cannot have size one. If `A=B`, the two remaining high rows avoid all four twin columns and have at most two available neighbors, impossible for high rows. Therefore `A,B` are disjoint and partition the high rows. Each remaining column meets each twin column in zero or two rows, so it contains either all or none of `A`, and independently all or none of `B`. Its degree is consequently two or four. The two remaining columns have total degree six, so one has degree four and the other degree two. A row of `A` and a row of `B` then share the degree-four column but no twin column or degree-two remaining column. They overlap exactly once, contradiction.
* **Pair-degrees `(4,3)`.** The two remaining columns have degree two. Their neighborhoods are disjoint two-subsets `A,B` of the four high rows, by the transposed isolation fact, and hence partition those rows. A degree-four twin column contains its low row and three high rows; every three-subset of `A∪B` meets one of `A,B` in exactly one row. That gives a forbidden one-overlap with one of the low columns.

Thus `k=2` is impossible. Neither case used a prior exclusion for a number of low columns. Transposing §§2.1–2.2 therefore independently excludes two or three low columns.

### 2.3. One low row

The other five rows have degrees `3,3,3,3,4`. By the just-established transposed cases there are at most one low column. If there are none, all six columns have degree three; if there is one, the five high columns have degrees `3,3,3,3,4`. In either case, equal-degree twin columns of the low row cannot include the unique degree-four column, so both have degree three.

Let their common row neighborhood be `{r,x,y}`, where `r` is the low row. Any other column avoids `r` and meets a twin column in zero or two positions, so it contains both `x,y` or neither. Hence `x,y` have identical neighborhoods and equal degrees. Since there is only one degree-four high row, both have degree three; in addition to the twin pair they share exactly one further column `c`. No other row can meet `c`: every row outside `{r,x,y}` avoids the twin columns and would then overlap `x` exactly once. Thus the three rows `{r,x,y}` and three columns `{a,b,c}` have no support edges to the remainder. This contradicts connectedness of the order-six component.

Consequently the one-low-row case is impossible. Transposing §§2.1–2.3 now excludes one, two, or three low columns.

### 2.4. No low rows

All rows have degree three; the transposed exclusions force all columns to have degree three as well. First, two distinct rows cannot have the same three-column neighborhood `S`. After those two rows, the three columns of `S` have exactly three incidences left. Each other row meets `S` in zero, two, or three positions. Those three incidences therefore all belong to a third row containing all of `S`: a contribution of two would leave a forbidden contribution of one. The three rows then exhaust the three columns and form a proper disconnected component, contradiction.

Fix a row. Its three columns have six incidences with the other five rows. A different row meets it in zero or two positions: one is forbidden and three would duplicate its neighborhood. Exactly three other rows therefore meet it twice, leaving two disjoint from it. But only one three-subset of six columns is disjoint from its three-subset, so those two rows have identical neighborhoods, contradiction.

All `k=0,1,2,3` cases are exhausted. **No connected actual-unitary support of order six has excess six.**

## 3. Exclusion at order eight: both low-row counts

Assume `m=8,e=6`, so there are 22 nonzeros. The bound in §1 gives `k∈{2,3}` on each side. The raw row-degree profiles are `2,2,3,3,3,3,3,3` for two low rows and `2,2,2,3,3,3,3,4` for three. The same profiles hold for columns according to their low-column count.

### 3.1. Three low rows, or three low columns

If there are three low rows, their six twin columns are high and consume all six column-excess units. Thus those six have degree three and the other two columns have degree two. The two low columns avoid all three low rows. Their two-element neighborhoods `A,B` among the five high rows are disjoint by transposed isolation.

Each twin column consists of its own low row and two high rows. Its intersection with each of the two low columns must have size zero or two, so its two high-row neighbors are either all of `A`, all of `B`, or two rows outside `A∪B`. Only one high row lies outside that union; the last option is impossible. That remaining high row is incident with neither a low column nor any twin column and therefore has degree zero, contradiction. The transpose of the same complete argument rules out three low columns. This transposition does not presume the next case.

### 3.2. Exactly two low rows and two low columns

Both sides now have exactly six degree-three high lines. The four twin columns of the two low rows have degree three; the two low columns avoid the low rows and have disjoint two-high-row neighborhoods `A,B`. Let `Z` be the remaining two high rows. The two remaining columns, besides the two low columns and four twin columns, are high and have degree three; they also avoid the low rows.

Each twin column has its own low row plus two high-row neighbors. Since it meets each low column in zero or two positions, those two high neighbors are exactly one of `A`, `B`, or `Z`; the two columns in a twin pair choose the same set. At least one pair must choose `Z`, for otherwise a `Z` row could meet only the two remaining high columns, contradicting degree three. Both pairs cannot choose `Z`, since then each `Z` row would already have degree four. Exactly one does. By symmetry let the other pair choose `A`.

Each `A` row has its low-column neighbor and both columns of its twin pair, exhausting degree three. Each `B` row has its low-column neighbor and neither twin pair, so it must meet both remaining high columns. Each `Z` row has the two `Z`-twin neighbors and needs one more neighbor. A remaining high column intersects either `Z`-twin column in zero or two rows, and avoids the low row of that twin pair; hence it contains both `Z` rows or neither. Yet it already contains both `B` rows and has degree three, so it cannot contain both `Z` rows. Neither remaining high column can supply the required neighbor of a `Z` row, contradiction.

The two possible low-row counts, with the necessary low-column transposes, are exhausted. **No connected actual-unitary support of order eight has excess six.**

## 4. Consequence for each `N=50,t=28` cut

For one normalized AME(4,6) tensor and one fixed local product basis, use the packet's actual interface: every two-versus-two flattening of `U=6ψ` is a 36×36 unitary. If `N=50` entries of `U` are nonzero and `t=28` have modulus one, each such entry is alone in its row and column. Removing their 28 distinct rows and columns leaves an 8×8 unitary with `50−28=22` nonzeros and excess `22−2·8=6`. It has no singleton row or column: a singleton of a unitary would have modulus one and would have been removed. Every component therefore has nonnegative excess, and every zero-excess component is a full 2×2 block.

For completeness, the low positive-excess inputs needed for the cut count also follow from §1:

* Excess one is impossible. Excess two has order at most three, hence is a 3×3 block with eight entries. Excess three has order at most four. If its order were four, there would be exactly one low row, all other rows would have degree three, and likewise on the column side. The low-row twin columns would each have degree three and miss one high row, which would have only two other columns available; contradiction. Thus excess three is the full 3×3 block.
* An excess-four component of order five is impossible. It has one or two low rows. With one, the other four rows have degree three. Its twin columns have degree three or four, hence at least one high row avoids them and uses all three other columns. Any high row meeting the twins has exactly one neighbor among those three and overlaps the avoiding row once. With two low rows, the four twin columns consume all four column-excess units and have degree three. Each pair's high-neighbor set is a two-subset of the three high rows. The two subsets meet and cannot meet once, so they are equal; the remaining high row has at most the fifth column available. Both cases contradict the degree requirement.

The possible positive-excess partitions of six are `6`, `4+2`, `3+3`, and `2+2+2`. Three excess-two components require at least nine rows. In `4+2`, the excess-two component has order three; the excess-four component has order at least four and, within the eight-row total, at most five. Order five is excluded above, while order four leaves one row, which cannot be filled by zero-excess 2×2 components. In `3+3`, two full 3×3 blocks leave one full 2×2 block.

For the single excess-six component, all remaining components have order two, so its order is even and at most eight. Order two has excess zero; §§2–3 eliminate orders six and eight. It must be a connected order-four component with 14 entries, accompanied by two full 2×2 blocks. Its two zero positions either share a row, share a column, or lie in distinct rows and columns; these are necessary mask types only.

Accordingly, **for each actual cut** the necessary alternatives are:

1. two full 3×3 blocks and one full 2×2 block; or
2. one connected 4×4 block with 14 nonzeros and two full 2×2 blocks.

No joint cut compatibility, phase feasibility, tensor witness, exclusion of `t=28`, or global minimum is concluded. In particular the masks are not asserted to be sufficient. Within the stated local exclusion, all row-count cases are addressed by the written argument; its correctness and the actual simultaneous `t=28` problem remain to be separately assessed.

## 5. Imports, actual coverage, and limitations

The mathematical import is precisely the actual-unitary flattening interface in §4; all graph, degree, twin-isolation, order-six/eight, and low-excess facts used here are derived above. I did not use a no-OLS assumption, a global bound on `t`, a phase ansatz, or a finite enumeration as a proof premise. The packet's S4 receipt concerns its stated order-at-most-seven/excess-at-most-five enumeration and does **not** itself establish either excess-six exclusion.

I read through their endings the frozen manifest, freeze receipt, final pre-dispatch binding, parent-live metadata supply, actual dispatch receipt, and all 22 manifest-listed controls, using the controls solely for status and permission. Before any packet body, mathematics, or comparison, I sent Main the direct PREBODY ACK identifying the exact controls and one ordered packet part of 488 LF. Thereafter I read part 01 serially in RAW windows `1–20, 21–40, …, 461–480, 481–488`, including complete long lines, through its ending before research. No sequence or presentation fault is known. The complete packet bodies and manifest-declared pins are:

| ID | Frozen body | Original LF | Manifest-declared SHA-256 |
|---|---|---:|---|
| S1 | `review-waves/f799-ame50-unitary-excess-five-t27-proof-author/author-candidate-v1.md` | 110 | `61dfb5205f9b6bf2022c17d6149f1926571c48d24307556f67a7f2201b684197` |
| S2 | `review-waves/f787-ame50-positive-excess-frontier-author/author-candidate-v1.md` | 161 | `3752d4b981b70d4626dbda6a87644044332ffd2e431a624f753fcccf9257d4f9` |
| S3 | `dispositions/physics-6-actual-AME50-t25-t27-exclusion-and-excess-frontier-parent-v1.md` | 33 | `9dcffb913663a29d438d53354e44aaacff0ba7cd0c5b37d4b803ea98936af336` |
| S4 | `review-waves/f800-ame50-small-excess-exact-finite-author/parent-small-excess-v1-run-v1-receipt.json` | 166 | `5e6d3b47c5d2026868cbc25064cd67b5d83eb4c21fc69c2d7bd3a459dddaab7a` |

Paths in the table are relative to `/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/`. The packet's declared SHA-256 is `2b6283019d49f8162ff60a0fab94aa31f34a29653cf657f8c4ffb7630eb6bce3`. These pins are transcribed administrative metadata; I did not open or independently hash the outgoing original sources. S1 already proposes the exclusions, so this is a reconstruction in full view of that proposal, not a blind derivation.

All genuinely held episodes and every consumer remain NONINPUT. I did not open old code, unlisted science, outgoing links, or sibling returns; did not use a network, Git, installation, or deletion; and did not execute scientific code, a solver, a test, compiler, build, linter, formatter, or external-model CLI. No finite source was assigned or prepared. This candidate is one immutable written submission; any correction requires a separate additive record or complete exclusive successor.
