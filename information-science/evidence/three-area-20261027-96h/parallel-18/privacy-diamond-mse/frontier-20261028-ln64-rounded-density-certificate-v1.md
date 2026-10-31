# Exact original optimizer density, core area and mass at epsilon=ln 64

**AUTHOR CANDIDATE — WRITTEN plus owner-run exact Fraction/alternating-series checks; NOT independently reviewed or parent-adopted.** Native pre-write observation: `Wed Oct 28 21:28:10 PDT 2026`.

## 1. Model, named original-law premise, and certified quantities

At epsilon=ln 64, b=1/64, the original registered target is J=E|X|_2^2 over ALL Borel additive-noise laws satisfying pure epsilon privacy for EVERY Borel event and EVERY shift in the FULL CLOSED unit l1 diamond D.

This certificate is CONDITIONAL on the parent-WRITTEN_SUPPORTED original all-law/uniqueness theorem in `institute/runs/three-area-2026-10-23-96h/privacy-all-law-self-contained-parent-v1.md`, SHA-256 `c08f6353f121ef9e35da0e9d5e8ec9c87b0da838be0d1adf38b807010a1cd979`, and the corresponding source's rounded scalar/normalization formulas in `information-science/evidence/three-area-20261023-96h/parallel-18/privacy-diamond-mse/privacy-all-law-optimum-self-contained-v1.md`, SHA-256 `957cab2bcf3eff1860ff9f4b5a1e5838708aceaf894a97fdc2c5244c3e7d8e53`, §8.5. This parent is same-harness written support at standard named imports, not a formal, human or cross-model proof. No earlier unreviewed author candidate is imported as a premise.

The unique original optimal LAW is the actual full-D geometric shell with core

    S_*={x: ||x||_1<=2t_*,
               |x|_2^2+(2/63)||x||_infinity+65/3969<=lambda_*},
    p_*(x)=64^(-min{k:x in S_*+kD})/Z_*.                                 (1)

Its core has a genuine curved arc and positive facet: the root screen below gives `0<d_*<t_*`, `c_*=t_*-d_*>0`. The following EXACT rational intervals are the new owner-checked numerical claims, conditional on the named all-law source:

    339888889366/10^12 < Z_* < 339888889367/10^12,
    283227683280/10^12 < |S_*| < 283227683281/10^12,
    833294915313/10^12 < P_*(S_*) < 833294915314/10^12,
    2942137949448/10^12 < esssup p_* < 2942137949449/10^12.             (2)

The peak is 1/Z_*; the core probability is |S_*|/Z_* because n=0 on S_* a.e. These are interval certificates from exact rational arithmetic, not floating approximations or an independently checked parent theorem.

## 2. Scalar root re-established without an unreviewed premise

Set

    m=1/63, v=m(m+1), T2=m+2m^2, T3=m+6m^2+6m^3,
    T4=m+14m^2+36m^3+24m^4, C0=m/3+(3/2)m^2+m^3.

For d define

    t(d)=[(4/3)d^3+2md^2+m^2d-C0]/v,
    lambda(d)=2t^2+2d^2+2m(t+d)+T2,
    c=t-d, A=lambda-v, Y=t+d+m, z=c/Y.                                   (3)

The parent screened rounded equation is `H_R(d)=0`. All rational parts of H_R are given directly in the complete code in §5; the only transcendental part is `-2A^2 atan(z)`, using the exact identities `A-c^2=Y^2` and `asin(c/sqrt A)=atan(c/Y)`.

The code proves by exact alternating-series bounds that

    H_R(17899568185394517/10^17)>10^-18,
    H_R(17899568185394518/10^17)<-10^-18,                               (4)

while `0<d<1/2`, `t>d`, `0<z<1`, and `T2<lambda<4m^2+4m+1/3` hold throughout the bracket: t and lambda are increasing and the lower t exceeds the upper d. The parent LAW642 globally screened-root theorem supplies the all-law identification. These checks re-establish the root interval directly; they do not import an earlier unreviewed numerical certificate.

## 3. Exact normalization and core-area identities

The parent source writes `J1=[c sqrt(A-c^2)+A asin(c/sqrt A)]/2` and

    Z=8[t^2-2tc+c^2/2+J1-mc]+8tm+2T2.

Using c=t-d, sqrt(A-c^2)=Y and (3) simplifies this EXACTLY to

    Z=8td+4m(t+d)+2T2+4A atan(z),
    |S_*|=Z-8tm-2T2=8td-4mc+4A atan(z).                                (5)

