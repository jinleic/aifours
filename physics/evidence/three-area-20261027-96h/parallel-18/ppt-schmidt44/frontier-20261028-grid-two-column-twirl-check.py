#!/usr/bin/env python3
"""Exact Gaussian-rational checks of a two-column projection decomposition.

Representative t,h values test the all-ratio written construction; they do
not prove the continuous parameter theorem. No floating arithmetic is used.
"""
from fractions import Fraction as F
from itertools import combinations
import json


Z = (F(0), F(0))
ONE = (F(1), F(0))
I = (F(0), F(1))
ROOTS = (ONE, I, (F(-1),F(0)), (F(0),F(-1)))


def add(a,b): return (a[0]+b[0],a[1]+b[1])
def neg(a): return (-a[0],-a[1])
def mul(a,b): return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def scale(a,x): return (a[0]*x,a[1]*x)
def conj(a): return (a[0],-a[1])
def inv(a):
    n=a[0]*a[0]+a[1]*a[1]
    if n==0: raise ZeroDivisionError
    return (a[0]/n,-a[1]/n)


def vec(*terms):
    out=[Z]*16
    for a,b,c in terms:
        out[4*a+b]=add(out[4*a+b],c)
    return out


def combine(*terms):
    out=[Z]*16
    for coeff,v in terms:
        out=[add(x,mul(coeff,y)) for x,y in zip(out,v)]
    return out


def outer_add(m, weight, v):
    for i,x in enumerate(v):
        for j,y in enumerate(v):
            m[i][j]=add(m[i][j],scale(mul(x,conj(y)),weight))


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
    ua=(ONE,z,mul(z,z),w)
    ub=(ONE,inv(z),mul(inv(z),inv(z)),mul(mul(z,z),inv(w)))
    return [mul(mul(ua[j//4],ub[j%4]),x) for j,x in enumerate(v)]


def check(t,h):
    # Take v=1 and u=-t^2. Other common nonzero scales are local filters.
    u=neg(mul(t,t)); r=t[0]*t[0]+t[1]*t[1]; H=h*h
    A=vec((0,0,ONE),(1,1,ONE),(2,2,ONE))
    B=vec((0,1,ONE),(1,2,ONE))
    D=vec((1,0,ONE),(2,1,(F(-1),F(0))))
    C=vec((0,2,ONE),(3,3,ONE))
    E=vec((2,0,ONE),(3,3,u))
    V_F=vec((2,3,u)); G=vec((3,0,ONE)); V_I=vec((3,2,ONE)); V_H=vec((0,3,ONE))
    tt=mul(t,t); t3=mul(tt,t)
    plus=combine((ONE,A),(t,C),(inv(t),E))
    minus=combine((ONE,A),(mul(I,t),C),(neg(mul(I,inv(t))),E),
                  (scale(mul(I,inv(t3)),h),V_F),
                  (scale(mul(I,t),F(2,1)/h),G),
                  (scale(tt,F(-2,1)/h),V_I),((h,F(0)),V_H))
    basis=(A,B,D,C,E,V_F,G,V_I,V_H)
    target=[[Z for _ in range(16)] for _ in range(16)]
    for weight,v in zip((1,1,1,3,3,3,3,3,3),basis): outer_add(target,F(weight),v)
    actual=[[Z for _ in range(16)] for _ in range(16)]
    count=0
    for z in ROOTS:
        for w in ROOTS:
            for q in (plus,minus):
                v=phase(q,z,w)
                if not rank2(v): raise AssertionError('rank2 failure')
                outer_add(actual,F(1,32),v)
                count+=1
    residual=(F(3)-r,F(3)-1/r,F(3)-H/(2*r**3),F(3)-2*r/H,
              F(3)-2*r*r/H,F(3)-H/2)
    if min(residual)<0: raise AssertionError({'negative_residual':residual})
    for weight,v in ((F(1),B),(F(1),D),*zip(residual,(C,E,V_F,G,V_I,V_H))):
        if not rank2(v): raise AssertionError('basis rank2 failure')
        outer_add(actual,weight,v)
    bad=[(i,j) for i in range(16) for j in range(16) if target[i][j]!=actual[i][j]]
    if bad: raise AssertionError({'mismatches':bad})
    trace=sum(target[j][j][0] for j in range(16))
    return {'t':[str(x) for x in t],'h':str(h),'r':str(r),'u':[str(x) for x in u],
            'rank2_twirl_vectors_checked':count,'entries_checked':256,'mismatches':len(bad),
            'residual_weights':[str(x) for x in residual],'unnormalized_trace':str(trace)}


cases=[((F(1),F(0)),F(1)),((F(3,2),F(0)),F(2)),
       ((F(2,3),F(0)),F(2,3)),((F(0),F(1)),F(1)),
       ((F(1),F(1)),F(2))]
print(json.dumps({'cases':[check(t,h) for t,h in cases]},indent=2))
