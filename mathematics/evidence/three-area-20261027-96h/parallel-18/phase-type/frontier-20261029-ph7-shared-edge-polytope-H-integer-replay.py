#!/usr/bin/env python3
"""Independent stdlib reconstruction/replay of shared-edge H dual covers."""
import hashlib,itertools,json,math,time
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).resolve().parent
C=json.loads((ROOT/'frontier-20261029-ph7-shared-edge-polytope-H-certificate-v1.json').read_text());n=7;zero=(0,)*n

def clean(a):return {k:v for k,v in a.items()if v}
def const(x):return {zero:F(x)}if x else{}
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
   z=tuple(k[i]+l[i]for i in range(n));out[z]=out.get(z,F(0))+x*y
 return clean(out)
def total(*seq):
 out={}
 for v in seq:out=add(out,v)
 return out
def prod(seq):
 out=const(1)
 for v in seq:out=mul(out,v)
 return out
def var(i):return {tuple(int(j==i)for j in range(n)):F(1)}
U=[var(i)for i in range(6)];t=var(6);one=const(1)
f=[]
for k in range(1,5):
 out={}
 for s in itertools.combinations(U,k):out=add(out,prod(s))
 f.append(out)
f1,f2,f3,f4=f;A=total(f2,scale(f1,-4),const(F(74,9)));B0=total(f3,scale(f2,-4),scale(f1,F(74,9)),const(F(-28,3)))
h0base=total(f4,scale(f2,F(-70,9)),scale(f1,F(212,9)),const(F(-1007,27)));h1base=total(f3,scale(f1,F(-70,9)),const(F(212,9)))
PA=prod(U[:3]);PB=prod(U[3:]);PC=prod([U[0],U[1],U[3]]);T=total(U[2],U[4],U[5]);neg_t=sub(one,t)

def H(W1,W2,W3):
 B=sub(sub(B0,W1),W2);h0=sub(sub(h0base,mul(W1,total(*U[3:]))),mul(W2,total(*U[:3])));h1=sub(sub(h1base,W1),W2)
 return scale(add(mul(A,sub(h0,mul(W3,T))),mul(sub(W3,B),sub(h1,W3))),-243)

def bytheta(p):
 out=[{}for _ in range(3)]
 for key,v in p.items():assert key[-1]<=2;out[key[-1]][key[:-1]]=v
 return out
def add6(a,b):
 out=a.copy()
 for k,v in b.items():out[k]=out.get(k,F(0))+v
 return clean(out)
def scale6(a,c):return clean({k:v*F(c)for k,v in a.items()})
def mul6(a,b):
 out={}
 for k,x in a.items():
  for l,y in b.items():
   z=tuple(k[i]+l[i]for i in range(6));out[z]=out.get(z,F(0))+x*y
 return clean(out)
forms={'AC':(mul(neg_t,PA),{},mul(t,PC)),'BC':({},mul(neg_t,PB),mul(t,PC)),
       'ABC':(mul(neg_t,PA),mul(neg_t,PB),mul(t,PC))};polys={}
for name,weights in forms.items():
 h=bytheta(H(*weights));h0=h[0];mid=add6(scale6(h[0],2),h[1]);h2=add6(add6(h[0],h[1]),h[2]);gram=add6(scale6(mul6(h0,h2),4),scale6(mul6(mid,mid),-1));polys[name+'_mid']=mid;polys[name+'_gram']=gram

def digest(p):
 assert all(c.denominator==1 for c in p.values());rows=[[list(k),str(int(c))]for k,c in sorted(p.items())]
 return hashlib.sha256(json.dumps(rows,separators=(',',':')).encode()).hexdigest()
for name,rec in C['records'].items():
 p=polys[name];assert len(p)==rec['terms'] and digest(p)==rec['sha256'];assert rec['degrees']==([2]*6 if name.endswith('_mid')else[4]*6)

def grid(p,degree):
 m=degree+1;stride=[m**(5-i)for i in range(6)];sc=math.lcm(*(math.comb(degree,j)for j in range(m)))**6;a=[0]*(m**6)
 for key,c in p.items():
  div=math.prod(math.comb(degree,k)for k in key);assert sc%div==0;a[sum(key[i]*stride[i]for i in range(6))]=int(c)*(sc//div)
 return a,m,stride

def split(a,m,stride,axis):
 L=[0]*len(a);R=[0]*len(a);d=m-1;other=[j for j in range(6)if j!=axis]
 for coord in itertools.product(range(m),repeat=5):
  base=sum(coord[k]*stride[other[k]]for k in range(5));idx=[base+j*stride[axis]for j in range(m)];lev=[[a[i]for i in idx]]
  while len(lev[-1])>1:lev.append([x+y for x,y in zip(lev[-1],lev[-1][1:])])
  for k in range(m):L[idx[k]]=lev[k][0]*(1<<(d-k));R[idx[k]]=lev[d-k][-1]*(1<<k)
 return L,R

def vertex(a,m,stride,bounds):
 found=False
 for corner in itertools.product((0,1),repeat=6):
  xyz=[bounds[j][corner[j]]for j in range(6)]
  if all(0<x<1 for x in xyz):
   found=True;idx=sum((0 if corner[j]==0 else m-1)*stride[j]for j in range(6))
   if a[idx]<=0:return False
 return found

def cover(name,pospaths,grampaths):
 assert len(pospaths)==len(set(pospaths))and len(grampaths)==len(set(grampaths));pos=set(pospaths);gram=set(grampaths);assert not(pos&gram)
 leaves=pos|gram;prefix={p[:j]for p in leaves for j in range(len(p)+1)};gp={p[:j]for p in gram for j in range(len(p)+1)};seen=set()
 a,ma,sa=grid(polys[name+'_mid'],2);b,mb,sb=grid(polys[name+'_gram'],4)
 def walk(path,A,B,bounds):
  dep=len(path)
  if path in pos:seen.add(path);assert A is not None and min(A)>=0;return
  if path in gram:seen.add(path);assert B is not None and dep>=6 and min(B)>=0 and vertex(B,mb,sb,bounds);return
  assert path+'0'in prefix and path+'1'in prefix;ax=dep%6;lo,hi=bounds[ax];mid=(lo+hi)/2
  AL,AR=split(A,ma,sa,ax)if A is not None else(None,None)
  BL,BR=split(B,mb,sb,ax)if B is not None and (path+'0'in gp or path+'1'in gp)else(None,None)
  for bit,a,b,inter in [('0',AL,BL,(lo,mid)),('1',AR,BR,(mid,hi))]:
   z=list(bounds);z[ax]=inter;walk(path+bit,a,b if path+bit in gp else None,tuple(z))
 walk('',a,b,tuple((F(0),F(1))for _ in range(6)));assert seen==leaves
 return len(pos),len(gram)

expected={'AC':(2649,210),'BC':(2815,576),'ABC':(2916,589)};start=time.monotonic()
for rec in C['covers']:
 counts=cover(rec['name'],rec['mid_nonnegative'],rec['gram_strict']);assert counts==expected[rec['name']];print(rec['name'],'checked mid/strict Gram',*counts,flush=True)
print('PASS: independent Fraction reconstruction, coefficient hashes, complete 3 dual trees, strict interior checks')
print('elapsed_seconds',time.monotonic()-start)
