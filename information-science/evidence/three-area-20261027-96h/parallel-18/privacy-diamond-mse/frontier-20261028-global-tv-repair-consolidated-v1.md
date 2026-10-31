# Complete review packet: global TV repair of a half-offset marginal product

**AUTHOR CANDIDATE — WRITTEN with bounded same-kernel exact checks; NOT independently reviewed or parent-adopted.** Native observation immediately before writing: `Wed Oct 28 20:52:27 PDT 2026`.

## 1. Exact contract, scope, and claimed bracket

Fix `b in (0,1)`, `epsilon=-log b`, and the CLOSED unit l1 diamond `D={h in R^2:||h||_1<=1}`. A probability measure mu is admissible if, for EVERY Borel event A and EVERY h in D,

    mu(A) <= b^(-1) mu(A+h).                                             (1)

The reverse follows by applying the same condition to -h. This is the original full event/full closed-D privacy model; axis-only privacy is NOT sufficient.

Let nu be the symmetric 1D half-offset staircase with density

    p1(x)=b^ceil((|x|-1/2)_+)/Z1,       Z1=(1+b)/(1-b),

The normalization follows by summing the core interval of length 1 and the two length-1 shells at each index n>=1. Since `||x+h|-|x||<=|h|<=1`, its ceiling index changes by at most 1, proving the actual 1D all-event privacy. Values on shell boundaries do not matter. Let Q=nu tensor nu. It is NOT full-D private: with A=(0,1/2)^2 and h=(1/2,1/2), `Q(A+h)=b^2 Q(A)<b Q(A)`. Its density is

    q(x)=q0 b^(n1+n2),    q0=[(1-b)/(1+b)]^2,
    ni=ceil((|xi|-1/2)_+).                                               (2)

For probability laws use the convention

    TV(mu,Q)=sup_A|mu(A)-Q(A)|=(1/2)integral|f_mu-q|,
    T_*(b)=inf_(mu satisfying (1)) TV(mu,Q).                              (3)

The equality with the density integral will be justified. The claimed **strongest consolidated result**, for all 0<b<=10^-4, is a completely specified finite bracket

    tau_b <= T_*(b) <= M_b+19 b^3,                                      (4)

where the lower root tau_b and rational upper M_b are defined exactly in §§5–6. It implies, with s=sqrt(b),

    2s^2-4s^3-O(s^6) <= T_*(b)
       <=2s^2-4s^3+4s^5+O(s^6).                                        (5)

Thus both the b^2 coefficient and the lower endpoint of the possible b^(5/2) coefficient are zero; IF the b^(5/2) coefficient limit exists, it is in [0,4]. Its existence, an exact finite-b nearest mechanism, scientific novelty and automatic acceptance are NOT claimed. The inequalities are global over ALL original Borel private laws, not only radial, convex-core or staircase candidates.

At each FIXED b, §3 establishes tightness of minimizing sequences and existence of a minimizer. This is separate from the asymptotic tightness of (5); no uniform-in-b compactness is asserted or needed.

## 2. Explicit dependency and provenance inventory

**Scientific inputs:** none from any parent target theorem, LAW642, MDA, PMLR, review verdict or external source. The entire mathematical proof is reconstructed below. Standard named mathematical tools used are Radon–Nikodym and Lebesgue differentiation, Fubini–Tonelli, Radon-measure vague compactness and regularity, Prokhorov's theorem, weak lower semicontinuity of total variation, elementary polynomial/geometry identities, and the analytic implicit-function theorem for a scalar root. Each use is identified below.

**Historical author artifacts, retained immutable and NOT imported as premises:**

* `frontier-20261028-second-order-global-tv-repair-v1.md`, SHA `36b8de16c1306d14cc396bd0ab270556a974b1a8146f76c9705cd54efa4fc6ae`;
* `frontier-20261028-third-order-global-tv-repair-v1.md`, SHA `97b01f8b4f25d1529a60a01e836c360088b69b3dcb5f2a4b098ed1ae9d366594`;
* `frontier-20261028-low-tv-five-halves-improved-v1.md`, SHA `ff76df9dc454c482c38b6f42ede640cf7e912a207d32b3e1f2fff45840e25d69`.

