# Exact original-J optimizer versus the true first-norm optimum at ln 64

**AUTHOR CANDIDATE — WRITTEN plus owner-run exact Fraction/alternating-series checks; NOT independently reviewed or parent-adopted.** Native pre-write observation: `Wed Oct 28 21:31:36 PDT 2026`.

## 1. Two exact target interfaces, explicitly distinct

At epsilon=ln 64, b=1/64, all laws below are Borel additive-noise laws private for EVERY event and EVERY shift in the FULL CLOSED unit l1 diamond D. Put J=E|X|_2^2 and L=E||X||_1.

* P_J is the UNIQUE actual original all-law J optimizer, conditional on parent LAW642 `privacy-all-law-self-contained-parent-v1.md`, SHA `c08f6353f121ef9e35da0e9d5e8ec9c87b0da838be0d1adf38b807010a1cd979`, and its globally screened rounded source `privacy-all-law-optimum-self-contained-v1.md`, SHA `957cab2bcf3eff1860ff9f4b5a1e5838708aceaf894a97fdc2c5244c3e7d8e53`.
* V_L is the ALL-law first-norm infimum. Its identification with an actual centered diamond staircase is CONDITIONAL on the distinct parent MDA26 matching-norm alternative `privacy-MDA26-entire-norm-cost-and-weighted-decay-parent-v1.md`, SHA `75614a6fc5cb66d9b26f13e64e58935fe6ea52121948e7a56592b91611576ac3`.

Under those named, separately scoped same-harness written premises, exact Fraction certificates give

    37639100249837/10^14 < L(P_J) < 37639100249838/10^14,
    36485977097754/10^14 < V_L    < 36485977097755/10^14,
    L(P_J)-V_L >1153/100000.                                             (1)

Thus the actual original-J optimizer is NOT a first-norm optimizer at this finite epsilon. This is NOT an inference from one cost theorem to another, a proof of the parent theorems, a source-equivalence verdict or a novelty/priority claim. No earlier unreviewed author result is imported as a premise.

## 2. Exact first-norm moment of the rounded J law

Put m=1/63, v=m(m+1), T2=m+2m^2, T3=m+6m^2+6m^3, and let (t,d,lambda) be the named LAW642 rounded parameters. Set c=t-d, A=lambda-v, Y=t+d+m. In the first octant the actual core cap is

    F(y)=sqrt(A-y^2)-m  for 0<=y<=c,
    F(y)=2t-y            for c<=y<=t.

For integer shell k the exact first-octant cap is `F(y)+k` for y<=t and `2t+k-y` for `t<=y<=t+k/2`. Direct integration of `(x+y)` from x=y to that cap and the geometric layer identity give the UNNORMALIZED first-norm numerator

    N_L=8 integral_0^t [F(y)^2/2+yF(y)-3y^2/2+m(F(y)+y)]dy
           +8t T2+(4/3)T3.                                               (2)

On the arc the integrand simplifies to `(A-m^2)/2-2y^2+y sqrt(A-y^2)`; on the facet it is `2t^2-2y^2+2mt`. As `A-c^2=Y^2` and t-c=d, exact integration reduces (2) to

    N_L=8[(A-m^2)c/2+(A^(3/2)-Y^3)/3
            +(2t^2+2mt)d-(2/3)t^3]+8tT2+(4/3)T3.                       (3)

The actual normalizer is `Z=8td+4m(t+d)+2T2+4A atan(c/Y)`, so `L(P_J)=N_L/Z`. Both are all-layer formulas for the actual original J law, not a radial surrogate.

## 3. Independent exact rounded root and source mean root

The code in §4 re-establishes the parent LAW642 R-screen root by exact signs at d in `(17899568185394517,17899568185394518)/10^17`. It uses the same parent formulas, not an unreviewed author certificate. The arctangent has rigorous odd/even alternating rational bounds. The R-branch d,t,lambda screens are checked; also `lambda<100/441<4/(ln 64)^2` because `ln 2<7/10`. The parent supplies the mapping to the global J law.

For the MDA first-norm family at m=1/63, its derivative has the exact sign polynomial

    Q_m(g)=g^4+4mg^3+6m^2g^2-2m(1+3m)g+m^2.                           (4)

It has two sign changes and positive values at 0 and 1. Exact signs at the two rational endpoints in the code isolate its larger root; by Descartes and the equal endpoint staircase law, this is the scalar minimum. The parent MDA theorem, and ONLY that additional premise, identifies the scalar minimum with V_L.

