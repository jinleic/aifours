#!/usr/bin/env python3
"""Independent stdlib replay of z=8/9 resultant factorization and Sturm counts.

Direct coefficient arithmetic builds the two V-polynomials at each of 55
integer U values; Newton interpolation and Fraction Gaussian elimination give
the 9x9 Sylvester determinant. Degree <=54 makes those 55 exact checks a
polynomial identity. Factors are parsed as arithmetic AST, never eval'd.
"""
import ast,json,math
from fractions import Fraction as Q
from pathlib import Path
ROOT=Path(__file__).resolve().parent
C=json.loads((ROOT/'frontier-20261028-ph7-asymmetric-cycle-89-resultant-certificate.json').read_text())

def trim(a):
 while len(a)>1 and not a[-1]:a.pop()
 return a
def add(a,b):return trim([(a[i]if i<len(a)else Q(0))+(b[i]if i<len(b)else Q(0))for i in range(max(len(a),len(b)))])
def mul(a,b):
 out=[Q(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):out[i+j]+=x*y
 return trim(out)
def scale(a,x):return trim([x*y for y in a])
def powp(a,n):
 p=[Q(1)]
 for _ in range(n):p=mul(p,a)
 return p

def polys(u,v,w):
 z=Q(8,9);p=4*u+w+2*v-4;q=6*u*u+8*u*v+v*v+4*u*w+2*v*w-4*p-(6+2*z)
 base=mul(mul([w,Q(1)],powp([u,Q(1)],4)),powp([v,Q(1)],2))
 D=mul([Q(0),Q(1)],powp([1+z,Q(2),Q(1)],2))
 R=add(base,scale(mul(D,[q,p,Q(1)]),-1));R+= [Q(0)]*max(0,5-len(R))
 return [R[4],R[3],R[1]-2*v*R[2]]

def elims(u,v):
 b=polys(u,v,Q(0));t=polys(u,v,Q(1));a=[t[i]-b[i]for i in range(3)]
 return a[0]*b[1]-a[1]*b[0],a[0]*b[2]-a[2]*b[0]

def interpolate(values):
 values=values[:];result=[Q(0)];basis=[Q(1)];fact=1
 for j in range(len(values)):
  if j:fact*=j
  result=add(result,scale(basis,values[0]/fact));basis=mul(basis,[Q(-j),Q(1)])
  values=[values[i+1]-values[i]for i in range(len(values)-1)]
 return result

def det(A):
 A=[row[:]for row in A];d=Q(1);n=len(A)
 for k in range(n):
  pivot=next((i for i in range(k,n)if A[i][k]),None)
  if pivot is None:return Q(0)
  if pivot!=k:A[k],A[pivot]=A[pivot],A[k];d=-d
  x=A[k][k];d*=x
  for i in range(k+1,n):
   c=A[i][k]/x
   for j in range(k+1,n):A[i][j]-=c*A[k][j]
   A[i][k]=Q(0)
 return d

def parse_poly(node):
 if isinstance(node,ast.Constant)and isinstance(node.value,int):return [Q(node.value)]
 if isinstance(node,ast.Name)and node.id=='u':return [Q(0),Q(1)]
 if isinstance(node,ast.UnaryOp)and isinstance(node.op,ast.USub):return scale(parse_poly(node.operand),-1)
 if isinstance(node,ast.BinOp):
  a=parse_poly(node.left)
  if isinstance(node.op,ast.Pow):
   assert isinstance(node.right,ast.Constant)and isinstance(node.right.value,int)and node.right.value>=0
   return powp(a,node.right.value)
  b=parse_poly(node.right)
  if isinstance(node.op,ast.Add):return add(a,b)
  if isinstance(node.op,ast.Sub):return add(a,scale(b,-1))
  if isinstance(node.op,ast.Mult):return mul(a,b)
 raise ValueError(ast.dump(node))

def val(poly,x):
 out=Q(0)
 for c in reversed(poly):out=out*x+c
 return out

factors=[(parse_poly(ast.parse(r['polynomial'],mode='eval').body),r['multiplicity'])for r in C['factor_sturm_records']]
constant=Q(C['resultant_coefficient'])
for xi in range(55):
 u=Q(xi);samples=[elims(u,Q(j))for j in range(6)]
 f=interpolate([x[0]for x in samples[:5]]);h=interpolate([x[1]for x in samples])
 f+=(5-len(f))*[Q(0)];h+=(6-len(h))*[Q(0)]
 # Five rows of F (V degree <=4), four rows of H (degree <=5).
 mat=[[Q(0)for _ in range(9)]for _ in range(9)]
 for i in range(5):
  for j,x in enumerate(reversed(f)):mat[i][i+j]=x
 for i in range(4):
  for j,x in enumerate(reversed(h)):mat[5+i][i+j]=x
 expected=constant
 for polynomial,mult in factors:expected*=val(polynomial,u)**mult
 assert det(mat)==expected,xi

def primitive(p):
 den=math.lcm(*(x.denominator for x in p));ints=[int(x*den)for x in p];g=math.gcd(*ints)
 return [Q(x//g)for x in ints]if g else [Q(0)]
def remainder(a,b):
 a=trim(a[:]);b=trim(b[:])
 while len(a)>=len(b) and any(a):
  c=a[-1]/b[-1];k=len(a)-len(b)
  for j,x in enumerate(b):a[j+k]-=c*x
  trim(a)
 return a
def changes(a):
 a=[1 if x>0 else -1 for x in a if x]
 return sum(a[i]!=a[i-1]for i in range(1,len(a)))
def sturm(poly):
 p=primitive(poly);q=primitive([i*p[i]for i in range(1,len(p))]);seq=[p,q]
 while any(seq[-1]):
  r=primitive(scale(remainder(seq[-2],seq[-1]),-1))
  if not any(r):break
  seq.append(r)
 return (changes([p[-1]*(-1)**(len(p)-1)for p in seq]),changes([p[-1]for p in seq]))
counts=[sturm(factor)for factor,_ in factors]
assert counts==[(1,1),(3,3),(3,3),(12,12)]
print('Independent stdlib Fraction replay PASS: 55 Sylvester evaluations establish degree<=54 identity; four Sturm root counts zero')
print('variations (-inf,+inf):',counts)
