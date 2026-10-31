#!/usr/bin/env python3
"""Exact K/halfgraph and exhaustive mod3 gauge obstructions for 12 q18 examples."""
from itertools import combinations,product
from functools import lru_cache
from pathlib import Path
import json
P=Path(__file__).resolve().parent
src=json.loads((P/'frontier-20261028-q18-multirect-all-sign-result-v1.json').read_text());cases=src['nonbinary_examples'];assert src['nonbinary_count']==len(cases)==24
lines=(P/'frontier-20261028-aalto-bh10-6-catalog-v1.txt').read_text().splitlines()
phi=[1,0,0,-1,0,0,1];pw=[]
for k in range(18):
 a=[0]*k+[1]
 for j in range(len(a)-1,5,-1):
  v=a[j]
  for i,c in enumerate(phi):a[j-6+i]-=v*c
 pw.append(tuple((a+[0]*6)[:6]))
def zero(v):return all(sum(pw[x%18][j] for x in v)==0 for j in range(6))
def match(adj):
 @lru_cache(None)
 def go(mask):
  if not mask:return True
  a=mask&-mask;i=a.bit_length()-1;rest=mask^a;opts=adj[i]&rest
  while opts:
   b=opts&-opts;opts-=b
   if go(rest^b):return True
  return False
 return go(1023)
records=[]
for no,D in enumerate(cases):
 line=lines[D['class']-1];H=[[ord(line[6+10*t+c])-48 for c in range(10)]for t in range(10)]
 M=[[[int(t in f['rows'] and c in f['columns']) for c in range(10)]for t in range(10)]for f in D['rectangles']]
 co=D['coefficients'];K=[[(3*H[t][c]+sum(co[j]*M[j][t][c] for j in range(len(M))))%18 for c in range(10)]for t in range(10)]
 for c,d in combinations(range(10),2):assert zero([K[t][d]-K[t][c] for t in range(10)])
 good=[]
 for E in combinations(range(10),5):
  adj=[0]*10
  for c,d in combinations(range(10),2):
   if zero([K[t][d]-K[t][c] for t in E]):adj[c]|=1<<d;adj[d]|=1<<c
  if match(adj):good.append(list(E))
 digits=[]
 for val in product(range(3),repeat=9):
  r=(0,)+val;bad=next((c for c in range(10) if len({(2-K[t][c]-r[t])%3 for t in range(10)})==3),None)
  assert bad is not None,('BINARY',no,r)
  digits.append(str(bad))
 assert len(digits)==19683
 records.append({'case':no,'class':D['class'],'coefficients':co,'rectangles':D['rectangles'],
                 'K_exponents_mod18':K,'matching_halves':good,'row_gauge_obstruction_digits':''.join(digits)})
 print('case',no,'class',D['class'],'matching_halves',len(good),'nonbinary row gauges certified',flush=True)
out={'scope':'12 literal q18 matrices; no general BH18 classification','records':records}
(P/'frontier-20261028-q18-nonbinary-twentyfour-v1.json').write_text(json.dumps(out,separators=(',',':'),sort_keys=True)+'\n')
print('DONE 24 cases; matching-half counts',[len(x['matching_halves']) for x in records],flush=True)
