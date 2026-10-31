#!/usr/bin/env python3
"""Independent f158 controls, from displayed formulas and direct plane integrals.
No author/reviewer code is imported or executed. Only Python standard library.
The finite controls supplement, and do not replace, the written analytic proof.
"""
from fractions import Fraction as F
from math import isqrt, factorial, comb
from pathlib import Path
import hashlib
import json
import subprocess
import sys

HERE = Path(__file__).resolve().parent
RUN = HERE.parent.parent
CAND = Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/privacy-diamond-mse/frontier-20261028-original-target-consolidated-review-v1.md')
EXPECTED = [
    (HERE/'manifest-v1.json', 'f399dff9e7a72376e64e6fd3f18e0d4bb354471dae5e045256859a6a53cd1a03', 3050, None),
    (RUN/'dispositions/info-1-ln64-nonradial-staircase-gap-parent-v1.md', 'd67b0ac9cbde8c6d1f81f0f407106070ea3cee640984b4d166929b12d6dd6516', 6805, 59),
    (CAND, '37d1a560990b44e23da0a7f3c94399b8d88737b9f8276f9f667aa8a80352fa34', 14512, 186),
]

def clock():
    return subprocess.check_output(['/bin/date', '+%Y-%m-%dT%H:%M:%S%z %Z'], text=True).strip()

def integrity():
    rows = []
    for path, sha, size, lf in EXPECTED:
        data = path.read_bytes()
        row = dict(path=str(path), sha256=hashlib.sha256(data).hexdigest(), bytes=len(data), LF=data.count(b'\n'), trailing_LF=data.endswith(b'\n'))
        assert row['sha256'] == sha and row['bytes'] == size
        assert lf is None or row['LF'] == lf
        assert row['trailing_LF']
        rows.append(row)
    return rows

START = clock()
INPUTS = integrity()
checks = []
witnesses = {}

def check(name, condition):
    checks.append(dict(name=name, passed=bool(condition)))

def outer(q, places=45):
    q = F(q); den = 10**places
    n = q.numerator*den//q.denominator
    return [str(F(n, den)), str(F(n+1, den))]

class Poly:
    """Sparse exact polynomials in (m,g,x,k); local arithmetic only."""
    def __init__(self, value=0):
        if isinstance(value, Poly):
            self.d = dict(value.d)
        elif isinstance(value, dict):
            self.d = {e:F(c) for e,c in value.items() if c}
        else:
            self.d = {(0,0,0,0):F(value)} if value else {}
    def __add__(self, other):
        out = dict(self.d)
        for e,c in Poly(other).d.items(): out[e] = out.get(e,F(0))+c
        return Poly(out)
    __radd__ = __add__
    def __neg__(self): return Poly({e:-c for e,c in self.d.items()})
    def __sub__(self, other): return self+-Poly(other)
    def __rsub__(self, other): return Poly(other)+-self
    def __mul__(self, other):
        out = {}
        for a,c in self.d.items():
            for b,d in Poly(other).d.items():
                e = tuple(i+j for i,j in zip(a,b))
                out[e] = out.get(e,F(0))+c*d
        return Poly(out)
    __rmul__ = __mul__
    def __truediv__(self, other): return self*F(1,F(other))
    def __pow__(self, n):
        assert n >= 0
        out = Poly(1)
        for _ in range(n): out = out*self
        return out
    def __eq__(self, other): return self.d == Poly(other).d
    def subst(self, index, value):
        out = Poly(0)
        for e,c in self.d.items():
            base = list(e); base[index] = 0
            out += Poly({tuple(base):c})*Poly(value)**e[index]
        return out
    def diff(self, index):
        out = {}
        for e,c in self.d.items():
            if e[index]:
                base = list(e); base[index] -= 1
                out[tuple(base)] = c*e[index]
        return Poly(out)
    def value(self, values=(0,0,0,0)):
        return sum((c*prod(F(v)**e for v,e in zip(values,powers)) for powers,c in self.d.items()),F(0))
    def expect_k(self, moments):
        assert all(e[:3] == (0,0,0) for e in self.d)
        return sum((c*moments[e[3]] for e,c in self.d.items()),F(0))

