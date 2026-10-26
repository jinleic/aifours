# Addendum3: diagonal Steiner contractions and exact full-head parallel geometry

Observed clock before creation: **2026-10-23T18:22:49-0700**.

## 0. Status and exact delta

**Author CANDIDATE, conditional on the existing complete coupled-optimizer packet.** No actual coupled reconstruction has yet been received/read by this owner, and no earlier verdict is inherited. No scientific program, sampling, symbolic execution, proof assistant, model CLI or new agent was used.

This strengthens the geometry of the SAME original all-Borel finite-ε V. It does not impose convexity, introduce a new mechanism family, claim a new Steiner principle, or solve the remaining V. NOVELTY_UNCLEAR remains.

The material consequence is that *every selected original optimal level* is an order ideal also in diagonal coordinates. Its first-octant profile is therefore nonincreasing1-Lipschitz at every scale. The cap-plus-line formula for its Minkowski-D parallels then holds for EVERY real dilation s≥0, without a small-core bound. This removes the irregular parallel-tail geometry from the full-head representation.

Imports are exactly the original globally optimal geometric density and its compact, D4-invariant, measure-regular closed levels from:

- `proof-coupled-level-tail-saturation-v1.md`, SHA `ae1e05470b233d2e51a3c56f45a58ab97ecd249a5ed479dc33c6d29ae4ea3958`;
- `proof-coupled-level-tail-ADDENDUM-1-closed-levels.md`, SHA `87320046a2396eb936138af7c3eb3122a5e3451140a70171dce73cb270fd5596`;
- `proof-coupled-level-tail-ADDENDUM-2-coordinate-Steiner.md`, SHA `15a4d1eda329a5f8eb22207c8fce9750f906d5f3cba8d290a65bde5426c29007`.

Measure-regularity here means K_k is the essential support of its level, not an arbitrary closed representative with isolated null appendages. This import is load-bearing for exact point inclusion below.

## 1. Why the diagonal symmetrization is licensed

Take the unit direction e=(1,-1)/sqrt2 and its perpendicular e_perp=(1,1)/sqrt2. In these coordinates the sensitivity diamond D is the centered square

```
|u| <= 1/sqrt2,   |v| <= 1/sqrt2.
```

In particular, every nonempty fiber of D parallel to e is a centered interval. Steiner symmetrization S_e therefore fixes D exactly. We do not replace the sensitivity set by another one in the original problem.

For any compact A, S_e(A) is defined only over its actual perpendicular projection: replace each nonempty compact fiber by the centered interval having its one-dimensional measure. Empty fibers stay empty; nonempty zero-length fibers become a point. This preserves area, gives a compact set, and is monotone under set inclusion, as in Addendum2.

The same one-dimensional argument gives

```
S_e(A)+D ⊂ S_e(A+D).
```

Indeed, for a nonempty compact fiber C of A and a centered interval I from a D fiber, C+I lies in the corresponding A+D fiber and has length at least length(C)+length(I). Thus its Steiner interval contains the sum of the two centered intervals. This includes interval endpoints and zero-length fibers, not just generic sections.

Apply S_e to every K_k of the original optimal geometric density. The inclusions K_k+D⊂K_(k+1) remain valid for the transformed levels. Their areas, and hence the layer-cake normalization, are unchanged. Their second moments do not increase: on each fiber the perpendicular coordinate is fixed, and the centered interval uniquely minimizes the e-coordinate second moment at fixed length.

The transformed sequence gives an actual original-feasible density. Its levels cover the plane: S_e(K_0)+kD⊂S_e(K_k), by the same inclusion and monotonicity. The geometric level index is therefore finite everywhere, and the all-shift privacy argument applies.

Global optimality forces equality of the total moment. Every positive-weight level deficit is nonnegative, so equality holds in every level. The unique one-dimensional interval minimizer then gives

```
K_k = S_e(K_k) almost everywhere, for every k.
```

This is equality of each original level to its symmetrization; we do not adopt transformed levels and then assume they retain other symmetries.

## 2. From almost-everywhere equality to exact diagonal contractions

For 0<a≤1, let T_a shrink the e coordinate by a and fix the perpendicular coordinate. It is invertible, preserves null sets, and sends each centered fiber into itself. Therefore

```
T_a(K_k) ⊂ K_k almost everywhere.
```

If some T_a(x), x∈K_k, were outside the closed K_k, an open neighborhood of x would be mapped outside K_k. Measure-regularity of K_k gives positive area in that neighborhood, and invertibility gives positive area after mapping, contradicting the almost-everywhere inclusion. Hence T_a(K_k)⊂K_k exactly. Closure gives the same statement at a=0.

D4 symmetry supplies the reflected half-segment and the other diagonal direction. In particular, K_k contains the entire segment joining (x,y) to (y,x), not merely its midpoint. Together with Addendum2, the SAME original optimal levels are coordinate-downward in both the original and diagonal coordinate systems.

## 3. Exact first-octant profile class at arbitrary size

Let K be any one of these levels, and put

```
t = max{s>=0 : (s,s) in K}.
```

