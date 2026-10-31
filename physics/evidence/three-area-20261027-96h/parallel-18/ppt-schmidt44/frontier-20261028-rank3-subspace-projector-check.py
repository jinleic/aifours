#!/usr/bin/env python3
"""Exact projector/PT comparison for an explicit 4x4 rank>=3 subspace."""
from fractions import Fraction as F
import json
D=16
def v(*terms):
 x=[F(0)]*D
 for i,j,c in terms:x[4*i+j]+=F(c)
 return x
def addouter(M,w,x):
 for i in range(D):
  for j in range(D):M[i][j]+=w*x[i]*x[j]
a=v((0,0,1),(1,1,1),(2,2,1),(3,3,1))
b=v((0,0,-3),(1,1,-1),(2,2,1),(3,3,3))
u=v((0,1,1),(1,2,1),(2,3,1));l=v((1,0,1),(2,1,1),(3,2,1))
P=[[F(0) for _ in range(D)] for _ in range(D)]
for w,x in ((F(1,4),a),(F(1,20),b),(F(1,3),u),(F(1,3),l)):addouter(P,w,x)
def mm(X,Y):return [[sum(X[i][k]*Y[k][j] for k in range(D)) for j in range(D)] for i in range(D)]
assert mm(P,P)==P
PT=[[P[4*(i//4)+j%4][4*(j//4)+i%4] for j in range(D)] for i in range(D)]
def psd(m):
 A=[row[:] for row in m];p=[]
 while A:
  if any(A[i][i]<0 for i in range(len(A))):return None
  k=next((i for i in range(len(A)) if A[i][i]>0),None)
  if k is None:return p if all(x==0 for row in A for x in row) else None
  s=A[k][k];p.append(s);r=[j for j in range(len(A)) if j!=k]
  A=[[A[i][j]-A[i][k]*A[k][j]/s for j in r] for i in r]
 return p
bound=[[F(11,15)*int(i==j)-PT[i][j] for j in range(D)] for i in range(D)]
piv=psd(bound);assert piv is not None
q=v((0,0,-1),(3,3,1));overlap=sum(q[i]*P[i][j]*q[j] for i in range(D) for j in range(D));assert overlap==F(9,5)
# Simple exact PT upper-bound eigenvector on the (0,1),(1,0) block.
# Matrix kernel search with rational elimination.
A=[row[:] for row in bound];pivs=[];row=0
for col in range(D):
 k=next((i for i in range(row,D) if A[i][col]),None)
 if k is None:continue
 A[row],A[k]=A[k],A[row];s=A[row][col];A[row]=[x/s for x in A[row]]
 for i in range(D):
  if i!=row and A[i][col]:
   t=A[i][col];A[i]=[x-t*y for x,y in zip(A[i],A[row])]
 pivs.append(col);row+=1
 if row==D:break
free=next(i for i in range(D) if i not in pivs);x=[F(0)]*D;x[free]=1
for i,p in enumerate(pivs):x[p]=-A[i][free]
assert all(sum(bound[i][j]*x[j] for j in range(D))==0 for i in range(D))
print(json.dumps({'projector_rank':sum(P[i][i] for i in range(D)).__str__(),
 'PT_upper_eigenvalue':'11/15','bound_psd_pivots':len(piv),
 'eigenvector':[(i,str(v)) for i,v in enumerate(x) if v],
 'SR2_ket':'-|00>+|33>','SR2_norm_squared':'2','projector_expectation':'9/5',
 'all_256_projector_entries_checked':True,'limits':'CES property and universal witness obstruction follow from written minors/duality.'},indent=2))
