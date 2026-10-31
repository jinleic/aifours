#!/usr/bin/env python3
"""Exact source pairing and SOS input for an UNVERIFIED KG witness candidate.

The candidate is NOT certified 2-block-positive. --emit-w prints sparse upper
triangle entries suitable for the separate SOS verifier, but no SOS identity.
"""
from fractions import Fraction as F
import argparse,json
n=20
def ket(*terms):
 v=[0]*n
 for a,b,c in terms:v[5*a+b]+=c
 return v
A=ket((0,0,1),(1,1,1),(2,2,1));B=ket((0,1,1),(1,2,1));D=ket((1,0,1),(2,1,-1));C=ket((0,2,1),(3,4,1));E=ket((2,0,1),(3,3,1));G=ket((3,0,1));I=ket((3,2,1));FF=ket((2,3,1));H=ket((0,4,1))
vecs=[A,B,D,C,E,FF,G,I,H];weights=[1,1,1,3,3,3,3,3,3]
for i in range(9):
 for j in range(i):assert sum(x*y for x,y in zip(vecs[i],vecs[j]))==0
norms=[sum(x*x for x in v) for v in vecs]
def add_outer(M,v,coef):
 for i in range(n):
  for j in range(n):M[i][j]+=coef*v[i]*v[j]
PK=[[F(i==j) for j in range(n)] for i in range(n)]
for v,norm in zip(vecs,norms):add_outer(PK,v,-F(1,norm))
W=[[F(300)*PK[i][j]+F(3,100)*int(i==j) for j in range(n)] for i in range(n)]
for v in (B,D,G,I):add_outer(W,v,F(3,10))
add_outer(W,A,-F(3,5))
def pair(W,v):return sum(F(v[i])*W[i][j]*v[j] for i in range(n) for j in range(n))
trace=sum(F(w)*pair(W,v) for w,v in zip(weights,vecs))
assert trace==F(-27,100) and pair(W,A)==F(-531,100)
# Exact T^2 characters for the source basis.
fa=((0,0),(1,0),(2,0),(0,1));gb=((0,0),(-1,0),(-2,0),(2,-1),(-2,-1))
chars=[(fa[a][0]+gb[b][0],fa[a][1]+gb[b][1]) for a in range(4) for b in range(5)]
assert all(W[i][j]==0 or chars[i]==chars[j] for i in range(n) for j in range(n))
p=argparse.ArgumentParser();p.add_argument('--emit-w',action='store_true');args=p.parse_args()
if args.emit_w:
 print(json.dumps({'w':[[i,j,str(W[i][j]),'0'] for i in range(n) for j in range(i,n) if W[i][j]],
                   'note':'Append an actually verified SOS identity; this matrix alone is NOT a 2-block-positivity certificate.'},indent=2))
else:
 print(json.dumps({'trace_W_R':str(trace),'A_negative_test':str(pair(W,A)),'T2_invariant':True,
                   'source_generator_norms_squared':norms,'status':'2-block positivity NOT CERTIFIED; no target result'},indent=2))
