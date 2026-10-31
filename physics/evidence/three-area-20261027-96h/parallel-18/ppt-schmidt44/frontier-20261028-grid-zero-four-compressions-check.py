#!/usr/bin/env python3
"""Exact Gaussian-rational checks for Bob 0/4 mixed compression."""
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

def check(u,v):
    A=vec((0,0,u),(1,1,O),(2,2,O)); B=vec((0,1,O),(1,2,O))
    D=vec((1,0,u),(2,1,(F(-1),F(0)))); C=vec((0,2,O),(3,0,v))
    E=vec((2,0,u),(3,3,O)); V_F=vec((2,3,O)); G=vec((3,0,u))
    V_I=vec((3,2,O)); V_H=vec((0,0,v))
    basis=(A,B,D,C,E,V_F,G,V_I,V_H)
    target=[[Z for _ in range(16)] for _ in range(16)]
    for wt,b in zip((1,1,1,3,3,3,3,3,3),basis): outer_add(target,F(wt),b)
    actual=[[Z for _ in range(16)] for _ in range(16)]
    for z in ROOTS:
        z2=mul(z,z); z3=mul(z2,z)
        q=combine((z,A),(z2,B),((F(-1),F(0)),D),(z3,C))
        if not rank2(q): raise AssertionError('rank2 failure')
        outer_add(actual,F(1,4),q)
    for w,q in ((2,C),(3,E),(3,V_F),(3,G),(3,V_I),(3,V_H)):
        if not rank2(q): raise AssertionError('basis rank2 failure')
        outer_add(actual,F(w),q)
    bad=[(i,j) for i in range(16) for j in range(16) if actual[i][j]!=target[i][j]]
    if bad: raise AssertionError({'mismatches':bad})
    return {'u':[str(x) for x in u],'v':[str(x) for x in v],
            'rank2_phase_vectors_checked':4,'state_entries_checked':256,'mismatches':len(bad)}

cases=[(O,Z),(Z,O),(O,(F(2),F(0))),((F(1),F(1)),(F(1),F(-1))),(J,(F(3),F(0)))]
print(json.dumps({'cases':[check(u,v) for u,v in cases]},indent=2))
