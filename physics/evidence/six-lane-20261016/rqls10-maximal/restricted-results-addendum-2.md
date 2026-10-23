# Addendum 2 to restricted-results-v1.md: R8 (controlled tensor products) and open split families

Written about 14:55 PDT, 2026-10-18. Lane-internal, **unreviewed**, restricted only.

## R8. Controlled tensor products for 10 = 2 x 5 and 10 = 5 x 2 never reach 100 rays

**Ansatz.**
- Cells are ((i1,i2),(j1,j2)), with outer indices in [m] and inner indices in [n], mn = 10.
- q = x_{i1 j1} (x) y^{(i1 j1)}_{i2 j2}.
- x is a QLS(m) on C^m. Each y^{(i1 j1)} is a QLS(n) on C^n and may depend on the outer cell.
- Rows and columns are automatically ONBs.
- B is any Latin square on the 100 cells.

**m = 5, n = 2.**
- Every QLS(2) has the form y00 = y11 = b and y01 = y10 = b^perp, as rays (orthogonality in C^2).
- So each outer cell's 2x2 block carries only the rays x (x) b and x (x) b^perp, each twice.
- Hence at most 50 rays, for every B.

**m = 2, n = 5.**
- x is a QLS(2): outer blocks (0,0) and (1,1) carry qubit ray a, and blocks (0,1) and (1,0) carry a^perp.
- This is the rectangular 5+5 half-split of R5. A class with x cells in block (0,0) has 2x cells with qubit ray a, but
  an ONB of C^10 needs 5 of them.
- So no B makes this a 1-RQLS.

## Split families not excluded (recorded so they are not mistaken for closed)

Setting: C^10 = W_1 (+) ... (+) W_k, with every cell vector inside one W_a and every line meeting the cells of W_a in
exactly dim W_a cells. A part of dimension 1 or 2 always repeats rays (R5).

| split | status |
|---|---|
| 5+5, rectangular | excluded (R5, Mann parity) |
| 5+5, non-rectangular W-cell patterns | **open** |
| 3+7 with a closed 3x3 block | excluded (QLS(3) has 3 rays) |
| 3+7 without such a block | **open** |
| 4+6 with a 4x4 corner block R1 x C1 inside the W_4-cells | combinatorially **feasible** (see below); **open** |
| 4+6 otherwise | **open** |
| 3+3+4 and other multi-splits with all parts >= 3 | **open** |

The 4+6 corner case in detail:
- Assume |R1| = |C1| = 4, and the remaining W_4-cells Q lie in R2 x C2 with 4 per row and per column.
- A class meeting R1 x C1 in x cells meets Q in 4 - x cells and the W_6-cells in 6 cells. This is consistent for every
  x in {1,..,4}. There is no parity obstruction, unlike two 5x5 blocks.
- Source Example 2.4 for v = 8 is of the analogous two-4x4-block type. Each class meets each block in 2 cells.
- A maximal-cardinality QLS(4) can fill the corner (16 rays). The coupled Q- and W_6-parts are unsolved.
- Classical analogue: a pair of incomplete MOLS (IMOLS) of type (10,4) would need 10 >= 12, so a common 4x4 hole is
  impossible. Here, however, B is not required to have a subsquare at the corner.
