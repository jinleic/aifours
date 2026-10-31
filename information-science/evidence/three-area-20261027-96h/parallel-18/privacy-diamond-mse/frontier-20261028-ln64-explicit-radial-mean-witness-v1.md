# An explicit full-D radial law improves the true J optimizer's mean at ln 64

**AUTHOR CANDIDATE — WRITTEN plus owner-run exact Fraction/alternating-series/isqrt checks; NOT independently reviewed or parent-adopted.** Native pre-write observation: `Wed Oct 28 21:45:10 PDT 2026`.

## 1. Original model and single named premise

At epsilon=ln 64 let b=1/64. The original class is ALL Borel additive-noise laws satisfying pure epsilon privacy for EVERY Borel event and EVERY shift in the FULL CLOSED unit l1 diamond D. Put `J=E|X|_2^2`, `L=E||X||_1`, `V_L=inf_F L`.

Condition ONLY on the named parent-WRITTEN_SUPPORTED original-J theorem `privacy-all-law-self-contained-parent-v1.md`, SHA `c08f6353f121ef9e35da0e9d5e8ec9c87b0da838be0d1adf38b807010a1cd979`, and its actual 642LF source `privacy-all-law-optimum-self-contained-v1.md`, SHA `957cab2bcf3eff1860ff9f4b5a1e5838708aceaf894a97fdc2c5244c3e7d8e53`, §8.5 rounded screen and parallel-core geometry. Let P_* be its UNIQUE actual original all-law J optimizer.

The present written/Fraction-checked result constructs an EXPLICIT other actual full-D-private radial law P_sharp such that

    L(P_*) >376391002498/10^12,
    L(P_sharp)<376388077343/10^12,
    L(P_*)-V_L >= L(P_*)-L(P_sharp) >29/10000000.                       (1)

The 2.9e-6 margin is rigorous exact rational arithmetic, not a float or an assertion that P_sharp is mean-optimal. Thus the true original J optimizer is NOT first-norm optimal at this finite epsilon, using NO MDA/PMLR or earlier unreviewed author theorem. The only global optimality premise is the named parent LAW642; no source equivalence, novelty, printed-proof repair or parent adoption of this new certificate is claimed.

## 2. Explicit radial law with original full-D privacy

The parent R-screen gives a compact rounded core S_*, parameters d,t,lambda and `c=t-d>0`, and actual shell `p_*=b^n/Z`. Its 4-quadrant source geometry gives, for every integer k>=0,

    |S_*+kD|=|S_*|+8t k+2k^2.                                           (2)

One direct derivation is to integrate the first-octant width F(y)+k-y for 0<=y<=t, then the tail width `2t+k-2y` for t<=y<=t+k/2, and multiply by 8. Define

    R_k=sqrt[|S_*+kD|/2]=sqrt[k^2+4tk+|S_*|/2].                        (3)

The parent core lies in 2tD, so `R_k<=k+2t`. Consequently

    R_(k+1)-R_k=(2(k+2t)+1)/(R_(k+1)+R_k)>=1.                           (4)

Thus `n_sharp(x)=min{k:||x||_1<=R_k}` changes by at most 1 under every closed-D shift. The law `p_sharp=Z^-1 b^n_sharp` is an ACTUAL full-event/full-D-private radial law with exactly the same normalizer Z, because `(1-b)sum b^k |R_kD|=(1-b)sum b^k |S_*+kD|`.

Its first norm is the convergent all-layer sum

    L(P_sharp)=(4/3)(1-b)/Z sum_(k>=0)b^k R_k^3.                         (5)

No theorem about the global first-norm optimum or a source optimizer is required.

## 3. Exact rational screen, moment and tail certificate

The rounded screen uses m=1/63, v=m(m+1), `T2=m+2m^2`, `T3=m+6m^2+6m^3`, and the screened root in

    17899568185394517/10^17 < d <17899568185394518/10^17.              (6)

The independent code below rechecks its exact H_R signs and all D/t/lambda screens using rational alternating arctan bounds, then derives outward Z and core-area bounds. It also directly evaluates an all-layer exact expression for L(P_*) and bounds (5) from above. For the tail after k=11, it uses R_k<=k+1 (because 2t<1) and the exact geometric sums for `(k+1)^3`; no infinite tail is dropped.

