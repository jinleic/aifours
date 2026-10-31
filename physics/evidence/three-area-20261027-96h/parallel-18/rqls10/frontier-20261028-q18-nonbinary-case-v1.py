#!/usr/bin/env python3
"""Exact K validation, halfgraph scan and exhaustive F3 nonbinary certificate."""
from itertools import product,combinations
from functools import lru_cache
from pathlib import Path
import json
P=Path(__file__).resolve().parent
D=json.loads((P/'frontier-20261028-q18-multirect-result-v1.json').read_text())['nonbinary_examples'][0]
line=(P/'frontier-20261028-aalto-bh10-6-catalog-v1.txt').read_text().splitlines()[D['class']-1]
H=[[ord(line[6+10*t+c])-48 for c in range(10)]for t in range(10)]
M=[[[int(t in f['rows'] and c in f['columns']) for c in range(10)]for t in range(10)]for f in D['rectangles']]
coeff=D['coefficients'];K=[[(3*H[t][c]+sum(coeff[j]*M[j][t][c] for j in range(len(M))))%18 for c in range(10)]for t in range(10)]
phi=[1,0,0,-1,0,0,1];pw=[]
for n in range(18):
 a=[0]*n+[1]
 for i in range(len(a)-1,5,-1):
  v=a[i]
  for j,x in enumerate(phi):a[i-6+j]-=v*x
 pw.append(tuple((a+[0]*6)[:6]))
def zero(v):return all(sum(pw[x%18][j] for x in v)==0 for j in range(6))
for c,d in combinations(range(10),2):assert zero([K[t][d]-K[t][c] for t in range(10)])
def match(adj):
 @lru_cache(None)
 def go(mask):
  if not mask:return True
  bit=mask&-mask;i=bit.bit_length()-1;rest=mask^bit;opts=adj[i]&rest
  while opts:
   b=opts&-opts;opts-=b
   if go(rest^b):return True
  return False
 return go(1023)
halves=[]
for E in combinations(range(10),5):
 adj=[0]*10
 for c,d in combinations(range(10),2):
  if zero([K[t][d]-K[t][c] for t in E]):adj[c]|=1<<d;adj[d]|=1<<c
 if match(adj):halves.append(E)
digits=[]
for vals in product(range(3),repeat=9):
 row=(0,)+vals;bad=None
 for c in range(10):
  forbidden={(2-K[t][c]-row[t])%3 for t in range(10)}
  if len(forbidden)==3:bad=c;break
 assert bad is not None,('BINARY_GAUGE',row)
 digits.append(str(bad))
assert len(digits)==19683
out={'class':D['class'],'coefficients':coeff,'rectangles':D['rectangles'],'K_exponents_mod18':K,
 'matching_halves':[list(e) for e in halves],'row_gauge_obstruction_digits':''.join(digits),
 'scope':'one literal nonbinary q18 matrix; row/column phase-gauge F3 obstruction'}
(P/'frontier-20261028-q18-nonbinary-case-v1.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print('class',D['class'],'BH18 valid, matching halves',len(halves),'F3 row-gauge obstruction 19683',flush=True)
print('first halves',halves[:5],flush=True)
