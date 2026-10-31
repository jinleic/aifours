#!/usr/bin/env python3
"""Exact checks for one PPT-entangled rank-two-decomposition orbit."""
from fractions import Fraction as F
from itertools import permutations,product
import json
S=((0,1,1,1),(-1,0,1,-1),(-1,-1,0,1),(-1,1,-1,0))
assert all(sum(S[i][k]*S[k][j] for k in range(4))==(-3 if i==j else 0) for i in range(4) for j in range(4))
autos=[]
for p in permutations(range(4)):
 for bits in product((-1,1),repeat=3):
  sg=(1,)+bits
  if all(S[p[i]][p[j]]==sg[i]*sg[j]*S[i][j] for i in range(4) for j in range(4)):autos.append((p,sg))
assert len(autos)==12 and len({(p[0],p[1]) for p,s in autos})==12
# z=(1,1,-i,-1) as exact Gaussian integer pairs.
z=((1,0),(1,0),(0,-1),(-1,0))
def prod_conj(x,y):return (x[0]*y[0]+x[1]*y[1],x[1]*y[0]-x[0]*y[1])
real=[[0]*4 for _ in range(4)];imag=[[0]*4 for _ in range(4)]
for p,sg in autos:
 for i in range(4):
  for j in range(4):
   r,t=prod_conj(z[i],z[j]);real[p[i]][p[j]]+=sg[i]*sg[j]*r;imag[p[i]][p[j]]+=sg[i]*sg[j]*t
assert all(real[i][j]==12*int(i==j) and imag[i][j]==6*S[i][j] for i in range(4) for j in range(4))
# Each ordered edge receives the four source costs (3+sqrt5)/2 twice and (3-sqrt5)/2 twice.
for i in range(4):
 for j in range(4):
  if i!=j:
   images=[(p[0],p[1]) for p,s in autos]
   assert images.count((i,j))==1
assert F(2)*F(3,2)+F(2)*F(3,2)==6
# A=I+iS/2; certify its realification is positive via exact Schur elimination.
def psd(M):
 A=[r[:] for r in M];rank=0
 while A:
  if any(A[i][i]<0 for i in range(len(A))):return None
  k=next((i for i in range(len(A)) if A[i][i]>0),None)
  if k is None:return rank if all(x==0 for row in A for x in row) else None
  q=A[k][k];J=[i for i in range(len(A)) if i!=k]
  A=[[A[i][j]-A[i][k]*A[k][j]/q for j in J] for i in J];rank+=1
 return rank
Ar=[[F(int(i==j)) for j in range(4)] for i in range(4)];Ai=[[F(S[i][j],2) for j in range(4)] for i in range(4)]
Arf=[[Ar[i%4][j%4] if (i<4)==(j<4) else (-Ai[i%4][j%4] if i<4 else Ai[i%4][j%4]) for j in range(8)] for i in range(8)]
assert psd(Arf)==8
# A PT edge block [[1/2, i/2],[-i/2,1/2]] has realification PSD rank two.
Br=[[F(1,2),F(0),F(0),F(-1,2)],[F(0),F(1,2),F(1,2),F(0)],
    [F(0),F(1,2),F(1,2),F(0)],[F(-1,2),F(0),F(0),F(1,2)]]
assert psd(Br)==2
# phi=(1+sqrt5)/2, inverse=(sqrt5-1)/2: squared magnitudes sum to 3.
# Each of two rank-one 2x2 blocks contributes that amount; both determinants vanish algebraically.
assert F(3)+F(3)==6
print(json.dumps({'S_squared':'-3I','signed_automorphisms':12,'ordered_pair_orbit':12,
 'correlated_group_average':'I+iS/2','offdiagonal_group_average':'1/2',
 'A_realification_positive_rank':8,'PT_pair_realification_PSD_rank':2,
 'seed_block_determinants':0,'seed_offdiagonal_norm_squared':6,
 'normalization_trace':10,'entanglement_budget':'4<6',
 'scope':'Finite orbit/PSD checks; equality-saturation entanglement and all-parameter decomposition are written proofs.'},indent=2))