It is positive for these levels, since K_0 has positive area and all later levels contain it. Any positive-quadrant point (x,y) contracts diagonally to ((x+y)/2,(x+y)/2). Consequently

```
max_(x,y in K) (|x|+|y|) = 2t.
```

Define F(y)=max{x>=0:(x,y)∈K} on 0≤y≤t. Coordinate contraction gives F(y)≥t and monotonicity. The sum bound gives F(y)≤2t-y and F(t)=t.

For 0≤y1<y2≤t, the segment from (F(y1),y1) to its coordinate interchange contains

```
(F(y1)+y1-y2, y2),
```

because y1≤y2≤t≤F(y1). Thus F(y2)≥F(y1)-(y2-y1). Therefore F is continuous, nonincreasing and1-Lipschitz, with

```
F(t)=t,   t<=F(y)<=2t-y.
```

No upper bound such as t≤1/2 is used. These conditions allow nonconcave F and nonconvex K.

Conversely a profile with these properties defines a compact D4 body by extending its first-octant region. The following parallel calculation uses only those properties, so it applies to every such body without assuming it is optimal.

## 4. Exact parallel profile for every real s≥0

For K+sD, the first-octant profile is EXACTLY

```
x_max(y) = s+F(y),        0<=y<=t,
x_max(y) = s+2t-y,        t<=y<=t+s/2.
```

Here is a full-shift proof that does not require all source heights to be eligible. Let Q(z) be the full nonnegative-quadrant upper profile of K. The right boundary at y is the maximum of Q(z)+s-|y-z| over eligible z≥0 with |y-z|≤s. Negative source heights are dominated by their positive reflection.

If y≤t, the source z=y gives s+F(y). For z≤y, the1-Lipschitz inequality gives F(z)≤F(y)+(y-z). For z≥y, monotonicity gives Q(z)≤Q(y)=F(y). Thus no eligible source exceeds s+F(y).

If t≤y≤t+s/2, the source z=t is eligible and gives s+2t-y. For z≤y, use Q(z)+z≤2t. For z≥y, use Q(z)+z≤2t and z≥y to obtain the same upper bound. Larger first-octant y is impossible because the l1 support of K+sD is2t+s. This also covers s=0 and every endpoint. D4 symmetry gives the whole set.

The argument works at arbitrary t and arbitrary s; it does not sample integer shells, assume smoothness, or import convex parallel-body formulas.

## 5. Complete nonconvex area and moment polynomials

Direct integration of that exact profile gives

```
Area(K+sD) = 8∫_0^t(F(y)-y)dy + 8ts + 2s².
```

The first-octant cap moment is

```
∫_0^t [(s+F(y))³/3 + y²(s+F(y)) - 4y³/3]dy,
```

and the triangular first-octant part is

```
∫_t^(t+s/2) [(s+2t-y)³/3 + y²(s+2t-y) - 4y³/3]dy
= s⁴/12 + ts³/3 + t²s²/2.
```

For w=s+2t, the latter integrand is w³/3-w²y+2wy²-8y³/3, with primitive w³y/3-w²y²/2+2wy³/3-2y⁴/3. Hence the full moment is

```
Moment(K+sD) = (2/3)s⁴ + (16/3)ts³ + 4t²s²
 +8∫_0^t [s²F(y) + s(F(y)²+y²)
           + F(y)³/3+y²F(y)-4y³/3]dy.
```

These are proved identities for this derived nonconvex class, not finite evaluations. In particular all integer geometric tails have exactly the Z_t(F) and N_t(F) formulas in the matching-value manuscript at ANY t, with no small-size restriction. This does not remove that manuscript's separate all-law head-collapse condition.

## 6. The genuinely coupled head now has same-height constraints

Let two such bodies have first-octant data (t,F) and (u,G). Then

```
K+D ⊂ H
```

is equivalent to

```
u >= t+1/2,
G(y) >= F(y)+1 for every0<=y<=t.
```

Necessity follows from the diagonal support and the first cap. For sufficiency, the added diamond's first-octant line segment lies on t≤y≤t+1/2. There G(y)≥G(t)-(y-t)≥2t+1-y by1-Lipschitz continuity. All other sectors follow by D4. Thus the conditions cover every full-D shift, not only axis translations.

For fixed diagonal supports t_0,...,t_L, the remaining head profiles therefore satisfy only the displayed pointwise inter-level inequalities together with their individual nonincreasing1-Lipschitz bounds. The signed profile objective is a finite sum of explicit cubic head terms and the explicit quadratic/cubic geometric-tail terms, hence convex at fixed supports. There is no irregular max-window tail left to hide.

The next missing step is substantive: eliminate this genuinely coupled profile system while preserving its1-Lipschitz continuity across changes of the active-level set, and select the diagonal supports globally. Pointwise scalar minimization that neglects those continuity and coupling constraints is NOT yet justified. No full-ε value or attaining law is asserted from this reduction alone.

This is one strengthening/tool in the same coupled research chain. Standard symmetrization and layer-cake methods are PRIOR; no independent discovery count or verification promotion is attached.
