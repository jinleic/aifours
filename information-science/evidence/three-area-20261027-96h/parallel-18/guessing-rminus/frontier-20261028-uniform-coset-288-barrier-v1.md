# Uniform group-coset strict gain requires at least 288 effective states

**Status: WRITTEN with two independently replayed exact finite checks, conditional on pinned graph-FD certificates; scientific review and novelty clearance pending.** Let `g` be uniform in a finite group `G`, set `X_i=gH_i` for ten subgroups satisfying the original R-minus FDs, and put `K=intersection_i H_i` and `m=[G:K]`. If the entropy-balance gap `Delta=H(X_V)-(2/3)sum_i H(X_i)` is strictly positive, then

\[
\boxed{m\ge288.}
\]

In particular, no uniform group-coset law on a group of order at most 287 can be a strict R-minus witness. This strengthens `frontier-20261028-uniform-coset-180-barrier-v1.md` SHA-256 `5d815efc88d2ce7c8c11c7f11314c30c78b5c4f335e18c8508adeb7438a20b63`. It does not cover nonuniform coset laws or arbitrary FD laws and is not an unrestricted guessing-number upper bound.

## Necessary index conditions

We use the preceding `180` barrier, itself conditional on the exact proper-subgraph inequality `frontier-20261028-conditioned-proper-subgraph-inequality-v1.md` SHA-256 `c46831b9324e7e8c65009c2a27f3391db7705c370bfb63435a73b0117be3df49` and the exact representable-rank bound `frontier-20261028-linear-ingleton-bound-v1.md` SHA-256 `e056dd9695a4b3e308431441b4f15ec3a2d81f3c733c604cff8246796abf3da4`. Under `Delta>0`, all ten coset indices `d_i=[G:H_i]` are at least 2, at least two are at least 3, and `m^3>product_i d_i^2`.

The conditioned inequality gives another necessary fact: **all index-two subgroups among the `H_i` are distinct**. Otherwise two binary coset variables determine each other, so their mutual information is one bit; inequality `3 Delta + 2 sum_{j!=i} I(X_i;X_j) <= H(X_i)=1` is violated. If `b` vertices have index two, their distinct quotient characters give a binary image of rank at least `ceil(log2(b+1))`. Since `K` lies in the intersection of these kernels, that image order divides `m`. Hence

\[
b\le2^{v_2(m)}-1.\tag{4}
\]

Each `d_i` divides `m`. Also

\[
m\mid \prod_i d_i!.\tag{5}
\]

For (5), let `G` act diagonally on the product of the ten coset spaces. The stabilizer of `(H_1,...,H_10)` is `K`, so its orbit has size `m`; orbit-stabilizer and Lagrange show that `m` divides the order of the action image, which divides `product_i d_i!`. No normality of `K` is required.

Two independently written exact divisor/multiset enumerators check all integers `180<=m<288`, all binary counts `0<=b<=8`, and all possible nonbinary divisors `d_i>=3`, pruning only when the integer product lower bound already fails `m^3>product d_i^2`. There are six product-bound patterns; (5) eliminates five, leaving only

\[
m=192,\qquad (d_1,...,d_{10})\text{ consists of eight 2's and two 3's}.\tag{6}
\]

The two index-three vertices `a,b` must be adjacent by the preceding `175` barrier. The remaining proof excludes (6).

## Necessary character system for m=192

Write `A=H_a`, `B=H_b`, and let `K_2` be the intersection of the eight index-two subgroups. The eight binary characters are distinct and nonzero. Because `a,b` are adjacent, their full-support FDs imply both `K_2∩B <= A` and `K_2∩A <= B`; hence

\[
K_2\cap A=K_2\cap B=K.
\]

Let `phi:G -> G/K_2` be the binary quotient map. Its image is an elementary abelian 2-group. The image of either index-three subgroup is the entire binary quotient: its index there divides both 3 and a power of 2. Therefore `[K_2:K]=3` and `|G/K_2|=192/3=64`, so the eight binary characters span a six-dimensional dual space.

