#!/usr/bin/env python3
"""Independent set-based, differently ordered 1980 forced-class replay."""
from fractions import Fraction
from itertools import combinations
from math import gcd
import json
n=1980;A=(0,3,8,11);Y=(0,1,7,13,14)
GA={gcd(a-b,n) for a,b in combinations(A,2)};GY={gcd(a-b,n) for a,b in combinations(Y,2)}

def solve(old,bans,spec,anchors):
    C={x for x in range(n) if any(x%m==r for m,r,k in spec) and
       all(x==a or gcd(x-a,n) not in bans for a in old)}
    adj={x:{y for y in C if x!=y and gcd(x-y,n) in bans} for x in C}
    groups=[{x for x in C if x%m==r} for m,r,k in spec];need=[k for m,r,k in spec]
    active=set(C)
    for x in anchors:
        assert x in active;active.remove(x);active-=adj[x]
        for j,g in enumerate(groups):need[j]-=int(x in g)
    stats={'nodes':0,'prunes':0}
    def dfs(active,need):
        stats['nodes']+=1
        if any(k<0 for k in need):return False
        active=set(active)
        for g,k in zip(groups,need):
            if k==0:active-=g
        if any(len(active&g)<k for g,k in zip(groups,need)):
            stats['prunes']+=1;return False
        if all(k==0 for k in need):return True
        j=min((j for j,k in enumerate(need) if k),key=lambda j:(Fraction(len(active&groups[j]),need[j]),-j))
        x=max(active&groups[j],key=lambda x:(len(adj[x]&active),-x))
        n2=[k-int(x in g) for k,g in zip(need,groups)]
        return dfs(active-{x}-adj[x],n2) or dfs(active-{x},need)
    if dfs(active,need):raise AssertionError('unexpected relaxed SAT')
    return {'candidates':len(C),'search':stats,'result':'UNSAT'}
p=solve(A,GY|{396},[(5,r,3) for r in (0,1,2,4)],(0,11))
q=solve(Y,GA|{396},[(4,1,33),(4,2,33),(4,3,33),(11,1,12),(11,2,12),(11,7,12)],(1,7,13,14))
assert p['candidates']==56 and q['candidates']==298
print(json.dumps({'head':p,'tail':q,'scope':'independent 1980 P15 branch replay'},indent=2))
