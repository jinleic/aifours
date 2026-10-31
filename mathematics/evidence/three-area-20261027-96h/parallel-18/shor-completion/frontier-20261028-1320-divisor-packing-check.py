#!/usr/bin/env python3
"""Verify finite clique certificates for the n=1320 divisor-class screen."""
from itertools import combinations
from math import gcd
from pathlib import Path
import json

n=1320;A={0,3,8,11};Y={0,1,7,13,14}
GA={gcd(a-b,n) for a,b in combinations(A,2)}
GY={gcd(a-b,n) for a,b in combinations(Y,2)}
P={x for x in range(n) if all(x==a or gcd(x-a,n) not in GY for a in A)}
Q={x for x in range(n) if all(x==y or gcd(x-y,n) not in GA for y in Y)}
data=json.loads(Path(__file__).with_name('frontier-20261028-1320-divisor-packing-v1.json').read_text())
if data['n']!=n or GA!={3,5,8,11} or GY!={1,2,6,12}:raise ValueError('wrong statement')
tris=data['P_triangles'];seen=set()
for tri in tris:
    if len(tri)!=3 or len(set(tri))!=3 or not set(tri)<=P or seen&set(tri):raise ValueError('bad triangle')
    if any(gcd(a-b,n) not in GY for a,b in combinations(tri,2)):raise ValueError('bad P conflict')
    seen.update(tri)
pbound=len(P)-2*len(tris)
groups=data['Q_conflict_cliques'];seen=set()
for g in groups:
    if not g or len(set(g))!=len(g) or not set(g)<=Q or seen&set(g):raise ValueError('bad Q group')
    if any(gcd(a-b,n) not in GA for a,b in combinations(g,2)):raise ValueError('bad Q conflict')
    seen.update(g)
if seen!=Q:raise ValueError('Q cover incomplete')
qbound=len(groups)
w=data['P80_divisor_screen_witness']
if len(w)!=80 or len(set(w))!=80 or not A<=set(w) or not set(w)<=P:raise ValueError('bad P control')
if any(gcd(a-b,n) in GY for a,b in combinations(w,2)):raise ValueError('P80 not independent')
if (len(P),len(Q),len(tris),pbound,qbound)!=(112,286,16,80,130):raise ValueError('wrong counts')
choices=[d for d in range(1,n+1) if n%d==0 and d<=pbound and n//d<=qbound]
print(json.dumps({'n':n,'anchor_gcd_P':sorted(GA),'anchor_gcd_Q':sorted(GY),
 'P_candidates':len(P),'Q_candidates':len(Q),'P_bound':pbound,'Q_bound':qbound,
 'P_divisor_choices':choices,'P80_screen_only_control':True,
 'scope':'necessary divisor-class screen, not existence of a tiling or completion'},indent=2))
