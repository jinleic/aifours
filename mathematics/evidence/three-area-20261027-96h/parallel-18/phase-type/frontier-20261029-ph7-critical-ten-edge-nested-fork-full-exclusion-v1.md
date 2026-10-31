# Complete critical spectral exclusion for a four-triangle ten-edge graph

Status: **WRITTEN-checked with separately implemented stdlib Fraction/integer certificate replay**, pending disjoint scientific review and parent disposition. This is an exact all-rate exclusion of one genuinely ten-transition, four-triangle graph at `z=8/9`. It does **not** exclude all ten-transition graphs, all no-two-cycle graphs, or PH7 as a whole.

## 1. Statement and graph

There is no seven-state row generator with critical repeated pair `-d +/- ib` (`d>0`, `b^2/d^2=8/9`) whose positive directed edges are exactly

`0->1, 0->5, 1->2, 1->3, 2->0, 3->0, 3->4, 4->1, 5->6, 6->0`.

The graph is strongly connected and has no directed two-cycles. Its four directed triangle vertex sets are `{0,5,6}`, `{1,3,4}`, `{0,1,3}`, `{0,1,2}`. The proof is spectral and does not require a PH input or exit vector. It imports the previously frozen one-/two-disjoint-triangle and unique-connector universal Q/H lemmas and the corrected shared-edge polytope theorem, all at their pending independent-review cuts.

## 2. Exact nested-fork weight simplex

Normalize `d=1`. Let the diagonal rates of vertices `0,5,6,1,3,4` respectively be `u_1,...,u_6>0`, and let `x>0` be the rate of vertex 2. Define the rate products

`P_A=u_1*u_2*u_3`, `P_B=u_4*u_5*u_6`, `P_C=u_1*u_4*u_5`, `P_D=u_1*u_4`.

Let `p` be the row fraction on `0->1`, `q` the row fraction on `1->3`, and `t` the row fraction on `3->0`. Every other outgoing edge at those fork vertices is the unique remaining edge, so `0<p,q,t<1`. The actual cycle products are exactly

`w_A=(1-p)*P_A`, `w_B=q*(1-t)*P_B`, `w_C=p*q*t*P_C`, `w_D=x*p*(1-q)*P_D`.

Write `w_D=x*K`. The normalized vector `(w_A/P_A,w_B/P_B,w_C/P_C,K/P_D)` is multi-affine in `(p,q,t)` and hence lies in the convex hull of its eight cube-corner values. Those eight values are exactly these five distinct points:

`v_0=(1,0,0,0)`, `v_1=(1,1,0,0)`, `v_2=(0,0,0,1)`, `v_3=(0,1,0,0)`, `v_4=(0,0,1,0)`.

They are affinely independent, giving a four-simplex. We prove positivity on the **entire** simplex, a relaxation of the actual product structure.

## 3. Coefficient identities with all four-cycles

Let `f_j` be elementary symmetric sums in the six `u` rates. Put

`A0=f_2-4*f_1+74/9`,

`B0=f_3-4*f_2+(74/9)*f_1-28/3-w_A-w_B-w_C`,

`h0=f_4-(70/9)*f_2+(212/9)*f_1-1007/27-w_A*(u_4+u_5+u_6)-w_B*(u_1+u_2+u_3)-w_C*(u_2+u_3+u_6)`,

`h1=f_3-(70/9)*f_1+212/9-w_A-w_B-w_C`, `T=u_2+u_3+u_5+u_6`.

The actual characteristic polynomial is `D(y)*(y^2+p_h*y+q_h)`, `D(y)=y*((y+1)^2+8/9)^2`, with `q_h>0` from strong connectivity and generator stability. The `y^4,y^3` coefficients give

`(A0-K)*x+B0=0`, `h0+x*(h1-K*T)-V4=0`,

where `V4>=0` is the sum of all directed four-cycle products. No two-cycles or disjoint-two-cycle terms are present. Define

`Q=81*[A0*(A0-K)-(f_1-4)*B0]`,

`H=-243*[h0*(A0-K)-(h1-K*T)*B0]`.

Exactly, without division,

`Q=81*q_h*(A0-K)`, `H=-243*(A0-K)*V4`.                  (ID)

The proof below shows `Q,H>0` on the full weight simplex. Then `q_h>0` forces `A0-K>0`, while(ID) forces `H<=0`, a contradiction.

## 4. Reduce full-simplex H positivity to its triangular faces

For fixed six rates, `Q` is affine in the four weights. Its values at `v_0,v_3,v_4` are the one-triple Q lemma, at `v_1` the two-disjoint-triangle Q lemma, and at `v_2` the `Q00` maximal-singleton-connector lemma. Those universal lemmas are pinned in `frontier-20261028-ph7-critical-two-triangle-vertex-sets-v1.md` (SHA256 `b08ddcaca076342c98089bef3592475c1698b8ee7762b0617111e4eaf7ce6793`), `frontier-20261028-ph7-critical-two-disjoint-triangle-full-exclusion-v1.md` (SHA256 `0489ce341fa98eb779f54f58926773943a827662f66bcd97619c28e52b9d040e`), and `frontier-20261028-ph7-unique-nine-edge-Q-positivity-v1.md` (SHA256 `1514d213dffbb64f88f6e635993a29a21db999a1f40ad6e6bfd469a539d25679`). Thus `Q>0` everywhere.

