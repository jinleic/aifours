#!/usr/bin/env python3
"""Exact 8/9 exclusion for every 7-state Metzler graph with directed girth>=5.

No short cycles means characteristic coefficients y^4,y^3 equal those of the
seven-diagonal product. Solve them for sum/product of two chosen diagonal
rates. A five-variable integer Bernstein cover proves the linear determinant
and NEGATIVE discriminant numerator strictly positive on all positive rates.
NumPy object arrays contain Python integers only; no floating arithmetic.
"""
import hashlib,itertools,json,math,sys
from fractions import Fraction as F
from pathlib import Path
import numpy as np
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'frontier-20261028-localdeps'))
import sympy as S
u=S.symbols('u0:5',real=True);s1,s2,s3,s4,t,r=S.symbols('s1 s2 s3 s4 t r',real=True)
p=s1+t-4;q=s2+t*s1+r-4*p-S.Rational(70,9)
E4=s3+t*s2+r*s1-(4*q+S.Rational(70,9)*p+S.Rational(68,9))
E3=s4+t*s3+r*s2-(S.Rational(70,9)*q+S.Rational(68,9)*p+S.Rational(289,81))
assert S.diff(E4,t,r)==S.diff(E3,t,r)==0
a00,a01=S.diff(E4,t),S.diff(E4,r);a10,a11=S.diff(E3,t),S.diff(E3,r)
b0,b1=E4.subs({t:0,r:0}),E3.subs({t:0,r:0})
den=S.factor(a00*a11-a01*a10);tn=S.factor(-b0*a11+a01*b1);rn=S.factor(-a00*b1+b0*a10)
commons=[sum(S.prod(c)for c in itertools.combinations(u,k))for k in (1,2,3,4)];subs=dict(zip((s1,s2,s3,s4),commons))
D=S.Poly(S.expand((81*den).subs(subs)),*u);N=S.Poly(S.expand((-19683*(tn*tn-4*rn*den)).subs(subs)),*u)
assert all(c.q==1 for c in D.coeffs()+N.coeffs())
assert [D.degree(x)for x in u]==[2]*5 and [N.degree(x)for x in u]==[4]*5

def digest(P):
 rows=[[list(k),str(int(c))]for k,c in sorted(P.as_dict().items())]
 return hashlib.sha256(json.dumps(rows,separators=(',',':')).encode()).hexdigest()
def grid(P):
 ds=[P.degree(x)for x in u];scale=math.prod(math.lcm(*[math.comb(d,i)for i in range(d+1)])for d in ds)
 arr=np.zeros(tuple(d+1 for d in ds),dtype=object)
 for key,c in P.as_dict().items():
  div=math.prod(math.comb(ds[j],key[j])for j in range(5));assert scale%div==0
  arr[key]=int(c)*(scale//div)
 return arr
def split(A,axis):
 A=np.moveaxis(A,axis,0);d=A.shape[0]-1;levels=[A]
 while levels[-1].shape[0]>1:levels.append(levels[-1][:-1]+levels[-1][1:])
 left=np.stack([levels[k][0]*(1<<(d-k))for k in range(d+1)])
 right=np.stack([levels[d-k][-1]*(1<<k)for k in range(d+1)])
 return np.moveaxis(left,0,axis),np.moveaxis(right,0,axis)
def cover(P):
 stack=[('',grid(P),tuple((F(0),F(1))for _ in range(5)))];leaves=[]
 while stack:
  path,A,bounds=stack.pop();depth=len(path)
  if depth>=5 and min(A.flat)>=0:
   good=True;interior=0
   for corners in itertools.product((0,1),repeat=5):
    coord=[bounds[j][corners[j]]for j in range(5)]
    if all(0<x<1 for x in coord):
     interior+=1;idx=tuple(0 if c==0 else A.shape[j]-1 for j,c in enumerate(corners))
     if A[idx]<=0:good=False;break
   if interior and good:leaves.append(path);continue
  assert depth<30,path
  axis=depth%5;L,R=split(A,axis);lo,hi=bounds[axis];mid=(lo+hi)/2
  for bit,child,interval in [('1',R,(mid,hi)),('0',L,(lo,mid))]:
   bb=list(bounds);bb[axis]=interval;stack.append((path+bit,child,tuple(bb)))
 return sorted(leaves)
Dc,Nc=cover(D),cover(N);assert (len(Dc),len(Nc))==(513,657)
out=ROOT/'frontier-20261028-ph7-girth5-critical-bernstein-certificate.json'
out.write_text(json.dumps({'z':'8/9','D_coefficients_sha256':digest(D),'N_coefficients_sha256':digest(N),
 'D_variable_degrees':[2]*5,'N_variable_degrees':[4]*5,'D_terms':len(D.terms()),'N_terms':len(N.terms()),
 'D_positive_compactified_binary_leaf_paths':Dc,'N_positive_compactified_binary_leaf_paths':Nc,
 'split_axis':'path depth modulo 5','compactification':'u_i=x_i/(1-x_i); multiply each (1-x_i)^degree_i',
 'identity':'den=D/81; t^2-4r=-N/(3D^2)',
 'scope':'all 7-state irreducible Metzler graphs with no directed cycles of length <=4, not unrestricted PH7'},indent=2)+'\n')
print('SymPy',S.__version__,'integer 5D Bernstein PASS: all girth>=5 spectral graphs excluded at z=8/9')
print('coefficient counts D,N:',len(D.terms()),len(N.terms()),'leaf counts:',len(Dc),len(Nc));print('saved:',out)
