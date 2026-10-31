# Exact transversal criterion for a two-sector QLS10

**WRITTEN AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date`: **Thu Oct 29 00:14:05 PDT 2026**. This reframes the obstruction of the 100-ray sector example as a concrete constructive decision problem; it does not solve that problem.

## Construction

Let Q be ANY QLS of order5 with unit vectors `q_(r,c)`, and let U,V be arbitrary unitaries on C5. Define

`psi_((a,r),(b,c)) = |a xor b> tensor (U^a V^b) q_(r,c)`,

where `a,b in {0,1}` and `r,c in {0,...,4}`. This is always a QLS10: fixing a global row, the two b-blocks lie in orthogonal sectors and each is a unitary image of a local Q row; fixing a global column, the two a-blocks lie in orthogonal sectors and each is a unitary image of a local Q column. Different blocks may overlap in ray content, and 100 distinct rays require a separate check.

## Exact criterion

Consider a transversal represented by a global-column permutation `p` on the ten rows. Define its sector-zero and sector-one cell sets

`T_0={((a,r),(b,c)): b=a}`,  `T_1={((a,r),(b,c)): b!=a}`.

Each set must contain exactly five cells: their vectors lie in a 5D sector, and all ten transversal vectors are orthogonal. Therefore the XOR count of (a,b) over the permutation must be five. But for EVERY permutation of the ten columns, exactly five b=1 values and five a=1 values occur, so the sum of a xor b is even. This is impossible.

Thus **NO choice of U,V,Q** in this construction has any transversal. This recovers the additive-sector theorem and explains why changing the relative sector gauges, even to generic full unitaries, cannot repair the 100-ray example. To escape, a construction must mix sectors within at least one cell or change the sector-label incidence away from XOR; simply adjusting U,V within each sector is a dead end.

This is an elementary exact argument, not an unrestricted impossibility or a claim about all individually separable rays. It applies after common unitary and cell phases; it needs independent review.
