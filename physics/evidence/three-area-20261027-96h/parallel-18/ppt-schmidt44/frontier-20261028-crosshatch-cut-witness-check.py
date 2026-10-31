#!/usr/bin/env python3
"""Exact trace-14 PPT/SN2 crosshatch tensor cut and product-valid witness."""
from fractions import Fraction as F
from itertools import product
import json
D=16;Z0=F(0)
def vec(*pairs):
 v=[0]*D
 for a,b in pairs:v[4*a+b]+=1
 return v
def outer(m,v):
 for i,x in enumerate(v):
  for j,y in enumerate(v):m[i][j]+=x*y
def mm(a,b):return [[sum(a[i][k]*b[k][j] for k in range(D)) for j in range(D)] for i in range(D)]
def trans(a):return [list(x) for x in zip(*a)]
def tracepair(a,b):return sum(a[i][j]*b[j][i] for i in range(D) for j in range(D))
orig=(((1,0),(0,2)),((2,0),(1,2)),((0,0),(2,1)),((0,1),(2,2)))
AA=(0,2,5,7);BB=(0,1,5,6);rho=[[0]*D for _ in range(D)];counts=[]
for left,right in product(orig,repeat=2):
 v=[0]*D
 for (a,b),(c,d) in product(left,right):
  A,B=3*a+c,3*b+d
  if A in AA and B in BB:v[4*AA.index(A)+BB.index(B)]+=1
 counts.append(sum(v));outer(rho,v)
assert counts==[0,2,2,0,1,1,0,0,0,2,2,1,2,0,0,1]
components=(vec((2,0),(1,3)),vec((2,1),(0,3)),vec((3,0)),vec((2,3)),
 vec((1,0),(3,2)),vec((0,0),(1,1)),vec((0,1)),vec((0,2),(3,3)),vec((1,2)))
assert len(components)==9
actual=[[0]*D for _ in range(D)]
for v in components:outer(actual,v)
assert actual==rho and sum(rho[i][i] for i in range(D))==14
pt=[[rho[4*(i//4)+j%4][4*(j//4)+i%4] for j in range(D)] for i in range(D)]
pt_terms=(vec((2,3),(1,0),(0,1)),vec((1,2),(3,0)),vec((0,3),(3,2)),
 vec((2,0)),vec((1,3)),vec((2,1)),vec((0,0)),vec((1,1)),vec((0,2)),vec((3,3)))
expected=[[0]*D for _ in range(D)]
for v in pt_terms:outer(expected,v)
assert expected==pt
# A rational operator-norm-one dual to realignment. Main 4x4 block is a partial isometry.
idx=(0,5,10,15);Y=((3,4,4,3),(3,4,4,3),(4,2,-8,4),(4,-8,2,4))
Z=[[Z0 for _ in range(D)] for _ in range(D)]
for i,a in enumerate(idx):
 for j,b in enumerate(idx):Z[a][b]=F(Y[i][j],10)
for i,j in ((1,1),(2,13),(3,11),(4,4),(6,12),(7,2),(8,7),(9,3),(12,14),(13,8)):Z[i][j]=F(1)
P=mm(Z,trans(Z));assert P==trans(P) and mm(P,P)==P and any(P[i][i] for i in range(D))
# Realignment inverse: R(X)_(a,c),(b,d)=X_(a,b),(c,d).
C=[[F(Z[4*(i//4)+j//4][4*(i%4)+j%4]+Z[4*(j//4)+i//4][4*(j%4)+i%4],2)
    for j in range(D)] for i in range(D)]
assert C==trans(C)
W=[[F(int(i==j))-C[i][j] for j in range(D)] for i in range(D)]
w=tracepair(W,rho);assert w==F(-4,5)
negative=vec((0,2),(3,3));negval=sum(negative[i]*W[i][j]*negative[j] for i in range(D) for j in range(D))
assert negval==F(-4,5)
print(json.dumps({'alice_input_indices':AA,'bob_input_indices':BB,'rho_trace':14,
 'rank2_source_kets':5,'product_source_kets':4,'source_projection_entries':256,
 'pt_projector_terms':10,'pt_entries_checked':256,'Z_Zt_orthogonal_projection':True,
 'witness_trace_unnormalized':str(w),'witness_trace_normalized':str(w/14),
 'rank2_negative_ket':'|02>+|33>','rank2_negative_value':str(negval),
 'limits':'W witnesses entanglement only and is explicitly NOT 2-block-positive.'},indent=2))
