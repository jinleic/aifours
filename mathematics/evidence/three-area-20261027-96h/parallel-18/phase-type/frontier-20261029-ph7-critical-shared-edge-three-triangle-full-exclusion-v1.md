# Complete all-edge exclusion for the shared-edge three-triangle case

Status: **WRITTEN-checked with separately implemented exact Fraction/integer certificate replay**, awaiting disjoint scientific review and parent disposition. This completes the corrected moment program in `frontier-20261029-ph7-critical-shared-edge-exact-moment-reduction-v1.md` (SHA256 `e27b2028bc9dbf043fe44aa20fc17a5f3cf2661431584a3dc4a717bc27c25352`), whose mandatory erratum `frontier-20261029-ph7-critical-shared-edge-exact-moment-reduction-v1-erratum-1.md` (SHA256 `b6c05cbfc71ae190a9310c0b5aa7409ba4ffa710e8e6ed12c0b99a497dad26f8`) corrects the previously misstated elimination polynomial. This manuscript uses **only the corrected identity**.

## 1. Theorem and consequence

There is no irreducible seven-state row generator with the critical double pair at `z=8/9`, no directed two-cycle, and exactly three directed triangle vertex sets consisting of two disjoint triples `A,B` and a third triple sharing one directed edge with one of them. Arbitrarily many other transitions, directed four-cycles and longer cycles are allowed so long as no additional triangle or two-cycle is introduced.

Together with the separately pending disjoint-pair theorem and all-edge connector-triangle exclusion, this implies: every critical no-two-cycle seven-state generator has **at least four distinct directed triangle vertex sets**. Thus, under the separately supported PH irreducibility/Perron normalization, a critical PH representation on at most seven states must either contain a directed two-cycle or have at least four triangle vertex sets. Neither consequence excludes graphs with four or more triangles or any graph with a two-cycle.

## 2. Full coefficient reduction

Normalize `d=1`. Label `A={u_1,u_2,u_3}`, `B={u_4,u_5,u_6}` with directed `A` edges `u_1->u_2->u_3->u_1`, and third triangle `C={u_1,u_2,u_4}` oriented `u_1->u_2->u_4->u_1`. This orientation is forced by the shared edge and absence of two-cycles. Let `x` be the singleton escape rate, and let `w_A,w_B,w_C>0` be actual triangle products. Put

`P_A=u_1*u_2*u_3`, `P_B=u_4*u_5*u_6`, `P_C=u_1*u_2*u_4`,

`alpha=w_A/P_A`, `beta=w_B/P_B`, `gamma=w_C/P_C`.

At the fork `u_2`, the `A` and `C` outgoing fractions sum to at most one, while `alpha` is no larger than the `A` fork fraction and `gamma` no larger than the `C` fork fraction. Similarly, at `u_4`, the `B` and `C` outgoing fractions sum to at most one. Thus the true normalized weight vector lies in the **relaxed polytope**

`alpha,beta,gamma>=0`, `alpha+gamma<=1`, `beta+gamma<=1`.      (POLY)

This intentionally enlarges the actual product-coupled domain; no independence assumption is made.

Let `f_j` be elementary symmetric sums of `u_1,...,u_6`, and define `A0,B0,h0,h1,T` exactly as in the corrected source:

`A0=f_2-4*f_1+74/9`,

`B0=f_3-4*f_2+(74/9)*f_1-28/3-w_A-w_B`,

`h0=f_4-(70/9)*f_2+(212/9)*f_1-1007/27-w_A*(u_4+u_5+u_6)-w_B*(u_1+u_2+u_3)`,

`h1=f_3-(70/9)*f_1+212/9-w_A-w_B`, `T=u_3+u_5+u_6`.

The actual characteristic quotient `y^2+p*y+q` has `q>0`. Its `y^4` and `y^3` coefficients, retaining every directed four-cycle product in `V4>=0`, give

`A0*x+B0-w_C=0`, `h0+x*h1-w_C*(x+T)-V4=0`.

Set

`Q=81*[A0^2-(f_1-4)*(B0-w_C)]`,

`H=-243*[A0*(h0-w_C*T)+(w_C-B0)*(h1-w_C)]`.

The **corrected** exact identities, without any division, are

`Q=81*q*A0`, `H=-243*A0*V4`.                              (ID)

Section 3 proves `Q,H>0` for the whole relaxed polytope. Since `q>0`, `Q>0` forces `A0>0`; the second identity then yields `H<=0`, contradiction.

