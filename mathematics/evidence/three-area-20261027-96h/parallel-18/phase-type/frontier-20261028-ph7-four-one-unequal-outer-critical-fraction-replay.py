#!/usr/bin/env python3
"""Independent stdlib bivariate polynomial/Bernstein replay of 4U+W exclusion."""
import ast,json,math
from fractions import Fraction as Q
from pathlib import Path
ROOT=Path(__file__).resolve().parent
C=json.loads((ROOT/'frontier-20261028-ph7-four-one-unequal-outer-critical-certificate.json').read_text())

def clean(a):return {k:x for k,x in a.items()if x}
def con(x):return {(0,0):Q(x)}if x else{}
def add(a,b):
 o=a.copy()
 for k,x in b.items():o[k]=o.get(k,Q(0))+x
 return clean(o)
def scale(a,c):return clean({k:x*Q(c)for k,x in a.items()})
def sub(a,b):return add(a,scale(b,-1))
def mul(a,b):
 o={}
 for (i,j),x in a.items():
  for (k,l),y in b.items():o[(i+k,j+l)]=o.get((i+k,j+l),Q(0))+x*y
 return clean(o)
def pw(a,n):
 o=con(1)
 for _ in range(n):o=mul(o,a)
 return o
def yadd(a,b):return [add(a[i]if i<len(a)else{},b[i]if i<len(b)else{})for i in range(max(len(a),len(b)))]
def ymul(a,b):
 o=[{}for _ in range(len(a)+len(b)-1)]
 for i,x in enumerate(a):
  for j,y in enumerate(b):o[i+j]=add(o[i+j],mul(x,y))
 return o
def yscale(a,c):return [scale(x,c)for x in a]
def ypow(a,n):
 o=[con(1)]
 for _ in range(n):o=ymul(o,a)
 return o
u={(1,0):Q(1)};w={(0,1):Q(1)};one=con(1);z=Q(8,9)

def e43(t,r):
 A=ymul(ymul(ypow([u,one],4),[w,one]),[con(r),con(t),one])
 p=sub(A[6],con(4));q=sub(sub(A[5],scale(p,4)),con(6+2*z))
 D=ymul([{},one],ypow([con(1+z),con(2),one],2));R=yadd(A,yscale(ymul(D,[q,p,one]),-1))
 return R[4],R[3]

z0=e43(0,0);at=e43(1,0);ar=e43(0,1)
a00,a10=sub(at[0],z0[0]),sub(at[1],z0[1]);a01,a11=sub(ar[0],z0[0]),sub(ar[1],z0[1])
assert e43(2,0)==tuple(add(z0[i],scale(sub(at[i],z0[i]),2))for i in range(2))
assert e43(0,2)==tuple(add(z0[i],scale(sub(ar[i],z0[i]),2))for i in range(2))
assert e43(1,1)==tuple(add(at[i],sub(ar[i],z0[i]))for i in range(2))
den=sub(mul(a00,a11),mul(a01,a10));tn=add(scale(mul(z0[0],a11),-1),mul(a01,z0[1]));rn=add(scale(mul(a00,z0[1]),-1),mul(z0[0],a10))
D=scale(den,Q(81,2));N=scale(sub(mul(tn,tn),scale(mul(rn,den),4)),-6561)

def parse(node):
 if isinstance(node,ast.Constant)and isinstance(node.value,int):return con(node.value)
 if isinstance(node,ast.Name)and node.id in ('u','w'):return u if node.id=='u' else w
 if isinstance(node,ast.UnaryOp)and isinstance(node.op,ast.USub):return scale(parse(node.operand),-1)
 if isinstance(node,ast.BinOp):
  a=parse(node.left)
  if isinstance(node.op,ast.Pow):
   assert isinstance(node.right,ast.Constant)and isinstance(node.right.value,int)and node.right.value>=0
   return pw(a,node.right.value)
  b=parse(node.right)
  if isinstance(node.op,ast.Add):return add(a,b)
  if isinstance(node.op,ast.Sub):return sub(a,b)
  if isinstance(node.op,ast.Mult):return mul(a,b)
  if isinstance(node.op,ast.Div):
   assert len(b)==1 and (0,0) in b and b[(0,0)]!=0
   return scale(a,1/b[(0,0)])
 raise ValueError(ast.dump(node))
assert D==parse(ast.parse(C['D_polynomial'],mode='eval').body)
assert N==parse(ast.parse(C['N_polynomial'],mode='eval').body)

def matrix(p,m,n):return [[p.get((i,j),Q(0))/math.comb(m,i)/math.comb(n,j)for j in range(n+1)]for i in range(m+1)]
def split1(b):
 rows=[b]
 while len(rows[-1])>1:rows.append([(x+y)/2 for x,y in zip(rows[-1],rows[-1][1:])])
 return [r[0]for r in rows],[r[-1]for r in rows][::-1]
def split2(A):
 m=len(A);n=len(A[0]);L=[[Q(0)]*n for _ in range(m)];R=[[Q(0)]*n for _ in range(m)]
 for j in range(n):
  lo,hi=split1([A[i][j]for i in range(m)])
  for i in range(m):L[i][j]=lo[i];R[i][j]=hi[i]
 ll=[];lh=[];rl=[];rh=[]
 for i in range(m):
  a,b=split1(L[i]);c,d=split1(R[i]);ll.append(a);lh.append(b);rl.append(c);rh.append(d)
 return [ll,lh,rl,rh]
def verify_cover(poly,m,n,leaves):
 leaves=set(leaves);seen=set()
 def walk(path,A,x0,x1,y0,y1):
  if path in leaves:
   seen.add(path);assert all(x>=0 for row in A for x in row)
   corners=[(x0,y0,A[0][0]),(x0,y1,A[0][-1]),(x1,y0,A[-1][0]),(x1,y1,A[-1][-1])]
   assert all(x>0 for i,j,x in corners if i<1 and j<1)
   return
  assert any(x.startswith(path)for x in leaves),path
  xm=(x0+x1)/2;ym=(y0+y1)/2;coords=[(x0,xm,y0,ym),(x0,xm,ym,y1),(xm,x1,y0,ym),(xm,x1,ym,y1)]
  for i,B in enumerate(split2(A)):walk(path+str(i),B,*coords[i])
 walk('',matrix(poly,m,n),Q(0),Q(1),Q(0),Q(1));assert seen==leaves
verify_cover(D,4,2,C['D_positive_compactified_bernstein_leaf_paths'])
verify_cover(N,10,4,C['N_positive_compactified_bernstein_leaf_paths'])
print('Independent stdlib Fraction PASS: exact bivariate coefficient identities and complete 10/16 Bernstein cover trees')
