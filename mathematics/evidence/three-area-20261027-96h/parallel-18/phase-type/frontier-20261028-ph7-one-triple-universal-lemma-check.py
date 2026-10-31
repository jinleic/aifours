#!/usr/bin/env python3
"""Exact Q/H positivity with one imbalanced triangle and arbitrary 2/4 cycles.

First three rates are positive, other three nonnegative, theta in [0,1].
Q(theta) is linear; H(theta) quadratic. Four endpoint polynomials are
strictly positive; an exact split cover proves either H1>=0 or the quadratic
Gram determinant>0 on every rate point. All Bernstein arithmetic is integer.
"""
import hashlib,itertools,json,math,sys
from fractions import Fraction as F
from pathlib import Path
import numpy as np
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'frontier-20261028-localdeps'))
import sympy as S
u=S.symbols('u0:6',real=True);theta=S.symbols('theta',real=True)
es=[sum(S.prod(a)for a in itertools.combinations(u,k))for k in (1,2,3,4)];f1,f2,f3,f4=es
w=theta*u[0]*u[1]*u[2];O=u[3]+u[4]+u[5]
A=f2-4*f1+S.Rational(74,9);B=f3-4*f2+S.Rational(74,9)*f1-S.Rational(28,3)-w
h0=f4-S.Rational(70,9)*f2+S.Rational(212,9)*f1-S.Rational(1007,27)-w*O
h1=f3-S.Rational(70,9)*f1+S.Rational(212,9)-w
Q=S.Poly(S.expand(81*(A*A-(f1-4)*B)),theta);H=S.Poly(S.expand(-243*(h0*A-h1*B)),theta)
assert Q.degree()==1 and H.degree()==2
qb=[S.Poly(S.expand(sum(Q.nth(j)*S.Rational(math.comb(k,j),math.comb(1,j))for j in range(k+1))),*u)for k in range(2)]
hb=[S.Poly(S.expand(sum(H.nth(j)*S.Rational(math.comb(k,j),math.comb(2,j))for j in range(k+1))),*u)for k in range(3)]
H1=S.Poly(S.expand(2*hb[1].as_expr()),*u);Gram=4*hb[0]*hb[2]-H1*H1
polys=[('Q0',qb[0]),('Q1',qb[1]),('H0',hb[0]),('H2',hb[2]),('H1_twice',H1),('Gram4',Gram)]
assert all(c.q==1 for _,P in polys for c in P.coeffs())

def digest(P):
 rows=[[list(k),str(int(c))]for k,c in sorted(P.as_dict().items())]
 return hashlib.sha256(json.dumps(rows,separators=(',',':')).encode()).hexdigest()
def grid(P):
 ds=[P.degree(x)for x in u];scale=math.prod(math.lcm(*[math.comb(d,i)for i in range(d+1)])for d in ds)
 A=np.zeros(tuple(d+1 for d in ds),dtype=object)
 for key,c in P.as_dict().items():
  div=math.prod(math.comb(ds[j],key[j])for j in range(6));assert scale%div==0
  A[key]=int(c)*(scale//div)
 return A
def split(A,axis):
 A=np.moveaxis(A,axis,0);d=A.shape[0]-1;lev=[A]
 while lev[-1].shape[0]>1:lev.append(lev[-1][:-1]+lev[-1][1:])
 L=np.stack([lev[k][0]*(1<<(d-k))for k in range(d+1)]);R=np.stack([lev[d-k][-1]*(1<<k)for k in range(d+1)])
 return np.moveaxis(L,0,axis),np.moveaxis(R,0,axis)
def vertex_positive(A,bounds):
 inside=0
 for corner in itertools.product((0,1),repeat=6):
  coord=[bounds[j][corner[j]]for j in range(6)]
  if all(0<coord[j]<1 for j in range(3)) and all(coord[j]<1 for j in range(3,6)):
   inside+=1;idx=tuple(0 if c==0 else A.shape[j]-1 for j,c in enumerate(corner))
   if A[idx]<=0:return False
 return inside>0

def single(P):
 stack=[('',grid(P),tuple((F(0),F(1))for _ in range(6)))];leaves=[]
 while stack:
  path,A,bounds=stack.pop();dep=len(path)
  if dep>=6 and min(A.flat)>=0 and vertex_positive(A,bounds):leaves.append(path);continue
  assert dep<45,path
  axis=dep%6;L,R=split(A,axis);lo,hi=bounds[axis];mid=(lo+hi)/2
  for bit,child,inter in [('1',R,(mid,hi)),('0',L,(lo,mid))]:bb=list(bounds);bb[axis]=inter;stack.append((path+bit,child,tuple(bb)))
 return sorted(leaves)
def dual(P,Q):
 stack=[('',grid(P),grid(Q),tuple((F(0),F(1))for _ in range(6)))];pos=[];gram=[]
 while stack:
  path,A,B,bounds=stack.pop();dep=len(path)
  if min(A.flat)>=0:pos.append(path);continue
  if dep>=6 and min(B.flat)>=0 and vertex_positive(B,bounds):gram.append(path);continue
  assert dep<45,path
  axis=dep%6;LA,RA=split(A,axis);LB,RB=split(B,axis);lo,hi=bounds[axis];mid=(lo+hi)/2
  for bit,aa,bb,inter in [('1',RA,RB,(mid,hi)),('0',LA,LB,(lo,mid))]:z=list(bounds);z[axis]=inter;stack.append((path+bit,aa,bb,tuple(z)))
 return sorted(pos),sorted(gram)
records=[]
for name,P in polys[:4]:
 paths=single(P);records.append({'name':name,'individual_degrees':[P.degree(x)for x in u],
  'coefficient_terms':len(P.terms()),'coefficient_sha256':digest(P),'positive_leaf_paths':paths})
 print(name,'leaves',len(paths),flush=True)
pos,gram=dual(H1,Gram)
for name,P in polys[4:]:records.append({'name':name,'individual_degrees':[P.degree(x)for x in u],
 'coefficient_terms':len(P.terms()),'coefficient_sha256':digest(P)})
assert [len(z['positive_leaf_paths'])for z in records[:4]]==[5332,1869,5334,2443]
assert (len(pos),len(gram))==(2714,199)
out=ROOT/'frontier-20261028-ph7-one-triple-universal-lemma-certificate.json'
out.write_text(json.dumps({'z':'8/9','rate_domain':'u0,u1,u2>0; u3,u4,u5>=0; all finite',
 'theta_domain':'[0,1]','records':records,'dual_H1_nonnegative_leaf_paths':pos,'dual_Gram_positive_leaf_paths':gram,
 'split_axis':'path depth modulo6','compactification':'u_i=x_i/(1-x_i)',
 'scope':'universal six-rate coefficient lemma, not by itself PH existence/exclusion'},indent=2)+'\n')
print('SymPy',S.__version__,'integer Bernstein PASS: Q,H positive for all theta and nonnegative outside rates')
print('single leaves 5332/1869/5334/2443; dual H1/Gram leaves 2714/199; saved:',out)
