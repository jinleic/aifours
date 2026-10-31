#!/usr/bin/env python3
"""Exact star decomposition with a rank-two correlated negative matrix."""
from fractions import Fraction as F
import json
n=16
def zero(m):return [[F(0) for _ in range(m)] for _ in range(m)]
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
d=zero(4)
for i,t in enumerate((F(7,2),F(18,5),F(37,10),F(19,5))):d[i][i]=t+F(1,50)
for i in range(1,4):d[0][i]=d[i][0]=F(13,25)
for i,j,x in ((1,2,F(107,100)),(1,3,F(101,50)),(2,3,F(151,50))):d[i][j]=d[j][i]=x
v=(1,1,0,0);K=[[F(1)+F(v[i]*v[j],100) for j in range(4)] for i in range(4)]
assert psd(K)==2
W=zero(n)
for i in range(4):
 for j in range(4):W[4*i+j][4*i+j]+=d[i][j];W[5*i][5*j]-=K[i][j]
a=[d[i][i]-K[i][i] for i in range(4)];b=[None]+[K[0][i]-d[0][i] for i in range(1,4)]
B=zero(n)
for i in range(4):
 for j in range(i+1,4):
  q=d[i][j];c=q if i==0 else min(q,K[i][j]+b[i]*b[j]/a[0]);p=4*i+j;k=4*j+i
  B[p][p]+=c;B[k][k]+=c;B[p][k]-=c;B[k][p]-=c
BG=pt(B);A=[[W[i][j]-BG[i][j] for j in range(n)] for i in range(n)]
ra,rb=psd(A),psd(B);assert ra is not None and rb is not None
H=[[A[5*i][5*j] for j in range(4)] for i in range(4)]
R=[[H[i][j]-H[i][0]*H[0][j]/a[0] for j in range(1,4)] for i in range(1,4)]
# Matching {0,3},{1,2}: its matching Schur block C.
assert d[1][2]-K[1][2]<=K[0][1]*K[0][2]/a[0]
M=[[a[i] if i==j else -K[i][j] for j in range(4)] for i in range(4)]
M[0][3]=M[3][0]=-b[3];M[1][2]=M[2][1]=d[1][2]-K[1][2]
C=[[M[i][j]-M[i][0]*M[0][j]/a[0] for j in range(1,4)] for i in range(1,4)]
assert psd(R) is not None and psd(C) is not None and all(R[i][j]>=C[i][j] for i in range(3) for j in range(3))
assert R[0][1]<0
wI=sum(W[5*i][5*j] for i in range(4) for j in range(4));T=pt(W);wpt=T[2][2]+T[2][8]+T[8][2]+T[8][8]
assert wI==F(-34,25) and wpt==F(-24,25)
print(json.dumps({'correlated_K_rank':2,'A_PSD_rank':ra,'B_PSD_rank':rb,'star_Schur_PSD':True,
 'matching_Schur_PSD':True,'R_minus_C_entrywise_nonnegative':True,'nonzero_star_deficit':str(-R[0][1]),
 'W_negative_test':str(wI),'W_partial_transpose_negative_test':str(wpt),
 '2block_positivity':'written: previous 2-block-positive star example plus PSD (2I-[00+11])/100'},indent=2))
