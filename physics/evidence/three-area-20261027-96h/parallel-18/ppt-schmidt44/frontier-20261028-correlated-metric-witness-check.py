#!/usr/bin/env python3
"""Exact singular product-metric, rank3 correlated subtraction example."""
from fractions import Fraction as F
import json
D=16;A=(1,4,0,9);B=(4,0,9,1);S1=(1,2,0,3);S2=(2,0,3,1);idx=(0,6,15)
C=((F(1),F(1,2),F(0)),(F(1,2),F(1),F(1,2)),(F(0),F(1,2),F(1)))
def psd(m):
 a=[list(row) for row in m];piv=[]
 while a:
  if any(a[i][i]<0 for i in range(len(a))):return None
  p=next((i for i in range(len(a)) if a[i][i]>0),None)
  if p is None:return piv if all(x==0 for row in a for x in row) else None
  s=a[p][p];piv.append(s);r=[j for j in range(len(a)) if j!=p]
  a=[[a[i][j]-a[i][p]*a[p][j]/s for j in r] for i in r]
 return piv
assert psd(C)==[F(1),F(3,4),F(2,3)]
Y=[[F(0) for _ in range(D)] for _ in range(D)]
for i,a in enumerate(idx):
 for j,b in enumerate(idx):Y[a][b]=C[i][j]
W=[[F(int(i==j)*A[i//4]*B[i%4])-F(S1[i//4]*S2[i%4]*S1[j//4]*S2[j%4])*Y[i][j]
    for j in range(D)] for i in range(D)]
PT=[[W[4*(i//4)+j%4][4*(j//4)+i%4] for j in range(D)] for i in range(D)]
piv=psd(PT);assert piv is not None
x=[F(0)]*D;x[0]=F(1,2);x[6]=F(1,3);x[15]=F(1,3)
val=sum(x[i]*W[i][j]*x[j] for i in range(D) for j in range(D));assert val==-4
y=[F(0)]*D;y[0]=F(1,2);y[6]=F(1,6)
val2=sum(y[i]*W[i][j]*y[j] for i in range(D) for j in range(D));assert val2==-1
print(json.dumps({'C_positive_pivots':list(map(str,psd(C))),'correlated_rank':3,
 'W_pt_pivots':list(map(str,piv)),'non_psd_test':'-4','rank2_negative_test':'-1',
 'matrix_entries_checked':256,'limits':'Universal correlated-metric coCP result is the written proof; this example is not 2-block-positive.'},indent=2))
