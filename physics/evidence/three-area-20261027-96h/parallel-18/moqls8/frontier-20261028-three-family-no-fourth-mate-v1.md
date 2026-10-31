# The frozen nonclassical three-family has no ordinary fourth mate

**WRITTEN candidate with two exact finite edge checks; disjoint mathematical review pending.** For the specific frozen three-MOQLS(8) witness `frontier-20261028-three-family-mixed8-witness-v1.json`, SHA256 **a638a5db88a5d76c01625c4857ff50888c06f26cd5a012571a423add53fec413**, there is **no** ordinary complex QLS D orthogonal to all three members. The obstruction is a literal set of nine cells whose D rays would have to be pairwise orthogonal in C^8.

This is a statement about **this one three-family only**, not all three-families, a global upper bound on M(8), an unrestricted four-family no-go, a novelty/priority result or an A10/A11 qualification. The parent has reported that the original three-member witness itself was physically validated under its f125 same-harness gate; the implication below can be reviewed directly from the nine rows and 36 marked edges without assuming any catalogue classification or numerical solver result.

## 1. The nine cells

Use zero-based linear index `x=8i+j`. The two classical members are A,B; `+ = (e_0+e_1)/sqrt(2)` and `− = (e_0−e_1)/sqrt(2)` are rays of the frozen quantum member Q. The relevant exact cells are:

| x | (i,j) | Q ray | A symbol | B symbol |
|---:|:---:|:---:|---:|---:|
| 0 | (0,0) | e_0 | 0 | 0 |
| 1 | (0,1) | e_1 | 1 | 1 |
| 2 | (0,2) | e_2 | 2 | 2 |
| 9 | (1,1) | e_0 | 2 | 5 |
| 17 | (2,1) | e_2 | 4 | 0 |
| 18 | (2,2) | + | 7 | 3 |
| 19 | (2,3) | − | 6 | 2 |
| 26 | (3,2) | − | 4 | 1 |
| 37 | (4,5) | + | 4 | 2 |

For a pair of distinct listed cells, any one of the following conditions forces the proposed D rays orthogonal:

- `R`: same grid row, by D's QLS row ONB;
- `C`: same grid column, by D's QLS column ONB;
- `A` or `B`: equal indicated classical symbol, because the corresponding classical⊗D product ONB has nonzero classical overlap;
- `Q`: the Q rays have nonzero overlap, because the Q⊗D product ONB then forces D's overlap to vanish.

The following upper-triangular rows give one valid reason for **each** of the 36 unordered pairs, in the displayed cell order. For example, the first row gives reasons for 0 against 1,2,9,17,18,19,26,37; the second for 1 against 2,9,17,18,19,26,37.

```text
0:  R R Q B Q Q Q Q
1:    R C C Q Q Q Q
2:      A Q C B C B
9:        C Q Q Q Q
17:         R R A A
18:           R C Q
19:             Q B
26:               A
```

Each Q entry marked `Q` is nonzero exactly, not a numerical tolerance: overlaps among the listed e_0,e_1,+,− rays are ±1/sqrt(2) or 1 where indicated, and the e_2/e_2 edge is 1. For instance, 0–18 has Q overlap 1/sqrt(2); 0–17 has equal B symbol 0; 18–37 has identical Q ray `+`; and 19–26 has identical Q ray `−`.

## 2. Dimension contradiction and checks

If a fourth D existed, the table forces its nine normalized nonzero cell rays to be pairwise orthogonal. C^8 has dimension eight, so this is impossible. The proof does not require D to be classical or real, and it does not infer that another nonclassical three-family cannot extend.

`frontier-20261028-three-family-nine-clique-check-v1.py` SHA256 **cb58c88973416a8552a9963c5adb4047db97a232d1c6d79119b7324acf73b6af** independently reads the pinned witness and records all 36 exact edge reasons; receipt `frontier-20261028-three-family-nine-clique-check-receipt-v1.json` SHA256 **6d03ae117caa884f4d3ab133b77410f5153a9e8f955e4d6c035253a6f47f8797**. It rejects a missing-vertex mutation, a quantum-ray mutation destroying the uniquely justified 0–18 edge, and a B-symbol mutation destroying the uniquely justified 0–17 edge for their intended reasons.

A separately written fixed-label table audit `frontier-20261028-three-family-nine-clique-table-check-v1.py` SHA256 **1b317aa0234058c2f2d44745bfcdd30c15c767bcef509ad1f46787070caa9ca5** checks each of the 36 displayed labels and rejects a changed edge label; receipt SHA256 **068bfb5e293453419415aa4e04ebbcc59b805fac0d77f65dde6ef05f8d65140b**. Both are owner-local finite checks, not a substitute for disjoint mathematical review of the original QLS/product-ONB implications or broader witness/priority gates.
