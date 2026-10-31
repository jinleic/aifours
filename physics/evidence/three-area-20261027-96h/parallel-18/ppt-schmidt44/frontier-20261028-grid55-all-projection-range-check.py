#!/usr/bin/env python3
"""Polynomial check of rank2 range vectors on both full tail charts."""
from itertools import combinations
import json
N=4
ZERO=(0,)*N
one={ZERO:1};zero={}
def var(i):
 e=[0]*N;e[i]=1;return {tuple(e):1}
def add(a,b):
 c=dict(a)
 for k,v in b.items():c[k]=c.get(k,0)+v
 return {k:v for k,v in c.items() if v}
def neg(a):return {k:-v for k,v in a.items()}
def sub(a,b):return add(a,neg(b))
def mul(a,b):
 c={}
 for x,u in a.items():
  for y,v in b.items():
   k=tuple(i+j for i,j in zip(x,y));c[k]=c.get(k,0)+u*v
 return {k:v for k,v in c.items() if v}
def scale(a,n):return {k:v*n for k,v in a.items() if v*n}
v0,v1,v2,lam=(var(i) for i in range(4))
def ket(*coords):
 m=[[{} for _ in range(5)] for _ in range(5)]
 for a,b in coords:m[a][b]=add(m[a][b],one)
 return m
A=ket((0,2),(1,1),(2,0));U=ket((0,0));V=ket((0,1));W=ket((1,0))
C=ket((2,1),(4,3));Q=ket((2,2),(3,3));J=ket((2,3))
def linear(terms):
 m=[[{} for _ in range(5)] for _ in range(5)]
 for c,k in terms:
  for i in range(5):
   for j in range(5):m[i][j]=add(m[i][j],mul(c,k[i][j]))
 return m
def project(m,fold):
 out=[[{} for _ in range(5)] for _ in range(4)]
 for i in range(5):
  if i==fold:
   for a,c in enumerate((v0,v1,v2,lam)):
    for b in range(5):out[a][b]=add(out[a][b],mul(c,m[i][b]))
  else:
   a=i if i<fold else i-1
   for b in range(5):out[a][b]=add(out[a][b],m[i][b])
 return out
def det(m,rr,cc):
 a,b,c=rr;x,y,z=cc
 return add(sub(mul(m[a][x],sub(mul(m[b][y],m[c][z]),mul(m[b][z],m[c][y]))),
                mul(m[a][y],sub(mul(m[b][x],m[c][z]),mul(m[b][z],m[c][x])))),
            mul(m[a][z],sub(mul(m[b][x],m[c][y]),mul(m[b][y],m[c][x]))))
def assert_minors(m):
 count=0
 for rr in combinations(range(4),3):
  for cc in combinations(range(5),3):
   assert not det(m,rr,cc);count+=1
 return count
def lambda_zero(m):
 return [[{k:v for k,v in x.items() if k[3]==0} for x in row] for row in m]
q4=linear(((lam,A),(lam,U),(neg(one),V),(neg(one),C),(lam,Q),(sub(v2,v0),J)))
m4=project(q4,4)
assert m4[0]==m4[2] and all(not p for p in m4[3])
assert m4[0]==[lam,neg(one),lam,neg(v0),zero]
q40=linear(((one,A),(one,W),(one,C),(sub(v1,v2),J)))
m40=lambda_zero(project(q40,4))
assert m40[1]==m40[2] and all(not p for p in m40[3])
assert m40[0]==[zero,zero,one,v0,zero]
q3=linear(((one,A),(one,U),(neg(lam),V),(neg(lam),C),(one,Q),(sub(v0,v2),J)))
m3=project(q3,3)
assert m3[0]==m3[2] and all(not p for p in m3[3])
assert m3[0]==[one,neg(lam),one,v0,zero]
print(json.dumps({'variables':['v0','v1','v2','lambda'],'chart4_lambda_nonzero_minors':assert_minors(m4),
 'chart4_lambda_zero_minors':assert_minors(m40),'chart3_all_lambda_minors':assert_minors(m3),
 'explicit_row_equalities_checked':True,'integer_polynomial_arithmetic':True,
 'anchor_coefficients':['lambda','1','1'],
 'limits':'Proves each displayed vector has rank<=2; source range span follows because every other grid generator has rank<=2. It does not prove the state has SN<=2.'},indent=2))
