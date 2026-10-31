# An unconditional conditioned entropy inequality for every original vertex

**Status: WRITTEN with separately checked exact Shannon/FD certificates; scientific review and novelty clearance pending.** Let `X_1,...,X_10` be any finite joint law satisfying all original-neighbour R-minus FDs, and put

\[
\Delta=H(X_1,\ldots,X_{10})-\frac23\sum_{i=1}^{10}H(X_i).
\]

For **every** `k=1,...,10`, the following unconditional inequality holds:

\[
\boxed{\quad 3\Delta+2\sum_{i\ne k} I(X_i;X_k)\le H(X_k).\quad}
\tag{1}
\]

In particular, `Delta>0` requires every original variable to be nonconstant and

\[
2\sum_{i\ne k}I(X_i;X_k)<H(X_k)\qquad\text{for every }k.
\]

Summing (1) also yields `30 Delta + 4 sum_{i<j} I(X_i;X_j) <= sum_i H(X_i)`. These are **Shannon/FD consequences**, not a new numerical upper bound on the guessing number and not a strengthening of an LP that already includes all original Shannon rows and FDs. They constrain any strict-gain law without assuming linearity, symmetry, support size, or uniformity.

## Proper-subgraph inequality

For each vertex `k`, every law satisfying the FDs on the induced graph `R-minus - k` obeys

\[
H(X_{-k})\le\frac23\sum_{i\ne k} H(X_i).
\tag{2}
\]

There are three vertex orbits under the checked graph automorphism group:
`{1,8}`, `{2,5,9,10}`, and `{3,4,6,7}`. For representative `k=1`, the induced graph is 3-colorable, with color classes `{2,5,8}`, `{3,6,10}`, and `{4,7,9}`. Any two grouped color-class tuples determine all support words: two distinct words must differ at neighbouring vertices by the FDs, and the edge's endpoints have different colors. Three applications of entropy subadditivity give (2).

For the other two representatives, `k=2` and `k=3`, the pinned exact certificates below give identities, valid for arbitrary nine-variable entropy vectors,

\[
M_k\left(2\sum_{i\ne k}H(X_i)-3H(X_{-k})\right)
=\sum_j a_j\,I_j+\sum_{i\ne k}b_i\,H(X_i\mid X_{N(i)\setminus\{k\}}),
\tag{3}
\]

where every `I_j` is an elemental CMI or elemental conditional entropy, every `a_j` is a positive integer, `b_i` is an integer, and `M_2=13`, `M_3=72`. The nine last conditional entropies are zero by the induced-graph FDs, so Shannon nonnegativity proves (2). The checker verifies all 511 nonempty entropy-coordinate coefficients, signs and FD rows in each identity. The two generator permutations, their group of order 8, the three orbits and the `k=1` coloring are also checked exactly. Relabeling proves (2) for all ten `k`.

## Lifting to all ten variables

Fix `k` and condition on any value of `X_k` with positive probability. The other nine variables satisfy the induced-graph FDs in that conditional law: if `k` is a neighbour, its fixed value can be supplied to the original decoder; otherwise the original decoder already uses only surviving vertices. Applying (2) to each conditional law and averaging gives

\[
H(X_{-k}\mid X_k)\le\frac23\sum_{i\ne k}H(X_i\mid X_k).
\]

Insert `H(X_V)=H(X_k)+H(X_{-k}|X_k)` and `H(X_i|X_k)=H(X_i)-I(X_i;X_k)`, and rearrange to obtain (1). If `X_k` is constant, the same inequality yields `Delta<=0`; thus every strict-gap FD law uses all ten vertices nontrivially. This strengthens the active-set conclusion in `frontier-20261028-active-vertex-obstruction-v1.md` without changing that pinned packet.

## Exact evidence

* Integer coefficient lists `frontier-20261028-nine-active-shannon-certificates-v1.json` SHA-256 `b4f8497f9c8400b360f004e9bb7b9f2e209e635e5a1af26dadd9c9e82173153d`. The `k=2` identity has 186 CMIs, one elemental conditional entropy and nine FDs; `k=3` has 270 CMIs, one elemental conditional entropy and nine FDs.
* Independent exact checker `frontier-20261028-nine-active-shannon-independent.py` SHA-256 `9ae8475f14ba702a1bf1e354a771c2d5f9e97146654b548541c057b0e12addd0`; receipt SHA-256 `a284cb2b2112e8482d9e316d3b64718e7d1dde1d1712b2250438264bc1af1cb2`. It pins the graph census, reconstructs both integer identities and every FD row from graph adjacency, checks signs and orbit/color claims, and rejects four intended mutations.
* Source graph census SHA-256 `75884fb96097853126b328c6308c822a8439bee05c0e94c083e91320e4c3062f`; its graph-neighbour lists are checked against the checker. The numerical LP duals only proposed the coefficient lists; the bound rests on the exact integer cancellation, not floating solver status.

No proof-assistant formalization, independent scientific review, or claim of broad novelty has been made. The true unrestricted balance inequality `Delta<=0` and original guessing-number question remain open.
