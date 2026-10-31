#!/usr/bin/env python3
"""Exact 6-variable Bernstein proof for the second two-triangle H face.

All six rates are positive, theta in [0,1], first triangle coefficient=1.
Two endpoint polynomials are strictly positive; a two-polynomial cover proves
middle coefficient nonnegative OR strict quadratic Gram determinant. Uses
SymPy to construct polynomials and integer Bernstein arithmetic; a separate
stdlib replay must independently reconstruct and check the frozen output.
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
u=S.symbols('u0:6',real=True);theta=S.symbols('theta',real=True)
f=[None]+[sum(S.prod(a)for a in combinations(u,k))for k in range(1,5)]
f1,f2,f3,f4=f[1:];wa=S.prod(u[:3]);wb=theta*S.prod(u[3:]);W=wa+wb
A=f2-4*f1+S.Rational(74,9);B=f3-4*f2+S.Rational(74,9)*f1-S.Rational(28,3)-W
H0=f4-S.Rational(70,9)*f2+S.Rational(212,9)*f1-S.Rational(1007,27)-wa*sum(u[3:])-wb*sum(u[:3])
H1=f3-S.Rational(70,9)*f1+S.Rational(212,9)-W
H=S.Poly(S.expand(-243*(H0*A-H1*B)),theta);assert H.degree()==2
hb=[S.Poly(S.expand(sum(H.nth(j)*S.Rational(comb(k,j),comb(2,j))for j in range(k+1))),*u)for k in range(3)]
mid=2*hb[1];gram=4*hb[0]*hb[2]-mid*mid
polys=[('H0',hb[0]),('H2',hb[2]),('H1_twice',mid),('Gram4',gram)]
assert all(c.q==1 for _,p in polys for c in p.coeffs())


def digest(p):
    rows=[[list(k),str(int(c))]for k,c in sorted(p.as_dict().items())]
    return hashlib.sha256(json.dumps(rows,separators=(',',':')).encode()).hexdigest()


def grid(p):
    ds=p.degree_list();scale=1
    for d in ds:scale*=lcm(*(comb(d,i)for i in range(d+1)))
    arr=np.zeros(tuple(d+1 for d in ds),dtype=object)
    for key,c in p.as_dict().items():
        div=1
        for d,k in zip(ds,key):div*=comb(d,k)
        assert scale%div==0;arr[key]=int(c)*(scale//div)
    return arr


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


def single(p):
    stack=[('',grid(p),tuple((F(0),F(1))for _ in range(6)))];leaves=[]
    while stack:
        path,arr,bounds=stack.pop();depth=len(path)
        if depth>=6 and min(arr.flat)>=0 and strict_vertices(arr,bounds):leaves.append(path);continue
        assert depth<48,('single depth',path)
        axis=depth%6;L,R=split(arr,axis);lo,hi=bounds[axis];mid=(lo+hi)/2
        for bit,child,inter in [('1',R,(mid,hi)),('0',L,(lo,mid))]:
            b=list(bounds);b[axis]=inter;stack.append((path+bit,child,tuple(b)))
    return sorted(leaves)


def dual(p,q):
    stack=[('',grid(p),grid(q),tuple((F(0),F(1))for _ in range(6)))];pos=[];strict=[]
    while stack:
        path,a,b,bounds=stack.pop();depth=len(path)
        if min(a.flat)>=0:pos.append(path);continue
        if depth>=6 and min(b.flat)>=0 and strict_vertices(b,bounds):strict.append(path);continue
        assert depth<48,('dual depth',path)
        axis=depth%6;La,Ra=split(a,axis);Lb,Rb=split(b,axis);lo,hi=bounds[axis];midpoint=(lo+hi)/2
        for bit,aa,bb,inter in [('1',Ra,Rb,(midpoint,hi)),('0',La,Lb,(lo,midpoint))]:
            z=list(bounds);z[axis]=inter;stack.append((path+bit,aa,bb,tuple(z)))
    return sorted(pos),sorted(strict)

records=[]
for name,p in polys[:2]:
    paths=single(p);records.append({'name':name,'degrees':list(p.degree_list()),'terms':len(p.terms()),'sha256':digest(p),'strict_paths':paths})
    print(name,'strict leaves',len(paths),flush=True)
pos,strict=dual(mid,gram)
for name,p in polys[2:]:records.append({'name':name,'degrees':list(p.degree_list()),'terms':len(p.terms()),'sha256':digest(p)})
out=ROOT/'frontier-20261028-ph7-two-disjoint-triangle-universal-H-certificate-v1.json'
out.write_text(json.dumps({'face':'theta_A=1, theta_B in [0,1]','rates':'six strictly positive finite rates',
 'compactification':'u_i=s_i/(1-s_i)','axis':'path depth modulo 6','records':records,
 'dual_mid_nonnegative_paths':pos,'dual_gram_strict_paths':strict},indent=2)+'\n')
print('dual nonnegative/strict leaves',len(pos),len(strict),flush=True)
print('PASS: exact integer Bernstein face cover; saved',out)
