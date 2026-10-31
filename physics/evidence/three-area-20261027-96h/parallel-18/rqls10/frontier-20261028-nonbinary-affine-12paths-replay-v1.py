#!/usr/bin/env python3
"""Independent Q(sqrt(-3))/Q(zeta8,zeta9) replay for 12 selected paths."""
from fractions import Fraction as Q
from functools import lru_cache
from itertools import combinations
from pathlib import Path
import json,time
P=Path(__file__).resolve().parent
cases=json.loads((P/'frontier-20261028-q18-nonbinary-twentyfour-v1.json').read_text())['records']
triage=json.loads((P/'frontier-20261028-nonbinary-affine-24paths-result-v1.json').read_text())['records']
selected=[x['case'] for x in triage if x['status']=='no_halfmatch_all_phases'];assert selected==list(range(4))+list(range(12,20))
lines=(P/'frontier-20261028-aalto-bh10-6-catalog-v1.txt').read_text().splitlines()
Z=(Q(0),Q(0));O=(Q(1),Q(0))
def add(a,b):return a[0]+b[0],a[1]+b[1]
def sub(a,b):return a[0]-b[0],a[1]-b[1]
def mul(a,b):return a[0]*b[0]-3*a[1]*b[1],a[0]*b[1]+a[1]*b[0]
def conj(a):return a[0],-a[1]
def div(a,b):
 n=b[0]*b[0]+3*b[1]*b[1];assert n>0
 v=mul(a,conj(b));return v[0]/n,v[1]/n
def trim(a):
 a=list(a)
 while a and a[-1]==Z:a.pop()
 return a
def rem(a,b):
 a=trim(a);b=trim(b)
 while a and len(a)>=len(b):
  k=len(a)-len(b);v=div(a[-1],b[-1])
  for j,x in enumerate(b):a[k+j]=sub(a[k+j],mul(v,x))
  a=trim(a)
 return a
def gcd(a,b):
 a,b=trim(a),trim(b)
 while b:a,b=b,rem(a,b)
 return [div(x,a[-1]) for x in a] if a else []
six=[];u=(Q(1,2),Q(1,2));z=O
for k in range(6):six.append(z);z=mul(z,u)
assert z==O
@lru_cache(None)
def order72(poly):
 g=gcd(poly,tuple(conj(x) for x in reversed(poly)))
 return len(g)<=1 or not rem([(-Q(1),Q(0))]+[Z]*71+[O],g)
@lru_cache(None)
def matching(adj,mask=1023):
 if not mask:return True
 b=mask&-mask;i=b.bit_length()-1;left=mask^b;opts=adj[i]&left
 while opts:
  c=opts&-opts;opts-=c
  if matching(adj,left^c):return True
 return False
eight=[]
for e in range(8):
 a=[0]*4;a[e%4]=1 if e<4 else -1;eight.append(a)
nine=[]
for e in range(9):
 a=[0]*6
 if e<6:a[e]=1
 else:a[e-6]-=1;a[e-3]-=1
 nine.append(a)
pw=[tuple(a*b for a in eight[e%8] for b in nine[(8*e)%9])for e in range(72)]
def zero72(v):return all(sum(pw[x%72][j] for x in v)==0 for j in range(24))
results=[];start=time.monotonic()
for ix in selected:
 D=cases[ix];line=lines[D['class']-1];H=[[ord(line[6+10*t+c])-48 for c in range(10)]for t in range(10)]
 M=[[[int(t in m['rows'] and c in m['columns'])for c in range(10)]for t in range(10)]for m in D['rectangles']]
 R=[[sum(D['coefficients'][j]*M[j][t][c] for j in range(4))for c in range(10)]for t in range(10)];N=max(map(max,R));assert N==6
 for r,s in combinations(range(10),2):
  bins={}
  for c in range(10):bins.setdefault(R[r][c]-R[s][c],[]).append((H[r][c]-H[s][c])%6)
  assert all(sum((six[x][0] for x in v),Q(0))==0 and sum((six[x][1] for x in v),Q(0))==0 for v in bins.values())
 polys=set();generic=0
 for E in combinations(range(10),5):
  adj=[0]*10
  for c,d in combinations(range(10),2):
   v=[Z]*(2*N+1)
   for t in E:
    k=R[t][d]-R[t][c]+N;v[k]=add(v[k],six[(H[t][d]-H[t][c])%6])
   while v and v[-1]==Z:v.pop()
   while v and v[0]==Z:v.pop(0)
   if not v:adj[c]|=1<<d;adj[d]|=1<<c
   else:
    lead=v[-1];key=tuple(div(x,lead) for x in v);polys.add(key);assert order72(key)
  assert not matching(tuple(adj))
 for s in range(72):
  K=[[(12*H[t][c]+s*R[t][c])%72 for c in range(10)]for t in range(10)]
  for E in combinations(range(10),5):
   adj=[0]*10
   for c,d in combinations(range(10),2):
    if zero72([K[t][d]-K[t][c] for t in E]):adj[c]|=1<<d;adj[d]|=1<<c
   assert not matching(tuple(adj)),(ix,s,E)
 results.append({'case':ix,'class':D['class'],'nonzero_projective_halfpolynomials':len(polys),'q72_halfgraphs':72*252})
 print('PASS case',ix,'polys',len(polys),'18144 q72 halfgraphs',flush=True)
out={'cases':results,'count':len(results),'total_halfpolynomials':len(results)*252*45,
     'total_q72_halfgraphs':len(results)*72*252,'scope':'12 literal paths; not all24 or full parameter tori',
     'elapsed_seconds':time.monotonic()-start}
(P/'frontier-20261028-nonbinary-affine-12paths-replay-result-v1.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print('PASS 12 paths',out['total_halfpolynomials'],'halfpolynomials',out['total_q72_halfgraphs'],'endpoint graphs')
