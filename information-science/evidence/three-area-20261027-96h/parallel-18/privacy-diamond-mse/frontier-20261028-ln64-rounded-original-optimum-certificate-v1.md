# Rigorous rounded original-optimum enclosure at epsilon=ln 64

**AUTHOR CANDIDATE — WRITTEN plus a bounded exact Fraction/alternating-series certificate; NOT independently reviewed or parent-adopted.** Native pre-write observation: `Wed Oct 28 21:25:15 PDT 2026`.

## 1. Original all-law target, parent premise and exact result

At epsilon=ln 64, b=1/64, the registered problem is the infimum V_J of `J=E|X|_2^2` over ALL Borel additive-noise laws satisfying pure epsilon privacy for EVERY Borel event and EVERY shift in the FULL CLOSED unit l1 diamond D.

The exact global/uniqueness premise is the separately named, parent-WRITTEN_SUPPORTED LAW642 adoption `institute/runs/three-area-2026-10-23-96h/privacy-all-law-self-contained-parent-v1.md`, SHA-256 `c08f6353f121ef9e35da0e9d5e8ec9c87b0da838be0d1adf38b807010a1cd979`, and its actual author source `information-science/evidence/three-area-20261023-96h/parallel-18/privacy-diamond-mse/privacy-all-law-optimum-self-contained-v1.md`, SHA-256 `957cab2bcf3eff1860ff9f4b5a1e5838708aceaf894a97fdc2c5244c3e7d8e53`, especially its globally screened rounded system in §8.5. Their assurance remains same-harness written support at named standard analysis imports, not independent-model, human or formal proof. No earlier unreviewed author candidate is used as a premise.

**Conditional on that named all-law theorem**, the UNIQUE original optimal law is the actual full-D-private shell of the rounded core (9) below, and its cost satisfies the EXACT RATIONAL enclosure

    1630066277350703 / 10^16 < V_J(ln 64)
                              < 1630066277350704 / 10^16.                 (1)

Its exact scalar parameter d satisfies

    17899568185394517 / 10^17 < d_* < 17899568185394518 / 10^17.        (2)

The core parameters also satisfy the exact rational bounds

    1882704899884405/10^16 < t_* < 1882704899884407/10^16,
    92748081344953/10^16 < c_*=t_*-d_* < 92748081344955/10^16.          (3)

These are Fraction/alternating-series certificates, not float-based confidence intervals. They do NOT verify the parent all-law theorem, prove source equivalence or establish novelty.

## 2. Exact scalar system and rational arctangent reduction

Put

    m=1/63, v=m(1+m), T2=m+2m^2,
    T3=m+6m^2+6m^3, T4=m+14m^2+36m^3+24m^4,
    C0=m/3+(3/2)m^2+m^3.

For rational d define

    t=[(4/3)d^3+2md^2+m^2d-C0]/v,
    lambda=2t^2+2d^2+2m(t+d)+T2,
    c=t-d, A=lambda-v, w=2t.                                             (4)

Set `M2=w^2+2mw+T2`, `M4=w^4+4mw^3+6T2w^2+4T3w+T4`, and `H_D=(2/3)M4-2lambda M2`. The parent scalar screen uses `H_R=H_D+8(Rint-Uint)` with

    J3=[c sqrt(A-c^2)(5A-2c^2)+3A^2 asin(c/sqrt A)]/8,
    Rint=-(2/3)J3+(mA-m^3/3)c-c^4/3+lambda c^2/2,
    Uint=[w^3/3+mw^2+(T2-lambda)w]c
       +[-w^2-2mw+2lambda-T2]c^2/2
       +(2/3)(w+m)c^3-(2/3)c^4.                                         (5)

The screen identity is `A-c^2=(t+d+m)^2`; because c,t,d,m>0 on our interval,

    asin(c/sqrt A)=atan[c/(t+d+m)].                                      (6)

Consequently H_R is a rational function of d,m plus `-2A^2 atan(z)`, `z=c/(t+d+m)`, with NO irrational square root in the rational part. For 0<z<1 the alternating Taylor sums

    L_11=sum_(k=0)^11 (-1)^k z^(2k+1)/(2k+1),
    U_12=L_11+z^25/25

satisfy `L_11<=atan(z)<=U_12`. The rigorously enclosed H interval is therefore `[Hrat-2A^2 U_12,Hrat-2A^2 L_11]`, where

    Hrat=H_D-(2/3)c(t+d+m)(5A-2c^2)
       +8[(mA-m^3/3)c-c^4/3+lambda c^2/2-Uint].                        (7)

The exact checks in §5 prove its lower endpoint is >10^-18 at the left d bound and its upper endpoint is <-10^-18 at the right d bound. Thus the signs are nonvacuous, with an arctan interval width <10^-35 at each end.

## 3. All screens, unique-law mapping, and actual feasible mechanism

On the interval (2), `t'(d)=[4d^2+4md+m^2]/v>0`; the certificate checks `t(d_left)>d_right`, hence t>d everywhere. Since `lambda'(d)=(4t+2m)t'(d)+4d+2m>0`, the endpoint checks prove `T2<lambda<lambdaP=4m^2+4m+1/3` throughout. Also `0<d<1/2`, c>0 and `A-c^2>0`. The independent elementary inequality `ln 2<7/10` gives `epsilon=6ln2<21/5`, so `4/epsilon^2>100/441` and the checked upper value in (1) lies below that Laplace screen.

IVT gives a root of H_R inside (2). The NAMED parent LAW642 global screen states that a screened H_R zero is the UNIQUE original all-law optimum, not merely an algebraic stationary point. Thus its lambda is V_J, proving (1). The root and t,c enclosures follow from the exact monotonicities above. The actual optimal law is the normalized geometric shell of

    S_*={x: ||x||_1<=2t_*,
               |x|_2^2+2m||x||_infinity+T2<=lambda_*}.                   (8)

