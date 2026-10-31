# All rank-13 local-plane subcodes of the triangle code

**Status: WRITTEN classification with exact finite quotient checks; restricted construction only.** This extends `frontier-20261028-rank13-local-parity-obstruction-v1.md` (SHA-256 `91af0e9d55bdd6308d5e366f038f34f79468c6433e489ce00d39015d24563639`) from one subcode to every subcode in the stated rank class. No unrestricted guessing-number or entropy-law upper bound is claimed.

## Statements

Let `C` be the binary 20-dimensional triangle-parity code on the fixed original R-minus cover listed in the predecessor packet. Each vertex receives its three separate triangle-occurrence bits.

1. If a linear subcode `K <= C` projects to dimension at most two at every vertex, then `dim K <= 13`.
2. For every such subcode of dimension exactly 13, the following strict-gain criterion is impossible: select 16 pairwise-compatible affine `K`-cosets with equal weights, with a local parity choice at every vertex for which the parity takes the less frequent value in at most two of the 16 cosets. Each local image of such a `K` has dimension exactly two.

The entropy reason for considering this criterion is explicit: a hypothetical law uniform on 16 such `K`-cosets would have joint entropy 17 and each vertex entropy at most `2+h_2(1/8)`, so its entropy ratio would exceed `20/3`; the exact comparison is `7^5>2^14`. The theorem rules it out only inside this linear-coset family. Fewer or more cosets, unequal weights, smaller-dimensional subcodes, other alphabets, other triangle codes and arbitrary laws remain open.

If a vertex's less frequent parity value is zero, first translate that vertex's alphabet by a fixed symbol that flips the parity. This leaves the difference subgroup `K`, coset compatibility and entropies unchanged, and makes the less frequent value one at every vertex.

## Classification of the linear subcodes

The 20 independent code coordinates are two per triangle. For any vertex `v`, its three component projections are independent on `C`. Since `K` projects to dimension at most two, choose a nonzero local linear form `g_v` that vanishes on `K`: it is the XOR of a nonempty subset of the three triangle-occurrence components. Regard the ten `g_v` as rows in the dual of `C`. Their span has dimension at most `20-dim K`.

For a linear dependence `sum_v lambda_v g_v=0`, inspect one triangle. Its three component forms have exactly the one relation that their sum is zero. Therefore the three coefficients `lambda_v` times the corresponding local-incidence indicators are either all zero or all one. If exactly one or two of the three incidences are selected by their local forms, every selected endpoint has `lambda_v=0`. If all three incidences are selected, their three lambda values must be equal. Call the first type a *partial* triangle and the second a *full* triangle.

Join vertices lying in a full triangle, and mark a vertex forced if a partial triangle selects its incidence. A dependence is freely constant on each connected component of full triangles with no forced vertex, and zero on every other vertex. Each free component has at least three vertices: a vertex with no incident full triangle nevertheless selects at least one incidence and is forced by a partial triangle. With ten vertices there are at most three free components, so the row-dependence dimension is at most three. Hence the ten rows have rank at least seven and `dim K<=13`.

If `dim K=13`, the ten rows have rank exactly seven, span all of `K`'s annihilator in the dual of `C`, and have exactly three free components. These components contain either nine or ten vertices.

* If they contain ten, their sizes are `3,3,4`. A 3-vertex component is one triangle. The four-vertex component consists of two triangles sharing an edge: the original graph is `K4`-free, so four vertices cannot contain three distinct triangles. There are no partial selections at free vertices, so `g_v` contains exactly the full-triangle incidences at `v`. The fixed cover has five such four-triangle configurations.
* If they contain nine, they are three pairwise disjoint triangles. Their nine vertices select only their own triangle. The remaining vertex is forced, and its `g_v` is an arbitrary nonempty subset of its three occurrences. The fixed cover has eight three-triangle packings, giving `8*7=56` representations.

The exact checker below enumerates all five plus 56 cases and verifies in each that the resulting `K` has dimension 13 and each vertex image dimension exactly two. Thus a rank-13 `K` with a one- or zero-dimensional vertex image cannot occur: any choice of nonzero local forms for it would have produced one of these enumerated row spans.

## Excluding the 16-coset target

For each of the 61 representations, the checker enumerates the isolated-vertex difference images in the 17-dimensional quotient `F_2^30/K`. It finds that (i) the zero `g` pattern has only the zero quotient class compatible with `K`, and (ii) among singleton `g` patterns, at most two vertices have any class compatible with `K`. Therefore distinct compatible classes must have distinct `g` patterns.

If 16 distinct ten-bit patterns have at most two ones at each coordinate, their total weight is at most 20. The minimum total weight of 16 distinct patterns is exactly `0+10*1+5*2=20`. Thus the patterns must contain zero, all ten singleton patterns and five disjoint two-bit patterns. Translate the selected zero-pattern class to `K`; the vertex parity counts and graph conflicts are unchanged. At most two singleton vertices remain possible, contradicting the required ten. This proves statement 2 for all rank-13 local-plane subcodes of this fixed triangle code.

## Evidence

`frontier-20261028-rank13-all-local-subcodes.py` SHA-256 `c3c9f470b090bbebcff69cc3c45f99a7c8bb2c1537a8911afcee3c53aba682ee`; receipt `frontier-20261028-rank13-all-local-subcodes-result.json` SHA-256 `2a077705eca7cdbb5ba6dacc42d3c592268b73fa32f264b8a3373b73573c6e4d`. The script checks the original graph's 210 possible `K4`s, finds the five covers and eight packings, verifies all ranks, builds forbidden quotient classes directly from original-graph isolated-vertex images, and checks the zero and singleton targets for all 61 cases. It uses only integer bit operations, not the earlier Z3 status or an external source.

The completeness of the 61-case reduction rests on the written dependence argument above; it has not been formally checked, cross-model reviewed or cleared for novelty. The finite code check is not an unrestricted guessing-number certificate.
