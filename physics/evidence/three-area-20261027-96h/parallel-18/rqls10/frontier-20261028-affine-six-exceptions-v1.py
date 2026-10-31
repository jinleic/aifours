#!/usr/bin/env python3
"""Exact halfgraph and row-obstruction certificates at zeta6 phases."""
from itertools import combinations,permutations
from functools import lru_cache
from pathlib import Path
import json
P=Path(__file__).resolve().parent
D=json.loads((P/'frontier-20261028-q18-binary-lift-result-v1.json').read_text())
line=(P/'frontier-20261028-aalto-bh10-6-catalog-v1.txt').read_text().splitlines()[D['catalog_class_1based']-1]
H=[[ord(line[6+10*t+c])-48 for c in range(10)] for t in range(10)]
R=set(D['rows']);C=set(D['columns']);six=[(1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1)]
def zero6(v):return all(sum(six[x%6][j] for x in v)==0 for j in range(2))
for r in R:
 for s in set(range(10))-R:assert zero6([H[r][c]-H[s][c] for c in C])
phi=[1,1,0,-1,-1,-1,0,1,1];pw=[]
for k in range(30):
 a=[0]*k+[1]
 for j in range(len(a)-1,7,-1):
  v=a[j]
  for i,c in enumerate(phi):a[j-8+i]-=v*c
 pw.append(tuple((a+[0]*8)[:8]))
def zero30(v):return all(sum(pw[x%30][j] for x in v)==0 for j in range(8))
def match(adj):
 @lru_cache(None)
 def go(mask):
  if not mask:return True
  a=mask&-mask;i=a.bit_length()-1;rem=mask^a;bits=adj[i]&rem
  while bits:
   b=bits&-bits;bits-=b
   if go(rem^b):return True
  return False
 return go(1023)
records=[]
for s in range(6):
 K=[[(H[t][c]+s*int(t in R and c in C))%6 for c in range(10)] for t in range(10)]
 assert all(zero6([K[t][d]-K[t][c] for t in range(10)]) for c,d in combinations(range(10),2))
 halves=[]
 for E in combinations(range(10),5):
  adj=[0]*10
  for c,d in combinations(range(10),2):
   if zero6([K[t][d]-K[t][c] for t in E]):adj[c]|=1<<d;adj[d]|=1<<c
  if match(adj):halves.append(E)
 print('zeta6 exponent',s,'matching halves',len(halves),flush=True)
 for E in halves:
  if 0 not in E:continue
  ev=[t for t in E if t];od=sorted(set(range(10))-set(E));digits=[]
  for a in permutations(ev):
   for b in permutations(od):
    order=[0,b[0],a[0],b[1],a[1],b[2],a[2],b[3],a[3],b[4]];bad=None
    for r in range(1,10):
     if all(not zero30([(3*r*t+5*(K[order[t]][d]-K[order[t]][0]))%30 for t in range(10)]) for d in range(1,10)):
      bad=r;break
    assert bad is not None,('NO_ROOT_WITNESS',s,E,order)
    digits.append(str(bad))
  assert len(digits)==2880
  records.append({'exponent':s,'even_half':list(E),'row_digits':''.join(digits)})
assert [r['exponent'] for r in records]==[1,4]
(P/'frontier-20261028-affine-six-exceptions-v1.json').write_text(json.dumps({'records':records,
 'scope':'root-row witnesses for two matching halves; others no half matching'},separators=(',',':'),sort_keys=True)+'\n')
print('PASS six zeta6 parameters; 4 halfgraph failures + 5760 row obstructions',flush=True)
