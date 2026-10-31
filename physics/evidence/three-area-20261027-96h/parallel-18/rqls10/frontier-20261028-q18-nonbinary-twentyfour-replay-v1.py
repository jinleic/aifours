#!/usr/bin/env python3
"""Independently replay 12 q18 nonbinary gauges and original-vector no-T checks."""
from itertools import product,combinations
from functools import lru_cache
from pathlib import Path
import json
P=Path(__file__).resolve().parent
D=json.loads((P/'frontier-20261028-q18-nonbinary-twentyfour-v1.json').read_text())['records'];assert len(D)==24
lines=(P/'frontier-20261028-aalto-bh10-6-catalog-v1.txt').read_text().splitlines()
# zeta9^6=-1-zeta9^3; zeta18=-zeta9^5; zeta90=-zeta9*zeta5^2.
nine=[]
for e in range(9):
 a=[0]*6
 if e<6:a[e]=1
 else:a[e-6]-=1;a[e-3]-=1
 nine.append(tuple(a))
five=[(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1),(-1,-1,-1,-1)]
p18=[tuple((-1)**e*x for x in nine[(5*e)%9]) for e in range(18)]
p90=[tuple((-1)**e*a*b for a in nine[e%9] for b in five[(2*e)%5]) for e in range(90)]
def zero(v,table):return all(sum(table[x%len(table)][j] for x in v)==0 for j in range(len(table[0])))
def matching(adj):
 @lru_cache(None)
 def go(left):
  if not left:return True
  a=min(left);return any(b in adj[a] and go(left-{a,b}) for b in left-{a})
 return go(frozenset(range(10)))
orders=graphs=0
for case in D:
 K=case['K_exponents_mod18'];line=lines[case['class']-1]
 H=[[ord(line[6+10*t+c])-48 for c in range(10)]for t in range(10)]
 for t in range(10):
  for c in range(10):
   exponent=3*H[t][c]+sum(co*int(t in f['rows'] and c in f['columns']) for co,f in zip(case['coefficients'],case['rectangles']))
   assert K[t][c]==exponent%18
 for c,d in combinations(range(10),2):assert zero([K[t][d]-K[t][c] for t in range(10)],p18)
 for E in combinations(range(10),5):
  adj=[set() for _ in range(10)]
  for c,d in combinations(range(10),2):
   if zero([K[t][d]-K[t][c] for t in E],p18):adj[c].add(d);adj[d].add(c)
  assert not matching(adj);graphs+=1
 assert not case['matching_halves']
 digits=case['row_gauge_obstruction_digits'];assert len(digits)==3**9
 for i,vals in enumerate(product(range(3),repeat=9)):
  rr=(0,)+vals;c=int(digits[i]);assert 0<=c<10
  assert {(2-K[t][c]-rr[t])%3 for t in range(10)}=={0,1,2}
  orders+=1
 V=[[[ (9*r*t+5*K[t][c])%90 for t in range(10)] for c in range(10)]for r in range(10)]
 def orth(x,y):return zero([b-a for a,b in zip(x,y)],p90)
 for r in range(10):
  for c,d in combinations(range(10),2):assert orth(V[r][c],V[r][d])
 for c in range(10):
  for r,s in combinations(range(10),2):assert orth(V[r][c],V[s][c])
 rays=[tuple((x-v[0])%90 for x in v) for row in V for v in row]
 assert len(set(rays))==100
 for a,b in combinations(rays,2):assert a!=b
 print('PASS case',case['case'],'original 100-ray QLS, 252 no-match graphs, 19683 nonbinary certificates',flush=True)
assert graphs==6048 and orders==472392
out={'cases':24,'halfgraphs':graphs,'nonbinary_row_gauges':orders,
 'scope':'24 literal q18 examples; no classification or unrestricted target claim'}
(P/'frontier-20261028-q18-nonbinary-twentyfour-replay-result-v1.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print('PASS',out,flush=True)
