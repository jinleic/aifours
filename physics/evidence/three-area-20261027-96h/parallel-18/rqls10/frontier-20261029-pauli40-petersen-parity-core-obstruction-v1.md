# The two-qubit 40-ray 30–15 parity cores are Petersen line graphs

**WRITTEN + EXACT-CHECKED AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date`: **Thu Oct 29 00:47:10 PDT 2026**. This rules out one concrete family of 4D parity cores in the unresolved 4+6 branch, NOT all 4D parity proofs or all 1RQLS10s.

## Claim

Take the literal 40 two-qubit rays in [Waegell–Aravind Table4](https://arxiv.org/html/1109.1299v2#S3.T4). Their vectors are transcribed as exact Gaussian integers in `frontier-20261029-pauli40-source-vectors-v1.json` SHA **a4f6cfedaa499442551a664599a8fbd9c8529388abc9c040f39ec57d9ddd5d10**. Among ALL their orthogonal 4-ray bases, there are exactly64 subsets of 15 bases in which every ray occurs 0 or2 times. For EVERY one of those 64 configurations, the graph whose vertices are its 15 bases and whose edges join bases sharing a ray is the **line graph of the Petersen graph**, and hence is not 3-colorable.

Now suppose a maximal 1RQLS10 has a balanced-Z2 resolution quotient and a 4+6 orthogonal split of its selected 75-ray parity core, as in `frontier-20261029-parity-core-sector-rank-obstruction-v1.md` SHA **bd49731bf18dccfb75b08cd6e368fce2a20d5773d3fa59edf7e7e29726ef9703**. If the 30 rays in its 4D sector were contained in a unitary image of the above 40-ray set, its 15 sector bases would be one of the 64 configurations. But the selected contexts are five rows, five columns and five transversals; contexts within each family are disjoint, so their shared-ray graph has a proper 3-coloring. This contradicts the Petersen obstruction. The 6D sector and the other25 QLS cells can be arbitrary; they are not used by this argument.

## Exact census and independent replay

`frontier-20261029-pauli40-parity-core-census-v2.py` SHA **a73be182efbcea108f3213e193aaebe4a12f171d03156b678206649d1ac08f70**, result SHA **87d629d223054158573d0cd37cce418338bea4f5106d2aed2231346b06e298b9**, checks all780 projective-distinctness pairs, regenerates all **40** orthogonal 4-bases by Gaussian-integer inner products, and exhausts all 15-basis subsets with 0/2 ray incidence by a direct finite DFS (13881 nodes). It finds64 and checks none is 3-colorable.

An independently written basis generator plus SMT parity-set replay `frontier-20261029-pauli40-parity-core-replay-v1.py` SHA **6293a87f2150934e6958df39d201dfaf7323c190fbf9f43559d3a00430b6c166**, result SHA **309b90afc0f50952119e1e279fb04e04553ee882e803a22b98671f6bab26873a**, obtains the same40 bases and exact same64 subsets; its SMT exhaustion is corroboration, not a formal proof log. `frontier-20261029-pauli40-3color-independent-v1.py` SHA **ffa821ff73ac9fdd8c12b697515642630728605aae9a90f32d6f2ad3b1608a08**, result SHA **d40e4fa46816e51bfab89cfdbd32702562f458ffdcb976eacb94f78f652ea56c**, independently exhausts all vertex-0-containing independent sets and tests whether their complement is bipartite: none of the64 graphs is 3-colorable.

The structural audit `frontier-20261029-pauli40-petersen-root-v1.py` SHA **215ee39b630b4b5c78996462ad478bcbab22a91e9985edaa37e713cbe000203f**, result SHA **bee043beb06a23cbf2b2cee7c05839fd40b04880ecdfe6962eba3df6b647267a**, finds the ten context-graph triangles, verifies each context lies in exactly two, reconstructs the 10-vertex cubic root graph, and supplies an explicit isomorphism to Petersen for EACH of the64 cases. It checks the full context adjacency equals intersection of root edges, i.e. the line-graph assertion.

## Why Petersen's line graph is not 3-colorable

A 3-coloring of the line graph is a 3-edge-coloring of Petersen. Petersen is cubic, so each color is a perfect matching; the complement of one color is a disjoint union of even cycles. Petersen has 10 vertices and girth5, so this complement would have to be one Hamiltonian 10-cycle.

Write Petersen as an outer 5-cycle, an inner 5-cycle with step2, and five matching spokes. A Hamiltonian cycle uses an even number of spokes. With two spokes, it traverses each 5-cycle as a spanning path, so the two spoke indices must be adjacent in BOTH the step1 and step2 cycles, impossible. With four spokes, the complementary perfect matching contains the unique remaining spoke; after relabeling that spoke to index0, the matching on the outer cycle is (1,2),(3,4), and on the inner cycle is (2,4),(1,3). Its complement is two 5-cycles, not a Hamiltonian cycle. Zero spokes also gives two 5-cycles. Hence Petersen is not Hamiltonian and not 3-edge-colorable.

## Boundary

The source ray transcription, full parity-set enumeration, 64 graph isomorphisms and translation to the 75-ray QLS core require independent review. The published set is only one 40-ray subsystem; other two-qubit 30–15 proofs or arbitrary 4D rays may have different context graphs. No universal even Fourier-product or unrestricted 1RQLS10 claim follows.
