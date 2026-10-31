# A cross-Perron rate inequality for two disjoint critical triangles

Status: **WRITTEN**, awaiting independent mathematical review. This is an all-rate necessary consequence of the separately written critical triangle-imbalance capacity theorem, not a complete graph-family or PH7 exclusion. It applies beyond nine transitions whenever the stated graph hypotheses hold.

## 1. Statement

Let `G` be an irreducible seven-state row generator with no directed two-cycle, and suppose its only directed triangle vertex sets are two disjoint triples `A,B`. Let the remaining vertex have diagonal rate `x`; write the positive triangle diagonal rates as `a_1,a_2,a_3` and `b_1,b_2,b_3`. Let `-rho_A,-rho_B` be the Perron eigenvalues of the respective induced 3-by-3 triangle subgenerators, retaining their full diagonal rates. If the spectrum contains `-d +/- ib` twice with `b^2/d^2=8/9`, then, with

`g_A=max(x,a_1,a_2,a_3)`, `g_B=max(x,b_1,b_2,b_3)`,

one necessarily has

`min_i b_i > 3*rho_A - 3*rho_A^2/g_A + rho_A^3/g_A^2`,

`min_i a_i > 3*rho_B - 3*rho_B^2/g_B + rho_B^3/g_B^2`.

In particular both isolated-triangle Perron decays are **strictly smaller than every one of the six triangle diagonal rates**. This need not hold for arbitrary irreducible generators; it is a necessary consequence of the repeated critical spectrum and the specified two-triangle graph.

## 2. Proof

The induced triangle `A` is an irreducible Metzler subgenerator with at least one strict leak row, because the full seven-state graph is irreducible. Therefore `rho_A>0`. If `w_A` is its positive oriented cycle product, its polynomial is

`C_A(y)=prod_i(y+a_i)-w_A`.

A positive Perron eigenvector gives `rho_A<min_i a_i`, and `C_A(-rho_A)=0` gives the exact identity

`w_A=prod_i(a_i-rho_A)`.

Analogous statements hold for `B`. Since the graph has no two-cycles and no other triangle vertex sets, the symmetric geometric-mean matrix is diagonal and total triangle imbalance equals `W=w_A+w_B`. The critical capacity theorem in `frontier-20261028-ph7-critical-triangle-imbalance-capacity-v1.md` (SHA256 `c2c95deebfaa048072704da11126636d19b166c60a3cc7f41a266927716dc409`) therefore gives

`W > M`, where `M` is the product of the three largest diagonal rates of all seven vertices.

Let `b_min<=b_mid<=b_max` be the sorted rates of `B`, and let `F` be the product of the largest three rates among `x,a_1,a_2,a_3`. Since `F>=a_1*a_2*a_3`, `M>=F`, and all `a_i<=g_A`,

`w_A/M <= prod_i(1-rho_A/a_i) <= (1-rho_A/g_A)^3`.

The rate `g_A` belongs to a vertex outside `B`, so `M>=g_A*b_mid*b_max`. Every transition in `B` is bounded by its row's diagonal rate; hence `w_B<=b_min*b_mid*b_max` and

`w_B/M <= b_min/g_A`.

Since `W/M>1`, combining the two bounds and expanding gives

`b_min > g_A*[1-(1-rho_A/g_A)^3] = 3*rho_A-3*rho_A^2/g_A+rho_A^3/g_A^2`.

All factors are positive and `0<rho_A/g_A<1`, so the right side equals `rho_A*[1+(1-rho_A/g_A)+(1-rho_A/g_A)^2]` and is strictly greater than `rho_A`. Interchange `A,B` to obtain the second inequality. □

The imported capacity theorem depends on its independently replayed six-rate mixed-domain Bernstein certificate and still requires its own scientific audit/adoption. This paper adds only the exact product/Perron argument, not a formal verification, new unrestricted PH6 result, global 8/9 decision, or novelty claim.
