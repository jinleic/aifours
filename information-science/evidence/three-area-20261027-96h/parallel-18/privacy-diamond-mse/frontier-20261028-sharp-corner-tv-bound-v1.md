# Sharper corner-overlap lower bound for global TV privacy repair

**AUTHOR CANDIDATE — WRITTEN; NOT independently reviewed or parent-adopted.** Native pre-write observation: `Wed Oct 28 20:27:55 PDT 2026`.

## 1. Exact lower bound and improved asymptotic

Let Q be the product of the two 1D half-offset epsilon-private staircases, b=e^(-epsilon), and let T_*(b) be the infimum of TV(mu,Q) over ALL original full-D pure-epsilon-private Borel laws. Write `q0=[(1-b)/(1+b)]^2`. For every 0<delta<1 the source-independent WRITTEN bound is

    T_*(b) >= 2b(1-b)q0(1-delta)^2 /
               [1+8b(1/delta+log(delta)-1)].                             (1)

An actual full-D-private square-core shell has exact TV

    U_square(b)=2b(1-b)(1+2b-b^2)/[(1+b)^2(1+4b-b^2)].                   (2)

Thus `T_*<=U_square`. Choosing delta=2sqrt(b) for b<1/4 gives the sharper globally valid low-privacy asymptotic

    T_*(b)=2b+O(b^(3/2)),       b->0.                                    (3)

The leading coefficient matches the earlier unreviewed 5f2 candidate, but the error improves its O(b^(4/3)) to O(b^(3/2)). No exact finite-b nearest-private law is asserted.

## 2. Integrating the actual variable overlap

Let `S=[-1/2,1/2]^2`, T=TV(mu,Q), and in each corner quadrant use `y=(sign1(1/2+a),sign2(1/2+c))`, a,c>0. For a+c<1, put `d=1-a-c`. The part of S within the unit diamond of y is EXACTLY the corresponding core-corner triangle

    C_y={u,v>=0:u+v<=d},   |C_y|=d^2/2,

where u,v are inward distances from that S corner. The all-point private density f satisfies `f(y)>=b mu(C_y)/|C_y|`, while Q's core density is q0, so

    f(y)>=b[q0-2T/d^2].                                                   (4)

Use this inequality only in the four triangles `K_delta={a,c>0,a+c<1-delta}`. Their total area is `2(1-delta)^2`, and Q has density b^2 q0 there. Integrating (4), using `T>=mu(K_delta)-Q(K_delta)`, and parameterizing `r=a+c` gives

    T >= 2b(1-b)q0(1-delta)^2
          -8b T integral_0^(1-delta) r/(1-r)^2 dr.

The elementary integral is `1/delta+log(delta)-1`, proving (1). The intermediate bracket in (4) may be negative; the resulting inequality remains valid. Each C_y is a legitimate Borel event, and the TV bound applies simultaneously for every y.

## 3. Actual upper law and rate

Let P_S be the explicit full-D-private geometric shell with core S. Direct shell geometry gives `|S+tD|=1+4t+2t^2`. Its normalizer is `1+6m+4m^2` with m=b/(1-b), while Q's product normalizer is `(1+2m)^2`. The shell-index difference is 0 or 1; summing the two-outside-coordinate triangles gives exactly (2). This is an actual law, not a relaxed cap construction.

For delta=2sqrt(b), the lower numerator in (1) is `2b[1-O(sqrt(b))]` and the denominator is `1+O(sqrt(b))`; (2) is `2b+O(b^2)`. These two inequalities establish the global asymptotic (3).

## 4. Status

No numeric, formal, independent-model or human verification was performed. The proof uses original all-event full-D privacy, a pointwise density representative, exact overlap geometry and the explicit square shell; it imports no named research theorem. No novelty, exact finite-b attainment or parent acceptance is claimed. Suggested disjoint review: the exact shape of C_y, the integral and four-quadrant factors, and the ceiling-index TV identity for the upper law.
