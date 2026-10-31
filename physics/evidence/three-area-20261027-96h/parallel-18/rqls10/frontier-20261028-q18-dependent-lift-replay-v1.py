#!/usr/bin/env python3
"""Independent compatible-mask reconstruction and Q(zeta6)[zeta18] halfgraphs."""
from itertools import combinations
from functools import lru_cache
from pathlib import Path
import json
P=Path(__file__).resolve().parent
lines=(P/'frontier-20261028-aalto-bh10-6-catalog-v1.txt').read_text().splitlines()
fams=json.loads((P/'frontier-20261028-bh6-rectangle-families-v1.json').read_text())['records']
claimed=json.loads((P/'frontier-20261028-bh6-two-parameter-pairs-v1.json').read_text())['pairs']
assert len(claimed)==176
six=[(1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1)]
# zeta18^3=zeta6 and [Q(zeta18):Q(zeta6)]=3.
p18=[]
for e in range(18):
 q,r=divmod(e,3);v=[0]*6;v[2*r],v[2*r+1]=six[q];p18.append(tuple(v))
def z6(v):return all(sum(six[x%6][j] for x in v)==0 for j in range(2))
def z18(v):return all(sum(p18[x%18][j] for x in v)==0 for j in range(6))
def mask(f):return [[int(t in f['rows'] and c in f['columns']) for c in range(10)] for t in range(10)]
def independent(A,B):
 v=[(A[r][c]-A[r][0]-A[0][c]+A[0][0],B[r][c]-B[r][0]-B[0][c]+B[0][0]) for r in range(1,10) for c in range(1,10)]
 pivot=next((x for x in v if x!=(0,0)),None)
 return pivot is not None and any(pivot[0]*b-pivot[1]*a!=0 for a,b in v)
def compatible(H,A,B):
 for r,s in combinations(range(10),2):
  groups={}
  for c in range(10):groups.setdefault((A[r][c]-A[s][c],B[r][c]-B[s][c]),[]).append(H[r][c]-H[s][c])
  if not all(z6(v) for v in groups.values()):return False
 return True
def match(adj):
 @lru_cache(None)
 def go(left):
  if not left:return True
  a=min(left);return any(b in adj[a] and go(left-{a,b}) for b in left-{a})
 return go(frozenset(range(10)))
actual=[]
for rec in fams:
 idx=rec['class'];s=lines[idx-1];H=[[ord(s[6+10*t+c])-48 for c in range(10)] for t in range(10)]
 for a,b in combinations(rec['families'],2):
  if independent(mask(a),mask(b)) and compatible(H,mask(a),mask(b)):actual.append({'class':idx,'first':a,'second':b})
assert actual==claimed
print('PASS independent reconstruction of 176 normalized compatible independent rectangle pairs',flush=True)
matrices=graphs=0
for no,item in enumerate(actual):
 s=lines[item['class']-1];H=[[ord(s[6+10*t+c])-48 for c in range(10)] for t in range(10)]
 A,B=mask(item['first']),mask(item['second'])
 for b in (1,2):
  K=[[(3*H[t][c]+A[t][c]+b*B[t][c])%18 for c in range(10)] for t in range(10)]
  for c,d in combinations(range(10),2):assert z18([K[t][d]-K[t][c] for t in range(10)])
  matrices+=1
  for E in combinations(range(10),5):
   adj=[set() for _ in range(10)]
   for c,d in combinations(range(10),2):
    if z18([K[t][d]-K[t][c] for t in E]):adj[c].add(d);adj[d].add(c)
   assert not match(adj),('MATCHING_HALF',no,b,E)
   graphs+=1
 if no%25==0:print('pair',no,'graphs',graphs,flush=True)
assert matrices==352 and graphs==88704
(P/'frontier-20261028-q18-dependent-lift-replay-result-v1.json').write_text(json.dumps({'pairs':len(actual),'matrices':matrices,'halfgraphs':graphs,
 'matching_halves':0,'scope':'exact literal dependent-phase halfgraph replay, no independent base classification'},indent=2,sort_keys=True)+'\n')
print('PASS all352 q18 matrices, 88704 halfgraphs, NO perfect matching')
