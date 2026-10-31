#!/usr/bin/env python3
"""Exact CH⊗CH identity cut and noncoordinate perturbation checks."""
from fractions import Fraction as F
from itertools import product
import json
edges=(((1,0),(0,2)),((2,0),(1,2)),((0,0),(2,1)),((0,1),(2,2)))
coords=[tuple((3*a+c,3*b+d) for (a,b),(c,d) in product(x,y)) for x,y in product(edges,repeat=2)]
allcoords=[x for q in coords for x in q]
assert len(coords)==16 and all(len(q)==4 for q in coords)
assert len(allcoords)==len(set(allcoords))==64
# Orthogonal kets have norm squared4; source Frobenius norm squared=16*4^2.
assert sum(len(q)**2 for q in coords)==256
S=(0,2,6,8)
def base():
 K=[[F(0) for _ in range(9)] for _ in range(4)]
 for i,j in enumerate(S):K[i][j]=1
 return K
def output(K,L):
 R=[[F(0) for _ in range(16)] for _ in range(16)]
 for q in coords:
  v=[F(0)]*16
  for a,b in q:
   for i in range(4):
    for j in range(4):v[4*i+j]+=K[i][a]*L[j][b]
  for i,x in enumerate(v):
   for j,y in enumerate(v):R[i][j]+=x*y
 return R
def rank(A):
 a=[row[:] for row in A];r=0
 for j in range(len(a[0])):
  piv=next((i for i in range(r,len(a)) if a[i][j]),None)
  if piv is None:continue
  a[r],a[piv]=a[piv],a[r];s=a[r][j]
  for i in range(r+1,len(a)):
   t=a[i][j]/s
   for k in range(j,len(a[0])):a[i][k]-=t*a[r][k]
  r+=1
  if r==len(a):break
 return r
def slice_ranks(K):
 # stack K(v⊗e_j) and K(e_j⊗v), linear in v.
 first=[[K[o][3*i+j] for i in range(3)] for o in range(4) for j in range(3)]
 second=[[K[o][3*j+i] for i in range(3)] for o in range(4) for j in range(3)]
 return rank(first),rank(second)
P=base();baseline=output(P,P)
assert baseline==[[int(i==j) for j in range(16)] for i in range(16)]
K=base();L=base();eps=F(1,1000);K[0][4]=eps;L[1][4]=eps
R=output(K,L);dist=sum((R[i][j]-int(i==j))**2 for i in range(16) for j in range(16))
assert dist<1 and rank(K)==rank(L)==4 and slice_ranks(K)==slice_ranks(L)==(3,3)
delta=F(1,72);e=2*delta+delta*delta;bound=16*(2*e+e*e);assert bound<1
print(json.dumps({'baseline_is_identity':True,'source_Frobenius_norm':16,
 'uniform_filter_Frobenius_radius':str(delta),'uniform_output_distance_bound':str(bound),
 'example_epsilon':str(eps),'example_distance_squared':str(dist),'both_filter_ranks':4,
 'example_A_slice_constraint_ranks':slice_ranks(K),'example_B_slice_constraint_ranks':slice_ranks(L),
 'limits':'Separable follows from the explicitly imported Gurvits-Barnum identity-ball theorem.'},indent=2))
