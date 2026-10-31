#!/usr/bin/env python3
"""Exact source rank4, PPT and completely-entangled-range checks for Q."""
import json
N=4;zero={};one={(0,0,0,0):1}
def var(i):
 k=[0]*N;k[i]=1;return {tuple(k):1}
def add(a,b):
 c=dict(a)
 for k,v in b.items():c[k]=c.get(k,0)+v
 return {k:v for k,v in c.items() if v}
def neg(a):return {k:-v for k,v in a.items()}
def mul(a,b):
 c={}
 for x,u in a.items():
  for y,v in b.items():
   k=tuple(i+j for i,j in zip(x,y));c[k]=c.get(k,0)+u*v
 return {k:v for k,v in c.items() if v}
def minor(M,r0,r1,c0,c1):return add(mul(M[r0][c0],M[r1][c1]),neg(mul(M[r0][c1],M[r1][c0])))
def drop(p,idx):return {k:v for k,v in p.items() if all(k[i]==0 for i in idx)}
a,b,c,d=(var(i) for i in range(4));M=((a,b,c),(c,zero,d),(d,a,b))
assert minor(M,0,1,0,1)==neg(mul(b,c))
assert minor(M,0,1,1,2)==mul(b,d)
assert minor(M,1,2,0,1)==mul(a,c)
assert minor(M,1,2,1,2)==neg(mul(a,d))
assert drop(minor(M,0,2,0,1),(2,3))==mul(a,a)
assert drop(minor(M,0,2,1,2),(2,3))==mul(b,b)
assert drop(minor(M,0,1,0,2),(0,1))==neg(mul(c,c))
assert drop(minor(M,1,2,0,2),(0,1))==neg(mul(d,d))
edges=(((1,0),(0,2)),((2,0),(1,2)),((0,0),(2,1)),((0,1),(2,2)))
flip=(((1,2),(0,0)),((2,2),(1,0)),((0,1),(2,0)),((0,2),(2,1)))
def matrix(es):
 m=[[0]*9 for _ in range(9)]
 for edge in es:
  v=[0]*9
  for i,j in edge:v[3*i+j]+=1
  for i in range(9):
   for j in range(9):m[i][j]+=v[i]*v[j]
 return m
support=[p for e in edges for p in e];assert len(support)==len(set(support))==8
rho=matrix(edges);pt=[[rho[3*(i//3)+j%3][3*(j//3)+i%3] for j in range(9)] for i in range(9)]
assert pt==matrix(flip) and sum(rho[i][i] for i in range(9))==8
print(json.dumps({'source_rank':4,'source_trace':8,'pt_entries_checked':81,
 'monomial_minors':4,'branch_square_minors':4,'range_no_product_vectors':True,
 'limits':'Source tensor SN4 uses the separately cited Chen-Yang-Tang lemma.'},indent=2))
