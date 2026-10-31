# Order-10 resolvable QLS: a locally rigid published classical reference

**Status: NEW WRITTEN/EXACT-CHECKED AUTHOR CANDIDATE, unreviewed.** Native `/bin/date` observed after initial creation and before correcting this header: Wed Oct 28 17:04:48 PDT 2026; exact initial creation time was not observed. The general local-rigidity theorem below is written mathematics; its application to the published order-10 table uses two separately written exact finite checkers. The random coupled-vector experiment is floating-point exploration, not a proof or witness. No novelty claim or global order-10 conclusion is made.

## 1. First scientific result and exact scope

Let n>=3. Let A and L be orthogonal Latin squares of order n, and regard L as the partition into n disjoint row/column transversals. Consider the CLASSICAL reference array `v_(r,c)=e_(A(r,c))` in C^n, which has n distinct rays and satisfies all 3n required basis constraints. For each unordered distinct symbol pair {a,b}, form a graph on its 2n cells: in every row, column, and L-transversal join the two cells whose A-symbols are a and b. Suppose EVERY one of these pair graphs is connected.

**Theorem (local rigidity, conditional on connected pair graphs).** There exists an open neighborhood of that reference in the space of labelled unit-vector arrays such that every array in the neighborhood satisfying the SAME row, column and L-transversal orthonormality constraints is obtained from the reference by ONE common unitary and individual cell phases. In particular all those nearby arrays have exactly n rays, so NONE has n^2 pairwise nonparallel rays.

This is local to one chosen A,L and its classical reference, NOT an unrestricted no-go, not a claim that every OLS pair has connected pair graphs, and not a statement about distant/nonclassical components. A common unitary/phase change in the theorem conclusion is an exact equivalence of labelled arrays, not a claim that one may assume a global ansatz WLOG for the whole target.

**Order-10 application.** For Weisner's published 1963 Fig. 1 pair transcribed in §4, all45 pair graphs are connected; hence its associated classical 10-ray array is locally isolated up to the above symmetries. Two independent exact algorithms check the graph connectivity and the original 30 actual-vector basis conditions. This is an exact, limited obstruction to a perturbative route around this particular starting array and fixed resolution; it does not show a 100-ray solution cannot exist elsewhere.

## 2. Complete proof of the local theorem

Every one of the 3n blocks has each A-symbol once. For a differentiable family of unit vectors at the reference, write the first-order variation at a cell x of color a as `d_x`. Unit norm implies `Re <e_a,d_x>=0`, so its a-component is purely imaginary and represents a per-cell phase direction.

Fix ANY two distinct colors a,b. For x of color a set `q_x=(d_x)_b`. For y of color b set `q_y=-conjugate((d_y)_a)`. Whenever x,y are paired by any one of the row, column or L-transversal blocks, differentiating their orthogonality gives

`0=<d_x,e_b>+<e_a,d_y>=conjugate((d_x)_b)+(d_y)_a`,

hence `q_x=q_y`. Each graph is bipartite, with ten or, generally, n vertices of each of the two colors; graph connectedness therefore forces ONE complex value q_ab across its entire 2n-vertex graph. These equalities are exact and use every block, not separately fitted row/column/transversal objects.

For all a<b define the off-diagonal entries of an n×n skew-Hermitian matrix K by `K_(b,a)=q_ab` and `K_(a,b)=-conjugate(q_ab)`, with zero diagonal. Then for EVERY cell x of color a, the off-color entries of d_x equal those of `K e_a`. Its remaining diagonal entry is an independent imaginary per-cell phase. Thus the ENTIRE tangent kernel consists exactly of infinitesimal common-unitary directions plus per-cell phase directions. Conversely those directions obviously preserve all original basis conditions. No dimension count alone is used to assert existence of a nonlinear continuation.

To pass from infinitesimal to ACTUAL local rigidity, take any sufficiently nearby exact solution. Its first row is an ONB. Apply the inverse of the unique nearby common unitary carrying the reference first-row vectors to that row, so that the first row is exactly its reference basis. Independently rephase each other vector so its coordinate on its reference color is positive real. This is possible in a neighborhood, with unique phases; it does not change any orthogonality or ray identity.

