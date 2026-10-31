# Maximal 1-RQLS(10): frontier map after the quantum-Mann work (29 Oct)

**SYNTHESIS OF UNREVIEWED AUTHOR CANDIDATES.** Native `/bin/date`: Thu Oct 29 06:31:13 PDT 2026. This document only collects statements proved or certified in the cited packets. No new claim is made here except where marked *[new here]*. The target remains OPEN.

## 1. Target and literature status

- **Target.** 100 pairwise non-parallel rays in C^10, arranged in a 10x10 array. Rows, columns and the ten classes of a resolution Latin square L must all be orthonormal bases.
- **Equivalent forms.**
  - L has a maximal-cardinality *quantum orthogonal mate*.
  - In Ball–Simoens language: an orthonormal representation in C^10 of the complement of L's Latin square graph, with all 100 vectors distinct.
- **Zhang–Cao, arXiv:2608.29201v2.** The open orders for maximal 1-RQLS(v) are exactly {10, 14, 18, 22, 26, 30, 34, 38, 42, 46, 54, 58, 62, 66, 74, 82, 94}. All of them satisfy v ≡ 2 mod 4. Their constructions need complete mappings, which groups of these orders lack (Hall–Paige).
- **Ball–Simoens, arXiv:2603.02334.**
  - No 2 MOQLS(6). This includes every 1-RQLS(6), of any cardinality.
  - 2 MOQLS(4) and 2 MOQLS(5) are classical.

## 2. Parity cores and the quantum Mann dichotomy

- A 1-RQLS(2m) contains an odd "parity core" (each cell in 0 or 2 selected bases) **iff** L has a Z2 quotient with m odd. *[new here: the reverse direction uses that a Z_p quotient with p odd admits only constant 0/1 solutions.]*
- In that case R0 ∪ C0 ∪ T1 is an orthonormal representation of L(K_{m,m,m}) in C^{2m}. Packet: `frontier-20261029-quantum-mann-kmmm-reformulation-v1.md`.
- **m = 3 is impossible** (Theorem A, written proof). Packet: `frontier-20261029-quantum-mann-dichotomy-k333-k555-v1.md`, SHA `9fba4852…dde3c`.
- **m = 5 exists.** Exact certificate in Z[ζ20]: 75 distinct flat rays, irreducible. Same packet.
- **m = 7 exists.** Exact certificate in Z[ζ28]. Packet: `frontier-20261029-half-resolved-maximal-qls10-and-m7-v1.md`, SHA `e72f7c7d…91d1`.
- **Flat Z_m^2-diagonal core criterion** *[new here, written; follows from the torus-kernel analysis in the cited packets]*. Let T be uniform along alpha, beta and alpha - beta, and let U be the union of the three induced perfect matchings on the 2m coordinates. Then the K-part is solvable iff every bipartite component of U has an even number of edges from each matching.
  - A two-line base with one hexagon trade meets the criterion for m = 5, 7, 13, 17, 23, 25, 29, 31 (computed).
  - The same family fails for m = 9, 11, 15, 19, 21, 27.
  - Existence for all odd m ≥ 5 is conjectured.

## 3. Full Z2-quotient squares

- **Flat Z_m^2-diagonal four-orbit ansatz: no square** for m = 5 (13,600 cases) and m = 7 (358,092 cases). Exact torus criterion. The mechanism is an odd integer circulation on the quadrant graph K4, which forces pi ≡ 0.
- **Consequence.** No flat abelian-character 1-RQLS(10) exists under a free diagonal action of |A| ≥ 25. Packet: `frontier-20261029-flat-character-1rqls10-no-go-v1.md`, SHA `1c8c5768…bb5b`. The same reduction gives the result for v = 14, |A| ≥ 49.
- **Numerical only** (no exact claim):
  - non-flat diagonal weights: best residual 0.0955;
  - Heisenberg Z5^2 actions: no core;
  - a warm start from the exact core stalls at 2.389.
- **Exact maximal QLS(10) with half a resolution.** 100 distinct rays; rows and columns are orthonormal bases; 5 disjoint orthogonal transversals; exactly 5 orthogonal transversals in total. Hence it is not 1-resolvable. This is the best explicit maximal-cardinality object so far.

## 4. Earlier exclusions (unchanged)

These are from the 27–28 Oct packets in this root:
- Fourier-product families: all odd orders, all orders with no factor 3, the q30 frontier, Dita and non-affine slices;
- Parker/Weisner classical-mate rigidity, with the 13-ray bound for globally two-sparse arrays;
- sector cardinality bounds;
- 4+6 sector parity-core analyses (Pauli and 600-cell cores).

Each was claimed only within its stated scope.

## 5. Where a maximal 1-RQLS(10) could still hide

1. **Z2-quotient L.** The core must be completed beyond flat characters. The local moduli of the known core equal the flat family, so a solution needs another component of the K5,5,5 variety.
2. **L without a Z2 quotient.** There is no parity core and none of the obstructions above applies. Classical mates exist for some such L (Parker, Weisner). A maximal quantum mate needs genuinely non-classical blocks; the earlier rigidity results limit near-classical deformations.
3. **Universal obstruction.** This is untried, apart from Ball–Simoens-style combinatorial closure. For order 10 that is plausible only with the maximal-cardinality (no merging) assumption and strong symmetry.

## 6. Recommended next steps

1. Run Ball–Simoens-style closure (projective-line propagation, 11-clique and complete-tripartite dimension counts, no merging) on the cyclic Z10 square, assuming maximal cardinality.
2. Search other components of the K5,5,5 variety using non-abelian symmetry groups.
3. Prove the odd-circulation lemma for all odd m in the flat ansatz.
4. Seek non-Z2-quotient constructions from non-abelian groups whose phase conditions linearise.
