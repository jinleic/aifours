# No transversal in the BH(10,6) Fourier-product family

**CATALOG-CONDITIONAL, COMPUTER-ASSISTED AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date` at independent certificate replay: **Wed Oct 28 19:37:32 PDT 2026**. This is a stronger-than-maximal, NONuniform, ALL-L restricted-family result; it does not rule out general quantum Latin squares.

## 1. Claim and classification import

For ANY `K in BH(10,6)`, with arbitrary Hadamard row/column phases or permutations, the actual Fourier-product QLS

`psi_(r,c)(t)=zeta10^(r t) K_(t,c)/sqrt(10)`

has **NO orthogonal transversal**. Hence it has no 1-resolution for ANY L, even allowing repeated rays. The ALL-K conclusion imports the computer classification of Lampio, Östergård and Szöllősi, [Orderly generation of Butson Hadamard matrices](https://arxiv.org/html/1707.02287v1), Theorem4.1/Table2, reporting 34 monomial classes. Its [official supplement](https://wiki.aalto.fi/spaces/Butson/pages/120482304/Matrices+up+to+monomial+equivalence) provides the 34 representatives; the literal frozen file `frontier-20261028-aalto-bh10-6-catalog-v1.txt` has SHA **3aab0ddb9d500946fbb45909fb6d5f6c46402033e2b26b797fce7a2a3547e281**. The catalog completeness calculation was not independently regenerated.

Row phases of K are a common coordinate unitary, column phases are cell phases, and column permutations merely relabel cells. Every possible row permutation is covered by the finite reduction below. The paper's q-root monomial equivalence is thus sufficient, and arbitrary further phase gauges are harmless.

## 2. Complete half-graph sieve

For a putative transversal, pair its cells in rows r,r+5. Let E be the five K rows assigned to even physical coordinates. The ten distinct K columns used by the transversal must admit a perfect matching in the graph where c,d are adjacent iff

`sum_(t in E) conjugate(K_(t,c))*K_(t,d)=0`.

Indeed K-column orthogonality says the E and O sums add to zero, and opposite-row physical orthogonality says they subtract to zero. The complement O gives the identical graph.

Two separate exact implementations checked all 34 matrices and all `34*252` five-row subsets. `frontier-20261028-aalto-halfgraph-census-v1.py` SHA **10a5ca121f1f9395bbcc3292d426b1c63d5a5f76fc3fa74961943ff076187d16** uses cyclotomic coefficient reduction and bitmask matching; independently `frontier-20261028-aalto-q6-root-replay-v1.py` SHA **0ce69200852acbfbf5f7f6b5f5b5039eeb06e81e12a833c54bb58509f51bed06** uses the integer basis `(1,zeta6)` and recursive set matching. Both verify every representative's 45 K-column orthogonalities and find exactly50 matching half-subsets: two each for classes7,16,19,22,26, and40 for class28. The other28 classes have no matching half and therefore no transversal under ANY physical K-row ordering.

## 3. Exact row-obstruction certificate for every survivor

E and O are interchangeable by a cyclic shift of the physical coordinate index. An even further shift puts source row0 at physical coordinate0, at the cost only of a common coordinate permutation and row-dependent cell phases. Thus take the25 matching subsets containing source row0; for each there are exactly `4!*5!=2880` remaining coordinate orders, a total of **72000**. No duplicate-ray or maximality filter is applied.

Any transversal can be translated in its physical row index so that its column0 cell lies at row0: `psi_(r+s,c)=D_s psi_(r,c)` for one common diagonal unitary D_s. For EVERY normalized coordinate order the certificate identifies one row `r in {1,...,9}` in which **NO different column d=1,...,9** is orthogonal to the `(row0,column0)` vector. Therefore no transversal can contain that normalized cell, and none exists.

`frontier-20261028-aalto-q6-root-certificate-v1.py` SHA **7584355de6e2f05e7ee8beb02a8f6813353457d27f388a64afb8ff657ea55dc6** produces `frontier-20261028-aalto-q6-root-certificate-v1.json` SHA **a929cfa6593b35d70b9f19812806a3fb3609dd27317bc93dbeb099ec3827a3eb**. It records, in deterministic lexicographic 4!×5! order, the obstructed-row digit for each of72000 orders. It uses exact Phi30 integer reduction on the actual physical root30 inner products.

The independently written replay SHA **0ce69200852acbfbf5f7f6b5f5b5039eeb06e81e12a833c54bb58509f51bed06** rebuilds ALL half graphs and their25 normalized survivors from the raw source catalog, checks their exact agreement with the certificate, reconstructs EVERY physical row order and tests all9 column inner products at its stated obstructed row. Its arithmetic is a different exact representation: `zeta30=-zeta3*zeta5`, using the 8-element product basis for the linearly disjoint fields Q(zeta3),Q(zeta5), rather than the producer's Phi30 reduction. Actual output ended:

```text
PASS all34 BH; 50 matching halves; all72000 root obstructions in Q(zeta3,zeta5)
```

A third C++ on-demand Phi30 scan `frontier-20261028-aalto-mixed-exhaustive-v1.cpp` SHA **21f30b002e00eb6428c72ac6adb3b21d0537047b513c0a0bb1d3e69ceb9dbebd** independently found `72000 root_empty, 0 branched` over those25 halves. None of these runs used floating arithmetic or timed out. The full 72000 row digits are retained for a reviewer to replay, not just an aggregate.

## 4. Boundary

The finite evidence proves the stated no-transversal result for the 34 literal representatives and every physical row ordering, conditional on the described symmetry caller. Extending to ALL BH(10,6) K imports the published 34-class completeness. This does NOT exclude BH(10,12), arbitrary higher/composite phase order, general complex Hadamards, other physical formulas or nonproduct QLS10. In particular, no candidate witness or unrestricted impossibility is claimed. Full independent mathematical/code review and novelty assessment remain necessary.
