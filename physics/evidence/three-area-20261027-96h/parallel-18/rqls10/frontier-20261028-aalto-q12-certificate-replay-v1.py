#!/usr/bin/env python3
"""Independent halfgraph and root/DFS-tree replay in a Q(i,zeta3,zeta5) basis."""
from functools import lru_cache
from itertools import combinations,permutations
from pathlib import Path
import json
P=Path(__file__).resolve().parent
lines=(P/'frontier-20261028-aalto-bh10-12-catalog-v1.txt').read_text().splitlines();assert len(lines)==577
cert=json.loads((P/'frontier-20261028-aalto-q12-certificate-v1.json').read_text())
four=[(1,0),(0,1),(-1,0),(0,-1)];three=[(1,0),(0,1),(-1,-1)]
five=[(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1),(-1,-1,-1,-1)]
# zeta12=i^3*zeta3; zeta60=i^3*zeta3^2*zeta5^3.
p12=[tuple(a*b for a in four[(3*e)%4] for b in three[e%3]) for e in range(12)]
p60=[tuple(a*b*c for a in four[(3*e)%4] for b in three[(2*e)%3] for c in five[(3*e)%5]) for e in range(60)]
def zero(v,table):return all(sum(table[x%len(table)][j] for x in v)==0 for j in range(len(table[0])))
def matching(adj):
 @lru_cache(None)
 def rec(left):
  if not left:return True
  a=min(left);return any(b in adj[a] and rec(left-{a,b}) for b in left-{a})
 return rec(frozenset(range(10)))
matrices=[];candidate=[];halves=0
for idx,line in enumerate(lines,1):
 assert len(line)==106 and line[:6]=='BH1::<'
 H=[[ord(line[6+10*t+c])-48 for c in range(10)] for t in range(10)]
 assert all(0<=x<12 for row in H for x in row)
 for c,d in combinations(range(10),2):assert zero([H[t][d]-H[t][c] for t in range(10)],p12)
 matrices.append(H)
 for E in combinations(range(10),5):
  adj=[set() for _ in range(10)]
  for c,d in combinations(range(10),2):
   if zero([H[t][d]-H[t][c] for t in E],p12):adj[c].add(d);adj[d].add(c)
  if matching(adj):
   halves+=1
   if 0 in E:candidate.append((idx,E))
 if idx%100==0:print('catalog matrices',idx,'matching halves',halves,flush=True)
assert halves==330 and len(candidate)==165
assert [(r['catalog_index_1based'],tuple(r['even_half'])) for r in cert['records']]==candidate
orders=roots=branches=nodes=0
for record in cert['records']:
 idx=record['catalog_index_1based'];E=tuple(record['even_half']);H=matrices[idx-1]
 digits=record['root_digits'];trees=record['branch_trees'];assert len(digits)==2880
 assert {str(i) for i,v in enumerate(digits) if v=='0'}==set(trees)
 ev=[t for t in E if t];od=sorted(set(range(10))-set(E));j=0
 for a in permutations(ev):
  for b in permutations(od):
   order=[0,b[0],a[0],b[1],a[1],b[2],a[2],b[3],a[3],b[4]]
   @lru_cache(None)
   def orth(r,c,s,d):
    vals=[(6*(s-r)*t+5*(H[order[t]][d]-H[order[t]][c]))%60 for t in range(10)]
    return zero(vals,p60)
   dig=digits[j]
   if dig!='0':
    assert dig in '123456789';r=int(dig)
    assert all(not orth(0,0,r,d) for d in range(1,10));roots+=1
   else:
    branches+=1
    def replay(tree,assigned,used):
     global nodes
     nodes+=1
     assert len(assigned)<10 and isinstance(tree,list) and len(tree)==2
     r,children=tree;assert isinstance(r,int) and 0<r<10 and r not in assigned
     available=[d for d in range(1,10) if d not in used and all(orth(s,c,r,d) for s,c in assigned.items())]
     got=[entry[0] for entry in children]
     assert got==available,(idx,E,j,r,got,available)
     for d,subtree in children:replay(subtree,{**assigned,r:d},used|{d})
    replay(trees[str(j)],{0:0},{0})
   j+=1;orders+=1
 assert j==2880
 print('PASS q12 class',idx,'E',E,'2880 certificates',flush=True)
assert orders==475200 and roots==472584 and branches==2616
assert nodes==cert['tree_nodes']
out={'matrices':577,'matching_halves':halves,'normalized_halves':len(candidate),
     'orders':orders,'root_empty':roots,'branches':branches,'tree_nodes':nodes,
     'scope':'independent exact Q(i,zeta3,zeta5) replay; catalog completeness imported'}
(P/'frontier-20261028-aalto-q12-certificate-replay-result-v1.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print('PASS',out,flush=True)
