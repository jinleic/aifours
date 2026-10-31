#!/usr/bin/env python3
"""Exact strict 6-rate Bernstein certificate for the three-triangle Q00 corner."""
from fractions import Fraction as F
from itertools import combinations,product
from math import comb,lcm
from pathlib import Path
import hashlib,json,sys
import numpy as np
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'frontier-20261028-localdeps'))
import sympy as S
u=S.symbols('u0:6',real=True)
f1=sum(u);f2=sum(S.prod(a)for a in combinations(u,2));f3=sum(S.prod(a)for a in combinations(u,3))
A=f2-4*f1+S.Rational(74,9);B=f3-4*f2+S.Rational(74,9)*f1-S.Rational(28,3);k=u[0]*u[3]
P=S.Poly(S.expand(81*(A*(A-k)-(f1-4)*B)),*u);assert all(c.q==1 for c in P.coeffs())
rows=[[list(q),str(int(c))]for q,c in sorted(P.as_dict().items())]
digest=hashlib.sha256(json.dumps(rows,separators=(',',':')).encode()).hexdigest()

def grid(p):
    ds=p.degree_list();scale=1
    for d in ds:scale*=lcm(*(comb(d,i)for i in range(d+1)))
    a=np.zeros(tuple(d+1 for d in ds),dtype=object)
    for key,c in p.as_dict().items():
        div=1
        for d,j in zip(ds,key):div*=comb(d,j)
        assert scale%div==0;a[key]=int(c)*(scale//div)
    return a

def split(a,axis):
    a=np.moveaxis(a,axis,0);d=a.shape[0]-1;lev=[a]
    while len(lev[-1])>1:lev.append(lev[-1][:-1]+lev[-1][1:])
    left=np.stack([lev[j][0]*(1<<(d-j))for j in range(d+1)])
    right=np.stack([lev[d-j][-1]*(1<<j)for j in range(d+1)])
    return np.moveaxis(left,0,axis),np.moveaxis(right,0,axis)

def strict_vertices(a,bounds):
    found=False
    for corner in product((0,1),repeat=6):
        coord=[bounds[j][corner[j]]for j in range(6)]
        if all(0<x<1 for x in coord):
            found=True;idx=tuple(0 if b==0 else a.shape[j]-1 for j,b in enumerate(corner))
            if a[idx]<=0:return False
    return found

stack=[('',grid(P),tuple((F(0),F(1))for _ in range(6)))];leaves=[]
while stack:
    path,a,bounds=stack.pop();dep=len(path)
    if dep>=6 and min(a.flat)>=0 and strict_vertices(a,bounds):leaves.append(path);continue
    assert dep<48,('depth limit',path)
    axis=dep%6;L,R=split(a,axis);lo,hi=bounds[axis];mid=(lo+hi)/2
    for bit,child,inter in [('1',R,(mid,hi)),('0',L,(lo,mid))]:
        x=list(bounds);x[axis]=inter;stack.append((path+bit,child,tuple(x)))
leaves.sort();out=ROOT/'frontier-20261028-ph7-three-triangle-Q00-certificate-v1.json'
out.write_text(json.dumps({'corner':'theta_A=theta_B=0, k=u0*u3','rates':'six strictly positive finite rates',
 'compactification':'u_i=s_i/(1-s_i)','axis':'path depth modulo 6','degrees':list(P.degree_list()),
 'terms':len(P.terms()),'sha256':digest,'strict_paths':leaves},indent=2)+'\n')
print('PASS: three-triangle Q00 corner, strict leaves',len(leaves),'saved',out)