The numerical bounds on (3) use only rational interval arithmetic. For `A^(3/2)`, `math.isqrt` supplies rigorous rational sqrt bounds by squaring; products and all negative terms use outward endpoints. The separately checked sign guards `A_lo>m^2`, `c_lo>0`, `Y_lo>0`, `Z_lo>0` and `N_L_lo>0` justify every multiplication/division direction.

## 4. Complete reproducible arithmetic certificate

The following standalone code's main assertions were run together in one Python eval-kernel cell; the final sign guards were checked in a separate successful Fraction cell. It uses no float, numerical optimizer or interval-library black box.

```python
from fractions import Fraction as F
from math import isqrt
m=F(1,63); v=m*(1+m); T2=m+2*m*m
T3=m+6*m*m+6*m**3; T4=m+14*m*m+36*m**3+24*m**4
C0=m/F(3)+F(3,2)*m*m+m**3

def atan_bd(z):
    a=sum((-1)**k*z**(2*k+1)/F(2*k+1) for k in range(12))
    return a,a+z**25/F(25)

def screen(d):
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
    z=c/(t+d+m); al,au=atan_bd(z)
    return t,lam,Hr-2*A*A*au,Hr-2*A*A*al

lo=F(17899568185394517,10**17)
hi=F(17899568185394518,10**17)
tl,Ll,Hll,_=screen(lo); tu,Lu,_,Huu=screen(hi)
assert Hll>F(1,10**18) and Huu<-F(1,10**18)
assert 0<lo<hi<F(1,2) and tl>hi
assert T2<Ll<Lu<4*m*m+4*m+F(1,3)
assert Lu<F(100,441)
cl=tl-hi; cu=tu-lo; yl=tl+lo+m; yu=tu+hi+m
zl=cl/yu; zu=cu/yl; assert 0<zl<zu<1
Al=Ll-v; Au=Lu-v; atl,_=atan_bd(zl); _,atu=atan_bd(zu)
Zl=8*tl*lo+4*m*(tl+lo)+2*T2+4*Al*atl
Zu=8*tu*hi+4*m*(tu+hi)+2*T2+4*Au*atu
N=10**25

def rootlo(x):
    return F(isqrt((x*N*N).numerator//(x*N*N).denominator),N)
rlo=rootlo(Al); rhi=rootlo(Au)+F(1,N)
assert rlo*rlo<=Al and rhi*rhi>Au
Il=(Al-m*m)*cl/2+(Al*rlo-yu**3)/3
Il+=(2*tl*tl+2*m*tl)*lo-F(2,3)*tu**3
Iu=(Au-m*m)*cu/2+(Au*rhi-yl**3)/3
Iu+=(2*tu*tu+2*m*tu)*hi-F(2,3)*tl**3
Nl=8*Il+8*tl*T2+F(4,3)*T3
Nu=8*Iu+8*tu*T2+F(4,3)*T3
assert Al>m*m and cl>0 and yl>0 and Zl>0 and Nl>0 and Nu>=Nl
jl=Nl/Zu; ju=Nu/Zl
assert F(37639100249837,10**14)<jl<ju<F(37639100249838,10**14)

def Qm(g):
    return g**4+4*m*g**3+6*m*m*g*g-2*m*(1+3*m)*g+m*m
def M2(g): return g*g+2*m*g+m+2*m*m
def M3(g):
    return g**3+3*m*g*g+3*(m+2*m*m)*g+m+6*m*m+6*m**3

a=F(2975366184837612,10**16)
z=F(2975366184837613,10**16)
assert Qm(0)>0 and Qm(a)<0<Qm(z) and Qm(1)>0
ml=2*M3(a)/(3*M2(z)); mu=2*M3(z)/(3*M2(a))
assert F(36485977097754,10**14)<ml<mu<F(36485977097755,10**14)
assert jl-mu>F(1153,100000)
print('PASS')
```

The main executed cell printed `PASS: exact J-opt mean interval, mean-family interval, >1153/100000 tradeoff, all rounded screens`; the separate sign guards and `Lu<100/441` assertion also passed. A separate FLOAT Simpson diagnostic of nine geometric layers gave raw N_L≈0.1279311198065118 versus formula≈0.1279311198065732; this was a finite, non-interval control and is NOT evidence of all-law optimality.

## 5. Verification and source boundaries

The exact checks certify only the displayed finite arithmetic, conditional on the named root/model theorem and radial matching-norm theorem. They do not verify those parent results, the full primary-source proof, an external publisher version, priority or novelty. This is not formal, human, cross-model or independent review, and Main has not adopted the new certificate. Suggested review: the all-layer first-norm integral (2)–(3), screened-root mapping, sqrt interval directions, Q_m scalar root, and the distinction between J-optimal law and separately attained L optimum.
