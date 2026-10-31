#!/usr/bin/env python3
"""Exact q6 endpoint halfgraphs and per-order transversal obstruction for eight paths."""
from itertools import combinations,permutations
from functools import lru_cache
from pathlib import Path
import json
P=Path(__file__).resolve().parent
cases=json.loads((P/'frontier-20261028-q18-nonbinary-twentyfour-v1.json').read_text())['records'];lines=(P/'frontier-20261028-aalto-bh10-6-catalog-v1.txt').read_text().splitlines()
six=[(1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1)]
def zero6(v):return all(sum(six[x%6][j] for x in v)==0 for j in range(2))
phi=[1,1,0,-1,-1,-1,0,1,1];pw=[]
for e in range(30):
 a=[0]*e+[1]
 for k in range(len(a)-1,7,-1):
  v=a[k]
  for j,x in enumerate(phi):a[k-8+j]-=v*x
 pw.append(tuple((a+[0]*8)[:8]))
def zero30(v):return all(sum(pw[x%30][j] for x in v)==0 for j in range(8))
def matching(adj):
 @lru_cache(None)
 def go(mask):
  if not mask:return True
  bit=mask&-mask;i=bit.bit_length()-1;rest=mask^bit;opts=adj[i]&rest
  while opts:
   b=opts&-opts;opts-=b
   if go(rest^b):return True
  return False
 return go(1023)
records=[];total=0
for ix in range(4,12):
 D=cases[ix];line=lines[D['class']-1];H=[[ord(line[6+10*t+c])-48 for c in range(10)]for t in range(10)]
 R=[[sum(co*int(t in m['rows'] and c in m['columns'])for co,m in zip(D['coefficients'],D['rectangles']))for c in range(10)]for t in range(10)]
 for s in range(6):
  K=[[(H[t][c]+s*R[t][c])%6 for c in range(10)]for t in range(10)]
  for c,d in combinations(range(10),2):assert zero6([K[t][d]-K[t][c] for t in range(10)])
  halves=[]
  for E in combinations(range(10),5):
   adj=[0]*10
   for c,d in combinations(range(10),2):
    if zero6([K[t][d]-K[t][c] for t in E]):adj[c]|=1<<d;adj[d]|=1<<c
   if matching(tuple(adj)):halves.append(E)
  for E in halves:
   if 0 not in E:continue
   ev=[t for t in E if t];od=sorted(set(range(10))-set(E));digits=[]
   for a in permutations(ev):
    for b in permutations(od):
     order=[0,b[0],a[0],b[1],a[1],b[2],a[2],b[3],a[3],b[4]];bad=None
     for r in range(1,10):
      if all(not zero30([3*r*t+5*(K[order[t]][d]-K[order[t]][0])for t in range(10)])for d in range(1,10)):
       bad=r;break
     assert bad is not None,('NO_ROOT_OBSTRUCTION',ix,s,E,order)
     digits.append(str(bad));total+=1
   assert len(digits)==2880
   records.append({'case':ix,'phase6':s,'even_half':list(E),'digits':''.join(digits)})
  print('case',ix,'phase',s,'matching halves',len(halves),flush=True)
(P/'frontier-20261028-nonbinary-eight-endpoints-v1.json').write_text(json.dumps({'records':records,'orders':total,
 'scope':'eight literal paths, six q6 phase endpoints, per-order root-row obstruction'},separators=(',',':'),sort_keys=True)+'\n')
print('DONE normalized matching half cases',len(records),'row orders',total,flush=True)
