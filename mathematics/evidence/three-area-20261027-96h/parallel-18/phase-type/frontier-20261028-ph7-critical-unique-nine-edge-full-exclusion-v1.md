# Complete critical spectral exclusion of the unique three-triangle nine-edge graph

Status: **WRITTEN-checked with separately implemented stdlib Fraction/integer certificate replay**, awaiting disjoint scientific review and parent disposition. This excludes the sole length-three connector graph identified by the separately pending nine-edge template; together with the separately pending two-disjoint-triangle exclusion it would force at least ten positive transitions in every critical PH7 representation. It does **not** exclude PH7 with ten or more transitions or settle existence/exclusion at `8/9`.

## 1. Statement

There is no seven-state row generator whose graph consists of two vertex-disjoint directed triangles and a singleton, with connector edges forming a third directed triangle through one vertex of each triangle and the singleton, and whose spectrum contains `-d +/- ib` twice with `d>0` and `b^2/d^2=8/9`.

This is a characteristic-polynomial exclusion and does not assume any particular input or exit vector. Its proof imports the all-variable two-disjoint-triangle `Hpol>0` lemma from `frontier-20261028-ph7-critical-two-disjoint-triangle-full-exclusion-v1.md` (SHA256 `0489ce341fa98eb779f54f58926773943a827662f66bcd97619c28e52b9d040e`) at its present unreviewed cut, including its old one-triangle lemma and separately replayed exact certificates.

## 2. Exact polynomial reduction

Scale `d=1`. Let the six triangle diagonal rates be `u_1,...,u_6>0`, with fork rates `u_1,u_4`, and let `x>0` be the singleton rate. Let `f_j` be the elementary symmetric sums in the six triangle rates. The directed triangle products and connector parameter are

`w_A=theta_A*u_1*u_2*u_3`, `w_B=theta_B*u_4*u_5*u_6`,

`k=(1-theta_A)*(1-theta_B)*u_1*u_4`, `0<theta_A,theta_B<1`.

The third triangle product is `k*x`. The only simple directed cycles are these three triangles; in particular there are no two- or four-cycles. Define

`A0=f_2-4*f_1+74/9`,

`B0=f_3-4*f_2+(74/9)*f_1-28/3-w_A-w_B`,

`h0=f_4-(70/9)*f_2+(212/9)*f_1-1007/27-w_A*(u_4+u_5+u_6)-w_B*(u_1+u_2+u_3)`,

`h1=f_3-(70/9)*f_1+212/9-w_A-w_B`, `T=u_2+u_3+u_5+u_6`.

The real characteristic polynomial contains `D(y)=y*((y+1)^2+8/9)^2` and has degree seven. Comparing `y^4` and `y^3` coefficients, with all three triangle contributions retained, gives

`(A0-k)*x+B0=0`,

`h0+x*(h1-k*T)=0`.

Multiplying the second equation by `A0-k` and using the first implies

`H_star := -243*[h0*(A0-k)-(h1-k*T)*B0] = 0`.             (NEC)

This remains valid even if `A0-k=0`; no division, hidden-root sign, or input-output assumption is used. Sections 3–5 prove the **strict opposite sign** `H_star>0` for every six positive rates and all `theta_A,theta_B` in `[0,1]`.

## 3. Reduction to a quadratic on a simplex

Let

`H_two=-243*(h0*A0-h1*B0)`, `L=h0-T*B0`.

The imported two-triangle universal lemma gives `H_two>0` for every rate and fraction in the full closed square, and exact expansion gives

`H_star=H_two+243*k*L`.

If `L>=0`, then `H_star>0`. If `L<0` and `theta_A>=theta_B`, use the upper bound `k<=k_rel=(1-theta_A)*u_1*u_4`; because `L` is negative,

`H_star >= H_rel := H_two+243*k_rel*L`.

For fixed rates, `H_rel` is a polynomial of **total degree at most two** in `(theta_A,theta_B)`. On the triangle `0<=theta_B<=theta_A<=1`, put

`z_0=1-theta_A`, `z_1=theta_A-theta_B`, `z_2=theta_B`.

The `z_i` are nonnegative and sum to one. Let `v_0=(0,0),v_1=(1,0),v_2=(1,1)` and define

`D_i=H_rel(v_i)`, `O_ij=4*H_rel((v_i+v_j)/2)-D_i-D_j`.

Quadratic homogenization gives exactly

`H_rel = sum_i D_i*z_i^2 + sum_{i<j} O_ij*z_i*z_j`.

We prove this quadratic is strictly copositive on the whole simplex in §4. When `theta_A<theta_B`, interchange the two triangle groups and their fork fractions; the same argument applies because the graph and `H_star` are symmetric under that interchange. Thus `H_star>0` on the entire closed square.

## 4. Copositivity from the exact selector covers

For `i<j`, set `G_ij=4*D_i*D_j-O_ij^2`, and define

`C_12=2*O_12*D_0-O_01*O_02`,

`C_01=2*O_01*D_2-O_02*O_12`.

The exact six-rate certificate of §5 establishes all of the following, simultaneously at every positive finite rate point:

