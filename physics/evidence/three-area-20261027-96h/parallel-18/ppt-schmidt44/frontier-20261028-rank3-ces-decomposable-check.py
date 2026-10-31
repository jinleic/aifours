#!/usr/bin/env python3
"""Exact rational PSD+coPSD decomposition of a CES projector witness."""
from fractions import Fraction as F
import json
D=16
def ket(*terms):
 v=[F(0)]*D
 for a,b,c in terms:v[4*a+b]+=F(c)
 return v
def outer(M,w,v):
 for i,x in enumerate(v):
  for j,y in enumerate(v):M[i][j]+=w*x*y
P=[[F(0) for _ in range(D)] for _ in range(D)]
a=ket((0,0,1),(1,1,1),(2,2,1),(3,3,1))
d=ket((0,0,1),(1,1,5),(2,2,-9),(3,3,3))
u=ket((0,1,1),(1,2,1),(2,3,1));l=ket((1,0,1),(2,1,1),(3,2,1))
for w,v in ((F(1,4),a),(F(1,116),d),(F(1,3),u),(F(1,3),l)):outer(P,w,v)
assert all(sum(P[i][k]*P[k][j] for k in range(D))==P[i][j] for i in range(D) for j in range(D))
B=[[F(0) for _ in range(D)] for _ in range(D)]
for i in (0,1,4,10,11,14,15):B[i][i]=F(1,500)
blocks=(((2,5,8),((90,-23,-59),(-23,35,-23),(-59,-23,90))),
 ((3,6,9,12),((61,-21,-41,-20),(-21,50,44,-41),(-41,44,50,-21),(-20,-41,-21,61))),
 ((7,13),((39,-38),(-38,39))))
for inds,block in blocks:
 for i,a0 in enumerate(inds):
  for j,b0 in enumerate(inds):B[a0][b0]=F(block[i][j],500)
BG=[[B[4*(i//4)+j%4][4*(j//4)+i%4] for j in range(D)] for i in range(D)]
A=[[F(24,25)*int(i==j)-P[i][j]-BG[i][j] for j in range(D)] for i in range(D)]
def psd(M):
 x=[r[:] for r in M];piv=[]
 while x:
  if any(x[i][i]<0 for i in range(len(x))):return None
  k=next((i for i in range(len(x)) if x[i][i]>0),None)
  if k is None:return piv if all(z==0 for row in x for z in row) else None
  t=x[k][k];piv.append(t);r=[i for i in range(len(x)) if i!=k]
  x=[[x[i][j]-x[i][k]*x[k][j]/t for j in r] for i in r]
 return piv
Ashift=[[A[i][j]-F(1,1000)*int(i==j) for j in range(D)] for i in range(D)]
Bshift=[[B[i][j]-F(1,10000)*int(i==j) for j in range(D)] for i in range(D)]
ap,bp=psd(Ashift),psd(Bshift);assert ap is not None and bp is not None and len(ap)==len(bp)==16
q=ket((1,1,1),(2,2,-2));norm=sum(x*x for x in q)
lower=sum(q[i]*P[i][j]*q[j] for i in range(D) for j in range(D))/norm
assert lower==F(279,290) and lower-F(24,25)==F(3,1450)
PG=[[P[4*(i//4)+j%4][4*(j//4)+i%4] for j in range(D)] for i in range(D)]
x=ket((1,3,1),(2,2,2),(3,1,1))
pttest=sum(x[i]*(F(24,25)*int(i==j)-PG[i][j])*x[j] for i in range(D) for j in range(D));assert pttest<0
print(json.dumps({'B_denominator':500,'A_margin':'1/1000','B_margin':'1/10000',
 'positive_shifted_A_pivots':len(ap),'positive_shifted_B_pivots':len(bp),
 'SR2_test_overlap':str(lower),'PPT_witness_gap_at_least':'3/1450',
 'non_copt_test_value':str(pttest),'identity_entries':256,
 'limits':'CES property and lambda threshold follow from written determinant/rank2 arguments.'},indent=2))
