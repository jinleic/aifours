#!/usr/bin/env python3
"""Independent stdlib integer replay of six-rate girth>=4 obstruction."""
import hashlib,itertools,json,math
from fractions import Fraction as Q
from pathlib import Path
ROOT=Path(__file__).resolve().parent
C=json.loads((ROOT/'frontier-20261028-ph7-girth4-critical-bernstein-certificate.json').read_text())
n=6;zero=(0,)*n

def clean(a):return {k:v for k,v in a.items()if v}
def const(c):return {zero:Q(c)}if c else{}
def add(a,b):
 o=a.copy()
 for k,v in b.items():o[k]=o.get(k,Q(0))+v
 return clean(o)
def scale(a,c):return clean({k:v*Q(c)for k,v in a.items()})
def sub(a,b):return add(a,scale(b,-1))
def mul(a,b):
 o={}
 for k,x in a.items():
  for l,y in b.items():
   key=tuple(k[i]+l[i]for i in range(n));o[key]=o.get(key,Q(0))+x*y
 return clean(o)
def sum_p(*a):
 o={}
 for v in a:o=add(o,v)
 return o
U=[]
for i in range(n):
 e=[0]*n;e[i]=1;U.append({tuple(e):Q(1)})
def prod(items):
 o=const(1)
 for x in items:o=mul(o,x)
 return o
e=[]
for k in range(1,5):
 o={}
 for v in itertools.combinations(U,k):o=add(o,prod(v))
 e.append(o)
f1,f2,f3,f4=e
A=sum_p(f2,scale(f1,-4),const(Q(74,9)))
B=sum_p(f3,scale(f2,-4),scale(f1,Q(74,9)),const(Q(-28,3)))
h0=sum_p(f4,scale(f2,Q(-70,9)),scale(f1,Q(212,9)),const(Q(-1007,27)))
h1=sum_p(f3,scale(f1,Q(-70,9)),const(Q(212,9)))
P=scale(sub(mul(A,A),mul(sub(f1,const(4)),B)),81)
H=scale(sub(mul(h0,A),mul(h1,B)),-243)
assert all(x.denominator==1 for x in list(P.values())+list(H.values()))
def digest(poly):
 rows=[[list(k),str(int(c))]for k,c in sorted(poly.items())]
 return hashlib.sha256(json.dumps(rows,separators=(',',':')).encode()).hexdigest()
assert digest(P)==C['Q_coefficients_sha256'] and digest(H)==C['H_coefficients_sha256']
assert len(P)==168 and len(H)==435

def grid(poly):
 m=3;stride=[m**(n-1-i)for i in range(n)];common=2**n;arr=[0]*(m**n)
 for key,val in poly.items():
  div=math.prod(math.comb(2,key[j])for j in range(n));assert common%div==0
  arr[sum(key[j]*stride[j]for j in range(n))]=int(val)*(common//div)
 return arr,m,stride

def split(arr,m,stride,axis):
 L=[0]*len(arr);R=[0]*len(arr);d=m-1;other=[j for j in range(n)if j!=axis]
 for coord in itertools.product(range(m),repeat=n-1):
  base=sum(coord[k]*stride[other[k]]for k in range(n-1));idx=[base+j*stride[axis]for j in range(m)]
  levels=[[arr[i]for i in idx]]
  while len(levels[-1])>1:levels.append([x+y for x,y in zip(levels[-1],levels[-1][1:])])
  for k in range(m):L[idx[k]]=levels[k][0]*(1<<(d-k));R[idx[k]]=levels[d-k][-1]*(1<<k)
 return L,R

def cover(poly,leaves):
 leaves=set(leaves);prefixes={p[:j]for p in leaves for j in range(len(p)+1)};seen=set();arr,m,stride=grid(poly)
 def walk(path,A,bounds):
  depth=len(path)
  if path in leaves:
   seen.add(path);assert depth>=n and min(A)>=0
   interior=0
   for corner in itertools.product((0,1),repeat=n):
    coords=[bounds[j][corner[j]]for j in range(n)]
    if all(0<x<1 for x in coords):
     interior+=1;idx=sum((0 if corner[j]==0 else m-1)*stride[j]for j in range(n));assert A[idx]>0
   assert interior>0;return
  assert path+'0'in prefixes and path+'1'in prefixes
  axis=depth%n;L,R=split(A,m,stride,axis);lo,hi=bounds[axis];mid=(lo+hi)/2
  a=list(bounds);a[axis]=(lo,mid);walk(path+'0',L,tuple(a))
  b=list(bounds);b[axis]=(mid,hi);walk(path+'1',R,tuple(b))
 walk('',arr,tuple((Q(0),Q(1))for _ in range(n)));assert seen==leaves
 return len(seen)
np=cover(P,C['Q_positive_compactified_binary_leaf_paths']);nh=cover(H,C['H_positive_compactified_binary_leaf_paths'])
assert (np,nh)==(5332,5334)
print('Independent stdlib integer PASS: all 168/435 coefficients and 5332/5334 exact six-dimensional Bernstein leaves')
