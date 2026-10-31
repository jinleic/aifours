#!/usr/bin/env python3
"""Exact compatible triple-rectangle q18 search; detect nonbinary gauge masks."""
from itertools import combinations
from pathlib import Path
import json
P=Path(__file__).resolve().parent
lines=(P/'frontier-20261028-aalto-bh10-6-catalog-v1.txt').read_text().splitlines()
fams=json.loads((P/'frontier-20261028-bh6-rectangle-families-v1.json').read_text())['records'];six=[(1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1)]
def zero6(v):return all(sum(six[x%6][j] for x in v)==0 for j in range(2))
def mask(f):return [[int(t in f['rows'] and c in f['columns']) for c in range(10)] for t in range(10)]
def rank3(M):
 v=[[x[r][c]-x[r][0]-x[0][c]+x[0][0] for r in range(1,10) for c in range(1,10)] for x in M]
 for i,j in combinations(range(81),2):
  d=v[0][i]*v[1][j]-v[0][j]*v[1][i]
  if d:
   return any(d*v[2][k]-(v[2][i]*v[1][j]-v[2][j]*v[1][i])*v[0][k]-(v[0][i]*v[2][j]-v[0][j]*v[2][i])*v[1][k] for k in range(81))
 return False
def compatible(H,M):
 for r,s in combinations(range(10),2):
  groups={}
  for c in range(10):groups.setdefault(tuple(x[r][c]-x[s][c] for x in M),[]).append(H[r][c]-H[s][c])
  if not all(zero6(v) for v in groups.values()):return False
 return True
def binary(A):
 sets=[7^(1<<((2-A[0][c])%3)) for c in range(10)]
 def go(r,allowed):
  if r==10:return True
  for u in range(3):
   new=[allowed[c]&~(1<<((2-A[r][c]-u)%3)) for c in range(10)]
   if all(new) and go(r+1,new):return True
  return False
 return go(1,sets)
triples=examples=nonbinary=0;first=None;hist=[]
for rec in fams:
 idx=rec['class'];line=lines[idx-1];H=[[ord(line[6+10*t+c])-48 for c in range(10)] for t in range(10)];nt=nb=0
 for fs in combinations(rec['families'],3):
  M=[mask(f) for f in fs]
  if not rank3(M) or not compatible(H,M):continue
  triples+=1;nt+=1
  for coeff in ((1,1,1),(1,1,2),(1,2,1),(2,1,1)):
   residues=[[sum(coeff[j]*M[j][t][c] for j in range(3))%3 for c in range(10)] for t in range(10)]
   examples+=1
   if not binary(residues):
    nonbinary+=1;nb+=1
    if first is None:
     K=[[(3*H[t][c]+sum(coeff[j]*M[j][t][c] for j in range(3)))%18 for c in range(10)] for t in range(10)]
     first={'class':idx,'rectangles':fs,'coefficients':coeff,'K_exponents_mod18':K}
 hist.append({'class':idx,'compatible_independent_triples':nt,'nonbinary_examples':nb})
 if nt:print('class',idx,'triples',nt,'nonbinary',nb,flush=True)
out={'triples':triples,'specializations':examples,'nonbinary_count':nonbinary,'classes':hist,'first_nonbinary':first,
 'scope':'fixed literal catalog/normalized 3-rectangle affine families; binary gauge exact F3 DFS'}
(P/'frontier-20261028-q18-triple-mask-result-v1.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print('DONE triples',triples,'specializations',examples,'nonbinary',nonbinary,flush=True)
