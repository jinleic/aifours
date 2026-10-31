#!/usr/bin/env python3
"""Exact finite checks for four remaining 1320 border cardinalities."""
from itertools import combinations
from math import gcd
import json
n=1320;A={0,3,8,11};Y={0,1,7,13,14}
GA={gcd(a-b,n) for a,b in combinations(A,2)};GY={gcd(a-b,n) for a,b in combinations(Y,2)}
PC={x for x in range(n) if all(x==a or gcd(x-a,n) not in GY for a in A)}
QC={x for x in range(n) if all(x==y or gcd(x-y,n) not in GA for y in Y)}
P1={x for x in PC if x%3==1}
expected={88,253,256,415,418,583,748,913,916,1075,1078,1243}
assert P1==expected
edges=[(88,916),(256,748),(253,415),(583,1075)]
assert len({x for e in edges for x in e})==8 and all(gcd(a-b,n) in GY for a,b in edges)
assert len({x for x in PC if x%5==2})==6
others={x for x in P1 if x%5!=3};assert others=={256,415,916,1075}
block={88:916,253:415,418:256,583:1075,748:256,913:415,1078:256,1243:415}
assert set(block)==P1-others and all(y in others and gcd(x-y,n) in GY for x,y in block.items())
assert not [x for x in QC if x%6==4]
qedges={1:[(891,386),(971,276),(561,716),(641,1266)],
        2:[(627,722),(707,282),(47,612),(1287,1052)],
        3:[(363,68),(443,618),(693,1058),(773,948)]}
for r,es in qedges.items():
    non1={x for x in QC if x%5==r and x%3!=1}
    odd={x for x in non1 if x%2}
    assert len(non1)==10 and len(odd)==4
    assert len({x for e in es for x in e})==8
    assert all({x,y}<=non1 and gcd(x-y,n)==5 for x,y in es)
    assert all(sum(x%5==r and x%11==l and x%3==1 for x in QC)<=4 for l in range(11))
print(json.dumps({'P_mod3_1_candidates':len(P1),'P_mod3_1_max_bound':8,
 'P_mod5_2_candidates':6,'P15_special_block':'PASS','Q_mod6_4_candidates':0,
 'Q22_three_mod5_class_checks':'PASS','scope':'finite gcd-screen identities, not complete code'},indent=2))
