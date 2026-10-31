#!/usr/bin/env python3
"""Exact Laurent-phase product decompositions of six 2x3 crosshatch cuts."""
from itertools import combinations
import json
edges=(((1,0),(0,2)),((2,0),(1,2)),((0,0),(2,1)),((0,1),(2,2)))
def outer(m,v):
 for i,x in enumerate(v):
  for j,y in enumerate(v):m[i][j]+=x*y
def addp(a,b):
 c=dict(a)
 for k,v in b.items():c[k]=c.get(k,0)+v
 return {k:v for k,v in c.items() if v}
def negp(a):return {k:-v for k,v in a.items()}
def mulp(a,b):
 c={}
 for i,x in a.items():
  for j,y in b.items():c[i+j]=c.get(i+j,0)+x*y
 return {k:v for k,v in c.items() if v}
# factors are (basis-index, power of z); last list is untouched product ket(s).
cases=(
 ('alice',0,3,((1,0),(2,1)),((0,0),(2,1)),((2,1),)),
 ('alice',1,4,((0,0),(2,1)),((0,1),(1,0),(2,-1)),()),
 ('alice',2,3,((0,0),(1,1)),((0,0),(2,1)),((0,1),)),
 ('bob',0,3,((0,0),(2,-1)),((1,0),(2,1)),((1,2),)),
 ('bob',1,4,((0,0),(1,1),(2,2)),((0,0),(2,1)),()),
 ('bob',2,3,((0,0),(2,-1)),((0,0),(1,1)),((1,0),)),
)
results=[]
for side,deleted,N,left,right,remaining in cases:
 target=[[0]*9 for _ in range(9)]
 for edge in edges:
  v=[0]*9
  for a,b in edge:
   if (a if side=='alice' else b)!=deleted:v[3*a+b]+=1
  outer(target,v)
 p=[[{} for _ in range(3)] for _ in range(3)];groups={}
 for a,da in left:
  for b,db in right:
   d=da+db;p[a][b]=addp(p[a][b],{d:1});groups.setdefault(d,[0]*9)[3*a+b]+=1
 assert len({d%N for d in groups})==len(groups)
 minors=0
 for rr in combinations(range(3),2):
  for cc in combinations(range(3),2):
   a,b=rr;x,y=cc
   assert not addp(mulp(p[a][x],p[b][y]),negp(mulp(p[a][y],p[b][x])));minors+=1
 actual=[[0]*9 for _ in range(9)]
 for q in groups.values():outer(actual,q)
 for a,b in remaining:
  v=[0]*9;v[3*a+b]=1;outer(actual,v)
 assert actual==target
 results.append({'side':side,'deleted':deleted,'phase_order':N,'product_minors':minors,'entries_checked':81})
print(json.dumps({'cases':results,'all_cases':6,'total_minor_polynomials':54,
 'total_matrix_entries_checked':486,'limits':'Proves six one-copy cuts separable; arbitrary rank2 maps use the separately cited 2x3 PPT separability theorem.'},indent=2))
