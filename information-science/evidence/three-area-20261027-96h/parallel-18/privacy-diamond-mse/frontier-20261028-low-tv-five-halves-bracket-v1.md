# A b^(5/2) coefficient bracket for global TV privacy repair

**AUTHOR CANDIDATE — WRITTEN with exact rational subchecks; NOT independently reviewed or parent-adopted.** Native pre-write observation: `Wed Oct 28 20:39:23 PDT 2026`.

## 1. Statement and dependency

Let Q be the product of the two half-offset 1D staircases, and `T_*(b)=inf_(mu original full-D pure-private)TV(mu,Q)`. Condition on the all-law finite inequality in the unreviewed source-independent candidate `frontier-20261028-third-order-global-tv-repair-v1.md`, SHA-256 `97b01f8b4f25d1529a60a01e836c360088b69b3dcb5f2a4b098ed1ae9d366594`. The written refinement is

    2b-4b^(3/2)-2b^(5/2)+O(b^3) <= T_*(b)
       <=2b-4b^(3/2)+8b^(5/2)+O(b^3).                                 (1)

Thus, if the b^(5/2) coefficient limit exists, it lies in [-2,8]; no existence or exact coefficient is claimed. As usual a lower `+O(b^3)` means a possibly negative bounded error. The upper is an actual clipped-square full-D-private law, not a relaxed model. The original all-law lower remains conditional on the pinned unreviewed 97b proof.

## 2. Exact lower expansion

The import gives, for all sufficiently small-T competitors and b<1/2,

    (1-b-2b^2)T+(b+2b^2)sqrt(8q0 T)
       >=(2b+4b^2)(1-b)q0,   q0=[(1-b)/(1+b)]^2.                       (2)

Its increasing positive root, expanded with `s=sqrt(b)`, is

    2s^2-4s^3+0*s^4-2s^5+O(s^6).                                       (3)

For T outside the import's small-deficit range the asymptotic lower is trivial, so the case split does not narrow the class. Matching powers in (2) gives the -2 directly; no new finite-b lower theorem is asserted beyond (2).

## 3. Sharper actual clipped-square upper

Set s=sqrt(b), t=s-b and `K_t=[-1/2,1/2]^2 intersect {||x||_1<=1-t}`. The true full-D shell P_t has core area `A=1-2t^2` and

    Z=A+(6-4t)m+4m^2, m=b/(1-b),
    Q(S)=q0, P_t(S)=[A+b(1-A)]/Z, S=[-1/2,1/2]^2.

`q0 Z=1+4b^2+O(b^(5/2))>1`, so Q dominates P_t on S. Exact series division to one more order gives

    Q(S)-P_t(S)=2b-4b^(3/2)-4b^2+16b^(5/2)+O(b^3).                  (4)

The first-Q-index strips excluded by K_t+D have exact total area 4t^2 and density difference `b(q0-b/Z)`. Their contribution is

    4t^2 b(q0-b/Z)=4b^2-8b^(5/2)+O(b^3).                               (5)

Inside K_t+D, the positive difference on these strips is only O(b^3).

For Q index 2, the part where P_t index 3 has total area `6t^2`: four t^2 from the outer one-coordinate strips and two t^2 from four diagonal corner triangles. It contributes O(b^3). Where both indices are 2 the density difference is O(b^4) on bounded area; where P_t index is 1, Q-P_t is negative. Q index>=3 has total mass O(b^3). Therefore the entire outside positive part equals (5)+O(b^3), giving

    TV(Q,P_t)=2b-4b^(3/2)+8b^(5/2)+O(b^3).                             (6)

This single actual law proves the upper in (1). The assertion of exact `6t^2` covers t<1/2 and follows from the same corner clips at S+2D; no numeric integration is assumed.

## 4. Actual checks and limits

The Python eval kernel used `fractions.Fraction` at s=1/100 and 1/1000 to evaluate the exact core deficit plus first-strip contribution. The residual divided by b^(5/2) was about 7.6445 and 7.9640, respectively. These are rational subchecks with decimal renderings, not a full TV computation. The lower explicitly depends on unreviewed 97b, and the new index-2 geometry, expansion and global coefficient bracket are WRITTEN without independent review or formal verification. No novelty, finite-b exact nearest law, coefficient-existence or parent adoption is claimed. Review should check index-2 omitted area 6t^2, positivity signs, s^5 expansion and all O(b^3) tails.
