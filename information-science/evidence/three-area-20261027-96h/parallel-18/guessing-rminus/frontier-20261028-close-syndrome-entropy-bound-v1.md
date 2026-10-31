# Two q=8 syndrome classes at distance at most four cannot yield a gain

**Status: WRITTEN with independently replayed exact mixed-space color certificates; conditional on the pinned graph-FD inequality; scientific review pending.** In the standard q=8 triangle-factor encoding, let an arbitrary original-neighbour R-minus FD law have syndrome support contained in `{s,t}`. If the Hamming distance `|s xor t|<=4`, then

\[
H(X_V)\le\frac23\sum_i H(X_i).
\]

This is an entropy-law statement for **all** probabilities and all FD-consistent supports in those classes. Thus a strict-gap q=8 law using at most two syndrome values would need those values at distance **at least five**. It does not rule out two farther-apart classes, larger syndrome support, or unrestricted guessing-number gain.

## Exact mixed-space color fact

For each of the 19 four-factor vertex covers `J`, form its 12-bit mixed space, with the eight one-bit and two two-bit vertex symbols. For each nonzero four-bit syndrome difference `d`, there is a three-coloring of the ten graph vertices such that **every nonconfusable nonzero word difference** with syndrome `0` or `d` meets at least two colors. The independently checked receipt covers all `19*15=285` cases and checks **140,368** allowed differences directly.

Consequently any FD-consistent support in two affine syndrome cosets of that mixed space has three grouped coordinate tuples any two of which determine the word. Summing the three pairwise subadditivity inequalities gives the two-thirds entropy bound for any law on that support. Translation by a fixed mixed word handles any affine offset and leaves all word differences unchanged.

## Lifting to all ten factors

Let `J` be the set of factor coordinates where `s,t` differ. If `|J|<=3`, or `|J|=4` but its triangles fail to cover all vertices, the syndrome-cover entropy gate `frontier-20261028-syndrome-cover-entropy-gate-v1.md` SHA-256 `d6df004e025f067a14a6cc69e9aef8d9fc78a20a2fc49c4e431328120e32014b` proves the result. The one-class case is covered by the triangle-product theorem.

If `|J|=4` and `J` is a vertex cover, process all six fixed-syndrome factors first and condition on their **full factor tuples**. In each positive-probability fiber the four-factor block still satisfies the original graph FDs, and its syndrome lies in two affine cosets. The exact mixed-space color fact gives the two-thirds bound for that block. The six fixed-parity factors individually satisfy the same ratio even with arbitrary past conditioning. Summing, then dropping from full-past conditioning to each vertex's own past and applying chain rules, gives the full-law bound. No independence, uniformity or cardinality assumption is used.

## Exact evidence

`frontier-20261028-mincover-outsider-color-census.py` SHA-256 `0e7b9f0bd6353a72ae7f3d09991f781d179158ca0ae1112aaaf2c96f53dff27c`, receipt SHA-256 `7c25535f2c52ffdc667f3c7b231c201fef4b1279e1da826299283230dbbb44c2`, supplies 285 vertex colorings. `frontier-20261028-mincover-two-coset-color-check.py` SHA-256 `48f06d2656e351a86bd7d44001f1e44f818e90a0ea359ee3d17cba088bb5930f`, receipt SHA-256 `ba1df830839ab10f91ec8a7e4f470a93363b90267e13a9cd5fd8c5f7a34a7f18`, independently rebuilds the 12-bit difference spaces and verifies all 140,368 nonconfusable differences in the two-coset cases; two intended mutations fail. The related direct support/FD/color replay receipt is SHA-256 `66490309f68757f7911eb278ebae09945ca5778c5af45d9a3aa09ce951c2dede`. The entropy lifting is written mathematics and the conditioned graph-FD certificate and full theorem await scientific review; no novelty or proof-assistant claim is made.
