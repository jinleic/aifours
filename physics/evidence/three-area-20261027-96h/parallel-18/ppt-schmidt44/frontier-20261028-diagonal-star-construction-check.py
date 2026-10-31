#!/usr/bin/env python3
"""Exact nontrivial star case for the diagonal-minus-correlated witness proof."""
from fractions import Fraction as F
import json
n=16;d=[[F(0) for j in range(4)] for i in range(4)]
for i,t in enumerate((F(7,2),F(18,5),F(37,10),F(19,5))):d[i][i]=t
for i in range(1,4):d[0][i]=d[i][0]=F(1,2)
for i,j,q in ((1,2,F(21,20)),(1,3,F(2)),(2,3,F(3))):d[i][j]=d[j][i]=q
def zeros():return [[F(0) for _ in range(n)] for _ in range(n)]
def pt(M):return [[M[4*(i//4)+j%4][4*(j//4)+i%4] for j in range(n)] for i in range(n)]
def psd(M):
 A=[r[:] for r in M];rank=0
 while A:
  if any(A[i][i]<0 for i in range(len(A))):return None
  k=next((i for i in range(len(A)) if A[i][i]>0),None)
  if k is None:return rank if all(x==0 for row in A for x in row) else None
  p=A[k][k];I=[i for i in range(len(A)) if i!=k]
  A=[[A[i][j]-A[i][k]*A[k][j]/p for j in I] for i in I];rank+=1
 return rank
W=zeros();B=zeros()
for i in range(4):
 for j in range(4):W[4*i+j][4*i+j]+=d[i][j]
for i in range(4):
 for j in range(4):W[5*i][5*j]-=1
a=[d[i][i]-1 for i in range(4)];b=[None]+[1-d[0][j] for j in range(1,4)]
for i in range(4):
 for j in range(i+1,4):
  q=d[i][j];c=q if i==0 else min(q,1+b[i]*b[j]/a[0]);p=4*i+j;k=4*j+i
  B[p][p]+=c;B[k][k]+=c;B[p][k]-=c;B[k][p]-=c
BG=pt(B);A=[[W[i][j]-BG[i][j] for j in range(n)] for i in range(n)]
rA,rB=psd(A),psd(B);assert rA is not None and rB is not None
# Matching {0,3},{1,2}; first high edge is below 1+1/a0.
assert d[1][2]<=1+1/a[0]
H=[[A[5*i][5*j] for j in range(4)] for i in range(4)]
R=[[H[i][j]-H[i][0]*H[0][j]/a[0] for j in range(1,4)] for i in range(1,4)]
C=[[a[i] if i==j else F(-1) for j in range(4)] for i in range(4)]
C[0][3]=C[3][0]=-b[3];C[1][2]=C[2][1]=d[1][2]-1
C=[[C[i][j]-C[i][0]*C[0][j]/a[0] for j in range(1,4)] for i in range(1,4)]
assert psd(C) is not None and psd(R) is not None
assert all(R[i][j]>=C[i][j] for i in range(3) for j in range(3))
assert R[0][1]<0
wI=sum(W[5*i][5*j] for i in range(4) for j in range(4));p01=pt(W)
wpt=p01[1][1]+p01[1][4]+p01[4][1]+p01[4][4]
assert wI==F(-7,5) and wpt==-1
print(json.dumps({'exact_A_PSD_rank':rA,'exact_B_PSD_rank':rB,'star_Schur_PSD':True,
 'matching_Schur_PSD':True,'star_minus_matching_entrywise_nonnegative':True,
 'nonzero_star_deficit':str(-R[0][1]),'W_negative_test':str(wI),'W_PT_negative_test':str(wpt),
 '2block_positivity':'written as baseline rank-two trace bound plus nonnegative diagonal increments'},indent=2))
