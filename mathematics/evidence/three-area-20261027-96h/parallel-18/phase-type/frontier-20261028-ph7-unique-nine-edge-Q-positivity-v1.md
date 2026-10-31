# Strict quotient positivity on the unique remaining nine-edge graph

Status: **WRITTEN-checked with an independently implemented exact integer certificate replay**, pending independent scientific review and parent disposition. This is a necessary condition and an exact reduction for the remaining three-triangle connector graph. It does **not** prove its exclusion, construct a PH realization, or decide PH7 at `8/9`.

## 1. Graph and claim

The graph has two vertex-disjoint directed triangles `A,B` and a singleton, with connector edges `A_f -> B_f -> singleton -> A_f`; thus the connector is itself a directed triangle. Let the six triangle diagonal rates be `u_1,...,u_6>0`, with fork rates `u_1,u_4`, and singleton rate `x>0`. For the two triangle products put

`w_A=theta_A*u_1*u_2*u_3`, `w_B=theta_B*u_4*u_5*u_6`, `0<theta_A,theta_B<1`,

and define `k=(1-theta_A)*(1-theta_B)*u_1*u_4>0`. The connector triangle product is **exactly** `k*x` by the row-generator ties.

If this graph has the critical double pair at `z=8/9`, the following quantity is strictly positive:

`A_star=f_2-4*f_1+74/9-k > 0`,

where `f_j` denotes the elementary symmetric sum of order `j` in the six triangle rates. Moreover the singleton rate is uniquely determined by the other rates and fork fractions:

`x = -B0/A_star > 0`,

`B0=f_3-4*f_2+(74/9)*f_1-28/3-w_A-w_B < 0`.

These signs and formula are necessary, not sufficient; they do not determine or exclude any PH input/exit vectors.

## 2. Coefficient derivation

Scale to `d=1`, set `A0=f_2-4*f_1+74/9`, and write the characteristic polynomial as `D(y)*(y^2+p*y+q)` with `D(y)=y*((y+1)^2+8/9)^2`. Irreducible row-generator stability gives `q>0`. Comparing the `y^4` coefficient, including all THREE triangle products, gives

`(A0-k)*x+B0=0`.

The `y^5,y^6` coefficients give `q=A0+x*(f_1-4)`. Therefore

`81*q*(A0-k) = Q_star := 81*[A0*(A0-k)-(f_1-4)*B0]`.

The universal strict positivity of `Q_star` in §3 forces `A0-k>0` because `q>0`; the displayed formula and `B0<0` follow since `x>0`.

The remaining `y^3` condition is **not yet discharged**. Its exact form is

`h0+x*(h1-k*T)=0`,

`h0=f_4-(70/9)*f_2+(212/9)*f_1-1007/27-w_A*(u_4+u_5+u_6)-w_B*(u_1+u_2+u_3)`,

`h1=f_3-(70/9)*f_1+212/9-w_A-w_B`, `T=u_2+u_3+u_5+u_6`.

Eliminating `x` gives the still-open exact equation

`H_star := -243*[h0*(A0-k)-(h1-k*T)*B0] = 0`.

All four-cycle terms vanish on this specific graph, but no sign is asserted for `H_star`; a candidate universal sign would require a separate exact proof and review.

## 3. Universal Q-star positivity

For fixed positive rates, `Q_star` is multi-affine in `(theta_A,theta_B)`, because `B0` is affine and `k` is bilinear. Its value on the closed square is the nonnegative bilinear convex combination of the four corner values. The `(1,0)` and `(0,1)` corners have `k=0` and are covered by the one-triple Q lemma in §5 of `frontier-20261028-ph7-critical-two-triangle-vertex-sets-v1.md` (SHA256 `b08ddcaca076342c98089bef3592475c1698b8ee7762b0617111e4eaf7ce6793`). The `(1,1)` corner is the Q11 positivity certificate in `frontier-20261028-ph7-critical-two-disjoint-triangle-full-exclusion-v1.md` (SHA256 `0489ce341fa98eb779f54f58926773943a827662f66bcd97619c28e52b9d040e`).

At `(0,0)`, `k=u_1*u_4` and `w_A=w_B=0`. Its strict positivity is proved by `frontier-20261028-ph7-three-triangle-Q00-check.py` SHA256 `2c0c95b1a51ed5f8c4cdfb2aeeb5076cea3197db04536602376a3db0c991d37b`; the frozen exact certificate `frontier-20261028-ph7-three-triangle-Q00-certificate-v1.json` SHA256 `b8e894422a1fa90433ff4b77a766430d2eeba6d7cc890b5dbd1c3c08b41f7ee2` has a complete 1,972-leaf strict six-rate integer Bernstein cover. The separately implemented stdlib `Fraction`/integer replay `frontier-20261028-ph7-three-triangle-Q00-integer-replay.py` SHA256 `9f19de8ce5240a3367e29cf81cfeea9a6814f90412a236c33411b6198ba0a602` returned PASS after reconstructing the coefficient hash, prefix coverage, all signs and every admissible interior-vertex strictness test.

Thus all four corners, and therefore the entire closed square, have `Q_star>0`. This independent-code replay is by the same owner, not independent mathematical review or formal verification. Applying this graph-specific reduction as the sole nine-edge candidate additionally depends on the separately pending graph-template and two-disjoint-triangle exclusion gates. No H-star positivity, global 8/9 verdict, novelty, parent adoption, or stronger-review gate is claimed.
