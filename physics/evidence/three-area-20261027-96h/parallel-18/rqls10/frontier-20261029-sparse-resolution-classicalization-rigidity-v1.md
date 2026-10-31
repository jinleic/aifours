# Two-sparse resolved QLSs: an exact classical trade criterion

**WRITTEN + EXACT-CHECKED AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date`: **Thu Oct 29 00:29:13 PDT 2026**. The general theorem is written mathematics; the Weisner application uses a finite exact census. This is not a no-go for arbitrary 1RQLS10.

## Theorem

Fix t>=1 mutually orthogonal Latin resolution squares L_1,...,L_t of order n. There exists a NONCLASSICAL t-resolvable QLS of order n, using exactly these resolution labels and globally support≤2 in some common ONB, **if and only if** there is a classical Latin square A orthogonal to every L_i with at least one disconnected two-color context-pair graph.

The graph for A-colors a,b has their 2n cells as vertices; in every row, column, and L_i-label class join the two cells of these colors. Nonclassical means more than n distinct rays, modulo global unitary and cell phases.

## Proof: classicalization plus analytic path

Choose a basis in which all rays are 2-sparse. In every ONB context, a support-two ray on `{i,j}` must be accompanied by its unique orthogonal-complement ray in that plane: a 2-sparse vector with just one overlapping coordinate cannot be orthogonal, and an ONB must span the plane. All other context vectors have supports disjoint from `{i,j}`. Consequently every context decomposes into singleton coordinate rays and orthogonal ray pairs on pairwise-disjoint coordinate planes.

For each distinct unordered orthogonal ray pair in each coordinate plane, independently choose an orientation and replace it by `(e_i,e_j)`; keep support-one rays fixed. The SAME ray pair is replaced identically wherever it occurs. Every one of the row, column and resolution bases remains an ONB because its support planes were disjoint. The resulting classical array A is Latin and is orthogonal to each L_i.

For each original ray pair choose a unitary path `U_pair(s)=exp(i s H_pair)`, 0<=s<=1, from the identity on its coordinate plane to an oriented unitary representing that ray pair; any finite-dimensional unitary has a Hermitian logarithm. Replace the relevant cells by the corresponding columns of U_pair(s), keeping singleton rays fixed. This gives a real-analytic path of exact t-resolved QLSs from A to the original array, with all vectors still 2-sparse. If the original array is nonclassical, two cells having the same A-color have different final rays. A suitable 2×2 projective minor of those two analytic vector paths is nonzero at s=1 and thus is not identically zero; it is nonzero for arbitrarily small positive s.

If ALL two-color graphs of A are connected, the standard tangent argument in `frontier-20261028-classical-rigidity-and-search-v1.md` SHA **3dc1eea8fdb47c04c39dea1d0a8a85122680db29b3d8c3fdea6c7ce05f712f24** (the same proof works with t resolutions) makes A locally rigid modulo common unitary and cell phases. The preceding analytic path has nonclassical arrays arbitrarily close to A, contradiction. Thus some pair graph must be disconnected.

Conversely, from a disconnected pair graph choose a proper connected component and apply a nontrivial 2×2 unitary on the two color rays only within that component. Each context contains either both paired colors in that same component or neither; all bases remain exact. Every connected component contains both colors, so both old color rays remain elsewhere. A generic rotation adds two new rays, producing a nonclassical globally 2-sparse t-RQLS. This proves the equivalence.

## Weisner L: all globally two-sparse solutions are classical

For L equal to the second coordinate of [Weisner's Figure 1](https://doi.org/10.4153/CMB-1963-009-0), `frontier-20261029-weisner-all-mates-trade-census-v1.py` SHA **94a623ae4fe2fd6eb70c41f2cb639480ca1eba950b6dd153727b872b6bc73d60**, result SHA **995796c616d4b48aec948f638234bdd2ac764267b66429a7321edd6de5bd4fb9**, enumerates all728 L-transversals and 102213 cell-disjoint pairs. It finds72 disconnected pairs; for EACH it emits a complete exact-cover proof tree showing that pair cannot extend to ten disjoint L-transversals, so it cannot be two colors of a classical mate.

Independently `frontier-20261029-weisner-mates-independent-replay-v1.py` SHA **3dc426dc8a1cacf46f18a9359eeb0eaa883ef252622f1ebdc771dc28bc5dea74**, result SHA **9d9b301d6b2c7896f30e21b52f0f9f4c899bfb52623eb5de6c3eccb358d093c6**, retranscribes L, enumerates via dynamic MRV and checks pair connectivity via 20-vertex disjoint-set union. It matches all728 transversal keys and all72 literal disconnected-pair components, then replays every branch of all72 completion trees, **2204 nodes**, with no possible extension.

Therefore EVERY classical mate A of this literal Weisner L has all pair graphs connected. By the general theorem, EVERY globally 2-sparse 1RQLS10 with this resolution L has exactly **10 rays**. In particular no 100-ray solution for this L can be globally 2-sparse. This strengthens the earlier any-L <=40 bound, only for this fixed L; it does not assert local rigidity around nonclassical arrays with support≥3 or about other resolution squares.

The analytic classicalization path, pair-graph rigidity import, original published table, all-transversal completeness and exact-cover checker require independent review. This is not formal verification or a novelty finding.
