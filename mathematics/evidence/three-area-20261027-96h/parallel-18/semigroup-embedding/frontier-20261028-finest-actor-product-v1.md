# Finest pure actors commute with products, but their quotient lattices need not

**Status: NEW AUTHOR WRITTEN STRUCTURAL DEDUCTION; UNREVIEWED / UNADOPTED.** This combines the finest-actor theorem with the separately unreviewed product syntactic-quotient theorem. It does not infer that arbitrary original sources factor or settle Q1.

## 1. Product row/column partitions

Let S,T be nonempty regular semigroups. Write R_S for the least equivalence containing `(s,su)` and C_S for that containing `(u,su)`, and similarly for T and their direct product. Then

`R_(S×T)=R_S×R_T`,  `C_(S×T)=C_S×C_T`.

Projection of each generating product edge proves the inclusions from left to right. Conversely, if s R_S su and t∈T, choose an inverse t' and put f=t't, so `tf=t` and f is idempotent. The product edge

`(s,t) · (u,f) = (su,t)`

realizes that S-edge without changing t; generated equivalence and symmetry cover an arbitrary R_S-chain. To realize a T-edge while fixing s, choose an idempotent e with se=s. Thus the reverse inclusion holds. For C, use left local identities `ss'` and `tt'` and the dual product edges. No global identity in either factor is required. □

## 2. Finest actor of a product

Assume the actual syntactic quotients of S,T are pure and completely simple. The product theorem `frontier-20261028-two-actor-product-factorization-v1.md`, SHA `341e2495c8f7dbbee3729c6f0f195e2013c4e373bb9e86278894c461982f517a`, asserts and derives at its named scope that the product actual quotient is `q_S×q_T`; verify that dependency independently. The finest-actor theorem `frontier-20261028-finest-pure-cs-actor-v1.md`, SHA `772cf39e2d5c6aab1c127ed73edaf3e7c2e617deda8f3113b8059df19f4c83ab`, then gives

`q̂_(S×T) ≅ q̂_S × q̂_T`

as maps from S×T: §1 gives product rows and columns, the q group is the product group, and every finest-actor sandwich entry is the componentwise product of the two q sandwich entries. This conclusion is conditional on both named predecessor proofs, not inferred from matching finite sizes.

In particular, since the identity on a CS semigroup D is a pure CS quotient and hence its own finest pure actor, the family `S68×D` from `frontier-20261028-quotient68-cs-factor-family-v1.md`, SHA `bc8cab96779aed3b3072fc8fc17a5373064d1d822519d04faa12965e8ee5db3f`, has finest actor `D₁₂×D` under these named imports, for finite or infinite D.

## 3. Quotient lattices can have entangled partitions

The lattice of pure CS quotients of a product is NOT in general the direct product of the quotient lattices of the factors. For example let S=T be the two-element left-zero band. Both actual q are the one-element semigroup, their finest actors are the two-element bands, and each factor has Bell(2)=2 pure-CS quotient kernels. Their product is the four-element left-zero band, with a one-element actual q and four refined rows; every partition of those four rows gives a pure CS quotient. There are Bell(4)=15 such kernels, not 2·2=4. Most merge product rows in non-coordinatewise ways.

The product actor assertion and this warning do not assert that band-factor minima multiply: source embeddings into products give only the usual product upper bound, and actor refinement and band coarsening can trade off as already shown by S68. All calculations and named source results remain unreviewed; no formal verification or novelty is claimed.