`A` and `B` cannot be equal: their two coset variables would determine one another and violate the conditioned inequality under `Delta>0`. The index `[G:A∩B]` is a multiple of 3, at most 9 by the injective coset-pair map, and divides 192 because `K<=A∩B`. Thus it is 6. As `K_2` is normal and `K_2∩(A∩B)=K`, the subgroup `(A∩B)K_2` has index `6/3=2`. Its image in `G/K_2` is the kernel of a nonzero binary character `s`.

For each binary vertex `i`, the FD becomes a linear-span condition on characters: its character lies in the span of the binary-neighbour characters, with `s` additionally available exactly when `i` neighbours **both** `a` and `b`. Indeed, intersecting binary subgroups corresponds to intersecting character kernels; one ternary subgroup projects onto the whole binary quotient, while `A∩B` projects onto `ker(s)`. The two ternary FDs require `s` to lie in the span of the binary neighbours of `a`, and also in the span of the binary neighbours of `b`. For the converse needed in this derivation, if an element of `B` has the same binary image as an element of `A∩B`, their quotient belongs to `K_2∩B=K<=A`, so the first element is in `A`; the other inclusion is symmetric. Thus all displayed span conditions are necessary for a genuine FD law.

Label the eight binary vertices by basis vectors `e_1,...,e_8` in `F_2^8`. The map sending `e_i` to the corresponding character is onto the six-dimensional dual space and has a two-dimensional kernel `R`. Distinct nonzero characters mean `R` contains no vector of Hamming weight 1 or 2. The nonzero character `s` is a nonzero coset `t+R`. Each FD condition above is therefore an exact subset-span membership test in `F_2^8/R`.

The full exact enumeration checks all **10,795** two-dimensional subspaces of `F_2^8`, retains the **6,769** with no weight-1 or weight-2 vector, and checks all **26** graph edges as the possible `(a,b)`. After the binary-only FD constraints, 42 edge/relation pairs survive; their 254 possible nonzero sign cosets all fail at least one remaining FD span condition. There is **no** character system required by (6). A separately written replay generates relation spaces in row-reduced echelon form and uses explicit spans rather than the producer's relation/coset tests. It checks one representative of each of the five graph edge orbits (sizes `4,8,8,4,2`), their orbit equivalence, and all four raw representatives of each sign coset. It confirms zero solutions.

Thus no `m<288` can satisfy all necessary conditions. This is a finite arithmetic/group obstruction, not a claim that `m=288` is attainable or that a strict FD law exists.

## Evidence pins and limits

* Exact arithmetic producer `frontier-20261028-coset-index-screen.py` SHA-256 `88c5613038bd7d7b31570eeb17e3e5cea709e533df46c847e7625c32518674a5`, receipt SHA-256 `c22c725832df38b9542a9aaf8cb86d4c189878c7779f62650dc601d7b8890fb3`; independent multiset replay `frontier-20261028-coset-index-screen-independent.py` SHA-256 `95338e48f18bbc16e751f29f1939aff1943be67220017127257c6a9b82c6e504`, receipt SHA-256 `a485d72d2c237f40bd6b2561795f2d1bc7edd9945cc929388f815ba2482a6292`.
* Exact character producer `frontier-20261028-coset192-character-enumeration.py` SHA-256 `47f48600164d997f72670eba831a8dfdddc6fb3432b7519ea4bb75be6d34e0c9`, receipt SHA-256 `598e486ee42e05f99768e7bd4fa53278b12dffc7ba1577fe2eb7c02e59cff624`. Independent RREF/span checker `frontier-20261028-coset192-character-independent.py` SHA-256 `fa3b8f56586e5c36c6aa18833ebd97e819cfe845d4a7c5e20d470040e06ab6d7`, receipt SHA-256 `6d191e8a3b33ab09d0a7ad083aeb6eb89047f26648f3883385482a8ca5dfd406`.
* Both replays are finite exact integer checks. The group-action, quotient/span, and entropy deductions above are written mathematics. No proof-assistant formalization, independent scientific review, or broad novelty claim has been made.
