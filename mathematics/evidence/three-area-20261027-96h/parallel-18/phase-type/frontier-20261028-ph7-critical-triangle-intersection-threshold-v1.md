# A necessary fork-threshold for three intersecting triangle sets

Status: **WRITTEN**, conditional on the universal Q/H lemmas and awaiting independent scientific review. This is an all-transition-count spectral restriction at `z=8/9`, not a complete PH7 exclusion.

## Statement

Let `G` be an irreducible seven-state row generator with no directed two-cycle and exactly three directed-triangle vertex sets. Suppose two triangles `A,B` are vertex-disjoint. The third triangle `C` then either uses one vertex of each plus the remaining vertex, or has the form `C={a_i,a_j,b}` with two vertices in `A` and one vertex `b` in `B` (or the same with the groups interchanged).

The first form is excluded by `frontier-20261028-ph7-critical-three-triangle-chain-all-edge-exclusion-v1.md` (SHA256 `d1fef060067dc618f4ba1978c57c65525fde7a350bf038953395552fc4bb7283`). In the second form let the three `A` rates be `a_1,a_2,a_3`, ordered so `A` has directed edges `a_1->a_2->a_3->a_1` and `C={a_1,a_2,b}`. Since there is no two-cycle, `C` has the unique orientation `a_1->a_2->b->a_1`. Let `w_A,w_B,w_C` be the positive directed products. Define

`theta_A=w_A/(a_1*a_2*a_3)`, `theta_B=w_B/(b_1*b_2*b_3)`,

`k_max=(1-theta_A)*(1-theta_B)*a_2*b`.

If the critical double pair exists, the singleton rate `x` satisfies the strict necessary disjunction

`x<a_1 OR x<a_2`.

Equivalently, `x` is smaller than at least one diagonal rate on the shared directed edge. Arbitrarily many four-cycles and longer transitions are allowed, subject to the exact three-triangle/no-two-cycle graph hypotheses.

## Proof

At the fork `a_2`, one outgoing row fraction follows `A` and one follows `C`, so the latter is at most `1-theta_A`; at `b` the analogous fraction is at most `1-theta_B`; and the common edge `a_1->a_2` has rate at most `a_1`. Hence `w_C<=k_max*a_1`.

Set `k=w_C/x`. Suppose `k<=k_max`. Then, exactly as in the all-edge chain manuscript, the six-rate universal polynomials `Q(k),H(k)` are strictly positive by affine interpolation between their `k=0` and `k=k_max` endpoints. At `y^4`, every triangle contributes `w_A+w_B+w_C`, so `(A0-k)*x+B0=0`. Since the hidden `q>0`, `81*q*(A0-k)=Q(k)>0`, hence `A0-k>0`.

At `y^3`, the contribution of `C` is `w_C` times the sum of its four outside diagonal rates. The outside sum is `x+a_3` plus the two `B` rates other than `b`. The chain-form outside sum is `T=a_2+a_3` plus those same two `B` rates. Therefore

`outside(C) = T+x-a_2`.

The chain `y^3` coefficient comparison must account for that difference. In fact

`h0+x*(h1-k*T)-V4 = k*x*(x-a_2)`,

where `V4>=0` is the sum of all directed four-cycle products. Consequently the chain positivity argument yields

`-H(k)/243-(A0-k)*V4=(A0-k)*k*x*(x-a_2)`.

Since the left side is strictly negative and every other displayed factor is positive, `x<a_2` when `k<=k_max`. Thus there is the conditional dichotomy

`w_C>k_max*x  OR  x<a_2`.

The first branch implies `a_1>x`; the second branch is independent. Thus every critical graph with this intersection pattern satisfies the rigorous disjunction

`x<a_1 OR x<a_2`.

The disjunction follows because if `w_C>k_max*x`, comparison with `w_C<=k_max*a_1` gives `x<a_1`; otherwise the coefficient argument gives `x<a_2`. In the equality case `k=k_max` the same strict conclusion holds since `H(k)>0`. The universal Q/H positivity, all-four-cycle sign and graph classification imports retain their named pending status. No unconstrained PH7, ten-edge, novelty, formal proof, independent scientific-review or parent-adoption claim follows.
