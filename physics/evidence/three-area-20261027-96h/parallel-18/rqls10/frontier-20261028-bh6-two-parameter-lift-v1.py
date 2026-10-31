#!/usr/bin/env python3
"""Exact 2-rectangle affine Hadamard scan and q126 candidate generation."""
from itertools import combinations
from pathlib import Path
import json
P=Path(__file__).resolve().parent
lines=(P/'frontier-20261028-aalto-bh10-6-catalog-v1.txt').read_text().splitlines()
data=json.loads((P/'frontier-20261028-bh6-rectangle-families-v1.json').read_text())
six=[(1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1)]
def zero(v):return all(sum(six[x%6][j] for x in v)==0 for j in range(2))
def mask(f):return [[int(t in f['rows'] and c in f['columns']) for c in range(10)] for t in range(10)]
def independent(A,B):
 x=[];y=[]
 for r in range(1,10):
  for c in range(1,10):
   x.append(A[r][c]-A[r][0]-A[0][c]+A[0][0]);y.append(B[r][c]-B[r][0]-B[0][c]+B[0][0])
 return any(x[i]*y[j]!=x[j]*y[i] for i in range(len(x)) for j in range(i+1,len(x)))
def compatible(H,A,B):
 for r,s in combinations(range(10),2):
  bins={}
  for c in range(10):
   key=(A[r][c]-A[s][c],B[r][c]-B[s][c])
   bins.setdefault(key,[]).append(H[r][c]-H[s][c])
  if not all(zero(v) for v in bins.values()):return False
 return True
count=0;best=None;classes=[]
for rec in data['records']:
 idx=rec['class'];line=lines[idx-1];H=[[ord(line[6+10*t+c])-48 for c in range(10)] for t in range(10)]
 found=0
 for f1,f2 in combinations(rec['families'],2):
  A,B=mask(f1),mask(f2)
  if not independent(A,B) or not compatible(H,A,B):continue
  count+=1;found+=1
  K=[[(21*H[t][c]+7*A[t][c]+3*B[t][c])%126 for c in range(10)] for t in range(10)]
  rep=[]
  for c,d in combinations(range(10),2):
   for m in (0,5):
    # Compare in zeta630: K phases are fifth powers, Fourier phases 63rd powers.
    if len({(5*(K[t][d]-K[t][c])-63*m*t)%630 for t in range(10)})==1:rep.append((c,d,m))
  if not rep and best is None:best=(idx,f1,f2,K)
 if found:classes.append({'class':idx,'pairs':found})
print('exact independent 2-rectangle families',count,'source classes',len(classes),'found 100-ray candidate',best is not None,flush=True)
out={'families':count,'classes':classes,'scope':'exact Laurent-coefficient compatibility for normalized rectangles; sample needs independent check'}
if best:
 idx,f1,f2,K=best;out.update({'candidate':{'class':idx,'first':f1,'second':f2,'K_exponents_mod126':K}})
(P/'frontier-20261028-bh6-two-parameter-lift-result-v1.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
