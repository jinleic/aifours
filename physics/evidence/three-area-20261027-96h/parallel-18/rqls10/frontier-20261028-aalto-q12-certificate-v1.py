#!/usr/bin/env python3
"""Produce exact root-row and complete DFS certificates for all q12 half orders."""
from itertools import permutations
from functools import lru_cache
from pathlib import Path
import json
P=Path(__file__).resolve().parent
lines=(P/'frontier-20261028-aalto-bh10-12-catalog-v1.txt').read_text().splitlines();assert len(lines)==577
candidates=[]
for line in (P/'frontier-20261028-aalto-q12-all-halves-v1.txt').read_text().splitlines():
 a=list(map(int,line.split()));assert len(a)==6 and a[1]==0;candidates.append((a[0],tuple(a[1:])))
assert len(candidates)==165 and len(set(candidates))==165
phi=[1,0,1,0,0,0,-1,0,-1,0,-1,0,0,0,1,0,1];pw=[]
for n in range(60):
 x=[0]*n+[1]
 for j in range(len(x)-1,15,-1):
  v=x[j]
  for k,c in enumerate(phi):x[j-16+k]-=v*c
 pw.append(tuple((x+[0]*16)[:16]))
def zero(e):
 for j in range(16):
  if sum(pw[x][j] for x in e)!=0:return False
 return True
records=[];total=rootempty=branched=nodes=0
for idx,E in candidates:
 line=lines[idx-1];assert len(line)==106 and line[:6]=='BH1::<'
 H=[[ord(line[6+10*t+c])-48 for c in range(10)] for t in range(10)]
 ev=[t for t in E if t!=0];od=sorted(set(range(10))-set(E));digits=[];trees={};ncase=0
 for a in permutations(ev):
  for b in permutations(od):
   order=[0,b[0],a[0],b[1],a[1],b[2],a[2],b[3],a[3],b[4]]
   @lru_cache(None)
   def orth(r,c,s,d):
    return zero([((s-r)*6*t+5*(H[order[t]][d]-H[order[t]][c]))%60 for t in range(10)])
   allowed={};empty=None
   for r in range(1,10):
    allowed[r]=[d for d in range(1,10) if orth(0,0,r,d)]
    if not allowed[r]:empty=r;break
   if empty is not None:digits.append(str(empty));rootempty+=1
   else:
    digits.append('0');branched+=1
    def prove(assigned,used):
     global nodes
     nodes+=1
     if len(assigned)==10:raise AssertionError(('TRANSVERSAL',idx,E,order,assigned))
     choices=[]
     for r in range(1,10):
      if r in assigned:continue
      avail=[d for d in allowed[r] if d not in used and all(orth(s,c,r,d) for s,c in assigned.items())]
      if not avail:return [r,[]]
      choices.append((len(avail),r,avail))
     _,r,avail=min(choices)
     return [r,[[d,prove({**assigned,r:d},used|{d})] for d in avail]]
    trees[str(ncase)]=prove({0:0},{0})
   ncase+=1;total+=1
 assert ncase==2880
 records.append({'catalog_index_1based':idx,'even_half':list(E),'root_digits':''.join(digits),'branch_trees':trees})
 print('q12 class',idx,'E',E,'branches',len(trees),'total orders',total,flush=True)
assert total==475200
out={'records':records,'total_orders':total,'root_empty':rootempty,'branched':branched,'tree_nodes':nodes,
 'scope':'root digits or exhaustive orthogonality branch trees; no maximality filter'}
(P/'frontier-20261028-aalto-q12-certificate-v1.json').write_text(json.dumps(out,separators=(',',':'),sort_keys=True)+'\n')
print('PASS certificate total',total,'rootempty',rootempty,'branched',branched,'tree_nodes',nodes,flush=True)
