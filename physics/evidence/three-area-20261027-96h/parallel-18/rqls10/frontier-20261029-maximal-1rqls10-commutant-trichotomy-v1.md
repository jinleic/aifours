# A universal commutant trichotomy for maximal 1-RQLS(10)

**WRITTEN AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date` before writing: Thu Oct 29 10:19:28 PDT 2026. This is a necessary structural condition for the original target, not an existence or nonexistence proof. The argument below is self-contained and uses no numerical input, graph census, covariance assumption or Z2 quotient. Novelty and independent review remain open.

## Statement

Suppose Q is a maximal 1-resolvable QLS of order 10: its 100 cell rays in C^10 are pairwise non-parallel, and its 10 rows, 10 columns and 10 resolution classes are ONBs. Construct the graph on the 100 rays where two rays are adjacent when their inner product is **nonzero**.

Exactly one of the following holds:

1. The graph is connected. The commutant of all 100 rank-one ray projectors is the scalar algebra C·I.
2. The graph has two components spanning orthogonal subspaces of dimensions **4 and 6**, and the components have **40 and 60 rays**. The commutant is C⊕C.
3. The graph has two components spanning orthogonal subspaces of dimensions **5 and 5**, and each component has **50 rays**. The commutant is C⊕C.

Thus a maximal 1-RQLS(10), if one exists, is either irreducible or has one of the two indicated orthogonal decompositions; no other reducible case is possible. This does not settle any of these three branches.

## 1. Orthogonal components and the commutant

Two different connected components have zero overlap between every pair of their rays, hence their spans are orthogonal. Because a row is an ONB, the spans of all components together equal C^10.

For each ray x let P_x be its rank-one orthogonal projector. If a linear operator X commutes with every P_x, write `X P_x = P_x X = lambda_x P_x`. Whenever rays x,y have nonzero overlap, P_x P_y is nonzero and

`lambda_x P_x P_y = P_x X P_y = lambda_y P_x P_y`,

so lambda_x=lambda_y. Therefore X is a scalar on each connected component's span. Conversely any operator that is scalar on each such orthogonal component commutes with all P_x. The commutant is thus C^k, where k is the component count, and its orthogonal projectors correspond exactly to unions of components.

If H is a union of components with dim H=d, every ray lies in H or H-perpendicular. Each row ONB contains exactly d H-rays, so because all 100 rays are distinct there are exactly 10d rays in H. The same is true for every column and resolution class.

## 2. Sector ranks 1 and 2 are impossible

If dim H=1, each of the ten rows contains the same unique H-ray, contradicting pairwise distinctness.

If dim H=2, take a cell x in H. Its row, its column and its resolution class are three ONBs containing x. Each contains exactly one other H-ray, which must be the unique orthogonal-complement ray to x in H. The three partner cells are distinct: any two of the three contexts intersect only at x. Hence one ray is repeated, contradiction.

## 3. Sector rank 3 is impossible: an elementary extremal count

Suppose dim H=3. There are 30 distinct sector rays, one for each H-cell. Build a simple graph on them, joining two when their cells share a row, column or resolution class. Each of the three contexts through a cell has exactly two other H-cells; since distinct contexts through that cell meet only there and all rays are distinct, each graph vertex has degree exactly 6.

The graph is C4-free. If four distinct rays a,b,c,d formed a 4-cycle, the distinct rays a,c would be linearly independent and b,d would both lie in their one-dimensional common orthogonal complement in H. Then b,d would be parallel, contradiction.

In a C4-free graph, every pair of distinct vertices has at most one common neighbor. Double-count unordered neighbor pairs at vertices:

`30 * binom(6,2) = 450 > binom(30,2) = 435`,

contradiction. This argument also shows, for a maximal 1-RQLS(n) and any 3D orthogonal sector, that `3n−1 >= 6·5`; thus n>=11.

## 4. Finish

A proper sector of rank 7, 8 or 9 would give a complementary sector of rank 3, 2 or 1, respectively, already excluded. Any connected component's span therefore has dimension at least 4. There can be at most two components because three positive dimensions at least 4 cannot sum to 10. If there are two, their dimensions must be 4+6 or 5+5. The component ray counts and commutant statements follow from §1. ∎

## 5. Related quantitative candidates and limits

The stronger author packet `frontier-20261029-universal-three-sector-cardinality-v1.md` (SHA-256 `6894733f793d317bc46039d3a056210b5b14614e4878853e0e36f1999dbc24dc`) gives a written 95-ray upper bound for any 3+7-sector 1-RQLS(10). Its additive `frontier-20261029-universal-three-sector-cardinality-addendum-1.md` (SHA-256 `1fdde6d5678bd515afafbb2201e4be2563213079337f66a779621c295200b29d`) gives a 90-ray candidate with an exact small-graph census. Neither quantitative result is needed for the trichotomy above.

The unrestricted 100-ray problem remains **OPEN**. In particular, the proof does not assert that 4+6 or 5+5 arrays exist or fail, and says nothing about the feasibility of the irreducible branch. This is not a reuse or adoption of the stopped full-Gram/selected-calibration episodes, Theorem C, or the m=7 diagonal search.
