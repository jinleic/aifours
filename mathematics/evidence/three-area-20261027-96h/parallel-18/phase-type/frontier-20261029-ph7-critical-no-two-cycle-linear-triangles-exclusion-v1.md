# A critical no-two-cycle graph must have edge-overlapping triangles

Status: **WRITTEN composition of named exact, independently replayed Q/H certificates**, awaiting disjoint scientific review and parent disposition. This is an all-transition-count necessary graph condition at `z=8/9`, not a complete PH7 exclusion or minimum-state result. It closes the specific multi-connector gap recorded as open in `frontier-20261028-ph7-critical-no-two-cycle-triangle-overlap-v1.md`; that earlier failed-route file is preserved unchanged.

## 1. Theorem

Every irreducible seven-state row generator with the critical double nonreal pair `-d +/- ib`, `b^2/d^2=8/9`, and **no directed two-cycle** must contain two distinct directed triangles sharing an edge. Thus, using the separately supported irreducibility/Perron normalization, any critical PH representation on at most seven states has either a directed two-cycle or a pair of triangles sharing a directed edge.

The statement permits arbitrarily many transitions, directed four-cycles, and longer cycles. It is conditional on the pending Q/H and capacity/disjoint-triangle inputs identified in §4; no independent scientific review, formal proof, novelty, parent adoption, or existence/exclusion verdict for PH7 is asserted.

## 2. Classify a linear triangle family

Suppose no two directed triangles share an edge. Their unordered vertex triples form a linear family: any two meet in at most one vertex. The previously written no-two-cycle disjoint-triangles theorem `frontier-20261028-ph7-no-two-cycle-disjoint-triangles-v1.md` (SHA256 `7306b0cc0eeca0f78c75c1867f99b4675e169da2fdfada82c5c0f5175eb97ddf`) then gives two **vertex-disjoint** directed triangles `A,B`. Their vertices use six of the seven states; let the remaining singleton be `x`.

Every other triangle must contain `x` and exactly one vertex of each of `A` and `B`: it cannot contain two vertices from either triple, nor be a distinct triple contained wholly in `A union B` without taking two vertices from one of them. Different such connector triangles use different `A` vertices and different `B` vertices, otherwise they would share an edge with each other through `x`. There can be one, two, or three connectors; if there are none, the two-disjoint-triangle exclusion `frontier-20261028-ph7-critical-two-disjoint-triangle-full-exclusion-v1.md` (SHA256 `0489ce341fa98eb779f54f58926773943a827662f66bcd97619c28e52b9d040e`) already rules out the graph, even with arbitrary four-cycles.

## 3. Aggregate all connectors by a convex endpoint argument

Scale `d=1`. Let the rates of the six triangle vertices be `u_1,...,u_6`, and let `x>0` also denote the singleton's rate. Put `w_A=theta_A*u_1*u_2*u_3`, `w_B=theta_B*u_4*u_5*u_6`, where `0<theta_A,theta_B<=1`; row fractions bound them by one. Each connector triangle `i` contains vertices `a_i in A`, `b_i in B`, and `x`, with product `w_i=x*k_i` for some `k_i>0`.

For a fixed connector `i`, let `s_i` be the singleton-row fraction on its actual outgoing edge. At `a_i`, the connector's outgoing edge differs from the outgoing internal edge of `A`; the latter's row fraction is at least `theta_A`, so the connector fraction is at most `1-theta_A`. Similarly the connector fraction at `b_i` is at most `1-theta_B`. Hence

`k_i <= s_i*(1-theta_A)*(1-theta_B)*a_i*b_i = s_i*K_i`.

Because distinct linear connector triples use different `A` and `B` vertices, their outgoing edges from `x` are distinct irrespective of their orientations. The row-generator ties give `sum_i s_i<=1`. Therefore the nonnegative weights

`lambda_i=k_i/K_i` when `K_i>0` (and `lambda_i=0` when `K_i=0`)

satisfy `sum_i lambda_i<=1`. If `K_i=0`, the displayed inequality forces `k_i=0`, so this convention is exact.

Let `f_j` be elementary sums in the six `u` rates and define

`A0=f_2-4*f_1+74/9`,

`B0=f_3-4*f_2+(74/9)*f_1-28/3-w_A-w_B`,

`h0=f_4-(70/9)*f_2+(212/9)*f_1-1007/27-w_A*(u_4+u_5+u_6)-w_B*(u_1+u_2+u_3)`,

`h1=f_3-(70/9)*f_1+212/9-w_A-w_B`.

For connector `i` define `T_i` as the sum of the four `A union B` rates outside `{a_i,b_i}`. Put `K=sum_i k_i` and `J=sum_i k_i*T_i`. With

`Q=81*[A0*(A0-K)-(f_1-4)*B0]`,

`H=-243*[h0*(A0-K)-(h1-J)*B0]`,

both `Q,H` are affine functions of the vector `(k_i)`. The admissible vector is a convex combination of zero and the single-connector vertices `(0,...,K_i,...,0)` with coefficients `1-sum_i lambda_i,lambda_i`.

At zero, `Q,H>0` by the universal two-disjoint-triangle lemma in the manuscript cited in §2. At each single-connector vertex, relabel `a_i,b_i` as the two fork rates and use the universal maximal-connector `Q_star>0` and `H_star>0` lemmas in `frontier-20261028-ph7-unique-nine-edge-Q-positivity-v1.md` (SHA256 `1514d213dffbb64f88f6e635993a29a21db999a1f40ad6e6bfd469a539d25679`) and `frontier-20261028-ph7-critical-unique-nine-edge-full-exclusion-v1.md` (SHA256 `f88664a9af485c8d58ff2ce01e0b96a983789bc636ec137a71909beff5884f5b`). These are **all-rate algebraic lemmas**, not assumptions that the single-connector graph is the actual graph. Consequently affine interpolation gives `Q,H>0` for the simultaneous multi-connector vector.

## 4. Complete coefficient contradiction

The characteristic polynomial is `D(y)*(y^2+p*y+q)`, with `D(y)=y*((y+1)^2+8/9)^2` and `q>0` from irreducible row-generator stability. There are no two-cycles, so the `y^4` coefficient gives

`(A0-K)*x+B0=0`.

Also `q=A0+x*(f_1-4)`, so `81*q*(A0-K)=Q>0` and hence `A0-K>0`.

Every four-cycle product contributes nonnegatively to a total `V4>=0`. The `y^3` coefficient, including all triangle outside sums and all four-cycles, is

`h0+x*(h1-J)-V4=0`.

Multiply by `A0-K` and use the first equation. This yields

`0 = -H/243-(A0-K)*V4 < 0`,

a contradiction. The graph therefore cannot have a linear triangle family, proving §1. Longer cycles do not enter these coefficients.

The single-connector `Q_star` certificate includes the independently reconstructed 1,972-leaf Q00 cover and earlier corner covers; the `H_star` proof includes the separately reconstructed 27,270-leaf simplex copositivity cover. All exact certificate paths, hashes, and replay scope are pinned in the cited manuscripts, and the parent has been informed of the owner checkpoint-cadence and auto-background transport qualification associated with the latter replay. The no-two-cycle disjoint-pair input and every scientific/dependency caller still require their disjoint full audit. This proof supplies no PH7/PH8 existence-exclusion verdict, no general two-cycle restriction, no formal proof or novelty clearance, and no parent adoption.
