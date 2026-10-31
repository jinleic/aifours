# A universal 3D-sector cardinality obstruction for 1-RQLS(10)

**WRITTEN AUTHOR CANDIDATE + EXACT SMALL-GRAPH CENSUS, UNREVIEWED.** Native `/bin/date` before writing: Thu Oct 29 10:12:35 PDT 2026. This gives a necessary structural restriction on the original target, not an unconditional 1-RQLS(10) no-go. Novelty is unassessed; no formal-kernel or independent-model-family review is claimed.

## 1. Statements and exact scope

Let Q be any 1-resolvable quantum Latin square of order 10, with **any** resolution Latin square. Suppose a 3-dimensional subspace H of C^10 exists such that every cell ray lies either in H or in H-perpendicular. The sector membership pattern is arbitrary; no choice of basis, ray support bound, classical mate, Z2 quotient, covariance or flatness is assumed.

1. **Written theorem:** Q has at most **95 distinct rays**.
2. **Stronger computer-assisted candidate:** Q has at most **91 distinct rays**. The additional finite calculation exhausts C4-free graphs on at most seven vertices; the only eight-vertex case is bounded by the written argument in §5.

Either statement excludes a 3+7 orthogonal-sector decomposition for a hypothetical **100-ray** 1-RQLS(10). Neither says every array admits such a sector, and neither excludes other decompositions or the original unrestricted target. Classical order-10 orthogonal pairs give nonvacuous examples with a 3+7 sector and 10 rays.

## 2. Context and ray counting

Every row, column and resolution class is an orthonormal basis. Under the sector hypothesis each of these 30 contexts has exactly three cells in H. The sector therefore contains exactly 30 cells, and each sector cell belongs to exactly three contexts. Any two different cells share at most one of those contexts, by the Latin property.

Let K be the number of distinct H-rays and let the multiplicities be m_1,...,m_K. Put

`D = sum_i (m_i − 1) = 30 − K`.

Let F be the number of distinct **unordered triples of H-rays** that appear as the sector part of the 30 contexts, and let k_B count how many contexts realize triple B. Every sector triple is an ONB of H. Thus

`sum_B k_B = 30`, and `30 − F = sum_B (k_B − 1)`.

Two orthogonal rays in H determine the third ONB ray uniquely. Therefore distinct ray triples share at most one ray. Also, if triple B contains distinct rays i,j,k, then

`k_B <= min(m_i m_j, m_i m_k, m_j m_k, 3m_i, 3m_j, 3m_k)`.       (1)

Indeed, a context containing rays i and j determines an ordered pair of their cells; two contexts cannot contain the same two distinct cells. The other bound counts the three contexts through each cell of a ray.

## 3. C4-free orthogonality graph and a written 95-ray bound

Build a simple graph G on the K H-rays, joining two rays whenever they occur together in a sector context. It is **C4-free**: if a,b,c,d are four distinct rays with consecutive pairs orthogonal, then a and c are linearly independent and both b,d lie in the one-dimensional space `span(a,c)^perp`, a contradiction.

Because every contextual pair has a unique third H-ray, the contextual ray triples are edge-disjoint triangles. Write t_i for the number of distinct ray triples containing ray i. The degree of i in G is 2t_i and `sum_i t_i=3F`. Since a pair of vertices in a C4-free graph has at most one common neighbor,

`sum_i binom(2t_i,2) <= binom(K,2)`.                                  (2)

We first bound repeated context triples without a graph census. Put d_i=m_i−1. For B={i,j,k}, sorting `m_i<=m_j<=m_k`, (1) implies

`k_B−1 <= d_i d_j + d_i d_k + d_j d_k`.                               (3)

To see this, if m_k=1 all three multiplicities are one and k_B=1. Otherwise m_k>=2, so

`m_i m_j−1 = d_i+d_j+d_i d_j <= d_i d_j + d_k(d_i+d_j)`.

Sum (3) over distinct B. The unordered pairs in different ray triples are disjoint, hence

