# ε=ln 64: a 33-decimal two-sided bracket for V_J and 29-decimal optimizer boxes

**AUTHOR CANDIDATE - WRITTEN, plus an owner-run exact certificate in `fractions.Fraction` and exact Q(sqrt D) arithmetic. NOT independently reviewed or parent-adopted.** Native clock observed immediately before writing: `Thu Oct 29 08:31:35 PDT 2026`.

This is an ADDITIVE tightening of the unreviewed bridge packet `frontier-20261029-independent-bridge-matching-optima-v1.md` (SHA-256 `58600f53f9e4c554566527d0800870485e4f9f97c262b5a08c9b6cd86d56dddc`): its §6 upper certificate (Proposition 5) and its outline step (R6). That packet's bytes are not edited. Nothing here is a new optimality theorem, and no further variant claims are made. The extra digits matter for one reason only: an explicit, LAW642-free feasible law is shown to agree with the LAW642 R-system value to 33 decimals.

## 1. Statement

The model and notation are those of the bridge packet §1: the FULL closed l1 diamond D, every Borel event, every shift h∈D, all Borel probability laws, and J=E|X|_2^2. Fix ε=ln 64, so b=1/64 and m=b/(1-b)=1/63. Put

    λ_lo = 163006627735070347894185905345794/10^33,   λ_hi = λ_lo + 10^-33.

**(A) LAW642-free upper bound.** Let P_K40 be the shell law of the bridge §6.1 core, with the rational parameters

    t40 = 1882704899884405717532381874371113060926/10^40,
    c40 = 92748081344953973231659959220098184342/10^40.

Then P_K40 is feasible, and λ_lo < J(P_K40) < λ_hi. Hence V_J < λ_hi.

**(B) Lower bound, conditional on LAW642 §8.** V_J > λ_lo. Together with (A), λ_lo < V_J < λ_hi, so

    V_J = 0.163006627735070347894185905345794...   (33 certified decimals).

The explicit law P_K40 is within 10^-33 of optimal, conditional on LAW642 only through this lower half.

**(C) Optimizer boxes, conditional on LAW642 §8.** In LAW642's rounded regime, let c_* be the junction and d_*=t_*-c_* the terminal facet width of the unique optimal core. Then c_* lies in (ca,cb), with ca=9274808134495397323165995922/10^30 and cb=ca+10^-30. Also

    d_* ∈ (0.17899568185394517443007219151, 0.17899568185394517443007219152),
    t_* ∈ (0.18827048998844057175323818743, 0.18827048998844057175323818744).

These boxes lie inside the earlier unreviewed 17-decimal brackets of `frontier-20261028-ln64-rounded-original-optimum-certificate-v1.md` (SHA-256 `013eca40176065a5a759a032f54510cd5af55c98662a971475c582b9a64621fd`). That file was left unchanged. The bridge §6 bound J<1630066277350704/10^16 is tightened by 17 orders of magnitude.

## 2. Logic of each assertion

### (I) Upper bound

Feasibility, the l1 distance formula and the moment formula (ZN) for the core with profile `F=sqrt(A-y^2)-m` on [0,c] and `F=2t-y` on [c,t] are exactly as in bridge §6.1-6.3. Here Y=2t-c+m and A=Y^2+c^2, so F(c)=2t-c. The density `b^ceil(d_1(x,K))/Z` is private because d_1(.,K) is 1-Lipschitz for the l1 norm.

The code asserts 0<c<t and z=c/Y∈(0,1). N and Z are affine in θ=arctan z, and θ is enclosed by the 20-term alternating partial sum and that sum plus the next term. J=N/Z is a Möbius function of θ, with Z>0 at both ends and hence on the whole interval, so the true J lies between the two endpoint ratios.

### (II) Lower bound

LAW642 premises used. All are in the parent-adopted written-supported record `privacy-all-law-optimum-self-contained-v1.md`, SHA-256 `957cab2bcf3eff1860ff9f4b5a1e5838708aceaf894a97fdc2c5244c3e7d8e53`.

