#!/usr/bin/env python3
"""Exact binary rectangle-affine family census of 34 literal BH10,6 matrices."""
from collections import Counter
from itertools import combinations
from pathlib import Path
import json
P=Path(__file__).resolve().parent
lines=(P/'frontier-20261028-aalto-bh10-6-catalog-v1.txt').read_text().splitlines();assert len(lines)==34
six=[(1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1)]
def zero(v):return all(sum(six[x%6][j] for x in v)==0 for j in range(2))
allrec=[];hist=Counter()
for idx,line in enumerate(lines,1):
 assert len(line)==106 and line[:6]=='BH1::6'
 H=[[ord(line[6+10*t+c])-48 for c in range(10)] for t in range(10)]
 for r,s in combinations(range(10),2):assert zero([H[r][c]-H[s][c] for c in range(10)])
 count=0;first=None;families=[]
 for cmask in range(1,1023,2): # select one from C / complement, require 0 in C
  C=[c for c in range(10) if cmask>>c&1]
  adj=[set() for _ in range(10)]
  for r,s in combinations(range(10),2):
   if not zero([H[r][c]-H[s][c] for c in C]):adj[r].add(s);adj[s].add(r)
  left=set(range(10));comps=[]
  while left:
   stack=[min(left)];comp=set()
   while stack:
    t=stack.pop()
    if t in comp:continue
    comp.add(t);stack.extend(adj[t]-comp)
   left-=comp;comps.append(comp)
  if len(comps)<2:continue
  for sel in range(1,2**len(comps)-1):
   R=set().union(*(comps[j] for j in range(len(comps)) if sel>>j&1))
   if 0 not in R:continue
   count+=1
   families.append({"rows":sorted(R),"columns":C})
   if first is None:first={'rows':sorted(R),'columns':C,'component_sizes':[len(x) for x in comps]}
 hist[count]+=1;allrec.append({'class':idx,'rectangle_count':count,'first':first,'families':families})
 print('class',idx,'normalized_rectangle_families',count,flush=True)
out={'scope':'literal catalog, exact nontrivial rectangle families modulo R/C complement only; no inequivalence claim',
 'histogram':dict(hist),'total_normalized_rectangles':sum(r['rectangle_count'] for r in allrec),'records':allrec}
(P/'frontier-20261028-bh6-rectangle-families-v1.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print('total',out['total_normalized_rectangles'],'histogram',dict(hist),flush=True)
