# Improved [0,4] b^(5/2) bracket for global TV repair

**AUTHOR CANDIDATE — WRITTEN plus exact Fraction series subchecks; NOT independently reviewed or parent-adopted.** Native pre-write observation: `Wed Oct 28 20:41:45 PDT 2026`.

## 1. Statement and scope

Let Q be the product of the two symmetric 1D half-offset epsilon-private staircases, b=e^(-epsilon), and let `T_*(b)` be its nearest TV distance over ALL original full-closed-D pure-epsilon-private 2D Borel laws. The written source-independent improvement is

    2b-4b^(3/2)+O(b^3) <= T_*(b)
       <=2b-4b^(3/2)+4b^(5/2)+O(b^3).                                 (1)

If the b^(5/2) coefficient limit exists it lies in [0,4]; existence is NOT claimed. The lower is sharpened using an additional genuine full-D privacy floor INSIDE each core-corner triangle; the upper uses an actual clipped-square private shell with a refined offset. This is not an exact finite-b nearest-law result or a claim of novelty.

## 2. Height bound from privacy INSIDE the core

Let f be any full-D-private density, T=TV(mu,Q), `S=[-1/2,1/2]^2`, `q0=[(1-b)/(1+b)]^2`, and `e=(q0-f)_+` on S. As before `integral_S e<=T`. In each corner let C_sigma(d) be the inward core triangle of depth d, and `h_sigma(d)=essinf_(C_sigma(d))e`.

The corner triangle C_sigma(1/2) has area 1/8 and l1 diameter exactly 1. Thus every pair of its points is related by an allowed D shift. Since Q has density q0 on it and `mu(C)>=q0/8-T`, privacy gives, for every x in C,

    f(x)>=b[q0-8T].

For small b and T<=3b, this lower is positive; consequently every h_sigma(d), including d>1/2 by monotonicity, is at most

    H=q0(1-b)+8bT.                                                       (2)

This is strictly stronger at the required order than the height q0 used in earlier lower bounds.

## 3. Two outer shells and improved lower root

The four disjoint core triangles of depth 1/2 give `sum_sigma integral_0^(1/2)d h_sigma(d)dd<=T`. The SAME exact layer-cake optimization as in 97b, with height H instead of q0, gives for `T<=H/8`

    sum_sigma integral_0^1(1-d)h_sigma(d)dd <=sqrt(8HT)-T.               (3)

For completeness, its scalar ingredients are `J(r)=r-r^2/2`, `K(r)=min(r,1/2)^2/2`: with `r0=sqrt[T/(2H)]<=1/4`, `lambda=1/r0-1`, one has `J(r)-lambda K(r)<=r0/2` for all r in [0,1]. Integrating superlevel radii, summing four corners and using the core deficit budget gives (3).

The one-step outer-corner set K1 has area 2 and Q density b^2 q0; the disjoint two-step set K2 (one outward coordinate >1, a+c<2) has area 4 and Q density b^3 q0. Their full-D/group privacy floors are `b(q0-h_sigma)` and `b^2(q0-h_sigma)`, with cross-sections `(1-d)` and `2(1-d)`, respectively. As `T>=mu(K1 union K2)-Q(K1 union K2)`, (3) yields

    (1-b-2b^2)T+(b+2b^2)sqrt[8T(q0(1-b)+8bT)]
       >=(2b+4b^2)(1-b)q0.                                              (4)

For b small the left side is increasing in T. Its unique positive root is `2b-4b^(3/2)+0*b^2+0*b^(5/2)+O(b^3)`. The actual square-core shell gives an O(b) trial, so minimizing sequences may be restricted to T<=3b; any law outside that range trivially obeys the claimed asymptotic lower. Hence the lower in (1) holds for the GLOBAL infimum.

## 4. Refined true-private clipped-square upper

Set s=sqrt(b), `t=s-s^2+s^3-2s^4`, S as above, `K_t=S intersect {||x||_1<=1-t}`, and let P_t be its actual full-D-private geometric shell. With `A=1-2t^2`, `m=b/(1-b)` and `Z=A+(6-4t)m+4m^2`, the Q core density satisfies

    q0 Z-1=4s^5+O(s^6)>0.                                                (5)

So Q dominates P_t on S. Its signed core deficit plus the exact positive first-strip omitted triangles of area 4t^2 is

    Q(S)-P_t(S)+4t^2 b(q0-b/Z)
       =2s^2-4s^3+4s^5+O(s^6).                                          (6)

The remaining positive outside parts are O(s^6): the rest of Q's first-index strips is O(b^3), the Q-index-2/P-index-3 area is exactly 6t^2 and costs O(b^3), and Q-index>=3 has mass O(b^3). Thus `TV(Q,P_t)=2b-4b^(3/2)+4b^(5/2)+O(b^3)`, proving the upper in (1).

## 5. Actual checks and limits

The Python eval kernel used exact `fractions.Fraction` truncated power-series arithmetic for the trial. It found `q0Z-1=4s^5+4s^6-16s^7+...` and `core+first strips=2s^2-4s^3+4s^5+0s^6-20s^7+...`; these checks do NOT include the other shells. A separate Decimal root diagnostic for (4) suggested the b^(5/2) lower coefficient tends to 0; it is not an interval certificate. All privacy, layer-cake, shell and asymptotic claims are WRITTEN, not formally or independently verified, novel by assertion or parent-adopted. Priority review: triangle diameter and averaged height, dependence H(T), small-T range, root monotonicity, and the optimized core sign.