* The canonical-class reduction, and pointwise clipping: for fixed (t,λ), every canonical core satisfies N-λZ>=H(t,CLIP;λ), with `R_λ(y)=sqrt(max(λ-v-y^2,0))-m` and `CLIP=min(2t-y,max(t,R_λ))` (§8.1, lines 425-438).
* The three successive t-regimes for λ∈(T2,λ_P) (§8.4, lines 505-509). In order they are the full diamond for t<=t_D=(sqrt(λ-v)-m)/2, the rounded arc plus upper facet, and lower clipping for t>=t_U.
* The envelope derivative (HT) (§8.3, lines 481-487) and the lower-regime screen (lines 489-495).
* The rounded-regime formulas H_t/16=C0+tv-P_3(d) with `P_3(d)=(4/3)d^3+2md^2+m^2d`, and (RC) `H_tt=16[v+(2d+m)(2t+m)]>0` (lines 521-534).

The code asserts T2<λ_lo<λ_hi<λ_P=4m^2+4m+1/3.

**(IIa) Diamond regime.** Here CLIP is the full diamond 2tD, so H=2M2(2t)[J(P_2t)-λ], and g=2t<=2t_D<1. For centered diamond staircases, J(P_g)=M4(g)/(3M2(g)) (bridge §1). Its g-derivative has the sign of `2M3M2-M1M4`. Expanding by hand with T2=m+2m^2, T3=m+6m^2+6m^3 and T4=m+14m^2+36m^3+24m^4 gives, in ascending powers of g, the coefficients

    m^2(1+2m), -m(1+2m)(1+6m), 12m^3-2m, 2m+12m^2, 5m, 1.

This is the polynomial P of the bridge packet. The code checks that there are exactly two sign changes, so by Descartes' rule P has 0 or 2 positive roots. Exact signs P(0)>0, P(aJ)<0<P(zJ) and P(1)>0, with aJ=3761763123/10^10 and zJ=aJ+10^-10, leave exactly two: r1<aJ<r2<zJ<1.

So J(P_g) increases on [0,r1], decreases on [r1,r2] and increases on [r2,∞). As laws P_0=P_1, so J(0)=J(1)>J(r2). Hence min over g∈[0,1] of J(P_g) is J(P_r2). Because M4 and M2 increase on g>=0, J(P_r2)>=M4(aJ)/(3M2(zJ)). The code checks that this exceeds λ_hi. Therefore H>0 throughout the diamond regime at every λ<=λ_hi.

**(IIb) Rounded regime.** For fixed λ, parametrize by the junction c: put S=sqrt(λ-v-c^2), t=(S+c-m)/2 and d=(S-c-m)/2. This is LAW642's junction equation `λ=2t^2+2d^2+2m(t+d)+T2`, since t+d=S-m and t-d=c. The rounded regime is exactly c>0, d>0.

At c=ca and at c=cb, H_t/16 is an exact element of Q(sqrt(λ-v-c^2)). Its signs are decided exactly: negative at ca and positive at cb. H itself is α+βθ, with α,β∈Q(sqrt D) and θ=arcsin(c/sqrt(λ-v)). It is enclosed by rational sqrt bounds of width 10^-70 together with the alternating arctan enclosure.

By (RC), H is convex in t on the whole rounded regime. So H'<0 left of t_a, H'>0 right of t_b, and on [t_a,t_b] it stays above its tangent at t_a. Hence

    min over the rounded regime >= H(t_a) - |H_t(t_a)| (t_b - t_a).

The code certifies a rational lower bound for this quantity above 27/10^35.

**(IIc) Lower-clip regime.** (HT) has no upper integral here. Its lower integrand `t^2+2mt+T2+y^2-λ` is positive on {R_λ<t}, and 16tT2+16mt^2>=0. So H_t>=(16/3)T3-8λm, which the code checks is positive at λ_hi. Thus H increases on [t_U,∞) from H(t_U). H(t_U) is positive by continuity with the rounded-regime bound; regime continuity is LAW642 §8.3 line 487.

Hence H(t,CLIP;λ_lo)>0 for every t>0. Every canonical-core law therefore has J>λ_lo, and so does every feasible law by the LAW642 reduction. This gives V_J>λ_lo.

