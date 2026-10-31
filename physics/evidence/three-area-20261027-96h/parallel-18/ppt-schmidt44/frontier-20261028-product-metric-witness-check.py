#!/usr/bin/env python3
"""Exact singular-metric, 2-block-positive but coCP witness example."""
from fractions import Fraction as F
import json
D=16;A=(1,4,0,9);B=(4,0,9,1);S1=(1,2,0,3);S2=(2,0,3,1)
phi=[F(0)]*D;phi[0]=F(4,5);phi[6]=F(3,5);phi[15]=F(1,2)
psi=[F(S1[i//4]*S2[i%4])*phi[i] for i in range(D)]
assert psi[0]==F(8,5) and psi[6]==F(18,5) and psi[15]==F(3,2)
W=[[F(int(i==j)*A[i//4]*B[i%4])-psi[i]*psi[j] for j in range(D)] for i in range(D)]
PT=[[W[4*(i//4)+j%4][4*(j//4)+i%4] for j in range(D)] for i in range(D)]
def psd(m):
 a=[row[:] for row in m];piv=[]
 while a:
  if any(a[i][i]<0 for i in range(len(a))):return None
  p=next((i for i in range(len(a)) if a[i][i]>0),None)
  if p is None:return piv if all(x==0 for row in a for x in row) else None
  s=a[p][p];piv.append(s);r=[j for j in range(len(a)) if j!=p]
  a=[[a[i][j]-a[i][p]*a[p][j]/s for j in r] for i in r]
 return piv
piv=psd(PT);assert piv is not None
x=[F(0)]*D;x[0]=F(2,5);x[6]=F(1,10);x[15]=F(1,6)
negative=sum(x[i]*W[i][j]*x[j] for i in range(D) for j in range(D))
assert negative==F(-5,16)
assert phi[0]**2+phi[6]**2==1 and sum(t*t for t in phi)==F(5,4)
print(json.dumps({'A':A,'B':B,'phi_coefficients':['4/5','3/5','1/2'],
 'two_largest_schmidt_squares_sum':'1','phi_squared_norm':'5/4',
 'W_pt_nonnegative_schur_pivots':list(map(str,piv)),'W_non_psd_test':'-5/16',
 'matrix_entries_checked':256,'limits':'Universal coCP conclusion follows from the written Schmidt/eigenvalue proof.'},indent=2))
