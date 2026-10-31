#!/usr/bin/env python3
"""Exact compatible rectangle subsets and binary-gauge q18 specializations."""
from collections import Counter
from itertools import combinations,product
from pathlib import Path
import json,time
P=Path(__file__).resolve().parent
lines=(P/'frontier-20261028-aalto-bh10-6-catalog-v1.txt').read_text().splitlines()
fams=json.loads((P/'frontier-20261028-bh6-rectangle-families-v1.json').read_text())['records'];six=[(1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1)]
def zero6(v):return all(sum(six[x%6][j] for x in v)==0 for j in range(2))
def mask(f):return [[int(t in f['rows'] and c in f['columns']) for c in range(10)] for t in range(10)]
def compat(H,M):
 for r,s in combinations(range(10),2):
  groups={}
  for c in range(10):groups.setdefault(tuple(x[r][c]-x[s][c] for x in M),[]).append(H[r][c]-H[s][c])
  if not all(zero6(v) for v in groups.values()):return False
 return True
def binary(A):
 allowed=[7^(1<<((2-A[0][c])%3)) for c in range(10)]
 def go(r,sets,u):
  if r==10:return u,[next(j for j in range(3) if b>>j&1) for b in sets]
  for x in range(3):
   n=[sets[c]&~(1<<((2-A[r][c]-x)%3)) for c in range(10)]
   if all(n):
    v=go(r+1,n,u+[x])
    if v:return v
  return None
 return go(1,allowed,[0])
start=time.monotonic();hist=Counter();special=0;nonbinary_total=0;nonbinary=[];witnesses=[];classhist=[]
for rec in fams:
 idx=rec['class'];line=lines[idx-1];H=[[ord(line[6+10*t+c])-48 for c in range(10)] for t in range(10)]
 F=rec['families'];M=list(map(mask,F));per=Counter()
 def visit(chosen,offset):
  global special,nonbinary_total
  if chosen:
   k=len(chosen);hist[k]+=1;per[k]+=1
   for rest in product((1,2),repeat=k-1):
    co=(1,)+rest;A=[[sum(co[j]*M[chosen[j]][r][c] for j in range(k))%3 for c in range(10)] for r in range(10)]
    g=binary(A);special+=1
    item={'class':idx,'mask_indices':chosen[:],'coefficients':co}
    if g is None:
     nonbinary_total+=1
     if len(nonbinary)<1000:item['rectangles']=[F[i] for i in chosen];nonbinary.append(item)
    else:
     u,v=g;assert all((A[r][c]+u[r]+v[c])%3!=2 for r in range(10) for c in range(10))
     witnesses.append({**item,'row_gauge':u,'column_gauge':v})
  for j in range(offset,len(M)):
   new=chosen+[j]
   if compat(H,[M[i] for i in new]):visit(new,j+1)
 visit([],0);classhist.append({'class':idx,'subset_counts':dict(per)})
 if per:print('class',idx,'subsets',dict(per),'nonbinary',nonbinary_total,flush=True)
out={'scope':'literal 34 BH6 reps, normalized simultaneous affine rectangles; no global arbitrary-mask claim',
 'subset_size_histogram':dict(hist),'specializations':special,'nonbinary_count':nonbinary_total,'nonbinary_examples':nonbinary,
 'binary_gauge_witnesses':witnesses,'class_histogram':classhist,'elapsed_seconds':time.monotonic()-start}
(P/'frontier-20261028-q18-multirect-all-result-v1.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print('DONE subsets',dict(hist),'specializations',special,'nonbinary',nonbinary_total,flush=True)
