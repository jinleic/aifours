#!/usr/bin/env python3
"""Exact 8/9 exclusion for a single 3-cycle/no 4-cycle with theta<=31/32.

The polynomial for the outer-diagonal discriminant is cubic in triangle
fraction theta. Five dyadic theta intervals reduce its positivity to 16
five-rate polynomials, each covered by exact integer tensor Bernstein leaves.
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
b=[S.expand(sum(P.nth(j)*S.Rational(math.comb(k,j),math.comb(3,j))for j in range(k+1)))for k in range(4)]

def digest(poly):
 rows=[[list(k),str(int(c))]for k,c in sorted(poly.as_dict().items())]
 return hashlib.sha256(json.dumps(rows,separators=(',',':')).encode()).hexdigest()
def grid(poly):
 ds=[poly.degree(x)for x in u];assert ds==[4]*5
 scale=math.prod(math.lcm(*[math.comb(d,i)for i in range(d+1)])for d in ds)
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
    coord=[bounds[j][corner[j]]for j in range(5)]
    if all(0<x<1 for x in coord):
     inside+=1;idx=tuple(0 if c==0 else A.shape[j]-1 for j,c in enumerate(corner))
     if A[idx]<=0:ok=False;break
   if inside and ok:leaves.append(path);continue
  assert dep<40,path
  axis=dep%5;L,R=split(A,axis);lo,hi=bounds[axis];mid=(lo+hi)/2
  for bit,child,inter in [('1',R,(mid,hi)),('0',L,(lo,mid))]:
   bb=list(bounds);bb[axis]=inter;stack.append((path+bit,child,tuple(bb)))
 return sorted(leaves)
def split_theta(row):
 layers=[row]
 while len(layers[-1])>1:layers.append([S.expand((x+y)/2)for x,y in zip(layers[-1],layers[-1][1:])])
 return [x[0]for x in layers],[x[-1]for x in layers][::-1]

records=[];current=b
for stage in range(1,6):
 left,current=split_theta(current)
 for j,expr in enumerate(left):
  if stage>1 and j==0:continue # previous interval right endpoint
  Pj=S.Poly(expr,*u);scale=S.ilcm(*[c.q for c in Pj.coeffs()]);Pj=S.Poly(S.expand(expr*scale),*u)
  leaves=cover(Pj)
  records.append({'stage':stage,'bernstein_index':j,'positive_scale':int(scale),
                  'coefficient_sha256':digest(Pj),'coefficient_terms':len(Pj.terms()),'positive_leaf_paths':leaves})
  print('stage',stage,'coefficient',j,'leaves',len(leaves),flush=True)
assert len(records)==16
out=ROOT/'frontier-20261028-ph7-one-triangle-31over32-critical-certificate.json'
out.write_text(json.dumps({'z':'8/9','theta_intervals':'[0,1/2],[1/2,3/4],[3/4,7/8],[7/8,15/16],[15/16,31/32]',
 'rate_compactification':'ui=xi/(1-xi), each degree4','split_axis':'path depth modulo5',
 'records':records,'scope':'exactly one directed 3-cycle, no 2- or 4-cycles; triangle product fraction theta<=31/32'},indent=2)+'\n')
print('SymPy',S.__version__,'integer 5D Bernstein PASS: all one-triangle theta<=31/32 excluded at 8/9')
print('saved:',out)