This packet contains the 97b/ff76 lower and optimized clipped-shell upper in one reviewable scope, with independent same-owner kernel controls but NOT an independent reviewer. Main reported that f136 was already checking its first four earlier inputs through 36b; no f136 verdict or review coverage of 97b/ff76 or this packet is asserted. Prior files remain frozen. This packet is not a proof of the original J/L optimizer or a source-equivalence/novelty result.

## 3. All-point density, positivity, fixed-b tightness and attainment

Integrating (1) over h in D, whose area is 2, gives for every Borel A

    mu(A) <= (1/(2b)) integral_D mu(A+h)dh <= |A|/(2b).                 (6)

Fubini proves the second inequality. Thus every admissible mu has a bounded density. Its ball-average limsup representative

    f(x)=limsup_(r down 0) mu(B(x,r))/|B(x,r)|

agrees with that density almost everywhere. Applying (1) to the SAME balls and taking limsups gives `f(x+h)>=b f(x)` for EVERY x and EVERY h in D simultaneously; finite-step group privacy follows. The representative is everywhere finite and everywhere positive for any probability law: positivity at one point propagates by finitely many D steps. This avoids choosing separate exceptional sets for uncountably many shifts.

**Fixed-b tightness/attainment.** An actual square-core full-D shell and Q have positive densities on a common positive-area set, so T_*(b)<1. Let mu_n be any minimizing sequence. A vague subsequence converges to a finite subprobability nu of mass t in [0,1]. Passing each fixed-h privacy inequality through nonnegative compactly supported continuous tests shows nu satisfies the SAME full-D measure inequalities. If t>0, nu/t is an admissible probability and nu has an everywhere-positive all-point density. Radon regularity and the TV variational definition give

    liminf_n TV(mu_n,Q) >= (Q-nu)_+(R^2).                                (7)

If t=0, the right side is 1, contradicting T_*<1. If 0<t<1, since Q and nu have positive densities and `(Q-nu)(R^2)=1-t>0`, the set where `q>f_nu>0` has positive measure. Normalizing nu strictly decreases its positive deficit there:

    TV(nu/t,Q)=integral(q-f_nu/t)_+ < integral(q-f_nu)_+
                 =(Q-nu)_+(R^2),

contradicting (7) and minimality. Hence every vague cluster point has mass 1. A nontight subsequence would have a vague cluster point of mass <1, so every minimizing sequence is tight. Prokhorov yields a weakly convergent subsequence; full-D privacy is weakly closed by the same test-function argument, and TV is weakly lower semicontinuous as a supremum of bounded continuous tests. Its limit attains T_*(b). This fixed-b argument is not used to interchange b and limits.

## 4. Lower bound: essinf/Fubini and the core height

Let mu be ANY admissible law, T=TV(mu,Q), `S=[-1/2,1/2]^2`, and `e=(q0-f)_+` on S. By (3),

    0<=e<=q0,     integral_S e<=T.                                       (8)

For each corner sigma and 0<d<1 let C_sigma(d) be the INWARD open right triangle `{u,v>0:u+v<d}` in corner coordinates, and

    h_sigma(d)=essinf_(C_sigma(d)) e.

It is nonincreasing and measurable. The four C_sigma(1/2) are pairwise disjoint up to boundaries. Crucially,

    sum_sigma integral_0^(1/2) d h_sigma(d)dd <=T.                       (9)

**Full a.e. justification:** for each rational q in (0,1/2), e>=h_sigma(q) a.e. on C_sigma(q). Remove the countable union of these null sets. For any remaining point with u+v=r<1/2, take rationals q down to r; e is at least `h_sigma(r+)`. A monotone function differs from its right limit only at countably many r, whose line segments have 2D measure zero. Thus e(u,v)>=h_sigma(u+v) a.e. The coarea/Fubini identity `integral_{u+v<1/2} h(u+v)dudv=integral_0^(1/2) d h(d)dd`, applied on the four disjoint triangles, proves (9). This is not an interchange of an arbitrary pointwise infimum with an integral.

