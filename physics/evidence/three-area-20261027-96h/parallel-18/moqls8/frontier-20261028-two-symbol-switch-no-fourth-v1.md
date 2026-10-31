# Every genuinely quantum two-symbol switch of a classical triple is unextendible

**WRITTEN author candidate; no catalogue, solver, source-classification or witness premise. Disjoint review pending.** Start with any three ordinary classical MOLS of order 8, and choose one square Q_0 and two symbols a,b. Replace its a/b basis rays by independent 2×2 unitary bases on connected components of their four-net incidence graph, keeping the other two classical squares fixed. Every such switch that makes Q genuinely nonclassical yields a valid ordinary three-MOQLS(8) with two classical mates, but **cannot have any ordinary fourth QLS mate**.

This excludes an entire two-symbol-switch construction mechanism for a nonclassical four-family. It does not say that all nonclassical triples arise this way, rule out a different four-family, establish an M(8) upper bound, settle A10/A11 or determine novelty. The concrete frozen three-family has a separate direct nine-cell obstruction in `frontier-20261028-three-family-no-fourth-mate-v1.md` SHA256 07d1683525a6c2ec5b2f11f3be314cd3af94d81f0c6cc1383a77828f34b0e833; that finite witness is not a premise here.

## 1. Incidence components and the switch

The rows, columns and the two other classical symbols form a four-net. Let H be the 16 cells where Q_0 has symbol a or b. On every line of the four-net, Q_0 is an ONB: rows/columns by Latinity, and each classical-mate-symbol line because Q_0 is orthogonal to that mate. Thus any net line meets H in exactly two cells, one a and one b. Join those two cells in each of the four line classes. Any two cells share at most one class-line, so the graph is simple, bipartite by Q_0 symbol, and 4-regular on 8+8 vertices.

Each connected component has at least four vertices in each part. Therefore there is either one 16-vertex component or exactly two 8-vertex components; an 8-vertex component is 4-regular on 4+4 and hence K4,4.

For each component C choose one 2×2 unitary U_C acting on span(e_a,e_b), and replace every Q_0=e_a or e_b ray in C by the corresponding column ray of U_C. Every net line's a/b pair lies in one component, so this replacement gives orthogonal paired rays on that line; all other Q_0 rays stay fixed. Consequently Q is a QLS and remains product-orthogonal to each of the two classical mates. This construction covers arbitrary phases in each unitary and does not replace the actual product-ONB conditions by an abstract graph claim.

If the graph has one component, the replacement is just one global output unitary on span(e_a,e_b), so Q is classical. With two components C_1,C_2, Q is classical exactly when `U_2^{-1} U_1` is monomial up to ray phases: the two pairs of rays must be the same orthonormal basis. If the relative unitary is nonmonomial, it has no zero entry in dimension 2, so each ray from one component has nonzero overlap with both rays from the other. Choosing a row meeting C_2 as the first row and applying one global output unitary makes the C_2 pair the coordinate rays e_a,e_b. Because each row meets exactly one component's a/b pair, C_1 occupies four other rows and its eight cells are precisely mixed; the other Q rays are coordinate rays.

## 2. Direct fourth-mate contradiction

Assume the relative 2×2 unitary is nonmonomial and let D be any ordinary QLS orthogonal to Q and to both classical mates. The eight cells of C_1 form K4,4 in the actual four-net. Cells in opposite parts share a net line, so D's rays there are orthogonal: by its row/column ONB or by its product ONB with the relevant equal classical symbol. Within either part the Q rays are collinear, so the Q⊗D product ONB makes D's rays orthogonal. Hence D's eight C_1 rays are pairwise orthogonal.

Every Q ray in C_1 has nonzero overlaps with both Q rays e_a,e_b on the chosen first row. Orthogonality of the corresponding Q⊗D products forces each D ray on C_1 orthogonal to the two distinct first-row D rays at a,b. Thus eight pairwise orthogonal nonzero D rays lie in a subspace of dimension at most six, contradiction. No numerical angle, coordinate sign, phase cancellation assumption, source classification or frozen five-family theorem is used.

Therefore no genuinely nonclassical member produced by this two-symbol component switch can extend the classical pair to a four-MOQLS(8) family. A monomial relative unitary produces only a classical Q and is not a counterexample. The argument does not cover multi-symbol trades or nonclassical triples without this switch representation.

A disjoint reviewer should check graph degree/simplicity and component dichotomy, switch validity on all four actual net line classes, the relative-unitary classicality equivalence, and both sources of D orthogonality before adoption.
