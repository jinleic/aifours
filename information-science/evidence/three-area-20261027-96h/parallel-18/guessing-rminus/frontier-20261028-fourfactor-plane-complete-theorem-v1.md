# Every four-varying-factor syndrome plane has nonpositive gap

**Status: WRITTEN with exact independently checked certificates for every case; scientific review pending.** In the q=8 binary ten-triangle-factor encoding of the original R-minus graph, let `X` be any original-neighbour FD law whose ten-bit syndrome support is contained in an affine two-dimensional binary plane, and suppose exactly four factor syndromes are nonconstant on that plane. Then

\[
\boxed{\quad H(X_V)\le\frac23\sum_{v=1}^{10}H(X_v).\quad}\tag{61}
\]

Probabilities and correlations are arbitrary, and the support may contain any one, two, three, or all four points of the plane. In particular every such FD support has at most `2^20` words. This completes all `2,730` such direction planes; it is **not** a theorem for planes with five or more varying factors, other syndrome supports, other alphabets, or the unrestricted guessing number.

## Exhaustive case split

1. **Noncover (2,483 planes).** The varying-factor triangles miss a vertex. The syndrome-cover gate `frontier-20261028-syndrome-cover-entropy-gate-v1.md` SHA-256 `d6df004e025f067a14a6cc69e9aef8d9fc78a20a2fc49c4e431328120e32014b`, which imports the pinned nine-active proper-subgraph inequality, gives (61).
2. **Universal three-color reconstruction (206 planes).** `frontier-20261028-fourfactor-plane-color-theorem-v1.md` SHA-256 `09cb78a5bcd1d811f45d087dad567a49ce4f9f9ca898a0fcde3ef96efa0bb4ca`.
3. **Visibility-family Shannon certificates (13 planes).** `frontier-20261028-fourfactor-visibility-family-theorem-v1.md` SHA-256 `ad7ee5d82f7a2ca20a21bc35f950bf1038fe660258dcbe41619bb67834cc410c`.
4. **The last 28 planes (seven four-element orbits).** New exact certificates below.

The three-way cover split is the exact census `frontier-20261028-three-syndrome-cover-census-result.json` SHA-256 `62a9b65a63d7cc72a966754f7c358c3a1a5018fd55da1a416a04df922c579303`; the remaining 28 and their orbits are `frontier-20261028-fourfactor-remaining-orbit-check-result.json` SHA-256 `69acd9041ea9d698b84bf0a75583df6b73ff006cbfb87764cae16f411e416b6e`.

## Certificates for the final seven orbits

Condition on the six fixed-syndrome factor tuples. Each fiber's selected four-factor vertex blocks `Y_v` satisfy the original graph FDs. Let `S` be the selected full syndrome vector. For a vertex `v`, if the parities of the selected factors incident to `v` are injective on the plane, then `H(S|Y_{N(v)})=0`: the graph FD recovers `Y_v`, and each incident triangle's other two components lie at neighbours. For every `v`, `H(Y_v|Y_{L_J(v)},S)=0`, where `L_J(v)` collects the other vertices of the selected triangles through `v`, since each component is fixed by its triangle parity. Finally `H(S|Y_V)=0`.

`frontier-20261028-fourfactor-seven-residual-dual-v1.json` SHA-256 `f70245bd16654d19177a771ea897f55377803257d929b9c63d1c05b95e5816c5` gives, for one representative of each of the seven orbits, an exact rational identity expressing the mixed-block `Delta` as a nonpositive combination of elemental CMIs (121 to 519 per case) plus only the above vanishing FD equalities. The used visibility vertices are respectively `{1,4}`, `{4}`, `{3,9}`, `{7}`, `{7}`, `{7}`, `{3,9}`, each satisfying the injectivity premise. No syndrome entropy cap, one-hot inequality, conditional factor gate, two-syndrome theorem, or floating LP optimum is used.

The separately written checker `frontier-20261028-fourfactor-seven-residual-dual-check.py` SHA-256 `b0bdf17b4c3a51edd6a09d810809ff2bcde9ca19358a397268e233a6fa3eafca`, receipt SHA-256 `7d998bdce90c6dbf46d1cd07979baeffd929e4d1d77d1547df33050eb5ef844b`, rebuilds every row from the graph and plane data, re-verifies each visibility premise from projection injectivity and triangle edges, each local-set inclusion and every CMI sign, and checks cancellation of all 2,047 entropy coefficients with exact `Fraction` arithmetic. It also checks that the factor-automorphism images of the seven representatives cover exactly the 28 residual planes, and rejects a changed target, a flipped CMI sign, and a deliberately invisible plane.

Graph automorphisms preserving the triangle-factor list transport laws, supports and FDs between orbit members, so each certificate covers its orbit. Fixed-syndrome factors tensorize exactly as in the noncover gate: process them first by their fixed parity inequality, then apply the mixed-block bound on each conditional fiber, and use the chain rule. This is written mathematics with exact finite certificates, not proof-assistant formalization, independent scientific adoption or novelty clearance.
