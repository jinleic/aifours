# A two-dimensional orthogonal sector excludes maximal quantum Latin squares

**WRITTEN AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date`: **Thu Oct 29 00:41:18 PDT 2026**. This is an unrestricted-support sector obstruction, not a no-go for arbitrary QLS10.

## Theorem

Let Q be a t-resolvable QLS of order N, with t>=0, and suppose there exists a two-dimensional subspace H such that EVERY cell ray lies in H or H-perpendicular. Sector membership may vary arbitrarily between cells. Set `s=t+2`. Then

`cardinality(Q) <= N² - 2N + 2 floor(N/s)`.                           (1)

For t=0, interpret Q as an ordinary QLS with only its row and column contexts. In particular **no maximal QLS of any order N>=3 admits such a 2D orthogonal sector split**. For a 1RQLS10, the bound is **86 rays**, independent of any sparsity, choice of Latin resolution or behavior in the complementary 8D sector.

## Proof

Each of the N row bases contains exactly two H-rays, so the array has exactly 2N cells in H. In any context, the H-rays form an ONB of H. For any H-ray x there is a unique projective orthogonal-complement ray `x_perp` in H. If a cell carries x, each of its s contexts must contain a cell carrying `x_perp`. These s partner cells are distinct: every pair of distinct contexts containing the original cell meets only there (rows, columns and Latin transversals; different resolution systems also intersect once). Hence `x_perp` occurs at least s times, and applying the same argument to it shows x occurs at least s times.

The H-rays come in disjoint orthogonal-complement pairs; each pair consumes at least 2s cells. Therefore there are at most `2 floor(N/s)` distinct H-rays. All `N²-2N` remaining cells contribute at most one distinct ray apiece. This proves (1). The argument makes no assumption on the coordinates or entanglement of the other rays.

A one-dimensional sector is even simpler: its N cells all carry the same ray, giving `cardinality<=N²-N+1`. Therefore a maximal QLS with N>=3 has no 1D or 2D orthogonal sector, although it may or may not have higher-dimensional sectors. The n=10 example in `frontier-20261029-maximal-separable-sector-qls10-no-transversal-v1.md` SHA **f689af59576f63d0dd4f0e9afc5f811e54009215b9748ff49d9471d753ee0b63** uses 5D sectors and is not in conflict.

Independent written review of the sector-occupancy and context-intersection arguments is requested. Mixed-sector rays or absence of such a decomposition are not excluded.
