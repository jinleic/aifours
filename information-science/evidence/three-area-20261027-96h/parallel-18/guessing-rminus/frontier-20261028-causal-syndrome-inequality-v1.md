# A causal syndrome-uncertainty bound for arbitrary q=8 laws

**Status: WRITTEN, exact chain-rule/Shannon argument; scientific review and novelty clearance pending.** Fix the standard ten-triangle q=8 bit encoding, let `Z_t` be the triple of factor-`t` bits, `S_t` their XOR, and order the ten factors arbitrarily. For **any** joint law on the vertex symbols, even without graph FDs,

\[
\Delta=H(X_V)-\frac23\sum_i H(X_i)
\le\sum_t H(S_t\mid Z_{<t}).\tag{21}
\]

In particular, if some factor order makes every syndrome `S_t` a deterministic function of the preceding factor tuples, then `Delta<=0`. Thus any strict-gap q=8 law must have irreducible syndrome uncertainty in **every** factor order. This includes nonlinear sequential switching of the triangle factors, but does not rule out laws with cyclic or otherwise irreducible syndrome dependence.

A stronger exact identity is

\[
\begin{aligned}
3\Delta=\sum_t\bigg(&3H(S_t\mid Z_{<t})
-2\sum_{i\in T_t}I(X_i^t;S_t\mid Z_{<t})\\
&-\sum_{\{i,j\}\subset T_t}I(X_i^t;X_j^t\mid S_t,Z_{<t})
-2\sum_{i\in T_t}I(X_i^t;Z_{<t}\mid X_i^{<t})\bigg).
\end{aligned}\tag{22}
\]

All terms subtracted from the conditional syndrome entropies are nonnegative. This is an encoding-dependent structural inequality, not a numerical q=8 upper bound, unrestricted guessing-number result, formal proof, or novelty claim.

## Proof

For each factor, `S_t` is a function of its three bits, and conditioning on `S_t` fixes their affine XOR parity. Any pair of bits then determines the third, so conditioned on `S_t,Z_<t`,

\[
3H(Z_t\mid S_t,Z_{<t})
=2\sum_{i\in T_t}H(X_i^t\mid S_t,Z_{<t})
-\sum_{\{i,j\}\subset T_t}I(X_i^t;X_j^t\mid S_t,Z_{<t}).
\]

Insert `H(Z_t|Z_<t)=H(S_t|Z_<t)+H(Z_t|S_t,Z_<t)` and `H(X_i^t|S_t,Z_<t)=H(X_i^t|Z_<t)-I(X_i^t;S_t|Z_<t)`. The remaining difference between conditioning a bit on all past factors and on its own vertex's past components is exactly `I(X_i^t;Z_<t|X_i^<t)`. Summing over factors and applying the joint and singleton chain rules gives (22), hence (21).

For the comparison with the earlier syndrome-tuple gate `frontier-20261028-syndrome-entropy-gate-v1.md` SHA-256 `2efc6640f4551bcad35ea3678737aa0242e0d85921846134166b9c7f59a98b81`, note that `S_<t` is a function of `Z_<t`, so `sum_t H(S_t|Z_<t)<=sum_t H(S_t|S_<t)=H(S)`. No independent scientific review or proof-assistant formalization has been completed.
