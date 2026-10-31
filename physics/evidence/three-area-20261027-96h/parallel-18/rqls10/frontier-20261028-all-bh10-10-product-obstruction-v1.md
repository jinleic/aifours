# No maximal 1-RQLS in the BH(10,10) Fourier-product family

**CATALOG-CONDITIONAL, COMPUTER-ASSISTED AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date` at independent replay: **Wed Oct 28 19:33:42 PDT 2026**. The catalog completeness and the mathematical caller must receive independent review before adoption. This is a NONuniform, ALL-L restricted-family obstruction; it is NOT an unrestricted QLS10 no-go.

## 1. Exact statement and named import

Let K be ANY BH(10,10) matrix, possibly after arbitrary Hadamard row/column phases or permutations, and put

`psi_(r,c)(t)=zeta10^(r t) K_(t,c)/sqrt(10)`.

**Claim:** this product QLS cannot simultaneously have100 distinct rays and an orthogonal transversal. Hence it cannot be a maximal 1-RQLS for ANY L. The proof does NOT claim that every such array has no transversal: some excluded branches have repeated rays.

The ALL-K quantifier imports the computer classification of Lampio, Östergård and Szöllősi, [Orderly generation of Butson Hadamard matrices](https://arxiv.org/html/1707.02287v1), Theorem4.1/Table2 and [electronic supplement](https://wiki.aalto.fi/spaces/Butson/pages/120482304/Matrices+up+to+monomial+equivalence), which list exactly51 BH(10,10) monomial-equivalence classes. This prior exhaustive classification was not independently regenerated. The 51 literal representative lines used here are `frontier-20261028-aalto-bh10-10-catalog-v1.txt`, SHA **3275d1f074dc3ac1bf82479755efb1f385361778ca35f85783a55be6cb4d0c55**, in the supplement's documented BH1 binary format. BOTH exact scans below independently checked every representative has 10×10 tenth-root entries and all45 K-column orthogonalities.

Row phases are a common coordinate unitary and column phases are cell phases; column permutations relabel cells. Every K row permutation is explicitly covered by the enumeration below. The theorem additionally holds after arbitrary row/column phase gauges, not just the root gauges in the cited classification.

## 2. Exact half-matching and ray caller

For any putative transversal, pair its cells in rows r and r+5; their ten K-column labels form a perfect matching. Let E be the five K rows occupying even Fourier-coordinate positions and O its complement. K-column orthogonality gives `S_E+S_O=0`, while orthogonality of an opposite-row pair gives `S_E-S_O=0`. Hence every matched pair has `S_E=0` and the graph on K columns with these half-zero edges MUST have a perfect matching.

If any two K columns have their phase quotient constant lambda on E and constant -lambda on O, then the product array has repeated rays: the appropriate two cells in rows differing5 are parallel. This is a NECESSARY obstruction to maximality, independent of the internal order of E and O. More generally a given ordered K-row arrangement has100 distinct rays iff no two K columns have quotient `lambda*zeta10^(m t)` for any m∈Z10. Both checks are exact.

All252 five-row E subsets of each of the51 matrices are checked. The literal first census `frontier-20261028-aalto-halfgraph-census-v1.py`, SHA **10a5ca121f1f9395bbcc3292d426b1c63d5a5f76fc3fa74961943ff076187d16**, result SHA **bba91b5b397409e5f84ccde7d4798ac27099715b9c4577b43fbecfc13da2612f**, used exact cyclotomic root-sum reduction and bitmask matching. It found 56 matching half-subsets. The separately coded collision audit SHA **b318595e667a3a2c191e51c27e21951f4c3f96b21d3b6ac746d9ca22ffd5e312**, result SHA **1c4ffcf2d9d2d2ae07f373f97750fd4e614397b41098b1f48484e4a12475562e**, found that50 of those56 force opposite-row repeated rays.

The six remaining subsets comprise three E/complement pairs, all on catalog classes 1,9,18. Taking the representative containing source row0, each has `E=(0,2,3,5,7)`; their complements are equally covered because full K-column orthogonality makes the E and O half graphs identical.

## 3. Every remaining coordinate order and transversal

A cyclic shift of the PHYSICAL coordinate index t acts as a common coordinate permutation and a cell phase `zeta10^(r*s)`. It preserves the original ONB and ray conditions. Such a shift can put source row0 at even physical index0: first an odd shift if necessary to choose the E/complement representative containing it, then an even shift to place it at0. This leaves exactly `4!*5!=2880` row arrangements per surviving class, with NO WLOG restriction on K beyond these proven symmetries.

For each arrangement, the code discards a case only if the full exact 45×10 Fourier-character test finds a repeated ray. For the remainder, any transversal may be shifted in its physical row index by a common diagonal unitary until its unique column0 cell is at row0; hence the exhaustive search fixes `(row0,column0)`. It then checks all possible placements of the other nine columns, using exact Phi10 integer reduction for every tested physical inner product.

C++ implementation `frontier-20261028-aalto-q10-exhaustive-v1.cpp`, SHA **8d1f4b22654e08b21b2ca30501b136bc3607bf9c6827cf36e904137ccaa6865d**, uses bitmask MRV backtracking. Independently written Python `frontier-20261028-aalto-q10-independent-v1.py`, SHA **6b4322621851237fa0a0274acc8100c5636dd796a820975b53b7cd422f3bde4e**, reconstructs the 51 Hadamards, ALL252 half graphs, all collisions and surviving classes with a different polynomial-reduction/recursive-matching implementation; it then uses FIXED-row, rather than MRV, transversal backtracking for all2880 orders in each class. Its result SHA is **94932010fd4a7679e21e6f29d3dbe6b3d7043f3a094543949f26eaf28ee56fe1**. Actual outputs:

```text
51 valid BH matrices; 56 matching halves; 50 immediate opposite-row collisions
class 1: 2880 arrangements, 24 further duplicate-ray, 2856 distinct-ray checked,
         2708 empty at row0 prune, 148 branched, no transversal
class 9: 2880 arrangements,  8 further duplicate-ray, 2872 distinct-ray checked,
         2716 empty at row0 prune, 156 branched, no transversal
class18: 2880 arrangements, 24 further duplicate-ray, 2856 distinct-ray checked,
         2708 empty at row0 prune, 148 branched, no transversal
```

C++ independently returned the same duplicate/checked counts and no transversal, with MRV DFS node counts3264,3352,3264. The Python fixed-order DFS node counts are972,1282,972 for the branched cases; those counts differ by algorithm and are NOT compared as if they were identical. Neither program uses floating arithmetic. Both complete rather than report a timeout.

## 4. Precise conclusion and remaining gap

The exact finite result covers the PROVIDED 51 representatives and every K-row ordering, up to the two proven cyclic symmetries, and checks original physical inner products/ray quotients. Upgrading that finite result to ALL BH(10,10) K uses the cited prior monomial-classification completeness and the stated gauge/column-relabelling caller. The preceding all-BH(10,5) result was independently self-contained up to its own finite certificate; it is a subfamily of the present catalog-conditional q10 statement.

This says nothing about arbitrary q, BH(10,6), BH(10,12), general complex Hadamards or nonproduct QLS10. In particular, 50 opposite-half matchings were observed for q6 and330 for q12 in the broader census; a half-graph perfect matching is only necessary, not an actual transversal, and those cases are NOT silently excluded. Independent review, exact proof/certificate replay by another party, catalog-source verification and novelty assessment remain pending.
