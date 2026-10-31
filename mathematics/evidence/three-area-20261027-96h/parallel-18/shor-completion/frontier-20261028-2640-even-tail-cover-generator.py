#!/usr/bin/env python3
"""Deterministic clique-cover generator for the n2640 tail gcd screen."""
from itertools import combinations
from math import gcd
from pathlib import Path
import json
n=2640;A={0,3,8,11};Y={0,1,7,13,14}
GA={gcd(a-b,n) for a,b in combinations(A,2)}
Q=[x for x in range(n) if all(x==y or gcd(x-y,n) not in GA for y in Y)]
N=len(Q);full=(1<<N)-1
adj=[sum(1<<j for j,y in enumerate(Q) if y!=x and gcd(x-y,n) in GA) for x in Q]
groups=[];left=set(range(N))
while left:
 best=None;score=None;validbest=None
 for i in left:
  valid=[j for j,g in enumerate(groups) if not g&(full^adj[i])]
  score_i=(len(groups)-len(valid),N-1-adj[i].bit_count(),-i)
  if score is None or score_i>score:best=i;score=score_i;validbest=valid
 if validbest:groups[max(validbest,key=lambda j:groups[j].bit_count())] |=1<<best
 else:groups.append(1<<best)
 left.remove(best)
cliques=[[Q[j] for j in range(N) if g>>j&1] for g in groups]
pairs=[(256,418),(415,253),(916,1078),(1075,913),
       (1576,1738),(1735,1573),(2236,2398),(2395,2233)]
out={'n':n,'Q_conflict_cliques':cliques,'P_mod3_1_conflict_pairs':pairs}
p=Path(__file__).with_name('frontier-20261028-2640-even-tail-cover-v1.json')
if p.exists():raise FileExistsError('refuse overwrite')
p.write_text(json.dumps(out,sort_keys=True,separators=(',',':'))+'\n')
print(json.dumps({'Q_candidates':N,'cliques':len(cliques),'bytes':p.stat().st_size}))