For any h in D its shell index changes by at most one, so it is a genuinely full-event/full-D feasible law. Its claimed global optimality and uniqueness are EXACTLY the named parent premise, not established by the local arithmetic alone.

## 4. Exact best-staircase separation and optional radial interpretation

At m=1/63 the centered diamond-staircase derivative polynomial is

    P(g)=g^5+5mg^4+(2m+12m^2)g^3+(12m^3-2m)g^2
         -m(1+2m)(1+6m)g+m^2(1+2m).

Exact signs at `a=3761763123/10^10`, `z=3761763124/10^10`, plus positive endpoint signs and Descartes' rule, put the UNIQUE scalar minimum root in (a,z). Since M4 and M2 have positive coefficients, its true staircase minimum is at least `M4(a)/(3M2(z))`. The certificate directly checks

    M4(a)/(3M2(z)) - 1630066277350704/10^16 > 11/5000000.              (10)

Thus, conditional on LAW642 ONLY, the original all-law optimum is more than 11/5000000 below EVERY centered diamond staircase at ln 64. This is independent of, and does not read or silently correct, the frozen f145 source Eq. (10).

To identify that scalar minimum with the infimum over ALL l1-radial private laws requires the SEPARATE parent MDA26 matching-norm alternative `privacy-MDA26-entire-norm-cost-and-weighted-decay-parent-v1.md`, SHA `75614a6fc5cb66d9b26f13e64e58935fe6ea52121948e7a56592b91611576ac3`, and the elementary radial identity `J=(2/3)E||X||_1^2`. With that additional input, (10) is a >11/5000000 l1-radial-vs-original all-law infimum gap. This does not assert an identical bound for all other norms or any source equivalence.

## 5. Complete owner-run exact certificate

The following is a standalone reconstruction of the exact `fractions.Fraction` checks run in the Python eval kernel: the main block and the four t,c assertions were executed in separate successful cells, as disclosed below. Every assertion uses exact rational arithmetic; the arctan enclosure is the mathematically alternating bound described in §2. No numerical optimizer, native solver, float or interval-library black box was used for the certificate.

```python
from fractions import Fraction as F
m=F(1,63); v=m*(1+m)
T2=m+2*m*m; T3=m+6*m*m+6*m**3
T4=m+14*m*m+36*m**3+24*m**4
C0=m/F(3)+F(3,2)*m*m+m**3
lambdaP=4*m*m+4*m+F(1,3)

def cert(d):
    t=(F(4,3)*d**3+2*m*d*d+m*m*d-C0)/v
    lam=2*t*t+2*d*d+2*m*(t+d)+T2
    c=t-d; A=lam-v; w=2*t
    M2=w*w+2*m*w+T2
    M4=w**4+4*m*w**3+6*T2*w*w+4*T3*w+T4
    HD=F(2,3)*M4-2*lam*M2
    Ui=(w**3/F(3)+m*w*w+(T2-lam)*w)*c
    Ui+=(-w*w-2*m*w+2*lam-T2)*c*c/2
    Ui+=F(2,3)*(w+m)*c**3-F(2,3)*c**4
    Hr=HD-F(2,3)*c*(t+d+m)*(5*A-2*c*c)
    Hr+=8*((m*A-m**3/3)*c-c**4/3+lam*c*c/2-Ui)
    z=c/(t+d+m)
    al=sum((-1)**k*z**(2*k+1)/F(2*k+1) for k in range(12))
    au=al+z**25/F(25)
    return t,lam,z,Hr-2*A*A*au,Hr-2*A*A*al

lo=F(17899568185394517,10**17)
hi=F(17899568185394518,10**17)
tl,jl,zl,hl,_=cert(lo); tu,ju,zu,_,hu=cert(hi)
assert 0<lo<hi<F(1,2) and tl>hi and 0<zl<1 and 0<zu<1
assert T2<jl<ju<lambdaP and hl>F(1,10**18) and hu<-F(1,10**18)
jlow=F(1630066277350703,10**16)
jhigh=F(1630066277350704,10**16)
assert jlow<jl<ju<jhigh and jhigh<F(100,441)
assert tl>F(1882704899884405,10**16)
assert tu<F(1882704899884407,10**16)
assert tl-hi>F(92748081344953,10**16)
assert tu-lo<F(92748081344955,10**16)

def P(g):
    return (g**5+5*m*g**4+(2*m+12*m*m)*g**3
      +(12*m**3-2*m)*g*g-m*(1+2*m)*(1+6*m)*g+m*m*(1+2*m))
def M2(g): return g*g+2*m*g+T2
def M4(g): return g**4+4*m*g**3+6*T2*g*g+4*T3*g+T4

ga=F(3761763123,10**10); gz=F(3761763124,10**10)
assert P(0)>0 and P(ga)<0<P(gz) and P(1)>0
assert M4(ga)/(3*M2(gz))-jhigh>F(11,5000000)
print('PASS')
```

The first run of the same rational certificate used the shorter endpoint bounds (1) and printed the detailed `PASS` result; the four added t,c assertions were separately executed successfully in the same kernel. Earlier exploratory floating scans only located the bracket and are NOT used to establish any displayed bound. This check does not prove LAW642, MDA26, their source ancestry or novelty. It is not Lean/formal/human/cross-model verification or a parent adoption of this new numeric certificate. Priority review should independently reconstruct the H_R algebra, alternating remainder and signs, the entire screened-root mapping, and the distinction between the unconditional staircase gap and conditional all-radial interpretation.
