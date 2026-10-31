# Excess-six boundary and exact one-cut support-50 classification

**Status.** Nonblind GENERAL AUTHOR written reconstruction in the same harness, for independent scrutiny; not a parent disposition or a human, model-family, formal/kernel, source-identity, or novelty claim. The argument is for arbitrary complex unitary entries: it assumes no phase or amplitude ansatz for the unknown matrix or tensor. The explicit real matrices in §6 are *existence witnesses for isolated one-cut support masks*, not assumptions about an AME tensor.

## 1. Exact statement and scope

Let a connected component of the bipartite support of a finite square complex unitary have order `m` on each side, and put `e = edges − 2m`. Every component considered after removing singleton rows/columns has minimum degree two. I propose:

1. There is no connected actual-unitary component with `(m,e) = (6,6)` or `(8,6)`.
2. Consequently, for **one** 36-by-36 unitary with exactly 50 nonzero entries of which exactly 28 have modulus one, its support, up to separate row and column permutations, consists of 28 singleton blocks plus exactly one of:
   * two full 3-by-3 blocks and one full 2-by-2 block; or
   * one 4-by-4 block with exactly two zero entries and two full 2-by-2 blocks. The two zeros share a row, share a column, or have distinct rows and distinct columns.
3. Conversely, each of these one-cut support types, including each of the three zero configurations, is attained by a real orthogonal 36-by-36 matrix with the stated 50/28 counts. This converse is **only a single-unitary statement**: it does not say that the same array remains unitary under its other two tensor reshufflings.

In particular, for an actual normalized complex AME(4,6) tensor `ψ` with `U=6ψ`, `N=50`, and `t=28`, the necessity applies independently to every two-versus-two flattening of that **same** tensor. The three cuts cannot be chosen independently in a global existence argument. This does not exclude or construct an AME tensor with these counts, settle cross-cut phase/incidence compatibility, or prove a new global support bound. Connected excess-six orders 5, 7, and 9 are not classified here; they are irrelevant to this particular order-eight residual parity argument.

**Imports.** The AME interface—that `6ψ` is unitary in each balanced flattening—is used as the definition/standard normalization. All graph and low-excess facts actually used below are proved in §§2–3; no unreviewed order-six/eight assertion is imported. S3 in the frozen packet states a prior parent disposition for lower excesses, and S4 reports a bounded necessary-support computation only through excess five. Neither is taken as evidence of an excess-six enumeration or phase feasibility. The input also contains the prior nonblind author proposal S1; this document reconstructs the argument after seeing it and does not claim blindness or an independent model family.

## 2. Unitary support facts, including the non-graph step

A unitary's support components are square: for a component with `r` rows and `s` columns the block has both orthonormal rows and columns, giving `r ≤ s ≤ r`. If two different rows share exactly one support column, their inner product consists of one nonzero summand, impossible. The same holds with rows and columns exchanged.

Call a degree-two line **low** and a higher-degree line **high**. Suppose a connected component has order greater than two. A low row supported on columns `a,b` forces every other row to meet both or neither; consequently columns `a,b` have identical row neighborhoods and are called its twin pair. If these twins had degree two, they would be supported on two rows and form two orthonormal vectors spanning those rows; all other columns vanish on those rows, giving a separate 2-by-2 component. Thus both twin columns are high.

Two low rows cannot share exactly one column. If they shared both, their restrictions would be an orthonormal basis of those two columns; every other row would have zero projection there, again isolating a 2-by-2 unitary. Hence different low rows have **disjoint** twin pairs. The same statements hold after transposition. In particular a low row and a low column cannot meet. The isolation argument uses actual orthogonality, not merely the no-single-overlap graph rule.

If there are `k` low rows, every other row contributes at least one unit of row excess, while each twin column contributes at least one unit of column excess. Hence

```text
m − k ≤ e,       2k ≤ e,       m ≤ e + floor(e/2)     (m>2).    (1)
```

The transposed inequalities also hold. An order-two component of minimum degree two is full and has excess zero.

The distinction is concrete: the connected 4-by-4 graph with row neighborhoods `12, 12, 1234, 1234` has minimum degree two and no pair of rows or columns overlapping in exactly one position. It is nevertheless not the support of a unitary: the first two rows would span columns 1 and 2, forcing the other two rows to vanish on those columns. Thus a graph-only necessary filter cannot be silently substituted for the actual-unitary twin/isolation condition.

## 3. Low-excess bookkeeping used in the cut decomposition

The following short proof avoids importing a finite enumeration. By (1), excess zero has no component of order greater than two and excess one is impossible. Excess two forces order three and eight edges, hence a 3-by-3 block with one zero.

For excess three, (1) permits order at most four. At order four there is exactly one low row and three degree-three rows. Its two twin columns must each have degree three: degree at least four for both would already spend four column-excess units. The twins contain the low row and exactly two of the other three rows, leaving a degree-three row to avoid them but use only two remaining columns. Contradiction. Thus excess three is a full 3-by-3 block.

