#!/usr/bin/env python3
"""Independent centered rational coefficient bounds; no author code imported."""
from fractions import Fraction as Q
from itertools import combinations
from pathlib import Path
import json

N=8
zero=(0,)*N
class P:
    def __init__(self,d): self.d={k:Q(v) for k,v in d.items() if v}
    @staticmethod
    def c(x): return P({zero:Q(x)})
    @staticmethod
    def variable(i,center,radius):
        k=list(zero); k[i]=1
        return P({zero:center,tuple(k):radius})
    def __add__(self,other):
        if not isinstance(other,P): other=P.c(other)
        d=self.d.copy()
        for k,v in other.d.items(): d[k]=d.get(k,Q(0))+v
        return P(d)
    __radd__=__add__
    def __neg__(self): return P({k:-v for k,v in self.d.items()})
    def __sub__(self,other): return self+-other if isinstance(other,P) else self+-Q(other)
    def __rsub__(self,other): return -self+other
    def __mul__(self,other):
        if not isinstance(other,P):
            return P({k:v*Q(other) for k,v in self.d.items()})
        d={}
        for a,x in self.d.items():
            for b,y in other.d.items():
                k=tuple(i+j for i,j in zip(a,b)); d[k]=d.get(k,Q(0))+x*y
        return P(d)
    __rmul__=__mul__
    def __truediv__(self,x): return self*(1/Q(x))
    def __pow__(self,n):
        p=P.c(1)
        for _ in range(n): p=p*self
        return p
    def diff(self,i):
        d={}
        for k,v in self.d.items():
            if k[i]:
                j=list(k); j[i]-=1; d[tuple(j)]=v*k[i]
        return P(d)
    def bound(self):
        center=self.d.get(zero,Q(0))
        err=sum((abs(v) for k,v in self.d.items() if k!=zero),Q(0))
        return center-err,center+err
    def absmax(self):
        lo,hi=self.bound(); return max(abs(lo),abs(hi))

def prod(xs):
    y=P.c(1)
    for x in xs: y=y*x
    return y

def es(v,k): return sum((prod(c) for c in combinations(v,k)),P.c(0))

root=Path('/Users/jinleic/repos/aifours/mathematics/evidence/three-area-20261027-96h/parallel-18/phase-type/frontier-20261029-ph7-local-global-local-certificate-v1.json')
record=json.loads(root.read_text())
U=Q(334696976789746519,250000000000000000)
V=Q(208405938226799943,200000000000000000)
z0=Q(410210220392063003,500000000000000000)
r=Q(1,10**16)
rho=Q(1,500)
delta=rho+r
centers=[V,V,U,U,U,U,U,z0]
v=[P.variable(i,centers[i],delta) for i in range(7)]
z=P.variable(7,z0,delta)
a0=Q(-13352719290130737,10**15)
b0=Q(343503525735997,50000000000000)
ai=[Q(x) for x in record['dual_a_interval']]
bi=[Q(x) for x in record['dual_b_interval']]
ae=max(abs(x-a0) for x in ai)
be=max(abs(x-b0) for x in bi)
RN=record['R_numerators_denominator_1000000']
R=[[Q(x,10**6) for x in row] for row in RN]
assert all(R[i][i]==1 and all(R[i][j]==0 for j in range(i)) for i in range(7))

e=[es(v,k) for k in range(7)]
p=e[1]-4
q=e[2]-4*e[1]+10-2*z
W=e[3]-4*e[2]+(10-2*z)*e[1]+12*z-20
E=e[4]-(6+2*z)*e[2]+(20+4*z)*e[1]+3*z*z+6*z-45
E2=e[5]-(1+z)**2*p-(4+4*z)*q
E1=e[6]-(1+z)**2*q
s=v[0]+v[1]
s4=sum(v[:4],P.c(0))
alpha=es(v[:4],3)-s*es(v[3:],2)
bjoint=v[0]*v[1]-s*s
Z=E1-s*E2
F=Z+a0*W+b0*E-E*E
lam=a0+alpha+b0*s4-W/2-s4*E
mu=b0+bjoint-E
LB=lam.bound()[0]-ae-be*s4.absmax()
MB=mu.bound()[0]-be
FZ=F.diff(7)/delta
WZ=W.diff(7)/delta
EZ=E.diff(7)/delta
FZ_hi=FZ.bound()[1]+ae*WZ.absmax()+be*EZ.absmax()
assert LB>0 and MB>0 and FZ_hi<0
wrong_mu=-b0+bjoint-E
assert wrong_mu.bound()[1]+be<0
print('PASS uniform local lambda>0, mu>0 and Fz<0; wrong-sign mu negative detected',flush=True)

def directional(poly,col):
    return sum((poly.diff(k)*(R[k][col]/delta) for k in range(7) if R[k][col]),P.c(0))

firstF=[directional(F,i) for i in range(7)]
firstW=[directional(W,i) for i in range(7)]
firstE=[directional(E,i) for i in range(7)]
T={}
for i in range(7):
    for j in range(i,7):
        ff=-directional(firstF[i],j)
        ww=-directional(firstW[i],j)
        ee=-directional(firstE[i],j)
        lo,hi=ff.bound()
        err=ae*ww.absmax()+be*ee.absmax()
        T[i,j]=(lo-err,hi+err)
        T[j,i]=T[i,j]
margins=[]
for i in range(7):
    margins.append(T[i,i][0]-sum(max(abs(T[i,j][0]),abs(T[i,j][1])) for j in range(7) if i!=j))
assert min(margins)>3
wrong_sign_diag=-T[0,0][1]-sum(max(abs(T[0,j][0]),abs(T[0,j][1])) for j in range(1,7))
assert wrong_sign_diag<0
print('PASS independent centered congruence diagonal dominance; all margins>3; reversed-Hessian negative detected',flush=True)
print('END uniform root-box local sign control; full global cover not attempted',flush=True)
