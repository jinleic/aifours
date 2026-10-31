#!/usr/bin/env python3
"""Exact P12 partial-head and 2-adic tail checks, contingent on CM-T2."""
from collections import Counter
from itertools import combinations
from math import gcd
import json
n=2640;A={0,3,8,11};Y={0,1,7,13,14}
GA={gcd(a-b,n) for a,b in combinations(A,2)};GY={gcd(a-b,n) for a,b in combinations(Y,2)}
P={x for x in range(n) if all(x==a or gcd(x-a,n) not in GY for a in A)}
E=sorted(x for x in P if x%3==1 and x%2==0);O=sorted(x for x in P if x%3==1 and x%2);assert len(E)==len(O)==12
histories={};headstats={}
for s in (2,3,4):
 hist=Counter();bad=allocfail=0;mod=1<<s;half=mod//2
 for a in combinations(E,2):
  for b in combinations(O,2):
   X=a+b;S=set(X)|A
   if any(gcd(x-y,n) in GY for x,y in combinations(S,2)):bad+=1;continue
   counts=[sum(((x-1)//3)%mod==r for x in X) for r in range(mod)]
   if any(counts[r]!=counts[r+half] for r in range(half)):allocfail+=1;continue
   hist[tuple(sorted({gcd(x-y,n) for x,y in combinations(S,2)}))]+=1
 histories[s]=hist;headstats[s]={'conflicts':bad,'allocation_failures':allocfail,'valid':sum(hist.values()),'H':len(hist)}
assert [headstats[s]['valid'] for s in (2,3,4)]==[256,144,100]
assert [len(histories[s]) for s in (2,3,4)]==[6,10,35]

def quota(C,F,spec,anchors):
 N=len(C);idx={x:i for i,x in enumerate(C)}
 adj=[sum(1<<j for j,y in enumerate(C) if x!=y and gcd(x-y,n) in F) for x in C]
 groups=[sum(1<<i for i,x in enumerate(C) if x%m==r) for m,r,k in spec]
 mem=[tuple(j for j,g in enumerate(groups) if g>>i&1) for i in range(N)]
 av=(1<<N)-1;need=[k for m,r,k in spec]
 for a in anchors:
  i=idx[a];assert av>>i&1;av &= ~(adj[i]|1<<i)
  for j in mem[i]:need[j]-=1
 nodes=[0];cache=set()
 def dfs(av,need):
  nodes[0]+=1;need=list(need)
  for j,k in enumerate(need):
   if k<0:return False
   if k==0:av &= ~groups[j]
  if any((av&groups[j]).bit_count()<k for j,k in enumerate(need)):return False
  if not any(need):return True
  key=(av,tuple(need))
  if key in cache:return False
  j=min((j for j,k in enumerate(need) if k),key=lambda j:((av&groups[j]).bit_count()-need[j],(av&groups[j]).bit_count()))
  bits=av&groups[j];pool=[]
  while bits:
   low=bits&-bits;bits-=low;pool.append(low.bit_length()-1)
  i=max(pool,key=lambda i:((adj[i]&av).bit_count(),len(mem[i])));bit=1<<i;nn=need.copy()
  for j in mem[i]:nn[j]-=1
  if dfs(av&~(adj[i]|bit),tuple(nn)) or dfs(av&~bit,tuple(need)):return True
  cache.add(key);return False
 return dfs(av,tuple(need)),nodes[0]

summary={};cases=0;maxnodes=0
for s,hist in histories.items():
 stats=Counter();special=0
 for H,freq in sorted(hist.items()):
  F=set(H);assert not any(gcd(a-b,n) in F for a,b in combinations(Y,2))
  Q=[x for x in range(n) if all(x==y or gcd(x-y,n) not in F for y in Y)]
  if any(sum(x%5==r for x in Q)<44 for r in range(5)) or any(sum(x%11==r for x in Q)<20 for r in range(11)):
   stats['prime_capacity']+=freq;continue
  C=[x for x in Q if x%5==0 or x%11==2]
  sat,nodes=quota(C,F,[(5,0,44),(11,2,20)],(0,13));maxnodes=max(maxnodes,nodes)
  if not sat:stats['two_quota_unsat']+=freq;continue
  if s!=4:raise AssertionError('unexpected surviving lower allocation')
  special+=1;stats['requires_2adic']+=freq
  aval=[a for a in range(1,55) if all(sum(x%8==r for x in Q)>=(a if r%2==0 else 55-a) for r in range(8))]
  for a in aval:
   spec=[(8,r,a if r%2==0 else 55-a) for r in range(8)]+[(5,0,44),(11,2,20)]
   sat,nodes=quota(Q,F,spec,tuple(sorted(Y)));maxnodes=max(maxnodes,nodes);cases+=1
   if sat:raise AssertionError(('unexpected 2-adic Q witness',H,a))
 summary[s]={'head':headstats[s],'tail':dict(stats),'special_H':special}
assert [summary[s]['tail'].get('two_quota_unsat',0) for s in (2,3,4)]==[256,144,84]
assert summary[4]['tail']['requires_2adic']==16 and summary[4]['special_H']==6 and cases==146
# Nonvacuity: a literal Q-only 2-quota witness for one s=4 partial H. It is
# deliberately not claimed to satisfy the additional 2-adic tail requirements.
H={3,4,5,8,11,16,20,24,44,80,88,165}
W=[0,13,50,60,110,120,170,180,211,240,277,290,300,343,350,360,410,541,600,607,660,673,720,770,780,830,840,871,890,900,960,1003,1010,1020,1070,1130,1201,1260,1267,1320,1333,1370,1380,1440,1490,1500,1531,1550,1560,1597,1610,1620,1680,1730,1790,1861,1920,1927,1980,2030,2257,2323,2521,2587]
assert len(W)==len(set(W))==64 and {0,13}<=set(W)
assert all(all(x==y or gcd(x-y,n) not in H for y in Y) for x in W)
assert all(gcd(a-b,n) not in H for a,b in combinations(W,2))
assert sum(x%5==0 for x in W)==44 and sum(x%11==2 for x in W)==20
print(json.dumps({'allocations':summary,'s4_2adic_cases':cases,'max_nodes':maxnodes,
 'control':'SAT for genuine s4 H two-quota relaxation','scope':'n2640 P12 even-Q assuming CM-T2'},indent=2))
