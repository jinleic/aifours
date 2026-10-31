#!/usr/bin/env python3
"""Independent Q(zeta5) halfgraph/root/DFS replay for all q10 K orders."""
from functools import lru_cache
from itertools import combinations,permutations
from pathlib import Path
import json
P=Path(__file__).resolve().parent
lines=(P/'frontier-20261028-aalto-bh10-10-catalog-v1.txt').read_text().splitlines();assert len(lines)==51
cert=json.loads((P/'frontier-20261028-aalto-q10-certificate-v1.json').read_text())
five=[(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1),(-1,-1,-1,-1)]
# zeta10=-zeta5^3.
pw=[tuple((-1)**e*x for x in five[(3*e)%5])for e in range(10)]
def zero(v):return all(sum(pw[x%10][j] for x in v)==0 for j in range(4))
def matching(adj):
 @lru_cache(None)
 def go(left):
  if not left:return True
  a=min(left);return any(b in adj[a] and go(left-{a,b}) for b in left-{a})
 return go(frozenset(range(10)))
matrices=[];candidate=[];halves=0
for idx,line in enumerate(lines,1):
 assert len(line)==106 and line[:6]=='BH1:::'
 H=[[ord(line[6+10*t+c])-48 for c in range(10)]for t in range(10)]
 assert all(0<=v<10 for row in H for v in row)
 for c,d in combinations(range(10),2):assert zero([H[t][d]-H[t][c] for t in range(10)])
 matrices.append(H)
 for E in combinations(range(10),5):
  adj=[set() for _ in range(10)]
  for c,d in combinations(range(10),2):
   if zero([H[t][d]-H[t][c] for t in E]):adj[c].add(d);adj[d].add(c)
  if matching(adj):
   halves+=1
   if 0 in E:candidate.append((idx,E))
assert halves==56 and len(candidate)==28
assert [(r['catalog_index_1based'],tuple(r['even_half']))for r in cert['records']]==candidate
orders=roots=branches=nodes=0
for record in cert['records']:
 idx=record['catalog_index_1based'];E=tuple(record['even_half']);H=matrices[idx-1]
 digits=record['root_digits'];trees=record['branch_trees'];assert len(digits)==2880
 assert {str(i)for i,v in enumerate(digits)if v=='0'}==set(trees)
 ev=[t for t in E if t];od=sorted(set(range(10))-set(E));j=0
 for a in permutations(ev):
  for b in permutations(od):
   order=[0,b[0],a[0],b[1],a[1],b[2],a[2],b[3],a[3],b[4]]
   @lru_cache(None)
   def orth(r,c,s,d):return zero([(s-r)*t+H[order[t]][d]-H[order[t]][c]for t in range(10)])
   dig=digits[j]
   if dig!='0':
    assert dig in '123456789';r=int(dig)
    assert all(not orth(0,0,r,d)for d in range(1,10));roots+=1
   else:
    branches+=1
    def replay(tree,assigned,used):
     global nodes
     nodes+=1
     assert len(assigned)<10 and isinstance(tree,list) and len(tree)==2
     r,children=tree;assert isinstance(r,int) and 0<r<10 and r not in assigned
     available=[d for d in range(1,10)if d not in used and all(orth(s,c,r,d)for s,c in assigned.items())]
     got=[entry[0]for entry in children];assert got==available,(idx,E,j,r,got,available)
     for d,subtree in children:replay(subtree,{**assigned,r:d},used|{d})
    replay(trees[str(j)],{0:0},{0})
   j+=1;orders+=1
 assert j==2880
 print('PASS q10 class',idx,'E',E,'2880 proofs',flush=True)
assert orders==80640 and roots==21792 and branches==58848 and nodes==cert['tree_nodes']
out={'matrices':51,'matching_halves':halves,'normalized_halves':len(candidate),'orders':orders,
 'root_empty':roots,'branches':branches,'tree_nodes':nodes,
 'scope':'exact literal q10 no-transversal replay; catalog completeness imported'}
(P/'frontier-20261028-aalto-q10-certificate-replay-result-v1.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print('PASS',out,flush=True)
