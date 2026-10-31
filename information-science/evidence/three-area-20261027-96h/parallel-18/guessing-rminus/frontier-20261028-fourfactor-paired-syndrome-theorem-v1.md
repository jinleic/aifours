# A non-colorable four-factor syndrome plane has nonpositive gap

**Status: WRITTEN with a separately checked exact 527-CMI certificate; scientific review pending.** In the q=8 binary triangle-factor R-minus encoding, suppose that, after fixed independent parity translations, the only varying syndrome factors are

\[
S_3=S_4=A,\qquad S_7=S_{10}=B,
\]

with every other factor syndrome constant. The joint law of binary `A,B` is **arbitrary**, including all four combinations. Then every original-neighbour FD law satisfies

\[
\boxed{\quad H(X_V)\le\frac23\sum_v H(X_v).\quad}\tag{60}
\]

A uniform FD support therefore has at most `2^20` words. This covers the whole two-dimensional syndrome plane on factors `{3,4,7,10}`, not just a three-point subset. Its universal fractional reconstruction-cover optimum is exactly `10/3` according to the pinned 41-plane obstruction, so this new Shannon/FD argument goes beyond that universal reconstruction method. The theorem is not a general q8 or unrestricted guessing-number bound.

## Mixed-block proof

Condition on the full component tuples of the six fixed-syndrome factors. In each positive-probability fiber, the four selected-factor vertex blocks `Y_v` retain the original graph FDs; vertex alphabets are eight binary and two quaternary. Let the auxiliary `S=(A,B)` be the two-bit syndrome pair, a deterministic function of all selected blocks. Each component of `Y_v` is recovered from the other two components of its triangle given `S`, so `H(Y_v|Y_{L_J(v)},S)=0` for the selected-factor local neighbourhood `L_J(v)`.

The original-neighbour tuples of vertices 6 and 7 determine both `A` and `B`: those vertices lie in selected factors of both classes, and their blocks are recovered by the graph FD. No assertion that other neighbourhoods or a single triangle determine the full pair is needed.

The exact rational identity `frontier-20261028-fourfactor-paired-syndrome-dual-v1.json` SHA-256 `96258a93dad1aea8b09969ade818438f87948a7afc841f317c8a119542ab318a` expresses the mixed-block `Delta` as a two-automorphism average of 527 elemental CMIs with negative weights plus 14 equalities: six original graph FDs, two full-syndrome-from-neighbour FDs (vertices 6 and 7), one full-syndrome-from-all FD, and five conditional local component FDs. Thus the mixed-block gap is nonpositive. No conditional triangle entropy gate, syndrome entropy cap, one-hot inequality, two-syndrome theorem, or numerical LP optimum is used in this identity.

The independent checker `frontier-20261028-fourfactor-paired-syndrome-dual-check.py` SHA-256 `4b7c942dca70dc8788c4d31ce8f36b70e50b10323bba7ec0bfc021dc3393a5c1`, receipt SHA-256 `f22641c7b04912c329233b2fbc16a7aa88d7c9cc3d27b1ed2753dde74ce1d4d3`, validates all 2,047 entropy-coordinate coefficients and signs, graph/factor/partition automorphisms, local-row inclusion and two negative controls exactly.

The six fixed-syndrome triangle factors, each of which has nonpositive conditional balance gap under any law, are then tensorized first; replacing conditioning on all previous factor tuples by conditioning only on each vertex's earlier components lifts the mixed-block result to the entire original law. This is written mathematics, not proof-assistant formalization or scientific adoption. The candidate has no novelty clearance.
