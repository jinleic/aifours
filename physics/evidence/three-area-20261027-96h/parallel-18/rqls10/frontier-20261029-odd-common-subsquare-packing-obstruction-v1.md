# The disjoint common-block OLS10 construction reaches at most 13 rays

**WRITTEN AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date` before discovery: **Thu Oct 29 00:10:43 PDT 2026**. This sharply closes the specific constructive route in `frontier-20261029-ols-disjoint-block-quantum-extension-v1.md` SHA **3d9eb442e897bea98fb80e1f886955abb925df95820507c8ee0b6ee9e27e1a30**, not all ways of constructing 1RQLS10.

## Theorem

An orthogonal Latin pair of order N with a proper common subsquare of order k satisfies `N>=3k`. If it has two common subsquares of orders k,l with disjoint row sets, disjoint column sets AND disjoint color-symbol sets (in either one of the Latin squares), then

`(N-k-l)^2 >= 2kl`.                                                  (1)

Consequently the proper disjoint-block construction in the cited packet produces at most **13 distinct rays** in order10. The existing exact 13-ray witness attains this bound.

## Single-block inequality N>=3k

Write R,C,S,T for the block rows, columns, A-symbols and L-symbols. Outside the k×k block, every occurrence of a symbol in S must lie in the `(N-k)×(N-k)` bottom-right complement: each block row and each block column already contains that symbol once. There are `k(N-k)` such occurrences. Likewise there are `k(N-k)` occurrences of L-symbols in T in this complement. These two sets of cells are disjoint: all `k²` ordered pairs S×T already occur in the block because A and L are orthogonal there. Thus `(N-k)²>=2k(N-k)`, and properness gives `N>=3k`.

## Two-block inequality

For disjoint blocks of sizes k,l, write their A-symbol sets S,U and L-symbol sets T,V. Orthogonality gives exactly kl cells with `(A,L) in S×V` and kl with `(A,L) in U×T`. Every one of these cells lies outside BOTH blocks' rows and BOTH blocks' columns, because each specified symbol is already used once inside the corresponding block in every block row and column. If S,U are disjoint, the two kl-cell sets are disjoint; the same holds if T,V are disjoint. The common complement has `(N-k-l)²` cells, proving (1).

At N=10, the first inequality gives every proper block size at most3. Two disjoint 3-blocks with disjoint A-symbol sets would require `4²>=18`, false. A common 2-block is impossible because its restrictions would give an orthogonal pair of Latin squares of order2; order1 blocks add no new ray. Hence at most one nontrivial 3-block can occur.

Every QLS3 is classical up to a common unitary and cell phases, by an elementary argument. Fix its first row as `e1,e2,e3`. The second-row vectors have forms `v1=(0,a,b)`, `v2=(c,0,d)`, `v3=(e,f,0)`. Their pairwise inner products require `b̄d=āf=c̄e=0`. If b is nonzero, these equations force `v2~e1`, `v3~e2`, `v1~e3`; if b=0, they force `v1~e2`, `v3~e1`, `v2~e3`. The final row is then forced by the columns. Thus the local block introduces at most three new rays beyond the original ten. A valid 13-ray instance exists in the cited extension packet, so the bound is sharp within this construction.

This result does not rule out overlapping blocks, different replacement schemes, nonclassical resolution labels, or arbitrary 1RQLS10s. The two-block inequality requires the disjoint-symbol hypothesis; without it the universally valid weaker bound is `(N-k-l)²>=kl`. Independent review requested.