For excess four, (1) permits order at most six. At order five there are one or two low rows. With one low row, the four high rows have degree three. Its twin columns have degree three or four, so some high row avoids them and uses all three other columns; a high row meeting them uses exactly one other column and therefore intersects the avoiding row exactly once. With two low rows, the four twin columns consume all four column-excess units, so each has degree three. Their high-neighbor sets are two-subsets of the three high rows. They intersect and cannot intersect once, hence are equal; the remaining high row has at most one available column. Both cases are impossible.

At order six and excess four, there are exactly two low rows and two low columns; every other line has degree three. The low columns have disjoint two-element neighborhoods `A,B` among the four high rows. All four high columns are the two low-row twin pairs. Each such column has two high neighbors and meets each low column in zero or two positions, so its high-neighbor set is `A` or `B`. If the two twin pairs choose the same set, the other two high rows have only their low column; if they choose different sets, the support splits into two components. Both contradict the hypotheses. Finally, order three can have excess at most three. Thus every excess-four component has order four.

## 4. Excess six: order six, all low-row cases

Assume for contradiction that a connected order-six component has 18 edges. By (1), its number `k` of low rows is at most three. All column statements use the same six excess units.

### Three low rows

Their three disjoint twin pairs occupy all six columns. Each of those columns is high, so all have degree exactly three. A twin column consists of its own low row and a two-subset of the three remaining rows. Two such two-subsets from distinct pairs must intersect; no-single-overlap forces an intersection of size two, hence equality. All three pairs therefore use the same two high rows, leaving the third high row without a neighbor. This argument does not assume in advance a particular high-row degree sequence.

### Two low rows

The four twin columns form two equal-degree pairs. Their pair degrees are either `(3,3)` and `(3,3)`, or `(3,3)` and `(4,4)`; a larger choice spends more than six excess units.

In the first case each pair has a two-subset of the four high rows as its high-neighbor set. These two subsets meet in zero or two positions. If equal, the two high rows outside that set have at most the other two columns, contradicting their degree at least three. If disjoint, call them `A,B`; they partition the high rows. Each of the two remaining columns avoids both low rows and must meet each of `A,B` in zero or two positions. Its neighborhood is thus `A`, `B`, or `A∪B`. Their degrees add to six, so one uses all four high rows and the other exactly one of `A,B`. Any row of `A` and any row of `B` then overlap in exactly the four-row column, contradiction.

In the second case the two remaining columns have degree two. They avoid the low rows and have disjoint two-element neighborhoods `A,B`, partitioning the four high rows. A degree-four twin column contains its low row and three of these high rows. That three-subset meets one of `A,B` in exactly one position, a forbidden singleton column overlap.

### One low row

The just-excluded cases apply to the transpose, so there are at most one low column. With no low column all columns have degree three; with one, the five high columns have degrees `3,3,3,3,4`. The two twin columns of the low row therefore both have degree three. Let their common neighborhood be `{r,x,y}`, where `r` is the low row.

Any other column avoids `r`, and its intersection with a twin column is zero or two; it therefore contains both `x,y` or neither. Thus rows `x,y` have identical column neighborhoods. The five high-row degrees are `3,3,3,3,4`, so these two equal degrees must be three. Besides the twin pair they share one further column `q`. No other row can meet `q`: it would overlap `x` in `q` alone, since the twin columns contain only `r,x,y`. The three rows `r,x,y` and the twin pair plus `q` form a separate component, contradiction.

### No low rows: the repeated-neighbor issue

All rows have degree three. Transposing the three exclusions above shows that there are no low columns either; hence all columns also have degree three. Suppose two rows have the same three-column neighborhood `Q`. The three columns have nine incidences, six of which lie in those two rows. Each remaining row meets `Q` in zero, two, or three positions. The remaining three incidences can therefore only be supplied by one row meeting all of `Q`; the three rows and three columns form an isolated full 3-by-3 block. This contradicts connectedness. Thus repeated neighborhoods are excluded before using any distinct-neighborhood count.

Fix a row with neighborhood `Q`. Its three columns have six incidences in the other five rows. Distinctness and no-single-overlap make every other row's intersection with `Q` either zero or two. Exactly three rows meet `Q` twice, and the other two avoid it. But there is only one three-subset of six columns disjoint from `Q`, so those two rows would have the same neighborhood, already excluded. This exhausts `k=0,1,2,3`; order six is impossible.

## 5. Excess six: order eight

Assume a connected order-eight component has 22 edges. On either side, (1) forces two or three low lines.

If there are three low rows, their six twin columns use all six column-excess units; each has degree three, and the remaining two columns have degree two. The two low columns avoid all low rows, and their neighborhoods are disjoint two-subsets `A,B` of the five high rows. Each twin column has two high neighbors and must meet each of `A,B` in zero or two positions. It must therefore choose exactly `A` or exactly `B`: the one high row outside `A∪B` is too small to form an alternative pair. That row has no neighbor at all. The transposed argument also excludes three low columns.

There are consequently exactly two low rows and two low columns. All six high rows and all six high columns have degree three. Write `A,B` for the disjoint two-high-row neighborhoods of the low columns and `Z` for the remaining two high rows. Each of the four twin columns contains its own low row and exactly two high rows; avoiding singleton overlap with the low columns forces its high-neighbor set to be `A`, `B`, or `Z`. The two columns of one twin pair have the same choice.

