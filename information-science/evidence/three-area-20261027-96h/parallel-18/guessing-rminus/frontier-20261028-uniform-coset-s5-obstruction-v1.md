# Uniform group-coset laws need at least 102 effective states; S5 cannot witness gain

**Status: WRITTEN conditional on the exact proper-subgraph/conditioned inequality; scientific review and novelty clearance pending.** The group step below is derived from elementary permutation identities, without an imported group-classification theorem. Assume `frontier-20261028-conditioned-proper-subgraph-inequality-v1.md` SHA-256 `c46831b9324e7e8c65009c2a27f3391db7705c370bfb63435a73b0117be3df49`.

For a finite group `G`, choose subgroups `H_1,...,H_10`, draw `g` uniformly from `G`, and set `X_i=gH_i`. If these variables satisfy the original R-minus FDs and have `Delta>0`, then with `K=intersection_i H_i` their effective joint support has size

\[
[G:K]\ge102.
\]

Moreover, **no uniform `S5`-coset law can have `Delta>0`**, irrespective of the ten subgroups. These are restricted-class necessary conditions, not an unrestricted guessing-number bound; no claim is made for nonuniform `S5` laws.

## Effective-support bound

The assumed conditioned inequality implies that every `X_i` is nonconstant whenever `Delta>0`. A uniform group element induces a uniform coset `gH_i`, so every nonconstant singleton has entropy at least one bit. Thus `H(X_V)>(2/3) sum_i H(X_i)>=20/3` bits. The joint variable is uniform on the `[G:K]` cosets, so `[G:K]^3>2^20`, which requires `[G:K]>=102` since `101^3<2^20<102^3`.

## Excluding S5

Let `G=S5`, of order 120. If `K` is nontrivial, `[G:K]<=60`, already impossible by the preceding bound. If any `H_i=G`, the corresponding variable is constant and the assumed conditioned inequality gives `Delta<=0`. It remains to consider `K={e}` with all `H_i` proper.

Any proper subgroup `H` of `S5` with index `r<5` gives a transitive action on its `r` cosets, hence a homomorphism `S5 -> S_r`. For `r<=4`, `S_r` has no element of order 5, so every 5-cycle lies in the kernel. Using right-to-left permutation composition, the elementary identity `(1 2 3)=(1 3 4 5 2)(1 5 4 3 2)` shows that a 3-cycle lies in the kernel. All 3-cycles are conjugate, and they generate the even permutations: pair transpositions in an even permutation; a pair sharing a point is a 3-cycle, while a disjoint pair satisfies `(1 2)(3 4)=(1 3 2)(1 3 4)` after relabeling. Thus the kernel contains `A5` and the image has at most two elements, so it cannot act transitively on three or four cosets. Indices 3 and 4 do not occur. A subgroup of index two is the kernel of a nontrivial map `S5 -> C2`; all transpositions are conjugate and generate `S5`, so this map is the sign map and its kernel is uniquely `A5`. Therefore every proper subgroup is either `A5` of order 60 or has order at most 24.

Not all ten subgroups can equal `A5`, because their intersection is `{e}`. Hence at least one has order at most 24, and the others have order at most 60. For uniform coset variables, strict positive balance is equivalent by exact logarithm algebra to

\[
\prod_i |H_i|^2 > |G|^{17}|K|^3.
\]

Here the ratio of the left to the right is at most

\[
\frac{(60^9\cdot24)^2}{120^{17}}=\frac{135}{512}<1,
\]

so strict balance is impossible. The two displayed permutation identities were checked by exact permutation composition in the kernel; the R-minus inequality remains subject to its own scientific review.

The earlier bounded numerical `S5` search `frontier-20261028-group-coset-s5-search.py` SHA-256 `2256e16300e0e877f46e48891076ced0ebc74af96457f674f099a0d94fe307bf`, receipt SHA-256 `ca7823b3eea9a10f41fe78619d11eea06794d2ff2760f29b3edf0aef243b3914`, produced no strict incumbent in seven time-limited cases. It is **not** used as a nonexistence proof; the written argument above supplies the result conditional on the pinned R-minus inequality.
