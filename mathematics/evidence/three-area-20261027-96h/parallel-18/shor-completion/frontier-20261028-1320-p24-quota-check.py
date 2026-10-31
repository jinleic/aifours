#!/usr/bin/env python3
"""Exact four-quota contradiction for the order-1320 |P|=24 border branch."""
from itertools import combinations
from math import gcd
import json
n=1320;A={0,3,8,11};Y={0,1,7,13,14}
GA={gcd(a-b,n) for a,b in combinations(A,2)};GY={gcd(a-b,n) for a,b in combinations(Y,2)}
PC=[x for x in range(n) if all(x==a or gcd(x-a,n) not in GY for a in A)]
forced=[x for x in PC if x%8 in (1,2,5,6)]
assert len(forced)==12 and all(sum(x%8==r for x in forced)==3 for r in (1,2,5,6))
H={55,165,220,440,660}
assert H<={gcd(x-y,n) for x,y in combinations(forced,2)}
G=GA|H
cand=[x for x in range(n) if (x%5 in (0,4) or x%11 in (0,3)) and
      all(x==y or gcd(x-y,n) not in G for y in Y)]
assert len(cand)==144
N=len(cand);at={x:i for i,x in enumerate(cand)}
adj=[sum(1<<j for j,y in enumerate(cand) if y!=x and gcd(x-y,n) in G) for x in cand]
groups=[sum(1<<i for i,x in enumerate(cand) if x%5==r) for r in (0,4)]+[
        sum(1<<i for i,x in enumerate(cand) if x%11==r) for r in (0,3)]
membership=[tuple(j for j,g in enumerate(groups) if g>>i&1) for i in range(N)]
avail=(1<<N)-1;needs=[11,11,5,5]
for a in (0,14):
    i=at[a];assert avail>>i&1;avail &= ~(adj[i]|(1<<i))
    for j in membership[i]:needs[j]-=1
stats={'nodes':0,'quota_prunes':0,'memo_hits':0};memo=set()
def visit(av,need):
    stats['nodes']+=1;need=list(need)
    for j,k in enumerate(need):
        if k<0:return False
        if k==0:av &= ~groups[j]
    if any((av&groups[j]).bit_count()<k for j,k in enumerate(need)):
        stats['quota_prunes']+=1;return False
    if not any(need):return True
    key=(av,tuple(need))
    if key in memo:stats['memo_hits']+=1;return False
    j=min((j for j,k in enumerate(need) if k),key=lambda j:((av&groups[j]).bit_count()-need[j],(av&groups[j]).bit_count()))
    bits=av&groups[j];possible=[]
    while bits:
        b=bits&-bits;bits-=b;possible.append(b.bit_length()-1)
    i=max(possible,key=lambda i:((adj[i]&av).bit_count(),len(membership[i])))
    b=1<<i;nextneed=need.copy()
    for j in membership[i]:nextneed[j]-=1
    if visit(av&~(adj[i]|b),tuple(nextneed)):return True
    if visit(av&~b,tuple(need)):return True
    memo.add(key);return False
if visit(avail,tuple(needs)):raise AssertionError('unexpected relaxed witness')
# Deliberately weaker positive control: remove only gcd220.
W=[0,14,60,110,204,230,234,300,324,444,560,564,630,680,704,800,900,924,1034,1040,1044,1284]
relaxed=G-{220}
assert len(W)==len(set(W)) and {0,14}<=set(W)
assert all(x in cand or all(x==y or gcd(x-y,n) not in relaxed for y in Y) for x in W)
assert all(gcd(x-y,n) not in relaxed for x,y in combinations(W,2))
assert [sum(x%mod==r for x in W) for mod,r in ((5,0),(5,4),(11,0),(11,3))]==[11,11,5,5]
assert any(gcd(x-y,n)==220 for x,y in combinations(W,2))
print(json.dumps({'forced_P_atoms':forced,'forced_P_gcd_classes':sorted(H),'Q_core_candidates':N,
                  'search':stats,'result':'UNSAT','relaxed_control':'SAT when gcd220 removed',
                  'scope':'necessary cyclic-border constraints at n1320, not a full code solver'},indent=2))
