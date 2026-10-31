# Complete critical spectral exclusion of the length-six connector

Status: **WRITTEN with imported exact integer-replayed certificates**, pending independent mathematical review and parent disposition. This is a complete exclusion of both length-six connector shapes inside the two-disjoint-triangle nine-transition template at `z=8/9`. It does **not** exclude connector lengths 3, 4, or 5, any ten-or-more-transition graph, or PH7 as a whole. It makes no new PH6, novelty, formal-verification, or adoption claim.

## 1. Statement and imports

There is no seven-state row generator whose graph consists of two disjoint directed triangles and a singleton with a length-six connector cycle and whose spectrum contains the target pair `-d +/- ib` twice when `d>0` and `b^2/d^2=8/9`.

The proof uses these earlier written results at their present, not yet independently adopted, cuts:

* The all-rate high-Perron/singleton theorem `frontier-20261028-ph7-nine-edge-length-six-high-rate-theorem-v1.md` (SHA256 `ecf238ccecf36369a614287579a19d6090a4093b6dbe760504d2ea408562da39`). It includes the exact amplification certificate, independently implemented integer replay, the three-state sector lemma, and the joint Perron gap as explicit dependencies.
* The critical triangle-imbalance capacity theorem `frontier-20261028-ph7-critical-triangle-imbalance-capacity-v1.md` (SHA256 `c2c95deebfaa048072704da11126636d19b166c60a3cc7f41a266927716dc409`), including its exact six-rate mixed-domain/copotential Bernstein proof and replay.
* The elementary omitted-block Perron squeeze `r_B+t<2d` in `frontier-20261028-ph7-nine-edge-length-six-block-root-exclusion-v1.md` (SHA256 `e0e54e74609827f881ae07bb8bc80d712e4478e9f808eeb64455ce187a6ab2dd`), also derived in the joint-gap proof.

The mathematical reduction below is an exact elementary product inequality; no selected rates, optimization, or newly generated numerical search is used as a premise.

## 2. High-rate and triangle-weight consequences

Scale `d=1` and put `tau=17/9`. Call `A` the triangle fully visited by the connector, with diagonal rates `a_1,a_2,a_3` and Perron decay `r_A`; call `B` the triangle with one omitted vertex of rate `t`, and call the singleton diagonal rate `x`.

The imported high-rate theorem gives

`x>tau`, `r_A>tau`, `a_i>r_A`, and `max(x,r_A)>1+10*sqrt(2)/9>5/2`.

The omitted-block Perron squeeze gives `t<2`. Let `w_A,w_B` be the two directed triangle edge products. The graph has no two-cycles and its only directed triangles are `A,B`. Its geometric-mean symmetrization is therefore the diagonal matrix with the seven negative diagonal rates, and the total triangle imbalance is exactly `W=w_A+w_B`.

Because `-tau` lies strictly to the right of every eigenvalue of the substochastic triangle `A`, its characteristic polynomial is positive there. Thus

`w_A < (a_1-tau)*(a_2-tau)*(a_3-tau) =: Delta_A`.

Indeed the triangle polynomial at `y=-tau` is the displayed product minus `w_A`. Row conservation also gives

`w_B < b_1*b_2*b_3 =: D_B`,

since the unique `B` connector fork has two positive outgoing transitions. All displayed rates and products are positive.

## 3. The product domination

Let `M` be the product of the **three largest** of the seven diagonal rates, and define

`g=max(x,a_1,a_2,a_3)`, `F=product of the three largest of {x,a_1,a_2,a_3}`.

Then `g>5/2` and `F<=M`. Since `F>=a_1*a_2*a_3` and every `a_i<=g`,

`Delta_A/M <= Delta_A/F <= prod_i(1-tau/a_i) <= (1-tau/g)^3`.

Order the three `B` rates as `b_min<=b_mid<=b_max`. Since one of them is `t<2`, `b_min<2`. The three rates `g,b_mid,b_max` belong to distinct vertices, so `M>=g*b_mid*b_max`. Hence

`D_B/M <= b_min/g < 2/g`.

Finally, for every `g>=5/2`,

`(1-tau/g)^3+2/g < 1`.

To see this without approximation, its left side minus one is `p(g)/g^3`, where

`p(g)=-(2673*g^2-7803*g+4913)/729`.

Here `p(5/2)=-8447/2916`, `p'(5/2)=-206/27`, and `p''(g)<0`, so `p(g)<0` throughout the stated range. Consequently

`W/M < Delta_A/M + D_B/M < 1`.

## 4. Contradiction and exact scope

The graph is strongly connected and the row generator has spectral bound zero. Its characteristic polynomial contains `y*((y+1)^2+8/9)^2`; its remaining quadratic has positive constant coefficient by Metzler stability. The imported critical capacity theorem therefore gives `W>M`, contradicting §3. This rules out the length-six spectral graph, before any input/exit matching.

On the separately **pending** universal nine-transition graph-template theorem, the two length-six connector choices are thus impossible; the earlier Hamiltonian result eliminates the one length-seven choice. That conditional combination leaves the six connector parameter choices of lengths 3, 4, and 5 and does not exclude them. Applying the reduction to all nine-transition critical PH7 representations additionally requires the pending capacity/overlap-budget/template chain and the separately supported irreducibility/Perron-normalization caller.

The present proof is a written conditional composition of named results and exact replayed certificates. The independent code replay establishes the certificate's stated polynomial signs and cover; it is not independent scientific review of these callers, a formal proof, original PH7 existence/exclusion, a ten-edge theorem, novelty, or parent adoption.
