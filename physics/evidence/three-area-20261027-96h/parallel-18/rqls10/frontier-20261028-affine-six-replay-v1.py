#!/usr/bin/env python3
"""Independent zeta3/zeta5 replay of all six affine exceptions."""
from itertools import combinations,permutations
from functools import lru_cache
from pathlib import Path
import json
P=Path(__file__).resolve().parent
D=json.loads((P/'frontier-20261028-q18-binary-lift-result-v1.json').read_text());rec=json.loads((P/'frontier-20261028-affine-six-exceptions-v1.json').read_text())['records']
line=(P/'frontier-20261028-aalto-bh10-6-catalog-v1.txt').read_text().splitlines()[D['catalog_class_1based']-1]
H=[[ord(line[6+10*t+c])-48 for c in range(10)] for t in range(10)];R=set(D['rows']);C=set(D['columns'])
six=[(1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1)]
three=[(1,0),(0,1),(-1,-1)];five=[(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1),(-1,-1,-1,-1)]
thirty=[tuple((-1)**e*a*b for a in three[e%3] for b in five[e%5]) for e in range(30)]
def z6(v):return all(sum(six[x%6][j] for x in v)==0 for j in range(2))
def z30(v):return all(sum(thirty[x%30][j] for x in v)==0 for j in range(8))
def match(adj):
 @lru_cache(None)
 def go(left):
  if not left:return True
  a=min(left);return any(b in adj[a] and go(left-{a,b}) for b in left-{a})
 return go(frozenset(range(10)))
for r in R:
 for s in set(range(10))-R:assert z6([H[r][c]-H[s][c] for c in C])
records={x['exponent']:x for x in rec};assert set(records)=={1,4}
verified=0
for s in range(6):
 K=[[(H[t][c]+s*int(t in R and c in C))%6 for c in range(10)] for t in range(10)]
 for c,d in combinations(range(10),2):assert z6([K[t][d]-K[t][c] for t in range(10)])
 halves=[]
 for E in combinations(range(10),5):
  adj=[set() for _ in range(10)]
  for c,d in combinations(range(10),2):
   if z6([K[t][d]-K[t][c] for t in E]):adj[c].add(d);adj[d].add(c)
  if match(adj):halves.append(E)
 assert len(halves)==(2 if s in (1,4) else 0)
 if s not in records:continue
 E=tuple(records[s]['even_half']);assert [x for x in halves if 0 in x]==[E]
 digits=records[s]['row_digits'];assert len(digits)==2880
 ev=[t for t in E if t];od=sorted(set(range(10))-set(E));j=0
 for a in permutations(ev):
  for b in permutations(od):
   order=[0,b[0],a[0],b[1],a[1],b[2],a[2],b[3],a[3],b[4]];r=int(digits[j]);j+=1
   assert 1<=r<=9
   for d in range(1,10):
    assert not z30([3*r*t+5*(K[order[t]][d]-K[order[t]][0]) for t in range(10)])
   verified+=1
assert verified==5760
print('PASS six zeta6 phases; 4 halfgraph failures; 5760 independently checked row obstructions')
print('PASS arbitrary-z rectangle is Hadamard by exact partial-row sums')
