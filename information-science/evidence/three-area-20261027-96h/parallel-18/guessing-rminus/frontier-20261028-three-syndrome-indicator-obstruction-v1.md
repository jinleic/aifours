# Why the two-syndrome theorem does not induct automatically to three

**Status: WRITTEN-CHECKED-IN-KERNEL, conditional on the unreviewed two-syndrome theorem; independent scientific review pending.** The natural induction that conditions a three-state syndrome on each of its three state indicators, then uses only Shannon inequalities and the resulting conditional two-syndrome entropy gates, cannot prove `Delta<=0`. An explicit rational **14-variable polymatroid** satisfies all of those constraints but has `Delta=7/92>0`. This is not an entropy law or an FD strategy, and does not decide the three-syndrome case.

## The candidate induction and its exact limit

For a genuine law with syndrome state `S in {0,1,2}`, write `S_j=1{S=j}`. On each `S_j=1` fiber the syndrome has one value, and on each `S_j=0` fiber it has at most two. Therefore the two-syndrome theorem gives `Delta(X|S_j)<=0` for each `j`; conditioning on the full syndrome also gives `Delta(X|S)<=0` by factor tensorization. Because all these variables are functions of `X_V`, each conditional inequality is an 11-variable gate of the form

\[
3H(X_V)+17H(U)-2\sum_iH(X_i,U)\le0,\quad U\in\{S,S_0,S_1,S_2\}.\tag{28}
\]

The state and indicators satisfy `H(S_j|S)=0`, `H(S|S_j,S_k)=0` for distinct `j,k`, and `H(S,S_0,S_1,S_2|X_V)=0`. The countermodel below respects these identities, all Shannon inequalities on the full joint 14-coordinate polymatroid, the ten graph FDs, the four gates (28), and the q=8 singleton caps.

## Exact countermodel

Read the required source erratum `frontier-20261028-full-source-lp-optimum-v1-erratum-1.md` SHA-256 `c64e2a1a3a78d1d71f76d9f04903408e619168945b959d787b06938f8ba6ded9` before the frozen primal `frontier-20261028-separator-bound-primal.json` SHA-256 `aadf84109c619791c5882cb688a30facdbf25b3ae5a6ddde25d17b2e7ef6b651`. Let `h` be the ten-original-variable primal coordinates scaled by 3. Then every singleton is 3, `h(V)=1847/92`, and `Delta(h)=7/92`. Put `k=7/92`, and for each subset `A` of original coordinates define

\[
h(A,S)=\min\{h(A)+2k,h(V)\},\quad
h(A,S_j)=\min\{h(A)+k,h(V)\}.
\]

For any auxiliary subset containing `S` or at least two `S_j`, assign entropy `h(A,S)`; for exactly one indicator, assign `h(A,S_j)`; for no auxiliary, use `h(A)`. This explicitly specifies all `2^14` coordinates. It has `h(S)=2k`, each `h(S_j)=k`, and `h(S_j,S_k)=2k`. It satisfies the functional equalities above, all four gates (28), and all graph FDs. `frontier-20261028-three-syndrome-indicator-countermodel-check.py` SHA-256 `9df388bce63603252e8e7648cb1248f888a72dc70e50f862d41e5d8029551660`, receipt SHA-256 `582216d8c76f5c86a71e9cfda6ed5d537d4394a622aa066414181b0e79b7d18e`, checks every one of 372,736 elemental CMIs, all 14 elemental monotonicities, each gate and graph FD, all 1,024 original-subset conditional indicator bounds, singleton caps and an altered-determinism control, using rational arithmetic.

The countermodel **cannot** realize actual one-hot indicators: for distinct `j,k` it makes `I(S_j;S_k)=0` while `H(S_j)=H(S_k)=k>0`; nonconstant one-hot binary indicators can never be independent because they cannot simultaneously equal one. Thus extra information specific to the three-state support, not merely the listed functional equalities and Shannon rules, is needed to close this proof route. No joint extension to the publisher's complete copy branches or realization by entropy distributions is asserted. Scientific review, formalization and novelty clearance remain open.
