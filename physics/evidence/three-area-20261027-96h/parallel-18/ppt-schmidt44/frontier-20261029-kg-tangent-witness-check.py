#!/usr/bin/env python3
"""Exact tangent path and torus weights for the 4x5 KG source."""
from fractions import Fraction as F
from itertools import combinations,permutations
import json

A={(0,0):1,(1,1):1,(2,2):1};B={(0,1):1,(1,2):1};D={(1,0):1,(2,1):-1}
C={(0,2):1,(3,4):1};E={(2,0):1,(3,3):1};G={(3,0):1};I={(3,2):1}
Z={(0,3):1,(0,4):1,(2,3):1,(2,4):1}
def add(*terms):
 out={}
 for v in terms:
  for ij,c in v.items():out[ij]=out.get(ij,0)+c
 return {ij:c for ij,c in out.items() if c}
U=add(G,I);V=add(A,C,E)
# X(t)=U+tV+t^2Z is the sum of two rank-one matrices:
# (e3+t(e0+e2)) (e0+e2+t(e3+e4))^T + t e1 e1^T.
assert U=={(3,0):1,(3,2):1}
assert V=={(0,0):1,(1,1):1,(2,2):1,(0,2):1,(3,4):1,(2,0):1,(3,3):1}
# Verify all forty 3x3 minors vanish as integer polynomials in t.
def pmul(x,y):
 z=[0]*(len(x)+len(y)-1)
 for i,a in enumerate(x):
  for j,b in enumerate(y):z[i+j]+=a*b
 return z
def padd(x,y,s=1):
 z=[0]*max(len(x),len(y))
 for i,a in enumerate(x):z[i]+=a
 for i,a in enumerate(y):z[i]+=s*a
 return z
def det_poly(rows,cols):
 out=[0]*7
 for p in permutations(range(3)):
  inv=sum(p[i]>p[j] for i in range(3) for j in range(i+1,3));term=[1]
  for i in range(3):
   ij=(rows[i],cols[p[i]]);term=pmul(term,[U.get(ij,0),V.get(ij,0),Z.get(ij,0)])
  out=padd(out,term,-1 if inv%2 else 1)
 return out
count=0
for rows in combinations(range(4),3):
 for cols in combinations(range(5),3):
  assert not any(det_poly(rows,cols));count+=1
fa=((0,0),(1,0),(2,0),(0,1));gb=((0,0),(-1,0),(-2,0),(2,-1),(-2,-1))
def weights(v):return {(fa[a][0]+gb[b][0],fa[a][1]+gb[b][1]) for a,b in v}
assert weights(U).isdisjoint(weights(V)) and weights(U).isdisjoint(weights(Z)) and weights(V).isdisjoint(weights(Z))
assert len(weights(U))==2 and len(weights(V))==3 and len(weights(Z))==4
# P_ker R kills U,V and its action on Z keeps only |03>,|24>.
source=[A,B,D,C,E,{(2,3):1},G,I,{(0,4):1}]
for x,y in combinations(source,2):assert sum(c*y.get(ij,0) for ij,c in x.items())==0
norms=[sum(c*c for c in x.values()) for x in source]
def dot(x,y):return sum(c*y.get(ij,0) for ij,c in x.items())
assert dot(A,V)==3 and dot(B,U)==dot(B,V)==dot(B,Z)==0 and dot(D,U)==dot(D,V)==dot(D,Z)==0
proj_norm=sum(F(dot(Z,v)**2,n) for v,n in zip(source,norms));ker_norm=F(sum(c*c for c in Z.values()))-proj_norm
assert ker_norm==2
alpha=eps=F(1,100);t=F(1,10)
path_value=ker_norm*t**4-eps*9*t**2;pairing=8*alpha-9*eps
assert path_value==F(-7,10000) and pairing==F(-1,100)
print(json.dumps({'vanishing_minor_polynomials':count,'distinct_torus_character_counts':[2,3,4],
 'source_generators_mutually_orthogonal':True,'kernel_Z_norm_squared':str(ker_norm),
 'naive_ansatz_alpha_epsilon':'1/100','rank2_test_t':'1/10',
 'naive_ansatz_SR2_expectation':str(path_value),'naive_ansatz_source_pairing':str(pairing),
 'scope':'Exact integer/Fraction arithmetic; general SOC bound uses written torus and quadratic reasoning.'},indent=2))
