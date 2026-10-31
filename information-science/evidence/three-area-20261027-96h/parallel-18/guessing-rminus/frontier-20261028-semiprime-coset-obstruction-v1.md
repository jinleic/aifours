# Prime and semiprime group-coset laws cannot give strict R-minus gain

**Status: WRITTEN, elementary group and entropy argument; review and novelty clearance pending.** This is a new restricted-class obstruction, not a general no-gain result.

Let `G` be a finite group, `H_1,...,H_10` subgroups, `K=intersection_i H_i`, and `g` any `G`-valued random variable. Set `X_i=gH_i`. Assume the **full-coset FD condition** `intersection_{j in N(i)} H_j <= H_i` for every original R-minus vertex. If `[G:K]` is prime or a product of two primes (including a prime square), then

\[
\Delta=H(X_1,\ldots,X_{10})-\tfrac23\sum_i H(X_i)\le0.
\]

The proof uses only the absence of self-loops, so it applies verbatim to any finite loop-free directed dependency graph, with the sum over all its vertices.

Thus a strict-gain group-coset witness with these full-coset FDs must have `[G:K]` with at least three prime factors counted with multiplicity. In particular this applies to every **uniform** group-coset law satisfying the original graph FDs, because uniformity makes those FDs equivalent to the full-coset subgroup condition. No normality of `K` or `H_i` is assumed. For prime index the same conclusion holds for arbitrary `g` even when only the distributional graph FDs are assumed.

## Facts used

The full-coset condition is sufficient for the original graph FD under any law on `g`: if all neighbour cosets agree, their relative group element lies in the intersection of neighbour subgroups, hence in `H_i`. It is also necessary for uniform `g`, but an FD on only a restricted support need not imply the full-coset condition. For any distribution, the full vector of cosets has exactly the information of `gK`: two elements have the same whole vector if and only if their relative element lies in `K`. Every `H_i` contains `K`, so `[G:H_i]` divides `[G:K]`.

If some `H_i=K`, then `X_i` determines the whole vector. Its FD and entropy subadditivity show that its neighbours' singleton entropies sum to at least `H(X_V)`. Since the graph has no self-loops, the total singleton sum is at least twice `H(X_V)`, so `Delta<=-H(X_V)/3`. This case holds for any distribution satisfying the graph FDs.

## Prime index

If `[G:K]=p` is prime, each `H_i` is either `G` or `K`, with at least one equal to `K`. For any distribution on `g`, the variables with subgroup `K` are copies of the same coset random variable, of entropy `h`; all others are constant. If `h=0` then `Delta=0`. If `h>0`, the graph FD for a nonconstant vertex requires a nonconstant neighbour, so their number `m` is at least two. Thus `Delta=(1-2m/3)h<=0`, including for distributions without full support.

## Semiprime index

Write `[G:K]=pq`, primes `p<=q`, and assume no `H_i=K` by the full-variable case. Every nonconstant subgroup then lies strictly between `K` and `G`, and has `[H_i:K]` equal to `p` or `q`. If `A` and `B` are two **distinct** such subgroups, their intersection is `K`: `A∩B` contains `K`, and its index over `K` divides both prime numbers `[A:K]` and `[B:K]`; if those primes agree, the only alternative to `K` would be `A=B`. Consequently no distinct intermediate subgroup contains another, and the pair of cosets `(gA,gB)` determines the entire vector `gK`, for any law on `g`.

If there are at least three distinct intermediate subgroup types `A,B,C`, select one vertex of each type. Every selected pair determines the whole joint vector, so pairwise entropy subadditivity gives `H(gA)+H(gB)>=H(X_V)`, `H(gA)+H(gC)>=H(X_V)`, and `H(gB)+H(gC)>=H(X_V)`. Hence these three singleton entropies already sum to at least `(3/2) H(X_V)`, proving `Delta<=0`.

If there are exactly two types `A,B`, each must occur at least twice. Indeed, at a vertex of type `A`, full-coset FD requires its neighbour intersection to lie in `A`. If none of its neighbours has type `A`, that intersection is `G` or `B`; neither lies in `A`. The same applies to type `B`. Since `(gA,gB)` determines the joint vector, the singleton sum is at least `2H(gA)+2H(gB)>=2H(X_V)`, giving the stronger `Delta<=-H(X_V)/3`. Exactly one intermediate type cannot have total intersection `K`. These arguments also handle degenerate or nonuniform laws on `g`.

## Exploratory search, not a proof

A bounded one-core integer-programming search proposed uniform coset FD laws for `S_3` and `S_4`; its integer incumbents were checked for subgroup closure, all graph FDs and the strict balance inequality. None of those returned incumbents had a strict gain. The floating solver statuses are not nonexistence proofs and are not used above. The successor script `frontier-20261028-group-coset-fd-search-v2.py` has SHA-256 `856a6b1cc28ef8d812c78769e9bb9d936e5ecc1e67838fca94661dd2f5947d5d` and receipt SHA-256 `5dd020341984c4b68a7fdcc45a21e77a940a1f3e0ea4420bebc9f92459ed1331`. Its predecessor had an unintended intersection-bound model; `frontier-20261028-group-coset-fd-search-erratum-v1.json` SHA-256 `c3464a654f7c54f30c1faf40fbe4bdeab3d2b7a134e0f3874f81ec2436e2b57e` retracts its result and must precede any reading of that older receipt.

This result uses only exact group-index arithmetic, injectivity, and written Shannon entropy identities. It does not cover effective index with three or more prime factors, semiprime group laws satisfying only distribution-specific FDs without the full-coset condition, arbitrary non-group FD laws, or any claim of global guessing-number equality.
