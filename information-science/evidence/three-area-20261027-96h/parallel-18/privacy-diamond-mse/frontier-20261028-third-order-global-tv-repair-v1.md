# The b^2 coefficient of global low-privacy TV repair is zero

**AUTHOR CANDIDATE — WRITTEN with explicitly nonrigorous Decimal root diagnostics; NOT independently reviewed or parent-adopted.** Native pre-write observation: `Wed Oct 28 20:37:41 PDT 2026`.

## 1. Source-independent all-law claim

Let Q be the product of the two symmetric half-offset 1D epsilon-private staircases, b=e^(-epsilon), and let `T_*(b)` be its nearest TV distance to ALL original pure-epsilon-private 2D Borel laws for the FULL closed l1 unit diamond. As b->0, the written claim is the sharpened global expansion

    T_*(b)=2b-4b^(3/2)+O(b^(5/2)).                                       (1)

Thus its b^2 coefficient is EXACTLY zero. The upper is realized to this order by a genuine clipped-square full-D-private shell, and the lower uses EVERY competing original private law. This closes the [-8,0] b^2 coefficient interval left in the earlier unreviewed 3464 candidate; that candidate is neither edited nor imported. No finite-b exact optimality, novelty, formal proof, independent review or parent acceptance is claimed.

## 2. Core deficits and the two disjoint outer shells

Write S=[-1/2,1/2]^2, `q0=[(1-b)/(1+b)]^2`, T=TV(mu,Q), and `e=(q0-f_mu)_+` on S. Then 0<=e<=q0 and `integral_S e<=T`. For each corner sigma and 0<d<1, let C_sigma(d) be the inward core triangle of depth d, and set `h_sigma(d)=essinf_(C_sigma(d))e`. The four triangles of depth 1/2 are disjoint up to null sets, and h_sigma are nonincreasing, so

    sum_sigma integral_0^(1/2) d h_sigma(d)dd <=T.                       (2)

Let K1 be the four outside corner triangles in coordinates a,c>0 with a+c<1. For y in K1, its overlap with the core after ONE D shift is C_sigma(1-a-c); Q density there is b^2 q0.

Let K2 be the four outside regions with a,c>0, a+c<2 and exactly one of a,c>1. The sets K1,K2 are disjoint. On K2 the product Q density is b^3 q0, and y's core overlap after TWO D shifts is C_sigma(2-a-c). Full group privacy gives, with the same h_sigma,

    f_mu(y)>=b^j[q0-h_sigma(j-a-c)]  for y in K_j, j=1,2.              (3)

K1 has total area 2, K2 total area 4. At a fixed depth d, K1 has per-corner cross-section length 1-d and K2 has twice that length. Set

    F=sum_sigma integral_0^1 (1-d)h_sigma(d)dd.                           (4)

Since the sets are disjoint, `T>=mu(K1 union K2)-Q(K1 union K2)`, and (3) gives

    T >= (2b+4b^2)(1-b)q0-(b+2b^2)F.                                   (5)

## 3. Sharp small-deficit bound on F

For sufficiently small T, the exact inequality is

    F <= sqrt(8q0 T)-T.                                                  (6)

Here is a complete bounded-height argument. For a nonincreasing h in [0,q0], layer-cake write its superlevel lengths as r in [0,1]. For a given r, the objective and the constrained first moment in (2) are

    J(r)=r-r^2/2,       K(r)=min(r,1/2)^2/2.

For any r0 in (0,1/4] set lambda=1/r0-1. On r<=1/2, the maximum of `J(r)-lambda K(r)` occurs at r0 and equals r0/2. On r>=1/2, it is at most `1/2-lambda/8<=r0/2`; the last comparison is exactly `4r0^2-5r0+1>=0`. Integrating this bound over all heights gives, for each corner,

    integral_0^1(1-d)h(d)dd <= q0 r0/2+lambda integral_0^(1/2)d h(d)dd.

Summing four corners and using (2), choose `r0=sqrt[T/(2q0)]<=1/4`. The result is exactly (6). Monotone functions have only countably many discontinuities, which justifies the nested-triangle/essential-infimum integration in (2).

For b sufficiently small, any law with T>q0/8 already satisfies the desired O(b) lower; otherwise (6) applies. Combining (5)–(6) yields

    (1-b-2b^2)T+(b+2b^2)sqrt(8q0 T)
        >=(2b+4b^2)(1-b)q0.                                             (7)

The left side is strictly increasing in T for b<1/2. Its positive root has expansion `2b-4b^(3/2)+0*b^2+O(b^(5/2))`; the zero coefficient follows by putting T=`2s^2-4s^3+c s^4+...`, s=sqrt(b), into (7), where matching the s^4 term forces c=0.

## 4. Matching actual clipped-square upper

Take `t=sqrt(b)-b` and core `K_t=S intersect {||x||_1<=1-t}`. The exact full-D-private shell around it has area A=1-2t^2 and normalizer

    Z=A+(6-4t)m+4m^2,  m=b/(1-b),
    Q(S)=q0,  P_t(S)=[A+b(1-A)]/Z.                                      (8)

Here `q0 Z=1+4b^2+O(b^(5/2))>1`. Thus Q dominates P_t on S, and exact expansion gives

    Q(S)-P_t(S)=2b-4b^(3/2)-4b^2+O(b^(5/2)).                          (9)

Outside S, the positive Q-P part in the first Q-index strips comes from eight omitted corner triangles of total area 4t^2, giving `4b t^2(q0-b/Z)=4b^2+O(b^(5/2))`; elsewhere in these strips it is O(b^3). The positive part with Q index 2 is O(b^(5/2)) because the only P-index-3 portion lies in `(S+2D)\(K_t+2D)` of area `2t^2+8t=O(sqrt b)`; its other index-2 density difference is O(b^4). Q index>=3 has mass O(b^3). Therefore

    TV(Q,P_t)<=2b-4b^(3/2)+O(b^(5/2)),                                  (10)

matching the all-law lower and proving (1). The shell privacy follows from the unit-change-of-index inequality; no radial or 2D-optimizer assumption is made.

## 5. Checks and review targets

A 65-digit Decimal cell evaluated only the positive root of (7) at b=10^-4,10^-6,10^-8; `[root-2b+4b^(3/2)]/b^2` was approximately -0.01881,-0.001988,-0.00019988, tending to 0. These are floating diagnostics, not interval certificates or a full-TV check. The core lower, second-shell area, layer-cake extremal inequality, zero coefficient and actual upper are WRITTEN, unreviewed arguments without named research imports. High-priority review should check K2's b^3 Q density and cross section, the layer-cake maximizer at r0, small-T case split, and the b^2 cancellation in the trial. No novelty, formal proof or parent adoption is claimed.
