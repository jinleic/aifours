#!/usr/bin/env python3
"""Independent q6 halfgraph enumeration and Q(zeta3,zeta5) certificate replay."""
from functools import lru_cache
from itertools import combinations,permutations
from pathlib import Path
import json
P=Path(__file__).resolve().parent
lines=(P/'frontier-20261028-aalto-bh10-6-catalog-v1.txt').read_text().splitlines();assert len(lines)==34
cert=json.loads((P/'frontier-20261028-aalto-q6-root-certificate-v1.json').read_text())['records']
# zeta6 powers in basis (1,zeta6); zeta30=-zeta3*zeta5.
six=[(1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1)]
three=[(1,0),(0,1),(-1,-1)]
five=[(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1),(-1,-1,-1,-1)]
thirty=[tuple(((-1)**e)*a*b for a in three[e%3] for b in five[e%5]) for e in range(30)]
def z6(v):return all(sum(six[x%6][j] for x in v)==0 for j in range(2))
def z30(v):return all(sum(thirty[x%30][j] for x in v)==0 for j in range(8))
def matching(adj):
 @lru_cache(None)
 def rec(rem):
  if not rem:return True
  a=min(rem);return any(b in adj[a] and rec(rem-{a,b}) for b in rem-{a})
 return rec(frozenset(range(10)))
matrices=[];candidate=[];halves=0
for idx,line in enumerate(lines,1):
 assert len(line)==106 and line[:6]=='BH1::6'
 H=[[ord(line[6+10*t+c])-48 for c in range(10)] for t in range(10)]
 assert all(0<=x<6 for row in H for x in row)
 for c,d in combinations(range(10),2):assert z6([H[t][d]-H[t][c] for t in range(10)])
 matrices.append(H)
 for E in combinations(range(10),5):
  adj=[set() for _ in range(10)]
  for c,d in combinations(range(10),2):
   if z6([H[t][d]-H[t][c] for t in E]):adj[c].add(d);adj[d].add(c)
  if matching(adj):
   halves+=1
   if 0 in E:candidate.append((idx,E))
assert halves==50 and len(candidate)==25
assert [(r['catalog_index_1based'],tuple(r['even_half'])) for r in cert]==candidate
orders=0
for rec in cert:
 idx=rec['catalog_index_1based'];E=tuple(rec['even_half']);H=matrices[idx-1]
 digit=rec['obstructed_row_digits'];assert len(digit)==2880 and all(x in '123456789' for x in digit)
 ev=[t for t in E if t];od=sorted(set(range(10))-set(E));j=0
 for a in permutations(ev):
  for b in permutations(od):
   order=[0,b[0],a[0],b[1],a[1],b[2],a[2],b[3],a[3],b[4]];r=int(digit[j]);j+=1
   for d in range(1,10):
    vals=[(3*r*t+5*(H[order[t]][d]-H[order[t]][0]))%30 for t in range(10)]
    assert not z30(vals),(idx,E,order,r,d)
   orders+=1
 assert j==2880
 print('PASS class',idx,'E',E,'2880 row obstructions',flush=True)
assert orders==72000
print('PASS all34 BH; 50 matching halves; all72000 root obstructions in Q(zeta3,zeta5)')
