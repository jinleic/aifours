# An all-edge exclusion for the three-triangle chain pattern

Status: **WRITTEN composition of previously exactly replayed universal Q/H certificates**, awaiting disjoint mathematical review and parent disposition. The result below applies with arbitrarily many transitions and directed four-cycles; it does not settle PH7 at `8/9` or graphs with directed two-cycles.

## 1. Statement

There is no irreducible seven-state row generator with critical double pair `-d +/- ib`, `b^2/d^2=8/9`, no directed two-cycle, and exactly three directed-triangle vertex sets of the following form: two are disjoint triples `A,B`, and the third consists of one vertex of `A`, one vertex of `B`, and the remaining seventh vertex `x`.

Either orientation of the third triangle is allowed. Arbitrarily many other transitions, four-cycles and longer cycles are allowed provided they create no two-cycle and no additional triangle vertex set. This is a spectral exclusion; no PH input or exit vector is assumed.

## 2. Row-fraction bound for the connector triangle

Scale `d=1`. Let the diagonal rates on `A,B` be `u_1,u_2,u_3` and `u_4,u_5,u_6`; choose `u_1,u_4` at the vertices used by the third triangle, and let the singleton rate be `x`. No two-cycle means each of the three triangle vertex sets has only one orientation. Write its products as

`w_A=theta_A*u_1*u_2*u_3`, `w_B=theta_B*u_4*u_5*u_6`, `w_C=k*x`,

with `0<theta_A,theta_B<=1` and `k>=0`. Row conservation yields the crucial all-edge inequality

`k <= k_max := (1-theta_A)*(1-theta_B)*u_1*u_4`.

Indeed, if `p_i` are the row fractions of triangle `A`'s internal edges, `theta_A=prod_i p_i<=p_1`. The outgoing edge of the third triangle at that vertex is distinct from the internal triangle edge, so its row fraction is at most `1-p_1<=1-theta_A`. The same argument holds at `u_4`; the singleton's selected outgoing-edge fraction is at most one. Multiplying proves the bound, irrespective of the direction of the third triangle or any other outgoing edges.

## 3. Universal Q/H positivity throughout 0<=k<=k_max

Let `f_j` be the elementary sums of the six triangle rates, and define

`A0=f_2-4*f_1+74/9`,

`B0=f_3-4*f_2+(74/9)*f_1-28/3-w_A-w_B`,

`h0=f_4-(70/9)*f_2+(212/9)*f_1-1007/27-w_A*(u_4+u_5+u_6)-w_B*(u_1+u_2+u_3)`,

`h1=f_3-(70/9)*f_1+212/9-w_A-w_B`, `T=u_2+u_3+u_5+u_6`.

For an independent scalar `k` put

`Q(k)=81*[A0*(A0-k)-(f_1-4)*B0]`,

`H(k)=-243*[h0*(A0-k)-(h1-k*T)*B0]`.

Both are affine in `k` when the rates and fractions are fixed. At `k=0`, their strict positivity is the universal two-disjoint-triangle Q/H lemma in `frontier-20261028-ph7-critical-two-disjoint-triangle-full-exclusion-v1.md` (SHA256 `0489ce341fa98eb779f54f58926773943a827662f66bcd97619c28e52b9d040e`). At `k=k_max`, strict positivity of `Q` is the universal Q-star lemma in `frontier-20261028-ph7-unique-nine-edge-Q-positivity-v1.md` (SHA256 `1514d213dffbb64f88f6e635993a29a21db999a1f40ad6e6bfd469a539d25679`); strict positivity of `H` is the full-square H-star lemma in `frontier-20261028-ph7-critical-unique-nine-edge-full-exclusion-v1.md` (SHA256 `f88664a9af485c8d58ff2ce01e0b96a983789bc636ec137a71909beff5884f5b`). Their independently implemented integer certificate replays and prior imports are pinned in those manuscripts. By affine interpolation, `Q(k)>0` and `H(k)>0` for every `0<=k<=k_max`, including `k_max=0`.

## 4. Retaining all four-cycles

The characteristic polynomial contains `D(y)=y*((y+1)^2+8/9)^2` and has quotient `y^2+p*y+q`, with `q>0` by irreducible row-generator stability. No two-cycles and exactly these three triangles give the `y^4` coefficient equation

`(A0-k)*x+B0=0`.

Since `q=A0+x*(f_1-4)`, multiplication by `A0-k` gives `81*q*(A0-k)=Q(k)>0`. Hence `A0-k>0`.

Let `V4>=0` be the sum of the products of **every** directed 4-cycle. At `y^3`, the first two triangles contribute their outside sums, the third contributes `k*x*T`, and all directed 4-cycles are subtracted. Thus

`h0+x*(h1-k*T)-V4=0`.

Multiply by `A0-k` and use the `y^4` equation:

`0 = -H(k)/243 - (A0-k)*V4 < 0`,

contradiction. Longer cycles cannot enter either coefficient. This proves the all-edge statement.

## 5. Conditional structural consequence

The previously written no-two-cycle disjoint-triangles theorem `frontier-20261028-ph7-no-two-cycle-disjoint-triangles-v1.md` (SHA256 `7306b0cc0eeca0f78c75c1867f99b4675e169da2fdfada82c5c0f5175eb97ddf`) says that every critical no-two-cycle generator has two vertex-disjoint directed triangles. Combining it with the present theorem: if such a generator has **exactly three** triangle vertex sets, two of its triangles must share a directed edge. For, relative to the disjoint pair, the only third triple not sharing two vertices with either is precisely the one-vertex-from-each plus singleton case excluded above; without a two-cycle, shared triangle vertices imply the shared edge has the same orientation.

Both the disjoint-pair caller and all Q/H certificates are pending disjoint scientific audit and parent disposition. Their exact replay is independent code by the same owner, not independent scientific review or formal verification. No general ten-edge exclusion, minimum-PH-order claim, 8/9 existence/exclusion verdict, novelty, or parent adoption is asserted.
