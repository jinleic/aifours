# Addendum 1: strengthening the universal 3D-sector bound to 90 rays

**WRITTEN + EXACT SMALL-GRAPH AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date` before writing: Thu Oct 29 10:17:58 PDT 2026. This is additive to the pinned packet `frontier-20261029-universal-three-sector-cardinality-v1.md`, SHA-256 `6894733f793d317bc46039d3a056210b5b14614e4878853e0e36f1999dbc24dc`. Its written 95-ray theorem and computer-assisted 91-ray candidate remain unchanged.

**Stronger candidate.** If an order-10 1-RQLS has a 3-dimensional subspace H such that every cell ray lies in H or H-perpendicular, then it has at most **90 distinct rays**. This holds for **every** resolution Latin square. It is a conditional sector obstruction, not an unconditional no-go for the original problem.

## 1. Reduction to D=9

Use exactly the notation and proved lemmas of the pinned packet: H has 30 cells, K=30−D distinct sector rays, F distinct contextual sector-ray triples, and a C4-free contextual graph with degrees 2t_i and `sum t_i=3F`. The pinned packet rules out D=0,...,8 using its exact graph census and written ex(8,C4) bound. It remains to rule out D=9.

For D=9, K=21. The repeated-ray graph cost satisfies `30−F <= M(9) <= 13`:

- For r=1,...,7 repeated-ray vertices, exhaustively enumerate all labeled C4-free graphs and all positive integer weight partitions of 9. The exact maxima of the cost defined in the pinned packet §4 are, respectively, **0, 4, 11, 10, 13, 12, 11**.
- At r=8 the weights are (2,1,1,1,1,1,1,1). Each nontriangle edge costs 1, while each graph triangle costs 3, exactly its number of edges. Thus cost=|E|<=11 by the pinned packet's written ex(8,C4) lemma.
- At r=9 all weights are 1, again cost=|E|<=13 by §2 below.

So F>=17. The C4-free common-neighbor inequality gives F<=17: if F>=18, then `sum t_i>=54` and convexity gives `sum binom(2t_i,2)>=9·6+12·15=234>binom(21,2)=210`. Thus F=17, and the contextual graph on 21 rays would have 17 edge-disjoint triangles. Section 3 proves such a graph cannot exist. Hence D>=10, K<=20 and Q has at most `70+20=90` rays. ∎

## 2. Written ex(9,C4) lemma

**Lemma.** A simple C4-free graph on 9 vertices has at most 13 edges.

*Proof.* At a vertex v of degree d, N(v) induces a matching and every non-neighbor of v has at most one neighbor in N(v). Therefore

`|E| <= d + floor(d/2) + (8−d) + binom(8−d,2)`.

If d>=5, this is at most 13. If the maximum degree is at most 3, there are at most floor(9·3/2)=13 edges. It remains to consider maximum degree 4. For a vertex v of degree 4, its four neighbors have at most two internal edges, the four non-neighbors have at most four internal edges, and there are at most four edges between those sets. Hence |E|<=14.

Suppose equality 14. Then N(v) is two disjoint edges; every non-neighbor has exactly one target in N(v); and the graph on the four non-neighbors has exactly four edges and no C4. Such a four-vertex graph is a triangle with a pendant edge. The three triangle vertices must have distinct targets in N(v): if two share a target, those two, the third triangle vertex and the common target form a C4. Among three distinct targets in two matched pairs, two targets are matched. Those two targets and their adjacent triangle vertices then form a C4, contradiction. Thus |E|<=13. ∎

The accompanying integer certificate checks a specific C4-free graph with 13 edges, so the bound 13 is sharp as a graph bound; that graph is not a quantum-array witness.

## 3. A C4-free graph cannot attain the 21-ray boundary

**Lemma.** No simple C4-free graph on 21 vertices has its edges partitioned into exactly 17 triangles.

*Proof.* Let t_i be the number of triangles at vertex i. Edge-disjointness gives degree 2t_i and `sum t_i=3·17=51`. C4-freeness implies

`sum_i binom(2t_i,2) <= binom(21,2)=210`.                            (6)

For every nonnegative integer t,

`binom(2t,2) = 9t−12 + 2(t−2)(t−3)`.

The final term is nonnegative, equals 0 only for t=2 or 3, and is at least 4 otherwise. Summing the linear part gives `9·51−12·21=207`. Because of (6), every t_i must be 2 or 3. Exactly 12 vertices therefore have degree 4 and 9 have degree 6.

For a degree-6 vertex v, C4-freeness implies that the length-2 walks from v have distinct endpoints, so

`sum_{u adjacent to v} (degree(u)−1) <= 20`.

If h of its six neighbors also have degree 6, the left side is `18+2h`, giving h<=1. Thus the subgraph on the nine degree-6 vertices is a matching with e<=4 edges. The 54 high-degree incidences include 2e high-high incidences, so there are 54−2e high-low edges. The twelve degree-4 vertices have 48 incidences total, so 54−2e<=48, hence e>=3. Their induced graph has exactly e−3 edges, at most one.

Every graph edge belongs to exactly one triangle of the given partition. The low-degree vertices collectively occur in `12·2=24` triangles, counting a triangle once per low vertex. A triangle with one low vertex uses a high-high edge, so there are at most e<=4 such incidences. A triangle with two low vertices uses a low-low edge, so there are at most e−3<=1 such triangles, contributing at most 2 incidences. A triangle with three low vertices requires three low-low edges and is impossible. Thus there are at most 6 low-vertex incidences, contradicting 24. ∎

This argument treats arbitrary C4-free graphs with a triangle-edge partition; it does not rely on the graph being realizable by quantum rays.

## 4. Exact census and independent replay

- `frontier-20261029-three-sector-nine-duplicates-v1.py`, SHA-256 `5dbfc7cabab67325bd6b1a099f7310a95ecc9f0b2904973cbf0a379f4eca3691` (124 LF); result `frontier-20261029-three-sector-nine-duplicates-v1.json`, SHA-256 `338dcb9f7d232c206627b9d1fe827b0a4ea6e13d6c56c34d22c1b89926c2122a` (876 LF). Observed native clock Thu Oct 29 10:17:02 PDT 2026.
- `frontier-20261029-three-sector-nine-duplicates-replay-v1.py`, SHA-256 `d770e93957bed84896a636fae727ac2d8eac3ffd2a7dccb90d3873098c82ecf8` (97 LF); result `frontier-20261029-three-sector-nine-duplicates-replay-v1.json`, SHA-256 `2edd30b8db22918245328f71cfd5d8a7a4230571e7eb9bed3ee66eb16cb494d7` (49 LF). Observed native clock Thu Oct 29 10:17:39 PDT 2026.

The producer recursively generates C4-free graphs by rejecting any added edge that closes a 4-cycle. The second implementation imports no producer code, enumerates labeled adjacency masks directly, checks C4-freeness via common neighbors, and matches all **28** weight-partition extrema. Each checks an explicit 13-edge C4-free graph; the replay rejects a 4-cycle control. The 8- and 9-vertex upper bounds and the 21-vertex near-equality contradiction are written arguments, not exhaustive graph runs. These are same-harness author computations and do not constitute external-model, formal or novelty review.

## 5. Boundary

A maximal 1-RQLS(10), if one exists, must avoid a global 3+7 orthogonal sector split. It may have no such sector. The unrestricted 100-ray existence question remains **OPEN**, and this addendum neither uses nor adopts Theorem C, the m=7 diagonal search, numerical local-rigidity claims, or a stopped full-Gram/selected-calibration episode.