### (III) Optimizer parameters

By (A) and (B), λ_*=V_J∈(λ_lo,λ_hi). By LAW642 the optimal core is CLIP(t_*,λ_*), where H(.;λ_*) attains its zero minimum. By (IIa) and (IIc) at λ_*<λ_hi, that minimum lies in the rounded regime, so H_t(t_*;λ_*)=0.

Two monotonicity facts hold on the box c∈[ca,cb], λ∈[λ_lo,λ_hi]. Write ∂_S for the derivative along increasing S at fixed c; S increases with λ, and both t and d change by dS/2.

* At fixed c, ∂_S(H_t/16)=(v-(2d+m)^2)/2<0, because the code checks (2d_lo+m)^2>v with d_lo the box minimum of d (attained at cb and λ_lo). So H_t decreases in λ.
* At fixed λ, dt/dc=(1-c/S)/2>0, because the code checks c<S on the box. Together with H_tt>0 this makes H_t increase in c.

So H_t(ca;λ_*)<=H_t(ca;λ_lo)<0<H_t(cb;λ_hi)<=H_t(cb;λ_*), and the unique stationary junction satisfies c_*∈(ca,cb).

Since S decreases in c and increases in λ, `S∈[S(λ_lo,cb),S(λ_hi,ca)]` holds with rational outward sqrt bounds. This yields the displayed d and t boxes.

## 3. Diagnostics (NOT certificates)

* A 90-digit Decimal Newton/bisection solve of the rounded R-system gave λ≈0.163006627735070347894185905345794809011654426920133150883557775. Exact enclosure gave J(P_K40)∈[0.163006627735070347894185905345794809011654426920133150883558] (both ends agree to 60 printed decimals). This 57-digit agreement is consistent with t40 and c40 being 40-digit approximations, since the cost error is quadratic in the parameter error. Only 33 decimals are certified.
* Decimal finite differences at t∈{0.186,t_*,0.20,0.24} matched the (HT)/(RC) envelope formulas to 12-13 significant digits. The D/R and R/L formulas agreed at t_D and t_U, and dH/dt was positive at four sampled lower-clip points.

## 4. Certificate (executed verbatim as ONE fresh-kernel cell; printed `PASS I`, `PASS II`, `PASS III`)

