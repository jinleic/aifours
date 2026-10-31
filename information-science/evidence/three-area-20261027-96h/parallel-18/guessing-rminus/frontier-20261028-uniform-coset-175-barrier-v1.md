# Strict uniform group-coset gain requires at least 175 effective cosets

**Status: WRITTEN, conditional on two separately pinned exact Shannon/FD and linear-rank certificates; scientific review and novelty clearance pending.** This strengthens the `102`-coset restriction in `frontier-20261028-uniform-coset-s5-obstruction-v1.md` (SHA-256 `db7880f7f91b5b541784fc4825809dfcd7d6be0161ac21e81c7a84997de6f531`).

Let `g` be uniform in a finite group `G`, let `X_i=gH_i` satisfy the ten original R-minus FDs, and set `K=intersection_i H_i`, `d_i=[G:H_i]`, `m=[G:K]`. If the balance gap `Delta=H(X_V)-(2/3)sum_i H(X_i)` is strictly positive, then

\[
m\ge175.
\]

In fact all `d_i>=2`, at least two satisfy `d_i>=3`, and if exactly two satisfy `d_i>=3` then their vertices must be adjacent. Consequently **no uniform group-coset law for any group of order at most 174** can give strict balance; this does not cover nonuniform group laws or arbitrary FD laws.

## Two exact imports

The conditioned proper-subgraph inequality `frontier-20261028-conditioned-proper-subgraph-inequality-v1.md` SHA-256 `c46831b9324e7e8c65009c2a27f3391db7705c370bfb63435a73b0117be3df49` implies that `Delta>0` requires all ten `X_i` nonconstant, hence all `d_i>=2`. The representable-rank result `frontier-20261028-linear-ingleton-bound-v1.md` SHA-256 `e056dd9695a4b3e308431441b4f15ec3a2d81f3c733c604cff8246796abf3da4` proves `Delta<=0` for every finite-field linear-rank law satisfying the graph FDs. Both certificates and their review boundaries are inherited; no numerical LP status is used as proof.

## At most one nonbinary coset is linear

Suppose all but at most one of the `d_i` equal 2. Every index-two subgroup is normal, and

\[
K_2=\bigcap_{i:\,d_i=2}H_i
\]

is the kernel of the product of their quotient homomorphisms. Hence `G/K_2` is isomorphic to a subgroup of a binary vector space and is itself an elementary abelian 2-group.

If every `d_i=2`, then `K=K_2`. Otherwise let `j` be the sole vertex with `d_j>=3`. Uniformity of `g` makes its FD equivalent to subgroup inclusion `intersection_{i in N(j)} H_i <= H_j`. All neighbours of `j` have index two, so `K_2` lies in that neighbour intersection and therefore in `H_j`; again `K=K_2`. Each subgroup `H_i/K_2` is a vector subspace of `G/K_2`, and every coset variable is a linear quotient of a common uniform binary vector. Thus the entire entropy profile is representable over `F_2`, including the original graph FDs. The pinned linear-rank inequality gives `Delta<=0`, contrary to strict gain.

If there are exactly two vertices with `d_i>=3` and they are nonadjacent, the same argument applies separately at both vertices: each has only index-two neighbours, so `K_2` lies in both exceptional subgroups, and again the law is a binary linear-rank law. Thus two exceptional vertices, if there are exactly two, must be adjacent.

## Exact lower bound

With at least two `d_i>=3` and all other `d_i>=2`, uniformity gives `H(X_i)=log d_i`, `H(X_V)=log m`. Strict balance is equivalent to

\[
m^3>\prod_{i=1}^{10}d_i^2\ge2^{16}3^4=5308416.
\]

Because `174^3=5268024 < 5308416 < 175^3=5359375`, one must have `m>=175`. This is a restricted-class obstruction only. No global guessing-number equality, novelty, nonuniform result or proof-assistant formalization is claimed.
