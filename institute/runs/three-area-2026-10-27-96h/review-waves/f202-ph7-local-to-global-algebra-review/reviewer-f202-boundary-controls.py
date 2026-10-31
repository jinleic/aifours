#!/usr/bin/env python3
"""Exact targeted boundary witness search; no-witness outcome is not exclusion."""
from fractions import Fraction as Q
from itertools import combinations, combinations_with_replacement

def es(v,k):
    s=Q(0)
    for c in combinations(v,k):
        t=Q(1)
        for x in c: t*=x
        s+=t
    return s
z=Q(410210220392063003,500000000000000000)
def data(v):
    f=[Q(1)]+[es(v,k) for k in range(1,5)]
    A=f[2]-4*f[1]+10-2*z; B=f[3]-4*f[2]+(10-2*z)*f[1]+12*z-20
    h1=f[3]-(6+2*z)*f[1]+20+4*z
    h0=f[4]-(6+2*z)*f[2]+(20+4*z)*f[1]+3*z*z+6*z-45
    D=h1-A*sum(v[:4]); H=-(h0*A-h1*B); Qp=A*A-(f[1]-4)*B
    return f[1],A,B,D,H,Qp

def solve(prefix,idx):
    lo=data(prefix+(Q(0),))[idx]; hi=data(prefix+(Q(1),))[idx]; slope=hi-lo
    if slope==0: return None
    x=-lo/slope
    assert data(prefix+(x,))[idx]==0
    return x

def fmt(v): return ','.join(map(str,v))
vals=[Q(5,11),Q(1,2),Q(3,5),Q(7,10),Q(4,5),Q(9,10),Q(1),Q(11,10),Q(6,5),Q(13,10),Q(37,27)]
checks=0; nb=0; mc=0
for p in combinations_with_replacement(vals,5):
    x=solve(p,1)
    if x is not None and p[-1]<=x<=Q(37,27):
        f1,A,B,D,H,Qp=data(p+(x,)); checks+=1
        if f1>=4 and B>=0:
            nb+=1
            if nb==1: print('NB_BOUNDARY_WITNESS',fmt(p+(x,)),'f1',f1,'B',B,'Q',Qp)
vals=[Q(7,9),Q(4,5),Q(9,10),Q(1),Q(11,10),Q(6,5),Q(13,10),Q(7,5),Q(3,2),Q(8,5),Q(5,3)]
checks2=0
for p in combinations_with_replacement(vals,5):
    x=solve(p,3)
    if x is not None and p[-1]<=x<=Q(5,3):
        f1,A,B,D,H,Qp=data(p+(x,)); checks2+=1
        if f1>=4 and A>0 and H<=0:
            mc+=1
            if mc==1: print('MC_BOUNDARY_WITNESS',fmt(p+(x,)),'f1',f1,'A',A,'H',H)
print('EXACT_BOUNDARY_SEARCH', 'NB_sorted_A0',checks,'NB_uncovered',nb,'MC_sorted_D0',checks2,'MC_uncovered',mc)
assert data((Q(1),)*6)[1]!=0
print('NEGATIVE_REJECTED fixed tuple not on A=0 boundary')