At least one twin pair chooses `Z`: otherwise each `Z` row would have at most the two remaining high columns as neighbors. Both pairs cannot choose `Z`, because that would give a `Z` row four neighbors. Up to exchanging `A,B`, the other pair chooses `A`. Each row in `B` already has its low column and no twin-column neighbor, so it must meet both remaining high columns. Each row of `Z` already meets its twin pair and needs one of those remaining columns. Comparing such a column with a `Z` twin forces it to contain both `Z` rows, not just one; but it already contains both `B` rows, giving degree at least four instead of three. This contradiction finishes order eight.

## 6. Exact `t=28` one-cut classification and local attainability

A modulus-one unitary entry is the only nonzero entry in both its row and column. Removing the 28 such pairs from a 36-by-36 unitary leaves an order-eight unitary with `50−28=22` nonzeros, no low-degree-one line, and total excess `22−2·8=6`. Its components have nonnegative excess. Positive excess cannot be one, so the positive-excess partitions of six are `6`, `4+2`, `3+3`, and `2+2+2`.

The last needs at least three order-three components, exceeding order eight. For `4+2`, §3 gives orders four and three, leaving one row/column, which no residual component can occupy. For `3+3`, the two full order-three components leave one full order-two component. For a single excess-six component, all other components are full order-two blocks. Its order is even and at most eight. Order two has excess zero, orders six and eight are excluded in §§4–5, and order four remains. It has 14 entries and thus exactly two zeros. Their relative positions give exactly the three listed masks.

The reverse one-cut existence is elementary. Let

```text
H2 = (1/sqrt(2)) [[1,1],[1,-1]],       H3 = I3 − (2/3) J3.
```

Both are real orthogonal and have full support. For a 4-by-4 block with two zeros in one row, let its first row be `(e3+e4)/sqrt(2)` and let the other three rows have coefficient rows `H3` in the orthonormal basis `e1,e2,(e3−e4)/sqrt(2)`. Those three rows are everywhere nonzero. Transposing provides two zeros in one column.

For two zeros in different rows and columns, the following four normalized rows are mutually orthogonal and have precisely the indicated two zeros:

```text
(0, 1, 1, 1) / sqrt(3)
(sqrt(2), 0, 1, -1) / 2
(sqrt(2), -4, 1, 3) / sqrt(28)
(-3/sqrt(2), -1, 2, -1) / sqrt(21/2)
```

Row and column permutations give every placement in each zero class. Form direct sums `H3 ⊕ H3 ⊕ H2` or `H4 ⊕ H2 ⊕ H2`, then add 28 unit scalar blocks. Every residual row has at least two nonzeros, so no residual entry has modulus one. The resulting 36-by-36 unitary has exactly 50 nonzeros and exactly 28 modulus-one entries. These explicit witnesses do not assume an ansatz for, or establish the existence of, any AME tensor.

## 7. Actual coverage and limits

Before packet science, I read the complete manifest, freeze receipt, final pre-dispatch binding, prepared metadata, actual dispatch receipt, and all 22 manifest-listed controls through their endings; controls were used for status and permissions only. I sent Main the DIRECT PREBODY ACK naming the exact controls and the ordered one-part/488-LF packet, with no packet body, mathematics, or comparison performed. I then read the entire sole packet serially in RAW windows `1–20, 21–40, …, 461–480, 481–488`, through its ending, including the complete long lines, before research. The packet contains the complete declared bodies S1/S2/S3/S4, respectively 110/161/33/166 original LF. No sequence or presentation fault is known.

The parent-declared packet SHA-256 is `2b6283019d49f8162ff60a0fab94aa31f34a29653cf657f8c4ffb7630eb6bce3`; the four parent-declared source-body pins in order are `61dfb5205f9b6bf2022c17d6149f1926571c48d24307556f67a7f2201b684197`, `3752d4b981b70d4626dbda6a87644044332ffd2e431a624f753fcccf9257d4f9`, `9dcffb913663a29d438d53354e44aaacff0ba7cd0c5b37d4b803ea98936af336`, and `5e6d3b47c5d2026868cbc25064cd67b5d83eb4c21fc69c2d7bd3a459dddaab7a`. They are administrative declarations, not independent original-source verification. I did not open the outgoing source paths, old code, a sibling return, unlisted science, held episode or consumer, or a network link. No scientific child execution, solver/CAS, test, compiler, build, lint, formatter, or external-model CLI was used; no finite source was assigned or prepared. The candidate was exclusively created once; any correction must be additive rather than an overwrite.

All genuinely held episodes **and every consumer** remain NONINPUT. The remaining scientific gaps are simultaneous all-three-cut and six-pair compatibility, arbitrary complex phase constraints across those cuts, existence/exclusion of an actual AME tensor at `(N,t)=(50,28)`, and any general classification of excess-six components outside orders six and eight. A separate full read and independent scrutiny are required before adopting any proposed statement.
