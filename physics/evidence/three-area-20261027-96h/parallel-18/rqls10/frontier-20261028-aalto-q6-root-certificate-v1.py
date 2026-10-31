#!/usr/bin/env python3
"""Create exact per-order row obstruction for all q6 matching halves."""
from itertools import combinations,permutations
from pathlib import Path
import json
P=Path(__file__).resolve().parent
lines=(P/'frontier-20261028-aalto-bh10-6-catalog-v1.txt').read_text().splitlines();assert len(lines)==34
candidates=[]
for line in (P/'frontier-20261028-aalto-q6-candidate-halves-v1.txt').read_text().splitlines():
 a=list(map(int,line.split()));assert len(a)==6 and a[1]==0;candidates.append((a[0],tuple(a[1:])))
assert len(candidates)==25 and len(set(candidates))==25
phi=[1,1,0,-1,-1,-1,0,1,1];pw=[]
for n in range(30):
 x=[0]*n+[1]
 for j in range(len(x)-1,7,-1):
  v=x[j]
  for k,c in enumerate(phi):x[j-8+k]-=v*c
 pw.append(tuple((x+[0]*8)[:8]))
def zero(e):
 for j in range(8):
  if sum(pw[x][j] for x in e)!=0:return False
 return True
records=[];total=0
for idx,E in candidates:
 line=lines[idx-1];assert len(line)==106 and line[:6]=='BH1::6'
 H=[[ord(line[6+10*t+c])-48 for c in range(10)] for t in range(10)]
 ev=[t for t in E if t!=0];od=sorted(set(range(10))-set(E));witness=[]
 for a in permutations(ev):
  for b in permutations(od):
   order=[0,b[0],a[0],b[1],a[1],b[2],a[2],b[3],a[3],b[4]]
   found=None
   for r in range(1,10):
    if all(not zero([(3*r*t+5*(H[order[t]][d]-H[order[t]][0]))%30 for t in range(10)]) for d in range(1,10)):
     found=r;break
   assert found is not None,('no row obstruction',idx,E,order)
   witness.append(str(found));total+=1
 assert len(witness)==2880
 records.append({'catalog_index_1based':idx,'even_half':list(E),
                 'ordering':'lexicographic permutations of four nonzero even rows, then five odd rows',
                 'obstructed_row_digits':''.join(witness)})
print('q6 per-order certificate',len(records),'normalized halves',total,'orders',flush=True)
assert total==72000
(P/'frontier-20261028-aalto-q6-root-certificate-v1.json').write_text(json.dumps({'records':records,
 'scope':'each digit is a row with no orthogonal different column to (row0,col0)'},separators=(',',':'),sort_keys=True)+'\n')
