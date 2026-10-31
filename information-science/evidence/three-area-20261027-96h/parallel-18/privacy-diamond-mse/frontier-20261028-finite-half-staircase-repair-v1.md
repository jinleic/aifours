# Exact finite-epsilon TV bracket for the half-offset product

**AUTHOR CANDIDATE — WRITTEN with explicitly nonrigorous Decimal illustrations; NOT independently reviewed or parent-adopted.** Native pre-write observation: `Wed Oct 28 20:20:49 PDT 2026`.

## 1. Exact finite bracket between actual model classes

For epsilon>0, put b=e^(-epsilon), and let Q be the product of two actual 1D epsilon-private symmetric half-offset staircases. Q is an auxiliary law, not a pure-full-D private 2D mechanism. Let P be the ACTUAL 2D full-D-private diamond staircase with the SAME half offset. The written source-independent finite-epsilon bracket is

    b(1-b)/(1+b)^3
       <= inf_(mu full-D epsilon-private) TV(mu,Q)
       <= TV(P,Q)
       = (1-b)(2b^2+5b+1)/[2(1+b)^2(1+6b+b^2)].                       (1)

In particular the general infimum is globally over all Borel private laws, not restricted to radial laws. The RHS is the exact distance to the specified feasible P, not a claimed exact finite-b nearest-private solution. Expanding both sides gives

    epsilon/8-epsilon^3/24+O(epsilon^5)
      <= inf TV <= epsilon/8+3epsilon^2/64+O(epsilon^3).                  (2)

At epsilon=ln 2 the exact bracket is `[2/27,16/153]`. This source-independent finite calculation is a concrete refinement of the unreviewed global first-order result d62; neither input nor optimizer/source correspondence is used in its proof.

## 2. The finite lower bound from four disjoint shifts

Let H+ be the positive-axis union of the intervals immediately before each half-offset downward jump, each of width 1/2; H-=-H+. Its exact 1D mass is `a=1/[2(1+b)]`. For each sign pair sigma in {+,-}^2 put A_sigma=H_sigma1 x H_sigma2 and shift by `(sigma1/2,sigma2/2)` to get B_sigma. The four A_sigma are disjoint and the four B_sigma are disjoint by quadrants. Each shift is in the original full D, so any private mu satisfies `mu(union B_sigma)>=b mu(union A_sigma)`.

For the product Q, the shifted density is b^2 times the initial one on each A_sigma. Hence `Q(union A_sigma)=4a^2`, `Q(union B_sigma)=4b^2 a^2`. Comparing both events to any mu using total variation gives

    TV(mu,Q) >=4b(1-b)a^2/(1+b)=b(1-b)/(1+b)^3,

which is the exact finite lower bound in (1).

## 3. Exact TV to the feasible radial staircase

Put `m=b/(1-b)`, `z=m+1/2`. The 1D normalizer is `Z1=2z`; the 2D radial half-offset normalizer is `Z2=2(2m^2+2m+1/4)`. Thus for radial and product shell indices n_R,n_1,n_2,

    q/p=C b^(n_1+n_2-n_R),
    C=Z2/Z1^2=(1+6b+b^2)/[2(1+b)^2],
    b<C<1.                                                             (3)

Write `r_i=|x_i|=n_i+u_i`; if n_i=0 then `u_i in [0,1/2]`, otherwise `u_i in (-1/2,1/2]`. The integer difference `n_1+n_2-n_R` is -1,0 or 1, and it is -1 EXACTLY on the triangle `u_1+u_2>1/2`. Since b<C<1, Q's density exceeds P's ONLY there. For every pair of n_1,n_2>=0, the triangle's area is 1/8, including either central coordinate. Summing all four sign quadrants and both geometric indices gives

    Q(q>p)=1/[2(1+b)^2].                                                 (4)

On that set p/q=b/C. Therefore

    TV(P,Q)=Q(q>p)(1-b/C),

and elementary factoring gives the right side of (1). This proof explicitly handles the central shells; no numerical integration is involved.

## 4. Checks and scope

A 70-digit Python Decimal cell evaluated the exact rational functions at epsilon=0.1,0.05,0.02,0.01; the upper's `[TV-epsilon/8]/epsilon^2` values were approximately 0.04577585, 0.04633965, 0.04666433, 0.04677025, consistent with 3/64. They are point diagnostics, not interval certificates. All geometric identities and (1)–(2) are WRITTEN, with no named research theorem imported, formal proof, independent review, novelty, or parent adoption. Suggested review: all central-shell triangles, the normalization ratio C and the signs of its three possible likelihood levels.
