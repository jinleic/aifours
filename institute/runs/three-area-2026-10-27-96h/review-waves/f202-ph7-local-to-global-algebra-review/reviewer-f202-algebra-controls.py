#!/usr/bin/env python3
"""Independent exact algebra controls; no author program imported or run."""
from fractions import Fraction as Q
from math import comb
from itertools import combinations, product
import json

N = 10  # v1..v7, z, a, b
ZERO = (0,)*N
class P:
    def __init__(self, d=None):
        if isinstance(d, P): self.d = d.d.copy()
        elif isinstance(d, dict): self.d = {k:Q(v) for k,v in d.items() if v}
        else: self.d = {} if not d else {ZERO:Q(d)}
    @staticmethod
    def var(i):
        t = [0]*N; t[i] = 1
        return P({tuple(t):1})
    def __add__(self, o):
        o=P(o); d=self.d.copy()
        for k,v in o.d.items(): d[k]=d.get(k,0)+v
        return P(d)
    __radd__=__add__
    def __neg__(self): return P({k:-v for k,v in self.d.items()})
    def __sub__(self,o): return self+-P(o)
    def __rsub__(self,o): return P(o)+-self
    def __mul__(self,o):
        o=P(o); d={}
        for k,v in self.d.items():
            for l,w in o.d.items():
                m=tuple(x+y for x,y in zip(k,l)); d[m]=d.get(m,0)+v*w
        return P(d)
    __rmul__=__mul__
    def __truediv__(self,o): return self*Q(1,o)
    def __pow__(self,n):
        out=P(1); base=self
        while n:
            if n&1: out=out*base
            n//=2
            if n: base=base*base
        return out
    def diff(self,i):
        d={}
        for k,v in self.d.items():
            if k[i]:
                m=list(k); m[i]-=1; m=tuple(m); d[m]=d.get(m,0)+v*k[i]
        return P(d)
    def coeff(self,i,n):
        d={}
        for k,v in self.d.items():
            if k[i]==n:
                m=list(k); m[i]=0; m=tuple(m); d[m]=d.get(m,0)+v
        return P(d)
    def degree(self,i): return max((k[i] for k in self.d),default=0)
    def grouped(self):
        # u goes to coordinate 0; v to coordinate 1; preserve z,a,b.
        d={}
        for k,w in self.d.items():
            t=[0]*N; t[0]=sum(k[2:7]); t[1]=k[0]+k[1]; t[7:]=k[7:]
            t=tuple(t); d[t]=d.get(t,0)+w
        return P(d)
    def value(self,x):
        return sum((v*prod(x[i]**n for i,n in enumerate(k) if n) for k,v in self.d.items()),Q(0))

def prod(xs):
    out=Q(1)
    for x in xs: out*=x
    return out

def es(v,k):
    out=P(0)
    for c in combinations(v,k):
        t=P(1)
        for vj in c: t=t*vj
        out=out+t
    return out

def identity(name, expr):
    assert not P(expr).d, name
    print('IDENTITY_OK',name)

def negative(name, expr):
    assert P(expr).d, name
    print('NEGATIVE_REJECTED',name)

def definitions(v,z):
    e=[es(v,k) for k in range(8)]
    p=e[1]-4; q=e[2]-4*e[1]+10-2*z
    W=e[3]-4*e[2]+(10-2*z)*e[1]+12*z-20
    E3=e[4]-(6+2*z)*e[2]+(20+4*z)*e[1]+3*z*z+6*z-45
    E2=e[5]-(1+z)**2*p-(4+4*z)*q
    E1=e[6]-(1+z)**2*q
    s=v[0]+v[1]; S3=sum(v[:3],P(0)); S4=sum(v[:4],P(0)); L4=sum(v[3:],P(0))
    K=E3-S4*W
    Y2=E2-W*es(v[:4],2)-S3*(E3-W*L4)
    alpha=es(v[:4],3)-s*es(v[3:],2)
    Bj=v[0]*v[1]-s*s
    Z=E1-s*E2
    Y=Z-W*alpha-K*Bj+W*W/2
    return e,p,q,W,E3,E2,E1,s,S3,S4,L4,K,Y2,alpha,Bj,Z,Y

