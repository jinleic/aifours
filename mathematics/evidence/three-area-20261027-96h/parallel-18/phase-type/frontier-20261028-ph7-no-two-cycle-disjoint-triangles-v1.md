# At 8/9 a no-2-cycle PH7 graph needs two vertex-disjoint directed triangles

**NEW ALL-TOPOLOGY WRITTEN APPLICATION; conditional on the separately frozen exact critical triangle-capacity theorem and pending independent review.** MathResearch96h-2. This removes the *linearity* assumption of `frontier-20261028-ph7-linear-triangle-packing-v1.md` when there are no 2-cycles, even if several triangles share edges or have no common hub.

## Statement

If an actual PH representation of the original H at z=8/9 uses at most seven states and its directed graph has NO directed 2-cycle, then that graph must contain two VERTEX-DISJOINT directed 3-cycles. Arbitrary edge counts, overlapping triangles and longer cycles are otherwise allowed. No global PH7 exclusion or order8 claim follows.

## Proof

After the previously supported critical SCC/Perron reduction and positive diagonal similarity, let G be a seven-state irreducible row generator with positive diagonal escape rates u_i. With no directed 2-cycles, the geometric-mean symmetrization has NO off-diagonal entries: `S=diag(-u_i)`. Its nonnegative eigenrates are exactly the diagonal rates.

No two opposite orientations on the same triangle can both occur, since that would create three directed 2-cycles. Therefore, for every unordered triple C, its imbalance is just the product of its unique directed orientation, if present, and0 otherwise:

    w_C=(product_(i in C) u_i) product_(i->j in C) P_ij,
    P_ij=G_ij/u_i.

Independently choose one outgoing successor at each vertex using the row probabilities P_ij. A directed 3-cycle C is present in this random deterministic mapping with probability equal to its product of P entries. Deterministic-map cycles are vertex-disjoint, so the expectation of the sum of their triangle diagonal products is exactly `W=sum_C w_C`.

If the original graph has NO vertex-disjoint pair of directed triangles, every deterministic map has at most one triangle. Hence its weighted sum is at most the largest product of three of the u_i, namely `lambda5 lambda6 lambda7` for the sorted eigenrates of -S. Taking expectations gives

    W<=lambda5 lambda6 lambda7.

But the separately frozen critical capacity theorem `frontier-20261028-ph7-critical-triangle-imbalance-capacity-v1.md`, SHA256 `c2c95deebfaa048072704da11126636d19b166c60a3cc7f41a266927716dc409`, requires `W>lambda5 lambda6 lambda7`. Contradiction. □

Unlike the earlier linear-hypergraph theorem, this argument handles ANY pattern of overlapping triangle triples because it uses exact deterministic-cycle probabilities, not disjoint outgoing-neighbor budgets. It says nothing about graphs with a 2-cycle or about the feasibility of a graph that does contain two disjoint triangles. The cited capacity theorem, its six-rate integer certificate and the PH caller remain separate review dependencies; no numerical, novelty, formal/kernel or historical process-cure claim is made.

END — any critical PH7 graph with no 2-cycle must contain two vertex-disjoint directed triangles.
