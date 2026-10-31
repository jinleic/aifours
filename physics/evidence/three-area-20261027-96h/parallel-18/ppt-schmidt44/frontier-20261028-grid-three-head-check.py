#!/usr/bin/env python3
"""Exact Gaussian-rational checks for a 3-complex-parameter projection chart."""
from fractions import Fraction as F
from itertools import combinations
import json

Z=(F(0),F(0)); O=(F(1),F(0))

def add(a,b): return (a[0]+b[0],a[1]+b[1])
def neg(a): return (-a[0],-a[1])
def mul(a,b): return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def scale(a,x): return (a[0]*x,a[1]*x)
def conj(a): return (a[0],-a[1])
def div(a,b):
    d=b[0]*b[0]+b[1]*b[1]
    if not d: raise ZeroDivisionError
    return scale(mul(a,conj(b)),1/d)

def vec(*terms):
    v=[Z]*16
    for a,b,c in terms: v[4*a+b]=add(v[4*a+b],c)
    return v

def combine(*terms):
    out=[Z]*16
    for c,v in terms: out=[add(x,mul(c,y)) for x,y in zip(out,v)]
    return out

def outer_cross(m,coefficient,v,w):
    for i,x in enumerate(v):
        for j,y in enumerate(w): m[i][j]=add(m[i][j],mul(coefficient,mul(x,conj(y))))

def outer_add(m,weight,v): outer_cross(m,(F(weight),F(0)),v,v)

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

def exact_hermitian_pivots(m):
    a=[list(row) for row in m]; pivots=[]
    while a:
        for i in range(len(a)):
            if a[i][i][1]!=0 or a[i][i][0]<0: return None
        p=next((i for i in range(len(a)) if a[i][i][0]>0),None)
        if p is None:
            return pivots if all(v==Z for row in a for v in row) else None
        pivot=a[p][p]; pivots.append(str(pivot[0]))
        rem=[i for i in range(len(a)) if i!=p]
        a=[[add(a[i][j],neg(div(mul(a[i][p],a[p][j]),pivot))) for j in rem] for i in rem]
    return pivots

def check(v0,v1,v2):
    A=vec((0,0,O),(1,1,O),(2,2,O)); B=vec((0,1,O),(1,2,O))
    D=vec((1,0,O),(2,1,(F(-1),F(0)))); C=vec((0,2,O),(3,3,O))
    E=vec((2,0,O),(3,0,v0),(3,1,v1),(3,2,v2))
    V_F=vec((2,0,v0),(2,1,v1),(2,2,v2))
    G=vec((3,0,O)); V_I=vec((3,2,O)); V_H=vec((0,3,O))
    X=combine((O,E),(neg(v0),G),(neg(v2),V_I))
    target=[[Z for _ in range(16)] for _ in range(16)]
    for wt,b in zip((1,1,1,3,3,3,3,3,3),(A,B,D,C,E,V_F,G,V_I,V_H)):
        outer_add(target,wt,b)
    parts=((0,O,B),(1,O,A),(2,(F(-1),F(0)),D),(3,(F(-1),F(0)),X),(4,neg(v1),G))
    q=[{} for _ in range(16)]
    for degree,c,basis in parts:
        for j,x in enumerate(basis):
            y=mul(c,x)
            if y!=Z: q[j]=padd(q[j],{degree:y})
    if not rank2_polynomial(q): raise AssertionError('rank2 polynomial failure')
    if len({degree%5 for degree,_,_ in parts})!=5: raise AssertionError('phase collision')
    actual=[[Z for _ in range(16)] for _ in range(16)]
    for _,c,basis in parts: outer_add(actual,c[0]**2+c[1]**2,basis)
    for basis in (C,V_F,V_H): outer_add(actual,3,basis)
    norm1=v1[0]**2+v1[1]**2
    t=(O,neg(v0),neg(v2)); HB=[]
    for i in range(3):
        row=[]
        for j in range(3):
            diag=(F(3)-norm1 if i==j==1 else F(3) if i==j else F(0),F(0))
            row.append(add(diag,neg(mul(t[i],conj(t[j])))))
        HB.append(row)
    for i,left in enumerate((E,G,V_I)):
        for j,right in enumerate((E,G,V_I)): outer_cross(actual,HB[i][j],left,right)
    bad=[(i,j) for i in range(16) for j in range(16) if target[i][j]!=actual[i][j]]
    if bad: raise AssertionError({'entry_mismatches':bad})
    return {'v0':[str(x) for x in v0],'v1':[str(x) for x in v1],'v2':[str(x) for x in v2],
            'H_psd_pivots':exact_hermitian_pivots(HB),'entries_checked':256,'mismatches':len(bad),
            'all_16_rank_minor_polynomials_zero':True}

samples=[(Z,Z,Z),((F(1,2),F(0)),(F(1,2),F(0)),(F(1,2),F(0))),
         ((F(0),F(1,2)),(F(1,2),F(0)),(F(1,2),F(0))),
         (Z,O,O),(O,O,Z),((F(2),F(0)),Z,Z)]
print(json.dumps({'cases':[check(*x) for x in samples]},indent=2))
