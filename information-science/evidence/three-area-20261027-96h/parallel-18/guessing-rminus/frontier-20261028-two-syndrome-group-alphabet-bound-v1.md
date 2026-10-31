# Two-syndrome bound for arbitrary finite group factor alphabets

**Status: WRITTEN; scientific review pending.** The q=8 result `frontier-20261028-two-syndrome-global-entropy-bound-v1.md` SHA-256 `4fcbf234c2710ee91c8a5e0a9b0b79414bb97438be7986468094d8e2230b2bf9` extends, with the same exact Shannon certificate, from bits to arbitrary finite, possibly nonabelian groups in each triangle factor.

For each of the ten ordered triangles `T_t=(i,j,k)`, fix a nontrivial finite group `G_t`. Let vertex `v` receive one component in `G_t` for each triangle containing `v`, and define the ordered factor syndrome `sigma_t=X_i^t X_j^t X_k^t` in `G_t`. For **any** original-neighbour FD law, with arbitrary probabilities and correlations, if the vector `(sigma_1,...,sigma_10)` has support of size at most two, then

\[
H(X_V)\le\frac23\sum_v H(X_v).\tag{27}
\]

Consequently an FD support `W` of this kind satisfies

\[
|W|\le\prod_{t=1}^{10}|G_t|^2.
\]

The product of the ten fixed-identity-syndrome factor codes attains equality. If all factors use one group of order `m`, this is a statement about q=`m^3` alphabets and reads `|W|<=m^20=q^(20/3)`. It constrains only strategies whose group-factor syndrome vector has at most two values; it is not a general guessing-number upper bound for all strategies or any arbitrary alphabet.

## Proof

Every group factor with a fixed syndrome has the property that any two components determine the third, with no commutativity required. Conditional triangle subadditivity and factor tensorization therefore give the same gate `3H(X_V|S)<=2 sum_v H(X_v|S)` used in the q=8 proof whenever all ten factor syndromes distinguish the same binary selector `S`. Each factor's syndrome determines `S`, so every triangle determines `S`; the original FDs then make `S` a function of every original neighbour tuple. The exact 319-CMI/FD dual and its checked signs and coefficients in the q=8 packet depend only on those entropy statements, not on alphabet size or group multiplication. It therefore proves (27) for this all-factor common-selector case.

For two general syndrome vectors `s,t`, write `J={r:s_r!=t_r}` and normalize each factor by the fixed bijection `X_i^r -> s_r^(-1) X_i^r` on the first triangle component. The two factor syndromes are now the identity or `d_r=s_r^(-1)t_r`; for `r in J`, `d_r` is nonidentity and determines the common selector `S`. If `J` does not cover all vertices, use the same proper-subgraph/conditional-tensorization proof as in the q=8 packet, which is alphabet-independent. For one syndrome value, ordinary fixed-syndrome tensorization suffices.

If `J` covers, condition on all constant-syndrome factor tuples. In each positive fiber the remaining blocks retain the graph FDs, and the selector `S` is determined by every original neighbourhood: choose any selected triangle containing the vertex, recover that vertex's block from its neighbours, and compute its factor syndrome from the three triangle components.

For each omitted factor `r`, choose a nonidentity `d_r in G_r` and adjoin independent uniform `A,B in G_r`; put

\[
C=B^{-1}A^{-1}h_r(S),\qquad h_r(0)=e_r,\quad h_r(1)=d_r.
\]

Thus `ABC=h_r(S)`, so each augmented factor syndrome determines `S`. Given `S`, any two of `A,B,C` determine the third, and every appended vertex component is recoverable from original neighbours because those neighbours already determine `S`. Every one of `A,B,C` is uniform and independent of the previous law and `S`; within any one vertex the new components from distinct factors are jointly independent. Because `S` is a function of the old selected blocks, factor `r` increases joint entropy by `2 log|G_r|` and the singleton entropy sum by `3 log|G_r|`, leaving `Delta` unchanged. Apply the all-factor lemma on each fiber and tensorize the conditioned fixed factors. The noncover branch retains the q=8 packet's dependence on the previously pinned proper-subgraph inequality.

## Exact support for the algebraic step

The group inverse formulas are `A=h(S) C^(-1) B^(-1)`, `B=A^(-1) h(S) C^(-1)`, and `C=B^(-1) A^(-1) h(S)`. Uniformity follows from translations/inversion being bijections. `frontier-20261028-group-syndrome-gadget-check.py` SHA-256 `f9343b21eb991908211baae6b24a3f77d9cf12cb9951c3b08dbad94cc728551e`, receipt SHA-256 `ec1ac1a241e8647bdcb2d30e08a2dee06dc31cc9e75b9d76013ab696e60c1326`, checks all selector/pair inputs, inverse decoders, and singleton uniformity in `Z/2`, `Z/3`, `Z/4`, `Z/5`, and nonabelian `S3`, with an incorrect-syndrome control. These finite checks illustrate but do not substitute for the written general-group proof. The result does not rely on the group law being abelian, does not extend to three syndrome vectors, and is neither formally verified nor novelty-cleared.