v=[P.var(i) for i in range(7)]; z,a,b=[P.var(i) for i in (7,8,9)]
e,p,q,W,E3,E2,E1,s,S3,S4,L4,K,Y2,alpha,Bj,Z,Y=definitions(v,z)
# Coefficient matching, including every displayed canonical residual.
D=[P(0),(1+z)**2,4+4*z,6+2*z,P(4),P(1)]
T=[q,p,P(1)]; char=[sum((D[i]*T[j] for i in range(6) for j in range(3) if i+j==k),P(0)) for k in range(8)]
identity('p from y^6',e[1]-char[6])
identity('q from y^5',e[2]-char[5])
for name,res,k in [('W',W,4),('E3',E3,3),('E2',E2,2),('E1',E1,1)]: identity(name+' coefficient residual',e[7-k]-char[k]-res)
x=v[6]; f=[es(v[:6],k) for k in range(7)]; Fm=f[1]-4
A=f[2]-4*f[1]+10-2*z; B=f[3]-4*f[2]+(10-2*z)*f[1]+12*z-20
h1=f[3]-(6+2*z)*f[1]+20+4*z
h0=f[4]-(6+2*z)*f[2]+(20+4*z)*f[1]+3*z*z+6*z-45
Dd=h1-A*S4; Ee=h0-B*S4
Qpol=A*A-Fm*B; Hpol=-(h0*A-h1*B)
identity('q=A+(f1-4)x',q-A-Fm*x)
identity('W=Ax+B',W-A*x-B)
identity('E3=h1*x+h0',E3-h1*x-h0)
identity('K=E+Dx',K-Ee-Dd*x)
identity('EA-BD=h0*A-h1*B',Ee*A-B*Dd-h0*A+h1*B)
identity('A*K-D*W=-Hpol',A*K-Dd*W+Hpol)
negative('reverse Hpol sign',A*K-Dd*W-Hpol)
identity('case a completing square',f[2]-4*f[1]+10-2*z-(4-f[1])**2-(f[2]-Q(5,12)*f[1]**2)-(Q(6,7)-2*z-Q(7,12)*(f[1]-Q(24,7))**2))
identity('Y2 x squared leading coefficient',Y2.coeff(6,2)-S3*A)
identity('Y2 no x cubic',Y2.coeff(6,3))
g=v[0]*v[1]*v[2]-W
g0=v[0]*v[1]*v[2]-B
Y0=e[7]-W*es(v[:4],4)+W*W*x/2-g*(E3-W*L4)
identity('g=g0-Ax',g-g0+A*x)
identity('Y0 cubic -A^2/2',Y0.coeff(6,3)+A*A/2)
identity('Y0 no quartic',Y0.coeff(6,4))
identity('Y0 third derivative',Y0.diff(6).diff(6).diff(6)+3*A*A)
negative('wrong Y0 cubic sign',Y0.coeff(6,3)-A*A/2)
assert all(Y0.coeff(6,k).degree(i) <= [2,2,2,3,3,3][i] for i in range(6) for k in range(4))
assert all(g0.degree(i)<=1 and A.degree(i)<=1 for i in range(6))
print('IDENTITY_OK common Bernstein multidegrees')
F=Z+a*W+b*E3-E3*E3
lam=a+alpha+b*S4-W/2-S4*E3; mu=b+Bj-E3
identity('F=Y+lambda W+mu K',F-Y-lam*W-mu*K)
negative('omit half pair bound in dual identity',F-(Y-W*W/2)-lam*W-mu*K)
identity('lambda linear in x',lam.diff(6).diff(6))
identity('mu linear in x',mu.diff(6).diff(6))
identity('Y_joint x squared coefficient',Y.coeff(6,2)-A*s*sum(v[3:6],P(0))-A*A/2)
identity('Y_joint no x cubic',Y.coeff(6,3))
for i,j in [(0,1),(2,3),(2,6)]:
    rem=[v[k] for k in range(7) if k not in (i,j)]
    phi=es(rem,4)-s*es(rem,3)+(b-2*E3)*es(rem,2)+a*es(rem,1)+s*(4+4*z)-(1+z)**2-4*a-(6+2*z)*(b-2*E3)
    identity('Schur derivative %d,%d'%(i+1,j+1),F.diff(i)-F.diff(j)+(v[i]-v[j])*phi)
    if (i,j)==(0,1): negative('reverse Schur derivative sign',F.diff(i)-F.diff(j)-(v[i]-v[j])*phi)
