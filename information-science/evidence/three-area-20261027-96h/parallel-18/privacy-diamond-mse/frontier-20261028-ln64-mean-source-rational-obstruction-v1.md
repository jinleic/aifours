# A rational original-law J competitor beats the mean-source staircase at ln 64

**AUTHOR CANDIDATE — WRITTEN plus exact Fraction checks; NOT independently reviewed or parent-adopted.** Native pre-write observation: `Wed Oct 28 21:34:15 PDT 2026`.

## 1. Original full-D model and exact obstruction

Let epsilon=ln 64, b=1/64, m=1/63. The original 2D class consists of ALL Borel additive-noise laws private for EVERY event and EVERY shift in the FULL CLOSED unit l1 diamond D. J=E|X|_2^2, L=E||X||_1.

Let P_g be the actual full-D-private centered diamond staircase with offset g. Let g_L be the scalar-family minimizer of L, explicitly identified below, and let

    r=3761763123/10^10.

The source-independent exact-Fraction/written claim is

    J(P_gL) - J(P_r) >7/1000.                                           (1)

Both P_gL and P_r are ACTUAL original-class laws; the rational comparator P_r proves directly that P_gL cannot minimize the original all-law squared-Euclidean objective. No original all-law optimizer theorem is used to establish (1).

**Separately conditional source consequence:** the named same-harness parent MDA26 alternative `privacy-MDA26-entire-norm-cost-and-weighted-decay-parent-v1.md`, SHA-256 `75614a6fc5cb66d9b26f13e64e58935fe6ea52121948e7a56592b91611576ac3`, states that the original full-D matching-first-norm all-law infimum is attained by a centered staircase. IF that parent theorem is valid, P_gL is an actual global L optimizer yet is >7/1000 worse in J than the explicitly specified full-private P_r. This proves that THIS source-side optimizer is not an original J optimizer; it does NOT claim every possible L optimizer has been characterized or that a mean theorem printed a squared-Euclidean theorem.

No LAW642, v241, v253, unreviewed author theorem, held source or review verdict is imported into (1). The named MDA parent is needed ONLY for the optional all-law mean-optimal interpretation. No source proof repair, novelty, priority or publication-wide non-equivalence is claimed.

## 2. Exact family costs and source-side root

Let N be geometric `(1-b)b^k` and M_j(g)=E(g+N)^j. Exact all-layer integration gives

    L(P_g)=2M3(g)/(3M2(g)),       J(P_g)=M4(g)/(3M2(g)),
    M2=g^2+2mg+m+2m^2,
    M3=g^3+3mg^2+3(m+2m^2)g+m+6m^2+6m^3,
    M4=g^4+4mg^3+6(m+2m^2)g^2
        +4(m+6m^2+6m^3)g+m+14m^2+36m^3+24m^4.                          (2)

Every P_g is genuinely full-D private because its l1-shell index changes by at most one under any D shift. The derivative of L has sign

    Q_m(g)=g^4+4mg^3+6m^2g^2-2m(1+3m)g+m^2.                            (3)

For m=1/63 the exact rational signs in §3 show two positive roots; Q_m has at most two by Descartes, and the larger lies in

    a=2975366184837612/10^16 < g_L
       < z=2975366184837613/10^16.                                       (4)

Both roots are simple, P_0=P_1 as normalized laws, so the larger root is the global L minimum in the ENTIRE staircase family. Its matching-norm all-law status is separately conditional as described in §1.

## 3. Complete exact arithmetic control

M2 and M4 have positive coefficients, so `J(P_gL)>=M4(a)/(3M2(z))`. The following standalone Fraction code was run in the Python eval kernel and every assertion succeeded:

```python
from fractions import Fraction as F
m=F(1,63)
def Q(g):
    return g**4+4*m*g**3+6*m*m*g*g-2*m*(1+3*m)*g+m*m
def M2(g): return g*g+2*m*g+m+2*m*m
def M4(g):
    return (g**4+4*m*g**3+6*(m+2*m*m)*g*g
       +4*(m+6*m*m+6*m**3)*g+m+14*m*m+36*m**3+24*m**4)
a=F(2975366184837612,10**16)
z=F(2975366184837613,10**16)
r=F(3761763123,10**10)
assert Q(0)>0 and Q(a)<0<Q(z) and Q(1)>0
assert M4(a)/(3*M2(z))-M4(r)/(3*M2(r))>F(7,1000)
print('PASS')
```

The actual cell's exact Fraction comparison printed the true gap lower as about 0.00744157 only for illustration; the proof is the rational `>7/1000` assertion. The scalar root classification, all-layer formulas and event privacy are WRITTEN, not machine-verified by the arithmetic cell.

## 4. Limits

The optional mean-optimal interpretation depends on the parent MDA alternative and its stated source/version/printed-proof qualifications. This packet does not need the original squared-Euclidean optimizer, any unreviewed result, or the frozen f145 Eq. (10) numerator/denominator. No source proof repair, global priority, novelty, formal/human/cross-model independent review or parent adoption is claimed. Review should check the all-event shell construction, scalar derivative/root identification, exact rational ratio enclosure and scope of the optional matching-norm import.
