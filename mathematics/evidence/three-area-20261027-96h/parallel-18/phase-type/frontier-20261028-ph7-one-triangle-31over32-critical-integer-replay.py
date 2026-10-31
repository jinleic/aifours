#!/usr/bin/env python3
"""Independent stdlib exact 5D Bernstein replay for theta<=31/32."""
import hashlib,itertools,json,math
from fractions import Fraction as Q
from pathlib import Path
ROOT=Path(__file__).resolve().parent
C=json.loads((ROOT/'frontier-20261028-ph7-one-triangle-31over32-critical-certificate.json').read_text())
N=6;zero=(0,)*N

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
   key=tuple(k[i]+l[i]for i in range(N));o[key]=o.get(key,Q(0))+x*y
 return clean(o)
def sum_p(*a):
 o={}
 for v in a:o=add(o,v)
 return o
U=[]
for i in range(5):
 e=[0]*N;e[i]=1;U.append({tuple(e):Q(1)})
theta={(0,0,0,0,0,1):Q(1)}
def prod(items):
 o=const(1)
 for x in items:o=mul(o,x)
 return o
e=[]
for k in range(1,5):
 o={}
 for x in itertools.combinations(U,k):o=add(o,prod(x))
 e.append(o)
e1,e2,e3,e4=e;W=mul(theta,prod(U[:3]));O=add(U[3],U[4])

def equations(t,r):
 p=add(e1,const(t-4));q=sum_p(e2,scale(e1,t),const(r),scale(p,-4),const(Q(-70,9)))
 F4=sum_p(e3,scale(e2,t),scale(e1,r),scale(W,-1),scale(q,-4),scale(p,Q(-70,9)),const(Q(-68,9)))
 F3=sum_p(e4,scale(e3,t),scale(e2,r),scale(mul(W,add(O,const(t))),-1),scale(q,Q(-70,9)),scale(p,Q(-68,9)),const(Q(-289,81)))
 return F4,F3

b=equations(0,0);it=equations(1,0);ir=equations(0,1)
a00,a10=sub(it[0],b[0]),sub(it[1],b[1]);a01,a11=sub(ir[0],b[0]),sub(ir[1],b[1])
assert equations(1,1)==tuple(add(it[i],sub(ir[i],b[i]))for i in range(2))
den=sub(mul(a00,a11),mul(a01,a10));tn=add(scale(mul(b[0],a11),-1),mul(a01,b[1]));rn=add(scale(mul(a00,b[1]),-1),mul(b[0],a10))
poly=scale(sub(mul(tn,tn),scale(mul(rn,den),4)),-19683);assert all(key[-1]<=3 for key in poly)
coef=[{}for _ in range(4)]
for key,val in poly.items():coef[key[-1]][key[:-1]]=val

def add5(a,b):
 o=a.copy()
 for k,x in b.items():o[k]=o.get(k,Q(0))+x
 return clean(o)
def scale5(a,c):return clean({k:x*Q(c)for k,x in a.items()})
bs=[]
for k in range(4):
 q={}
 for j in range(k+1):q=add5(q,scale5(coef[j],Q(math.comb(k,j),math.comb(3,j))))
 bs.append(q)
def split_theta(row):
 levels=[row]
 while len(levels[-1])>1:levels.append([scale5(add5(x,y),Q(1,2))for x,y in zip(levels[-1],levels[-1][1:])])
 return [x[0]for x in levels],[x[-1]for x in levels][::-1]
def digest(poly):
 assert all(c.denominator==1 for c in poly.values())
 rows=[[list(k),str(int(c))]for k,c in sorted(poly.items())]
 return hashlib.sha256(json.dumps(rows,separators=(',',':')).encode()).hexdigest()
def grid(poly):
 n=5;m=5;stride=[m**(n-1-i)for i in range(n)];common=12**n;arr=[0]*(m**n)
 for key,val in poly.items():
  div=math.prod(math.comb(4,key[j])for j in range(n));assert common%div==0
  arr[sum(key[j]*stride[j]for j in range(n))]=int(val)*(common//div)
 return arr,m,stride

def split(arr,m,stride,axis):
 n=5;L=[0]*len(arr);R=[0]*len(arr);d=m-1;other=[j for j in range(n)if j!=axis]
 for coord in itertools.product(range(m),repeat=n-1):
  base=sum(coord[k]*stride[other[k]]for k in range(n-1));idx=[base+j*stride[axis]for j in range(m)]
  levels=[[arr[i]for i in idx]]
  while len(levels[-1])>1:levels.append([x+y for x,y in zip(levels[-1],levels[-1][1:])])
  for k in range(m):L[idx[k]]=levels[k][0]*(1<<(d-k));R[idx[k]]=levels[d-k][-1]*(1<<k)
 return L,R

def cover(poly,leaves):
 n=5;leaves=set(leaves);prefixes={p[:j]for p in leaves for j in range(len(p)+1)};seen=set();arr,m,stride=grid(poly)
 def walk(path,A,bounds):
  dep=len(path)
  if path in leaves:
   seen.add(path);assert dep>=n and min(A)>=0;inside=0
   for corner in itertools.product((0,1),repeat=n):
    coord=[bounds[j][corner[j]]for j in range(n)]
    if all(0<x<1 for x in coord):
     inside+=1;idx=sum((0 if corner[j]==0 else m-1)*stride[j]for j in range(n));assert A[idx]>0
   assert inside>0;return
  assert path+'0'in prefixes and path+'1'in prefixes
  axis=dep%n;L,R=split(A,m,stride,axis);lo,hi=bounds[axis];mid=(lo+hi)/2
  a=list(bounds);a[axis]=(lo,mid);walk(path+'0',L,tuple(a))
  b=list(bounds);b[axis]=(mid,hi);walk(path+'1',R,tuple(b))
 walk('',arr,tuple((Q(0),Q(1))for _ in range(n)));assert seen==leaves
 return len(seen)
records={(r['stage'],r['bernstein_index']):r for r in C['records']};assert len(records)==16
current=bs;total=0
for stage in range(1,6):
 left,current=split_theta(current)
 for j,p in enumerate(left):
  if stage>1 and j==0:continue
  rec=records[(stage,j)];p=scale5(p,rec['positive_scale']);assert digest(p)==rec['coefficient_sha256'];assert len(p)==rec['coefficient_terms']
  total+=cover(p,rec['positive_leaf_paths']);print('stage',stage,'index',j,'checked',flush=True)
print('Independent stdlib integer PASS: all 16 triangle-rate polynomials and',total,'exact Bernstein leaves')
