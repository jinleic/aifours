# Sharp second-order global TV privacy repair

**AUTHOR CANDIDATE — WRITTEN with explicitly nonrigorous Decimal root illustrations; NOT independently reviewed or parent-adopted.** Native pre-write observation: `Wed Oct 28 20:33:08 PDT 2026`.

## 1. Exact finite lower and matching second-order global asymptotic

Let Q be the product of the two actual 1D epsilon-private symmetric HALF-offset staircases, b=e^(-epsilon), and let `T_*(b)=inf_(mu full-D pure-epsilon private)TV(mu,Q)` over ALL original Borel laws. Q is an auxiliary product, not a full-D private 2D mechanism. Define

    q0=[(1-b)/(1+b)]^2,
    A_b=b sqrt(8q0),    B_b=2b(1-b)q0.                                  (1)

The source-independent written finite bound is

    T_*(b) >= [2B_b/(A_b+sqrt(A_b^2+4(1+b)B_b))]^2.                     (2)

An actual full-D-private clipped-square shell gives the matching SECOND-ORDER expansion

    T_*(b)=2b-4b^(3/2)+O(b^2),      b->0.                                (3)

This improves both the error-only low-privacy result and the coefficient interval in the earlier unreviewed `frontier-20261028-clipped-square-tv-correction-v1.md` SHA `933d9c66478356a13aab82d00f1c53ea988935433f053a19f685c6c03cbad94b`. Neither prior candidate nor any named research theorem is imported into this proof. Equation (3) is a global infimum claim, not an exact finite-b optimizer or novelty claim.

## 2. All-point floor and a core-deficit budget

Fix ANY actual full-D-private mu, write T=TV(mu,Q), and let f be its bounded all-point density representative. Let S=[-1/2,1/2]^2; Q's density on S is q0. Set `e(x)=(q0-f(x))_+` on S. By the definition of TV,

    integral_S e <=T,       0<=e<=q0.                                    (4)

At each of the four S corners, let C_sigma(d) be the inward right triangle of depth d in (0,1), and define

    h_sigma(d)=essinf_(x in C_sigma(d)) e(x).

Each h_sigma is measurable, nonincreasing, and lies in [0,q0]. For a point y outside both corresponding sides, with outward distances a,c>0, a+c<1, let d=1-a-c. Its exact overlap `S intersect (y-D)` is C_sigma(d). Privacy therefore gives the POINTWISE lower envelope

    f(y)>=b[q0-h_sigma(d)].                                               (5)

This is an essential-SUPREMUM privacy floor; unlike an average over C_sigma(d), it can exploit the geometry of all points in the overlap.

## 3. A sharp universal bound on lost corner floor

The four core-corner triangles of depth 1/2 are pairwise disjoint up to null boundaries. Monotonicity of h and (4) imply

    sum_sigma integral_0^(1/2) d h_sigma(d)dd <=T.                        (6)

For `H_sigma=integral_0^(1/2)h_sigma(d)dd`, the bounded-density bathtub inequality gives

    integral_0^(1/2) d h_sigma(d)dd >=H_sigma^2/(2q0).                   (7)

Indeed among 0<=h<=q0 with fixed integral, concentrating height q0 nearest d=0 minimizes the first moment. Cauchy–Schwarz and (6) imply `sum H_sigma<=sqrt(8q0 T)`.

For d>=1/2, monotonicity gives `h_sigma(d)<=h_sigma(1/2)`. Since `integral_(1/2)^1(1-d)dd=1/8` and `integral_0^(1/2)d h_sigma(d)dd>=h_sigma(1/2)/8`, the total weighted tail over the four corners is at most T. Consequently

    sum_sigma integral_0^1 (1-d)h_sigma(d)dd <=sqrt(8q0 T)+T.             (8)

Let K be the four outside corner triangles a,c>0,a+c<1. Their total area is 2, Q's density there is b^2 q0, and integration of (5), using T>=mu(K)-Q(K), gives

    (1+b)T+b sqrt(8q0 T) >=2b(1-b)q0.                                   (9)

Solving this monotone quadratic in sqrt(T) gives (2) for EVERY private mu. Since q0=1+O(b), (2) expands to `2b-4b^(3/2)+O(b^2)` as a LOWER bound.

## 4. Matching ACTUAL clipped-square upper

Choose `t=sqrt(b)-2b>0` and take core `K_t=S intersect {||x||_1<=1-t}`. Its genuine full-D-private geometric shell has `A=1-2t^2`, `m=b/(1-b)`,

    Z_t=A+(6-4t)m+4m^2,
    P_t(S)=[A+b(1-A)]/Z_t,
    Q(S)=q0.                                                              (10)

The normalization follows from the exact Minkowski area `|K_t+kD|=A+(4-4t)k+2k^2`. Here `q0 Z_t=1+4b^(3/2)+O(b^2)>1`, so q>=p_t on S. Outside S, the positive part `(q-p_t)_+` has mass O(b^2): on first-coordinate strips inside K_t+D the two densities are b[1+O(b)]; the omitted strip corners have total area <=4t^2; and Q's remaining shell-index>=2 mass is O(b^2). Therefore

    TV(Q,P_t)<=Q(S)-P_t(S)+O(b^2)
             =2b-4bt+O(b^2)
             =2b-4b^(3/2)+O(b^2).                                        (11)

The implicit constants are absolute for small b. Combining (2) and (11) proves the global expansion (3).

## 5. Checks, scope and review targets

A 60-digit Python Decimal cell evaluated only the positive-root formula in (2) at b=10^-4,10^-6,10^-8; `[lower-2b+4b^(3/2)]/b^2` was approximately -7.7789,-7.9780,-7.9978. These are point diagnostics, not interval proofs or exact-optimality checks. The floor/deficit geometry, bathtub constant and matching clipped-shell error are WRITTEN, source-independent and unreviewed. No exact finite-b optimum, formal proof, independent model/human review, novelty or parent acceptance is claimed. High-priority review should check (5) for all overlaps, the nested-triangle/Fubini step (6), the bounded-height inequality (7), tail factor in (8), and the upper core sign/strip estimates.
