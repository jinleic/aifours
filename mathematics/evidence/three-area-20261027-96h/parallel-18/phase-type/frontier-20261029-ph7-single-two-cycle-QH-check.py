#!/usr/bin/env python3
"""Exact critical Q/H endpoint covers for a single two-cycle on x and u0."""
from fractions import Fraction as F
from itertools import combinations,product
from math import comb,lcm
from pathlib import Path
import hashlib,json,sys
import numpy as np
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'frontier-20261028-localdeps'))
import sympy as S
u=S.symbols('u0:6',real=True);f=[None]+[sum(S.prod(a)for a in combinations(u,k))for k in range(1,5)]
f1,f2,f3,f4=f[1:];A=f2-4*f1+S.Rational(74,9);B=f3-4*f2+S.Rational(74,9)*f1-S.Rational(28,3)
h0=f4-S.Rational(70,9)*f2+S.Rational(212,9)*f1-S.Rational(1007,27);h1=f3-S.Rational(70,9)*f1+S.Rational(212,9)
Q=S.Poly(S.expand(81*(A*(A-u[0])-(f1-4)*B)),*u)
H=S.Poly(S.expand(-243*(h0*(A-u[0])-(h1-u[0]*sum(u[1:]))*B)),*u)
assert all(c.q==1 for p in [Q,H]for c in p.coeffs())
def digest(p):
 rows=[[list(k),str(int(c))]for k,c in sorted(p.as_dict().items())]
 return hashlib.sha256(json.dumps(rows,separators=(',',':')).encode()).hexdigest()
def grid(p):
 ds=p.degree_list();scale=1
 for d in ds:scale*=lcm(*(comb(d,i)for i in range(d+1)))
 a=np.zeros(tuple(d+1 for d in ds),dtype=object)
 for key,c in p.as_dict().items():
  div=1
  for d,k in zip(ds,key):div*=comb(d,k)
  assert scale%div==0;a[key]=int(c)*(scale//div)
 return a
def split(a,axis):
 a=np.moveaxis(a,axis,0);d=a.shape[0]-1;lev=[a]
 while len(lev[-1])>1:lev.append(lev[-1][:-1]+lev[-1][1:])
 L=np.stack([lev[j][0]*(1<<(d-j))for j in range(d+1)]);R=np.stack([lev[d-j][-1]*(1<<j)for j in range(d+1)])
 return np.moveaxis(L,0,axis),np.moveaxis(R,0,axis)
def vertex(a,bounds):
 found=False
 for corner in product((0,1),repeat=6):
  xyz=[bounds[j][corner[j]]for j in range(6)]
  if all(0<x<1 for x in xyz):
   found=True;idx=tuple(0 if c==0 else a.shape[j]-1 for j,c in enumerate(corner))
   if a[idx]<=0:return False
 return found
def cover(p):
 stack=[('',grid(p),tuple((F(0),F(1))for _ in range(6)))];leaves=[]
 while stack:
  path,a,bounds=stack.pop();dep=len(path)
  if dep>=6 and min(a.flat)>=0 and vertex(a,bounds):leaves.append(path);continue
  assert dep<48,('depth limit',path)
  axis=dep%6;L,R=split(a,axis);lo,hi=bounds[axis];mid=(lo+hi)/2
  for bit,child,inter in [('1',R,(mid,hi)),('0',L,(lo,mid))]:
   z=list(bounds);z[axis]=inter;stack.append((path+bit,child,tuple(z)))
 return sorted(leaves)
records=[]
for name,p in [('Q1',Q),('H1',H)]:
 paths=cover(p);records.append({'name':name,'degrees':list(p.degree_list()),'terms':len(p.terms()),'sha256':digest(p),'strict_paths':paths})
 print(name,'leaves',len(paths),flush=True)
out=ROOT/'frontier-20261029-ph7-single-two-cycle-QH-certificate-v1.json'
out.write_text(json.dumps({'domain':'six positive finite diagonal rates, theta=1','compactification':'u_i=s_i/(1-s_i)',
 'axis':'path depth modulo six','records':records},indent=2)+'\n')
print('PASS: exact Q/H theta1 endpoint covers; saved',out)
