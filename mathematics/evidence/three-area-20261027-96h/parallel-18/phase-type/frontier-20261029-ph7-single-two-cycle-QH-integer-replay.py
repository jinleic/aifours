#!/usr/bin/env python3
"""Stdlib Fraction reconstruction/replay of single-two-cycle endpoint covers."""
from fractions import Fraction as F
from itertools import combinations,product
from math import comb,lcm,prod
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parent
C=json.loads((ROOT/'frontier-20261029-ph7-single-two-cycle-QH-certificate-v1.json').read_text());n=6;zero=(0,)*n

def clean(a):return {k:v for k,v in a.items()if v}
def const(c):return {zero:F(c)}if c else{}
def add(a,b):
 out=a.copy()
 for k,v in b.items():out[k]=out.get(k,F(0))+v
 return clean(out)
def scale(a,c):return clean({k:v*F(c)for k,v in a.items()})
def sub(a,b):return add(a,scale(b,-1))
def mul(a,b):
 out={}
 for k,x in a.items():
  for l,y in b.items():
   t=tuple(k[i]+l[i]for i in range(n));out[t]=out.get(t,F(0))+x*y
 return clean(out)
def total(*seq):
 out={}
 for p in seq:out=add(out,p)
 return out
def mult(seq):
 out=const(1)
 for p in seq:out=mul(out,p)
 return out
U=[]
for i in range(6):U.append({tuple(int(j==i)for j in range(6)):F(1)})
f=[]
for k in (1,2,3,4):
 out={}
 for term in combinations(U,k):out=add(out,mult(term))
 f.append(out)
f1,f2,f3,f4=f;A=total(f2,scale(f1,-4),const(F(74,9)));B=total(f3,scale(f2,-4),scale(f1,F(74,9)),const(F(-28,3)))
h0=total(f4,scale(f2,F(-70,9)),scale(f1,F(212,9)),const(F(-1007,27)));h1=total(f3,scale(f1,F(-70,9)),const(F(212,9)))
Q=scale(sub(mul(A,sub(A,U[0])),mul(sub(f1,const(4)),B)),81)
H=scale(sub(mul(h0,sub(A,U[0])),mul(sub(h1,mul(U[0],total(*U[1:]))),B)),-243)
polys={'Q1':Q,'H1':H}
def digest(p):
 assert all(c.denominator==1 for c in p.values());rows=[[list(k),str(int(c))]for k,c in sorted(p.items())]
 return hashlib.sha256(json.dumps(rows,separators=(',',':')).encode()).hexdigest()

def grid(p):
 m=3;stride=[m**(5-i)for i in range(6)];common=lcm(*(comb(2,i)for i in range(m)))**6;a=[0]*(m**6)
 for key,c in p.items():
  div=prod(comb(2,k)for k in key);assert common%div==0;a[sum(key[j]*stride[j]for j in range(6))]=int(c)*(common//div)
 return a,stride

def split(a,stride,axis):
 L=[0]*len(a);R=[0]*len(a);other=[j for j in range(6)if j!=axis]
 for coord in product(range(3),repeat=5):
  base=sum(coord[k]*stride[other[k]]for k in range(5));idx=[base+j*stride[axis]for j in range(3)];lev=[[a[i]for i in idx]]
  while len(lev[-1])>1:lev.append([x+y for x,y in zip(lev[-1],lev[-1][1:])])
  for k in range(3):L[idx[k]]=lev[k][0]*(1<<(2-k));R[idx[k]]=lev[2-k][-1]*(1<<k)
 return L,R

def vertex(a,stride,bounds):
 found=False
 for corner in product((0,1),repeat=6):
  xyz=[bounds[j][corner[j]]for j in range(6)]
  if all(0<x<1 for x in xyz):
   found=True;idx=sum((0 if corner[j]==0 else 2)*stride[j]for j in range(6))
   if a[idx]<=0:return False
 return found

def replay(p,paths):
 assert len(paths)==len(set(paths));leaves=set(paths);prefix={p[:j]for p in leaves for j in range(len(p)+1)};seen=set();a,stride=grid(p)
 def walk(path,a,bounds):
  dep=len(path)
  if path in leaves:seen.add(path);assert dep>=6 and min(a)>=0 and vertex(a,stride,bounds);return
  assert path+'0'in prefix and path+'1'in prefix;axis=dep%6;L,R=split(a,stride,axis);lo,hi=bounds[axis];mid=(lo+hi)/2
  z=list(bounds);z[axis]=(lo,mid);walk(path+'0',L,tuple(z));z=list(bounds);z[axis]=(mid,hi);walk(path+'1',R,tuple(z))
 walk('',a,tuple((F(0),F(1))for _ in range(6)));assert seen==leaves
 return len(seen)

counts=[]
for rec in C['records']:
 p=polys[rec['name']];assert len(p)==rec['terms'] and rec['degrees']==[2]*6 and digest(p)==rec['sha256']
 count=replay(p,rec['strict_paths']);counts.append(count);print(rec['name'],'checked',count,'strict leaves',flush=True)
assert counts==[2025,2613]
print('PASS: independent Fraction polynomial reconstruction, coefficient digests, complete integer covers and strictness')
