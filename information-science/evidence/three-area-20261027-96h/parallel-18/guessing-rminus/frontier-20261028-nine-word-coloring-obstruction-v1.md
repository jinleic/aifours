# A nine-word R-minus FD support that defeats three-group reconstruction

**Status: WRITTEN-checked-in-kernel with a separately implemented exact checker; scientific review pending.** The three-group method used in `frontier-20261028-five-point-k4free-bound-v1.md` cannot be extended verbatim to all nine-word original-graph supports: the explicit support below satisfies every original-neighbour FD, but **no** three-coloring of the ten coordinate vertices makes every pair of support words differ in at least two color classes.

This is a **method obstruction**, not a strict-gain law. Four coordinates are constant on this support, so the conditioned inequality `frontier-20261028-conditioned-proper-subgraph-inequality-v1.md` SHA-256 `c46831b9324e7e8c65009c2a27f3391db7705c370bfb63435a73b0117be3df49` gives `Delta<=0` for every distribution on it. The independent exact uniform-entropy comparison is strictly negative.

## Construction

Use five independent binary triangle-factor coordinates, in order

```text
123   134   239   348   389
```

For a triangle `T` and one of its edges `e`, define a ten-vertex word by putting 1 on the two endpoints of `e` in that triangle's coordinate and zero on all other vertices and factor coordinates. Take the all-zero word and these eight edge words:

```text
123: 12
134: 13,14
239: 23,29
348: 48
389: 38,39
```

Each vertex symbol is its five-bit tuple, viewed in a common alphabet of size 32. In every triangle factor the three bits XOR to zero. Thus each vertex reconstructs its own bit in each incident factor from the other two vertices of that triangle, which are original neighbours; for nonincident factors it outputs zero. This gives a decoder defined on the full alphabet domain, and all nine listed words are fixed. The checker also verifies the FD directly by the neighbour-tuple lookup on every word.

The differences of selected word pairs force all ten edges of the induced five-wheel on `{1,2,3,4,8,9}` to be bichromatic in any three-group reconstruction coloring. Eight forced edges arise from zero versus each selected word; the two missing wheel edges arise from the differences of the selected word pairs in factors `134` and `389`. That wheel has a five-cycle rim and a hub adjacent to the whole rim, so it is not 3-colorable. Consequently no coloring can make every support-word difference meet two color classes. This does not rule out a different proof of a stronger small-support entropy theorem.

## Evidence

Producer `frontier-20261028-nine-word-coloring-obstruction.py` SHA-256 `67adc29e9222a19497dd5dc4a0868138d4cc7bec36bea0113711d7a403c97068`, receipt with all words and 36 difference sets SHA-256 `d47007043b84ee4b6e9ad88af271d7ecf29931235de98f0af2949b5aaa1c5415`. Separately written `frontier-20261028-nine-word-coloring-independent.py` SHA-256 `cbb47096d6746bb805e3783db8a00827c4eb442d3051b5e6775a0642d617dafd`, receipt SHA-256 `16dd7a9100be734ee91e3a43407042a9469bcc68c58c3f99909ded444fe0c98e`, independently checks all 90 neighbour lookups and decoder outputs, all ten forced wheel edges, all 729 wheel colorings, and the exact negative uniform gap. Four intended-reason controls reject a duplicate word, a single-vertex FD conflict, an out-of-alphabet symbol, and removal of a word needed to force a wheel edge. No novelty claim or proof-assistant formalization is made.