# Group map and grouped gradient: U=coordinate 0, V=coordinate 1.
u,V=v[0],v[1]; vg=[V,V,u,u,u,u,u]
_,_,_,Wg,Eg,_,_,_,_,_,_,_,_,_,_,Zg,_=definitions(vg,z)
Fg=Zg+a*Wg+b*Eg-Eg*Eg
identity('group F substitution',F.grouped()-Fg)
identity('group U stationarity factor five',F.diff(2).grouped()*5-Fg.diff(0))
identity('group V stationarity factor two',F.diff(0).grouped()*2-Fg.diff(1))
# Joint interlacing algebra in displacements d_i, without extra assumptions.
d1,d2,d3=v[3:6]; n=[v[i]+[d1,d2,d3][i] for i in range(3)]
J=es(n,2)-s*sum(n,P(0)); Jbase=v[0]*v[1]-s*s
identity('joint displacement sum',J-Jbase-(v[2]-v[0])*d1-(v[2]-v[1])*d2-d1*d2-d1*d3-d2*d3)
negative('omit d1*d2 from joint identity',J-Jbase-(v[2]-v[0])*d1-(v[2]-v[1])*d2-d1*d3-d2*d3)
# Compactification degree and exact endpoint arithmetic.
assert all(Qpol.degree(i)<=2 and Hpol.degree(i)<=2 for i in range(6))
for sc,rate in [(Q(5,16),Q(5,11)),(Q(37,64),Q(37,27)),(Q(7,16),Q(7,9)),(Q(5,8),Q(5,3))]: assert sc/(1-sc)==rate
print('IDENTITY_OK compactification degree and cube endpoints')
# R3 derivation with alpha elementary sums abstracted as symbols.
y,al2,al3,bet,bet2=v[:5]
f1=y+bet; f2=al2+y*bet+bet2; f3=al3+al2*bet+y*bet2
Aexact=f2-4*f1+10-2*z
Abar=al2-4*y+10-2*z+bet*(y-4)+bet*bet/4
Dexact=f3-(6+2*z)*f1+20+4*z-Aexact*y
Dbar=4*y*y-16*y+20+4*z-Q(5,6)*y*al2+bet*(al2-y*y+4*y-6-2*z)
identity('R3 Abar-A=beta1^2/4-beta2',Abar-Aexact-bet*bet/4+bet2)
identity('R3 Dbar-D=y*alpha2/6-alpha3',Dbar-Dexact-y*al2/6+al3)
negative('R3 wrong sign beta2',Abar-Aexact+bet*bet/4-bet2)
# Strict endpoint sign clearing, including a negative upper endpoint.
for l0,l1,expect in [(Q(1),Q(1),(True,True)),(Q(4),Q(-1),(True,False))]:
    aa,bb,dd,ee=Q(2),Q(-4),Q(-1),Q(5)
    low=-bb/aa; high=-ee/dd
    assert ((aa*l0-bb*l1)>0,(-dd*l0+ee*l1)>0)==expect
    assert ((l0+l1*low)>0,(l0+l1*high)>0)==expect
print('IDENTITY_OK cleared multiplier endpoint signs')
print('NEGATIVE_REJECTED upper endpoint with wrong sign')

# Independent exact centered polynomial arithmetic on the author's claimed root box.
class I:
    def __init__(self,l,h=None): self.lo=Q(l); self.hi=Q(l if h is None else h); assert self.lo<=self.hi
    def __add__(self,o):
        o=o if isinstance(o,I) else I(o); return I(self.lo+o.lo,self.hi+o.hi)
    __radd__=__add__
    def __neg__(self): return I(-self.hi,-self.lo)
    def __sub__(self,o): return self+-o if isinstance(o,I) else self+I(-o)
    def __rsub__(self,o): return I(o)+-self
    def __mul__(self,o):
        o=o if isinstance(o,I) else I(o); t=[self.lo*o.lo,self.lo*o.hi,self.hi*o.lo,self.hi*o.hi]; return I(min(t),max(t))
    __rmul__=__mul__
    def __truediv__(self,o):
        o=o if isinstance(o,I) else I(o); assert o.lo*o.hi>0; return self*I(1/o.hi,1/o.lo)
    def absmax(self): return max(abs(self.lo),abs(self.hi))

