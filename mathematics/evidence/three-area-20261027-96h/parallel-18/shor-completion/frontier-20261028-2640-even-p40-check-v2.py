#!/usr/bin/env python3
"""Corrected explicit head matchings plus exact Q quotas for n2640 P40.

v1 failed a too-strong equality that forgot the old-anchor 660 screen. The
actual screened class1 has SIX candidates, which makes the required quota8
impossible even more directly. The failed v1 source is preserved.
"""
from itertools import combinations,product
from math import gcd
import json
n=2640;A={0,3,8,11};Y={0,1,7,13,14}
GA={gcd(a-b,n) for a,b in combinations(A,2)};GY={gcd(a-b,n) for a,b in combinations(Y,2)}
def head(r,F):return {x for x in range(n) if x%5==r and all(x==a or gcd(x-a,n) not in F for a in A)}
for g,pair in ((4,(872,459)),(16,(872,1779))):
 F=GY|{g};L=head(2,F);R=head(4,F)
 assert len(L)==len(R)==8 and pair[0] in L and pair[1] in R and gcd(pair[0]-pair[1],n) in GY
# no1320: six half-turn pairs cover all12 class4 candidates.
F=GY|{1320};R=head(4,F)
pairs=[(264,1584),(344,1664),(459,1779),(539,1859),(924,2244),(1199,2519)]
assert len(R)==12 and {x for p in pairs for x in p}==R and all(gcd(a-b,n)==1320 for a,b in pairs)
# no660: two four-cycles + four singles. Quota8 forces both singles and an
# opposite pair from each cycle. Each case leaves just6 class1 candidates.
F=GY|{660};R=head(4,F)
cycles=[(264,924,1584,2244),(539,1199,1859,2519)];singles={344,1664,459,1779}
assert set(sum((list(c) for c in cycles),[]))|singles==R and len(R)==12
for c in cycles:assert all(gcd(c[i]-c[(i+1)%4],n)==660 for i in range(4))
choices=[((264,1584),(924,2244)),((539,1859),(1199,2519))]
for x,y in product(*choices):
 S=singles|set(x)|set(y)
 C={v for v in head(1,F) if all(gcd(v-z,n) not in F for z in S)}
 assert C=={11,396,1056,1331,1716,2376}
# Q must avoid all four forced P classes and satisfy mod3/11 quotas.
F=GA|{4,16,660,1320};C=[x for x in range(n) if all(x==y or gcd(x-y,n) not in F for y in Y)]
assert len(C)==457
N=len(C);idx={x:i for i,x in enumerate(C)}
adj=[sum(1<<j for j,y in enumerate(C) if x!=y and gcd(x-y,n) in F) for x in C]
groups=[sum(1<<i for i,x in enumerate(C) if x%3==r) for r in range(3)]+[sum(1<<i for i,x in enumerate(C) if x%11==r) for r in range(11)]
mem=[tuple(j for j,g in enumerate(groups) if g>>i&1) for i in range(N)];av=(1<<N)-1;need=[22]*3+[6]*11
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
 i=max(pool,key=lambda i:((adj[i]&av).bit_count(),len(mem[i])));b=1<<i;nn=need.copy()
 for j in mem[i]:nn[j]-=1
 if dfs(av&~(adj[i]|b),tuple(nn)) or dfs(av&~b,tuple(need)):return True
 cache.add(key);return False
if dfs(av,tuple(need)):raise AssertionError('unexpected Q quota solution')
W=[0,1,7,13,14,50,62,140,181,204,230,240,330,331,337,343,398,470,494,511,660,661,667,734,841,900,950,960,974,990,1003,1194,1214,1280,1290,1320,1327,1333,1604,1650,1651,1790,1831,1880,1934,1950,1981,1993,2000,2100,2120,2160,2161,2220,2270,2280,2311,2317,2340,2360,2430,2490,2491,2514,2540,2610]
assert len(W)==len(set(W))==66 and Y<=set(W)
assert all(gcd(a-b,n) not in GA for a,b in combinations(W,2))
assert all(sum(x%3==r for x in W)==22 for r in range(3)) and all(sum(x%11==r for x in W)==6 for r in range(11))
print(json.dumps({'P_forced_gcds':[4,16,660,1320],'Q_candidates':N,'search':stats,
 'result':'UNSAT','control':'SAT when extra forced classes omitted','scope':'n2640 P40 even-Q'},indent=2))
