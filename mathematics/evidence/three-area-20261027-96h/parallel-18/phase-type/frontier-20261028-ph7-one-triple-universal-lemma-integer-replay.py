#!/usr/bin/env python3
"""Independent stdlib integer replay of universal one-triple Q/H lemma."""
import hashlib,itertools,json,math,time
from fractions import Fraction as Q
from pathlib import Path
ROOT=Path(__file__).resolve().parent
C=json.loads((ROOT/'frontier-20261028-ph7-one-triple-universal-lemma-certificate.json').read_text())
n=7;zero=(0,)*n

def clean(a):return {k:v for k,v in a.items()if v}
def const(x):return {zero:Q(x)}if x else{}
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
def sump(*a):
 o={}
 for x in a:o=add(o,x)
 return o
U=[]
for i in range(6):
 e=[0]*n;e[i]=1;U.append({tuple(e):Q(1)})
th={(0,0,0,0,0,0,1):Q(1)}
def prod(a):
 o=const(1)
 for x in a:o=mul(o,x)
 return o
es=[]
for k in range(1,5):
 o={}
 for x in itertools.combinations(U,k):o=add(o,prod(x))
 es.append(o)
f1,f2,f3,f4=es;w=mul(th,prod(U[:3]));O=sump(*U[3:])
A=sump(f2,scale(f1,-4),const(Q(74,9)))
B=sump(f3,scale(f2,-4),scale(f1,Q(74,9)),const(Q(-28,3)),scale(w,-1))
h0=sump(f4,scale(f2,Q(-70,9)),scale(f1,Q(212,9)),const(Q(-1007,27)),scale(mul(w,O),-1))
h1=sump(f3,scale(f1,Q(-70,9)),const(Q(212,9)),scale(w,-1))
QQ=scale(sub(mul(A,A),mul(sub(f1,const(4)),B)),81)
HH=scale(sub(mul(h0,A),mul(h1,B)),-243)

def bytheta(poly,degree):
 out=[{}for _ in range(degree+1)]
 for key,val in poly.items():assert key[-1]<=degree;out[key[-1]][key[:-1]]=val
 return out
def add6(a,b):
 o=a.copy()
 for k,v in b.items():o[k]=o.get(k,Q(0))+v
 return clean(o)
def scale6(a,c):return clean({k:v*Q(c)for k,v in a.items()})
qc=bytheta(QQ,1);hc=bytheta(HH,2)
Q0=qc[0];Q1=add6(qc[0],qc[1]);H0=hc[0];H1=add6(scale6(hc[0],2),hc[1]);H2=add6(add6(hc[0],hc[1]),hc[2])
def mul6(a,b):
 out={}
 for k,x in a.items():
  for l,y in b.items():
   key=tuple(k[i]+l[i]for i in range(6));out[key]=out.get(key,Q(0))+x*y
 return clean(out)
Gram=add6(scale6(mul6(H0,H2),4),scale6(mul6(H1,H1),-1))
polys={'Q0':Q0,'Q1':Q1,'H0':H0,'H2':H2,'H1_twice':H1,'Gram4':Gram}

def digest(poly):
 assert all(x.denominator==1 for x in poly.values())
 rows=[[list(k),str(int(c))]for k,c in sorted(poly.items())]
 return hashlib.sha256(json.dumps(rows,separators=(',',':')).encode()).hexdigest()
for rec in C['records']:
 p=polys[rec['name']];assert len(p)==rec['coefficient_terms'] and digest(p)==rec['coefficient_sha256']

