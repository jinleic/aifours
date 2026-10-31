#!/usr/bin/env python3
"""Independent Phi10/half-graph/fixed-row replay for q10 catalog search."""
from itertools import combinations,permutations
from pathlib import Path
from functools import lru_cache
import json
P=Path(__file__).resolve().parent
lines=(P/'frontier-20261028-aalto-bh10-10-catalog-v1.txt').read_text().splitlines()
assert len(lines)==51
phi=[1,-1,1,-1,1]
def zero(values):
 a=[0]*10
 for x in values:a[x%10]+=1
 for k in range(9,3,-1):
  v=a[k]
  for j,c in enumerate(phi):a[k-4+j]-=v*c
 return not any(a[:4])
def pairable(vertices,adj):
 if not vertices:return True
 a=min(vertices)
 for b in sorted(vertices-{a}):
  if b in adj[a] and pairable(vertices-{a,b},adj):return True
 return False
survive=[];half_count=dup_half=0
for idx,line in enumerate(lines,1):
 assert len(line)==106 and line[:6]=='BH1:::'
 H=[[ord(line[6+10*t+c])-48 for c in range(10)] for t in range(10)]
 for c,d in combinations(range(10),2):assert zero([H[t][d]-H[t][c] for t in range(10)])
 for E in combinations(range(10),5):
  adj=[set() for _ in range(10)]
  for c,d in combinations(range(10),2):
   if zero([H[t][d]-H[t][c] for t in E]):adj[c].add(d);adj[d].add(c)
  if not pairable(set(range(10)),adj):continue
  half_count+=1;O=set(range(10))-set(E)
  collided=False
  for c,d in combinations(range(10),2):
   diff=[(H[t][d]-H[t][c])%10 for t in range(10)];x=diff[E[0]]
   if all(diff[t]==x for t in E) and all(diff[t]==(x+5)%10 for t in O):collided=True;break
  if collided:dup_half+=1
  elif 0 in E:survive.append((idx,E))
assert half_count==56 and dup_half==50
assert survive==[(1,(0,2,3,5,7)),(9,(0,2,3,5,7)),(18,(0,2,3,5,7))]
print('PASS 51 BH matrices; 56 matching halves, 50 immediate opposite-row collisions; 3 normalized surviving class/half pairs',flush=True)
results=[]
for idx,E in survive:
 H=[[ord(lines[idx-1][6+10*t+c])-48 for c in range(10)] for t in range(10)]
 rest=[t for t in E if t!=0];odd=sorted(set(range(10))-set(E))
 cases=dups=checked=root_empty=branches=nodes=0
 for ev in permutations(rest):
  for od in permutations(odd):
   order=[0,od[0],ev[0],od[1],ev[1],od[2],ev[2],od[3],ev[3],od[4]]
   cases+=1;duplicated=False
   for c,d in combinations(range(10),2):
    for m in range(10):
     if len({(H[order[t]][d]-H[order[t]][c]-m*t)%10 for t in range(10)})==1:
      duplicated=True;break
    if duplicated:break
   if duplicated:dups+=1;continue
   checked+=1
   @lru_cache(None)
   def orth(r,c,s,d):
    return zero([((s-r)*t+H[order[t]][d]-H[order[t]][c])%10 for t in range(10)])
   allowed=[None]+[{d for d in range(1,10) if orth(0,0,r,d)} for r in range(1,10)]
   if any(not allowed[r] for r in range(1,10)):root_empty+=1;continue
   branches+=1
   def search(r,used,chosen):
    global nodes
    nodes+=1
    if r==10:return chosen
    for d in sorted(allowed[r]-used):
     if all(orth(s,c,r,d) for s,c in enumerate(chosen)):
      got=search(r+1,used|{d},chosen+[d])
      if got is not None:return got
    return None
   answer=search(1,{0},[0])
   assert answer is None,('TARGET_CANDIDATE_REQUIRES_RECHECK',idx,order,answer)
 assert cases==2880 and checked+dups==cases
 print('class',idx,'cases',cases,'dups',dups,'checked',checked,'root_empty',root_empty,'branched',branches,'fixed_row_nodes',nodes,flush=True)
 results.append({'class':idx,'cases':cases,'duplicates':dups,'checked':checked,'root_empty':root_empty,'branched':branches,'fixed_row_nodes':nodes})
(P/'frontier-20261028-aalto-q10-independent-result-v1.json').write_text(json.dumps({'classes':results,'half_count':half_count,'dup_half':dup_half,
 'scope':'catalog-dependent restricted Fourier product; not general QLS'},indent=2,sort_keys=True)+'\n')
print('PASS independent exhaustive q10 replay; catalog completeness remains an imported claim')
