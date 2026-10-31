#!/usr/bin/env python3
"""Independent stdlib exact replay of the 3U+2W/V,V critical exclusion.

For 181 rational U values, obtain first quadratic W-resultants and both
V-polynomials independently by Newton interpolation; a direct Fraction 18x18
Sylvester determinant checks the given factors. Degree <=180 makes agreement
an exact polynomial identity. Verify every Bernstein/tail sign independently.
"""
import ast,json,math,time
from fractions import Fraction as Q
from pathlib import Path
ROOT=Path(__file__).resolve().parent
C=json.loads((ROOT/'frontier-20261028-ph7-three-two-cycle-89-certificate.json').read_text())

def trim(p):
 while len(p)>1 and not p[-1]:p.pop()
 return p
def add(a,b):return trim([(a[i]if i<len(a)else Q(0))+(b[i]if i<len(b)else Q(0))for i in range(max(len(a),len(b)))])
def mul(a,b):
 o=[Q(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):o[i+j]+=x*y
 return trim(o)
def scale(a,c):return trim([x*c for x in a])
def powp(a,n):
 o=[Q(1)]
 for _ in range(n):o=mul(o,a)
 return o

def eval_E(u,v,w):
 z=Q(8,9);p=3*u+2*w+2*v-4
 e2=3*u*u+6*u*w+w*w+6*u*v+4*w*v+v*v;q=e2-4*p-(6+2*z)
 base=mul(mul(powp([u,Q(1)],3),powp([w,Q(1)],2)),powp([v,Q(1)],2))
 dz=mul([Q(0),Q(1)],powp([1+z,Q(2),Q(1)],2))
 R=add(base,scale(mul(dz,[q,p,Q(1)]),-1));R += [Q(0)]*max(0,5-len(R))
 return [R[4],R[3],R[1]-2*v*R[2]]

def interpolate(values):
 values=values[:];out=[Q(0)];basis=[Q(1)];fact=1
 for i in range(len(values)):
  if i:fact*=i
  out=add(out,scale(basis,values[0]/fact));basis=mul(basis,[Q(-i),Q(1)])
  values=[values[j+1]-values[j]for j in range(len(values)-1)]
 return out

def det(mat):
 A=[r[:]for r in mat];d=Q(1);n=len(A)
 for k in range(n):
  ix=next((i for i in range(k,n)if A[i][k]),None)
  if ix is None:return Q(0)
  if ix!=k:A[k],A[ix]=A[ix],A[k];d=-d
  x=A[k][k];d*=x
  for i in range(k+1,n):
   c=A[i][k]/x
   for j in range(k+1,n):A[i][j]-=c*A[k][j]
   A[i][k]=Q(0)
 return d

def syl(f,g,m,n):
 f=f+[Q(0)]*(m+1-len(f));g=g+[Q(0)]*(n+1-len(g));M=[[Q(0)]*(m+n)for _ in range(m+n)]
 for i in range(n):
  for j,x in enumerate(reversed(f)):M[i][i+j]=x
 for i in range(m):
  for j,x in enumerate(reversed(g)):M[n+i][i+j]=x
 return det(M)

def first(u,v):
 samples=[eval_E(u,v,Q(w))for w in range(3)]
 E=[interpolate([r[i]for r in samples])for i in range(3)]
 return syl(E[0],E[1],2,2),syl(E[0],E[2],2,2)

def parse(node):
 if isinstance(node,ast.Constant)and isinstance(node.value,int):return [Q(node.value)]
 if isinstance(node,ast.Name)and node.id=='u':return [Q(0),Q(1)]
 if isinstance(node,ast.UnaryOp)and isinstance(node.op,ast.USub):return scale(parse(node.operand),-1)
 if isinstance(node,ast.BinOp):
  a=parse(node.left)
  if isinstance(node.op,ast.Pow):
   assert isinstance(node.right,ast.Constant)and isinstance(node.right.value,int)and node.right.value>=0
   return powp(a,node.right.value)
  b=parse(node.right)
  if isinstance(node.op,ast.Add):return add(a,b)
  if isinstance(node.op,ast.Sub):return add(a,scale(b,-1))
  if isinstance(node.op,ast.Mult):return mul(a,b)
 raise ValueError(ast.dump(node))
def val(poly,x):
 out=Q(0)
 for c in reversed(poly):out=out*x+c
 return out

factors=[(parse(ast.parse(r['polynomial'],mode='eval').body),int(r['multiplicity']))for r in C['outer_factors']]
assert [(len(p)-1,m)for p,m in factors]==[(1,6),(2,12),(6,1),(30,1),(66,1)]
const=Q(C['outer_factor_constant']);start=time.monotonic()
for ui in range(181):
 u=Q(ui);samples=[first(u,Q(j))for j in range(11)]
 f=interpolate([x[0]for x in samples[:9]]);h=interpolate([x[1]for x in samples])
 result=syl(f,h,8,10);expected=const
 for factor,m in factors:expected*=val(factor,u)**m
 assert result==expected,ui
 if ui%30==0:print('exact U points',ui+1,'/181',flush=True)

def bernstein(poly,lo,hi):
 n=len(poly)-1;w=hi-lo
 power=[sum(poly[i]*math.comb(i,j)*lo**(i-j)*w**j for i in range(j,n+1))for j in range(n+1)]
 return [sum(power[j]*Q(math.comb(k,j),math.comb(n,j))for j in range(k+1))for k in range(n+1)]
assert factors[0][0]==[Q(0),Q(1)] and factors[1][0]==[Q(17),Q(-18),Q(9)]
for record,(poly,mult)in zip(C['outer_factors'][2:],factors[2:]):
 leaves=[(Q(a),Q(b))for a,b in record['bernstein_positive_subintervals_0_to_2']]
 assert leaves[0][0]==0 and leaves[-1][1]==2 and all(leaves[i][1]==leaves[i+1][0]for i in range(len(leaves)-1))
 for lo,hi in leaves:assert all(c>0 for c in bernstein(poly,lo,hi))
 # Coefficients of p(x+2), all strictly positive for x>=0.
 for j in range(len(poly)):
  assert sum(poly[i]*math.comb(i,j)*Q(2)**(i-j)for i in range(j,len(poly)))>0
print('Independent stdlib Fraction PASS: 181 nested Sylvester evaluations prove degree<=180 identity; all Bernstein/tail signs exact')
print('elapsed_seconds',time.monotonic()-start)
