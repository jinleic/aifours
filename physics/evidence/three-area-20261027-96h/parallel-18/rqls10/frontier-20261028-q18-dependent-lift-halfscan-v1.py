#!/usr/bin/env python3
"""Exact halfgraphs for dependent q18 phases on valid two-rectangle families."""
from functools import lru_cache
from itertools import combinations,combinations_with_replacement
from pathlib import Path
import json
P=Path(__file__).resolve().parent
lines=(P/'frontier-20261028-aalto-bh10-6-catalog-v1.txt').read_text().splitlines()
data=json.loads((P/'frontier-20261028-bh6-two-parameter-pairs-v1.json').read_text())['pairs'];assert len(data)==176
f=[1,0,0,-1,0,0,1];powers=[]
for e in range(18):
 a=[0]*e+[1]
 for k in range(len(a)-1,5,-1):
  v=a[k]
  for j,x in enumerate(f):a[k-6+j]-=v*x
 powers.append(tuple((a+[0]*6)[:6]))
def zero(v):return all(sum(powers[x%18][j] for x in v)==0 for j in range(6))
Z={x for x in combinations_with_replacement(range(18),5) if zero(x)}
def pm(adj):
 @lru_cache(None)
 def go(mask):
  if not mask:return True
  bit=mask&-mask;i=bit.bit_length()-1;rem=mask^bit;cs=adj[i]&rem
  while cs:
   b=cs&-cs;cs-=b
   if go(rem^b):return True
  return False
 return go(1023)
result=[];totalmatch=totalgood=0
for no,item in enumerate(data):
 line=lines[item['class']-1];H=[[ord(line[6+10*t+c])-48 for c in range(10)] for t in range(10)]
 def mm(f,t,c):return int(t in f['rows'] and c in f['columns'])
 for slope in (1,2):
  K=[[(3*H[t][c]+mm(item['first'],t,c)+slope*mm(item['second'],t,c))%18 for c in range(10)] for t in range(10)]
  for c,d in combinations(range(10),2):assert zero([K[t][d]-K[t][c] for t in range(10)])
  diff={(c,d):[(K[t][d]-K[t][c])%18 for t in range(10)] for c,d in combinations(range(10),2)}
  matches=[]
  for E in combinations(range(10),5):
   adj=[0]*10
   for (c,d),v in diff.items():
    if tuple(sorted(v[t] for t in E)) in Z:adj[c]|=1<<d;adj[d]|=1<<c
   if not pm(adj):continue
   other=set(range(10))-set(E);dups=[]
   for (c,d),v in diff.items():
    x=v[E[0]]
    if all(v[t]==x for t in E) and all(v[t]==(x+9)%18 for t in other):dups.append([c,d])
   totalmatch+=1
   if not dups:
    totalgood+=1
    if 0 in E:matches.append(list(E))
  result.append({'pair_index_0based':no,'class':item['class'],'slope2':slope,'normalized_good_halves':matches})
 if no%25==0:print('pair',no,'matching',totalmatch,'collisionfree',totalgood,flush=True)
out={'scope':'352 q18 matrices in dependent-phase subfamilies; halfmatching is necessary only',
 'matching_halves':totalmatch,'collisionfree_halves':totalgood,'records':result}
(P/'frontier-20261028-q18-dependent-lift-halfscan-result-v1.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print('DONE',len(result),'matrices','matching',totalmatch,'collisionfree',totalgood,flush=True)
