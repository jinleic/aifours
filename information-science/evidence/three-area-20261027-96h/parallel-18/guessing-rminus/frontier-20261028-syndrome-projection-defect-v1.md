# A syndrome-only upper bound on the entropy gap

**Status: WRITTEN, conditional on the compact exact coefficient certificate; scientific review pending.** For any original-neighbour R-minus FD law in the finite-group triangle-factor encoding, let `S=(S_1,...,S_10)` be the full syndrome vector. Let `I(v)` be the three factor indices incident to `v`. Then

\[
\begin{aligned}
12\Delta(X)\le{}&\sum_{v\in\{2,5,9,10\}}H(S\mid S_{I(v)})\\
&+2\sum_{v\in\{6,7\}}H(S\mid S_{I(v)})\\
&+\sum_{t\in\{1,2,6,8\}}H(S\mid S_t).
\end{aligned}\tag{49}
\]

This bound depends only on the **syndrome distribution**, not on unknown conditional entropies of vertex tuples, and is valid for arbitrarily many syndrome values, nonabelian groups, and arbitrary correlations. It does not show the right side vanishes in general or improve the known unrestricted numerical guessing-number bound.

## Proof

For each vertex `v`, the original neighbour tuple determines the whole block `X_v`. For every factor incident to `v`, the other two components are already in neighbours, so `S_{I(v)}` is a deterministic function of `X_{N(v)}`. Conditioning on a richer tuple cannot increase conditional entropy, hence

\[
H(S\mid X_{N(v)})\le H(S\mid S_{I(v)}).
\]

Likewise triangle `T_t` itself exposes all three components of its factor and hence `S_t`, giving `H(S|X_{T_t})<=H(S|S_t)`. Substitute these inequalities into the exact compact bound (42) in `frontier-20261028-compact-full-syndrome-inequality-v1-addendum-1.md` SHA-256 `2f7a18d11fde89e9c94bf57ee376967f0f8294b1b6660699d6be2c4cc25eeed6`; its coefficient identity is checked by receipt SHA-256 `fe63e84172928106831f8e6062da5ad9f0d0226d40d5f466c1e863ce8790f029`.

In particular, (49) proves `Delta<=0` if each of the four factor coordinates `1,2,6,8` individually determines the full syndrome vector **and** each incident-factor triple `S_{I(v)}` does so for vertices `2,5,6,7,9,10`. This joint-triple condition is less restrictive than requiring an individual incident factor to identify `S`; the binary five-factor criterion is a special case. Other support sets require separate analysis. Formal proof, novelty clearance and independent scientific adoption are not claimed.
