# All-edge extension of the nested-fork four-triangle exclusion

Status: **WRITTEN-checked with separately implemented stdlib Fraction/integer certificate replay**, pending disjoint scientific review and parent disposition. This strictly extends `frontier-20261029-ph7-critical-ten-edge-nested-fork-full-exclusion-v1.md` (SHA256 `2a5b34f04aef1868b3e5346d9c6338b70db40ddbe91f20871e4e51a7744fa64b`) from one fixed ten-edge graph to every graph containing it under the stated cycle restrictions. It is not a general PH7 exclusion.

## 1. Statement

Let `G` be an irreducible seven-state row generator at the critical ratio `z=8/9` (the target pair repeated twice). Suppose its positive transitions **include** the ten edges

`0->1, 0->5, 1->2, 1->3, 2->0, 3->0, 3->4, 4->1, 5->6, 6->0`,

the graph has **no directed two-cycle**, and its directed triangle vertex sets are **exactly** `{0,5,6}`, `{1,3,4}`, `{0,1,3}`, `{0,1,2}`. Any number of further transitions, directed four-cycles, and longer cycles are allowed under those restrictions. Then no such generator exists. The statement is spectral and needs no input/exit vector.

Because the ten listed edges are present and two-cycles are excluded, each listed triangle set carries exactly the orientation used in the ten-edge source; the opposite orientation would require reverse edges.

## 2. Down-closed weight polytope

Use the six rates `u_1,...,u_6` of vertices `0,5,6,1,3,4`, the singleton rate `x` of vertex 2, and the products `P_A,P_B,P_C,P_D` of the ten-edge source. Let `p,q,t` be the row fractions of `0->1`, `1->3`, `3->0`. Other actual row fractions are at most the complementary amounts available at their rows. Hence the actual normalized weights

`alpha=w_A/P_A`, `beta=w_B/P_B`, `gamma=w_C/P_C`, `kappa=K/P_D` with `w_D=x*K`

satisfy, coordinatewise,

`alpha<=1-p`, `beta<=q*(1-t)`, `gamma=p*q*t`, `kappa<=p*(1-q)`.

For instance, `alpha` is the product of fractions on `0->5,5->6,6->0`, and the fraction on `0->5` is at most `1-p`; `kappa` contains the fraction on `1->2`, which is at most `1-q`.

Let `V={v_0,...,v_4}` be the five simplex vertices of the ten-edge source. The vector `(1-p,q(1-t),pqt,p(1-q))` lies in `conv(V)` by multi-affinity. If `0<=y<=x` coordinatewise and `x` lies in `conv(V)`, write `y=lambda∘x`; expanding `prod_i[lambda_i+(1-lambda_i)]` gives `y` as a convex combination of coordinate projections of `x`, and hence of coordinate projections of points of `V`. Every coordinate projection of every `v_i` lies in `V∪{0}`. Therefore the actual weight vector lies in

`P'=conv(v_0,v_1,v_2,v_3,v_4,v_5)`, `v_5=0`.

## 3. Coefficient identities

Exactly as in the ten-edge source, absence of two-cycles and new triangle vertex sets gives

`(A0-K)*x+B0=0`, `h0+x*(h1-K*T)-V4=0`,

with `V4>=0` the sum of all directed four-cycle products, including any new four-cycles. Disjoint triangle pairs and longer cycles do not enter the `y^4,y^3` coefficients. Thus

`Q=81*q_h*(A0-K)`, `H=-243*(A0-K)*V4`

with `Q,H` as defined there. It suffices to prove `Q,H>0` on `P'`; then `q_h>0` forces `A0-K>0`, contradicting `H<=0`.

## 4. Positivity on P'

`Q` is affine in the weights. Its five values at `V` are positive by the ten-edge source, and at `v_5=0` by the one-triple Q lemma at zero triangle weight. Hence `Q>0`.

