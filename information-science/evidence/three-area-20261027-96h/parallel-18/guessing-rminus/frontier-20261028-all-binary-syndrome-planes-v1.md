# Every binary syndrome plane has a confusability transversal

**Status: WRITTEN with independent exact finite witness verification.** This is a substantially stronger restriction on the explicit `q=8` triangle-parity construction, not a global upper bound. An unrestricted nonlinear support, a support using an affine syndrome space of dimension at least three, and a nonuniform entropy-ratio gain remain open. No formal proof, cross-model review or novelty clearance was performed.

## Statement

Take the specific ten triangles and original R-minus graph in `frontier-20261028-triangle-two-coset-obstruction-v1.md` (SHA-256 `da26dfb13dfe38bdcc5c07a3d33a90a5b7adba77eebbcb6d36c2141ce4e032b7`). Work over `F_2`; let `pi:F_2^30 -> F_2^10` give the ten triangle parities and let `C=ker(pi)`, so `|C|=2^20`. Every vertex has alphabet `F_2^3`, hence `q=8`.

For **every** two-dimensional linear subspace `H` of the syndrome space, there exists a linear two-dimensional subgroup `D` of the original word space such that `pi|D:D -> H` is bijective and every nonzero element of `D` is a forbidden difference: it is nonzero at some vertex and zero at all that vertex's original neighbours. Consequently every valid functional-dependence support in **any affine syndrome plane** `pi^{-1}(a+H)` has at most `2^20` words. The same bound holds for affine syndrome subspaces of dimension zero or one by extending them to a plane. In particular, a valid support contained in any three cosets of `C` has at most `2^20` words. A support of more than `2^20` must use at least four cosets whose syndromes span affine dimension at least three.

The statement does not cover four arbitrary cosets of affine dimension three, let alone all `2^10` cosets.

## Proof from the finite certificate

For any `H` and `D` in the statement, fix a word whose syndrome is `a`. The affine slice is the disjoint union of its `|C|` translates of `D`, because `C` is the syndrome kernel and `pi` maps `D` bijectively to `H`. Every translate of `D` is a clique in the original confusability graph: differences of distinct words are nonzero elements of `D`, hence forbidden. A functional-dependence support takes at most one word from each clique, proving the `|C|` bound.

It remains to exhibit `D` for all 174,251 planes. Number the ten triangle occurrences as in the predecessor packet. For a vertex `v`, let `star(v)` be its three incident triangle coordinates. If the projection of `H` to those coordinates has rank two, construct `d_v(z)` linearly for each syndrome `z` as follows: put `z[t]` into `v`'s triangle coordinate for every `t` containing `v`; for each triangle not containing `v`, put `z[t]` at one of its vertices nonadjacent to `v`; set every other coordinate to zero. Such a non-neighbour exists because the graph is `K4`-free. Then `pi(d_v(z))=z`, and every nonzero `z` in `H` has nonzero restriction to `star(v)`, making `d_v(z)` nonzero at `v` and zero at every neighbour of `v`. Therefore `D=d_v(H)` is the desired clique transversal.

Exactly **174,077** planes have such a vertex. For the remaining **174**, the certificate gives syndrome generators `a,b` and two 20-bit coefficient vectors `c_a,c_b`. In triangle `t`, coefficient bits `2t` and `2t+1` specify the first two triangle coordinates; the third is their XOR with the triangle's syndrome bit. Decode `d_a` from `(a,c_a)` and `d_b` from `(b,c_b)`. The independent checker tests directly that the three 30-bit words `d_a`, `d_b`, and `d_a XOR d_b` have the three prescribed nonzero syndromes and each is an original-neighbour forbidden difference. Thus `D=span(d_a,d_b)` works for every exceptional plane too.

The number of two-dimensional binary subspaces is `(2^10-1)(2^10-2)/6=174251`. The checker enumerates each plane once, recomputes all common-vertex cases from scratch and decodes the 174 exceptional cases. It checks all **522,753** nonzero witness words for their exact syndrome and original-neighbour isolation, and checks all 210 four-vertex subsets for the `K4` premise. Only integer and bit operations are used.

## Pinned evidence

* Producer `frontier-20261028-all-syndrome-planes-certificate.py`, SHA-256 `cbfc15ff57fcf5180d4172801e103bbef32ec38e8f9fd7caa5d5be1306587bfe`; it uses its pinned earlier quotient-search implementation to find exceptional witnesses. Certificate and exceptional vectors: `frontier-20261028-all-syndrome-planes-certificate-result.json`, SHA-256 `e607cd0ff871cf744193c50cd70476759a465a5b45f020706afc5cabe4f261af`.
* Independent checker `frontier-20261028-all-syndrome-planes-independent-check.py`, SHA-256 `05f03ac3459c74497d29ab1d912c93eb372c03d2ff497e9f8fab24740443ef86`. It imports no producer module and independently reconstructs graph, coordinate positions, syndromes and full 30-bit differences.
* Checker receipt `frontier-20261028-all-syndrome-planes-independent-check-result.json`, SHA-256 `a8593b74e6719e6a95a55d3145b2ebe6b89e173662d053830c6dbabf2af86f4b`, records the graph, plane and witness counts above.

These checks certify the stated finite construction and its written consequence, subject to the usual implementation and human-review limits. They do not certify an improved original guessing-number bound.
