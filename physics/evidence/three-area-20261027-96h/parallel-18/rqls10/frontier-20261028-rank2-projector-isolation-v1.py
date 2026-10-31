#!/usr/bin/env python3
"""Exact cyclotomic second-order isolation certificate for one flat rank2 P."""
from fractions import Fraction as Q
from itertools import product
from functools import lru_cache
MOD=[Q(1),Q(0),Q(-1),Q(0),Q(1),Q(0),Q(-1),Q(0),Q(1)]

def trim(p):
 p=p[:]
 while p and not p[-1]:p.pop()
 return p

def divmodp(a,b):
 a=trim(a);b=trim(b);out=[Q(0)]*max(0,len(a)-len(b)+1)
 while a and len(a)>=len(b):
  k=len(a)-len(b);v=a[-1]/b[-1];out[k]=v
  for j,w in enumerate(b):a[k+j]-=v*w
  a=trim(a)
 return trim(out),a

def subp(a,b):
 out=[Q(0)]*max(len(a),len(b))
 for j in range(len(out)):out[j]=(a[j] if j<len(a) else 0)-(b[j] if j<len(b) else 0)
 return trim(out)
def mulp(a,b):
 if not a or not b:return []
 out=[Q(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):out[i+j]+=x*y
 return trim(out)

def reducep(a):
 a=list(a)+[Q(0)]*max(0,8-len(a))
 for k in range(len(a)-1,7,-1):
  v=a[k]
  for j,x in enumerate(MOD):a[k-8+j]-=v*x
 return tuple(a[:8])
Z=reducep([]);ONE=reducep([Q(1)])
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def neg(a):return tuple(-x for x in a)
def sub(a,b):return add(a,neg(b))
def scale(a,k):return tuple(x*Q(k) for x in a)
def mul(a,b):return reducep(mulp(a,b))
@lru_cache(None)
def inverse(a):
 assert a!=Z
 r0,r1=MOD[:],trim(list(a));s0,s1=[],[Q(1)]
 while r1:
  q,r=divmodp(r0,r1);r0,r1=r1,r;s0,s1=s1,subp(s0,mulp(q,s1))
 assert len(r0)==1
 return reducep([x/r0[0] for x in s0])
def divide(a,b):return mul(a,inverse(b))
@lru_cache(None)
def power(k):
 k%=20;return reducep([Q(0)]*k+[Q(1)])
def conj(a):
 out=Z
 for i,x in enumerate(a):out=add(out,scale(power(-i),x))
 return out
def isreal(a):return conj(a)==a
omega=lambda k:power(4*k)
ii=power(5);root5=add(ONE,scale(add(omega(1),omega(-1)),2))
assert mul(root5,root5)==scale(ONE,5) and mul(ii,ii)==neg(ONE)

def summ(vals):
 out=Z
 for v in vals:out=add(out,v)
 return out

# N=sqrt5 * B† W, W=D5² U, and B=I,U,D5U.
N=[]
for basis in range(3):
 mat=[]
 for j in range(5):
  row=[]
  for a in range(5):
   if basis==0:val=omega(3*j*j+3*j*a)
   else:
    q=3 if basis==1 else 4
    val=scale(mul(root5,summ(omega(q*t*t+3*(a-j)*t) for t in range(5))),Q(1,5))
   assert mul(val,conj(val))==ONE
   row.append(val)
  mat.append(row)
 N.append(mat)

# Real chart coordinates x=(Re T00, Im T00, ..., Re T21, Im T21).
J=[]
for basis in range(3):
 for j in range(4):
  row=[]
  for q in range(3):
   for k in range(2):
    t=mul(N[basis][j][2+q],conj(N[basis][j][k]))
    row.extend((add(t,conj(t)),add(mul(ii,t),conj(mul(ii,t)))))
  assert len(row)==12 and all(isreal(v) for v in row)
  J.append(row)

def nullspace(A):
 A=[row[:] for row in A];m=len(A);n=len(A[0]);pivot=[];r=0
 for col in range(n):
  pick=next((i for i in range(r,m) if A[i][col]!=Z),None)
  if pick is None:continue
  A[r],A[pick]=A[pick],A[r];v=A[r][col]
  A[r]=[divide(x,v) for x in A[r]]
  for i in range(m):
   if i!=r and A[i][col]!=Z:
    v=A[i][col];A[i]=[sub(x,mul(v,y)) for x,y in zip(A[i],A[r])]
  pivot.append(col);r+=1
  if r==m:break
 free=[c for c in range(n) if c not in pivot];basis=[]
 for c in free:
  v=[Z]*n;v[c]=ONE
  for k,pc in enumerate(pivot):v[pc]=neg(A[k][c])
  basis.append(v)
 return r,basis
rank,K=nullspace(J)
rankT,L=nullspace([list(x) for x in zip(*J)])
assert rank==rankT==10 and len(K)==len(L)==2
assert all(isreal(v) for row in K+L for v in row)

def quadratic(x):
 T=[[add(x[2*(2*q+k)],mul(ii,x[2*(2*q+k)+1])) for k in range(2)] for q in range(3)]
 out=[]
 for basis in range(3):
  for j in range(4):
   n=N[basis][j]
   t1=summ(mul(v,conj(v)) for v in (summ(mul(n[2+q],T[q][k]) for q in range(3)) for k in range(2)))
   t2=summ(mul(v,conj(v)) for v in (summ(mul(T[q][k],conj(n[k])) for k in range(2)) for q in range(3)))
   val=sub(t1,t2);assert isreal(val);out.append(val)
 return out

def dot(a,b):return summ(mul(x,y) for x,y in zip(a,b))
q1=quadratic(K[0]);q2=quadratic(K[1]);q12=[sub(sub(x,y),z) for x,y,z in zip(quadratic([add(x,y) for x,y in zip(K[0],K[1])]),q1,q2)]
coeff=[[dot(l,q1),dot(l,q12),dot(l,q2)] for l in L]
assert all(isreal(v) for row in coeff for v in row)
# Resultant of two homogeneous quadratics in the projective t=y/x chart.
def det(A):
 A=[row[:] for row in A];value=ONE;n=len(A)
 for c in range(n):
  pick=next((i for i in range(c,n) if A[i][c]!=Z),None)
  if pick is None:return Z
  if pick!=c:A[c],A[pick]=A[pick],A[c];value=neg(value)
  p=A[c][c];value=mul(value,p)
  for i in range(c+1,n):
   if A[i][c]==Z:continue
   v=divide(A[i][c],p)
   for j in range(c,n):A[i][j]=sub(A[i][j],mul(v,A[c][j]))
 return value
(a,b,c),(d,e,f)=coeff
res=det([[c,b,a,Z],[Z,c,b,a],[f,e,d,Z],[Z,f,e,d]])
assert res!=Z and not (c==Z and f==Z)
print('PASS Phi20 arithmetic; exact 12x12 Jacobian rank',rank,'and real 2D kernels')
print('PASS two left-null quadratic forms have nonzero exact resultant, including infinity')
print('Therefore no nonzero common kernel direction; written local-isolation proof required')
