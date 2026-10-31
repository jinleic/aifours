#!/usr/bin/env python3
"""Complement-head and set-state replay of n2640 P12 CM-T2 branch."""
from collections import Counter
from itertools import combinations
from math import gcd
import json
n=2640;A=(0,3,8,11);Y=(0,1,7,13,14)
GY={gcd(a-b,n) for a,b in combinations(Y,2)}
P={x for x in range(n) if all(x==a or gcd(x-a,n) not in GY for a in A)}
E={x for x in P if x%3==1 and x%2==0};O={x for x in P if x%3==1 and x%2};assert len(E)==len(O)==12
histories={};headstats={}
for s in (2,3,4):
 hist=Counter();bad=allocfail=0;mod=1<<s;half=mod//2
 for omitO in combinations(sorted(O),10):
  for omitE in combinations(sorted(E),10):
   X=(E-set(omitE))|(O-set(omitO));S=X|set(A)
   if any(gcd(x-y,n) in GY for x,y in combinations(S,2)):bad+=1;continue
   cnt=Counter(((x-1)//3)%mod for x in X)
   if any(cnt[r]!=cnt[r+half] for r in range(half)):allocfail+=1;continue
   hist[tuple(sorted({gcd(x-y,n) for x,y in combinations(S,2)}))]+=1
 histories[s]=hist;headstats[s]={'conflicts':bad,'allocation_failures':allocfail,'valid':sum(hist.values()),'H':len(hist)}
assert [headstats[s]['valid'] for s in (2,3,4)]==[256,144,100] and [len(histories[s]) for s in (2,3,4)]==[6,10,35]

def quota(C,F,spec,anchors):
 C=set(C);adj={x:{y for y in C if x!=y and gcd(x-y,n) in F} for x in C}
 groups=[{x for x in C if x%m==r} for m,r,k in spec];need=[k for m,r,k in spec];active=set(C)
 for x in anchors:
  assert x in active;active.remove(x);active-=adj[x]
  for j,g in enumerate(groups):need[j]-=int(x in g)
 nodes=[0];cache=set()
 def dfs(active,need):
  nodes[0]+=1
  if any(k<0 for k in need):return False
  active=set(active)
  for g,k in zip(groups,need):
   if k==0:active-=g
  if any(len(active&g)<k for g,k in zip(groups,need)):return False
  if all(k==0 for k in need):return True
  key=(frozenset(active),tuple(need))
  if key in cache:return False
  j=min((j for j,k in enumerate(need) if k),key=lambda j:(len(active&groups[j])-need[j],len(active&groups[j])))
  x=max(sorted(active&groups[j]),key=lambda x:(len(adj[x]&active),sum(x in g for g in groups)))
  nn=[k-int(x in g) for k,g in zip(need,groups)]
  if dfs(active-{x}-adj[x],nn) or dfs(active-{x},need):return True
  cache.add(key);return False
 return dfs(active,need),nodes[0]
summary={};cases=0;maxnodes=0
for s,hist in histories.items():
 stats=Counter();special=0
 for H,freq in sorted(hist.items()):
  F=set(H);assert not any(gcd(a-b,n) in F for a,b in combinations(Y,2))
  Q={x for x in range(n) if all(x==y or gcd(x-y,n) not in F for y in Y)}
  if any(sum(x%5==r for x in Q)<44 for r in range(5)) or any(sum(x%11==r for x in Q)<20 for r in range(11)):
   stats['prime_capacity']+=freq;continue
  C={x for x in Q if x%5==0 or x%11==2};sat,nodes=quota(C,F,[(5,0,44),(11,2,20)],(0,13));maxnodes=max(maxnodes,nodes)
  if not sat:stats['two_quota_unsat']+=freq;continue
  if s!=4:raise AssertionError('unexpected lower allocation survival')
  special+=1;stats['requires_2adic']+=freq
  aval=[a for a in range(1,55) if all(sum(x%8==r for x in Q)>=(a if r%2==0 else 55-a) for r in range(8))]
  for a in aval:
   spec=[(8,r,a if r%2==0 else 55-a) for r in range(8)]+[(5,0,44),(11,2,20)]
   sat,nodes=quota(Q,F,spec,tuple(sorted(Y)));maxnodes=max(maxnodes,nodes);cases+=1
   if sat:raise AssertionError(('unexpected 2adic tail witness',H,a))
 summary[s]={'head':headstats[s],'tail':dict(stats),'special_H':special}
assert [summary[s]['tail'].get('two_quota_unsat',0) for s in (2,3,4)]==[256,144,84]
assert summary[4]['tail']['requires_2adic']==16 and summary[4]['special_H']==6 and cases==146
print(json.dumps({'allocations':summary,'s4_2adic_cases':cases,'max_nodes':maxnodes,
                  'scope':'set-state independent n2640 P12 T2 replay'},indent=2))
