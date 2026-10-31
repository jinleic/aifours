#!/usr/bin/env python3
"""Exact matching and clique certificates for the n1980 P66 branch."""
from itertools import combinations
from math import gcd
import json
n=1980;A={0,3,8,11};Y={0,1,7,13,14}
GA={gcd(a-b,n) for a,b in combinations(A,2)};GY={gcd(a-b,n) for a,b in combinations(Y,2)}
P={x for x in range(n) if all(x==a or gcd(x-a,n) not in GY for a in A)}
P1={x for x in P if x%11==1};P2={x for x in P if x%11==2}
assert P1=={155,188,243,848,903,936,1508,1563}
assert P2=={68,123,695,728,783,1388,1443,1476}
tri=[{188,848,1508},{243,903,1563}]
assert all(gcd(a-b,n)==660 for t in tri for a,b in combinations(t,2))
m180=[(155,695),(188,728),(243,783),(848,1388),(903,1443),(936,1476),(1508,68),(1563,123)]
m60=[(188,68),(848,728),(1508,1388),(243,123),(903,783),(1563,1443)]
for matching,g in ((m180,180),(m60,60)):
 assert len({v for pair in matching for v in pair})==2*len(matching)
 assert all(a in P1 and b in P2 and gcd(a-b,n)==g for a,b in matching)
F=GA|{60,180,660}
C={x for x in range(n) if x%5==0 and all(x==y or gcd(x-y,n) not in F for y in Y)}
cliques=[
 [315,975,1635,20,80,140,380,500,560,620,680,740,800,1040,1160,1220,1280,1340,1400,1460,1700,1820,1880,1940,440,1100,1760],
 [55,715,1375,50,170,230,290,350,410,470,710,830,890,950,1010,1070,1130,1370,1490,1550,1610,1670,1730,1790],
 [385,1045,1705,630,1290,1950],[110,770,1430],[0]]
flat=[x for g in cliques for x in g]
assert len(C)==61 and len(flat)==len(set(flat))==61 and set(flat)==C
assert all(gcd(a-b,n) in F for g in cliques for a,b in combinations(g,2))
print(json.dumps({'P_class1_candidates':len(P1),'P_class2_candidates':len(P2),
 'P_forced_gcds':[60,180,660],'Q_mod5_0_candidates':len(C),'Q_clique_sizes':[len(g) for g in cliques],
 'scope':'necessary border obstruction n1980 P-size66'},indent=2))
