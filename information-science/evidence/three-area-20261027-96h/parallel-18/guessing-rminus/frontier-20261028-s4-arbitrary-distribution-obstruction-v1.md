# No S4-coset law, even nonuniform, gives a strict balance gap

**Status: WRITTEN with an independently replayed exact finite subgroup census; conditional on the pinned graph-FD inequality; scientific review and novelty clearance pending.** Let `G=S4`, let `g` have **any** distribution on `G` (including restricted support), and let `X_i=gH_i` satisfy the original R-minus FDs. Then

\[
H(X_V)\le\frac23\sum_{i=1}^{10}H(X_i).
\]

This excludes a whole nonuniform group-coset construction class, not arbitrary FD laws or groups other than `S4`. It depends on `frontier-20261028-conditioned-proper-subgraph-inequality-v1.md` SHA-256 `c46831b9324e7e8c65009c2a27f3391db7705c370bfb63435a73b0117be3df49`, whose exact certificates and scientific-review boundary remain unchanged.

## Two general necessary conditions

Suppose `Delta>0`. The conditioned inequality makes all ten `X_i` nonconstant and forbids one from determining another. Thus the ten subgroups form an inclusion **antichain**: if `H_i<=H_j`, the coset `gH_i` determines `gH_j`, regardless of the distribution of `g`. Put `K=intersection_i H_i`. None of the ten subgroups is `G` or `K`, since `G` gives a constant variable and `K` is contained in every other subgroup.

Also, there cannot be three subgroups `H_i,H_j,H_k` with every pairwise intersection equal to `K`. Each pair of their coset variables would then determine `gK`, and hence the entire joint vector, for every value of `g`. Adding the three pairwise entropy-subadditivity inequalities gives `2[H(X_i)+H(X_j)+H(X_k)]>=3H(X_V)`, so the full singleton sum is at least `(3/2)H(X_V)`, contradicting `Delta>0`.

## Exact S4 census

`S4` has exactly 30 subgroups. If `K` is nontrivial, the exact census finds at most **seven** proper strict supergroups of `K`; hence ten distinct `H_i` cannot exist. If `K={e}`, there are 28 proper nontrivial subgroups. Exhaustive enumeration of their incomparable families containing **no** triple with pairwise intersection `{e}` gives these counts by family size 0 through 10:

```text
1, 28, 315, 740, 1126, 1092, 715, 309, 79, 9, 0
```

Thus every ten-element subgroup antichain contains a reconstruction triple, contradicting strict balance. This proves the result for every `K` and every distribution of `g`; it does not assume that the graph FDs hold outside the distribution's support.

## Evidence

Producer `frontier-20261028-s4-antichain-triple-census.py` SHA-256 `0b2a5d443c583bb1ffff707f63f7d1bd2628dfef45dd585fb8b5f9f3edb9cb66`, receipt SHA-256 `cd4d16622d7c56bebbc396295542fe7e1d78a274809e9ec0805c21b0889ad282`, enumerates subgroups by adjoining generators and counts families by a bitset search. Separately written `frontier-20261028-s4-antichain-triple-independent.py` SHA-256 `0ebc0f9dc54605749416ab557f5e3e78671e9b19e051091723debd47e58b0325`, receipt SHA-256 `149a5a4d54ab6e7edd2014343f16e2fe2ae0532795446a64d32a995fc2185c9d`, independently enumerates all 12,403 inverse-closed candidate sets whose cardinalities divide 24 and checks closure, recovering exactly the same 30 subgroups; it replays the family counts using include/exclude recursion, all 29 nontrivial `K` cases, and a ten-element antichain control that is rejected specifically by its reconstruction triple. Exact integer/permutation checks are not a proof-assistant formalization or independent scientific review.
