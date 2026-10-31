#!/usr/bin/env python3
"""Exact finite F3 row/column gauge classification of 352 dependent lifts."""
from pathlib import Path
import json
P=Path(__file__).resolve().parent
pairs=json.loads((P/'frontier-20261028-bh6-two-parameter-pairs-v1.json').read_text())['pairs'];assert len(pairs)==176
def mask(f,r,c):return int(r in f['rows'] and c in f['columns'])
def solve(A):
 # Require (A[r,c]+u[r]+v[c]) mod3 != 2; fix u[0]=0 by gauge.
 allowed=[7^(1<<((2-A[0][c])%3)) for c in range(10)];nodes=0
 def dfs(r,sets,us):
  nonlocal nodes
  nodes+=1
  if r==10:
   vs=[next(v for v in range(3) if bits>>v&1) for bits in sets]
   return us,vs
  for u in range(3):
   nxt=[sets[c]&~(1<<((2-A[r][c]-u)%3)) for c in range(10)]
   if all(nxt):
    got=dfs(r+1,nxt,us+[u])
    if got is not None:return got
  return None
 result=dfs(1,allowed,[0]);return result,nodes
records=[];counts={'binary':0,'nonbinary':0};maxnodes=0
for i,pair in enumerate(pairs):
 for s in (1,2):
  A=[[(mask(pair['first'],r,c)+s*mask(pair['second'],r,c))%3 for c in range(10)] for r in range(10)]
  result,nodes=solve(A);maxnodes=max(maxnodes,nodes)
  if result is None:
   counts['nonbinary']+=1;records.append({'pair_index_0based':i,'slope':s,'nodes':nodes,'binary':False})
  else:
   u,v=result;assert all((A[r][c]+u[r]+v[c])%3!=2 for r in range(10) for c in range(10))
   counts['binary']+=1;records.append({'pair_index_0based':i,'slope':s,'nodes':nodes,'binary':True,'row_gauge':u,'column_gauge':v})
print('exact binary-gauge census',counts,'maxnodes',maxnodes,flush=True)
(P/'frontier-20261028-q18-binary-gauge-census-result-v1.json').write_text(json.dumps({'counts':counts,'records':records,
 'scope':'352 literal two-mask examples, not all BH18'},indent=2,sort_keys=True)+'\n')
