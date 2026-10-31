# Third-order bracket for global low-privacy TV repair

**AUTHOR CANDIDATE — WRITTEN with exact rational subchecks; NOT independently reviewed or parent-adopted.** Native pre-write observation: `Wed Oct 28 20:35:02 PDT 2026`.

## 1. Statement and pinned dependency

For Q equal to the product of the two half-offset 1D epsilon-private staircases, let `T_*(b)=inf_(mu full-D pure-epsilon private)TV(mu,Q)` and b=e^(-epsilon). Condition on the explicit all-law finite lower of the unreviewed source-independent candidate `frontier-20261028-second-order-global-tv-repair-v1.md`, SHA-256 `36b8de16c1306d14cc396bd0ab270556a974b1a8146f76c9705cd54efa4fc6ae`. Its exact root expands as

    T_*(b) >= 2b-4b^(3/2)-8b^2+O(b^(5/2)).                             (1)

A sharper explicitly constructed ACTUAL full-D-private clipped-square shell gives

    T_*(b) <= 2b-4b^(3/2)+O(b^(5/2)).                                  (2)

In particular if a third coefficient limit exists, it lies in [-8,0]; its existence or exact value is NOT claimed. Formula (2)'s trial geometry is rederived below. Neither bound implies an exact finite-b nearest-private law.

## 2. Actual trial and core deficit

Put s=sqrt(b), `t=s-b`, `S=[-1/2,1/2]^2`, and `K_t=S intersect {||x||_1<=1-t}`. The geometric shell P_t around K_t is an ACTUAL full-D-private law. With `A=1-2t^2`, `m=b/(1-b)`,

    Z=A+(6-4t)m+4m^2,
    P_t(S)=[A+b(1-A)]/Z,
    Q(S)=q0=[(1-b)/(1+b)]^2.                                             (3)

For t=s-b, `q0 Z=1+4b^2+O(b^(5/2))>1`, so Q's density dominates P_t's everywhere inside S for small b. Exact series division gives

    Q(S)-P_t(S)=2b-4b^(3/2)-4b^2+O(b^(5/2)).                          (4)

## 3. Exact b^2 cancellation outside the core

Q's one-index region outside S consists of four strips. Inside K_t+D, Q and P_t have first-shell densities `b q0` and `b/Z`, so their positive difference has integral O(b^3), since `q0 Z-1=O(b^2)`. The portion of these strips NOT in K_t+D consists of eight right triangles of total area exactly `4t^2`. On them P_t has shell index 2, giving positive difference density `b q0-b^2/Z`; their contribution is

    4t^2 b(q0-b/Z)=4b^2+O(b^(5/2)).                                     (5)

The Q index-2 region lies in S+2D. Where P_t has index 2, its positive density difference is O(b^4) on a bounded region; where P_t has index 3, that region is contained in `(S+2D)\(K_t+2D)` of area `2t^2+8t=O(s)`, so its Q mass is O(b^(5/2)). Q index>=3 has mass O(b^3). These estimates use actual shell indices, not a radial approximation.

As Q dominates P_t on S, total variation is the core deficit plus outside positive differences. Combining (4)–(5) proves (2), including the cancellation of the two b^2 terms.

## 4. Finite lower expansion and actual checks

The pinned 36b lower solves `(1+b)T+b sqrt(8q0 T)>=2b(1-b)q0`. Put s=sqrt(b), `T=2s^2-4s^3+c s^4+...`; exact coefficient matching gives c=-8, establishing (1).

The Python eval kernel used `fractions.Fraction` at (b,t)=(10^-4,99/10000) and (10^-6,999/10^6), checking the exact normalizer, sign q0Z>1, and core-deficit plus 4t^2 strip contribution. Their residual divided by b^2 was about 0.07645 and 0.007964, respectively; these decimal displays are diagnostics, not a full-TV computation or proof. The all-law lower remains conditional on unreviewed 36b; the trial construction and shell estimates are WRITTEN and unreviewed. No formal/independent review, novelty or parent acceptance is claimed. Review should focus on exact strip-area 4t^2, index-2 omission containment and the error orders.
