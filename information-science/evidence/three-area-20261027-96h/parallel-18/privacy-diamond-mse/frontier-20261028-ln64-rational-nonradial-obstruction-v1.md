# A rational full-D law beats EVERY diamond staircase at epsilon=ln 64

**AUTHOR CANDIDATE — WRITTEN plus exact Fraction arithmetic; NOT independently reviewed or parent-adopted.** Native pre-write observation: `Wed Oct 28 21:01:31 PDT 2026`.

## 1. Original all-law claim and exact source boundary

Take epsilon=ln 64, so b=1/64 and m=b/(1-b)=1/63. The ORIGINAL class is ALL Borel additive-noise laws satisfying epsilon privacy for EVERY Borel event and EVERY shift in the FULL CLOSED unit l1 diamond D. The registered cost is `J=E|X|_2^2`.

Define rational values

    a=3761763123/10^10,     z=3761763124/10^10,    eta=1/100,
    S=aD intersect {||x||_infinity<=a-eta}.                              (1)

Let P_S be the geometric shell law with density proportional to `b^(min{k:x in S+kD})`. It is an ACTUAL full-event/full-D private Borel law. The source-independent written/checked claim is

    J(P_S)+1/1000000 < J(P_gamma)   for EVERY gamma in [0,1],            (2)

where P_gamma is the actual centered l1-diamond staircase with core gamma D. Thus NO law in that entire one-parameter staircase family can be an original all-law J optimizer at this epsilon. The construction is a concrete counterexample, not a claim that P_S is itself optimal.

**Separately conditional all-radial strengthening:** the named same-harness parent MDA alternative `institute/runs/three-area-2026-10-23-96h/privacy-MDA26-entire-norm-cost-and-weighted-decay-parent-v1.md`, SHA-256 `75614a6fc5cb66d9b26f13e64e58935fe6ea52121948e7a56592b91611576ac3`, states that for the SAME full-D class the minimum of `W=E||X||_1^2` is attained by a centered diamond staircase. Every l1-radial density satisfies `J=(2/3)W`; hence, IF that parent input is valid, (2) proves P_S beats EVERY l1-radial full-D-private law by >1/1000000, and no radial law can be all-law J-optimal. This conditional application does NOT follow from a mean-only source theorem, and the parent alternative does not by itself identify the original nonradial optimizer.

No LAW642, v241, v253, earlier unreviewed author theorem or review result is needed for the unconditional counterexample (2). This is an explicit finite-epsilon obstruction, not an exact original optimum, printed-source-proof verdict, claim of non-equivalence in all models, novelty or priority assertion.

## 2. Feasibility and exact clipped-shell geometry

For ANY h in D, inclusion `(S+kD)+h subset S+(k+1)D` and its reverse give `|n_S(x+h)-n_S(x)|<=1`; therefore P_S satisfies (all events, all closed-D shifts) exactly. The clipped core is not radial: at the same r in (a-eta,a), points near an axis have a larger shell index than points near the diagonal.

For every integer k>=0, put R=a+k. Since eta<a/2,

    S+kD = R D intersect {||x||_infinity<=R-eta}.                        (3)

Proof: the forward inclusion follows from the triangle inequalities. Conversely take x,y>=0 satisfying the right side; reduce each coordinate to at most a-eta. If both need reduction the total is <=k-a+2eta<k by x+y<=a+k; if only one does, its outer cap bounds that reduction by k. If the remaining sum exceeds a, lower further until the sum is a; the TOTAL reduction is then x+y-a<=k. The resulting point is in S and the removed displacement lies in kD. Signs and coordinate permutations cover all points.

For one axis cap of height eta, at radius R use `x1=R-u`, `-u<=x2<=u`, `0<=u<=eta`. Its area and squared-Euclidean moment are

    eta^2,      R^2 eta^2-(4/3)R eta^3+(2/3)eta^4.                     (4)

The four caps are disjoint. If N is geometric with `P(N=k)=(1-b)b^k`, and `M_j(g)=E(g+N)^j`, the exact layer-sum formula yields

    Z_S=2M2(a)-4eta^2,
    N_S=(2/3)M4(a)-4M2(a)eta^2+(16/3)M1(a)eta^3-(8/3)eta^4,
    J(P_S)=N_S/Z_S.                                                       (5)

Every term includes ALL geometric layers; there is no finite truncation or linearized approximation.

## 3. Exact scalar staircase minimum and rational enclosure

For any gamma, the true full-D staircase P_gamma has

    J(P_gamma)=M4(gamma)/[3M2(gamma)],
    M2=g^2+2mg+m+2m^2,
    M4=g^4+4mg^3+6(m+2m^2)g^2
       +4(m+6m^2+6m^3)g+m+14m^2+36m^3+24m^4.                          (6)

Its derivative has the sign of

    P_m(g)=g^5+5mg^4+(2m+12m^2)g^3+(12m^3-2m)g^2
              -m(1+2m)(1+6m)g+m^2(1+2m).                                (7)

For m=1/63 the exact comparisons `P_m(0)>0`, `P_m(a)<0<P_m(z)`, `P_m(1)>0` and Descartes' two-sign-change bound imply exactly two positive roots, both simple; the larger root g_* lies in (a,z). P_0=P_1 as normalized laws, so g_* is the global minimum over the ENTIRE interval [0,1]. No other all-law or radial optimality is inferred here.

M2 and M4 have positive coefficients and are increasing for g>=0. Thus

    min_[0,1] J(P_gamma)=M4(g_*)/[3M2(g_*)]
       >= M4(a)/[3M2(z)].                                                (8)

## 4. Exact rational cost and >10^-6 separation

Substituting the rationals in (1),(5) gives the ACTUAL law's exact cost

    J(P_S)=4355768046089487574226880288026708390699272667
            /26721376640271909097532496900000000000000000000.             (9)

Exact Fraction arithmetic with (6) verifies

    M4(a)/[3M2(z)]-J(P_S)
      =55892104628095766169604064637687395172793197064705238995982813
       /28589579218686463271455054512504719394059809867200000000000000
      >1/1000000.                                                         (10)

Equations (8)–(10) prove (2) with a FULLY RATIONAL core, not merely a core depending on an unevaluated optimal root. Equation (10) is a certified LOWER bound on the family gap, not the exact value of that gap.

## 5. Actual arithmetic controls and scientific limits

The owner ran bounded Python-kernel `fractions.Fraction` checks of all signs and inequalities in (8)–(10); the exact law cost and difference printed above are their observed results. An initial coarse root bracket `[37617/100000,37618/100000]` produced a NEGATIVE outward gap because the denominator enclosure was too wide. That attempt was not accepted; only the failed enclosure was refined to the 10-decimal rational endpoints in (1), after which (10) was positive and >10^-6. A preceding exploratory check at the unknown root gave only selected diagnostics and is NOT used as proof. Decimal renderings in the kernel were illustrative, not interval certificates.

The named MDA parent theorem in §1 is used ONLY for the explicitly conditional extension from staircase family to ALL radial laws. Its source reconstruction has its own printed-proof/version qualifications; this packet makes no claim to repair them or to establish priority, source equivalence, novelty, or a new mechanism discovery. The unconditional finite-ε full-law competitor and exact comparisons are WRITTEN plus named Fraction arithmetic, not formally checked, independently reviewed, cross-model reviewed or parent-adopted. Priority review should reconstruct (3) for all k, cap moments, derivative sign/root classification, rational enclosure, and the optional radial import.