```python
from fractions import Fraction as F
from math import isqrt

class QS:
    """Exact a + b*sqrt(D), D>0 rational."""
    __slots__=('a','b','D')
    def __init__(s,a,b,D): s.a=F(a); s.b=F(b); s.D=F(D)
    def _c(s,o): return o if isinstance(o,QS) else QS(o,0,s.D)
    def __add__(s,o): o=s._c(o); return QS(s.a+o.a,s.b+o.b,s.D)
    __radd__=__add__
    def __neg__(s): return QS(-s.a,-s.b,s.D)
    def __sub__(s,o): return s+(-s._c(o))
    def __rsub__(s,o): return s._c(o)-s
    def __mul__(s,o): o=s._c(o); return QS(s.a*o.a+s.b*o.b*s.D,s.a*o.b+s.b*o.a,s.D)
    __rmul__=__mul__
    def __truediv__(s,o): return QS(s.a/F(o),s.b/F(o),s.D)
    def __pow__(s,n):
        r=QS(1,0,s.D)
        for _ in range(n): r=r*s
        return r
    def sign(s):
        a,b,D=s.a,s.b,s.D
        if b==0: return (a>0)-(a<0)
        if a>=0 and b>0: return 1
        if a<=0 and b<0: return -1
        if a>0: return 1 if a*a>b*b*D else (-1 if a*a<b*b*D else 0)
        return 1 if b*b*D>a*a else (-1 if b*b*D<a*a else 0)
    def bounds(s,lo,hi):
        x=s.a+s.b*lo; y=s.a+s.b*hi; return (min(x,y),max(x,y))

def sqrt_bounds(x,scale=10**70):
    q=x*scale*scale; k=isqrt(q.numerator//q.denominator)
    lo,hi=F(k,scale),F(k+1,scale); assert lo*lo<=x<hi*hi; return lo,hi
def atan_bounds(z,terms=20):
    assert 0<z<1
    s=sum((-1)**k*z**(2*k+1)/F(2*k+1) for k in range(terms))
    return s, s+z**(2*terms+1)/F(2*terms+1)

b=F(1,64); m=b/(1-b); v=m*(1+m)
T2=m+2*m*m; T3=m+6*m*m+6*m**3; T4=m+14*m*m+36*m**3+24*m**4
C0=m/F(3)+F(3,2)*m*m+m**3
lamP=4*m*m+4*m+F(1,3)

def moments(t,c,Ycoef,A,mk):
    """(ZN) of the arc/facet core: N,Z as pairs (r0,r1) meaning r0+r1*theta."""
    add=lambda *p:(sum((q[0] for q in p),mk(0)),sum((q[1] for q in p),mk(0)))
    sc=lambda p,s:(p[0]*s,p[1]*s)
    cst=lambda r:(r,mk(0))
    I0=(Ycoef*(c/2),mk(A/2)); I1=(Ycoef*(c*(2*c*c-A)/8),mk(A*A/8))
    intF  = add(I0, cst(-m*c+2*t*(t-c)-(t*t-c*c)/2))
    intF2 = add(cst(mk(A*c-c**3/3)), sc(I0,-2*m), cst(m*m*c+((2*t-c)**3-t**3)/3))
    intF3 = add(sc(I0,A), sc(I1,-1), cst(mk(-3*m*(A*c-c**3/3))), sc(I0,3*m*m),
                cst(-m**3*c+((2*t-c)**4-t**4)/4))
    inty2F= add(I1, cst(-m*c**3/3+2*t*(t**3-c**3)/3-(t**4-c**4)/4))
    Z = add(sc(add(intF,cst(-t*t/2)),8), cst(8*t*m+2*T2))
    N = add(cst(F(2,3)*T4+F(16,3)*t*T3+4*t*t*T2),
            sc(add(sc(intF,T2),sc(intF2,m),cst(m*t**3/3),sc(intF3,F(1,3)),inty2F,cst(-t**4/3)),8))
    return N,Z

lam_low=F(163006627735070347894185905345794,10**33)
lam_high=F(163006627735070347894185905345795,10**33)
assert T2<lam_low<lam_high<lamP

# ---- (I) LAW642-free upper bound: actual shell law P_K with rational t, c ----
def shell_cost(t,c):
    Y=2*t-c+m; A=Y*Y+c*c; z=c/Y; assert 0<c<t and 0<z<1
    N,Z=moments(t,c,Y,A,lambda r:F(r))
    lo,hi=atan_bounds(z); vals=[]
    for th in (lo,hi):
        Zv=Z[0]+Z[1]*th; Nv=N[0]+N[1]*th; assert Zv>0 and Nv>0; vals.append(Nv/Zv)
    return min(vals),max(vals)
t40=F(1882704899884405717532381874371113060926,10**40)
c40=F(92748081344953973231659959220098184342,10**40)
Jlo,Jhi=shell_cost(t40,c40)
assert lam_low<Jlo<=Jhi<lam_high
print('PASS I   V_J <= J(P_K40) < lam_high')

# ---- (II) LAW642-conditional lower bound: H_min(t;lam_low)>0 for every t>0 ----
def canonical_R(c,lam):
    A=lam-v; Dv=A-c*c; assert Dv>0
    S=QS(0,1,Dv); mk=lambda r: QS(r,0,Dv)
    t=(S+(c-m))/2; d=(S-(c+m))/2
    Ht16=C0+t*v-(F(4,3)*d**3+2*m*d*d+m*m*d)
    N,Z=moments(t,c,S,A,mk)
    H=(N[0]-Z[0]*lam, N[1]-Z[1]*lam)
    return dict(t=t,d=d,Ht16=Ht16,H=H,Dv=Dv)
def H_interval(c,lam):
    r=canonical_R(c,lam); slo,shi=sqrt_bounds(r['Dv'])
    thlo,_=atan_bounds(c/shi); _,thhi=atan_bounds(c/slo)
    al=r['H'][0].bounds(slo,shi); be=r['H'][1].bounds(slo,shi)
    pr=[be[0]*thlo,be[0]*thhi,be[1]*thlo,be[1]*thhi]
    return r,(al[0]+min(pr),al[1]+max(pr)),(slo,shi)
# (IIa) diamond regime: J(P_g) >= J(P_gJ) > lam_high for all g in [0,1]
Pc=[m*m*(1+2*m), -m*(1+2*m)*(1+6*m), 12*m**3-2*m, 2*m+12*m*m, 5*m, F(1)]
sg=[x>0 for x in Pc]; assert sum(sg[i]!=sg[i+1] for i in range(5))==2
Pq=lambda x: sum(c_*x**i for i,c_ in enumerate(Pc))
M2q=lambda x: x*x+2*m*x+T2
M4q=lambda x: x**4+4*m*x**3+6*T2*x*x+4*T3*x+T4
aJ=F(3761763123,10**10); zJ=F(3761763124,10**10)
assert Pq(0)>0 and Pq(aJ)<0<Pq(zJ) and Pq(1)>0
assert M4q(aJ)/(3*M2q(zJ))>lam_high
# (IIb) rounded regime: (RC) convexity + tangent bound around the stationary junction
ca=F(9274808134495397323165995922,10**30); cb=F(9274808134495397323165995923,10**30)
ra,(Hal,Hah),(sal,sah)=H_interval(ca,lam_low); rb,(Hbl,Hbh),(sbl,sbh)=H_interval(cb,lam_low)
assert ra['Ht16'].sign()<0<rb['Ht16'].sign()
assert ra['d'].bounds(sal,sah)[0]>0 and rb['d'].bounds(sbl,sbh)[0]>0 and ca>0
ta_lo=ra['t'].bounds(sal,sah)[0]; tb_hi=rb['t'].bounds(sbl,sbh)[1]
ht=ra['Ht16'].bounds(sal,sah); slope=16*max(abs(ht[0]),abs(ht[1]))
assert Hal-slope*(tb_hi-ta_lo)>F(27,10**35)
# (IIc) lower-clip regime: HT base (16/3)T3+16tT2+16mt^2-8 lam m > 0
assert F(16,3)*T3-8*lam_high*m>0
print('PASS II  H_min(.;lam_low)>0 on diamond, rounded and lower-clip regimes')

# ---- (III) box for the optimizer's junction and facet parameters at lambda_* ----
c_hi=cb
assert canonical_R(ca,lam_low)['Ht16'].sign()<0 and canonical_R(c_hi,lam_high)['Ht16'].sign()>0
S_lo=sqrt_bounds(lam_low-v-c_hi*c_hi)[0]; S_hi=sqrt_bounds(lam_high-v-ca*ca)[1]
d_lo=(S_lo-c_hi-m)/2; d_hi=(S_hi-ca-m)/2; t_lo=(S_lo+ca-m)/2; t_hi=(S_hi+c_hi-m)/2
assert d_lo>0 and (2*d_lo+m)**2>v and c_hi<S_lo
assert F(17899568185394517443007219151,10**29)<d_lo<=d_hi<F(17899568185394517443007219152,10**29)
assert F(18827048998844057175323818743,10**29)<t_lo<=t_hi<F(18827048998844057175323818744,10**29)
print('PASS III c_* in (ca,cb); d_* and t_* in 29-digit boxes')
```

The same assertions had first been run in pieces in an earlier kernel. That run lacked the explicit T2/λ_P and Descartes-pattern assertions, which were added before the single verbatim cell above was executed.

## 5. Scope

These are exact finite computations plus written logic. They are not formal, kernel, independent-model, human or parent verification.

* (A) does NOT use LAW642, but it does depend on the unreviewed bridge §6 moment derivation.
* (B) and (C) use exactly the LAW642 §8 premises listed in §2.
* No novelty, priority or source-equivalence claim is made, and no earlier file is modified.

Review, if wanted, should check the (ZN) transcription, the Q(sqrt D) sign routine, the (RC) tangent step, and the monotonicity directions in §2(III).
