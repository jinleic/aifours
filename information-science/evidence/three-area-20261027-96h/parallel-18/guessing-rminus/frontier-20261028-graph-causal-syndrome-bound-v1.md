# A graph-aware causal syndrome bound for every q=8 FD law

**Status: WRITTEN, conditional on the pinned proper-subgraph inequality; scientific review pending.** Fix the standard ten-triangle q=8 component encoding. For any original-neighbour R-minus FD law, choose a set `J` of factor indices whose triangles do **not** cover every graph vertex. Order the remaining factors arbitrarily, and write `P_t` for the full tuples of previously ordered factors outside `J`. Then

\[
\boxed{\quad \Delta\le\sum_{t\notin J} H(S_t\mid P_t).\quad}\tag{23}
\]

In particular, if all syndromes outside such a `J` are deterministic functions of their respective preceding factor tuples, then `Delta<=0`, even when those syndromes are not constant and the variables are nonuniform. This strengthens the varying-factor cover criterion `frontier-20261028-syndrome-cover-entropy-gate-v1.md` SHA-256 `d6df004e025f067a14a6cc69e9aef8d9fc78a20a2fc49c4e431328120e32014b`. It is an information inequality/structural gate, not a numerical guessing-number bound.

## Proof

For each ordered factor `t` outside `J`, syndrome `S_t` is a function of its three bits. Conditional on `S_t,P_t`, its affine XOR parity is fixed, so any two bits determine the third. Hence

\[
\begin{aligned}
H(Z_t\mid P_t)
&=H(S_t\mid P_t)+H(Z_t\mid S_t,P_t)\\
&\le H(S_t\mid P_t)+\frac23\sum_{i\in T_t}H(X_i^t\mid P_t),
\end{aligned}
\]

where the last step additionally drops conditioning on `S_t` from the bit entropies.

Condition on all outside-`J` factor tuples and treat the `J` factors as one final block. Their reduced components still obey the graph FDs with the fixed components supplied to the original decoders. At a vertex outside the union of triangles in `J`, the reduced component is constant. Thus the pinned inequality `frontier-20261028-conditioned-proper-subgraph-inequality-v1.md` SHA-256 `c46831b9324e7e8c65009c2a27f3391db7705c370bfb63435a73b0117be3df49` gives the two-thirds balance bound for that conditional block.

Sum over the ordered outside factors and the final block. Replacing conditioning on all prior factor tuples by conditioning only on the corresponding vertex's prior components can only increase the right side; the joint and singleton chain rules then yield (23). No independence or uniformity is assumed. For `J=empty`, the final block is trivial and (23) is the general causal syndrome bound; the derivation here is self-contained.

This result leaves open whether its right side can be bounded tightly enough, or its subtracted information terms controlled, to improve the inherited unrestricted upper bound. No independent scientific review, proof-assistant formalization or novelty claim has been made.
