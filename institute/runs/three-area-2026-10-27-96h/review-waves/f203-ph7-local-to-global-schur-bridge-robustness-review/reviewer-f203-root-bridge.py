#!/usr/bin/env python3
"""Independent rational endpoint/dual enclosure controls, not author code."""
from fractions import Fraction as Q
from itertools import combinations
from math import comb
import json
from pathlib import Path

zero=(0,0,0)
class P:
    def __init__(self, d): self.d={k:Q(v) for k,v in d.items() if v}
    @staticmethod
    def c(x): return P({zero:Q(x)})
    def __add__(self, other):
        if not isinstance(other,P): other=P.c(other)
        d=self.d.copy()
        for k,v in other.d.items(): d[k]=d.get(k,Q(0))+v
        return P(d)
    __radd__=__add__
    def __neg__(self): return P({k:-v for k,v in self.d.items()})
    def __sub__(self,other): return self+-other if isinstance(other,P) else self+-Q(other)
    def __rsub__(self,other): return -self+other
    def __mul__(self,other):
        if not isinstance(other,P): other=P.c(other)
        out={}
        for a,x in self.d.items():
            for b,y in other.d.items():
                k=tuple(i+j for i,j in zip(a,b)); out[k]=out.get(k,Q(0))+x*y
        return P(out)
    __rmul__=__mul__
    def __pow__(self,n):
        p=P.c(1)
        for _ in range(n): p=p*self
        return p
    def diff(self,i):
        out={}
        for k,v in self.d.items():
            if k[i]:
                t=list(k); t[i]-=1; out[tuple(t)]=v*k[i]
        return P(out)
    def at(self,point):
        return sum((a*prod(point[i]**k[i] for i in range(3)) for k,a in self.d.items()),Q(0))
    def shifted_bound(self,center,radius):
        shifted={}
        for k,a in self.d.items():
            for j0 in range(k[0]+1):
                for j1 in range(k[1]+1):
                    for j2 in range(k[2]+1):
                        j=(j0,j1,j2)
                        t=a*prod(comb(k[i],j[i])*center[i]**(k[i]-j[i]) for i in range(3))
                        shifted[j]=shifted.get(j,Q(0))+t
        mid=shifted.get(zero,Q(0))
        err=sum((abs(c)*radius**sum(k) for k,c in shifted.items() if k!=zero),Q(0))
        return I(mid-err,mid+err)

def prod(items):
    x=1
    for y in items: x=x*y
    return x

def es(xs,k):
    return sum((prod(t) for t in combinations(xs,k)),P.c(0))

class I:
    def __init__(self,lo,hi=None):
        self.lo=Q(lo); self.hi=Q(lo if hi is None else hi); assert self.lo<=self.hi
    def __add__(self,other):
        if not isinstance(other,I): other=I(other)
        return I(self.lo+other.lo,self.hi+other.hi)
    __radd__=__add__
    def __neg__(self): return I(-self.hi,-self.lo)
    def __sub__(self,other): return self+-other if isinstance(other,I) else self+-Q(other)
    def __rsub__(self,other): return -self+other
    def __mul__(self,other):
        if not isinstance(other,I): other=I(other)
        a=[self.lo*other.lo,self.lo*other.hi,self.hi*other.lo,self.hi*other.hi]
        return I(min(a),max(a))
    __rmul__=__mul__
    def __truediv__(self,other):
        if not isinstance(other,I): other=I(other)
        assert other.lo*other.hi>0
        return self*I(1/other.hi,1/other.lo)
    def absmax(self): return max(abs(self.lo),abs(self.hi))

def inverse(m):
    a=[row[:]+[Q(int(i==j)) for j in range(3)] for i,row in enumerate(m)]
    for i in range(3):
        if not a[i][i]:
            j=next(j for j in range(i+1,3) if a[j][i]); a[i],a[j]=a[j],a[i]
        pivot=a[i][i]; a[i]=[x/pivot for x in a[i]]
        for j in range(3):
            if j!=i:
                v=a[j][i]; a[j]=[x-v*y for x,y in zip(a[j],a[i])]
    return [row[3:] for row in a]

u=P({(1,0,0):1}); v=P({(0,1,0):1}); z=P({(0,0,1):1})
vs=[v,v,u,u,u,u,u]
e=[es(vs,k) for k in range(7)]
p=e[1]-4
q=e[2]-4*e[1]+10-2*z
W=e[3]-4*e[2]+(10-2*z)*e[1]+12*z-20
E=e[4]-(6+2*z)*e[2]+(20+4*z)*e[1]+3*z*z+6*z-45
E2=e[5]-(1+z)**2*p-(4+4*z)*q
E1=e[6]-(1+z)**2*q
Z=E1-2*v*E2
fs=[W,E,Z]
center=[Q(334696976789746519,250000000000000000),Q(208405938226799943,200000000000000000),Q(410210220392063003,500000000000000000)]
r=Q(1,10**16)
old=[Q(1338787907,10**9),Q(1042029691,10**9),Q(820420441,10**9)]
assert all(abs(x-y)+r<Q(1,10**7) for x,y in zip(center,old))
jac=[[f.diff(j) for j in range(3)] for f in fs]
j0=[[x.at(center) for x in row] for row in jac]
pre=inverse(j0)
assert all(sum(pre[i][k]*j0[k][j] for k in range(3))==int(i==j) for i in range(3) for j in range(3))
jbox=[[p.shifted_bound(center,r) for p in row] for row in jac]
def norm_for(jb):
    return max(sum((I(int(i==j))-sum((pre[i][k]*jb[k][j] for k in range(3)),I(0))).absmax() for j in range(3)) for i in range(3))
norm=norm_for(jbox)
err=max(abs(sum(pre[i][k]*fs[k].at(center) for k in range(3))) for i in range(3))
assert norm<Q(1,10**8) and err+norm*r<r
small=err/(1-norm)
assert small<r
swapped=[jbox[1],jbox[0],jbox[2]]
assert norm_for(swapped)>1
print('PASS nested root box and rational contraction; wrong-row-swap fails contraction')
for n in range(16,24):
    if small<Q(1,10**n): best=n
print('ROOT_DEVIATION_LT_10_NEGATIVE_POWER:',best)

# Grouped dual is solved from exact grouped partials on an enclosure of the root.
wj=[W.diff(i).shifted_bound(center,small) for i in (0,1)]
ej=[E.diff(i).shifted_bound(center,small) for i in (0,1)]
zj=[Z.diff(i).shifted_bound(center,small) for i in (0,1)]
det=wj[0]*ej[1]-ej[0]*wj[1]
assert det.lo>0
ia=(-zj[0]*ej[1]+ej[0]*zj[1])/det
ib=(-wj[0]*zj[1]+zj[0]*wj[1])/det
cert=json.loads(Path('/Users/jinleic/repos/aifours/mathematics/evidence/three-area-20261027-96h/parallel-18/phase-type/frontier-20261029-ph7-local-global-local-certificate-v1.json').read_text())
ca=[Q(s) for s in cert['dual_a_interval']]; cb=[Q(s) for s in cert['dual_b_interval']]
subseta=ca[0]<=ia.lo<=ia.hi<=ca[1]
subsetb=cb[0]<=ib.lo<=ib.hi<=cb[1]
print('DUAL_INTERVAL_SUBSET recorded-a:',subseta,'recorded-b:',subsetb,'positive-determinant:',det.lo>0)
assert subseta and subsetb
print('PASS exact independent root-to-recorded-dual containment')
