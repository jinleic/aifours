# Two q=8 syndrome values at distance at most five cannot yield a gain

**Status: WRITTEN with independently replayed exact support-mask/color census; conditional on the pinned graph-FD inequality; scientific review pending.** For any original-neighbour R-minus FD law in the standard q=8 triangle-factor encoding, if its syndrome support is contained in two values whose Hamming distance is at most **five**, then `Delta<=0`, for arbitrary probabilities. This strengthens `frontier-20261028-close-syndrome-entropy-bound-v1.md` SHA-256 `68de93f8a9a6fd4efd1a54c4568a48e31a9862dfcfa202f799c7b158dc569df7` from distance four to five. Hence any two-syndrome strict-gap q=8 law would need syndrome distance at least six. This is not a proof that such a farther-distance law exists or a global q=8 bound.

At distance six, the same proof excludes every difference-factor set except these **seven**:

```text
{1,2,5,6,8,9}    {1,3,4,6,7,10}   {2,3,4,6,7,10}
{1,3,4,7,8,10}   {2,3,4,7,8,10}   {2,3,5,6,9,10}
{1,3,5,8,9,10}
```

These are only the cases where the particular **universal three-coloring** certificate fails; no positive law, impossibility, or entropy verdict is inferred for them.

## Finite mixed-block test

Let `J` be the differing factor set of two syndrome values. If its triangles do not cover all graph vertices, the pinned syndrome-cover gate `frontier-20261028-syndrome-cover-entropy-gate-v1.md` SHA-256 `d6df004e025f067a14a6cc69e9aef8d9fc78a20a2fc49c4e431328120e32014b` applies. If `J` covers the graph, fix the full tuples of the other factors and normalize the affine syndrome offset. The variable `J`-block has `3|J|` component bits; any difference of two block words has parity syndrome either all-zero or all-one on `J`.

A difference is **nonconfusable** exactly when its set of differing graph vertices induces no isolated vertex. For a given `J`, enumerate every vertex support achievable by a nonzero nonconfusable difference of either allowed syndrome. If one 3-coloring makes all these supports nonmonochromatic, every FD-consistent two-coset block support has the property that any two grouped color tuples determine the whole word; pairwise subadditivity gives `H(block)<=(2/3)sum_i H(block_i)` for any law.

The finite census finds a universal coloring for all 19 covering 4-factor sets, all 90 covering 5-factor sets, and 138 of 145 covering 6-factor sets. No universal 3-coloring exists for the seven listed 6-factor sets, as checked exhaustively; that negative result is about this proof method only. The fixed-parity factors outside `J` individually satisfy the two-thirds inequality conditionally. Processing them first and applying the mixed-block inequality to each last-block fiber gives the full-law conclusion by the same chain-rule/conditioning argument as the distance-four packet.

## Two independent exact enumerations

The producer `frontier-20261028-two-syndrome-mobius-census.py` SHA-256 `7ba7865bbe7d65512e1d6edfa5d1ab797cf26f1ef62a295560cbe03055fa49c9`, receipt SHA-256 `a1be7e3a7dc9b491cbe3395d2c9342c7fd419b086ea3144ec4971c79df31e957`, derives exact attainable vertex-support masks using subset Möbius inversion on factor bit assignments and records the colorings. Separately written `frontier-20261028-two-syndrome-direct-check.py` SHA-256 `8956fd66f45d0291e3659ffdd9d813df572fccc99b21977e5ae91dc22f37477b`, receipt SHA-256 `51102bd81b2cb21ddd58dca01df1aadb54071c947c94622c486da6c9051aeb20`, enumerates **41,037,824** actual component-bit assignments across all 254 covering 4/5/6-factor sets, independently checks every attainable mask and color, and exhausts all 19,683 canonical 3-colorings for the seven no-color cases. A monochrome mutation is rejected. The graph/entropy lifting and imported proper-subgraph inequality remain subject to scientific review; no formal proof or novelty claim is made.
