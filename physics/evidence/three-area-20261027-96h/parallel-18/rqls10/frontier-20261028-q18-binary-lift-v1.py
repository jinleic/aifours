#!/usr/bin/env python3
"""Find and exactly validate one genuinely q18 affine lift of a BH(10,6)."""
from itertools import combinations
from pathlib import Path
import json
P=Path(__file__).resolve().parent
lines=(P/'frontier-20261028-aalto-bh10-6-catalog-v1.txt').read_text().splitlines();assert len(lines)==34
six=[(1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1)]
def zero6(v):return all(sum(six[x%6][j] for x in v)==0 for j in range(2))
def makepow(phi,n):
 deg=len(phi)-1;out=[]
 for k in range(n):
  a=[0]*k+[1]
  for j in range(len(a)-1,deg-1,-1):
   v=a[j]
   for i,c in enumerate(phi):a[j-deg+i]-=v*c
  out.append(tuple((a+[0]*deg)[:deg]))
 return out
pw=makepow([1,0,0,-1,0,0,1],18)
def zero18(v):return all(sum(pw[x%18][j] for x in v)==0 for j in range(6))
found=None
for idx,line in enumerate(lines,1):
 H=[[ord(line[6+10*t+c])-48 for c in range(10)] for t in range(10)]
 assert all(zero6([H[t][d]-H[t][c] for t in range(10)]) for c,d in combinations(range(10),2))
 for bits in range(1,1023):
  C=[j for j in range(10) if bits>>j&1]
  if not 2<=len(C)<=8:continue
  adj=[set() for _ in range(10)]
  for r,s in combinations(range(10),2):
   if not zero6([H[r][j]-H[s][j] for j in C]):adj[r].add(s);adj[s].add(r)
  unseen=set(range(10));components=[]
  while unseen:
   stack=[min(unseen)];comp=set()
   while stack:
    x=stack.pop()
    if x in comp:continue
    comp.add(x);stack.extend(adj[x]-comp)
   unseen-=comp;components.append(comp)
  if len(components)>1:
   R=sorted(components[0]);found=(idx,H,R,C);break
 if found:break
assert found is not None
idx,H,R,C=found;A=[[ (3*H[t][c]+int(t in R and c in C))%18 for c in range(10)] for t in range(10)]
assert all(zero18([A[t][d]-A[t][c] for t in range(10)]) for c,d in combinations(range(10),2))
# A cross-ratio exponent not divisible by3 cannot belong to mu6, hence no row/column phase gauges can reduce K to BH(10,6).
r=R[0];s=next(t for t in range(10) if t not in R);c=C[0];d=next(j for j in range(10) if j not in C)
cross=(A[r][c]+A[s][d]-A[r][d]-A[s][c])%18
assert cross%3!=0
# All possible Fourier-character ratios have m=0 or5 since gcd(10,18)=2.
repeats=[]
for c,d in combinations(range(10),2):
 for m in (0,5):
  if len({(5*(A[t][d]-A[t][c])-9*m*t)%90 for t in range(10)})==1:repeats.append((c,d,m))
print('q18 affine example class',idx,'rows',R,'columns',C,'crossratio_exponent',cross,'repeated_pairs',len(repeats),flush=True)
out={'catalog_class_1based':idx,'source_q':6,'target_q':18,'rows':R,'columns':C,
     'crossratio_exponent':cross,'K_exponents':A,'m0_or5_repeated_pairs':repeats,
     'scope':'new q18 affine Hadamard; maximal QLS needs independent vector check'}
(P/'frontier-20261028-q18-binary-lift-result-v1.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