For the finite lower restrict first to T<=3b. Each C_sigma(1/2) has area 1/8 and l1 diameter 1. Q has density q0 there, so `mu(C)>=q0/8-T`; for EVERY x in the triangle, averaging all-point privacy over y in it yields

    f(x)>=b(q0-8T).                                                       (10)

For b<=10^-4 and T<=3b this is positive. Therefore all h_sigma(d), including d>1/2 by nesting, obey the sharper common bound

    0<=h_sigma(d)<=H(T)=q0(1-b)+8bT.                                     (11)

Here 8T<=q0 and T<=H/8 throughout this finite range.

## 5. Sharp layer cake and both outer privacy layers

Define the total weighted deficit

    F=sum_sigma integral_0^1(1-d)h_sigma(d)dd.

For a nonincreasing h in [0,H], write its superlevel length at each height as r in [0,1]. Its contribution to F and to the constrained integral in (9) is

    J(r)=r-r^2/2,    K(r)=min(r,1/2)^2/2.

If `r0=sqrt[T/(2H)]<=1/4` and `lambda=1/r0-1`, then for every r in [0,1],

    J(r)-lambda K(r)<=r0/2.                                              (12)

For r<=1/2 this is a concave quadratic with maximum at r0; for r>=1/2 its maximum is `1/2-lambda/8`, and `(4r0-1)(r0-1)>=0` is exactly the required comparison. Integrate (12) over heights, sum four corners, use (9), and obtain

    F<=2H r0+lambda T=sqrt(8HT)-T.                                       (13)

When T=0, (9) and monotonicity give F=0 directly.

Outside S use corner coordinates `(sign1(1/2+a),sign2(1/2+c))`, a,c>0. Define disjoint regions:

* K1: a+c<1, one-step core-overlap depth `d=1-a-c`; total area 2, Q density b^2 q0, and each corner's d-cross-section has length 1-d.
* K2: a+c<2 and exactly one of a,c>1, two-step depth `d=2-a-c`; total area 4, Q density b^3 q0, and each corner's d-cross-section has length 2(1-d).

For y in Kj and x in its core-overlap triangle C_sigma(d), `||y-x||_1<=j`; the all-point group inequality gives

    f(y)>=b^j esssup_(C_sigma(d))f >=b^j[q0-h_sigma(d)].                (14)

The second step holds even if esssup f>q0. K1 and K2 are disjoint, so `T>=mu(K1 union K2)-Q(K1 union K2)`. Integrating (14), inserting (13), and using (11) yields the exact finite necessary inequality

    (1-b-2b^2)T+(b+2b^2)sqrt[8T(q0(1-b)+8bT)]
      >=(2b+4b^2)(1-b)q0.                                               (15)

For 0<b<=10^-4 its left side is continuous and strictly increasing for T>=0. Let tau_b be its UNIQUE positive equality root. Also tau_b<3b: at T=3b the linear term alone exceeds the RHS (`1-b-2b^2>0.999`, RHS/b<2.001). Hence laws with T>3b also have T>=tau_b. Therefore **every** admissible law, without a minimizer or limiting assumption, obeys T>=tau_b.

For an explicit radical, put

    a=b+2b^2, c=1-b-2b^2, h0=q0(1-b), d0=(2b+4b^2)(1-b)q0,
    K=c^2-64a^2 b,  B=2c d0+8a^2 h0.

In this range K>0, the discriminant is positive, and the SMALLER quadratic root, which also has `d0-c tau_b>0`, is

    tau_b=2 d0^2/[B+sqrt(B^2-4K d0^2)].                                  (16)

## 6. Upper: exact clipped-shell partition and error bound

Set s=sqrt(b),

    t=s-s^2+s^3-2s^4,    S=[-1/2,1/2]^2,
    K_t=S intersect {||x||_1<=1-t},    A=1-2t^2,
    m=b/(1-b),   Z=A+(6-4t)m+4m^2.                                      (17)

