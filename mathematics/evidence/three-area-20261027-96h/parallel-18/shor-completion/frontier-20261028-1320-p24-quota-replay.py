#!/usr/bin/env python3
"""Set-based, independently ordered replay of the 24-head quota contradiction."""
from fractions import Fraction
from itertools import combinations
from math import gcd
import json
n=1320;P0=(0,3,8,11);Q0=(0,1,7,13,14)
pforbid={gcd(a-b,n) for a,b in combinations(Q0,2)}
qforbid={gcd(a-b,n) for a,b in combinations(P0,2)}
heads={x for x in range(n) if all(x==a or gcd(x-a,n) not in pforbid for a in P0)}
forced={x for x in heads if x%8 in {1,2,5,6}}
assert len(forced)==12 and all(len({x for x in forced if x%8==r})==3 for r in (1,2,5,6))
H={55,165,220,440,660};assert H<={gcd(x-y,n) for x,y in combinations(forced,2)}
F=qforbid|H
core={x for x in range(n) if (x%5 in (0,4) or x%11 in (0,3)) and
      all(x==y or gcd(x-y,n) not in F for y in Q0)}
assert len(core)==144
conf={x:{y for y in core if x!=y and gcd(x-y,n) in F} for x in core}
groups=[{x for x in core if x%5==r} for r in (0,4)]+[{x for x in core if x%11==r} for r in (0,3)]
active=set(core);quotas=[11,11,5,5]
for a in (0,14):
    assert a in active;active.remove(a);active-=conf[a]
    for k,g in enumerate(groups):quotas[k]-=int(a in g)
counts={'nodes':0,'prunes':0}
def dfs(active,quotas):
    counts['nodes']+=1
    if any(q<0 for q in quotas):return False
    active=set(active)
    for g,q in zip(groups,quotas):
        if q==0:active-=g
    if any(len(active&g)<q for g,q in zip(groups,quotas)):
        counts['prunes']+=1;return False
    if all(q==0 for q in quotas):return True
    eligible=[i for i,q in enumerate(quotas) if q>0]
    k=min(eligible,key=lambda j:(Fraction(len(active&groups[j]),quotas[j]),-j))
    choice=max(active&groups[k],key=lambda x:(len(conf[x]&active),-x))
    nextq=[q-int(choice in g) for q,g in zip(quotas,groups)]
    if dfs(active-{choice}-conf[choice],nextq):return True
    return dfs(active-{choice},quotas)
if dfs(active,quotas):raise AssertionError('unexpected relaxed SAT witness')
print(json.dumps({'result':'UNSAT','core':len(core),'search':counts,
                  'scope':'same necessary four-quota instance, separate set-based search'},indent=2))