def prod(items):
    out = F(1)
    for x in items: out *= x
    return out

def var(i):
    e = [0]*4; e[i] = 1
    return Poly({tuple(e):1})

# Falling factorial generating function: E(N)_j = j! m^j.
def geom_moments(m, top=4):
    stirling = [[0]*(top+1) for _ in range(top+1)]
    stirling[0][0] = 1
    for n in range(1,top+1):
        for j in range(1,n+1): stirling[n][j] = stirling[n-1][j-1]+j*stirling[n-1][j]
    return [sum((stirling[n][j]*factorial(j)*m**j for j in range(n+1)),m*0) for n in range(top+1)]

def sqrt_bounds(q, digits=60):
    q=F(q); scale=10**digits
    n=isqrt(q.numerator*scale*scale//q.denominator)
    a,b=F(n,scale),F(n+1,scale)
    assert a*a <= q < b*b
    return a,b

def atan_alternating(z, n=12):
    assert 0 < z < 1 and n%2 == 0
    lower=sum((F((-1)**j,2*j+1)*z**(2*j+1) for j in range(n)),F(0))
    return lower,lower+z**(2*n+1)/F(2*n+1)

def atan_euler(z, n=20):
    # atan(z)=z/(1+z^2) sum a_j, a_0=1,
    # a_(j+1)/a_j=((2j+2)/(2j+3))*z^2/(1+z^2).
    # This follows from integrating the geometric expansion after tan substitution.
    u=z*z/(1+z*z); term=F(1); total=F(0)
    for j in range(n):
        total += term
        term *= F(2*j+2,2*j+3)*u
    pref=z/(1+z*z)
    return pref*total,pref*(total+term/(1-u))

m=F(1,63); v=m*(1+m)
mu=geom_moments(m)
T2,T3,T4=mu[2:5]
check('A.geometric_moments', [T2,T3,T4] == [m+2*m*m,m+6*m*m+6*m**3,m+14*m*m+36*m**3+24*m**4])
C0=m/3+F(3,2)*m*m+m**3

def branch(d):
    t=(F(4,3)*d**3+2*m*d*d+m*m*d-C0)/v
    lam=2*t*t+2*d*d+2*m*(t+d)+T2
    c=t-d; A=lam-v; y=t+d+m; w=2*t
    check('A.square_identity.'+str(d), A-c*c == y*y)
    return t,lam,c,A,y,w

def primitive(d):
    t,lam,c,A,y,w=branch(d)
    M2=sum((comb(2,j)*w**(2-j)*mu[j] for j in range(3)),F(0))
    M4=sum((comb(4,j)*w**(4-j)*mu[j] for j in range(5)),F(0))
    # Direct substitution into the printed J3/Rint/Uint, retaining atan coefficient.
    j3rat=c*y*(5*A-2*c*c)/8
    j3theta=3*A*A/8
    rrat=-F(2,3)*j3rat+(m*A-m**3/3)*c-c**4/3+lam*c*c/2
    rtheta=-F(2,3)*j3theta
    uint=(w**3/3+m*w*w+(T2-lam)*w)*c+(-w*w-2*m*w+2*lam-T2)*c*c/2+F(2,3)*(w+m)*c**3-F(2,3)*c**4
    return F(2,3)*M4-2*lam*M2+8*(rrat-uint),8*rtheta

def green_law(d, wrong_arc_center=False):
    t,lam,c,A,y,w=branch(d)
    k=var(3); e=k+(m if wrong_arc_center else -m)
    # Boundary of S+kD in 0<=y<=x: circular arc centered (k-m,0),
    # then edge from (t+d+k,c) to (t+k/2,t+k/2), then diagonal.
    a=t+d+k; s=t+k/2
    cross=(a-c)*s
    Zr=(4*(e*c+cross)).expect_k(mu); Ztheta=4*A
    arc_rat=e*(e*e+3*A)*c+e*e*c*y
    arc_theta=A*(2*e*e+A)
    edge=cross*(a*a+c*c+(a+c)*s+2*s*s)/3
    Nr=(2*(arc_rat+edge)).expect_k(mu)
    Ntheta=(2*arc_theta).expect_k(mu)
    return Zr,Ztheta,Nr-lam*Zr,Ntheta-lam*Ztheta

def enclose_pair(r,a,bounds):
    l,u=bounds
    return (r+a*l,r+a*u) if a>=0 else (r+a*u,r+a*l)

def H(d,n=12):
    t,lam,c,A,y,w=branch(d)
    return enclose_pair(*primitive(d),atan_alternating(c/y,n))

lo=F(17899568185394517,10**17); hi=F(17899568185394518,10**17)
params=[]
for label,d in [('left',lo),('right',hi)]:
    t,lam,c,A,y,w=branch(d); params.append((t,lam,c,A,y,w))
    ar,ac=primitive(d); zr,zc,hr,hc=green_law(d)
    check('A.Green_normalizer.'+label,zr == 8*t*d+4*m*(t+d)+2*T2 and zc == 4*A)
    check('A.Green_moment_minus_lambda_Z.'+label,(ar,ac)==(hr,hc))
    aa=atan_alternating(c/y,12); ae=atan_euler(c/y,20); a16=atan_alternating(c/y,16)
    check('A.atan_Euler_inside_alternating.'+label,aa[0]<ae[0]<ae[1]<aa[1] and a16[0]<ae[0]<ae[1]<a16[1])
    hb=enclose_pair(ar,ac,aa)
    check('A.H_enclosure_width.'+label,hb[1]-hb[0]<F(1,10**35))
    check('A.atan_enclosure_width.'+label,aa[1]-aa[0]<F(1,10**35))
    sq=sqrt_bounds(A)
    check('A.arc_geometry.'+label,0<c<t+d and c<sq[0] and sq[0]>m and y>0 and t>0 and d>0)
    check('A.center_diagonal_inside_circle.'+label,(t+m)**2+t*t<A)
    witnesses['A.'+label]=dict(d=str(d),t=outer(t),lambda_interval=outer(lam),atan=outer(ae[0],65)+outer(ae[1],65),H_lower_outer=outer(hb[0],55),H_upper_outer=outer(hb[1],55),sqrt_A=[str(sq[0]),str(sq[1])])
    wrong=green_law(d,True)
    check('A.negative_wrong_arc_center_detected.'+label,(wrong[0],wrong[2])!=(zr,hr))

tl,Ll,cl0,Al0,yl0,_=params[0]; tu,Lu,cu0,Au0,yu0,_=params[1]
Hl=H(lo); Hu=H(hi)
check('A.root_bracket_signs',Hl[0]>F(1,10**18) and Hu[1]<-F(1,10**18))
check('A.full_interval_screens',0<lo<hi<F(1,2) and tl>hi and 2*tu<1 and T2<Ll<Lu<4*m*m+4*m+F(1,3) and Lu<F(100,441))
check('A.VJ_bracket',F(1630066277350703,10**16)<Ll<Lu<F(1630066277350704,10**16))
check('A.t_bracket',F(1882704899884405,10**16)<tl<tu<F(1882704899884407,10**16))
check('A.c_bracket',F(92748081344953,10**16)<tl-hi<tu-lo<F(92748081344955,10**16))
check('A.exponential_bound_ln2',sum((F(7,10)**j/factorial(j) for j in range(4)),F(0))>2)
cl=tl-hi; cu=tu-lo; yl=tl+lo+m; yu=tu+hi+m
zl=cl/yu; zu=cu/yl
check('A.positive_interval_components',0<zl<zu<1 and 0<Ll-v<Lu-v)
atl=atan_alternating(zl,16)[0]; atu=atan_alternating(zu,16)[1]
Zlo=8*tl*lo+4*m*(tl+lo)+2*T2+4*(Ll-v)*atl
Zhi=8*tu*hi+4*m*(tu+hi)+2*T2+4*(Lu-v)*atu
check('A.normalizer_bracket',F(339888889366,10**12)<Zlo<Zhi<F(339888889367,10**12))
witnesses['A.normalizer']={'lower_outer':outer(Zlo),'upper_outer':outer(Zhi)}
# Ordered interval; only the right endpoint is replaced. It stays left of the
# zero, so the failure is the intended H(right)<0 requirement, not ordering.
mut_hi=lo+F(1,10**30); hm=H(mut_hi)
check('A.negative_mutated_endpoint_detected',lo<mut_hi<hi and hm[0]>0 and not(hm[1]<-F(1,10**18)))
witnesses['A.endpoint_negative']={'left':str(lo),'mutated_right':str(mut_hi),'H_mutated_right_lower_outer':outer(hm[0],55),'reason':'Ordered interval retained, but H(right) is strictly positive; root-sign test rejects.'}

# CLAIM B: complete formal identities, independently constructed from moments.
M,G,X,K=[var(i) for i in range(4)]
V=M*(M+1); Tau=1+2*M; xx=G+M
mus=geom_moments(M)
MM=[sum((comb(j,i)*G**(j-i)*mus[i] for i in range(j+1)),Poly(0)) for j in range(5)]
check('B.centered_M2',MM[2]==xx**2+V)
check('B.centered_M3',MM[3]==xx**3+3*V*xx+V*Tau)
check('B.centered_M4',MM[4]==xx**4+6*V*xx**2+4*V*Tau*xx+V+9*V**2)
Q=X**4-2*V*Tau*X+3*V**2
P=X**5+2*V*X**3-2*V*Tau*X**2-V*(1+3*V)*X+2*V**2*Tau
R=2*X**3-(1+6*V)*X+2*V*Tau
qg=G**4+4*M*G**3+6*M**2*G**2-2*M*(1+3*M)*G+M**2
pg=G**5+5*M*G**4+(2*M+12*M**2)*G**3+(12*M**3-2*M)*G**2-M*(1+2*M)*(1+6*M)*G+M**2*(1+2*M)
check('B.derivative_Q',3*MM[2]**2-2*MM[1]*MM[3]==Q.subst(2,xx)==qg)
check('B.derivative_P',2*MM[2]*MM[3]-MM[1]*MM[4]==P.subst(2,xx)==pg)
check('B.quotient_derivative_L',MM[3].diff(1)*MM[2]-MM[3]*MM[2].diff(1)==qg)
check('B.quotient_derivative_J',MM[4].diff(1)*MM[2]-MM[4]*MM[2].diff(1)==2*pg)
check('B.P_equals_xQ_plus_vR',P==X*Q+V*R)
check('B.R_on_Q_zero',X*R==3*(X**2-V)**2-X**2-Q)
check('B.tau_squared',Tau**2==4*V+1)
check('B.root_square_relation',(X**4+3*V**2)**2-4*V**2*Tau**2*X**2==Q*(X**4+3*V**2+2*V*Tau*X))
Z=K
check('B.z_factorization',(Z**2+3)**2-16*Z-12*(Z-1)**2==(Z-1)**3*(Z+3))
check('B.Q_endpoint_values',qg.subst(1,0)==M**2 and qg.subst(1,1)==(1+M)**2)
check('B.P_endpoint_values',pg.subst(1,0)==M**2*(1+2*M) and pg.subst(1,1)==(1+M)**2*(1+2*M))

def reduce_sqrt(poly):
    out=Poly(0)
    for e,c in poly.d.items():
        base=list(e); base[2]%=2
        out+=Poly({tuple(base):c})*V**(e[2]//2)
    return out
check('B.Q_at_sqrt_v',reduce_sqrt(Q)==4*V**2-2*V*Tau*X)
check('B.P_at_sqrt_v',reduce_sqrt(P)==-V*X)

def sign_changes(coeffs):
    s=[1 if c>0 else -1 for c in coeffs if c]
    return sum(a!=b for a,b in zip(s,s[1:]))

def eval_poly(poly,mm,gg): return poly.value((mm,gg,0,0))

def bisect(poly,mm,a,b,steps=150):
    fa=eval_poly(poly,mm,a); fb=eval_poly(poly,mm,b)
    assert fa*fb<0
    for _ in range(steps):
        c=(a+b)/2; fc=eval_poly(poly,mm,c)
        if fa*fc<0: b=c; fb=fc
        else: a=c; fa=fc
    return a,b

def moments_at(mm,g):
    mus=geom_moments(mm)
    return [sum((comb(j,i)*g**(j-i)*mus[i] for i in range(j+1)),F(0)) for j in range(5)]

def costs(mm,g):
    ms=moments_at(mm,g)
    return F(2,3)*ms[3]/ms[2],ms[4]/(3*ms[2])

for mm in [F(1,1000),F(1,63),F(1,2),F(1),F(3),F(100)]:
    vv=mm*(mm+1); tt=1+2*mm
    qs=[F(1),4*mm,6*mm*mm,-2*mm*(1+3*mm),mm*mm]
    ps=[F(1),5*mm,2*mm+12*mm*mm,12*mm**3-2*mm,-mm*(1+2*mm)*(1+6*mm),mm*mm*(1+2*mm)]
    check('B.Descartes.'+str(mm),sign_changes(qs)==2 and sign_changes(ps)==2)
    sl,su=sqrt_bounds(vv); ga=sl-mm; gb=su-mm
    check('B.g0_in_unit_interval.'+str(mm),0<ga<gb<1 and 4*vv<tt*tt)
    check('B.g0_signs.'+str(mm),all(eval_poly(f,mm,z)<0 for f in [qg,pg] for z in [ga,gb]))
    qsmall=bisect(qg,mm,F(0),ga); qlarge=bisect(qg,mm,gb,F(1))
    psmall=bisect(pg,mm,F(0),ga); plarge=bisect(pg,mm,gb,F(1))
    check('B.root_order.'+str(mm),ga<gb<qlarge[0]<qlarge[1]<plarge[0]<plarge[1]<1)
    check('B.P_negative_at_L_bracket.'+str(mm),eval_poly(pg,mm,qlarge[0])<0 and eval_poly(pg,mm,qlarge[1])<0)
    check('B.strict_L_witness.'+str(mm),costs(mm,qlarge[1])[0]<costs(mm,plarge[0])[0])
    check('B.endpoint_laws_costs.'+str(mm),costs(mm,F(0))==costs(mm,F(1)))
    witnesses['B.roots.'+str(mm)]={'gL_lower_outer':outer(qlarge[0],35),'gL_upper_outer':outer(qlarge[1],35),'gJ_lower_outer':outer(plarge[0],35),'gJ_upper_outer':outer(plarge[1],35)}
    for gg in [F(11,10),F(7,4),F(3)]:
        check('B.g_greater_one_decrease.'+str((mm,gg)),costs(mm,gg-1)[1]<costs(mm,gg)[1])
        ms=moments_at(mm,gg)
        check('B.inner_uniform_moment_smaller.'+str((mm,gg)),(gg-1)**2/2<ms[4]/(2*ms[2]))

# Diamond integral formulas from monomial integration over four triangles.
def triangle_monomial(i,j,r): return F(4*factorial(i)*factorial(j),factorial(i+j+2))*r**(i+j+2)
for r in [F(1,3),F(1),F(7,4),F(10)]:
    check('B.diamond_integrals.'+str(r),triangle_monomial(0,0,r)==2*r*r and triangle_monomial(1,0,r)+triangle_monomial(0,1,r)==F(4,3)*r**3 and triangle_monomial(2,0,r)+triangle_monomial(0,2,r)==F(2,3)*r**4 and triangle_monomial(2,0,r)+2*triangle_monomial(1,1,r)+triangle_monomial(0,2,r)==r**4)

# Independent non-diamond example: square [-a,a]^2 plus kD. Area and first
# l1 integral follow from rectangle + two strips + corner triangle per quadrant.
def square_area(a,k): return 4*a*a+8*a*k+2*k*k

def square_I(a,k): return 4*a**3+12*a*a*k+8*a*k*k+F(4,3)*k**3

def shell_for_squared_radii(point,a):
    r=abs(point[0])+abs(point[1]); k=0
    while r*r>square_area(a,k)/2:
        k+=1
        assert k<200
    return k

privacy_cases=0
for a in [F(1,10),F(1,2),F(1),F(3)]:
    for k in range(21):
        rr=square_area(a,k)/2; rrnext=square_area(a,k+1)/2
        # rrnext >= (sqrt(rr)+1)^2 iff u=(rrnext-rr-1)/2>=sqrt(rr).
        u=(rrnext-rr-1)/2
        check('B.BM_square_radii.'+str((a,k)),u>=0 and u*u>=rr)
        II=square_I(a,k)
        check('B.bathtub_square_strict.'+str((a,k)),(F(3,4)*II)**2>rr**3)
    mus=geom_moments(m)
    zexact=4*a*a+8*a*mus[1]+2*mus[2]
    N=60; b=F(1,64)
    partial=(1-b)*sum((b**k*square_area(a,k) for k in range(N+1)),F(0))
    nextterm=(1-b)*b**(N+1)*square_area(a,N+1)
    # For k>=N+1, (a+k+1)/(a+k)<(k+1)/k and quadratic area ratio<(k+1)^2/k^2.
    ratio=b*F((N+2)**2,(N+1)**2)
    check('B.Abel_square_normalizer_tail.'+str(a),partial<zexact<partial+nextterm/(1-ratio))
    for ix in range(-8,9):
        for iy in range(-4,5):
            p=(F(ix,4),F(iy,4)); base=shell_for_squared_radii(p,a)
            for h in [(F(1),F(0)),(F(0),F(-1)),(F(1,3),F(2,3)),(F(-1,2),F(1,4)),(F(0),F(0))]:
                q=(p[0]+h[0],p[1]+h[1]); privacy_cases+=1
                assert abs(shell_for_squared_radii(q,a)-base)<=1
check('B.full_D_shell_sample',privacy_cases==3060)
# Negative privacy control: equal-radius gap .9 instead of >=1 permits a
# two-level jump under the allowed shift h=(1,0).
def bad_index(r):
    k=0
    while r>F(1,2)+F(9,10)*k: k+=1
    return k
check('B.negative_short_radius_spacing_detected',bad_index(F(49,100))==0 and bad_index(F(149,100))==2)
# Negative strictness control: already-centered diamonds have zero first-level gap.
r=F(7,4)
check('B.negative_bathtub_equality_detected',triangle_monomial(1,0,r)+triangle_monomial(0,1,r)-F(4,3)*r**3==0)
witnesses['B.privacy_cases']=privacy_cases

# Exact shell mixture identity, including radii on both closed boundaries.
def ceil_nonnegative(q):
    q=F(q)
    return max(0,-((-q.numerator)//q.denominator))

def u(g,r): return F(1,64)**ceil_nonnegative(r-g)
for g in [F(11,10),F(7,4),F(3)]:
    for r in sorted({F(0),g-1,g,g+1,g-F(1,100),g+F(1,100),g-1-F(1,100),g-1+F(1,100),F(10)}):
        if r>=0:
            check('B.shell_mixture.'+str((g,r)),u(g-1,r)==F(1,64)*u(g,r)+F(63,64)*int(r<=g-1))

END_INPUTS=integrity()
check('input_integrity_unchanged',INPUTS==END_INPUTS)
failed=[r['name'] for r in checks if not r['passed']]
receipt={
    'kind':'INDEPENDENT_SAME_HARNESS_EXACT_CONTROLS',
    'script':str(Path(__file__).resolve()),
    'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'python':sys.version,
    'observed_native_clock_before_controls':START,
    'inputs':INPUTS,
    'arithmetic':'fractions.Fraction and integer isqrt only; no floating arithmetic',
    'author_code_imported_or_executed':False,
    'checks':checks,
    'check_count':len(checks),
    'failure_count':len(failed),
    'failures':failed,
    'witnesses':witnesses,
    'status':'PASS' if not failed else 'FAIL',
    'observed_native_clock_before_receipt_write':clock(),
}
output=HERE/'reviewer-controls-v1-receipt.json'
with output.open('x') as f: json.dump(receipt,f,indent=2,ensure_ascii=False); f.write('\n')
print(json.dumps({k:receipt[k] for k in ['status','check_count','failure_count','failures','script_sha256','observed_native_clock_before_controls','observed_native_clock_before_receipt_write']},indent=2))
sys.exit(bool(failed))
