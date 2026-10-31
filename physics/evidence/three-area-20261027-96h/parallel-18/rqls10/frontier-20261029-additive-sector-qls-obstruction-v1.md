# An additive-sector obstruction for arbitrary QLSs

**WRITTEN AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date`: **Thu Oct 29 00:05:11 PDT 2026**. This is an original-order structural no-go broader than an array-level tensor product; it does not exclude arbitrary QLS10.

## Theorem

Let G be a finite abelian group, let `N=n |G|`, and let `H = direct_sum_(s in G) H_s` with every sector `dim H_s=n`. Suppose an order-N QLS has every cell ray lying in the sector

`H_(alpha(r)+beta(c))`,

for arbitrary maps from rows and columns to G. Let `Sigma_G=sum_(g in G) g`. If `n Sigma_G != 0` in G, the QLS has NO orthogonal transversal, regardless of ray multiplicities or the vectors' form within each sector.

## Proof

For a fixed row, its N orthonormal rays split among |G| mutually orthogonal n-dimensional sectors, so each sector occurs exactly n times. Consequently beta takes every group value n times; similarly alpha does. A hypothetical transversal is another orthonormal basis, so each sector occurs exactly n times among its selected cells. Summing sector labels over the transversal gives

`n Sigma_G = sum_r alpha(r) + sum_c beta(c) = 2 n Sigma_G`.

Hence `n Sigma_G=0`, contradicting the hypothesis. This uses only dimension and the additive sector pattern: individual rays within a sector may vary arbitrarily and need not themselves factor into QLS arrays.

## Original order10

Take two orthogonal five-dimensional sectors H0,H1 and G=Z2. If every ray lies in `H_(alpha(r) xor beta(c))`, the row and column ONBs force alpha and beta each to have five zeros and five ones; any transversal ONB would have five rays in H1, but summing the XOR labels along a transversal gives 5+5=0 mod2, contradiction. Thus such an order10 QLS is never 1-resolvable. Unlike the 5×2 tensor-array exclusion, this condition does not itself bound the ray count by50; it allows arbitrary rays within both sectors.

For finite abelian G, `Sigma_G` is the unique nonzero involution if G has exactly one, and is zero otherwise. Thus every odd n and every such G gives an obstruction. The no-T condition applies after any global unitary or row/column permutation. It does NOT rule out arbitrary separable vectors, non-additive sector patterns, mixed-sector rays, or general QLS10. This elementary written result needs independent review.