For 0<s<=1/100, 0<t<=s<1/2. Let P_t have density `b^p/Z`, with p=min{k:x in K_t+kD}. It is ACTUALLY admissible: adding any h in D changes p by at most 1, in both directions.

For x in a positive quadrant define `a_i=(x_i-1/2)_+`. The exact l1 distance to K_t is

    dist_D(x,K_t)=max[a_1+a_2, x_1+x_2-1+t].                             (18)

This follows by clipping the square corner: when both coordinates are outside it adds t to a_1+a_2; when one is inside, only the unmet clipping amount is added; inside S it is the amount above `x1+x2=1-t`. Other quadrants follow by signs. Thus p=ceil(dist_D) a.e.

The normalizer in (17) follows WITHOUT importing a mixed-volume theorem. `|S+kD|=1+4k+2k^2`. In each quadrant, `(S+kD)\(K_t+kD)` consists of two end triangles of total area t^2 and, for k>=1, a diagonal strip of area `kt-t^2/2`; its area is `kt+t^2/2`. At k=0 the missing area is t^2/2 per quadrant. Therefore

    |K_t+kD|=1-2t^2+(4-4t)k+2k^2,   k=0,1,...,
    Z=(1-b) sum_(k>=0)b^k |K_t+kD|=A+(6-4t)m+4m^2.                    (19)

The actual Q shell index is n=n1+n2. On its n=0,1,2 regions, (18) gives the following EXACT 4-quadrant areas by P_t index p:

| n | p=0 | p=1 | p=2 | p=3 |
|---|---|---|---|---|
| 0 | 1-2t^2 | 2t^2 | 0 | 0 |
| 1 | 0 | 4-4t^2 | 4t^2 | 0 |
| 2 | 0 | 2(1-t)^2 | 6+4t-8t^2 | 6t^2 |

In the n=2,p=3 cell, four t^2 comes from eight outer strip-end triangles and two t^2 from four diagonal triangles. The exact Fraction polygon controls in §8 checked ALL seven nonzero entries, including two offsets that are exactly the optimized t(s).

Let `Delta=q0-1/Z`, `Delta_b=q0-b/Z`. Direct exact algebra gives

    q0 Z-1 = s^5 P(s)/(1+s^2)^2,
    P(s)=4+4s-8s^2-2s^3-4s^4+6s^5+8s^6-8s^7.                     (20)

For 0<s<=1/100, `0<P(s)<5`, `Z>=1/2`, and `b q0 Z<1`; hence Delta,Delta_b>0, while Q-P_t is NEGATIVE on n=2,p=1. Define the EXACT rational core-plus-omitted-first-strip expression

    M_b=q0-[A+b(1-A)]/Z+4t^2 b Delta_b.                                  (21)

The table and sign inequalities show the EXACT positive-part integral through Q index 2 is

    T_partial=M_b+(4-4t^2)b Delta
                    +(6+4t-8t^2)b^2 Delta+6t^2 b^2 Delta_b.             (22)

The unintegrated Q index>=3 tail is EXACTLY

    R_tail=4b^3(3-2b)/(1+b)^2.                                           (23)

Thus `T_partial<=TV(P_t,Q)<=T_partial+R_tail`. Moreover Delta<=10s^5, t<=s and R_tail<=12s^6, so the extra terms in (22) plus the tail are <19s^6. Consequently

    T_*(b)<=TV(P_t,Q)<=M_b+19s^6,                                       (24)

which supplies the explicit upper in (4). No conclusion about P_t being the exact nearest law is made.

## 7. Exact asymptotic arithmetic and scope

For the lower, put T=s^2 w and divide the equality in (15) by s^2. Its square-root argument has positive constant 16 and its derivative with respect to w at (s,w)=(0,2) is 1, so the analytic implicit-function theorem applies. Exact Fraction recurrence gives

    tau_b=2s^2-4s^3+0s^4+0s^5+8s^6-38s^7+O(s^8).                     (25)

For the explicit rational expression M_b in (21), exact Fraction series division gives

    M_b=2s^2-4s^3+0s^4+4s^5+0s^6-20s^7+O(s^8).                       (26)

