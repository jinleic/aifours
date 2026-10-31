# Conditioned balance inequalities for every nonempty vertex set

**Status: WRITTEN corollary of the pinned exact proper-subgraph certificate; scientific review pending.** For any original-neighbour R-minus FD law and every nonempty vertex set `S`, with `Delta=H(X_V)-(2/3)sum_i H(X_i)`,

\[
3\Delta+2\sum_{i\notin S} I(X_i;X_S)+2\sum_{i\in S}H(X_i)\le 3H(X_S).\tag{17}
\]

Consequently a strict-gap law must satisfy `3H(X_S)>2 sum_{i in S}H(X_i)` for every nonempty `S`. In particular, any nonempty subcollection whose joint entropy is at most two-thirds of the sum of its singleton entropies is already an obstruction to strict gain. These are graph-FD/Shannon consequences, not a new numerical guessing-number upper bound.

## Proof

Fix `S` and condition on each positive-probability value of `X_S`. The remaining variables obey their original-neighbour FDs with the conditioned values supplied as constants; the vertices in `S` themselves are constant. The proper-subgraph theorem in `frontier-20261028-conditioned-proper-subgraph-inequality-v1.md` SHA-256 `c46831b9324e7e8c65009c2a27f3391db7705c370bfb63435a73b0117be3df49` applies to each conditional law. Averaging gives

\[
H(X_{V\setminus S}\mid X_S)\le\frac23\sum_{i\notin S}H(X_i\mid X_S).
\]

Insert `H(X_V)=H(X_S)+H(X_{V\setminus S}|X_S)` and `H(X_i|X_S)=H(X_i)-I(X_i;X_S)`, multiply by 3 and rearrange to obtain (17). Its singleton case is exactly the pinned inequality. For a two-vertex set `{a,b}`, it becomes

\[
3\Delta+3I(X_a;X_b)+2\sum_{i\notin\{a,b\}}I(X_i;X_a,X_b)
\le H(X_a)+H(X_b).
\]

No symmetry, uniformity, linearity or finite-alphabet-size restriction beyond finite entropy is used. The proper-subgraph certificate and this derivation await scientific review; no novelty or stronger numerical upper-bound claim is made.