In these gauges, use the remaining off-color complex coordinates as local variables z; the positive real on-color coordinate is the positive square root imposed by unit normalization. This gives a finite-dimensional smooth coordinate chart around z=0. Let F(z) collect real and imaginary parts of ALL within-block off-diagonal inner products. The previous tangent argument, together with the first-row gauge, forces all off-diagonal entries of K to be zero; the positive-real phase gauge and normalization then force every diagonal phase variation to zero. Therefore `DF(0)` is injective on the gauge-fixed variables.

In finite dimensions, injectivity gives a constant c>0 with `||DF(0)z||>=c||z||`. Smoothness gives `F(z)=DF(0)z+o(||z||)`. For all sufficiently small nonzero z, `||F(z)||>0`; thus an exact solution F(z)=0 in that neighborhood has z=0. Undoing the common unitary and cell phases yields precisely the claimed local equivalence. The proof does not require that the tangent space be integrated or that a nonlinear search failed. The neighborhood is existential; no numerical radius is claimed.

## 3. Exact original-object incidence and independent orbit checks

Published input: Louis Weisner, *Special Orthogonal Latin Squares of Order 10*, Canadian Mathematical Bulletin 6(1) (1963), Fig. 1, DOI [10.4153/CMB-1963-009-0](https://doi.org/10.4153/CMB-1963-009-0); the actual published PDF text/table was read at https://www.cambridge.org/core/services/aop-cambridge-core/content/view/571060BE1548BAE1FE39B45B58F4403E/S0008439500051638a.pdf/special-orthogonal-latin-squares-of-order-10.pdf . The two decimal digits below are respectively A-symbol and L-label:

```text
00 28 59 84 67 32 15 93 71 46
82 11 30 69 05 78 43 26 94 57
95 03 22 41 79 16 80 54 37 68
48 96 14 33 52 89 27 01 65 70
76 50 97 25 44 63 09 38 12 81
23 87 61 98 36 55 74 19 40 02
51 34 08 72 90 47 66 85 29 13
39 62 45 10 83 91 58 77 06 24
17 49 73 56 21 04 92 60 88 35
64 75 86 07 18 20 31 42 53 99
```

`frontier-20261028-ols10-switch-v1.py`, SHA256 **394c59221d0526ca623d46925d4d82e68d13ddb55b6c45f5bdada1ee622ff172**, independently checks both coordinates' row/column Latin property and all100 distinct ordered pairs, then directly builds all3 block-pair matchings for every color pair and computes connected components. Actual output:

```text
published_table: PASS; both rows/columns Latin; 100 distinct ordered pairs
all 45 color-pairs: component-size distribution {(20,): 45}
independent component switch opportunities: 0
```

A separately written, independently transcribed check, `frontier-20261028-rigidity-orbit-check-v1.py`, SHA256 **96fc18b25c872185b6e89b42418b4eeb6d6e1230316799335428579cb676210e**, checks the ORIGINAL classical vector block inner products exactly (Kronecker deltas), and computes the same connectivity by row permutations/orbits rather than the 20-cell graph code. Actual output:

```text
reference: all 30 original vector blocks exactly orthonormal; labels are disjoint transversals
reference ray cardinality: 10 of 100
row-permutation orbit sizes across 45 symbol pairs: {10: 45}
tangent count: 45 complex global-mixing parameters + 100 real per-cell phases = 190 real
gauge-fixed reference tangent kernel dimension = 0; local isolation follows by analytic argument
```

The 190 count is 90 real off-diagonal common-unitary directions plus100 per-cell phase directions; global diagonal phases are redundant with the per-cell phases. In the proof's fixed-row/positive-coordinate gauge all those directions vanish. The independent graph routines establish the finite instance, not the analytic local theorem by themselves.

## 4. Rejected web-generated table: COMPLETE replay input/output

The generic search response proposed the following as a pair of orthogonal Latin squares. It is not a published-table primary source, and its orthogonality assertion is **false**. `frontier-20261028-latin-check-v1.py`, SHA256 **4c311f8a4ae6ed5c0ade63bc5692cec4ebd06dac187c7d47ad77011b22fd070d**, contains the COMPLETE replayable input below and the exact deterministic check.

```text
L1
0 1 2 3 4 5 6 7 8 9
1 0 3 2 5 4 7 6 9 8
2 3 4 5 6 7 8 9 0 1
3 2 5 4 7 6 9 8 1 0
4 5 6 7 8 9 0 1 2 3
5 4 7 6 9 8 1 0 3 2
6 7 8 9 0 1 2 3 4 5
7 6 9 8 1 0 3 2 5 4
8 9 0 1 2 3 4 5 6 7
9 8 1 0 3 2 5 4 7 6

L2
0 1 2 3 4 5 6 7 8 9
2 3 4 5 6 7 8 9 0 1
4 5 6 7 8 9 0 1 2 3
6 7 8 9 0 1 2 3 4 5
8 9 0 1 2 3 4 5 6 7
1 0 3 2 5 4 7 6 9 8
3 2 5 4 7 6 9 8 1 0
5 4 7 6 9 8 1 0 3 2
7 6 9 8 1 0 3 2 5 4
9 8 1 0 3 2 5 4 7 6
```

Actual run `python3 frontier-20261028-latin-check-v1.py`:

```text
L1 rows_latin True columns_latin True
L2 rows_latin True columns_latin True
distinct_ordered_pairs 90 of 100
repeated_pair_groups 10
first_repeated_pair ((0, 0), [(0, 0), (9, 3)])
orthogonal False
```

This rejects ONLY that proposed pair, not the known existence of two orthogonal Latin squares of order10 and not the QLS target. It is included as a data-integrity falsification, not counted as mathematical target progress.

## 5. Actual coupled-vector search, not a relaxation

Using Weisner's verified L, `frontier-20261028-coupled-projection-v1.py`, SHA256 **8338ed1210e6984d17ee43bdd61c823c24126997e9a6ca34906e8845a661f06a**, starts from complex 10×100 arrays and cyclically replaces each of the30 required 10-column blocks by its polar unitary factor. It operates on SAME actual cell vectors for all blocks. Four seeded restarts,400 sweeps each, single BLAS thread, took1.19s. At sweep samples, the best saved vector array had maximum within-block Gram error **0.30097746430753547** and maximum distinct-cell inner-product modulus **0.854757111010105** (seed1,sweep250). Other final maximum block errors were0.34353513070564573,0.36061690324077983,0.4277510046222571,0.330972669503362 for seeds0–3 respectively.

Full record `frontier-20261028-coupled-projection-result-v1.json`, SHA256 **236e479d1a1bd7cd4352768a9d956a460622cc86826798f3352b0662cf1a21e9**; best FLOATING candidate data `frontier-20261028-coupled-projection-best-v1.npy`, SHA256 **81be1052d315bb3d3503d1f6f04467499b233279cf25c6629250dfe5a8a12f25**. The first metric is very far from zero, so this is NOT a valid QLS or an approximate verification of the requested orthogonality. The experiment does not establish global convergence, infeasibility, a certified gap or a bound across other Latin incidences; it only reports the actual bounded run and a reusable exploratory iterate.

## 6. Remaining target and independent verification boundary

Original target remains: an ACTUAL 10×10 unit-vector array in C10, 30 simultaneous original ONBs including a partition into ten actual transversal ONBs, and100 pairwise nonparallel rays, OR an unrestricted obstruction over every resolution incidence. The theorem above excludes only a neighborhood of one published classical 10-ray reference. Other references, disconnected pair graphs, nonlocal continuous/discrete families and distinct incidences remain. Neither the numerical failure nor the source's list of possible exceptions is a worldwide nonexistence theorem.

An actual candidate would need an independently written original-definition verifier checking every complex inner product, norm, transversal incidence and all4950 distinct-cell ray pairs with an exact certificate or rigorous error bounds. No such100-ray candidate has been found. Local-rigidity proof requires independent review before adoption. Past process/quarantine records are historical and remain unaltered; no held outcome is used as a mathematical premise. New local computations were run under the prospective owner direction; no external model, secret, deletion, publication or infrastructure action.

**END initial scientific candidate and bounded experiment report.**
