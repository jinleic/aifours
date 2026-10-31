# Semiprime coset obstruction with distributional FDs only

**Status: WRITTEN, elementary entropy and subgroup argument; scientific review and novelty clearance pending.** This is an additive generalization of `frontier-20261028-semiprime-coset-obstruction-v1.md` (SHA-256 `6f03cf0278c9d92ba9ca2ad10d32ba8afbccc1a3696e2fb3b5a77941ae55cd8f`), not an edit to that packet. It removes its full-coset FD assumption, including for nonuniform or restricted-support distributions.

Let `G` be a finite group, `H_i` subgroups, `K=intersection_i H_i`, `g` an arbitrary `G`-valued random variable, and `X_i=gH_i`. Suppose the `X_i` satisfy the FDs of any finite loop-free directed dependency graph **under the given distribution**. If `[G:K]` is prime or a product of two primes, then

\[
H(X_V)\le \frac23\sum_{i\in V}H(X_i).
\]

No full-support or subgroup-inclusion FD is assumed; no normality of the subgroups is assumed. In particular this holds for original-neighbour R-minus laws of this form. It does not exclude strict-gain group laws of effective index with three or more prime factors, nor general non-group laws.

## Proof

For every distribution of `g`, the joint variable `X_V` has exactly the information of `gK`, because two group elements have the same whole coset vector precisely when their relative element belongs to every `H_i`. A graph FD says that `X_i` is a function of its neighbours on the support of `g`.

If some `H_i=K`, then `X_i` has the whole joint entropy `H(X_V)`. Its neighbours have total singleton entropy at least this much by the FD and subadditivity. The loop-free condition keeps vertex `i` out of its own neighbourhood, so the total singleton sum is at least `2H(X_V)`.

If `[G:K]=p` is prime and no `H_i=K`, then all `H_i=G`, contradicting the definition of `K` with index `p`. The full-variable case already proves the prime result, even for nonuniform `g`.

Now let `[G:K]=pq` for primes `p<=q` and suppose no `H_i=K`. Every nonconstant subgroup is strictly between `K` and `G` and has `[H_i:K]` equal to `p` or `q`. For any two distinct such subgroups `A,B`, one has `A∩B=K`: the index `[A∩B:K]` divides the primes `[A:K]` and `[B:K]`; if these primes agree, the only alternative to `K` is `A=B`. Thus `(gA,gB)` determines `gK` under **any** distribution. Call each distinct intermediate subgroup a type; repeated vertices of one type have exactly the same random variable.

* **At least three types.** Pick one vertex each of three distinct types `A,B,C`. Any chosen pair determines `X_V`. The three pairwise subadditivity inequalities add to `2[H(gA)+H(gB)+H(gC)] >= 3H(X_V)`, proving the desired bound.
* **Exactly two types `A,B`.** If each occurs at least twice, the total singleton sum is at least `2H(gA)+2H(gB)>=2H(X_V)`. If `A` occurs once and `B` at least twice, the unique `A` vertex's neighbours can contain only copies of `gB` or constants. Its distributional FD therefore makes `gA` a function of `gB`; since the pair determines the whole vector, `H(X_V)=H(gB)`, and the two `B` copies already contribute `2H(X_V)`. The symmetric case is identical. If both occur once, each FD makes its type a function of the other, so both have entropy `H(X_V)` and their sum is `2H(X_V)`. These arguments include degenerate random variables.
* **At most one type.** Without an `H_i=K`, the intersection of all subgroups is either `G` or that sole intermediate subgroup, not `K`; this contradicts `[G:K]=pq`.

All cases yield the bound. In the prime/full-variable case and the two-type case, the stronger `sum_i H(X_i)>=2H(X_V)` holds. No claim is made about novelty, a strict original guessing-number bound, arbitrary finite laws, or group indices with more than two prime factors.