All square roots in the rational enclosures are bounded by `math.isqrt` on scaled integers. Every interval product/division has positive sign guards. The exact computation proves (1); Decimal/float is not used in the certificate.

## 4. Complete owner-run arithmetic

The following standalone code was executed as one Python eval-kernel cell and all assertions passed. The arctan series uses the odd lower/even upper alternating remainders for 0<z<1.

```python
from fractions import Fraction as F
from math import isqrt
b=F(1,64); m=F(1,63); v=m*(1+m); T2=m+2*m*m
T3=m+6*m*m+6*m**3; T4=m+14*m*m+36*m**3+24*m**4
C0=m/F(3)+F(3,2)*m*m+m**3

def atanbd(z):
    q=sum((-1)**k*z**(2*k+1)/F(2*k+1) for k in range(12))
    return q,q+z**25/F(25)

def rootcert(d):
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
    al,au=atanbd(c/(t+d+m))
    return t,lam,Hr-2*A*A*au,Hr-2*A*A*al

lo=F(17899568185394517,10**17)
hi=F(17899568185394518,10**17)
tl,Ll,Hll,_=rootcert(lo); tu,Lu,_,Huu=rootcert(hi)
assert Hll>F(1,10**18) and Huu<-F(1,10**18)
assert 0<lo<hi<F(1,2) and tl>hi and 2*tu<1
assert T2<Ll<Lu<4*m*m+4*m+F(1,3) and Lu<F(100,441)
cl=tl-hi;cu=tu-lo;yl=tl+lo+m;yu=tu+hi+m
zl=cl/yu;zu=cu/yl; assert 0<zl<zu<1
Al=Ll-v;Au=Lu-v;atl,_=atanbd(zl);_,atu=atanbd(zu)
Zl=8*tl*lo+4*m*(tl+lo)+2*T2+4*Al*atl
Zu=8*tu*hi+4*m*(tu+hi)+2*T2+4*Au*atu
Sl=Zl-8*m*tu-2*T2; Su=Zu-8*m*tl-2*T2
assert 0<Sl<Su and Zl>0 and Al>m*m
NN=10**25
def sqlo(x):
    x=x*NN*NN; return F(isqrt(x.numerator//x.denominator),NN)
def sqhi(x): return sqlo(x)+F(1,NN)
il=(Al-m*m)*cl/2+(Al*sqlo(Al)-yu**3)/3
il+=(2*tl*tl+2*m*tl)*lo-F(2,3)*tu**3
Nl=8*il+8*tl*T2+F(4,3)*T3; assert Nl>0
LstarLower=Nl/Zu
N=11; sumhi=F(0)
for k in range(N+1):
    x=Su/2+4*tu*k+k*k
    sumhi+=b**k*x*sqhi(x)
n=N+1
S0=1/(1-b); S1=b/(1-b)**2
S2=b*(1+b)/(1-b)**3; S3=b*(1+4*b+b*b)/(1-b)**4
tail=b**n*((n+1)**3*S0+3*(n+1)**2*S1+3*(n+1)*S2+S3)
LsharpUpper=F(4,3)*(1-b)*(sumhi+tail)/Zl
assert LstarLower>F(376391002498,10**12)
assert LsharpUpper<F(376388077343,10**12)
assert LstarLower-LsharpUpper>F(29,10**7)
print('PASS')
```

The actual cell printed `PASS: screened root, actual shell radializer, exact geometric tail and >29/10^7 mean-cost improvement`. The displayed code shortens only the print label. The calculations certify arithmetic, not the parent global theorem.

## 5. Scope and review

This is an explicit original-class law and finite cost inequality conditional on the NAMED original-J parent. It does not assert a globally mean-optimal law, resolve publication/source equivalence, repair a source proof, or establish novelty, formal/human/cross-model review or parent adoption. Suggested review: (2)'s parallel area, radial shell step (4), all-layer L formula, exact positive interval directions, and tail bound.