`30−F <= sum_{i<j} d_i d_j <= binom(D,2)`.                            (4)

Suppose D<=4, so K=30−D and F>=30−binom(D,2). For fixed K and `sum t_i=3F`, the left side of (2) is minimized when the integer t_i differ by at most one, since `binom(2t,2)=t(2t−1)` is convex. At the stated lower bound on F, the required minimum already exceeds (2):

| D | K | lower bound F | minimum sum binom(2t_i,2) | binom(K,2) |
|---:|---:|---:|---:|---:|
| 0 | 30 | 30 | 450 | 435 |
| 1 | 29 | 30 | 474 | 406 |
| 2 | 28 | 29 | 459 | 378 |
| 3 | 27 | 27 | 405 | 351 |
| 4 | 26 | 24 | 336 | 325 |

Larger F only increases the minimum. Contradiction in every row. Thus D>=5, K<=25, and the other 70 cells contribute at most 70 further rays. Therefore `cardinality(Q)<=25+70=95`. ∎

This written proof uses no computer output. The five numeric rows were also checked with integer arithmetic in the author's kernel, as was (3) on a finite 27,000-triple sample; the proof of (3) itself covers **all** positive integer multiplicities.

## 4. Sharpening to 91 rays by a finite graph census

The basic bound (4) counts pairs of repeated rays that need not be orthogonal. We improve it using only the induced contextual graph on the repeated rays.

Let U={i:d_i>0}, with weight d_i on vertex i. The induced graph G[U] is C4-free. Every edge in it belongs to exactly one contextual ray triple. A graph triangle on three repeated vertices is itself one such triple: all three rays are pairwise orthogonal and the third is uniquely determined by either edge. Since G[U] is C4-free, no edge is in two of its triangles.

For a nontriangle edge ij, its contextual triple has a third ray of multiplicity 1, so by (1) its excess satisfies

`k_B−1 <= min(d_i,d_j)`.

For a graph triangle ijk, its excess is bounded by

`min(m_i m_j, m_i m_k, m_j m_k, 3m_i, 3m_j, 3m_k) − 1`.

Define `cost(G[U],d)` as the sum of these upper bounds, taking each nontriangle edge and each triangle once. Distinct ray triples cannot reuse a repeated-ray pair, so every repeated context triple is counted at most once and

`30−F <= cost(G[U],d)`.                                                 (5)

For D<=8 there are at most eight repeated-ray vertices, their positive integer weights sum to D, and every induced graph is C4-free. Let M(D) be the maximum cost over this finite **over-approximation**. The exact enumerator checks all labeled C4-free graphs for 1–7 vertices and every nondecreasing positive weight partition of D; labeling the graph covers all assignments of those weights. If there are 8 vertices and D<=8, all weights are 1 and the cost equals the edge count, which is at most 11 by §5. The resulting bounds are:

| D | K=30−D | M(D) | F>=30−M(D) | minimum sum binom(2t_i,2) | binom(K,2) |
|---:|---:|---:|---:|---:|---:|
| 0 | 30 | 0 | 30 | 450 | 435 |
| 1 | 29 | 0 | 30 | 474 | 406 |
| 2 | 28 | 1 | 29 | 459 | 378 |
| 3 | 27 | 3 | 27 | 405 | 351 |
| 4 | 26 | 4 | 26 | 390 | 325 |
| 5 | 25 | 6 | 24 | 348 | 300 |
| 6 | 24 | 8 | 22 | 306 | 276 |
| 7 | 23 | 9 | 21 | 291 | 253 |
| 8 | 22 | 11 | 19 | 249 | 231 |

Each row contradicts (2), by the same integer-convexity minimization. Hence D>=9, so K<=21 and `cardinality(Q)<=70+21=91`. ∎

The enumerated weighted graphs need not be realizable by rays; including all of them only weakens the upper bound in (5), so no graph-realizability assumption is used.

## 5. Written bound for the eight-vertex case

**Lemma.** A simple C4-free graph on 8 vertices has at most 11 edges.