1. `D_0,D_1,D_2>0`.
2. For each pair `i<j`, either `O_ij>=0` or `G_ij>0`.
3. Either `O_01>=0` or `O_12>=0`.
4. At least one of `O_01>=0`, `O_02>=0`, `C_12>=0` holds.
5. At least one of `O_02>=0`, `O_12>=0`, `C_01>=0` holds.

If all off-diagonal coefficients are nonnegative, positivity is immediate. If exactly one is negative, item 2 makes its 2-by-2 block positive definite, while every other cross term is nonnegative.

If `O_01,O_02<0`, item 3 forces `O_12>=0`, item 4 forces `C_12>=0`, and item 2 makes `G_01,G_02>0`. Completing the square in `z_0` gives

`D_0*(z_0+O_01*z_1/(2D_0)+O_02*z_2/(2D_0))^2`

` + [G_01/(4D_0)]*z_1^2 + [G_02/(4D_0)]*z_2^2 + [C_12/(2D_0)]*z_1*z_2 > 0`

for every nonzero nonnegative `z`. If `O_02,O_12<0`, use item 5 and complete the square in `z_2` symmetrically. The remaining possible pair of negative off-diagonals, `O_01,O_12<0`, is forbidden by item 3. Thus every case is strictly positive and the simplex assertion follows. By §3 this contradicts(NEC), proving §1.

## 5. Exact certificate and independent-code replay

The primary constructor `frontier-20261028-ph7-three-triangle-copositivity-check.py` SHA256 `934ac760dde8107b240b097d43595b5743c1d243688ba7f523db967e29741d65` generated the frozen exact certificate `frontier-20261028-ph7-three-triangle-copositivity-certificate-v1.json` SHA256 `d03d02414d31eca8efcfdcea5fdbe7d0aa934cdd36768968eabad5ee45b4fdc9`. It constructs the 11 displayed polynomials by SymPy rational algebra, compactifies all six rates by `u_i=s_i/(1-s_i)`, and uses integer tensor Bernstein subdivision.

The nine complete selector covers have leaf counts:

| Selector | Certified leaves per alternative |
|---|---:|
| `D_0>0`, `D_1>0`, `D_2>0` | 2521; 2443; 2141 |
| `O_01>=0` OR `G_01>0` | 3055; 415 |
| `O_02>=0` OR `G_02>0` | 3804; 1080 |
| `O_12>=0` OR `G_12>0` | 2693; 445 |
| `O_01>=0` OR `O_12>=0` | 2266; 116 |
| `O_01>=0` OR `O_02>=0` OR `C_12>=0` | 2879; 64; 412 |
| `O_02>=0` OR `O_12>=0` OR `C_01>=0` | 2595; 78; 263 |

For strict leaves, the checker requires all Bernstein coefficients nonnegative and all admissible finite interior box vertices strictly positive; non-strict alternatives require the coefficient signs only. Each selector's leaf prefixes cover the entire six-cube. These are **27,270** leaves in total, not sampled rates.

A separately implemented standard-library-only replay, `frontier-20261028-ph7-three-triangle-copositivity-integer-replay.py` SHA256 `65580ff9fe57c8acc6d5b3c89ff80f7d6ca19abb52ec3358930875e8a88ac69b`, returned PASS after independently reconstructing all 11 polynomial coefficient dictionaries, binding their hashes, and verifying every full selector tree, integer sign, and required interior strictness. The replay call was automatically backgrounded by the tool after its foreground window and completed with reported wall time 70.18 seconds; this and the owner checkpoint-cadence interval are disclosed in `frontier-20261028-checkpoint-three-triangle-cadence-v1.json`. Independent code by the same owner is not independent scientific review or a formal proof assistant.

A disjoint audit must reconstruct the graph cycle coefficients, the sign of the connector relaxation, full-square/triangle symmetry, the precise homogeneous simplex matrix and all five selector implications; independently rebuild the 11 polynomials and verify the **union** and strictness of all nine covers; and review the imported two-triangle Q/H lemma. Scientific acceptance and any process classification are reserved to Main.

## 6. Conditional PH7 consequence and limits

The separately pending `frontier-20261028-ph7-critical-nine-edge-graph-template-v1.md` (SHA256 `b9814bdf1c3d5c1746af3b40731de0777ae7c626bd9e6d44df452c10813e78e8`) reduces any nine-transition critical PH7 candidate to two disjoint triangles plus a singleton connector. The separately pending two-disjoint-triangle exclusion removes connector lengths 4–7. This manuscript removes the remaining length-three connector. Combined with `frontier-20261028-ph7-critical-nine-transition-theorem-v1.md` (SHA256 `f7bbba1dea12d604ff5ec9d3d4eaf3388e852c495d3ba0c244b5a1d474202cb4`) and the round's supported irreducibility/Perron normalization, the **conditional** result is: every actual PH representation using at most seven states at `8/9` needs at least **ten** strictly positive transitions.

The candidate does not say whether any seven-state ten-or-more-transition realization exists; it does not establish the minimum number of PH states, a PH8 theorem, formal verification, novelty, disjoint mathematical review, or parent adoption. Prior held material is not a premise and all process history remains intact.