Together with (24), these yield (5). These are series of the proven finite bounds, NOT claims that T_* has the coefficients 8 or -38 at s^6,s^7. The b^(5/2) coefficient of T_* may fail to exist.

## 8. Owner-run bounded controls — exact scope and failure disclosure

All controls were run in this owner's persistent Python eval kernel, with `fractions.Fraction` for every asserted inequality. They do NOT independently review or formalize the proof.

1. **Layer-cake controls.** Four equal step functions with height 1 and radius 1/10 gave `T=1/50`, `F=19/50` and exact equality `(F+T)^2=8T`. Four constant tails of height 1/100 gave `(T,F)=(1/200,1/50)` and slack `8T-(F+T)^2=63/1600`. An unequal four-corner step/tail example gave `T=1783/67200`, `F=13957/67200`, slack `1776983/11289600>0`. These are selected algebra controls, not universal verification.
2. **Exact polygon controls.** A Fraction Sutherland–Hodgman half-plane clipping cell independently computed all Q-index/P-index areas in the table using (18), at t=1/5,1/10,494951/50000000, and at the ACTUAL optimized offsets `495049/50000000` (s=1/100) and `499500499/500000000000` (s=1/1000). All seven listed nonzero areas and zero omitted cells agreed exactly. These are finite geometric controls, not proof for every t.
3. **Actual trial sign and finite-tail controls.** At s=1/100 and 1/1000, Fraction checks found `q0 Z>1`, `b q0 Z<1`, and proved by exact squaring that T_partial is above the scalar lower root. With base `2s^2-4s^3+4s^5`, `(T_partial-base)/s^6` was approximately 5.83847 and 5.98398; `R_tail/s^6` approximately 11.99680 and 11.999968. These decimal renderings summarize EXACT rational computations; no full infinite TV integral was run.
4. **Actual clipped-core h-profile.** For the same s values, the trial's h is `q0-b/Z` for d<t and `q0-1/Z` for d>t. Exact Fraction checks confirmed the height bound (11), core budget (9), `(F+T_partial)^2<=8H T_partial`, and the K1+K2 floor lower <=T_partial. These are selected controls of the precise proof interfaces, not exhaustive validation.
5. **Exact series and a failed assumption.** Fraction recurrence produced (25) and (26). An initial owner assertion incorrectly EXPECTED the s^7 coefficient of the lower root to be -36; it failed, and the exact recurrence showed -38. Only that failed assertion was retried with -38 and succeeded. The false guess did not enter any earlier scientific claim. Decimal evaluations of the root were diagnostic only.
6. **End-to-end finite-bracket controls.** At the same two exact s values, Fraction checks also verified `T_partial-M_b+R_tail<19s^6`, that the displayed upper `M_b+19s^6` lies above the lower root by a sign-aware exact squaring, and the small-range guards `q0-8(3b)>0`, `3b<H(3b)/8` and `c(3b)>d0`. These are two selected point checks only, not verification of the uniform ranges or complete infinite TV integral.

For reproducibility of the polygon cell: in the positive-quadrant Q cell `(i,j)` use `[0,1/2]` for index 0 and `[k-1/2,k+1/2]` for index k>=1. To compute area with P index <=n, intersect that rectangle with the halfplanes `a_1+a_2<=n` and `x_1+x_2<=n+1-t`, where `a_i=0` in index 0 and `a_i=x_i-1/2` otherwise; subtract the <=n-1 area and multiply by 4. Sutherland–Hodgman interpolation uses exact fractions, with boundaries assigned either way.

## 9. Review boundary

This is a **single self-contained author packet**, not an accepted theorem or independent review. Priority review should independently reconstruct the all-point/group representative; the rational-radius essinf/Fubini argument; the nested-triangle layer cake and height H(T); the K2 b^3 density and cross section; the root case split and fixed-b tightness proof; the exact distance-to-core formula, polygon table, q0Z polynomial, tail sign and 19s^6 bound. Do not infer that the unrelated f136 review covers these later claims. No external model, publication, novelty claim or parent adoption occurred.
