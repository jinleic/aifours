#!/usr/bin/env python3
"""Bounded exact rational counterexample search, not a covering proof."""
from fractions import Fraction as Q
from itertools import combinations, combinations_with_replacement

def es(v,k):
    out=Q(0)
    for subset in combinations(v,k):
        term=Q(1)
        for x in subset: term*=x
        out+=term
    return out
z=Q(410210220392063003,500000000000000000)
vals=list(map(Q,['1/10','1/2','1','6/5','7/5','2','3','5']))
assert Q(820420341,10**9)<z<Q(820420541,10**9)
count=0; cq=ch=cb=cc=0; first={}
for v in combinations_with_replacement(vals,6):
    f=[Q(1)]+[es(v,k) for k in range(1,5)]
    A=f[2]-4*f[1]+10-2*z
    B=f[3]-4*f[2]+(10-2*z)*f[1]+12*z-20
    h1=f[3]-(6+2*z)*f[1]+20+4*z
    h0=f[4]-(6+2*z)*f[2]+(20+4*z)*f[1]+3*z*z+6*z-45
    D=h1-A*sum(v[:4]); Qp=A*A-(f[1]-4)*B; Hp=-(h0*A-h1*B)
    outsideN=not all(Q(5,11)<=x<=Q(37,27) for x in v)
    outsideM=not all(Q(7,9)<=x<=Q(5,3) for x in v)
    if outsideN and Qp<=0:
        cq+=1; first.setdefault('QO',v)
        if f[1]>=4 and A<=0: cb+=1; first.setdefault('QO_CASE_B',v)
    if outsideM and Hp<=0:
        ch+=1; first.setdefault('HO',v)
        if f[1]>=4 and A>0 and D<=0: cc+=1; first.setdefault('HO_CASE_C',v)
    count+=1
print('EXACT_RATIONAL_GRID',count,'QO_violations',cq,'HO_violations',ch,'QO_case_b',cb,'HO_case_c',cc)
for k,v in first.items(): print('EXACT_WITNESS',k,','.join(map(str,v)))
# Coverage is NOT inferred from no witnesses.
assert count==1716
assert not all(Q(5,11)<=x<=Q(37,27) for x in [Q(1,10)]*6)
print('NEGATIVE_REJECTED outside point cannot be called N6')
