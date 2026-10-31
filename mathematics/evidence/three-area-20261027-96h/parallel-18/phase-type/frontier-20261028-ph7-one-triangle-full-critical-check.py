#!/usr/bin/env python3
"""Exclude ALL theta for one 3-cycle/no 2/4-cycle at z=8/9.

Discriminant numerator N is cubic in theta. Its theta Bernstein coefficients
b0,b1,b3 and 4*b1*b3-3*b2^2 are strictly positive on all five positive rates.
Then a 2x2 quadratic-form argument proves N>0 for the entire [0,1].
Every positivity proof is exact integer tensor Bernstein, not floating point.
"""
import hashlib,itertools,json,math,sys
from fractions import Fraction as F
from pathlib import Path
import numpy as np
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'frontier-20261028-localdeps'))
import sympy as S
u=S.symbols('u0:5',real=True);th=S.symbols('theta',real=True)
s1,s2,s3,s4,W,O,t,r=S.symbols('s1 s2 s3 s4 W O t r',real=True)
p=s1+t-4;q=s2+t*s1+r-4*p-S.Rational(70,9)
E4=s3+t*s2+r*s1-W-(4*q+S.Rational(70,9)*p+S.Rational(68,9))
E3=s4+t*s3+r*s2-W*(O+t)-(S.Rational(70,9)*q+S.Rational(68,9)*p+S.Rational(289,81))
a00,a01=S.diff(E4,t),S.diff(E4,r);a10,a11=S.diff(E3,t),S.diff(E3,r)
b0,b1=E4.subs({t:0,r:0}),E3.subs({t:0,r:0})
den=S.expand(a00*a11-a01*a10);tn=S.expand(-b0*a11+a01*b1);rn=S.expand(-a00*b1+b0*a10)
es=[sum(S.prod(a)for a in itertools.combinations(u,k))for k in (1,2,3,4)]
subs=dict(zip((s1,s2,s3,s4),es));subs.update({W:th*u[0]*u[1]*u[2],O:u[3]+u[4]})
P=S.Poly(S.expand((-19683*(tn*tn-4*rn*den)).subs(subs)),th);assert P.degree()==3
b=[S.Poly(S.expand(sum(P.nth(j)*S.Rational(math.comb(k,j),math.comb(3,j))for j in range(k+1))),*u)for k in range(4)]
assert all(c.q==1 for poly in b for c in poly.coeffs())
G=4*b[1]*b[3]-3*b[2]*b[2]
polys=[('b0',b[0]),('b1',b[1]),('b3',b[3]),('quadratic_discriminant',G)]

def digest(poly):
 rows=[[list(k),str(int(c))]for k,c in sorted(poly.as_dict().items())]
 return hashlib.sha256(json.dumps(rows,separators=(',',':')).encode()).hexdigest()
def grid(poly):
 ds=[poly.degree(x)for x in u];scale=math.prod(math.lcm(*[math.comb(d,i)for i in range(d+1)])for d in ds)
 arr=np.zeros(tuple(d+1 for d in ds),dtype=object)
 for key,c in poly.as_dict().items():
  assert c.q==1;div=math.prod(math.comb(ds[j],key[j])for j in range(5));assert scale%div==0
  arr[key]=int(c)*(scale//div)
 return arr
def split(A,axis):
 A=np.moveaxis(A,axis,0);d=A.shape[0]-1;levels=[A]
 while levels[-1].shape[0]>1:levels.append(levels[-1][:-1]+levels[-1][1:])
 L=np.stack([levels[k][0]*(1<<(d-k))for k in range(d+1)])
 R=np.stack([levels[d-k][-1]*(1<<k)for k in range(d+1)])
 return np.moveaxis(L,0,axis),np.moveaxis(R,0,axis)
def cover(poly):
 stack=[('',grid(poly),tuple((F(0),F(1))for _ in range(5)))];leaves=[]
 while stack:
  path,A,bounds=stack.pop();dep=len(path)
  if dep>=5 and min(A.flat)>=0:
   ok=True;inside=0
   for corner in itertools.product((0,1),repeat=5):
    coords=[bounds[j][corner[j]]for j in range(5)]
    if all(0<x<1 for x in coords):
     inside+=1;idx=tuple(0 if c==0 else A.shape[j]-1 for j,c in enumerate(corner))
     if A[idx]<=0:ok=False;break
   if inside and ok:leaves.append(path);continue
  assert dep<35,path
  axis=dep%5;L,R=split(A,axis);lo,hi=bounds[axis];mid=(lo+hi)/2
  for bit,child,inter in [('1',R,(mid,hi)),('0',L,(lo,mid))]:
   bb=list(bounds);bb[axis]=inter;stack.append((path+bit,child,tuple(bb)))
 return sorted(leaves)
records=[]
for name,poly in polys:
 paths=cover(poly);records.append({'name':name,'individual_degrees':[poly.degree(x)for x in u],
 'coefficient_terms':len(poly.terms()),'coefficient_sha256':digest(poly),'positive_leaf_paths':paths})
 print(name,'terms',len(poly.terms()),'leaves',len(paths),flush=True)
assert [len(r['positive_leaf_paths'])for r in records]==[657,567,522,565]
out=ROOT/'frontier-20261028-ph7-one-triangle-full-critical-certificate.json'
out.write_text(json.dumps({'z':'8/9','theta_domain':'[0,1]','rate_compactification':'ui=xi/(1-xi)',
 'split_axis':'path depth modulo5','records':records,
 'identity':'N=b0(1-theta)^3+theta[3b1(1-theta)^2+3b2 theta(1-theta)+b3 theta^2]',
 'scope':'one directed 3-cycle, no directed 2/4 cycles, arbitrary other long cycles/edges'},indent=2)+'\n')
print('SymPy',S.__version__,'integer 5D Bernstein PASS: every one-triangle/no-2/4 spectral graph excluded at 8/9')
print('saved:',out)
