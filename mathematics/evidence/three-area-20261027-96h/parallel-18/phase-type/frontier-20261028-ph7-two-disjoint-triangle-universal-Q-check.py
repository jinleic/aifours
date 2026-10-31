#!/usr/bin/env python3
"""Exact strict Bernstein certificate for the both-full triangle Q corner."""
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
A=f2-4*f1+S.Rational(74,9)
B=f3-4*f2+S.Rational(74,9)*f1-S.Rational(28,3)-S.prod(u[:3])-S.prod(u[3:])
P=S.Poly(S.expand(81*(A*A-(f1-4)*B)),*u);assert all(c.q==1 for c in P.coeffs())
rows=[[list(k),str(int(c))]for k,c in sorted(P.as_dict().items())]
digest=hashlib.sha256(json.dumps(rows,separators=(',',':')).encode()).hexdigest()

def grid(p):
    ds=p.degree_list();scale=1
    for d in ds:scale*=lcm(*(comb(d,i)for i in range(d+1)))
    A=np.zeros(tuple(d+1 for d in ds),dtype=object)
    for key,c in p.as_dict().items():
        div=1
        for d,k in zip(ds,key):div*=comb(d,k)
        assert scale%div==0;A[key]=int(c)*(scale//div)
    return A

def split(A,axis):
    A=np.moveaxis(A,axis,0);d=A.shape[0]-1;lev=[A]
    while len(lev[-1])>1:lev.append(lev[-1][:-1]+lev[-1][1:])
    left=np.stack([lev[k][0]*(1<<(d-k))for k in range(d+1)])
    right=np.stack([lev[d-k][-1]*(1<<k)for k in range(d+1)])
    return np.moveaxis(left,0,axis),np.moveaxis(right,0,axis)

def strict_vertices(A,bounds):
    found=False
    for corner in product((0,1),repeat=6):
        coord=[bounds[i][corner[i]]for i in range(6)]
        if all(0<x<1 for x in coord):
            found=True;idx=tuple(0 if c==0 else A.shape[i]-1 for i,c in enumerate(corner))
            if A[idx]<=0:return False
    return found

stack=[('',grid(P),tuple((F(0),F(1))for _ in range(6)))];leaves=[]
while stack:
    path,A,bounds=stack.pop();depth=len(path)
    if depth>=6 and min(A.flat)>=0 and strict_vertices(A,bounds):leaves.append(path);continue
    assert depth<48,('depth limit',path)
    axis=depth%6;L,R=split(A,axis);lo,hi=bounds[axis];mid=(lo+hi)/2
    for bit,child,inter in [('1',R,(mid,hi)),('0',L,(lo,mid))]:
        b=list(bounds);b[axis]=inter;stack.append((path+bit,child,tuple(b)))
leaves.sort();out=ROOT/'frontier-20261028-ph7-two-disjoint-triangle-universal-Q-certificate-v1.json'
out.write_text(json.dumps({'corner':'theta_A=theta_B=1','rates':'six strictly positive finite rates',
 'compactification':'u_i=s_i/(1-s_i)','axis':'path depth modulo 6','degrees':list(P.degree_list()),
 'terms':len(P.terms()),'sha256':digest,'strict_paths':leaves},indent=2)+'\n')
print('PASS: strict two-triangle Q corner, leaves',len(leaves),'saved',out)