For fixed `K` and fixed `W=w_A+w_B+w_C`, `H` is affine. An extreme point of `P'` intersected with these two hyperplanes lies in a face of `P'` of dimension at most two. Every such face is the union of triangles whose vertices are vertices of `P'`. It is therefore enough to prove strict copositivity of the quadratic form `H` on the convex hull of every three vertices among `v_0,...,v_5`.

1. **Triples in `{v_0,v_1,v_3,v_4,v_5}`.** Then `K=0`; these points are exactly the five vertices `O,A,B,AB,C` of the relaxed shared-edge polytope after interchanging the two disjoint triangle groups. The polynomial identity `H|_(K=0)=H_shared` holds exactly; the full-polytope positivity is proven in `frontier-20261029-ph7-critical-shared-edge-three-triangle-full-exclusion-v1.md` (SHA256 `a727ddc379f469a18cc7132a702272e570c3acde04ac78f601835c070dc8c4c6`).
2. **Triples containing `v_2` but not `v_5`.** These are the six connector faces proved in the ten-edge source.
3. **Triples containing both `v_2,v_5`.** All edges are strictly positive: `v_5-v_2` because `H` is affine in `K` when the other weights vanish and both endpoints are positive; `v_5-v_0,v_5-v_3,v_5-v_4` by the one-triple lemma; `v_5-v_1` by the two-disjoint-triangle full-square lemma along its diagonal; and the edges `v_2-v_j` by the ten-edge source. A new exact certificate proves `O_25>=0` globally. Thus face `v_2v_4v_5` has at most one negative off-diagonal coefficient (because `O_24>=0`), and strict edge positivity gives copositivity. For `c=0,1,3`, the remaining possibly negative pair is `O_5c,O_c2`; the certificate proves

`O_5c>=0 OR O_c2>=0 OR Z_c:=2*O_25*D_c-O_5c*O_c2 >=0`.

If both are negative, completing the square in the `v_c` barycentric coordinate leaves positive diagonal coefficients `G_5c/(4D_c)`, `G_c2/(4D_c)` from strict edge positivity and nonnegative cross coefficient `Z_c/(2D_c)`. Thus every one of these faces is strictly copositive.

Consequently `H>0` on all of `P'`, proving §1.

## 5. Exact evidence

New primary constructor `frontier-20261029-ph7-nested-fork-down-closure-check.py` SHA256 `3e41fff7da4c4e7fc890cd013d5dee7d5320bc14a00336eaad1333621c77293b` returned PASS and froze `frontier-20261029-ph7-nested-fork-down-closure-certificate-v1.json` SHA256 `c845ca2e2997836bcb9e7e44d678ec64fcb16a0fca7badeab454622673b7e2fc`. Its complete six-rate trees are: `O25>=0` (2,570 leaves); face `v_0v_2v_5` (2,466/108/125); face `v_1v_2v_5` (2,599/204/393); face `v_3v_2v_5` (2,444/169/263), totalling 11,351 leaves.

Separately implemented stdlib `Fraction`/integer replay `frontier-20261029-ph7-nested-fork-down-closure-integer-replay.py` SHA256 `107aa9b195d901ba0c763b28a5e7bee7c4d64f71d0731f1235ab40cef9059b5c` reconstructed all new polynomials and hashes from the definitions in the pinned stdlib nested-fork replay and fully replayed all four selector trees; it returned PASS in 34.61 seconds foreground. It reuses that earlier independent implementation's polynomial arithmetic; it is not disjoint scientific review or formal proof. An earlier exploratory one-face file `frontier-20261029-ph7-nested-fork-zero-face-certificate-v1.json` is superseded for this theorem and is not an input.

## 6. Scope

The theorem requires the actual graph to have exactly these four triangle vertex sets and no two-cycle. It does not cover other four-triangle patterns, any graph with a two-cycle, graphs with five or more triangle sets, actual PH7 existence/exclusion at `8/9`, minimum-state theorems, novelty, formal proof, or parent adoption. All imported one-/two-triangle, unique-connector, shared-edge, and ten-edge certificates remain disjoint-review targets.
