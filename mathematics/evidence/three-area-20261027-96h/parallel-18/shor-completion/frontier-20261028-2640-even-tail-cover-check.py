#!/usr/bin/env python3
"""Independent gcd verification of an n2640 clique/pair certificate."""
from itertools import combinations
from math import gcd
from pathlib import Path
import json
n=2640;A={0,3,8,11};Y={0,1,7,13,14}
GA={gcd(a-b,n) for a,b in combinations(A,2)};GY={gcd(a-b,n) for a,b in combinations(Y,2)}
P={x for x in range(n) if all(x==a or gcd(x-a,n) not in GY for a in A)}
Q={x for x in range(n) if all(x==y or gcd(x-y,n) not in GA for y in Y)}
data=json.loads(Path(__file__).with_name('frontier-20261028-2640-even-tail-cover-v1.json').read_text())
assert data['n']==n and GA=={3,5,8,11} and GY=={1,2,6,12}
assert (len(P),len(Q))==(224,658)
seen=set();groups=data['Q_conflict_cliques']
for group in groups:
 assert group and len(set(group))==len(group) and not seen&set(group) and set(group)<=Q
 assert all(gcd(a-b,n) in GA for a,b in combinations(group,2));seen.update(group)
assert seen==Q and len(groups)==266
V={x for x in P if x%3==1};pairs=data['P_mod3_1_conflict_pairs']
assert len(V)==24 and len(pairs)==8
flat=[x for pair in pairs for x in pair]
assert len(flat)==len(set(flat))==16 and set(flat)<=V
assert all(gcd(a-b,n) in GY for a,b in pairs)
D=[d for d in range(8,len(P)+1) if n%d==0 and (n//d)%2==0]
filtered=[]
for d in D:
 q=n//d;ok=True
 for p in (3,5,11):
  vec=P if d%p==0 else Q;old=A if d%p==0 else Y;k=(d if d%p==0 else q)//p
  if min(sum(x%p==r for x in vec) for r in range(p))<k:ok=False
  if max(sum(x%p==r for x in old) for r in range(p))>k:ok=False
 if d%3==0 and d//3>16:ok=False
 if q>len(groups):ok=False
 if ok:filtered.append(d)
assert filtered==[10,12,15,20,22,24,30,33,40,44,55,88]
print(json.dumps({'P_candidates':len(P),'Q_candidates':len(Q),'Q_clique_bound':len(groups),
 'P_mod3_1_bound':16,'even_Q_remaining_P_sizes':filtered,
 'scope':'conditional n2640 even-tail border screen only'},indent=2))
