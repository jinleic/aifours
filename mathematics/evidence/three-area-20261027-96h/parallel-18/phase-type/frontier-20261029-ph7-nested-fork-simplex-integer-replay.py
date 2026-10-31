#!/usr/bin/env python3
"""Independent stdlib exact reconstruction/replay of nested-fork selectors.

Pass part 0,1 or 2. Each invocation reconstructs all six-rate polynomials,
checks all pinned hashes, and fully replays that part's selector-prefix trees.
"""
import hashlib,itertools,json,math,sys,time
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).resolve().parent
assert len(sys.argv)==2 and sys.argv[1] in ('0','1','2');part=int(sys.argv[1])
C=json.loads((ROOT/f'frontier-20261029-ph7-nested-fork-simplex-certificate-part{part}-v1.json').read_text())
n=6;zero=(0,)*n

def clean(a):return {k:v for k,v in a.items()if v}
def const(x):return {zero:F(x)}if x else{}
def add(a,b):
 o=a.copy()
 for k,v in b.items():o[k]=o.get(k,F(0))+v
 return clean(o)
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
U=[var(i)for i in range(6)];f=[]
for k in range(1,5):
 out={}
 for z in itertools.combinations(U,k):out=add(out,prod(z))
 f.append(out)
f1,f2,f3,f4=f;A=total(f2,scale(f1,-4),const(F(74,9)));B0=total(f3,scale(f2,-4),scale(f1,F(74,9)),const(F(-28,3)))
h0base=total(f4,scale(f2,F(-70,9)),scale(f1,F(212,9)),const(F(-1007,27)));h1base=total(f3,scale(f1,F(-70,9)),const(F(212,9)))
PA=prod(U[:3]);PB=prod(U[3:]);PC=prod([U[0],U[3],U[4]]);PD=prod([U[0],U[3]]);Tout=total(U[1],U[2],U[4],U[5]);weights=(PA,PB,PC,PD)
vertices=[(1,0,0,0),(1,1,0,0),(0,0,0,1),(0,1,0,0),(0,0,1,0)]

def H(w):
 W1,W2,W3,K=w;B=sub(sub(sub(B0,W1),W2),W3);h0=sub(sub(sub(h0base,mul(W1,total(*U[3:]))),mul(W2,total(*U[:3]))),mul(W3,total(U[1],U[2],U[5])));h1=sub(sub(sub(h1base,W1),W2),W3)
 return scale(sub(mul(h0,sub(A,K)),mul(sub(h1,mul(K,Tout)),B)),-243)
V=[[scale(p,c)for p,c in zip(weights,v)]for v in vertices];D=[H(w)for w in V];O={}
for i,j in itertools.combinations(range(5),2):
 mid=[scale(add(a,b),F(1,2))for a,b in zip(V[i],V[j])];O[i,j]=sub(scale(H(mid),4),add(D[i],D[j]))
polys={'O'+str(i)+str(j):p for (i,j),p in O.items()};polys['G23']=sub(scale(mul(D[2],D[3]),4),mul(O[2,3],O[2,3]))
faces=[(0,1,2),(0,2,3),(0,2,4),(1,2,3),(1,2,4),(2,3,4)];forbid={(0,1,2):(0,1),(0,2,3):(0,2),(1,2,3):(1,2)}
expected=[('O24',['O24'],[False]),('edge23',['O23','G23'],[False,True])]
for face in faces:
 pairs=list(itertools.combinations(face,2))
 if 4 not in face:
  ii,jj=forbid[face];names=['O'+str(i)+str(j)for i,j in (pairs[ii],pairs[jj])];expected.append((str(face)+'_OR',names,[False,False]))
 for i,j in itertools.combinations(range(3),2):
  if (4 in face and (2,4)in(pairs[i],pairs[j]))or(4 not in face and(i,j)==forbid[face]):continue
  common=next(iter(set(pairs[i])&set(pairs[j])));others=sorted(set(face)-{common});opp=tuple(others);name='C'+''.join(map(str,face))+str(i)+str(j)
  polys[name]=sub(scale(mul(O[opp],D[common]),2),mul(O[pairs[i]],O[pairs[j]]));names=['O'+str(a)+str(b)for a,b in(pairs[i],pairs[j])]+[name]
  expected.append((str(face)+'_C'+str(i)+str(j),names,[False,False,False]))
assert len(expected)==14

def digest(p):
 assert all(v.denominator==1 for v in p.values());rows=[[list(k),str(int(v))]for k,v in sorted(p.items())]
 return hashlib.sha256(json.dumps(rows,separators=(',',':')).encode()).hexdigest()
assert set(C['records'])==set(polys)
for name,rec in C['records'].items():
 p=polys[name];assert len(p)==rec['terms'] and digest(p)==rec['sha256'];assert rec['degrees']==([2]*6 if name.startswith('O')else[4]*6)

def grid(p,degree):
 m=degree+1;stride=[m**(5-i)for i in range(6)];sc=math.lcm(*(math.comb(degree,j)for j in range(m)))**6;arr=[0]*(m**6)
 for key,c in p.items():
  div=math.prod(math.comb(degree,k)for k in key);assert sc%div==0;arr[sum(key[i]*stride[i]for i in range(6))]=int(c)*(sc//div)
 return arr,m,stride

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

def replay(rec):
 names,strict,paths=rec['names'],rec['strict'],rec['paths'];leaves=[set(p)for p in paths];assert all(len(a)==len(b)for a,b in zip(leaves,paths));union=set().union(*leaves);assert len(union)==sum(map(len,leaves))
 prefs=[{p[:j]for p in ls for j in range(len(p)+1)}for ls in leaves];prefix=set().union(*prefs);seen=set();initial=[grid(polys[n],2 if n.startswith('O')else 4)for n in names];dims=[(m,s)for _,m,s in initial]
 def walk(path,arr,bounds):
  dep=len(path)
  for i,ls in enumerate(leaves):
   if path in ls:
    seen.add(path);assert arr[i] is not None and min(arr[i])>=0
    if strict[i]:assert dep>=6 and vertex(arr[i],*dims[i],bounds)
    assert path+'0'not in prefix and path+'1'not in prefix;return
  assert path+'0'in prefix and path+'1'in prefix;ax=dep%6;lo,hi=bounds[ax];mid=(lo+hi)/2;parts=[]
  for i,a in enumerate(arr):
   if a is not None and (path+'0'in prefs[i]or path+'1'in prefs[i]):parts.append(split(a,*dims[i],ax))
   else:parts.append((None,None))
  for bit,j,inter in [('0',0,(lo,mid)),('1',1,(mid,hi))]:
   z=list(bounds);z[ax]=inter;child=path+bit;walk(child,[q[j]if child in prefs[i]else None for i,q in enumerate(parts)],tuple(z))
 walk('',[a for a,_,_ in initial],tuple((F(0),F(1))for _ in range(6)));assert seen==union
 return [len(ls)for ls in leaves]

start,end=[(0,5),(5,10),(10,14)][part];assert (C['part'],C['start'],C['end'])==(part,start,end);assert len(C['covers'])==end-start
clock=time.monotonic()
for rec,(label,names,strict)in zip(C['covers'],expected[start:end]):
 assert rec['label']==label and rec['names']==names and rec['strict']==strict
 print(label,'checked',replay(rec),flush=True)
print('PASS: independent Fraction reconstruction, coefficient hashes and complete selector trees part',part,'elapsed',time.monotonic()-clock)
