#!/usr/bin/env python3
"""Independent q15 catalog halfgraph scan in Q(zeta3,zeta5)."""
from itertools import combinations
from functools import lru_cache
from pathlib import Path
P=Path(__file__).resolve().parent
lines=(P/'frontier-20261028-aalto-bh10-15-catalog-v1.txt').read_text().splitlines();assert len(lines)==1
s=lines[0];assert len(s)==106 and s[:6]=='BH1::?'
H=[[ord(s[6+10*t+c])-48 for c in range(10)] for t in range(10)]
assert all(0<=v<15 for row in H for v in row)
three=[(1,0),(0,1),(-1,-1)];five=[(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1),(-1,-1,-1,-1)]
# zeta15=zeta3^2*zeta5^2.
pow15=[tuple(a*b for a in three[(2*e)%3] for b in five[(2*e)%5]) for e in range(15)]
def zero(v):return all(sum(pow15[x%15][j] for x in v)==0 for j in range(8))
for c,d in combinations(range(10),2):assert zero([H[t][d]-H[t][c] for t in range(10)])
def matching(adj):
 @lru_cache(None)
 def go(left):
  if not left:return True
  a=min(left);return any(b in adj[a] and go(left-{a,b}) for b in left-{a})
 return go(frozenset(range(10)))
count=0
for E in combinations(range(10),5):
 adj=[set() for _ in range(10)]
 for c,d in combinations(range(10),2):
  if zero([H[t][d]-H[t][c] for t in E]):adj[c].add(d);adj[d].add(c)
 if matching(adj):count+=1
assert count==0
print('PASS one valid BH(10,15) representative; all252 halfgraphs lack perfect matching')
print('ALL-BH(10,15) claim depends on prior one-class monomial classification.')
