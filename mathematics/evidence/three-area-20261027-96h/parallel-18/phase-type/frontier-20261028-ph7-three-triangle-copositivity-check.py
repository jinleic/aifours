#!/usr/bin/env python3
"""Exact six-rate Bernstein covers for the unique graph's simplex reduction.

All six rates are positive. Certifies three positive diagonals, three paired
copositivity alternatives, one two-edge OR, and two ternary cross alternatives.
Polynomial construction uses SymPy, subdivision uses exact Python integers.
A separate stdlib replay is required for independent code evidence.
"""
from fractions import Fraction as F
from itertools import combinations,product
from math import comb,lcm
from pathlib import Path
import hashlib,json,sys
import numpy as np
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'frontier-20261028-localdeps'))
import sympy as S
u=S.symbols('u0:6',real=True);ta,tb=S.symbols('ta tb',real=True)
f=[None]+[sum(S.prod(q)for q in combinations(u,k))for k in range(1,5)]
f1,f2,f3,f4=f[1:];wa=ta*S.prod(u[:3]);wb=tb*S.prod(u[3:]);W=wa+wb
A=f2-4*f1+S.Rational(74,9);B=f3-4*f2+S.Rational(74,9)*f1-S.Rational(28,3)-W
h0=f4-S.Rational(70,9)*f2+S.Rational(212,9)*f1-S.Rational(1007,27)-wa*sum(u[3:])-wb*sum(u[:3])
h1=f3-S.Rational(70,9)*f1+S.Rational(212,9)-W;T=u[1]+u[2]+u[4]+u[5]
krel=(1-ta)*u[0]*u[3];H=S.expand(-243*(h0*(A-krel)-(h1-krel*T)*B))
assert S.Poly(H,ta,tb).total_degree()==2
verts=[(0,0),(1,0),(1,1)];D=[]
for a,b in verts:D.append(S.Poly(S.expand(H.subs({ta:a,tb:b})),*u))
pairs=[(0,1),(0,2),(1,2)];O=[]
for i,j in pairs:
    a=S.Rational(verts[i][0]+verts[j][0],2);b=S.Rational(verts[i][1]+verts[j][1],2)
    O.append(S.Poly(S.expand(4*H.subs({ta:a,tb:b})-D[i].as_expr()-D[j].as_expr()),*u))
G=[4*D[i]*D[j]-O[k]*O[k]for k,(i,j)in enumerate(pairs)]
C12=2*O[2]*D[0]-O[0]*O[1];C01=2*O[0]*D[2]-O[1]*O[2]
polys={**{f'D{i}':p for i,p in enumerate(D)},**{f'O{i}':p for i,p in enumerate(O)},
       **{f'G{i}':p for i,p in enumerate(G)},'C12':C12,'C01':C01}
assert all(c.q==1 for p in polys.values()for c in p.coeffs())


def digest(p):
    rows=[[list(k),str(int(c))]for k,c in sorted(p.as_dict().items())]
    return hashlib.sha256(json.dumps(rows,separators=(',',':')).encode()).hexdigest()

def grid(p):
    ds=p.degree_list();scale=1
    for d in ds:scale*=lcm(*(comb(d,j)for j in range(d+1)))
    a=np.zeros(tuple(d+1 for d in ds),dtype=object)
    for key,c in p.as_dict().items():
        div=1
        for d,j in zip(ds,key):div*=comb(d,j)
        assert scale%div==0;a[key]=int(c)*(scale//div)
    return a

def split(a,axis):
    a=np.moveaxis(a,axis,0);d=a.shape[0]-1;lev=[a]
    while len(lev[-1])>1:lev.append(lev[-1][:-1]+lev[-1][1:])
    L=np.stack([lev[j][0]*(1<<(d-j))for j in range(d+1)])
    R=np.stack([lev[d-j][-1]*(1<<j)for j in range(d+1)])
    return np.moveaxis(L,0,axis),np.moveaxis(R,0,axis)

def strict_vertices(a,bounds):
    found=False
    for corner in product((0,1),repeat=6):
        xyz=[bounds[j][corner[j]]for j in range(6)]
        if all(0<x<1 for x in xyz):
            found=True;idx=tuple(0 if b==0 else a.shape[j]-1 for j,b in enumerate(corner))
            if a[idx]<=0:return False
    return found

def cover(names,strict):
    stack=[('',[grid(polys[n])for n in names],tuple((F(0),F(1))for _ in range(6)))];paths=[[]for _ in names]
    while stack:
        path,arrays,bounds=stack.pop();dep=len(path);chosen=None
        for i,a in enumerate(arrays):
            if min(a.flat)>=0 and (not strict[i] or (dep>=6 and strict_vertices(a,bounds))):chosen=i;break
        if chosen is not None:paths[chosen].append(path);continue
        assert dep<48,('depth limit',names,path)
        axis=dep%6;parts=[split(a,axis)for a in arrays];lo,hi=bounds[axis];mid=(lo+hi)/2
        for bit,index,inter in [('1',1,(mid,hi)),('0',0,(lo,mid))]:
            z=list(bounds);z[axis]=inter;stack.append((path+bit,[p[index]for p in parts],tuple(z)))
    return [sorted(q)for q in paths]

specs=[(['D0'],[True]),(['D1'],[True]),(['D2'],[True]),
       (['O0','G0'],[False,True]),(['O1','G1'],[False,True]),(['O2','G2'],[False,True]),
       (['O0','O2'],[False,False]),(['O0','O1','C12'],[False,False,False]),
       (['O1','O2','C01'],[False,False,False])]
records={n:{'degrees':list(p.degree_list()),'terms':len(p.terms()),'sha256':digest(p)}for n,p in polys.items()};covers=[]
for names,strict in specs:
    paths=cover(names,strict);covers.append({'names':names,'strict':strict,'paths':paths})
    print('/'.join(names),'leaves',[len(p)for p in paths],flush=True)
out=ROOT/'frontier-20261028-ph7-three-triangle-copositivity-certificate-v1.json'
out.write_text(json.dumps({'domain':'six finite strictly positive rates','compactification':'u_i=s_i/(1-s_i)',
 'axis':'path depth modulo six','records':records,'covers':covers},indent=2)+'\n')
print('PASS: exact integer simplex copositivity cover; saved',out)
