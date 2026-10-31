# An open mixed-band family with an exact dual exclusion

Owner InfoSPR7-2, info-2. Actual native clock observed before writing: **Thu Oct 29 16:54:29 PDT 2026**. **WRITTEN theorem candidate with WRITTEN-checked-in-kernel rational dual identities and guards**; not independently reviewed, parent-adopted, formally verified or novelty-cleared. The result is an explicit open region of the previously problematic second-odd-band case, not a universal repair.

## 1. Statement

Let \(\epsilon=10^{-40}\). Independently perturb the six odd-band endpoint roots and five positive squared frequencies by at most \(\epsilon\):
\[
(a,b,c,d,e,f)\approx(1,4,7,13,20,24),\qquad
(t_1,t_2,t_3,t_4,t_5)\approx(2,3,5,6,8). \tag{1}
\]
Set \(O_-=-(t-a)(t-d)(t-e)\), \(O_+=-(t-b)(t-c)(t-f)\); their coefficient difference remains strictly positive in every odd coordinate, so these define an actual independent odd coefficient box. The final node stays strictly inside \((c,d)\), while nodes 1–2 remain inside the first odd band and nodes 3–4 remain in \((b,c)\).

For **every** all-Hurwitz monic septic independent box with exactly this odd box and arbitrary positive even intervals, and every choice of actual members and positive weights at these five nodes, there is no weak odd-canceling/eight-Vieta-vertex no-go, even with infinity and zero-odd atoms. The test polynomial is
\[
F(t)=(-t)(\xi-t)(d-t),\qquad \xi=(t_3+t_4)/2\in(b,c). \tag{2}
\]
It is a convex combination of the two Vieta vertices with middle roots \(b,c\), so strictly positive even pairing with \(F\) excludes a weak no-go.

This 11-parameter neighborhood is nonvacuous, with all seven widths positive: the fixed even box centered at \((363/8,407/4,45/2,1)\) with radius \(1/1000\) remains all-Hurwitz for every perturbed odd box. The same explicit coefficient and marker guards are in `frontier-20261029-open-odd-box-five-node-exclusion-v1.md`, SHA-256 `f9cdddb08d93ded38ea227e3b25a577b5dceb991ab7b3e744d3dec9b626212fd`; that packet's finite nodes differ, but its stability construction depends only on the odd box.

## 2. A strictly interior exact dual at the base point

Let \(S_j\), \(j=1,\ldots,6\), denote the stability-margin linear forms
\[
-E_+(a),\ -E_+(b),\ E_-(c),\ E_-(d),\ -E_+(e),\ -E_+(f),
\]
and \(W_k=u_k-\ell_k\ge0\), \(\ell_k>0\), \(k=0,1,2,3\), for the even coefficient intervals. Odd cancellation has two four-finite-plus-infinity rays X and Y as in `frontier-20261029-fixed-odd-box-mixed-band-five-node-exclusion-v1.md`, SHA-256 `edb459c949f05fa8ea34c348dd28219ca0301312b2472472c1a0a98610a248d4`. At the first, second and final nodes the minimizing odd values are respectively \(O_-\), \(O_+\), \(O_+\). The middle node of each ray has two endpoint choices.

The four base-point mixed-envelope pairing functionals \(g\) satisfy exact identities
\[
g=\sum_{j=1}^6\alpha_jS_j+\sum_{k=0}^3\beta_kW_k+\sum_{k=0}^3\gamma_k\ell_k,\qquad
\alpha_j,\beta_k,\gamma_k>0. \tag{3}
\]
All 56 positive rational multipliers, in the stated generator order, are frozen in `frontier-20261029-mixed-band-strict-duals-frozen-v1.json`, SHA-256 `c8dc14446d0bd35a444759948e737675698feed0856ed98ea96f615d0f5359a3`. The four eight-coefficient identities and all 56 positivity checks were performed exactly with `fractions.Fraction` in one Eval host. Across all four identities, every \(\alpha_j<1\), and every \(\beta_k,\gamma_k\) is at least
\[
10607/234114048>10^{-6}. \tag{4}
\]
Unlike a boundary Farkas certificate, every width and coefficient multiplier is strictly positive; this allows an explicit perturbation argument.

## 3. Persisting the dual identities

Fix the base-point \(\alpha_j\) for each of the four cases. At a perturbed parameter tuple, define the target coefficient vector of \(g\) in the coordinates
\((\ell_0,\ell_1,\ell_2,\ell_3,u_0,u_1,u_2,u_3)\). Subtract \(\sum\alpha_jS_j\). Because the eight forms \((W_0,\ldots,W_3,\ell_0,\ldots,\ell_3)\) form a basis, the new \(\beta_k,\gamma_k\) are uniquely obtained by
\[
\beta_k=\operatorname{coeff}_{u_k}(\text{remainder}),\qquad
\gamma_k=\operatorname{coeff}_{\ell_k}(\text{remainder})+\beta_k. \tag{5}
\]

At the base point every denominator factor in a circuit weight is separated from zero by at least 1; in (1) every such factor has magnitude at least \(4/5\). Every root, node and test-root value has magnitude at most 25, and every relevant linear factor has magnitude at most 50. Each coefficient of \(g\) is a sum of four rational terms whose numerators contain at most six linear factors and denominators seven. The product-telescoping calculation from the named open-gap predecessor gives a per-coefficient change at most
\[
4(60\epsilon50^5+350\epsilon50^{12}).
\]
Each coefficient of each stability form changes by at most \(2000\epsilon\), and \(\sum_j\alpha_j<6\). Therefore every \(\beta_k\) changes by at most
\(12000\epsilon+4(60\epsilon50^5+350\epsilon50^{12})\), and every \(\gamma_k\) by at most twice that amount. Exact arithmetic gives
\[
2\!\left(12000\epsilon+4(60\epsilon50^5+350\epsilon50^{12})\right)
=\frac{85449218750018750003}{1250000000000000000000000000000000000}<10^{-6}. \tag{6}
\]
By (4), every perturbed \(\beta_k,\gamma_k\) remains strictly positive, and the fixed \(\alpha_j\) are positive. Thus (3) continues to hold with strictly positive multipliers for all four endpoint cases.

The mixed-envelope signs also persist: \(F\) is negative at nodes 1–3 for X, negative at nodes 1–2 for Y, and positive at each remaining node. The first two actual even values are negative and the last is positive by root-band separation. Endpoint minimization of actual odd values reduces arbitrary members to the four positive dual cases, as in the predecessor. Each odd circuit therefore has strictly positive even pairing with (2); a positive combination cannot be nonpositive at both defining Vieta vertices. Zero-odd rows can be removed as in the named weak-circuit theorem.

## 4. Limits

This is a neighborhood result for one concrete odd box/node pattern, with a strict mixed-envelope Farkas proof. It does **not** prove the all-box second-band case, eliminate any additional entire phase word, decide larger supports, or settle the original septic interval-box question. Product bounds, reciprocal endpoint minimization, algebraic identity continuation and root-band arguments are written deductions; only the displayed finite dual identities and rational guards were machine-checked in one Eval host. There was no independent scientific review, formal proof, parent adoption or novelty clearance. Process ancestry includes `owner-incidental-held-source-search-display-v1.json`, SHA-256 `dfb30abdebfc8785870e14fdba5d4e55574ded5fafef86647db1eb74d8abd724`; no clean-cognition claim is made.
