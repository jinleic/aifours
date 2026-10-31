#!/usr/bin/env python3
"""Exact 8/9 exclusion for every 7-state Metzler graph without 2- or 3-cycles.

The y4 coefficient equals the diagonal e3, while y3 is diagonal e4 minus
nonnegative 4-cycle weights. Eliminate one rate and certify two universal
six-rate signs by exhaustive integer Bernstein covers. No floating arithmetic.
"""
import hashlib,itertools,json,math,sys
from fractions import Fraction as F
from pathlib import Path
import numpy as np
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'frontier-20261028-localdeps'))
import sympy as S
u=S.symbols('u0:6',real=True);f1,f2,f3,f4=S.symbols('f1 f2 f3 f4',real=True)
A=f2-4*f1+S.Rational(74,9);B=f3-4*f2+S.Rational(74,9)*f1-S.Rational(28,3)
qnum=S.expand(A*A-(f1-4)*B)
h0=f4-S.Rational(70,9)*f2+S.Rational(212,9)*f1-S.Rational(1007,27)
h1=f3-S.Rational(70,9)*f1+S.Rational(212,9)
hnum=S.expand(h0*A-h1*B)
commons=[sum(S.prod(c)for c in itertools.combinations(u,k))for k in (1,2,3,4)]
subs=dict(zip((f1,f2,f3,f4),commons))
Q=S.Poly(S.expand((81*qnum).subs(subs)),*u);H=S.Poly(S.expand((-243*hnum).subs(subs)),*u)
assert all(c.q==1 for c in Q.coeffs()+H.coeffs())
assert [Q.degree(x)for x in u]==[2]*6 and [H.degree(x)for x in u]==[2]*6

def digest(P):
 rows=[[list(k),str(int(c))]for k,c in sorted(P.as_dict().items())]
 return hashlib.sha256(json.dumps(rows,separators=(',',':')).encode()).hexdigest()
def grid(P):
 ds=[P.degree(x)for x in u];scale=math.prod(math.lcm(*[math.comb(d,i)for i in range(d+1)])for d in ds)
 arr=np.zeros(tuple(d+1 for d in ds),dtype=object)
 for key,c in P.as_dict().items():
  div=math.prod(math.comb(ds[j],key[j])for j in range(6));assert scale%div==0
  arr[key]=int(c)*(scale//div)
 return arr
def split(A,axis):
 A=np.moveaxis(A,axis,0);d=A.shape[0]-1;levels=[A]
 while levels[-1].shape[0]>1:levels.append(levels[-1][:-1]+levels[-1][1:])
 left=np.stack([levels[k][0]*(1<<(d-k))for k in range(d+1)])
 right=np.stack([levels[d-k][-1]*(1<<k)for k in range(d+1)])
 return np.moveaxis(left,0,axis),np.moveaxis(right,0,axis)
def cover(P):
 stack=[('',grid(P),tuple((F(0),F(1))for _ in range(6)))];leaves=[]
 while stack:
  path,A,bounds=stack.pop();depth=len(path)
  if depth>=6 and min(A.flat)>=0:
   good=True;interior=0
   for corners in itertools.product((0,1),repeat=6):
    coord=[bounds[j][corners[j]]for j in range(6)]
    if all(0<x<1 for x in coord):
     interior+=1;idx=tuple(0 if c==0 else A.shape[j]-1 for j,c in enumerate(corners))
     if A[idx]<=0:good=False;break
   if interior and good:leaves.append(path);continue
  assert depth<45,path
  axis=depth%6;L,R=split(A,axis);lo,hi=bounds[axis];mid=(lo+hi)/2
  for bit,child,interval in [('1',R,(mid,hi)),('0',L,(lo,mid))]:
   bb=list(bounds);bb[axis]=interval;stack.append((path+bit,child,tuple(bb)))
 return sorted(leaves)
Qc,Hc=cover(Q),cover(H);assert (len(Qc),len(Hc))==(5332,5334)
out=ROOT/'frontier-20261028-ph7-girth4-critical-bernstein-certificate.json'
out.write_text(json.dumps({'z':'8/9','Q_coefficients_sha256':digest(Q),'H_coefficients_sha256':digest(H),
 'Q_variable_degrees':[2]*6,'H_variable_degrees':[2]*6,'Q_terms':len(Q.terms()),'H_terms':len(H.terms()),
 'Q_positive_compactified_binary_leaf_paths':Qc,'H_positive_compactified_binary_leaf_paths':Hc,
 'split_axis':'path depth modulo 6','compactification':'u_i=x_i/(1-x_i); multiply each (1-x_i)^2',
 'identity':'E4=A*u7+B; q=Q/(81*A); E3=-H/(243*A)',
 'scope':'all irreducible 7-state Metzler graphs without directed 2- or 3-cycles, not unrestricted PH7'},indent=2)+'\n')
print('SymPy',S.__version__,'integer 6D Bernstein PASS: all girth>=4 spectral graphs excluded at z=8/9')
print('coefficient counts Q,H:',len(Q.terms()),len(H.terms()),'leaf counts:',len(Qc),len(Hc));print('saved:',out)
