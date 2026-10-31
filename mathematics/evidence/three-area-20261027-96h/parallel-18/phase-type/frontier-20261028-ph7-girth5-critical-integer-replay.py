#!/usr/bin/env python3
"""Independent stdlib integer replay of five-rate girth>=5 obstruction."""
import hashlib,itertools,json,math
from fractions import Fraction as Q
from pathlib import Path
ROOT=Path(__file__).resolve().parent
C=json.loads((ROOT/'frontier-20261028-ph7-girth5-critical-bernstein-certificate.json').read_text())
zero=(0,)*5

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
   key=tuple(k[i]+l[i]for i in range(5));o[key]=o.get(key,Q(0))+x*y
 return clean(o)
def sum_p(*a):
 o={}
 for v in a:o=add(o,v)
 return o
U=[]
for i in range(5):
 e=[0]*5;e[i]=1;U.append({tuple(e):Q(1)})
def prod(items):
 o=const(1)
 for x in items:o=mul(o,x)
 return o
e=[]
for k in range(1,5):
 o={}
 for v in itertools.combinations(U,k):o=add(o,prod(v))
 e.append(o)
e1,e2,e3,e4=e

def equations(t,r):
 p=add(e1,const(t-4));q=sum_p(e2,scale(e1,t),const(r),scale(p,-4),const(Q(-70,9)))
 F4=sum_p(e3,scale(e2,t),scale(e1,r),scale(q,-4),scale(p,Q(-70,9)),const(Q(-68,9)))
 F3=sum_p(e4,scale(e3,t),scale(e2,r),scale(q,Q(-70,9)),scale(p,Q(-68,9)),const(Q(-289,81)))
 return F4,F3

b=equations(0,0);it=equations(1,0);ir=equations(0,1)
a00,a10=sub(it[0],b[0]),sub(it[1],b[1]);a01,a11=sub(ir[0],b[0]),sub(ir[1],b[1])
assert equations(2,0)==tuple(add(b[i],scale(sub(it[i],b[i]),2))for i in range(2))
assert equations(0,2)==tuple(add(b[i],scale(sub(ir[i],b[i]),2))for i in range(2))
assert equations(1,1)==tuple(add(it[i],sub(ir[i],b[i]))for i in range(2))
den=sub(mul(a00,a11),mul(a01,a10));tn=add(scale(mul(b[0],a11),-1),mul(a01,b[1]));rn=add(scale(mul(a00,b[1]),-1),mul(b[0],a10))
D=scale(den,81);N=scale(sub(mul(tn,tn),scale(mul(rn,den),4)),-19683)
assert all(x.denominator==1 for x in list(D.values())+list(N.values()))
def digest(P):
 rows=[[list(k),str(int(c))]for k,c in sorted(P.items())]
 return hashlib.sha256(json.dumps(rows,separators=(',',':')).encode()).hexdigest()
assert digest(D)==C['D_coefficients_sha256'] and digest(N)==C['N_coefficients_sha256']
assert len(D)==96 and len(N)==1753

def grid(P,degree):
 m=degree+1;total=m**5;common=math.lcm(*[math.comb(degree,i)for i in range(m)])**5
 A=[0]*total;stride=[m**(4-i)for i in range(5)]
 for key,val in P.items():
  div=math.prod(math.comb(degree,key[j])for j in range(5));assert common%div==0
  A[sum(key[j]*stride[j]for j in range(5))]=int(val)*(common//div)
 return A,m,stride

def split(A,m,stride,axis):
 L=[0]*len(A);R=[0]*len(A);d=m-1;other=[j for j in range(5)if j!=axis]
 for coord in itertools.product(range(m),repeat=4):
  base=sum(coord[k]*stride[other[k]]for k in range(4));idx=[base+j*stride[axis]for j in range(m)]
  levels=[[A[i]for i in idx]]
  while len(levels[-1])>1:levels.append([x+y for x,y in zip(levels[-1],levels[-1][1:])])
  for k in range(m):L[idx[k]]=levels[k][0]*(1<<(d-k));R[idx[k]]=levels[d-k][-1]*(1<<k)
 return L,R

def cover(P,degree,paths):
 paths=set(paths);seen=set();A,m,stride=grid(P,degree)
 def walk(path,arr,bounds):
  depth=len(path)
  if path in paths:
   seen.add(path);assert depth>=5 and min(arr)>=0
   interior=0
   for corners in itertools.product((0,1),repeat=5):
    coords=[bounds[j][corners[j]]for j in range(5)]
    if all(0<x<1 for x in coords):
     interior+=1;idx=sum((0 if corners[j]==0 else m-1)*stride[j]for j in range(5));assert arr[idx]>0
   assert interior>0
   return
  assert any(x.startswith(path)for x in paths),path
  axis=depth%5;L,R=split(arr,m,stride,axis);lo,hi=bounds[axis];mid=(lo+hi)/2
  a=list(bounds);a[axis]=(lo,mid);walk(path+'0',L,tuple(a))
  b=list(bounds);b[axis]=(mid,hi);walk(path+'1',R,tuple(b))
 walk('',A,tuple((Q(0),Q(1))for _ in range(5)));assert seen==paths
 return len(seen)
nd=cover(D,2,C['D_positive_compactified_binary_leaf_paths']);nn=cover(N,4,C['N_positive_compactified_binary_leaf_paths'])
assert (nd,nn)==(513,657)
print('Independent stdlib integer PASS: all 96/1753 polynomial coefficients and 513/657 exact Bernstein leaves')
