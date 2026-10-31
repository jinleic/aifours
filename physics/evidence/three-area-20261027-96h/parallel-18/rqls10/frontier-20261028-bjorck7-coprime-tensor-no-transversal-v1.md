# A non-Butson seven-dimensional factor rules out infinitely many even Fourier transversals

**COMPUTER-ASSISTED AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date`: **Wed Oct 28 23:50:39 PDT 2026**. This arose from an actual positive-T search at order14. The result is an infinite restricted-family no-go, not a universal even-order statement.

## Construction and claim

Let `a=(-3+sqrt(-7))/4`, with the positive-imaginary square root, and let `K7_(t,c)=s_(t-c mod7)` for

`s=(1,1,1,a,1,a,a)`.

Both exact implementations below verify all unit norms and Hadamard column Grams (the first also checks row Grams). For every local source-row permutation pi and every positive m coprime to7, the CRT-aligned cyclic Fourier-product QLS of order `n=7m` based on `K7^pi tensor F_m` has NO orthogonal transversal. Thus, in particular, this excludes these non-Butson examples at all even orders `n=14k` with `7` not dividing k. It does not cover arbitrary source-coordinate permutations mixing the two tensor factors.

The entry field Q(sqrt(-7)) is the quadratic subfield of Q(zeta7), so Phi7 is reducible over it: this family is genuinely outside the hypothesis of `frontier-20261028-large-prime-field-fourier-obstruction-v1.md` SHA **3348a6acd5876859722d980c20ec42433c4b7a6e91fa274fa34ba8a4e40fe286**. The number a is not a root of unity because `a+1/a=-3/2` is not a rational algebraic integer. The dephased 2×2 cross-ratio `1/a` persists in the tensor, so no matrix in this family is monomially equivalent to any Butson matrix.

## Local clique and tensor-incidence proof

For every one of the 720 normalized local source orders, the exact all-clique computations find precisely 14 seven-cell orthogonal bases in the local Fourier-product QLS: the seven rows and the seven columns, and no others. Coordinate cyclic rotation covers all7! source orders without changing Gram zeroes or row/column incidence.

For gcd(m,7)=1, CRT converts the `7m` Fourier factor to F7 tensor F_m. The F_m-factor product QLS is classical, with m orthogonal rays. Any hypothesized `7m` transversal splits into m groups by that ray; each has at most seven local7 orthogonal cells, so each has exactly seven and is a local row or column clique.

Let R_i be the number of these groups equal to local row i, C_j the number equal to local column j, and R=sum R_i, C=sum C_j. Since each global local row i occurs exactly m times, `7 R_i+C=m=R+C`, so `7 R_i=R`; hence 7 divides R. Similarly `7 C_j= C` for each j, so 7 divides C. Thus m=R+C is divisible by7, contradicting gcd(m,7)=1. The same counting argument applies to a tensor of this local QLS with any classical Latin QLS of order m whenever 7 does not divide m; only the Fourier-product identification needs CRT.

## Exact evidence and boundary

`frontier-20261028-n14-bjorck7-tensor-search-v2.py` SHA **dc2a337371c9e2d1bf2e1e1a495d0ca52cb9fcee05ddb591ead00c05a6d15f6f**, result SHA **52489065df89a55ecae7341630337cbef970c9b8f428f764b3930a034099e0db**, uses exact Z[zeta7] with the quadratic Gauss sum for sqrt(-7), and an increasing-vertex clique DFS: 720 orders, 10080 total 7-cliques, 14 per order, all rows or columns. The independently implemented `frontier-20261028-bjorck7-real-cubic-clique-replay-v1.cpp` SHA **b04574ea0680cba04ec579ba08af46467ab69c288fefb0840aa8428a50432e61**, result SHA **8dc51325952e96fa4b5bdccae09c9fff58ec9ff0ed1383e9a97e118eff979c3b**, uses the distinct basis `Q(z,g)` with `z³+z²-2z-1=0`, `g²=-7`, `14 zeta7=7z+g(6+z-2z²)`, plus pivoted Bron–Kerbosch; it obtains 5040 row and 5040 column cliques, zero other. `frontier-20261028-bjorck7-order-clique-coverage-v1.py` SHA **a55015a2f1d82507f30311642ed051c189810e0b0dd4f320e1dcc0e35e208b51**, result SHA **bf635d05688f4c9d805d35fa6e4b413811ec75dbc8718c1d5848ee490455131f**, confirms counts and types separately for all720 orders.

The n=14 tensor QLS in particular has 98 distinct rays, not 196: the local7 rays are distinct by the non-root argument, while the F2 factor is classical. This result does not construct an even-order transversal or settle unrestricted QLS10. The cyclotomic embeddings, local clique coverage and tensor caller require independent full review.
