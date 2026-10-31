# Complete critical exclusion of exactly two disjoint triangles without two-cycles

Status: **WRITTEN-checked with independently implemented stdlib integer certificate replay**, awaiting disjoint scientific review and parent disposition. This is an all-transition-count spectral exclusion at `z=8/9`: directed four-cycles and arbitrarily many longer cycles are allowed. It does **not** settle the remaining three-triangle graph or unrestricted PH7.

## 1. Theorem and consequences

There is no irreducible seven-state row generator with the critical double pair `-d +/- ib`, `b^2/d^2=8/9`, whose graph has no directed two-cycles and has exactly two directed-triangle vertex sets, both disjoint.

This is a characteristic-polynomial result and needs no PH input/exit matching. Conditioned on the separately pending nine-transition graph-template theorem, it excludes **eight** of its nine connector parameter choices: all connector lengths 4, 5, 6, and 7. The sole remaining nine-edge template is the length-three connector: two disjoint directed triangles and a third triangle through one vertex of each and the singleton. That remaining graph is not excluded here.

Also, conditional on `frontier-20261028-ph7-no-two-cycle-disjoint-triangles-v1.md` (SHA256 `7306b0cc0eeca0f78c75c1867f99b4675e169da2fdfada82c5c0f5175eb97ddf`), every critical row generator without a two-cycle must have **at least three** directed-triangle vertex sets. Neither implication says anything about critical graphs containing two-cycles.

## 2. Exact coefficient reduction

Scale `d=1`. Let the two triangle triples be `A,B`, with six positive diagonal rates `u_1,...,u_6`, and let the seventh diagonal rate be `x>0`. Denote by `f_j` the elementary symmetric sum of order `j` in those six rates. Since there are no two-cycles, each triangle has only one orientation. Its positive edge product can be written

`w_A=theta_A*u_1*u_2*u_3`, `w_B=theta_B*u_4*u_5*u_6`, `0<=theta_A,theta_B<=1`.

The inequalities follow from the nonnegative row-generator ties; no minimality or special rates are assumed. Let `W=w_A+w_B` and put

`A0=f_2-4*f_1+74/9`,

`B0=f_3-4*f_2+(74/9)*f_1-28/3-W`,

`h0=f_4-(70/9)*f_2+(212/9)*f_1-1007/27-w_A*(u_4+u_5+u_6)-w_B*(u_1+u_2+u_3)`,

`h1=f_3-(70/9)*f_1+212/9-W`,

`Qpol=81*[A0^2-(f_1-4)*B0]`, `Hpol=-243*[h0*A0-h1*B0]`.

The universal lemma in §3 proves `Qpol>0` and `Hpol>0` for **all six positive rates** and all `theta_A,theta_B` in the closed unit square.

The characteristic polynomial is `D(y)*(y^2+p*y+q)`, with `D(y)=y*((y+1)^2+8/9)^2` and `q>0` by irreducible row-generator stability. Compare the `y^4` coefficient: the only directed 3-cycles are `A,B`, so

`A0*x+B0=0`.                                                     (E4)

The `y^3` coefficient includes the same triangle terms and a subtraction for every directed 4-cycle. Let `V4>=0` be the sum of all directed 4-cycle transition products, including cycles through the singleton. There are no disjoint two-cycle products. The exact residual is

`h0+x*h1-V4=0`.                                                  (E3)

The hidden constant satisfies `q=A0+x*(f_1-4)`. Multiplying by `A0` and using(E4) yields `81*q*A0=Qpol>0`; because `q>0`, necessarily `A0>0`. Multiplying(E3) by `A0` and again using(E4) gives

`0=h0*A0-h1*B0-A0*V4 = -Hpol/243-A0*V4 < 0`,

a contradiction. This retains **every** directed 4-cycle with the correct sign; longer cycles cannot enter these two coefficients.

## 3. Universal two-triangle Q/H lemma

