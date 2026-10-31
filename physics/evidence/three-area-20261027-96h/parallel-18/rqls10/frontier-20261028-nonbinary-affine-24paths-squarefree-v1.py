#!/usr/bin/env python3
"""Exact reciprocal-gcd/order72 scan of 24 literal 4-mask paths."""
from collections import Counter
from functools import lru_cache
from itertools import combinations
from pathlib import Path
import importlib.util,json,time
P=Path(__file__).resolve().parent
sp=importlib.util.spec_from_file_location('f',P/'frontier-20261028-q18-affine-unitroots-v1.py');f=importlib.util.module_from_spec(sp);sp.loader.exec_module(f)
data=json.loads((P/'frontier-20261028-q18-nonbinary-twentyfour-v1.json').read_text())['records']
lines=(P/'frontier-20261028-aalto-bh10-6-catalog-v1.txt').read_text().splitlines()
phi72=[1]+[0]*11+[-1]+[0]*11+[1];pw=[]
for e in range(72):
 a=[0]*e+[1]
 for k in range(len(a)-1,23,-1):
  v=a[k]
  for j,x in enumerate(phi72):a[k-24+j]-=v*x
 pw.append(tuple((a+[0]*24)[:24]))
def zero(v):
 for j in range(24):
  if sum(pw[x%72][j] for x in v):return False
 return True
@lru_cache(None)
def gcd72(p):
 g=f.gcd(list(p),[f.conj(x) for x in reversed(p)])
 if len(g)<=1:return True
 derivative=[tuple(v*i for v in g[i]) for i in range(1,len(g))]
 repeated=f.gcd(g,derivative)
 squarefree,rem=f.poldiv(g,repeated);assert not rem
 _,rem=f.poldiv([f.neg(f.O)]+[f.Z]*71+[f.O],squarefree)
 return not rem
@lru_cache(None)
def matching(adj,mask=1023):
 if not mask:return True
 bit=mask&-mask;i=bit.bit_length()-1;rem=mask^bit;can=adj[i]&rem
 while can:
  b=can&-can;can-=b
  if matching(adj,rem^b):return True
 return False
res=[];start=time.monotonic()
for D in data:
 line=lines[D['class']-1];H=[[ord(line[6+10*t+c])-48 for c in range(10)]for t in range(10)]
 R=[[sum(co*int(t in m['rows'] and c in m['columns']) for co,m in zip(D['coefficients'],D['rectangles']))for c in range(10)]for t in range(10)]
 N=max(map(max,R));assert N==6;unique=set();generic=0;bad=0
 for E in combinations(range(10),5):
  adj=[0]*10
  for c,d in combinations(range(10),2):
   v=[f.Z]*(2*N+1)
   for t in E:
    j=R[t][d]-R[t][c]+N;v[j]=f.add(v[j],tuple(map(f.Q,f.six[(H[t][d]-H[t][c])%6])))
   while v and v[-1]==f.Z:v.pop()
   while v and v[0]==f.Z:v.pop(0)
   if not v:adj[c]|=1<<d;adj[d]|=1<<c
   else:
    lead=v[-1];ky=tuple(f.div(x,lead) for x in v);unique.add(ky)
    if not gcd72(ky):bad+=1
  if matching(tuple(adj)):generic+=1
 phases=[]
 if generic==0 and bad==0:
  for s in range(72):
   K=[[(12*H[t][c]+s*R[t][c])%72 for c in range(10)]for t in range(10)]
   for E in combinations(range(10),5):
    adj=[0]*10
    for c,d in combinations(range(10),2):
     if zero([K[t][d]-K[t][c] for t in E]):adj[c]|=1<<d;adj[d]|=1<<c
    if matching(tuple(adj)):phases.append({'phase':s,'even_half':list(E)});break
 status='no_halfmatch_all_phases' if generic==0 and bad==0 and not phases else 'unresolved'
 rec={'case':D['case'],'class':D['class'],'unique':len(unique),'generic_matching_halves':generic,
      'polynomial_nondivisibility':bad,'endpoint_matching_phases':phases,'status':status}
 res.append(rec);print('case',D['case'],'unique',len(unique),'generic',generic,'bad',bad,'phases',len(phases),'status',status,flush=True)
out={'scope':'24 literal one-parameter diagonal paths, not full four-parameter families','records':res,
     'status_counts':dict(Counter(x['status'] for x in res)),'elapsed_seconds':time.monotonic()-start}
(P/'frontier-20261028-nonbinary-affine-24paths-squarefree-result-v1.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print('DONE',out['status_counts'],flush=True)
