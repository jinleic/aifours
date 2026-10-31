#!/usr/bin/env python3
"""Independent Q(zeta3,zeta5) replay for eight paths' six q6 endpoints."""
from itertools import combinations,permutations
from functools import lru_cache
from pathlib import Path
import json
P=Path(__file__).resolve().parent
cases=json.loads((P/'frontier-20261028-q18-nonbinary-twentyfour-v1.json').read_text())['records']
cert=json.loads((P/'frontier-20261028-nonbinary-eight-endpoints-v1.json').read_text())
lines=(P/'frontier-20261028-aalto-bh10-6-catalog-v1.txt').read_text().splitlines()
six=[(1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1)]
three=[(1,0),(0,1),(-1,-1)];five=[(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1),(-1,-1,-1,-1)]
thirty=[tuple((-1)**e*a*b for a in three[e%3] for b in five[e%5])for e in range(30)]
def z6(v):return all(sum(six[x%6][j] for x in v)==0 for j in range(2))
def z30(v):return all(sum(thirty[x%30][j] for x in v)==0 for j in range(8))
def match(adj):
 @lru_cache(None)
 def go(left):
  if not left:return True
  a=min(left);return any(b in adj[a] and go(left-{a,b}) for b in left-{a})
 return go(frozenset(range(10)))
records={(x['case'],x['phase6'],tuple(x['even_half'])):x for x in cert['records']}
assert len(records)==len(cert['records'])
seen=set();orders=graphs=0
for ix in range(4,12):
 D=cases[ix];line=lines[D['class']-1];H=[[ord(line[6+10*t+c])-48 for c in range(10)]for t in range(10)]
 R=[[sum(co*int(t in f['rows'] and c in f['columns'])for co,f in zip(D['coefficients'],D['rectangles']))for c in range(10)]for t in range(10)]
 for s in range(6):
  K=[[(H[t][c]+s*R[t][c])%6 for c in range(10)]for t in range(10)]
  for c,d in combinations(range(10),2):assert z6([K[t][d]-K[t][c] for t in range(10)])
  for E in combinations(range(10),5):
   adj=[set() for _ in range(10)]
   for c,d in combinations(range(10),2):
    if z6([K[t][d]-K[t][c] for t in E]):adj[c].add(d);adj[d].add(c)
   graphs+=1
   if not match(adj) or 0 not in E:continue
   key=(ix,s,E);assert key in records and key not in seen;seen.add(key)
   digits=records[key]['digits'];assert len(digits)==2880
   ev=[t for t in E if t];od=sorted(set(range(10))-set(E));j=0
   for a in permutations(ev):
    for b in permutations(od):
     order=[0,b[0],a[0],b[1],a[1],b[2],a[2],b[3],a[3],b[4]];r=int(digits[j]);j+=1
     assert 1<=r<=9
     for d in range(1,10):assert not z30([3*r*t+5*(K[order[t]][d]-K[order[t]][0]) for t in range(10)])
     orders+=1
   assert j==2880
 print('PASS case',ix,'all six endpoint halfgraphs and row certificates',flush=True)
assert seen==set(records) and orders==cert['orders'] and graphs==8*6*252
out={'cases':8,'phases':48,'halfgraphs':graphs,'normalized_matching_halves':len(seen),'row_orders':orders,
     'scope':'literal eight paths only; no catalog-completeness premise'}
(P/'frontier-20261028-nonbinary-eight-endpoints-replay-result-v1.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print('PASS',out,flush=True)