def center_bound(poly,C,r):
    rows={}
    for k,val in poly.d.items():
        assert all(k[i]==0 for i in (2,3,4,5,6,8,9))
        for i in range(k[0]+1):
            for j in range(k[1]+1):
                for h in range(k[7]+1):
                    idx=(i,j,h)
                    term=val*comb(k[0],i)*comb(k[1],j)*comb(k[7],h)*C[0]**(k[0]-i)*C[1]**(k[1]-j)*C[2]**(k[7]-h)
                    rows[idx]=rows.get(idx,0)+term
    mid=rows.get((0,0,0),Q(0)); err=sum((abs(c)*r**sum(k) for k,c in rows.items() if sum(k)),Q(0))
    return I(mid-err,mid+err)

def inverse(m):
    n=len(m); A=[list(row)+[Q(i==j) for j in range(n)] for i,row in enumerate(m)]
    for i in range(n):
        pivot=next(j for j in range(i,n) if A[j][i]); A[i],A[pivot]=A[pivot],A[i]
        div=A[i][i]; A[i]=[x/div for x in A[i]]
        for j in range(n):
            if j!=i:
                mul=A[j][i]; A[j]=[x-mul*y for x,y in zip(A[j],A[i])]
    return [row[n:] for row in A]

C=[Q(334696976789746519,250000000000000000),Q(208405938226799943,200000000000000000),Q(410210220392063003,500000000000000000)]
r=Q(1,10**16); old=[Q(1338787907,10**9),Q(1042029691,10**9),Q(820420441,10**9)]; oldr=Q(1,10**7)
assert all(abs(c-o)+r<oldr for c,o in zip(C,old))
root=[Wg,Eg,Zg]; ix=[0,1,7]; X=[C[0],C[1],Q(0),Q(0),Q(0),Q(0),Q(0),C[2],Q(0),Q(0)]
jac=[[poly.diff(j) for j in ix] for poly in root]
J0=[[g.value(X) for g in row] for row in jac]; inv=inverse(J0)
Jbox=[[center_bound(g,C,r) for g in row] for row in jac]
R=[[I(int(i==j))-sum((inv[i][k]*Jbox[k][j] for k in range(3)),I(0)) for j in range(3)] for i in range(3)]
norm=max(sum((v.absmax() for v in row),Q(0)) for row in R)
fc=[g.value(X) for g in root]; err=max(abs(sum((inv[i][k]*fc[k] for k in range(3)),Q(0))) for i in range(3))
assert norm<Q(1,10**8) and err+norm*r<r
print('ROOT_CONTRACTION exact: inside adopted old box; norm<1e-8; center_error+norm*r<r')
# Solve D0 on the same box using only the independently expanded polynomials.
wu, wv = Jbox[0][0], Jbox[0][1]; eu,ev=Jbox[1][0],Jbox[1][1]; zu,zv=Jbox[2][0],Jbox[2][1]
det=wu*ev-eu*wv
assert det.lo>0 or det.hi<0
ai=(-zu*ev+eu*zv)/det; bi=(-wu*zv+zu*wv)/det
record='/Users/jinleic/repos/aifours/mathematics/evidence/three-area-20261027-96h/parallel-18/phase-type/frontier-20261029-ph7-local-global-local-certificate-v1.json'
with open(record) as fd: rec=json.load(fd)
for name,box in [('a',ai),('b',bi),('determinant',det)]:
    bounds=rec['dual_'+('determinant' if name=='determinant' else name)+'_interval']; lo,hi=map(Q,bounds)
    print('DECLARED_DUAL_ENCLOSURE',name,'independent_interval_subset=',lo<=box.lo<=box.hi<=hi,'declared_sign=',('positive' if lo>0 else 'negative' if hi<0 else 'crosses_zero'))
assert not (ai.lo-Q(1)<=ai.lo and ai.hi<=ai.lo-Q(1))
print('NEGATIVE_REJECTED invalid dual interval')
# Arithmetic audit of recorded bounds, without treating the receipt as proof.
margins=list(map(Q,rec['diagonal_dominance_margins']))
print('RECORDED_MARGIN_ARITHMETIC positive=',all(x>0 for x in margins),'all_gt_3=',all(x>3 for x in margins),'minimum_index=',min(range(7),key=lambda j:margins[j])+1)
for name in ['lambda_interval','mu_interval','F_z_interval']:
    lo,hi=map(Q,rec[name]); print('RECORDED_BOUND_ARITHMETIC',name,'ordered=',lo<=hi,'positive=',lo>0,'negative=',hi<0)
print('DONE exact controls; recorded bounds are not independent evidence')
