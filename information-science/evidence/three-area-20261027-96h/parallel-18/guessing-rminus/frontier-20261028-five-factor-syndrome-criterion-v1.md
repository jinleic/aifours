# A five-factor identifiability criterion for arbitrary syndrome counts

**Status: WRITTEN, exact compact Shannon certificate checked, scientific review pending.** For an original-neighbour R-minus FD law on arbitrary finite group triangle factors, let `S` denote the full syndrome vector. If `S` is a function of each single factor syndrome in the five triangles

\[
123,\quad145,\quad167,\quad389,\quad4\,8\,10,\tag{43}
\]

then `Delta<=0`, regardless of the number of possible syndromes, their probabilities or the group orders. Equivalently, for each of these five coordinates, its projection is injective on the support of `S`. In the uniform support case, `|W|<=product_t |G_t|^2`. This is not a theorem for arbitrary syndrome supports or a new unrestricted numerical upper bound.

## Proof

The compact exact dual yields (42) in `frontier-20261028-compact-full-syndrome-inequality-v1-addendum-1.md` SHA-256 `2f7a18d11fde89e9c94bf57ee376967f0f8294b1b6660699d6be2c4cc25eeed6`, with full group-syndrome vector `S`. Its four triangle terms concern `123,145,389,4·8·10`. On each of those triangle tuples the respective factor product is visible, so the hypothesis makes `S` visible and all four terms vanish.

Its six distinct neighbourhood terms are at vertices `2,5,6,7,9,10`. Each such vertex belongs to at least one triangle in (43): respectively `123,145,167,167,389,4·8·10`. In each case its original graph decoder recovers its own block from its neighbours, while the other two components of the incident triangle already lie at neighbours. Thus the neighbours determine that factor syndrome, which by hypothesis determines `S`; every remaining term vanishes. The right side of (42) is zero.

This is the corrected strengthening of `frontier-20261028-local-syndrome-identifiability-v1.md` SHA-256 `17c9bfffd71c9ff4dcdb393ab6e59cf476223217d45b6453125758875c89678a`, which MUST be read after its required pre-source erratum SHA-256 `27fdf3b0759ba6122a8f47e583fba7f2ccc305b7e195d6c499e840a3125ed3d3`. Here the additional triangle `167` explicitly covers vertices 6 and 7. Every claim is conditional on the pinned exact coefficient identity and written group-decoder argument; proof-assistant formalization and novelty are not asserted.
