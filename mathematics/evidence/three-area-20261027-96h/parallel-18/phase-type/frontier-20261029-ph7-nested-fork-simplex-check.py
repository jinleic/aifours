#!/usr/bin/env python3
"""Exact six-rate selector covers for a four-triangle nested-fork simplex.

Records vertex/mid/Gram/cross polynomial hashes. Certifies O24>=0; the missing
D-B edge by nonnegative offdiag OR strictly positive Gram; and all sign/cross
selectors for six connector-containing 2D simplex faces. Other edge/vertex
positivity is imported by the accompanying written theorem.
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
u=S.symbols('u0:6',real=True);W1,W2,W3,K=S.symbols('W1 W2 W3 K',real=True)
f=[None]+[sum(S.prod(z)for z in combinations(u,k))for k in range(1,5)];f1,f2,f3,f4=f[1:]
A=f2-4*f1+S.Rational(74,9);B=f3-4*f2+S.Rational(74,9)*f1-S.Rational(28,3)-W1-W2-W3
h0=f4-S.Rational(70,9)*f2+S.Rational(212,9)*f1-S.Rational(1007,27)-W1*sum(u[3:])-W2*sum(u[:3])-W3*(u[1]+u[2]+u[5])
h1=f3-S.Rational(70,9)*f1+S.Rational(212,9)-W1-W2-W3;Tout=u[1]+u[2]+u[4]+u[5]
H=S.expand(-243*(h0*(A-K)-(h1-K*Tout)*B))
PA=S.prod(u[:3]);PB=S.prod(u[3:]);PC=u[0]*u[3]*u[4];PD=u[0]*u[3]
Vnorm=[(1,0,0,0),(1,1,0,0),(0,0,0,1),(0,1,0,0),(0,0,1,0)];prodv=(PA,PB,PC,PD)
vertices=[tuple(a*b for a,b in zip(v,prodv))for v in Vnorm];weights=(W1,W2,W3,K)
D=[S.Poly(S.expand(H.subs(dict(zip(weights,v)))),*u)for v in vertices];O={}
for i,j in combinations(range(5),2):
 mid=[(a+b)/2 for a,b in zip(vertices[i],vertices[j])]
 O[i,j]=S.Poly(S.expand(4*H.subs(dict(zip(weights,mid)))-D[i].as_expr()-D[j].as_expr()),*u)
G23=4*D[2]*D[3]-O[2,3]*O[2,3]
faces=[(0,1,2),(0,2,3),(0,2,4),(1,2,3),(1,2,4),(2,3,4)]
forbid={(0,1,2):(0,1),(0,2,3):(0,2),(1,2,3):(1,2)}
polys={'O'+str(i)+str(j):p for (i,j),p in O.items()};polys['G23']=G23;specs=[]
specs.append(('O24',['O24'],[False]));specs.append(('edge23',['O23','G23'],[False,True]))
for face in faces:
 pairs=list(combinations(face,2))
 if 4 not in face:
  ii,jj=forbid[face];names=['O'+str(i)+str(j)for i,j in (pairs[ii],pairs[jj])];specs.append((str(face)+'_OR',names,[False,False]))
 for i,j in combinations(range(3),2):
  if (4 in face and (2,4) in (pairs[i],pairs[j])) or (4 not in face and (i,j)==forbid[face]):continue
  common=next(iter(set(pairs[i])&set(pairs[j])));others=sorted(set(face)-{common});opp=tuple(others)
  cross=2*O[opp]*D[common]-O[pairs[i]]*O[pairs[j]];name='C'+''.join(map(str,face))+str(i)+str(j);polys[name]=cross
  names=['O'+str(a)+str(b)for a,b in (pairs[i],pairs[j])]+[name];specs.append((str(face)+'_C'+str(i)+str(j),names,[False,False,False]))
assert len(specs)==14 and all(c.q==1 for p in polys.values()for c in p.coeffs())

def digest(p):
 rows=[[list(k),str(int(c))]for k,c in sorted(p.as_dict().items())]
 return hashlib.sha256(json.dumps(rows,separators=(',',':')).encode()).hexdigest()
def grid(p):
 ds=p.degree_list();sc=1
 for d in ds:sc*=lcm(*(comb(d,i)for i in range(d+1)))
 arr=np.zeros(tuple(d+1 for d in ds),dtype=object)
 for key,c in p.as_dict().items():
  div=1
  for d,k in zip(ds,key):div*=comb(d,k)
  assert sc%div==0;arr[key]=int(c)*(sc//div)
 return arr
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
def cover(names,strict):
 stack=[('',[grid(polys[n])for n in names],tuple((F(0),F(1))for _ in range(6)))];paths=[[]for _ in names]
 while stack:
  path,arr,bounds=stack.pop();dep=len(path);choice=None
  for i,a in enumerate(arr):
   if min(a.flat)>=0 and (not strict[i] or (dep>=6 and vertex(a,bounds))):choice=i;break
  if choice is not None:paths[choice].append(path);continue
  assert dep<48,('depth limit',names,path)
  ax=dep%6;parts=[split(a,ax)for a in arr];lo,hi=bounds[ax];mid=(lo+hi)/2
  for bit,j,inter in [('1',1,(mid,hi)),('0',0,(lo,mid))]:
   z=list(bounds);z[ax]=inter;stack.append((path+bit,[p[j]for p in parts],tuple(z)))
 return [sorted(p)for p in paths]
assert len(sys.argv)==2 and sys.argv[1] in ('0','1','2')
part=int(sys.argv[1]);start,end=[(0,5),(5,10),(10,14)][part]
records={n:{'degrees':list(p.degree_list()),'terms':len(p.terms()),'sha256':digest(p)}for n,p in polys.items()};covers=[]
for label,names,strict in specs[start:end]:
 paths=cover(names,strict);covers.append({'label':label,'names':names,'strict':strict,'paths':paths});print(label,'leaves',[len(p)for p in paths],flush=True)
out=ROOT/f'frontier-20261029-ph7-nested-fork-simplex-certificate-part{part}-v1.json'
out.write_text(json.dumps({'domain':'six strictly positive finite rates','compactification':'u_i=s_i/(1-s_i)',
 'axis':'path depth modulo six','part':part,'start':start,'end':end,'records':records,'covers':covers},indent=2)+'\n')
print('PASS: nested-fork exact selector batch saved',out)
