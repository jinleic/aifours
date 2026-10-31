# Isolated A8A supplies a second non-Butson odd-tensor obstruction

**WRITTEN + EXACT-CHECKED AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date`: **Wed Oct 28 23:08:47 PDT 2026**. This is a second explicit infinite family, NOT a universal even-order no-go.

## Claim

Let `A8A` be the exact isolated order8 Hadamard, with `a=(1+2 i sqrt2)/3`, displayed and sourced in `frontier-20261028-isolated-a8a-nonbutson-no-transversal-v1.md` SHA **cec28eca986f9a33bb8d77c196315cfc918a0133067fcb1a948fb60d766f0a18**. For EVERY local source-row permutation pi and EVERY odd positive m, its CRT-aligned order `8m` Fourier product based on `A8A^pi tensor F_m` has NO orthogonal transversal, whether or not the total QLS is maximal. Row/column relabellings and gauges preserve this conclusion; arbitrary source permutations mixing both tensor coordinates are NOT included.

A8A is not Butson-equivalent: its cross-ratio `-a²` is nonroot and persists in the tensor. It is also not monomially equivalent to the previous T8B example: A8A's cross-ratios lie in `Q(i sqrt2)`, while T8B has a nonreal cross-ratio `-d` in the distinct imaginary quadratic field `Q(i sqrt3)`, whose intersection is Q. The new result is therefore not simply a relabeling of that example.

## Proof and finite exact caller

For a local 8-clique Q write `a_r(Q), b_c(Q)` for row/column multiplicities. Across EVERY normalized source order and EVERY local 8-clique, exact calculations below find the SAME invariant as for T8B:

`a_0(Q)+a_1(Q)+2 b_0(Q)+2 = 0 mod4`.                            (1)

CRT decomposes the order8m Fourier-product rays into local A8A-product rays tensor a classical F_m ray labelled by `u+v mod m`. Any putative transversal partitions into m F_m-ray classes. Each class has at most8 orthogonal local rays; since there are8m total, each class is a local8 clique. Across the m classes, the numbers of chosen cells in local rows0 and1, and local column0, are each m. Summing (1) gives `6m=0 mod4`, contradicting odd m. Local coordinate rotation reduces all8! source orders to5040 with coordinate0 fixed, preserving all Gram zeroes and clique incidence.

The primary finite checker `frontier-20261028-a8a-all-row-orders-n24-eligible-v1.cpp` SHA **23fd488b5f8f68afeef212917bdec4b75f1beaacd19635bb2a3c85a9daf2d618** uses Z[zeta8] with common denominator3 and increasing-vertex bitset DFS; result SHA **a49df3e5af96312b5d60b5222d863de44317c1a375b78d7b289b9e2949d4b947**. It checks 5040 orders, 85248 local eight-cliques, maximum18 per order, 0 violations of (1), 4282704 DFS nodes. The independently written `frontier-20261028-a8a-all-row-orders-clique-replay-v1.cpp` SHA **d3eb961f099346d8cab137d2db46cb2964f8490fa7c6e30202e9cfa51e52f834** uses the distinct integral basis `1,i,sqrt2,i sqrt2` and pivoted Bron–Kerbosch; result SHA **69d17a29a7942bb6a415cd8550f931cbaefb167b7c6e4bcc29d2f3f9b4ef0b8e** reports 5040/85248/0, 1597536 nodes. Exact per-order stream comparison `frontier-20261028-a8a-all-row-orders-coverage-v1.py` SHA **8181416191a17c8335b1ae9617f16a2bab86741a0225d190c661640c63168dd8**, result SHA **ebe04a8c03c96f696b37cf19824f90b546124b257cfd9c2a0dcbc73c053b87db**, matches counts for every order and confirms every replay congruence. The two checkers share the source matrix transcription; neither is a formal or external-model proof.

## Scope

The argument applies to this isolated K and its conjugate (conjugate/reflection preserves Fourier-product Gram zeroes); it says nothing about arbitrary even K, arbitrary source-coordinate mixing, or unrestricted QLS10. The A8A matrix transcription, field computations, all-clique completeness and CRT caller require independent full review.