def grid(poly,degree):
 n=6;m=degree+1;stride=[m**(n-1-i)for i in range(n)];common=math.lcm(*[math.comb(degree,i)for i in range(m)])**n;arr=[0]*(m**n)
 for key,val in poly.items():
  div=math.prod(math.comb(degree,key[j])for j in range(n));assert common%div==0
  arr[sum(key[j]*stride[j]for j in range(n))]=int(val)*(common//div)
 return arr,m,stride

def split(arr,m,stride,axis):
 n=6;L=[0]*len(arr);R=[0]*len(arr);d=m-1;other=[j for j in range(n)if j!=axis]
 for coord in itertools.product(range(m),repeat=n-1):
  base=sum(coord[k]*stride[other[k]]for k in range(n-1));idx=[base+j*stride[axis]for j in range(m)]
  levels=[[arr[i]for i in idx]]
  while len(levels[-1])>1:levels.append([x+y for x,y in zip(levels[-1],levels[-1][1:])])
  for k in range(m):L[idx[k]]=levels[k][0]*(1<<(d-k));R[idx[k]]=levels[d-k][-1]*(1<<k)
 return L,R

def vertex(A,m,stride,bounds):
 inside=0
 for corner in itertools.product((0,1),repeat=6):
  coord=[bounds[j][corner[j]]for j in range(6)]
  if all(0<coord[j]<1 for j in range(3)) and all(coord[j]<1 for j in range(3,6)):
   inside+=1;idx=sum((0 if corner[j]==0 else m-1)*stride[j]for j in range(6));
   if A[idx]<=0:return False
 return inside>0

def single(poly,degree,leaves):
 leaves=set(leaves);prefix={p[:j]for p in leaves for j in range(len(p)+1)};seen=set();arr,m,stride=grid(poly,degree)
 def walk(path,A,bounds):
  dep=len(path)
  if path in leaves:seen.add(path);assert dep>=6 and min(A)>=0 and vertex(A,m,stride,bounds);return
  assert path+'0'in prefix and path+'1'in prefix;axis=dep%6;L,R=split(A,m,stride,axis);lo,hi=bounds[axis];mid=(lo+hi)/2
  x=list(bounds);x[axis]=(lo,mid);walk(path+'0',L,tuple(x));x=list(bounds);x[axis]=(mid,hi);walk(path+'1',R,tuple(x))
 walk('',arr,tuple((Q(0),Q(1))for _ in range(6)));assert seen==leaves
 return len(seen)

def dual():
 pos=set(C['dual_H1_nonnegative_leaf_paths']);gram=set(C['dual_Gram_positive_leaf_paths']);assert not(pos&gram)
 leaves=pos|gram;prefix={p[:j]for p in leaves for j in range(len(p)+1)};gprefix={p[:j]for p in gram for j in range(len(p)+1)};seen=set()
 h,mh,sh=grid(H1,2);g,mg,sg=grid(Gram,4)
 def walk(path,H,G,bounds):
  dep=len(path)
  if path in pos:seen.add(path);assert H is not None and min(H)>=0;return
  if path in gram:seen.add(path);assert dep>=6 and G is not None and min(G)>=0 and vertex(G,mg,sg,bounds);return
  assert path+'0'in prefix and path+'1'in prefix;axis=dep%6;lo,hi=bounds[axis];mid=(lo+hi)/2
  HL,HR=split(H,mh,sh,axis)if H is not None else(None,None)
  if G is not None and (path+'0'in gprefix or path+'1'in gprefix):GL,GR=split(G,mg,sg,axis)
  else:GL=GR=None
  for bit,hh,gg,interval in [('0',HL,GL,(lo,mid)),('1',HR,GR,(mid,hi))]:
   x=list(bounds);x[axis]=interval;walk(path+bit,hh,gg if path+bit in gprefix else None,tuple(x))
 walk('',h,g,tuple((Q(0),Q(1))for _ in range(6)));assert seen==leaves
 return len(pos),len(gram)

start=time.monotonic();counts=[]
for rec in C['records'][:4]:
 name=rec['name'];counts.append(single(polys[name],2,rec['positive_leaf_paths']));print(name,'checked',counts[-1],flush=True)
assert counts==[5332,1869,5334,2443];dc=dual();assert dc==(2714,199)
print('Independent stdlib integer PASS: 6 exact polynomials, 14978 positive leaves and 2913 complete copositive leaves')
print('elapsed_seconds',time.monotonic()-start)
