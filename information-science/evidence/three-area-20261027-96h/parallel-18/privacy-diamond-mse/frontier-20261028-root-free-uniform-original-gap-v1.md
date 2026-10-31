# A root-free quantitative original-J obstruction for every sufficiently large epsilon

**AUTHOR CANDIDATE — WRITTEN plus exact Fraction polynomial checks; NOT independently reviewed or parent-adopted.** Native pre-write observation: `Wed Oct 28 21:20:03 PDT 2026`.

## 1. Exact original model and claim

For every finite `epsilon>=ln(1000000000001)`, put `b=e^(-epsilon)`, `m=b/(1-b)`, `s=m^(1/4)`, so `0<s<=1/1000`. The original class is ALL Borel additive-noise laws satisfying epsilon privacy for EVERY Borel event and EVERY shift in the FULL CLOSED unit l1 diamond D. Set J=E|X|_2^2.

Define the EXPLICIT core with NO optimization or unevaluated root

    S=sD intersect {||x||_infinity<=4s/5},

and let P_S be its actual geometric shell law. Let P_gamma denote the actual uncut centered diamond staircase at any gamma in [0,1]. The source-independent written result is

    J(P_S)+s^2/200 <= min_(0<=gamma<=1)J(P_gamma).                       (1)

Thus every such finite epsilon has an explicit original-class mechanism that beats EVERY centered diamond staircase by at least `sqrt[b/(1-b)]/200`. This gap is much larger than the earlier conservative constructive bound but is not asserted to be optimal. P_S is not claimed to be the global all-law optimum.

The separately named same-harness parent MDA26 matching-norm alternative `privacy-MDA26-entire-norm-cost-and-weighted-decay-parent-v1.md`, SHA `75614a6fc5cb66d9b26f13e64e58935fe6ea52121948e7a56592b91611576ac3`, gives an OPTIONAL stronger interpretation: since `J=(2/3)E||X||_1^2` for l1-radial densities and the same-class W optimum is a centered staircase, (1) also beats EVERY l1-radial private law if that parent theorem holds. This bridge is explicitly conditional; the exact full-law competitor and family comparison are not.

## 2. Root-free lower bound for the whole staircase family

For any gamma in [0,1], write N geometric with law `(1-b)b^k`, and let `M_j=E(gamma+N)^j`. Its actual shell cost is `J(P_gamma)=M4/(3M2)`. Since all terms are nonnegative,

    M4>=gamma^4+m,      M2<=gamma^2+4m                                 (m<=1/2).

With x=gamma^2, elementary minimization over x>=0 gives

    J(P_gamma) >= (x^2+m)/[3(x+4m)]
       >=(2/3)[sqrt(m+16m^2)-4m]
       >=(2/3)s^2-(8/3)s^4.                                              (2)

The middle minimum is at `x=sqrt(m+16m^2)-4m`. No staircase root, selected example, or original-law radiality assumption is used.

## 3. Exact actual-shell upper

Here `eta=s/5`, so eta<s/2. The clipped core's exact dilation is

    S+kD=(s+k)D intersect {||x||_infinity<=s+k-eta},   k>=0.

It follows by coordinate clipping and the l1 triangle inequality. Its density `b^(min{k:x in S+kD})/Z` is an ACTUAL full-event/full-closed-D private law. With `M_j=E(s+N)^j`, exact integration of all four removed caps and ALL geometric layers gives

    Z=2M2-4eta^2 >=(46/25)s^2,
    Num=(2/3)M4-4M2 eta^2+(16/3)M1 eta^3-(8/3)eta^4,
    J(P_S)=Num/Z.                                                        (3)

Expanding Num exactly at m=s^4, eta=s/5,

    Num=(2272/1875)s^4 +(8/3)s^5 +(96/25)s^6 +(896/375)s^7
         +(28/3)s^8+16s^9+(192/25)s^10+24s^12+16s^13+16s^16.            (4)

All coefficients after s^4 are nonnegative, and their exact sum after bounding `s<=1/12` is `<4` times s^5. Thus for our smaller range,

    J(P_S) <=s^2[1136/1725+(50/23)s].                                    (5)

Subtract (5) from (2):

    min J(P_gamma)-J(P_S)
      >=s^2[14/1725-(50/23)s-(8/3)s^2]
      >=s^2/200,                                                         (6)

where the endpoint s=1/1000 already gives the exact rational bracket `51227/8625000>1/200`, and the bracket decreases as s increases. This proves (1) for EVERY epsilon in the stated interval with a genuine feasible law.

## 4. Actual checks, dependencies and limitations

The owner used Python-kernel `fractions.Fraction` polynomial arithmetic to expand (4) coefficient-by-coefficient, bound its positive tail at s=1/12, and check the exact endpoint comparison in (6). These are all-variable polynomial and rational arithmetic checks, NOT a machine proof of privacy, layer geometry, the root-free variational bound or the original all-law optimum.

No parent or previous unreviewed theorem is imported into (1)–(6). Only the OPTIONAL all-radial bridge names parent MDA26; its source/version qualifications remain, and no printed-source repair is claimed. This written mechanism/gap is not automatically adopted, formally or independently reviewed, novel by assertion, or a global optimizer. Priority review should reconstruct (2), all-k clipped dilation, all coefficients of (4), and the denominator/inequality directions.