## 3. Positivity by a five-vertex polytope and three certified edges

(POLY) is the convex hull of the five vertices

`O=(0,0,0), A=(1,0,0), B=(0,1,0), AB=(1,1,0), C=(0,0,1)`.

For fixed positive rates, `Q` is affine in `(alpha,beta,gamma)`. Its values at `O,A,B,C` are strictly positive by the earlier one-triple universal Q/H lemma in `frontier-20261028-ph7-critical-two-triangle-vertex-sets-v1.md` (SHA256 `b08ddcaca076342c98089bef3592475c1698b8ee7762b0617111e4eaf7ce6793`), after permuting rates for vertex C. Its value at `AB` is strictly positive by the two-disjoint-triangle universal Q/H lemma in `frontier-20261028-ph7-critical-two-disjoint-triangle-full-exclusion-v1.md` (SHA256 `0489ce341fa98eb779f54f58926773943a827662f66bcd97619c28e52b9d040e`). Thus `Q>0` throughout the polytope.

For `H`, let `W=w_A+w_B+w_C`. Exact expansion shows its Hessian in `(w_A,w_B,w_C)` is the rank-one matrix with **every entry 486**. Thus, for fixed total `W`, `H` is affine in the weight vector. Any nonempty intersection of(POLY) with a plane `W=constant` is a compact polygon; a minimum of an affine function is attained at one of its vertices. Each polygon vertex is either an original polytope vertex or lies on a polytope edge; an edge lying inside the plane needs only its endpoints. It is therefore enough to prove `H>0` along **every** polytope edge.

The edges in the face `gamma=0` are covered by the full-square two-triangle lemma. Edge `O-C` is covered by the one-triple lemma after rate permutation. The only remaining edges are `A-C`, `B-C`, and `AB-C`. On each, write `H(t)=H0(1-t)^2+2H1*t*(1-t)+H2*t^2`. Both endpoints `H0,H2` are strictly positive by the named one-/two-triangle lemmas. The new exact six-rate dual certificates in §4 prove everywhere either `H1>=0` or `H0*H2-H1^2>0`; both alternatives imply `H(t)>0` for the entire closed edge. This establishes `H>0` on the full three-dimensional polytope.

## 4. Exact certificate and independent-code replay

Primary constructor `frontier-20261029-ph7-shared-edge-polytope-H-check.py` SHA256 `ab89faaef99cc109f56a68bead6b36886381a9c8829460b491c4691dad57a151` generated `frontier-20261029-ph7-shared-edge-polytope-H-certificate-v1.json` SHA256 `b55f0bb26fffd99535ba7bb270568a1f6ff3609b45883c8ffd50e5c2661c0418`. Six-rate integer Bernstein dual covers have the following full selector-leaf counts:

* `A-C`: 2,649 nonnegative-middle / 210 strictly positive-Gram.
* `B-C`: 2,815 / 576.
* `AB-C`: 2,916 / 589.

Separately implemented stdlib `Fraction`/integer replay `frontier-20261029-ph7-shared-edge-polytope-H-integer-replay.py` SHA256 `31cb0a8dbc49081feb0280a1b16799d2584c3b4afd4a173bf415a90691fa189a` returned PASS after independently reconstructing all six polynomials and hashes, checking all complete prefix unions and integer coefficient signs, and requiring strict positivity at every admissible interior vertex for Gram leaves. This is independent code by the same owner, not disjoint scientific review or formal verification. The already pinned one-/two-triangle endpoint certificates remain explicit inputs.

## 5. Scope and review boundary

The all-no-two-cycle four-triangle corollary additionally imports `frontier-20261028-ph7-no-two-cycle-disjoint-triangles-v1.md` (SHA256 `7306b0cc0eeca0f78c75c1867f99b4675e169da2fdfada82c5c0f5175eb97ddf`) and `frontier-20261028-ph7-critical-three-triangle-chain-all-edge-exclusion-v1.md` (SHA256 `d1fef060067dc618f4ba1978c57c65525fde7a350bf038953395552fc4bb7283`). All remain unadopted pending review. A disjoint audit should check the row-fraction polytope, all cycle/4-cycle coefficients and corrected identities, the fixed-W face-to-edge reduction, all three dual union/strictness covers, endpoint imports, and the actual PH caller.

No general graph with a directed two-cycle, no graph with four or more triangle vertex sets, no unrestricted PH7/PH8 existence verdict, minimum-state claim, novelty, formal proof, or parent adoption is asserted.
