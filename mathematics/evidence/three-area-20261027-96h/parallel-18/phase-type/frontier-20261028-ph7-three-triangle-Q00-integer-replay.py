#!/usr/bin/env python3
"""Independent stdlib Fraction reconstruction/replay of the three-triangle Q00 cover."""
from fractions import Fraction as F
from itertools import combinations,product
from math import comb,lcm,prod
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parent
C=json.loads((ROOT/'frontier-20261028-ph7-three-triangle-Q00-certificate-v1.json').read_text())
n=6;zero=(0,)*n

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
def sumall(*seq):
    out={}
    for p in seq:out=add(out,p)
    return out
def mult(seq):
    out=const(1)
    for p in seq:out=mul(out,p)
    return out
U=[]
for i in range(6):
    key=tuple(int(j==i)for j in range(6));U.append({key:F(1)})
f=[]
for k in (1,2,3):
    out={}
    for term in combinations(U,k):out=add(out,mult(term))
    f.append(out)
f1,f2,f3=f;A=sumall(f2,scale(f1,-4),const(F(74,9)));B=sumall(f3,scale(f2,-4),scale(f1,F(74,9)),const(F(-28,3)));k=mul(U[0],U[3]);P=scale(sub(mul(A,sub(A,k)),mul(sub(f1,const(4)),B)),81)
assert all(v.denominator==1 for v in P.values())
rows=[[list(key),str(int(c))]for key,c in sorted(P.items())]
assert len(P)==C['terms'] and hashlib.sha256(json.dumps(rows,separators=(',',':')).encode()).hexdigest()==C['sha256']
assert C['degrees']==[2]*6

def grid():
    degree=2;m=3;stride=[m**(5-i)for i in range(6)];common=lcm(*(comb(degree,i)for i in range(m)))**6;a=[0]*(m**6)
    for key,c in P.items():
        div=prod(comb(degree,k)for k in key);assert common%div==0
        a[sum(key[j]*stride[j]for j in range(6))]=int(c)*(common//div)
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

paths=C['strict_paths'];assert len(paths)==len(set(paths));leaves=set(paths);prefix={p[:j]for p in leaves for j in range(len(p)+1)};seen=set();a,stride=grid()
def walk(path,a,bounds):
    dep=len(path)
    if path in leaves:seen.add(path);assert dep>=6 and min(a)>=0 and vertex(a,stride,bounds);return
    assert path+'0'in prefix and path+'1'in prefix;axis=dep%6;L,R=split(a,stride,axis);lo,hi=bounds[axis];mid=(lo+hi)/2
    z=list(bounds);z[axis]=(lo,mid);walk(path+'0',L,tuple(z));z=list(bounds);z[axis]=(mid,hi);walk(path+'1',R,tuple(z))
walk('',a,tuple((F(0),F(1))for _ in range(6)));assert seen==leaves and len(seen)==1972
print('PASS: independently reconstructed Q00, coefficient hash, complete 1972-leaf integer cover and interior strictness')
