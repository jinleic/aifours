# The nine-word example is minimal within the single-factor triangle template

**Status: WRITTEN, conditional on the small `K4`-free coloring lemma in the pinned five-point packet; review pending.** The nine-word construction in `frontier-20261028-nine-word-coloring-obstruction-v1.md` SHA-256 `532ff9e58f335e40f84c8301c8d5da5c41fd8ad2c2572a3c8c336fee35acc001` is optimal within this specific template: an all-zero word plus single-triangle-factor edge words. With at most seven such nonzero words, a three-group reconstruction coloring always exists; eight suffice by the pinned construction. This is **not** a lower bound for arbitrary FD supports or arbitrary triangle-code words.

## Proof

Take any finite loop-free `K4`-free graph, choose any collection of its triangle factors, and for each selected nonzero word activate a single edge in one factor. A difference between two words in distinct factors has vertex support equal to the union of their two selected edges. If the two selected words use the same factor, their difference is the third edge of that triangle. Thus a proper three-coloring of the graph `F` formed by all selected edges plus every third edge forced by a pair from one factor makes every support-word difference meet at least two colors.

Let `r` be the number of selected nonzero words. A factor with two selected edge words contributes at most three edges to `F`; one with one contributes at most one, and one with all three contributes at most three. Therefore

\[
|E(F)|\le r+\lfloor r/2\rfloor.
\]

For `r<=6`, this is at most nine, and the coloring lemma in `frontier-20261028-five-point-k4free-bound-v1.md` SHA-256 `7f2103f8f47ea57830836a5e7e8887577fef8876b1af8b2ca7f51075ae3b7ca0` makes `F` 3-colorable. For `r=7`, non-3-colorability would force exactly ten distinct edges and `F=W5`. Equality in the edge count would require three distinct triangle factors with two selected words each, plus one single edge, with all ten contributed edges distinct. The wheel would then contain three pairwise edge-disjoint triangles. But its five triangles correspond to the five rim edges, and two wheel triangles sharing adjacent rim edges share a spoke; choosing edge-disjoint wheel triangles is an independent-set selection in a five-cycle, of maximum size two. Contradiction.

The pinned explicit eight-word selection produces all ten edges of a five-wheel and therefore has no three-group coloring. Its original-neighbour FD and full-domain decoders are checked in the pinned independent receipt `16dd7a9100be734ee91e3a43407042a9469bcc68c58c3f99909ded444fe0c98e`. This result leaves arbitrary six-, seven- and eight-word FD supports entirely open and makes no strict-gain, global guessing-number or novelty claim.
