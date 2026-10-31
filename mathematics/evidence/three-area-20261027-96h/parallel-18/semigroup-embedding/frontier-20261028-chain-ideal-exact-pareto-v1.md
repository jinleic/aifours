# Exact actor–band Pareto curve for a two-parameter original-class family

**Status: NEW AUTHOR WRITTEN FAMILY and finite table controls; UNREVIEWED / UNADOPTED.** This makes the optimization in `frontier-20261028-ideal-gluing-band-optimum-v1.md`, SHA `3e5a9fa811840bc815fcd1a6f75292a61c03244c73aaf5c04e89886de434b4fc`, exact for every source actor image. It does not solve general Q1.

## 1. Source and theorem

Let k,m≥2. Let L be k disjoint chains of length m joined at a common bottom 0, and let A_i be the i-th chain. The source

`S_(k,m)={(i,x):x∈A_i}`, `(i,x)(j,y)=(i,x∧y)`

has km elements and is a left normal band, hence an original-class regular weakly-E locally-r semigroup. Each onto CS homomorphic image is a left-zero band obtained by partitioning the k chain indices. For a partition Π of those indices let a=|Π| and `r=max_(C∈Π)|C|`.

**Theorem.** The minimum band cardinality of a faithful physical host whose actor map identifies chain indices exactly by Π is

`k(m−1)+r`.                                               (1)

Hence, when only the actor-image size a is fixed, the exact optimum is

`b_min(a)=k(m−1)+ceil(k/a)`,       1≤a≤k.                    (2)

The exact nondominated pairs among `(a,b_min(a))` form the actor-image/band Pareto frontier. The smallest band has `k(m−1)+1` elements at a=k, while the smallest **whole host** has km elements at a=1 and band km. A larger ambient CS actor never improves these factor minima: restricting it to the source actor image preserves the same band after the explicit row gauge from the predecessor.

## 2. Direct lower bound

All S elements are idempotent. Within a chain fibre they commute, so under any CS actor map they have the same actor idempotent d_i. As shown in the predecessor, these d_i form a left-zero band. Thus every onto CS image is left-zero, with i,j identified precisely when d_i=d_j, and every partition is possible.

For any faithful ambient host, the predecessor's row normalization gives injective coefficient maps b_i with

`b_i(x)b_j(y)=b_i(x∧y)`.

If coefficients b_i(x),b_j(y) agree, this equation in both directions forces x=y by fibrewise injectivity. For nonzero x, each x belongs to exactly one chain, so all k(m−1) nonzero coefficients are distinct and cannot equal a coefficient representing 0. Among indices in a fixed Π-block C, the actor values are equal; faithfulness makes the |C| zero coefficients pairwise distinct. Therefore at least r zero coefficients are required, proving (1)'s lower bound. No restriction on B or the ambient actor's group action is used.

## 3. Matching globally normal host

Choose labels ℓ_i∈{1,…,r} injective within each Π-block; different blocks may reuse labels. Define B as r zero labels `z_1,...,z_r` plus one element b_(i,x) for every nonzero x∈A_i. Its multiplication is

`z_p z_q=z_p`, `z_p b_(j,y)=z_p`, `b_(i,x) z_q=z_(ℓ_i)`,

and `b_(i,x)b_(j,y)=b_(i,x∧y)` if i=j, while it is `z_(ℓ_i)` if i≠j. This B is a subband of `LZ_r×L`: represent z_p by (p,0) and b_(i,x) by (ℓ_i,x). Hence B is a normal band and satisfies every required local-r/SN identity. Map `(i,0)` to band coefficient `z_(ℓ_i)` and `(i,x≠0)` to b_(i,x); use the Π-block as left-zero actor, with trivial group. All products and injectivity follow directly, achieving (1).

Among partitions with a blocks, the least possible maximum blocksize is ceil(k/a), attained by balanced partitions. This gives (2), including every integer a. Whole host size is `a[k(m−1)+ceil(k/a)]`; it is at least km by injectivity and equals km at a=1. For k,m≥2 and a>1 it is strictly larger, since `a k(m−1)+k > km`. Thus the singleton actor is uniquely optimal in actor-image size for the whole cardinality, despite being worst for the band cardinality.

## 4. Exact finite controls and scope

`frontier-20261028-chain-ideal-pareto-checker-v1.py`, SHA `75ff027d209af03868716ec133710e6fac3128a8a608a50bc7dd22044ef347f2`, executed in the Python eval kernel before Wed Oct 28 22:57:58 PDT 2026. It enumerates EVERY partition for (k,m)=(2,2),(3,2),(4,3),(5,2), constructs the displayed band/actor maps, exhausts associativity and normal identities, source products and injectivity, and verifies the observed minima match (2). It does not use a solver, but the universal lower bound is the written argument rather than finite sampling.

The example has all source idempotents and a globally normal band host; it is not an unresolved nonorthodox original source. Its role is a sharp exact obstruction to optimizing only the largest pure-actor fibre, and an explicit actor/band tradeoff. No novelty, formal verification or independent mathematical review is claimed.