The area formula is the first octant integral `8 integral_0^t[F(y)-y]dy`, with its rounded arc for y<c and diamond facet for c<y<t. Thus the positive shell-mass contribution `Z-|S_*|=8tm+2T2` is explicit.

The code evaluates t and lambda at the exact d endpoints; bounds c by `[t_lo-d_hi,t_hi-d_lo]`, Y by its positive endpoint bounds and z by `[c_lo/Y_hi,c_hi/Y_lo]`. All factors in the first expression of (5) are nonnegative. Alternating rational arctangent sums therefore give rigorous outward Z bounds. It then bounds core area by `Z_lo-8m t_hi-2T2` and `Z_hi-8m t_lo-2T2`, and obtains the mass and peak intervals by positive ratio/reciprocal monotonicity. No untracked float operation enters (2).

## 4. Reproducible exact owner check

The following complete `fractions.Fraction` code was run as one Python eval-kernel cell and printed `PASS` for all assertions. The only analytic input beyond rational operations is the proven alternating arctan remainder; no interval library, root-finding black box or floating arithmetic is used.

```python
from fractions import Fraction as F
m=F(1,63);v=m*(1+m);T2=m+2*m*m
T3=m+6*m*m+6*m**3;T4=m+14*m*m+36*m**3+24*m**4
C0=m/F(3)+F(3,2)*m*m+m**3

def atan_bounds(z):
    L=sum((-1)**k*z**(2*k+1)/F(2*k+1) for k in range(12))
    return L,L+z**25/F(25)

def cert(d):
    t=(F(4,3)*d**3+2*m*d*d+m*m*d-C0)/v
    lam=2*t*t+2*d*d+2*m*(t+d)+T2
    c=t-d; A=lam-v; w=2*t
    M2=w*w+2*m*w+T2
    M4=w**4+4*m*w**3+6*T2*w*w+4*T3*w+T4
    HD=F(2,3)*M4-2*lam*M2
    U=(w**3/F(3)+m*w*w+(T2-lam)*w)*c
    U+=(-w*w-2*m*w+2*lam-T2)*c*c/2
    U+=F(2,3)*(w+m)*c**3-F(2,3)*c**4
    Hr=HD-F(2,3)*c*(t+d+m)*(5*A-2*c*c)
    Hr+=8*((m*A-m**3/3)*c-c**4/3+lam*c*c/2-U)
    z=c/(t+d+m); al,au=atan_bounds(z)
    return t,lam,Hr-2*A*A*au,Hr-2*A*A*al

lo=F(17899568185394517,10**17)
hi=F(17899568185394518,10**17)
tl,Ll,Hll,_=cert(lo); tu,Lu,_,Huu=cert(hi)
assert Hll>F(1,10**18) and Huu<-F(1,10**18)
assert 0<lo<hi<F(1,2) and tl>hi
assert T2<Ll<Lu<4*m*m+4*m+F(1,3)
cl=tl-hi; cu=tu-lo; yl=tl+lo+m; yu=tu+hi+m
zl=cl/yu; zu=cu/yl; assert 0<zl<zu<1
Al=Ll-v; Au=Lu-v; atl,_=atan_bounds(zl); _,atu=atan_bounds(zu)
Zl=8*tl*lo+4*m*(tl+lo)+2*T2+4*Al*atl
Zu=8*tu*hi+4*m*(tu+hi)+2*T2+4*Au*atu
Sl=Zl-8*tu*m-2*T2; Su=Zu-8*tl*m-2*T2
assert F(339888889366,10**12)<Zl<Zu<F(339888889367,10**12)
assert F(283227683280,10**12)<Sl<Su<F(283227683281,10**12)
assert F(833294915313,10**12)<Sl/Zu<Su/Zl<F(833294915314,10**12)
assert F(2942137949448,10**12)<1/Zu<1/Zl<F(2942137949449,10**12)
print('PASS')
```

The actual cell printed `PASS: independent exact root signs, all screens, Z, core area, core probability, and peak 12-decimal bounds`; the code above shortens only the print text. It does not machine-check the parent theorem, optimality, privacy proof, source identities, or novelty.

## 5. Scope and review

The original cost problem is not replaced by a radial surrogate: the R-branch core in (1) is nonradial and its all-law/uniqueness claim is conditional on the cited parent. No MDA/PMLR theorem, previously unreviewed author result, source-proof repair, global priority, novelty clearance, formal proof, independent review or parent adoption of these new interval computations is asserted. Suggested review: H_R/atan transcription, interval products and directions, octant area subtraction, core mass, and exact named source scope.
