# A stronger exact obstruction after one-hot exclusion

**Status: WRITTEN-CHECKED-IN-KERNEL, conditional on the unreviewed two-syndrome theorem; scientific review pending.** The natural three-state induction remains insufficient even after adding the actual one-hot entropy inequality `3 sum_j H(S_j|A)>=5H(S|A)` from `frontier-20261028-three-state-exclusion-entropy-v1.md` SHA-256 `9c5ee203ba255776702e93e90b958663e98a43ebfb3b522b97898381116785e7` for **every** original-coordinate conditioning set `A`.

Use the notation, scaled original primal `h`, required source erratum, graph FDs and four conditional two-syndrome gates from `frontier-20261028-three-syndrome-indicator-obstruction-v1.md` SHA-256 `789cc5d89adab8c4bea659837012a93380466f8dd3dd6d4b7d1143103214b6ac`. Set `k=7/92` and change the auxiliary entropies to

\[
h(A,S)=\min\{h(A)+5k/3,h(V)\},\qquad
h(A,S_j)=\min\{h(A)+k,h(V)\}.
\]

As before, any auxiliary set containing `S` or at least two indicators uses the `h(A,S)` value; one indicator uses `h(A,S_j)`; no auxiliaries uses `h(A)`. The resulting exact 14-variable polymatroid has `Delta=7/92`, `h(S)=35/276`, and all three indicator entropies `7/92`. It satisfies every elemental Shannon inequality, the graph FDs, q=8 singleton caps, state/indicator functional relations, all four conditional gates, and inequality (29) for all 1,024 original-coordinate conditioning sets.

`frontier-20261028-three-syndrome-exclusion-countermodel-check.py` SHA-256 `07ee59a09206f73ea681e27e19d89971809788542bf7a5dd8a2d7574fbd336a6`, receipt SHA-256 `12cf29782755a47f1fa3b9500561b6cfb17325514b7691e019648afe4df90158`, performs 372,736 exact full-joint CMI checks, 14 monotonicity checks, the gates, and every conditional exclusion inequality. The shared original primal has the required pre-source erratum identified in the checker.

This remains an **abstract polymatroid**, not a genuine one-hot law or guessing strategy. Indeed, if actual one-hot indicators have the same strictly positive entropy, their state probabilities must all be `1/3`: binary entropy is strictly increasing on `[0,1/2]`, and any mixture of its two symmetric preimages cannot sum to 1 unless all three are `1/3`. Such a state would have `H(S)=log_2 3>1`, whereas this countermodel has `h(S)=35/276<1`. Thus (29), although it excludes the earlier countermodel, does not alone resolve three-syndrome laws. Additional support-specific, copy/non-Shannon, or structural information remains necessary; no full-copy auxiliary extension, formal proof, scientific adoption or novelty claim is made.
