# Sharp low-privacy global TV repair of the half-offset product

**AUTHOR CANDIDATE — WRITTEN plus bounded exact Fraction checks; NOT independently reviewed or parent-adopted.** Native pre-write observation: `Wed Oct 28 20:26:45 PDT 2026`.

## 1. Source-independent exact bounds and asymptotic

Let b=e^(-epsilon) in (0,1), let Q be the product of two actual 1D epsilon-private half-offset staircases, and let

    T_*(b)=inf_(mu original FULL-D pure-epsilon private) TV(mu,Q).

Q is an auxiliary product and is not asserted to satisfy full-D 2D privacy. For ANY 0<delta<1 define

    q0=[(1-b)/(1+b)]^2,
    L_delta= [2b(1-delta)^2 q0(1-b)]
              /[1+32b(1-delta)^2/delta^2],
    U_square=2b(1-b)(1+2b-b^2)/[(1+b)^2(1+4b-b^2)].                   (1)

The written source-independent exact bounds are

    L_delta(b) <= T_*(b) <= U_square(b).                                 (2)

The upper side is attained as a comparison by an explicitly constructed ACTUAL full-D-private square-core shell law. Taking delta=b^(1/3) gives the globally sharp low-privacy asymptotic

    T_*(b)=2b+O(b^(4/3))   as b->0.                                     (3)

The infimum here is over ALL Borel full-D-private laws, not only square-core or radial laws. No claim that the specific square-core law is the exact finite-b closest law is made.

For comparison, the separately written unreviewed high-privacy result d62 has `T_*=epsilon/8+O(epsilon^2)` as b->1. That result is not an input to (1)–(3).

## 2. Explicit finite lower bound from the corner triangles

Let `S=[-1/2,1/2]^2`, and T=TV(mu,Q). The product Q has constant density q0 on S. In each quadrant define a corner triangle by x=(sign1(1/2+a),sign2(1/2+c)) with a,c>0 and a+c<1-delta. Let K_delta be the four-triangle union; its exact area is `2(1-delta)^2`. Q's density on K_delta is `b^2 q0`.

In the corresponding corner of S take the square C_sigma with side delta/4. For EVERY y in that quadrant's K_delta and EVERY x in C_sigma, `||y-x||_1<1`: their distance is at most `(1-delta)+delta/2`. A full-private mu has an all-point bounded density f, and privacy implies

    f(y) >= b mu(C_sigma)/|C_sigma|.

Since `mu(C_sigma)>=Q(C_sigma)-T=q0 delta^2/16-T`, integrate over the four triangles and subtract `Q(K_delta)=b^2 q0 |K_delta|`. Using `T>=mu(K_delta)-Q(K_delta)` gives

    T[1+16b |K_delta|/delta^2] >=b(1-b)q0 |K_delta|,

which is the displayed L_delta in (1). If the intermediate lower estimate of mu(C_sigma) is negative, the inequality remains valid; no unstated positivity assumption is made. No optimizer existence, centeredness or symmetry of mu is used.

## 3. Actual square-core shell and exact TV

Take the genuine full-D-private shell law P_S with core S and density `b^n/Z_S`, `n=min{k:x in S+kD}`. For t>=0,

    |S+tD|=1+4t+2t^2,
    Z_S=1+6m+4m^2,   m=b/(1-b).

The 1D normalizer of Q is `Z1=1+2m`. Define `a_i=max(|x_i|-1/2,0)`, `n_i=ceil(a_i)`, `n_S=ceil(a_1+a_2)`. Then `k=n_1+n_2-n_S` is 0 or 1 almost everywhere and

    q/p_S = C b^k,   C=Z_S/Z1^2>1,   Cb<1.                             (4)

The event k=1 requires both coordinates outside the core; in each pair of outside unit shells it is a triangle of area 1/2. Summing geometric weights and quadrants gives

    Q(k=1)=2m^2/(1+2m)^2,
    TV(Q,P_S)=Q(k=1)[1/(Cb)-1]=U_square(b).                               (5)

P_S is fully private because a D shift changes its shell index by at most 1. From (1)–(2), choosing delta=b^(1/3) gives `L_delta=2b-O(b^(4/3))`, while `U_square=2b+O(b^2)`, proving (3).

## 4. Exact sample arithmetic and limits

The eval kernel used `fractions.Fraction` to evaluate the exact square-shell upper against the separate half-diamond radial upper. At b=1/10, U_square=`2142/16819` while the radial upper is `6840/19481`; at b=1/2, U_square=`14/99` while the radial upper is `16/153`. These comparisons concern two actual feasible repair laws, not the exact T_* at those b. The all-law lower, square-core geometry and asymptotic remain WRITTEN, not formal, independently reviewed, novelty-cleared or parent-adopted. Suggested review: corner-averaged privacy bound, the delta denominator, Minkowski square area and the ceiling-difference triangle.
