#!/usr/bin/env python3
"""Exact Gaussian-rational checks for two uniform projection decompositions.

The five values checked here are finite samples of two algebraic formulas;
their all-complex-domain correctness is proved separately in the receipt.
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

def vec(*terms):
    v=[Z]*16
    for a,b,c in terms: v[4*a+b]=add(v[4*a+b],c)
    return v

def combine(*terms):
    out=[Z]*16
    for c,v in terms: out=[add(x,mul(c,y)) for x,y in zip(out,v)]
    return out

def outer_add(m,w,v):
    for i,x in enumerate(v):
        for j,y in enumerate(v): m[i][j]=add(m[i][j],scale(mul(x,conj(y)),w))

def rank2(v):
    m=[v[4*i:4*i+4] for i in range(4)]
    for rr in combinations(range(4),3):
        for cc in combinations(range(4),3):
            a,b,c=rr; x,y,z=cc
            d=add(add(mul(m[a][x],add(mul(m[b][y],m[c][z]),neg(mul(m[b][z],m[c][y])))),
                      neg(mul(m[a][y],add(mul(m[b][x],m[c][z]),neg(mul(m[b][z],m[c][x])))))),
                  mul(m[a][z],add(mul(m[b][x],m[c][y]),neg(mul(m[b][y],m[c][x])))))
            if d!=Z: return False
    return True

def phase(v,z,w):
    ua=(O,z,mul(z,z),w)
    ub=(O,inv(z),mul(inv(z),inv(z)),mul(mul(z,z),inv(w)))
    return [mul(mul(ua[k//4],ub[k%4]),x) for k,x in enumerate(v)]

def check(u,v,regime):
    A=vec((0,0,O),(1,1,O),(2,2,O))
    B=vec((0,1,O),(1,2,O))
    D=vec((1,0,O),(2,1,(F(-1),F(0))))
    C=vec((0,2,O),(3,3,v)); E=vec((2,0,O),(3,3,u))
    V_F=vec((2,3,u)); G=vec((3,0,O)); V_I=vec((3,2,O)); V_H=vec((0,3,v))
    if regime=='large':
        p=mul(v,inv(u)); p2=p[0]**2+p[1]**2
        if p2>4: raise ValueError('outside large regime')
        q=combine((O,A),(O,B),((F(-1),F(0)),D),(O,C),
                  (scale(p,F(3,4)),V_F),((F(4,3),F(0)),G),((F(3,2),F(0)),V_H))
        residual=((F(2),C),(F(3),E),(F(3)-F(9,16)*p2,V_F),
                  (F(11,9),G),(F(3),V_I),(F(3,4),V_H))
    else:
        p=mul(u,inv(v)); p2=p[0]**2+p[1]**2
        if p2>F(1,4): raise ValueError('outside small regime')
        q=combine((O,A),(O,B),((F(-1),F(0)),D),((F(-1),F(0)),E),
                  (scale(p,F(-2)),G),(p,V_I),(O,V_H))
        residual=((F(3),C),(F(2),E),(F(3),V_F),
                  (F(3)-4*p2,G),(F(3)-p2,V_I),(F(2),V_H))
    if not rank2(q): raise AssertionError('seed is not rank<=2')
    target=[[Z for _ in range(16)] for _ in range(16)]
    for wt,b in zip((1,1,1,3,3,3,3,3,3),(A,B,D,C,E,V_F,G,V_I,V_H)):
        outer_add(target,F(wt),b)
    actual=[[Z for _ in range(16)] for _ in range(16)]
    for z in ROOTS:
        for w in ROOTS:
            x=phase(q,z,w)
            if not rank2(x): raise AssertionError('twirled rank failure')
            outer_add(actual,F(1,16),x)
    for wt,b in residual:
        if wt<0 or not rank2(b): raise AssertionError('invalid residual')
        outer_add(actual,wt,b)
    bad=[(i,j) for i in range(16) for j in range(16) if actual[i][j]!=target[i][j]]
    if bad: raise AssertionError({'mismatches':bad})
    return {'regime':regime,'u':[str(x) for x in u],'v':[str(x) for x in v],
            'p':[str(x) for x in p],'p_norm_squared':str(p2),'checked_twirl_vectors':16,
            'checked_state_entries':256,'mismatches':len(bad),
            'residual_weights':[str(x[0]) for x in residual]}

cases=[(O,(F(2),F(0)),'large'),(O,Z,'large'),
       ((F(1),F(1)),(F(1),F(-1)),'large'),
       (Z,O,'small'),(O,(F(2),F(0)),'small'),
       (J,(F(3),F(0)),'small')]
print(json.dumps({'cases':[check(u,v,regime) for u,v,regime in cases]},indent=2))
