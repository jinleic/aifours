# A distribution-only entropy envelope for every strict-gap law

**Status: WRITTEN with exact six-point examples; conditional on the pinned graph-FD inequality and scientific review.** Let `P` be a positive probability law on a finite set of `m` labeled atoms. Consider every partition of those atoms except the constant and discrete partitions. Order their entropies as `h_(1)<=h_(2)<=...`, counting each distinct partition once. If there are fewer than ten such partitions, or if

\[
\sum_{j=1}^{10}h_{(j)}\ge\frac32 H(P),\tag{18}
\]

then **no** original-neighbour R-minus FD law with joint atom probabilities `P` can have positive balance gap, regardless of coordinate alphabet or atom-to-word assignment.

Indeed, the conditioned inequality `frontier-20261028-conditioned-proper-subgraph-inequality-v1.md` SHA-256 `c46831b9324e7e8c65009c2a27f3391db7705c370bfb63435a73b0117be3df49` requires every strict-gap coordinate to be nonconstant and forbids one coordinate from determining another. Thus its ten singleton level-set partitions are ten **distinct**, nonconstant and nondiscrete partitions. Their entropy sum is at least the left side of (18), while `Delta>0` would require that sum to be strictly less than `(3/2)H(P)`.

The criterion is distribution-only and does not require enumerating graph decoders. Because the sum of the ten smallest entropies is the minimum of finitely many continuous ten-term sums, any vector satisfying (18) **strictly** has an open probability neighborhood also excluded by the criterion.

## Exact six-point examples

The normalized weights `(8,4,2,1,1,1)`, `(10,5,3,2,1,1)` and `(15,7,3,2,1,1)` all satisfy (18) strictly. They are excluded together with some open neighborhoods, including nonuniform laws not necessarily covered by the earlier minimum-atom or skew-coloring gates.

For integer weights `w_i`, total `W`, and a partition `P`, write `F(P)=product_B (sum_{i in B}w_i)^(sum_{i in B}w_i)`. The ten smallest partition entropies are precisely the ten largest `F(P)` values. Let their product be `F_top`, and let `F_atoms=product_i w_i^w_i`. The strict version of (18) is equivalent to

\[
F_{\rm top}^{2}<W^{17W}F_{\rm atoms}^{3}.
\]

Checker `frontier-20261028-sixpoint-entropy-envelope-check.py` SHA-256 `f18ca2e90e859ae9c998bbd2a2685c95f200892b73ce22b394bfd49f03e9cdf4`, receipt SHA-256 `fe5493ae2b85dfa00d369f32ccbcd62c275ebb03a68fe2ba1991edd14f16c2c8`, independently reconstructs all 201 eligible six-atom partitions and checks the three inequalities exactly. Its control `(71,61,38,6,4,1)` does **not** satisfy the envelope test; that is a limitation of this sufficient test, not a strict-gap witness. No global no-gain, numerical guessing-number, novelty or independent scientific-review claim is made.
