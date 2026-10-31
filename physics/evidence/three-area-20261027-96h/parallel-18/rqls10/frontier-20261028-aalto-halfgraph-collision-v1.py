#!/usr/bin/env python3
"""Independent exact root-sum/matching and opposite-row duplicate census."""
from itertools import combinations
from functools import lru_cache
from pathlib import Path
import json
P=Path(__file__).resolve().parent
# Ascending coefficients for Phi6, Phi10, Phi12.
PHI={6:[1,-1,1],10:[1,-1,1,-1,1],12:[1,0,-1,0,1]}
def powers(q):
 f=PHI[q];deg=len(f)-1;out=[]
 for n in range(q):
  a=[0]*n+[1]
  for k in range(len(a)-1,deg-1,-1):
   v=a[k]
   for j,x in enumerate(f):a[k-deg+j]-=v*x
  out.append(tuple((a+[0]*deg)[:deg]))
 return out

def perfect(a):
 @lru_cache(None)
 def rec(mask):
  if mask==0:return True
  b=mask&-mask;i=b.bit_length()-1;rest=mask^b;can=a[i]&rest
  while can:
   c=can&-can;can-=c
   if rec(rest^c):return True
  return False
 return rec(1023)
results=[]
for q,expected in ((6,34),(10,51),(12,577)):
 lines=(P/f'frontier-20261028-aalto-bh10-{q}-catalog-v1.txt').read_text().splitlines()
 assert len(lines)==expected
 pw=powers(q);deg=len(pw[0]);rows=[];total=duplicates=0
 for no,line in enumerate(lines,1):
  assert len(line)==106 and line[:3]=='BH1' and [ord(x)-48 for x in line[3:6]]==[10,10,q]
  a=[[ord(line[6+10*t+c])-48 for c in range(10)] for t in range(10)]
  diff={(c,d):[(a[t][d]-a[t][c])%q for t in range(10)] for c,d in combinations(range(10),2)}
  for v in diff.values():assert all(sum(pw[x][j] for x in v)==0 for j in range(deg))
  good=[]
  for E in combinations(range(10),5):
   adj=[0]*10
   for (c,d),v in diff.items():
    if all(sum(pw[v[t]][j] for t in E)==0 for j in range(deg)):
     adj[c]|=1<<d;adj[d]|=1<<c
   if not perfect(adj):continue
   eset=set(E);O=[t for t in range(10) if t not in eset];dups=[]
   for (c,d),v in diff.items():
    x=v[E[0]]
    if all(v[t]==x for t in E) and all(v[t]==(x+q//2)%q for t in O):dups.append([c,d])
   total+=1;duplicates+=bool(dups)
   good.append({'even_half':list(E),'opposite_row_duplicate_columns':dups})
  if good:rows.append({'matrix_index_1based':no,'matching_halves':good})
 print('q',q,'matching_halves',total,'with_opposite_row_duplicate',duplicates,'without',total-duplicates,flush=True)
 results.append({'q':q,'matrices':expected,'matching_halves':total,
                 'halves_with_opposite_row_duplicate':duplicates,'records':rows})
(P/'frontier-20261028-aalto-halfgraph-collision-result-v1.json').write_text(json.dumps(results,indent=2,sort_keys=True)+'\n')
