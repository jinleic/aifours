# Any three-point FD law obeys the entropy-balance bound

**Status: WRITTEN, elementary partition/entropy proof; review and novelty clearance pending.** For a finite joint law satisfying the FDs of any finite loop-free directed dependency graph, if its joint support contains at most three outcomes, then

\[
H(X_V)\le \frac23\sum_{v\in V}H(X_v).
\]

Thus any original-neighbour R-minus FD law with strict positive entropy-balance gap must use at least four joint support words. This is a support restriction only; it is not a no-gain theorem or a bound on the size of a guessing alphabet.

## Proof

Let `Omega` be the joint support. If `|Omega|<=1` the result is immediate. Each coordinate is a function on `Omega` and induces a partition of `Omega` into its level sets. If some coordinate is injective on `Omega`, that vertex has entropy `H(X_V)`. Its FD and entropy subadditivity imply that its neighbours' singleton entropies sum to at least `H(X_V)`; because there is no self-loop, the total singleton sum is at least `2H(X_V)`. This settles support size two and any size-three case having an injective coordinate.

For the remaining three-point case, every nonconstant coordinate induces a `1+2` partition. There are exactly three possible types, according to which support point is isolated, and two coordinates of the same type are deterministic bijections of one another. Any two distinct types jointly distinguish all three support points and therefore determine the whole joint vector, under any positive weights on the three support points.

* If all three types occur, take one representative of each. Each pair determines the joint vector. Adding the three pairwise entropy-subadditivity inequalities yields singleton sum at least `(3/2)H(X_V)`.
* If exactly two types occur and each appears at least twice, their representatives determine the joint vector, so all singleton entropies sum to at least twice the joint entropy. If one type has just one vertex and the other at least two, the unique vertex's neighbours contain only copies of the other type and constants; its FD makes its value a function of the other type. Consequently the other type alone has the full joint entropy, and its two copies already contribute twice that entropy. If both types appear once, the same argument in both directions shows each has full joint entropy.
* Exactly one nonconstant type cannot occur in this remaining case: then the whole joint vector would have only that two-block partition, not all three distinct joint outcomes.

All cases prove the bound. The same two-type argument also applies to the finite-group coset theorem in `frontier-20261028-semiprime-coset-generalization-v1.md` (SHA-256 `221469b9413c806023683b933bf8206e2f76c9ca96b2cf756371a6030dc899ad`), but no group representation is assumed here. No formal proof, cross-model review or general guessing-number conclusion is claimed.
