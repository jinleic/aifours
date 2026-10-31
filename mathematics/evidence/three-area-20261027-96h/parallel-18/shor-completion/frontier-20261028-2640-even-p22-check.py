#!/usr/bin/env python3
"""Exact finite P22 tail quotas, contingent on written CM-T2 structure."""
from collections import Counter
from itertools import combinations,product
from math import gcd
import json
n=2640;A={0,3,8,11};Y={0,1,7,13,14}
GA={gcd(a-b,n) for a,b in combinations(A,2)};GY={gcd(a-b,n) for a,b in combinations(Y,2)}
P={x for x in range(n) if all(x==a or gcd(x-a,n) not in GY for a in A)}
L=sorted(x for x in P if x%11==1);R=sorted(x for x in P if x%11==2)
assert len(L)==len(R)==12 and all(sum(x%2==r for x in C)==6 for C in (L,R) for r in (0,1))
# CM-T2 structure supplies one even and one odd per head mod11 class;
# forced240 is an independently checked prerequisite, not derived here.
hist=Counter();bad=total=0
for a in combinations(L,2):
 if (a[0]-a[1])%2==0:continue
 for b in combinations(R,2):
  if (b[0]-b[1])%2==0:continue
  total+=1;S=set(a+b)|A
  if any(gcd(x-y,n) in GY for x,y in combinations(S,2)):bad+=1;continue
  hist[tuple(sorted({gcd(x-y,n) for x,y in combinations(S,2)}|{240}))]+=1
assert (total,bad,sum(hist.values()),len(hist))==(1296,272,1024,37)
# Base Q screen has no even residue 1 modulo3; Q class1 mod3 has40 entries.
Q0={x for x in range(n) if all(x==y or gcd(x-y,n) not in GA for y in Y)}
assert not any(x%6==4 for x in Q0)

def quota(C,F,a):
 b=15-a;N=len(C);idx={x:i for i,x in enumerate(C)}
 adj=[sum(1<<j for j,y in enumerate(C) if x!=y and gcd(x-y,n) in F) for x in C]
 specs=[(16,r,a if r%2==0 else b) for r in range(16)]+[(3,1,40),(5,1,24)]
 groups=[sum(1<<i for i,x in enumerate(C) if x%m==r) for m,r,k in specs]
 mem=[tuple(j for j,g in enumerate(groups) if g>>i&1) for i in range(N)];av=(1<<N)-1;need=[k for m,r,k in specs]
 for x in sorted(Y):
  i=idx[x];assert av>>i&1;av &= ~(adj[i]|1<<i)
  for j in mem[i]:need[j]-=1
 stats={'nodes':0,'prunes':0};cache=set()
 def dfs(av,need):
  stats['nodes']+=1;need=list(need)
  for j,k in enumerate(need):
   if k<0:return False
   if k==0:av &= ~groups[j]
  if any((av&groups[j]).bit_count()<k for j,k in enumerate(need)):stats['prunes']+=1;return False
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
 if dfs(av,tuple(need)):raise AssertionError('unexpected quota SAT')
 return stats
stats=Counter();cases=[];survH=0
for H,freq in sorted(hist.items()):
 F=set(H);assert not any(gcd(a-b,n) in F for a,b in combinations(Y,2))
 Q=[x for x in range(n) if all(x==y or gcd(x-y,n) not in F for y in Y)]
 if any(sum(x%3==j for x in Q)<40 for j in range(3)) or any(sum(x%5==j for x in Q)<24 for j in range(5)):
  stats['prime_capacity']+=freq;continue
 valid=[a for a in range(1,11) if all(sum(x%16==r for x in Q)>=(a if r%2==0 else 15-a) for r in range(16))]
 if not valid:stats['twoadic_capacity']+=freq;continue
 survH+=1;stats['quota_unsat']+=freq
 for a in valid:cases.append(quota(Q,F,a)['nodes'])
assert (stats['prime_capacity'],stats['twoadic_capacity'],stats['quota_unsat'],survH,len(cases))==(64,452,508,24,139)
# Explicit SAT balance-only control, deliberately removing ALL gcd constraints:
# even fibres take residues 0,3,6,9,12 mod165; odd fibres take ten residues
# 1/2 mod3. Swap mod5=4 representatives in fibres14 and3 to include old14.
inv=pow(16,-1,165);W=[]
for r in range(16):
 S=[0,3,6,9,12] if r%2==0 else [1,2,4,5,7,8,10,11,13,14]
 if r==14:S=[14 if y==9 else y for y in S]
 if r==3:S=[9 if y==14 else y for y in S]
 W.extend(r+16*(((y-r)*inv)%165) for y in S)
assert len(W)==len(set(W))==120 and Y<=set(W)
assert all(sum(x%16==r for x in W)==(5 if r%2==0 else 10) for r in range(16))
assert all(sum(x%3==r for x in W)==40 for r in range(3)) and all(sum(x%5==r for x in W)==24 for r in range(5))
assert any(gcd(a-b,n) in GA for a,b in combinations(W,2))
print(json.dumps({'head_choices':total,'head_conflicts':bad,'distinct_H':len(hist),'stats':dict(stats),
 'surviving_H':survH,'a_cases':len(cases),'max_nodes':max(cases),
 'control':'SAT for balances/anchors after removing ALL gcd constraints',
 'scope':'n2640 P22 even-Q; assumes named CM-T2 and forced240'},indent=2))
