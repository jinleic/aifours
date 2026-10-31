#!/usr/bin/env python3
"""Independent exact Gaussian-rational verification of f44 candidates.

No author scripts or author output are imported. All arithmetic below uses
Fraction pairs; all range/minor and 256/400-entry identities are exact.
"""
from fractions import Fraction as F
from itertools import combinations,permutations
from pathlib import Path
import importlib.util

ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('poly',ROOT/'frontier-review-f8-exact-check-v1.py')
poly=importlib.util.module_from_spec(spec); spec.loader.exec_module(poly)
Z=(F(0),F(0)); O=(F(1),F(0)); I=(F(0),F(1))


def Q(x):
    if isinstance(x,tuple): return (F(x[0]),F(x[1]))
    return (F(x),F(0))

def add(x,y): return (x[0]+y[0],x[1]+y[1])
def neg(x): return (-x[0],-x[1])
def sub(x,y): return add(x,neg(y))
def mul(x,y): return (x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def conj(x): return (x[0],-x[1])
def div(x,y):
    norm=y[0]*y[0]+y[1]*y[1]
    if not norm: raise ZeroDivisionError
    z=mul(x,conj(y)); return (z[0]/norm,z[1]/norm)
def abs2(x): return x[0]**2+x[1]**2

def vec(terms,bob):
    out=[Z]*(4*bob)
    for a,b,value in terms:
        out[a*bob+b]=add(out[a*bob+b],Q(value))
    return out

def scale(v,c):
    c=Q(c); return [mul(c,x) for x in v]
def vsum(*vectors):
    out=[Z]*len(vectors[0])
    for v in vectors: out=[add(x,y) for x,y in zip(out,v)]
    return out

def outer(v): return [[mul(x,conj(y)) for y in v] for x in v]
def matzero(n): return [[Z]*n for _ in range(n)]
def matadd(A,B): return [[add(x,y) for x,y in zip(a,b)] for a,b in zip(A,B)]
def matscale(A,c):
    c=Q(c); return [[mul(c,x) for x in row] for row in A]
def weighted(vectors):
    out=matzero(len(vectors[0][1]))
    for weight,v in vectors: out=matadd(out,matscale(outer(v),weight))
    return out

def pt(M,bob):
    n=4*bob
    return [[M[(i//bob)*bob+(j%bob)][(j//bob)*bob+(i%bob)] for j in range(n)] for i in range(n)]

def trace(M):
    return sum((M[i][i][0] for i in range(len(M))),F(0))

def realrank(M):
    assert all(x[1]==0 for row in M for x in row)
    A=[[x[0] for x in row] for row in M]
    rows=len(A); cols=len(A[0]); rank=0
    for c in range(cols):
        pivot=next((r for r in range(rank,rows) if A[r][c]),None)
        if pivot is None: continue
        A[rank],A[pivot]=A[pivot],A[rank]
        p=A[rank][c]
        A[rank]=[x/p for x in A[rank]]
        for r in range(rank+1,rows):
            if A[r][c]:
                f=A[r][c]; A[r]=[x-f*y for x,y in zip(A[r],A[rank])]
        rank+=1
        if rank==rows: break
    return rank

def project(v,omit):
    return [v[5*a+b] for a in range(4) for b in range(5) if b!=omit]

def mapk(v,u,w):
    out=[Z]*16
    for a in range(4):
        for b in range(5):
            if b<3: index=b; coeff=O
            else: index=3; coeff=u if b==3 else w
            out[4*a+index]=add(out[4*a+index],mul(coeff,v[5*a+b]))
    return out

def det3(m):
    result=Z
    for p in permutations(range(3)):
        inversions=sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))
        term=O
        for i in range(3): term=mul(term,m[i][p[i]])
        result=add(result,neg(term) if inversions%2 else term)
    return result

def rank2(v):
    M=[v[4*r:4*r+4] for r in range(4)]
    return all(det3([[M[r][c] for c in cs] for r in rs])==Z
               for rs in combinations(range(4),3) for cs in combinations(range(4),3))

def phase4(v,z,w):
    z2=mul(z,z); zi=conj(z); zmi=conj(z2); wi=conj(w)
    la=(O,z,z2,w); lb=(O,zi,zmi,mul(z2,wi))
    return [mul(mul(la[a],lb[b]),v[4*a+b]) for a in range(4) for b in range(4)]

def twirl(v):
    phases=(O,I,neg(O),neg(I))
    phased=[phase4(v,z,w) for z in phases for w in phases]
    assert all(rank2(q) for q in phased)
    return matscale(weighted([(1,q) for q in phased]),F(1,16))

A=vec([(0,0,1),(1,1,1),(2,2,1)],5)
B=vec([(0,1,1),(1,2,1)],5)
D=vec([(1,0,1),(2,1,-1)],5)
C=vec([(0,2,1),(3,4,1)],5)
E=vec([(2,0,1),(3,3,1)],5)
V=[A,B,D,C,E,vec([(2,3,1)],5),vec([(3,0,1)],5),vec([(3,2,1)],5),vec([(0,4,1)],5)]
weights=[1,1,1,3,3,3,3,3,3]
R=weighted(list(zip(weights,V)))
assert trace(R)==31 and realrank(R)==9
PPT=weighted([
 (1,vec([(0,1,1),(1,0,1)],5)),(1,vec([(1,2,1),(2,1,1)],5)),
 (F(1,3),vec([(0,2,3),(1,1,1),(2,0,1)],5)),
 (F(2,3),vec([(1,1,1),(2,0,-2)],5)),
 (3,vec([(0,4,1),(3,2,1)],5)),(3,vec([(2,3,1),(3,0,1)],5)),
 (1,vec([(0,0,1)],5)),(1,vec([(2,2,1)],5)),
 (3,vec([(3,3,1)],5)),(3,vec([(3,4,1)],5)),
])
assert pt(R,5)==PPT
assert realrank(PPT)==10
print('PASS 4x5 state trace=31 rank=9, PT=10 positive projectors entrywise, PT rank=10')

# Direct symbolic minors in original 4x5 range, entirely separate from author code.
n=9; a,b,c,d,e,f,g,ii,h=(poly.var(n,k) for k in range(n)); zero=poly.coerce(n,0)
M=[[a,b,c,zero,h],[d,a,b,zero,zero],[e,-d,a,f,zero],[g,zero,ii,e,c]]
gens=[e*(a*a-b*d),c*(a*a+b*d),e*(b*b-a*c),-c*(d*d+a*e),a**3+b*b*e-d*d*c-a*c*e]
minors=[poly.det([[M[r][col] for col in cs] for r in rs])
        for rs in combinations(range(4),3) for cs in combinations(range(5),3)]
assert all(any(m==q or m==-q for m in minors) for q in gens)
g1,g2,g3,g4,g5=gens
assert 2*a*(g5-g3-g4)-c*g1-e*g2==2*a**4
assert a*(g5-g3-g4)-c*g1+e*g2-a**4==a*a*c*e+2*b*c*d*e
print('PASS all five are actual 3x3 minors; corrected 2a^4 identity and primary residual exact')

tr=[]; ranks=[]; ptranks=[]
for omit in range(5):
    P=[project(v,omit) for v in V]
    Rj=weighted(list(zip(weights,P)))
    tr.append(int(trace(Rj))); ranks.append(realrank(Rj)); ptranks.append(realrank(pt(Rj,4)))
    if omit in (0,1,2): assert all(rank2(v) for v in P)
    if omit==3:
        pp=[project(A,3),project(B,3),project(D,3),project(vec([(2,0,1)],5),3)]
        A3,B3,D3,E20=pp
        phases=(O,I,neg(O),neg(I))
        qs=[vsum(scale(A3,z),B3,scale(D3,neg(mul(z,z))),scale(E20,neg(mul(mul(z,z),z)))) for z in phases]
        assert all(rank2(q) for q in qs)
        result=matscale(weighted([(1,q) for q in qs]),F(1,4))
        result=matadd(result,weighted([(2,E20),(3,P[3]),(3,P[6]),(3,P[7]),(3,P[8])]))
        assert result==Rj
    if omit==4:
        E02=project(vec([(0,2,1)],5),4)
        A4,B4,D4=P[0],P[1],P[2]
        phases=(O,I,neg(O),neg(I))
        qs=[vsum(scale(A4,z),scale(B4,mul(z,z)),scale(D4,-1),scale(E02,mul(mul(z,z),z))) for z in phases]
        assert all(rank2(q) for q in qs)
        result=matscale(weighted([(1,q) for q in qs]),F(1,4))
        result=matadd(result,weighted([(2,E02),(3,P[4]),(3,P[5]),(3,P[6]),(3,P[7])]))
        assert result==Rj
assert tr==[23,28,23,25,25] and ranks==[8,9,8,8,8] and ptranks==[9,10,9,9,9]
print('PASS five projections exact traces',tr,'ranks',ranks,'PT ranks',ptranks)
print('PASS j=0,1,2 direct rank<=2 and j=3,4 twirl rank/minor + full 256-entry decompositions')

samples=[('large',Q(1),Q(2)),('large',Q(1),Q(0)),('large',Q((1,1)),Q((1,-1))),
         ('small',Q(0),Q(1)),('small',Q(1),Q(2)),('small',I,Q(3))]
for case,u,w in samples:
    P=[mapk(v,u,w) for v in V]
    target=weighted(list(zip(weights,P)))
    if case=='large':
        pp=div(w,u); assert abs2(w)<=4*abs2(u)
        q=vsum(P[0],P[1],scale(P[2],-1),P[3],scale(P[5],mul(Q(F(3,4)),pp)),
               scale(P[6],F(4,3)),scale(P[8],F(3,2)))
        res=[(2,P[3]),(3,P[4]),(3-F(9,16)*abs2(pp),P[5]),(F(11,9),P[6]),(3,P[7]),(F(3,4),P[8])]
    else:
        pp=div(u,w); assert 4*abs2(u)<=abs2(w)
        q=vsum(P[0],P[1],scale(P[2],-1),scale(P[4],-1),scale(P[6],mul(Q(-2),pp)),
               scale(P[7],pp),P[8])
        res=[(3,P[3]),(2,P[4]),(3,P[5]),(3-4*abs2(pp),P[6]),(3-abs2(pp),P[7]),(2,P[8])]
    assert all(weight>=0 for weight,_ in res)
    assert all(rank2(vec) for _,vec in res)
    result=matadd(twirl(q),weighted(res))
    assert result==target
    print('PASS',case,'u',u,'v',w,'16 rank2 twirl kets + nonnegative residuals + 256 exact entries')
print('PASS all six Gaussian-rational compression samples; no universal claim from sampling alone')