For fixed rates, `Qpol` is affine in `(theta_A,theta_B)`, so its strict positivity on the square follows from its four corners. The three corners with at least one zero coefficient are covered by the earlier one-triple universal lemma in §5 of `frontier-20261028-ph7-critical-two-triangle-vertex-sets-v1.md` (SHA256 `b08ddcaca076342c98089bef3592475c1698b8ee7762b0617111e4eaf7ce6793`), including its exact mixed-domain certificate and independent-code replay. The remaining corner `(1,1)` is strictly positive by the new 1,338-leaf exact Bernstein cover pinned in §4.

For `Hpol`, fix the total `W=w_A+w_B`. The terms quadratic in the two weights depend only on `W`; the remaining weight dependence is linear in `w_A*(u_4+u_5+u_6)+w_B*(u_1+u_2+u_3)`. Therefore `Hpol` is affine along every segment of the rectangle `0<=w_A<=u_1u_2u_3`, `0<=w_B<=u_4u_5u_6` having fixed `W`. Each such segment has endpoints on the rectangle boundary; positivity at both endpoints implies positivity throughout.

The boundary faces with one weight zero are the earlier one-triple lemma, with the triangle groups interchanged where needed. On the remaining face `theta_A=1`, the new exact certificate proves strict positivity for every `theta_B` in `[0,1]`; interchanging groups gives the face `theta_B=1`.

Specifically, express the new face's quadratic in `theta_B` as `H_0*(1-theta_B)^2+2*H_1*theta_B*(1-theta_B)+H_2*theta_B^2`. The certificate proves `H_0,H_2>0` everywhere and covers every positive six-rate point by either `H_1>=0` or `H_0*H_2-H_1^2>0`. The first case gives strict positivity directly; the second gives positive definiteness. Thus the entire square is covered, not merely the corners or selected parameters.

## 4. Reproducible exact evidence and review boundary

New primary H constructor `frontier-20261028-ph7-two-disjoint-triangle-universal-H-check.py` SHA256 `7a35f95a90119358d74184b1916b231a4a4c815e25ed051b154b1b28cac22818` returned PASS. Its frozen certificate `frontier-20261028-ph7-two-disjoint-triangle-universal-H-certificate-v1.json` SHA256 `5f844f19a36d856e4b77abda72acffc0be81283829547b7f7302aa8187322a7f` contains `2443,2141` strict endpoint leaves and a complete two-way cover of `2693` nonnegative-middle leaves plus `445` strictly positive-Gram leaves.

New primary Q constructor `frontier-20261028-ph7-two-disjoint-triangle-universal-Q-check.py` SHA256 `b23cf2afb2123c90b20312743e88fdc6fcd2e559e5006c7b9a2b8e3b8ea80e48` returned PASS; frozen Q certificate `frontier-20261028-ph7-two-disjoint-triangle-universal-Q-certificate-v1.json` SHA256 `0245674a98ea761d2de0c57d3a7b50be509ed1304f1c42c8ba538eec26ea1549` contains `1338` strict leaves.

The separately implemented stdlib `Fraction`/integer replay `frontier-20261028-ph7-two-disjoint-triangle-integer-replay.py` SHA256 `d1af5d00285727a0ede0f0585b5ee9963f68d4c1677a5d8fd7df645639286079` actually returned PASS: it reconstructed all five polynomials from elementary symmetric sums, bound their coefficient digests, checked complete prefix trees, every integer Bernstein sign, and strictness at all admissible interior box vertices. The old one-triple certificate and its independent-code replay are pinned in the imported manuscript. Independent code by this owner is **not** independent scientific review, a formal proof assistant, or a novelty screen.

A disjoint audit should reconstruct the two coefficient equations including all 4-cycles; prove positivity of `Qpol` on the entire square and the fixed-`W` boundary reduction for `Hpol`; verify both old and new positive-domain cuts and their certificate coverage; and check `q>0` and the caller. Applying the nine-edge or all-no-two-cycle corollaries additionally requires their separately named pending templates. No complete 8/9 existence/exclusion, minimum8, ten-edge exclusion in general, novel-PH6 claim, parent adoption, or scientific-review gate is asserted.