*Proof.* Fix a vertex v of degree d. Its neighbors induce a matching, since two incident edges there together with v make a C4. Every non-neighbor of v has at most one neighbor in N(v), otherwise two common neighbors with v form a C4. Consequently

`|E| <= d + floor(d/2) + (7−d) + binom(7−d,2)`.

- If d>=5 this is at most 10.
- If d=4 it is at most 12. Equality would require N(v) to consist of two disjoint edges, the three non-neighbors to form a triangle, and each non-neighbor to have exactly one neighbor in N(v). Their three targets in N(v) must be distinct: if two outsiders use the same target, they and the third outsider form a C4. Among three distinct targets in two matched pairs, two are matched; those two targets and their two adjacent outsiders form another C4. Thus equality 12 is impossible.
- If the maximum degree is at most 3, 12 edges would force a 3-regular graph. Choose v. Its three neighbors have at most one internal edge. They have `6−2k` edges to the four non-neighbors, where k is the number of internal edges. Each non-neighbor has at most one such edge, so k=1 and all four have one. Each of the four then has degree 2 inside the non-neighbor set, making that induced graph a C4, contradiction.

Thus no case has 12 edges. ∎

The certificate also checks an explicit 11-edge C4-free graph, so the upper bound is attained; this positive graph is only a combinatorial control, not a quantum witness.

## 6. Exact arithmetic and replay

- `frontier-20261029-three-sector-duplicate-extrema-v1.py`, SHA-256 `e8d93df97db9e058c0a8df1266a1438c4be3a1dc095c742e79db2d6d5843d2c9` (151 LF), result `frontier-20261029-three-sector-duplicate-extrema-v1.json`, SHA-256 `c7c2b0e8bd236928e82b0ec978368629486af6a16502ad8e49989b4af750a0bc` (1,622 LF); observed native clock Thu Oct 29 10:11:38 PDT 2026.
- `frontier-20261029-three-sector-duplicate-extrema-replay-v1.py`, SHA-256 `ba4ee908a93ff428057f9c7b39d7bdb7919a7804b0aef617033ada7b7d3c159f` (132 LF), result `frontier-20261029-three-sector-duplicate-extrema-replay-v1.json`, SHA-256 `5ca37d0427e713cd0541add237c4444891ebb19e264972d5f4c70a3994d46fd0` (44 LF); observed native clock Thu Oct 29 10:12:17 PDT 2026.

The first implementation adds labeled edges recursively and rejects an edge precisely when it closes a 4-cycle. Its counts of C4-free labeled graphs for vertex counts 1,...,7 are **1, 2, 8, 54, 548, 7,984, 163,440**. It records a maximizing graph for every weight partition. The second implementation imports no producer code: it enumerates all labeled adjacency bit masks directly, tests C4-freeness by common-neighbor counts, calculates cost by edge neighborhoods, and matches all **65** weight-partition maxima and all nine table rows. It rejects a 4-cycle control and checks a weighted-triangle value and the 8-vertex positive graph. The §5 upper bound is written mathematics, not an 8-vertex exhaustive run. Both executions are same-harness integer computations.

## 7. Relation to the nonquotient bridge and remaining gap

The separate packet `frontier-20261029-nonquotient-three-sector-bridge-v1.md`, SHA-256 `2d3a59160999e8581a78843dba0227a9d9bbd98ef178a762487caa09ae19b02e`, studies a literal Weisner resolution L with no Z2 quotient. Its exact census gives stronger **L-and-support-specific** 73-ray bounds for 1,194 sector patterns, and identifies residual triangle-free patterns. The present universal 91-ray bound is independent of that census and applies to **every** resolution and sector pattern, including all 1,968 triangle-free Weisner supports. The earlier support-specific 97-ray bound remains correct but is weaker than the new universal result.

An unrestricted maximal 1-RQLS(10) may have no 3D orthogonal sector at all. The existence of such an array, or a universal obstruction without a sector hypothesis, is still open.
