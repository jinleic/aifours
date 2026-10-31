#!/usr/bin/env python3
"""Exact finite SR2-spanning certificates for coordinate-filtered CH⊗CH ranges.
Any failed bounded search is INCONCLUSIVE, not a counterexample.
"""
from itertools import product,combinations
from collections import Counter
import json
edges=(((1,0),(0,2)),((2,0),(1,2)),((0,0),(2,1)),((0,1),(2,2)))
coords=[tuple((3*a+c,3*b+d) for (a,b),(c,d) in product(x,y)) for x,y in product(edges,repeat=2)]
flat=[x for q in coords for x in q]
assert len(flat)==len(set(flat))==64
subsets=list(combinations(range(9),4));R=list(combinations(range(4),3)); minors=list(product(R,R))
def det(m,r,c):
 a,b,d=r;x,y,z=c
 return (m[4*a+x]*(m[4*b+y]*m[4*d+z]-m[4*b+z]*m[4*d+y])-
         m[4*a+y]*(m[4*b+x]*m[4*d+z]-m[4*b+z]*m[4*d+x])+
         m[4*a+z]*(m[4*b+x]*m[4*d+y]-m[4*b+y]*m[4*d+x]))
def rank2(m):return all(det(m,r,c)==0 for r,c in minors)
outputs=0;nonzero=0;anchors=0;passes=0;trials=0;hist=Counter();fails=[];max_support=0;samples=[];certs=[]
for aa,bb in product(subsets,repeat=2):
 outputs+=1;A={v:i for i,v in enumerate(aa)};B={v:i for i,v in enumerate(bb)}
 mats=[];counts=[]
 for q in coords:
  m=[0]*16
  for a,b in q:
   if a in A and b in B:m[4*A[a]+B[b]]=1
  mats.append(m);counts.append(sum(m))
 active=[i for i,k in enumerate(counts) if k];low=[i for i in active if counts[i]<=2];high=[i for i in active if counts[i]>=3]
 assert len(high)<=2
 # Every projected original ket is a partial permutation, so its rank is its support count.
 for q in active:
  m=mats[q]
  assert all(sum(m[4*i+j] for j in range(4))<=1 for i in range(4))
  assert all(sum(m[4*i+j] for i in range(4))<=1 for j in range(4))
 nonzero+=bool(active);hist[(len(active),len(high),sum(counts[i]==4 for i in high))]+=1
 for anchor in high:
  anchors+=1;found=None
  for k in range(0,5):
   if found is not None:break
   for chosen in combinations(low,k):
    if found is not None:break
    for signs in product((1,-1),repeat=k):
     trials+=1;m=mats[anchor][:]
     for j,s in zip(chosen,signs):
      m=[x+s*y for x,y in zip(m,mats[j])]
     if rank2(m):found=(chosen,signs);break
  if found is None:fails.append({'alice':aa,'bob':bb,'anchor':anchor,'low':low})
  else:
   passes+=1;max_support=max(max_support,len(found[0]))
   certs.append({'alice':aa,'bob':bb,'anchor':anchor,'low_terms':list(zip(*found))})
   if len(samples)<8:samples.append({'alice':aa,'bob':bb,'anchor':anchor,'low_terms':list(zip(*found))})
assert not fails and len(certs)==anchors
with open('frontier-20261028-crosshatch-coordinate-certificates-v1.json','x',encoding='utf8') as out:
 json.dump({'source':'CH tensor CH coordinate projections','certificates':certs},out,separators=(',',':'))
print(json.dumps({'coordinate_pairs':outputs,'nonzero_outputs':nonzero,'high_rank_anchors':anchors,
 'exact_anchor_certificates':passes,'bounded_search_failures':fails,'trials':trials,'max_low_terms_used':max_support,
 'histogram':[{'active':k[0],'high':k[1],'rank4':k[2],'count':v} for k,v in sorted(hist.items())],
 'certificate_samples':samples,'limits':'A pass proves the actual source image range is SR2-spanned, not that the state is SN2. Every bounded search failure is inconclusive.'},indent=2))
