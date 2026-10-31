#!/usr/bin/env python3
"""Exact 72 root phases of the specified 4-mask q6 affine family."""
from itertools import combinations
from functools import lru_cache
from pathlib import Path
import json
P=Path(__file__).resolve().parent
D=json.loads((P/'frontier-20261028-q18-nonbinary-twentyfour-v1.json').read_text())['records'][0]
line=(P/'frontier-20261028-aalto-bh10-6-catalog-v1.txt').read_text().splitlines()[D['class']-1]
H=[[ord(line[6+10*t+c])-48 for c in range(10)]for t in range(10)]
R=[[sum(co*int(t in f['rows'] and c in f['columns']) for co,f in zip(D['coefficients'],D['rectangles'])) for c in range(10)]for t in range(10)]
# Phi72=x24-x12+1.
pow72=[]
for e in range(72):
 a=[0]*e+[1]
 for k in range(len(a)-1,23,-1):
  v=a[k];a[k]-=v;a[k-12]+=v;a[k-24]-=v
 pow72.append(tuple((a+[0]*24)[:24]))
def zero(v):
 for j in range(24):
  if sum(pow72[x%72][j] for x in v):return False
 return True
def match(adj):
 @lru_cache(None)
 def go(mask):
  if not mask:return True
  bit=mask&-mask;i=bit.bit_length()-1;rest=mask^bit;bits=adj[i]&rest
  while bits:
   b=bits&-bits;bits-=b
   if go(rest^b):return True
  return False
 return go(1023)
rec=[]
for s in range(72):
 K=[[(12*H[t][c]+s*R[t][c])%72 for c in range(10)]for t in range(10)]
 for c,d in combinations(range(10),2):assert zero([K[t][d]-K[t][c] for t in range(10)])
 good=[]
 for E in combinations(range(10),5):
  adj=[0]*10
  for c,d in combinations(range(10),2):
   if zero([K[t][d]-K[t][c] for t in E]):adj[c]|=1<<d;adj[d]|=1<<c
  if match(adj):good.append(list(E))
 rec.append({'s':s,'matching_halves':good})
 if good:print('phase',s,'matching halves',len(good),'first',good[0],flush=True)
print('DONE phases',len(rec),'with matching',sum(bool(x['matching_halves']) for x in rec),flush=True)
(P/'frontier-20261028-nonbinary-affine-q72-scan-v1.json').write_text(json.dumps({'records':rec,
 'scope':'specified 4-mask one-parameter family; matching necessary not sufficient'},indent=2,sort_keys=True)+'\n')
