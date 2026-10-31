#!/usr/bin/env python3
"""Gaussian-rational and Laurent-polynomial checks of Bob 1/3 compressions.

Large-ratio seeds are symbolic in z, and fifth-root averages are computed by
exact coefficient orthogonality, not floating-point approximations to roots.
"""
from fractions import Fraction as F
from itertools import combinations
import json

Z=(F(0),F(0)); O=(F(1),F(0)); J=(F(0),F(1))
ROOTS=(O,J,(F(-1),F(0)),(F(0),F(-1)))

def add(a,b): return (a[0]+b[0],a[1]+b[1])
def neg(a): return (-a[0],-a[1])
def mul(a,b): return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def scale(a,x): return (a[0]*x,a[1]*x)
def conj(a): return (a[0],-a[1])
def inv(a):
    d=a[0]**2+a[1]**2
    if not d: raise ZeroDivisionError
    return (a[0]/d,-a[1]/d)
def power(a,n):
    x=O
    for _ in range(abs(n)): x=mul(x,a if n>=0 else inv(a))
    return x

def vec(*terms):
    out=[Z]*16
    for a,b,x in terms: out[4*a+b]=add(out[4*a+b],x)
    return out

def combine(*terms):
    out=[Z]*16
    for c,v in terms: out=[add(x,mul(c,y)) for x,y in zip(out,v)]
    return out

def outer_add(m,w,v):
    for i,x in enumerate(v):
        for j,y in enumerate(v): m[i][j]=add(m[i][j],scale(mul(x,conj(y)),w))

def phase(v,z):
    ua=(O,z,power(z,2),power(z,3)); ub=(O,power(z,-1),power(z,-2),power(z,-5))
    return [mul(mul(ua[k//4],ub[k%4]),x) for k,x in enumerate(v)]

def padd(p,q):
    out=dict(p)
    for k,x in q.items(): out[k]=add(out.get(k,Z),x)
    return {k:x for k,x in out.items() if x!=Z}

def pneg(p): return {k:neg(x) for k,x in p.items()}
def pmul(p,q):
    out={}
    for i,a in p.items():
        for j,b in q.items(): out[i+j]=add(out.get(i+j,Z),mul(a,b))
    return {k:x for k,x in out.items() if x!=Z}

def rank2_polynomial(v):
    m=[v[4*i:4*i+4] for i in range(4)]
    for rr in combinations(range(4),3):
        for cc in combinations(range(4),3):
            a,b,c=rr; x,y,z=cc
            d=padd(padd(pmul(m[a][x],padd(pmul(m[b][y],m[c][z]),pneg(pmul(m[b][z],m[c][y])))),
                         pneg(pmul(m[a][y],padd(pmul(m[b][x],m[c][z]),pneg(pmul(m[b][z],m[c][x])))))),
                   pmul(m[a][z],padd(pmul(m[b][x],m[c][y]),pneg(pmul(m[b][y],m[c][x])))))
            if d: return False
    return True

def rank2(v): return rank2_polynomial([{0:x} if x!=Z else {} for x in v])

def check(u,v,regime):
    A=vec((0,0,O),(1,1,u),(2,2,O)); B=vec((0,1,u),(1,2,O))
    D=vec((1,0,O),(2,1,neg(u))); C=vec((0,2,O),(3,3,O))
    E=vec((2,0,O),(3,1,v)); V_F=vec((2,1,v)); G=vec((3,0,O))
    V_I=vec((3,2,O)); V_H=vec((0,3,O))
    target=[[Z for _ in range(16)] for _ in range(16)]
    for w,x in zip((1,1,1,3,3,3,3,3,3),(A,B,D,C,E,V_F,G,V_I,V_H)):
        outer_add(target,F(w),x)
    actual=[[Z for _ in range(16)] for _ in range(16)]
    if regime=='small':
        p=mul(u,inv(v)); p2=p[0]**2+p[1]**2
        if p2>1: raise ValueError('outside small regime')
        q=combine((O,A),(O,B),(p,V_F))
        for z in ROOTS:
            transformed=phase(q,z)
            if not rank2(transformed): raise AssertionError('small seed rank failure')
            outer_add(actual,F(1,4),transformed)
        residual=((F(1),D),(F(3),C),(F(3),E),(F(3)-p2,V_F),
                  (F(3),G),(F(3),V_I),(F(3),V_H))
        rank_check='4 evaluated phase vectors, all 16 minors each'
    else:
        p=mul(v,inv(u)); p2=p[0]**2+p[1]**2
        if p2>1: raise ValueError('outside large regime')
        parts=((0,O,B),(1,O,A),(2,(F(-1),F(0)),D),
               (3,(F(-1),F(0)),E),(4,neg(p),G))
        q=[{} for _ in range(16)]
        for degree,coefficient,term in parts:
            for j,x in enumerate(term):
                c=mul(coefficient,x)
                if c!=Z: q[j]=padd(q[j],{degree:c})
        if not rank2_polynomial(q): raise AssertionError('large symbolic seed rank failure')
        # All exponents are distinct modulo 5, so root average retains only diagonal terms.
        if len({degree%5 for degree,_,_ in parts})!=5: raise AssertionError('phase collision')
        for _,coefficient,term in parts:
            outer_add(actual,coefficient[0]**2+coefficient[1]**2,term)
        residual=((F(2),E),(F(3),C),(F(3),V_F),
                  (F(3)-p2,G),(F(3),V_I),(F(3),V_H))
        rank_check='16 zero determinant polynomials for all z; 5-root orthogonality exact'
    for w,x in residual:
        if w<0 or not rank2(x): raise AssertionError('invalid residual')
        outer_add(actual,w,x)
    bad=[(i,j) for i in range(16) for j in range(16) if actual[i][j]!=target[i][j]]
    if bad: raise AssertionError({'mismatches':bad})
    return {'regime':regime,'u':[str(x) for x in u],'v':[str(x) for x in v],
            'p_norm_squared':str(p2),'rank_check':rank_check,'entries_checked':256,
            'mismatches':len(bad),'residual_weights':[str(w) for w,_ in residual]}

cases=[(Z,O,'small'),(O,(F(2),F(0)),'small'),(J,O,'small'),
       ((F(1),F(1)),(F(2),F(0)),'small'),(O,Z,'large'),
       ((F(2),F(0)),O,'large'),(O,J,'large'),((F(1),F(1)),(F(1),F(-1)),'large')]
print(json.dumps({'cases':[check(u,v,r) for u,v,r in cases]},indent=2))
