#!/usr/bin/env python3
"""Complement-enumeration and set-based independent 1980 P36 replay."""
from fractions import Fraction
from itertools import combinations
from math import gcd
import json
n=1980;oldp=(0,3,8,11);oldq=(0,1,7,13,14)
pbad={gcd(a-b,n) for a,b in combinations(oldq,2)}
qbad={gcd(a-b,n) for a,b in combinations(oldp,2)}
heads={x for x in range(n) if all(x==a or gcd(x-a,n) not in pbad for a in oldp)}
V={x for x in heads if x%3==1};assert len(V)==18
survivors=[]
for omitted in combinations(sorted(V),6):
    S=V-set(omitted)
    if all(gcd(a-b,n) not in pbad for a,b in combinations(S,2)):survivors.append(S)
assert len(survivors)==1
H={165,330,495,660,990};assert H<={gcd(a-b,n) for a,b in combinations(survivors[0],2)}
F=qbad|H
C={x for x in range(n) if (x%5 in (0,4) or x%11 in (0,3)) and all(x==y or gcd(x-y,n) not in F for y in oldq)}
assert len(C)==170
adj={x:{y for y in C if x!=y and gcd(x-y,n) in F} for x in C}
groups=[{x for x in C if x%5==r} for r in (0,4)]+[{x for x in C if x%11==r} for r in (0,3)]
active=set(C);need=[11,11,5,5]
for x in (0,14):
    assert x in active;active.remove(x);active-=adj[x]
    for i,g in enumerate(groups):need[i]-=int(x in g)
stats={'nodes':0,'prunes':0}
def search(active,need):
    stats['nodes']+=1
    if any(v<0 for v in need):return False
    active=set(active)
    for g,k in zip(groups,need):
        if k==0:active-=g
    if any(len(active&g)<k for g,k in zip(groups,need)):
        stats['prunes']+=1;return False
    if all(k==0 for k in need):return True
    i=min((i for i,k in enumerate(need) if k),key=lambda i:(Fraction(len(active&groups[i]),need[i]),-i))
    x=max(active&groups[i],key=lambda x:(len(adj[x]&active),-x))
    after=[k-int(x in g) for k,g in zip(need,groups)]
    return search(active-{x}-adj[x],after) or search(active-{x},need)
if search(active,need):raise AssertionError('unexpected quota witness')
print(json.dumps({'unique_12_head_set':len(survivors),'core':len(C),'search':stats,
                  'result':'UNSAT','scope':'independent 1980 P36 branch'},indent=2))