For `H`, fix both linear quantities `K` and `W=w_A+w_B+w_C`. Inspection of its formula shows that on that slice `H` is affine in the remaining weights. In barycentric coordinates of the four-simplex, an extreme point of the slice has at most three nonzero coordinates: the constraints `sum lambda=1`, fixed `K`, fixed `W` provide at most three independent linear equations; four positive coordinates would admit a nonzero perturbation preserving all three. Thus each slice minimum occurs on a **triangular or lower-dimensional face** of the simplex. To prove `H>0` on the whole simplex it suffices to prove positivity on all its triangular faces.

The four triangular faces not containing `v_2` are contained in the relaxed shared-edge polytope already proven in `frontier-20261029-ph7-critical-shared-edge-three-triangle-full-exclusion-v1.md` (SHA256 `a727ddc379f469a18cc7132a702272e570c3acde04ac78f601835c070dc8c4c6`), after interchanging the two disjoint triangle groups. Their full Q/H positivity is a named import. Six faces contain `v_2`; these are handled below.

## 5. Exact copositivity of all six connector faces

For each simplex vertex let `D_i=H(v_i)` and for each pair let

`O_ij=4*H((v_i+v_j)/2)-D_i-D_j`.

On a triangular face with nonnegative barycentric coordinates `lambda_i,lambda_j,lambda_k` summing to one,

`H=D_i*lambda_i^2+D_j*lambda_j^2+D_k*lambda_k^2+O_ij*lambda_i*lambda_j+O_ik*lambda_i*lambda_k+O_jk*lambda_j*lambda_k`.

All `D_i>0` by the imported endpoint lemmas. All ten simplex edges have `H>0`: edges among `0,1,3,4` by the shared-edge polytope; edges `02,12` by the **relaxed** positive `H_rel` lemma in `frontier-20261028-ph7-critical-unique-nine-edge-full-exclusion-v1.md` (SHA256 `f88664a9af485c8d58ff2ce01e0b96a983789bc636ec137a71909beff5884f5b`), with fractions `(theta_A,theta_B)=(1-s,0)` and `(1-s,1-s)` respectively and connector coefficient `s*P_D`; edge `23` by the exact dual cover below; edge `24` because `O_24>=0` and its endpoints are positive. In particular, whenever `O_ij<0`, strict positivity of that edge forces `4D_iD_j-O_ij^2>0`.

For each of the six faces containing `v_2`, the exact selector covers below establish either an indicated pair of off-diagonal coefficients cannot both be negative, or, for each remaining possible pair of negative coefficients incident at vertex `i`,

`O_ij>=0 OR O_ik>=0 OR [2*O_jk*D_i-O_ij*O_ik >=0]`.

The globally nonnegative `O_24` excludes all negative pairs involving that edge. The remaining forbidden pairs are `(O_01,O_02)` on face `012`, `(O_02,O_23)` on face `023`, and `(O_13,O_23)` on face `123`. If zero or one off-diagonal coefficient is negative, positive edge blocks suffice. If two are negative, the corresponding cross selector and completing the square in their common vertex give a strictly positive form on nonzero nonnegative barycentric coordinates; three negative coefficients are impossible by the forbidden-pair rules. Thus every connector face is strictly copositive, and §4 gives `H>0` throughout the simplex.

## 6. Frozen exact certificate and replay

The primary `frontier-20261029-ph7-nested-fork-simplex-check.py` SHA256 `5e4a25c1520215b6c3ecc26b84be807448edd2c105a11699df26710a423ec002` builds all six-rate SymPy polynomials and exact integer Bernstein covers. Three pinned certificate parts are:

* `frontier-20261029-ph7-nested-fork-simplex-certificate-part0-v1.json`, SHA256 `7bdd0da7e5239e94e2542dc8cc006fcd1ef0a1ca0cf293e06d413466371523f1` — 14,996 leaves.
* `frontier-20261029-ph7-nested-fork-simplex-certificate-part1-v1.json`, SHA256 `0a391ad3be1cb37a23e6cd2cef1109d41a57e4c4366f8232851ef444d8e9c437` — 12,543 leaves.
* `frontier-20261029-ph7-nested-fork-simplex-certificate-part2-v1.json`, SHA256 `dd2e484c3ac9ee3800d8176ab246df12dd7cac32aa5178e22ce830c639b34b93` — 11,652 leaves.

The 14 complete selector trees include `O24>=0` (2,419 leaves), the `O23>=0 OR G23>0` edge cover (3,236/668), three off-diagonal-pair OR covers, and nine conditional cross covers, for **39,191** leaves total. Each strict Gram leaf requires positive admissible finite interior Bernstein vertices; all non-strict selector coefficients are checked nonnegative.

The separately implemented stdlib `Fraction`/integer replay `frontier-20261029-ph7-nested-fork-simplex-integer-replay.py` SHA256 `ba02a15ea269d509746ecff0e4adb9803087c3f949efc3929ba3150bfcb173a7` reconstructed all 20 selector polynomials and coefficient hashes, validated all three full prefix-tree unions and required interior strictness, and returned PASS for **all three parts**. Its invocations completed foreground in 45.95, 25.27, and 43.10 seconds. The primary's first single-batch attempt auto-backgrounded and timed out before output; the disclosed three successful replacement batches and historical cadence qualification are recorded in `frontier-20261029-checkpoint-nested-fork-certificate-v1.json`. Independent code by the same owner is not independent scientific review or formal verification.

A disjoint audit must reconstruct the graph's four products and ALL `y^4,y^3` terms, Q/H identities, simplex convexification, the fixed-`K,W` extreme-point reduction, imported vertex/edge scopes including `H_rel`, all 14 selector unions and strict leaves, and actual spectral caller. No actual seven-state realization, general 10-edge/PH7/PH8 exclusion, novelty clearance, or parent adoption is claimed.
