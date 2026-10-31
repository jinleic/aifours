#!/usr/bin/env python3
"""Exact six-rate dual Bernstein certificates for shared-edge weight polytope.

For each of three edges AC, BC, ABC, prove the middle coefficient >=0 OR the
quadratic Gram determinant >0, with all six rates strictly positive. Endpoint
positivity is supplied by separately pinned one/two-triangle universal lemmas.
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
u=S.symbols('u0:6',real=True);w1,w2,w3,t=S.symbols('w1 w2 w3 t',real=True)
f=[None]+[sum(S.prod(q)for q in combinations(u,k))for k in range(1,5)];f1,f2,f3,f4=f[1:]
A=f2-4*f1+S.Rational(74,9);B=f3-4*f2+S.Rational(74,9)*f1-S.Rational(28,3)-w1-w2
h0=f4-S.Rational(70,9)*f2+S.Rational(212,9)*f1-S.Rational(1007,27)-w1*sum(u[3:])-w2*sum(u[:3])
h1=f3-S.Rational(70,9)*f1+S.Rational(212,9)-w1-w2;T=u[2]+u[4]+u[5]
H=S.expand(-243*(A*(h0-w3*T)+(w3-B)*(h1-w3)))
PA=S.prod(u[:3]);PB=S.prod(u[3:]);PC=u[0]*u[1]*u[3]
subs={'AC':{w1:(1-t)*PA,w2:0,w3:t*PC},'BC':{w1:0,w2:(1-t)*PB,w3:t*PC},
      'ABC':{w1:(1-t)*PA,w2:(1-t)*PB,w3:t*PC}}
polys={}
for name,sub in subs.items():
 p=S.Poly(S.expand(H.subs(sub)),t);assert p.degree()==2
 h=[S.Poly(S.expand(sum(p.nth(j)*S.Rational(comb(k,j),comb(2,j))for j in range(k+1))),*u)for k in range(3)]
 mid=2*h[1];gram=4*h[0]*h[2]-mid*mid
 polys[name+'_mid']=mid;polys[name+'_gram']=gram
assert all(c.q==1 for p in polys.values()for c in p.coeffs())

def digest(p):
 rows=[[list(k),str(int(c))]for k,c in sorted(p.as_dict().items())]
 return hashlib.sha256(json.dumps(rows,separators=(',',':')).encode()).hexdigest()
def grid(p):
 ds=p.degree_list();sc=1
 for d in ds:sc*=lcm(*(comb(d,i)for i in range(d+1)))
 a=np.zeros(tuple(d+1 for d in ds),dtype=object)
 for key,c in p.as_dict().items():
  div=1
  for d,k in zip(ds,key):div*=comb(d,k)
  assert sc%div==0;a[key]=int(c)*(sc//div)
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
def cover(p,q):
 stack=[('',grid(p),grid(q),tuple((F(0),F(1))for _ in range(6)))];pos=[];gram=[]
 while stack:
  path,a,b,bounds=stack.pop();dep=len(path)
  if min(a.flat)>=0:pos.append(path);continue
  if dep>=6 and min(b.flat)>=0 and vertex(b,bounds):gram.append(path);continue
  assert dep<48,('depth limit',path)
  ax=dep%6;AL,AR=split(a,ax);BL,BR=split(b,ax);lo,hi=bounds[ax];mid=(lo+hi)/2
  for bit,x,y,inter in [('1',AR,BR,(mid,hi)),('0',AL,BL,(lo,mid))]:
   z=list(bounds);z[ax]=inter;stack.append((path+bit,x,y,tuple(z)))
 return sorted(pos),sorted(gram)
records={name:{'degrees':list(p.degree_list()),'terms':len(p.terms()),'sha256':digest(p)}for name,p in polys.items()};covers=[]
for name in ['AC','BC','ABC']:
 pos,gram=cover(polys[name+'_mid'],polys[name+'_gram']);covers.append({'name':name,'mid_nonnegative':pos,'gram_strict':gram})
 print(name,'mid/gram leaves',len(pos),len(gram),flush=True)
out=ROOT/'frontier-20261029-ph7-shared-edge-polytope-H-certificate-v1.json'
out.write_text(json.dumps({'domain':'six strictly positive finite rates','compactification':'u_i=s_i/(1-s_i)',
 'axis':'path depth modulo 6','records':records,'covers':covers},indent=2)+'\n')
print('PASS: three exact shared-edge dual covers; saved',out)
