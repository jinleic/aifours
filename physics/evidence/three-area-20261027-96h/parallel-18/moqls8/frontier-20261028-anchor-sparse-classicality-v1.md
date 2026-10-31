# Classicality from a single uniform-sparse net-line basis

**Status: WRITTEN candidate with independent exact finite certificate; Hcat is an external, unproved source premise.** This strictly weakens the global four-ray assumption in `frontier-20261028-four-ray-classicality-v1.md` (SHA256 f39acce9b5bd88e25fe2ea5bffa809b568e6ccad54516254206cffe80c003606); that earlier immutable packet remains as written.

Call a QLS **uniform-sparse relative to an actual ONB line L** if, when its eight rays on L are used as the coordinate basis, every one of its 64 rays has either one nonzero coordinate of magnitude 1 or four nonzero coordinates each of magnitude 1/2. This requirement concerns ONE chosen line and does not restrict overlaps between other pairs of rays. When Q has three classical mates, every line of the resulting five-net is an actual Q ONB, so L may be any of those five classes.

Let **Hcat** mean that every ordinary order-8 triple of MOLS is paratopic to one of the 39 triples in the pinned local Wanless catalogue snapshots. Under Hcat:

1. If an actual ordinary four-MOQLS(8) has three classical members and the fourth member Q is uniform-sparse relative to even one of its five net lines, then Q is classical.
2. If all four members are uniform-sparse relative to their respective bases on **one common actual grid row**, the entire four-family is classical. Their output bases and phases may be unrelated.

The all-variable prerequisite that at most one member can be nonclassical under the common-row hypothesis is a direct application of §1 of the four-ray packet: its support, disjoint-heavy-column and 16-board product-dimension proof uses only the support property in the one common row frame, not its global overlap assumption. The q1 argument below uses no corresponding property of the three already classical mates. Exact original row/column and all six pair-product ONBs are required. No claim follows for arbitrary nonsparse complex QLS, original A10/A11, numerical M(8), priority, formal or human review.

## 1. Universal forcing graph and the all-heavy alternative

In a five-net, Q is an ONB along rows/columns and each mate-symbol line, because equality of a mate's classical ray forces Q rays there orthogonal. Choose the hypothesized sparse anchor L as the first row, use any other net class for columns, and normalize the other three class labels so their first-row values equal the column label. This merely permutes the Q rays; it does not assume the sparse property relative to a different anchor.

As shown self-contained in §2 of the four-ray packet, every off-anchor cell x has a four-element allowed coordinate set A_x, the complement of its column and three mate labels. The five-net incidence implies that on a net line not through the anchor point t exactly four cells allow t. A heavy cell uses all four of A_x, with weights 1/4. Completeness of a line and orthogonality to that heavy cell force all four cells of that line which allow any t in its support to be heavy.

Join any two off-anchor cells on a common net line if their allowed sets intersect. The graph is connected for **every** five-net, with no catalogue import: every column's seven cells form a clique because their allowed four-sets all avoid the column label and any two four-subsets of seven meet. If components separated columns, their allowed sets in any row would split into two complementary four-sets; the component column sets would equal those complements. Then in one component every symbol of any normalized classical mate's fixed column would belong to only four labels, contradicting the Latin property. The full all-variable proof and quantifiers are in the referenced §2. Heavy/light status is constant on graph components, so a nonclassical Q forces **all 56 off-anchor cells heavy**.

## 2. Two exact obstructions

Suppose all off-anchor rays are heavy and hence their supports are their corresponding allowed sets.

**Single intersection.** If two cells on the same net line have allowed sets meeting in exactly one coordinate, their inner product has exactly one nonzero summand, impossible for orthogonal rays.

**Odd phase cycle.** Suppose distinct off-anchor cells x_1,...,x_(2m+1) form a cycle such that successive cells share a net line and the intersection of their allowed sets is exactly the same pair of axes `{t,u}`. Let the two nonzero coordinate amplitudes of x_i be a_it,a_iu. Orthogonality of successive cells implies

`conj(a_it) a_(i+1,t) + conj(a_iu) a_(i+1,u) = 0`.

Because both amplitudes have equal magnitude, ratios `r_i=a_it/a_iu` have unit modulus, so `conj(r_i) r_(i+1) = -1`, hence `r_(i+1)=-r_i`. An odd cycle gives `r_1=-r_1`, impossible. This is an all-phase complex obstruction; the finite certificate checks actual same-line incidences and the exact two-coordinate intersections, not a graph surrogate replacing the physical ONBs.

## 3. Complete anchor coverage in the pinned local nets

For each of the 39 listed five-net representatives, each of its five line classes, and each of the eight actual anchor lines of that class, the certificate chooses the least-indexed different class as columns, moves the chosen anchor symbol to row 0 and normalizes the other symbol classes. One column-class choice is enough for a fixed anchor: choosing another class only relabels points of the same Q ONB; any fixed choice yields a valid five-net and Q ONBs. Thus the 39×5×8 = **1,560** contexts cover all possible representative images of a sparse anchor under paratopy. In 1,528 contexts there is a single-intersection pair; in the remaining 32 there is an odd phase cycle, in fact a triangle in each case. Every pair or cycle is explicitly recorded with the physical line classes/symbols, cells and allowed sets.

