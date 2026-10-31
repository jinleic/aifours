#!/usr/bin/env python3
"""Exact non-PSD, non-coPSD member of the matching-symmetric witness family."""
from fractions import Fraction as F
import json
n=16
def v(*terms):
 x=[F(0)]*n
 for i,j,c in terms:x[4*i+j]+=F(c)
 return x
def add(M,a,x):
 for i in range(n):
  for j in range(n):M[i][j]+=a*x[i]*x[j]
def pt(M):return [[M[4*(i//4)+j%4][4*(j//4)+i%4] for j in range(n)] for i in range(n)]
def quadratic(M,x):return sum(x[i]*M[i][j]*x[j] for i in range(n) for j in range(n))
def psd(M):
 x=[r[:] for r in M];rank=0
 while x:
  if any(x[i][i]<0 for i in range(len(x))):return None
  p=next((i for i in range(len(x)) if x[i][i]>0),None)
  if p is None:return rank if all(z==0 for row in x for z in row) else None
  q=x[p][p];R=[i for i in range(len(x)) if i!=p]
  x=[[x[i][j]-x[i][p]*x[p][j]/q for j in R] for i in R];rank+=1
 return rank
I=v((0,0,1),(1,1,1),(2,2,1),(3,3,1))
W=[[F(int(i==j),2) for j in range(n)] for i in range(n)]
A=[[F(0) for _ in range(n)] for _ in range(n)]
B=[[F(0) for _ in range(n)] for _ in range(n)]
for i in range(4):
 e=v((i,i,1));add(W,F(3),e);add(A,F(3),e)
add(W,-F(1),I);add(A,-F(1,2),I)
for i in range(4):
 for j in range(i+1,4):add(B,F(1,2),v((i,j,1),(j,i,-1)))
Bg=pt(B)
assert all(W[i][j]==A[i][j]+Bg[i][j] for i in range(n) for j in range(n))
a,b=psd(A),psd(B);assert a==4 and b==6
x=v((0,1,1),(1,0,1));wx=quadratic(W,I);wpt=quadratic(pt(W),x)
assert wx==-2 and wpt==-1
print(json.dumps({'decomposition_exact_entries':n*n,'PSD_A_rank':a,'PSD_B_rank':b,
 'W_test_negative':str(wx),'W_partial_transpose_test_negative':str(wpt),
 'SR2_validity':'written trace inequalities, not this finite test'},indent=2))
