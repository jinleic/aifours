# No nonuniform entropy gain inside a fixed triangle-syndrome coset

**Status: WRITTEN with an exact symbolic entropy-identity check.** This is a nonuniform-law result for a specified construction, not an unrestricted upper bound on the original R-minus guessing number. It applies to any finite abelian group and arbitrary probability distributions on the coset, including distributions with smaller support or correlations between triangles.

## Theorem

For the ten-triangle cover and original R-minus graph in `frontier-20261028-triangle-two-coset-obstruction-v1.md` (SHA-256 `da26dfb13dfe38bdcc5c07a3d33a90a5b7adba77eebbcb6d36c2141ce4e032b7`), give each vertex a separate component for every triangle occurrence, and let `X_v` be its three-component symbol. Suppose that, for each triangle, its three component variables satisfy a fixed sum constraint over a finite abelian group. The fixed triangle sums need not be zero. Then for **every** joint probability distribution on those words,

\[
H(X_1,\ldots,X_{10})\le \frac23\sum_{v=1}^{10}H(X_v)
\le \frac{20}{3}\max_v H(X_v).
\]

Thus the entropy-ratio bridge cannot improve `20/3` using any law supported on one affine coset of this triangle-parity code. This is stronger than excluding only larger uniform supports: arbitrary nonuniform weights and arbitrary dependencies across triangles are allowed. If all singleton entropies are zero, the joint entropy is zero as well and no ratio is asserted.

The proof needs only that any two components of each triangle determine the third, so the same inequality holds for products of finite three-variable Latin relations, not just group sums. The separate-coordinate assumption is essential to the statement; the ten symbols are not arbitrary R-minus variables.

## Written proof and exact gap

Order the triangle occurrences arbitrarily. Let `Y_t=(U_t,V_t,W_t)` be the three components of triangle `t`, let `P_t=(Y_1,...,Y_{t-1})`, and let `Q_{v,t}` be the components of vertex `v` belonging to earlier triangles. Every `Q_{v,t}` is a deterministic subtuple of `P_t`.

Conditionally on `P_t`, any two of `U_t,V_t,W_t` determine the third, hence all three pair entropies equal `H(Y_t | P_t)`. Conditional subadditivity gives

\[
3H(Y_t\mid P_t)\le
2\bigl(H(U_t\mid P_t)+H(V_t\mid P_t)+H(W_t\mid P_t)\bigr).
\]

Sum over triangles. The chain rule gives `sum_t H(Y_t | P_t)=H(X_1,...,X_10)`. Because conditioning on `P_t` can only decrease entropy relative to conditioning on `Q_{v,t}`, the sum of the right-hand component entropies is at most `sum_v H(X_v)` by the vertexwise chain rule. This proves the first inequality. The second uses the ten vertices.

More precisely, under the triangle FD constraints the following gap is an exact sum of nonnegative conditional mutual informations:

\[
\begin{aligned}
2\sum_v H(X_v)-3H(X_1,\ldots,X_{10})
={}&\sum_t\sum_{\{u,v\}\subset t}
 I(X_{u,t};X_{v,t}\mid P_t)\\
&+2\sum_t\sum_{v\in t}
 I(X_{v,t};P_t\mid Q_{v,t}).
\end{aligned}
\]

Here `X_{v,t}` denotes that vertex's component at triangle `t`. The pair-CMI terms are nonnegative by Shannon's inequality, as are the temporal terms. The chain rule and deterministic-FD identities justify the displayed equality. In particular, for positive maximum singleton entropy, equality in the `20/3` ratio requires all ten singleton entropies to agree and all listed conditional mutual informations to vanish; those conditions are also sufficient. Independent uniform group-parity triples meet them.

## Integer-coefficient check

`frontier-20261028-triangle-entropy-identity-check.py` SHA-256 `51bc36a81dc44fdbdee3342d53ed70dc0a849f4a987cd085f444c6a5004cd2a6`; receipt SHA-256 `e22f43bf7a8f61d5006ee621c065d40d9529fc98ae053f22eb9d6f0128d12966`.

The checker expands entropy forms on 30 formal component variables using integer coefficients. Before assuming FDs, it verifies exactly that the 30 pair CMIs plus twice the 30 temporal CMIs minus the left-hand gap equal the sum of the 30 triangle conditional entropies `H(third | other two, P_t)`. The coefficient remainder is empty. Those 30 conditional entropies vanish for a fixed triangle-syndrome coset, establishing the displayed identity. The check uses no numerical entropy values, floating-point arithmetic, source LP or external theorem beyond the named Shannon identities.

No formal proof, cross-model review or novelty clearance was performed. Mixed-syndrome laws and strategies outside this particular parity construction remain open.