A separate implementation reconstructs all 1,560 oriented OAs directly from the pinned triples, checks every listed witness and all Latin/MOLS conditions, and validates exact coverage. It rejects mutations deleting an anchor, changing a line, duplicating a cycle cell, removing a cycle edge, changing an axis and changing an allowed set. These finite checks do not prove Hcat or the written forcing argument. Under Hcat, every actual triple maps to one of these representatives with its particular sparse anchor in one of the 1,560 covered positions, proving claim 1. Claim 2 follows by the common-row at-most-one argument and then claim 1.

- Producer `frontier-20261028-anchor-sparse-net-obstructions-v1.py`: SHA256 6e46c39749b322809758b16d64171c89d429a4d6bfcdc848bed86508f9f1c8e3; certificate `frontier-20261028-anchor-sparse-net-obstructions-v1.json`: 8197df87c67c2bfada19ce4a13d8d724b4ccfbfe60322456c9c234773cbd9191.
- Independent verifier `frontier-20261028-anchor-sparse-net-obstructions-check-v1.py`: 04f4081da8cd8b2980f63376d2c93054a501456953f526ec93155bd4a1fbcf84; receipt `frontier-20261028-anchor-sparse-net-obstructions-check-receipt-v1.json`: 1983a1eece1b89e5c70d5d35b20c1ea6d85861733c58a2c979a73a3c3ed2fba9.
- The maximal local snapshot is SHA256 95943777fc50075220569c53fca1382bd30e79ccf7c1fc29efbee55a30322a67 and nonmaximal snapshot f8156dc17b3900e5d09796510acc630a3735d471ae08dcc248beebb9612be4b5. Additive page-audit `frontier-20261028-wanless-source-page-audit-v1.json` SHA256 07cc372190f3d2d3100f8d389c4efaf739ca1eed29afad439f8e346e9363ec8b verifies that all 913 nonblank maximal source-reader lines match the screen snapshot in order. The nonmaximal snapshot was also observed to equal the current complete raw-reader output. Neither check proves original HTTP byte identity or the classification.
- Hcat is motivated by [Wanless's exhaustive species catalogue](https://users.monash.edu.au/~iwanless/data/MOLS/) and its [format documentation](https://users.monash.edu.au/~iwanless/data/LSformat.html), with [Egan–Wanless's species convention](https://arxiv.org/html/1406.3681); the external catalogue's completeness and faithful source-to-snapshot correspondence remain named assumptions, not independently reproduced classification results.

## 4. Strictness: a QLS sparse in one anchor but not four-ray

This is a standalone example, not a four-family witness. Label rows `(a,b)` and columns `(c,d)` with a,c∈{0,1}, b,d∈{0,1,2,3}; split C^8 into two four-dimensional blocks. The cell lies in block `a XOR c` and has local index `b XOR d`. In three high-level quadrants use the standard block basis. In quadrant a=c=1 use an order-4 QLS made from a real 4×4 Hadamard basis `(h_0,h_1,h_2,h_3)` and the classical XOR Latin square, except in its 2×2 subsquare b,d∈{0,1} replace h_0,h_1 consistently by

`h'_0=(3 h_0+4 i h_1)/5`,  `h'_1=(4 i h_0+3 h_1)/5`.

The replacement is an orthonormal pair; because the two real Hadamard columns have entries ±1/2, every coordinate of h'_0,h'_1 still has modulus 1/2. Every row and column of the local QLS is an ONB, and every global row/column combines two orthogonal four-bases in different blocks. The global first row is the standard ONB, and all cells have support one or four with uniform nonzero magnitudes relative to it. Yet the cell rays h_0 and h'_0 have squared overlap **9/25**, so the global four-ray property fails.

Exact rational-complex checker `frontier-20261028-anchor-sparse-not-four-ray-check-v1.py` SHA256 81b9e34e19ac49adda0694c3cff916f739e47ee7c5a735e32da431cd7c8822a7; receipt `frontier-20261028-anchor-sparse-not-four-ray-check-receipt-v1.json` be6f549d1767ace05437736c0e301df8e8273106bb7d956f6c21a1e165e44e0d. It checks all row/column Gram entries and every cell's anchor-coordinate weights exactly, reports the 9/25 overlap and rejects a duplicate-ray control. The example demonstrates strictness of the property for standalone QLS only; it does not assert that a nonclassical such square has any mate.

Independent review should reconstruct the common-row two-nonclassical exclusion, the entire connected-graph proof, arbitrary anchor and paratopy coverage, both physical obstructions, the 1,560 certificates and the Hcat/source boundary. No source classification, model-family, human, formal or novelty clearance is claimed.
