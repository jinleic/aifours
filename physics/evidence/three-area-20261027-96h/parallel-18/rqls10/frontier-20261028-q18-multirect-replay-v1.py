#!/usr/bin/env python3
"""Independent all-subset compatibility and all binary-witness coverage replay."""
from itertools import combinations,product
from collections import Counter
from pathlib import Path
import json
P=Path(__file__).resolve().parent
fams=json.loads((P/'frontier-20261028-bh6-rectangle-families-v1.json').read_text())['records']
src=json.loads((P/'frontier-20261028-q18-multirect-all-result-v1.json').read_text())
non=json.loads((P/'frontier-20261028-q18-nonbinary-twelve-v1.json').read_text())['records']
lines=(P/'frontier-20261028-aalto-bh10-6-catalog-v1.txt').read_text().splitlines()
six=[(1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1)]
def zero(v):return all(sum(six[x%6][j] for x in v)==0 for j in range(2))
def mask(f):return [[int(r in f['rows'] and c in f['columns']) for c in range(10)]for r in range(10)]
def compat(H,M):
 for r,s in combinations(range(10),2):
  bins={}
  for c in range(10):bins.setdefault(tuple(A[r][c]-A[s][c] for A in M),[]).append(H[r][c]-H[s][c])
  if any(not zero(v) for v in bins.values()):return False
 return True
expected={};hist=Counter()
for rec in fams:
 idx=rec['class'];line=lines[idx-1];H=[[ord(line[6+10*r+c])-48 for c in range(10)]for r in range(10)]
 M=list(map(mask,rec['families']))
 for size in range(1,len(M)+1):
  for ids in combinations(range(len(M)),size):
   if not compat(H,[M[i] for i in ids]):continue
   hist[size]+=1
   for co in product((1,2),repeat=size-1):expected[(idx,ids,(1,)+co)]=[M[i] for i in ids]
assert len(expected)==1944 and hist=={1:104,2:176,3:164,4:76,5:14}
seen=set()
for w in src['binary_gauge_witnesses']:
 key=(w['class'],tuple(w['mask_indices']),tuple(w['coefficients']));assert key in expected and key not in seen
 M=expected[key];u=w['row_gauge'];v=w['column_gauge'];assert len(u)==len(v)==10
 assert all(0<=x<3 for x in u+v)
 assert all((sum(key[2][j]*M[j][r][c] for j in range(len(M)))+u[r]+v[c])%3 in (0,1) for r in range(10) for c in range(10))
 seen.add(key)
nonkeys=set()
for w in src['nonbinary_examples']:
 key=(w['class'],tuple(w['mask_indices']),tuple(w['coefficients']));assert key in expected and key not in seen
 # Match to independently replayed twelve literal matrices by full rectangle/coeff data.
 rects=[fams[w['class']-1]['families'][i] for i in key[1]]
 found=[x for x in non if x['class']==key[0] and x['coefficients']==list(key[2]) and x['rectangles']==rects]
 assert len(found)==1 and not found[0]['matching_halves']
 nonkeys.add(key);seen.add(key)
assert len(nonkeys)==12 and len(src['binary_gauge_witnesses'])==1932 and seen==set(expected)
out={'compatible_subsets':dict(hist),'specializations':len(expected),'binary_witnesses':1932,'nonbinary_cases':12,
 'scope':'literal 34 representative rectangle systems, no independent catalog classification'}
(P/'frontier-20261028-q18-multirect-replay-result-v1.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print('PASS independent all-subset compatibility, 1932 F3 gauge witnesses, 12 linked no-halfgraph cases')
print(out)
