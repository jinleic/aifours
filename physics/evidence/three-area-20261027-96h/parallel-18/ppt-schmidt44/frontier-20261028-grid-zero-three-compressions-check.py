#!/usr/bin/env python3
"""Exact Gaussian-rational checks of mixed Bob 0/3 compression formulas."""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import json
import runpy

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
    A=vec((0,0,u),(1,1,O),(2,2,O))
    B=vec((0,1,O),(1,2,O)); D=vec((1,0,u),(2,1,(F(-1),F(0))))
    C=vec((0,2,O),(3,3,O)); E=vec((2,0,u),(3,0,v))
    V_F=vec((2,0,v)); G=vec((3,0,u)); V_I=vec((3,2,O)); V_H=vec((0,3,O))
    basis=(A,B,D,C,E,V_F,G,V_I,V_H)
    target=[[Z for _ in range(16)] for _ in range(16)]
    for w,q in zip((1,1,1,3,3,3,3,3,3),basis): outer_add(target,F(w),q)
    actual=[[Z for _ in range(16)] for _ in range(16)]
    U=u[0]**2+u[1]**2; V=v[0]**2+v[1]**2
    X=2*U+3*V
    if not X: raise ValueError('rank-deficient map')
    t=scale(mul(conj(u),v),F(3)/X)
    delta=(6*U**2+6*U*V+9*V**2)/X
    for z in ROOTS:
        z2=mul(z,z); z3=mul(z2,z)
        q=combine((z,A),(O,B),(neg(z2),D),(neg(mul(z3,u)),vec((2,0,O))))
        if not rank2(q): raise AssertionError('q_z rank failure')
        outer_add(actual,F(1,4),q)
    for q in (C,V_I,V_H):
        if not rank2(q): raise AssertionError('basis rank failure')
        outer_add(actual,F(3),q)
    noise=vec((2,0,O),(3,0,t))
    outer_add(actual,X,noise); outer_add(actual,delta,vec((3,0,O)))
    bad=[(i,j) for i in range(16) for j in range(16) if target[i][j]!=actual[i][j]]
    if bad: raise AssertionError({'mismatches':bad})
    return {'u':[str(x) for x in u], 'v':[str(x) for x in v], 'X':str(X),
            't':[str(x) for x in t], 'delta':str(delta),
            'rank2_phase_vectors_checked':4,'entries_checked':256,'mismatches':0}

def symmetry():
    src=runpy.run_path(str(Path(__file__).with_name('frontier-20261028-grid-state-sr2-check.py')))
    rho=src['state']()
    pa=(2,1,0,3); sa=(-1,1,1,1)
    pb=(2,1,0,4,3); sb=(-1,1,1,-1,-1)
    transformed=[[0 for _ in range(20)] for _ in range(20)]
    for a in range(4):
        for b in range(5):
            for c in range(4):
                for d in range(5):
                    transformed[5*pa[a]+pb[b]][5*pa[c]+pb[d]]=sa[a]*sb[b]*sa[c]*sb[d]*rho[5*a+b][5*c+d]
    bad=[(i,j) for i in range(20) for j in range(20) if rho[i][j]!=transformed[i][j]]
    if bad: raise AssertionError({'symmetry_mismatches':bad})
    return {'checked_entries':400,'mismatches':len(bad),'bob_maps_span_0_3_to_span_2_4':True}

cases=[(O,Z),(Z,O),(O,(F(2),F(0))),((F(1),F(1)),(F(1),F(-1))),(J,(F(3),F(0)))]
print(json.dumps({'cases':[check(u,v) for u,v in cases],'source_local_symmetry':symmetry()},indent=2))
