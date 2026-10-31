#!/usr/bin/env python3
"""Exact rectangle-affine families of 24 nonbinary BH10,18 examples."""
from collections import Counter
from itertools import combinations
from pathlib import Path
import json
P=Path(__file__).resolve().parent
cases=json.loads((P/'frontier-20261028-q18-nonbinary-twentyfour-v1.json').read_text())['records'];assert len(cases)==24
six=[(1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1)];pw=[]
for e in range(18):
 q,r=divmod(e,3);v=[0]*6;v[2*r],v[2*r+1]=six[q];pw.append(v)
def zero(v):return all(sum(pw[x%18][j] for x in v)==0 for j in range(6))
records=[];hist=Counter()
for case in cases:
 H=case['K_exponents_mod18'];families=[]
 for cm in range(1,1023,2):
  C=[c for c in range(10) if cm>>c&1];adj=[set() for _ in range(10)]
  for r,s in combinations(range(10),2):
   if not zero([H[r][c]-H[s][c] for c in C]):adj[r].add(s);adj[s].add(r)
  left=set(range(10));components=[]
  while left:
   stack=[min(left)];comp=set()
   while stack:
    x=stack.pop()
    if x in comp:continue
    comp.add(x);stack.extend(adj[x]-comp)
   left-=comp;components.append(comp)
  for sel in range(1,2**len(components)-1):
   R=set().union(*(components[i] for i in range(len(components)) if sel>>i&1))
   if 0 in R:families.append({'rows':sorted(R),'columns':C})
 hist[len(families)]+=1;records.append({'case':case['case'],'family_count':len(families),'families':families})
 print('case',case['case'],'q18 rectangle families',len(families),flush=True)
out={'scope':'24 literal BH18 examples; no full BH18 classification','histogram':dict(hist),
 'total':sum(x['family_count'] for x in records),'records':records}
(P/'frontier-20261028-q18-nonbinary-rectangle-v1.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print('total',out['total'],'histogram',dict(hist),flush=True)
