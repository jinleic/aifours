#!/usr/bin/env python3
"""Exact finite relaxed slot certificate for |P|=20 at order 1320."""
from collections import Counter
from itertools import combinations,product
from math import gcd
import json
n=1320;A={0,3,8,11};Y={0,1,7,13,14}
GA={gcd(a-b,n) for a,b in combinations(A,2)};GY={gcd(a-b,n) for a,b in combinations(Y,2)}
PC={x for x in range(n) if all(x==a or gcd(x-a,n) not in GY for a in A)}
QC={x for x in range(n) if all(x==y or gcd(x-y,n) not in GA for y in Y)}
# P must use gcd class264: uniform mod5 forces 4 of each of two size-6 sets.
c2=sorted(x for x in PC if x%5==2);c4=sorted(x for x in PC if x%5==4)
assert c2==[132,407,792,872,987,1067] and c4==[264,344,459,539,924,1199]
match=[(132,924),(407,1199),(792,264),(872,344),(987,459),(1067,539)]
assert {x for x,y in match}==set(c2) and {y for x,y in match}==set(c4)
assert all(gcd(x-y,n)==264 for x,y in match)
# Under no264, any Q member 1 mod3 is odd and each (mod11,mod8) slot has capacity1.
assert not any(x%6==4 for x in QC)
js=(1,2,7);N={j:sorted(x for x in QC if x%11==j and x%3!=1) for j in js}
assert all(len(N[j])==10 for j in js)
non=sorted({x for a in N.values() for x in a});idx={x:i for i,x in enumerate(non)}
G=GA|{264};anchorbad=sum(1<<idx[x] for x in non if any(x!=y and gcd(x-y,n) in G for y in Y))
adj=[sum(1<<idx[y] for y in non if y!=x and gcd(x-y,n) in G) for x in non]
bad=[(1<<idx[a])|(1<<idx[b]) for a,b in combinations(non,2) if gcd(a-b,n) in G]
slots={}
for x in QC:
    if x%3==1:slots.setdefault((x%11,x%8),[]).append(x)
assert len(slots)==44 and all(key[1] in (1,3,5,7) for key in slots)
slot_masks=[(key,[sum(1<<idx[y] for y in non if gcd(x-y,n) in G) for x in xs])
            for key,xs in sorted(slots.items())]
pairs={j:[(1<<idx[a])|(1<<idx[b]) for a,b in combinations(N[j],2)] for j in js}
total=compatible=bound_reject=quota_reject=residual=0
for aa,bb,cc in product(*(pairs[j] for j in js)):
    total+=1;mask=aa|bb|cc
    if mask&anchorbad or any(mask&b==b for b in bad):continue
    compatible+=1;opened=Counter()
    for key,alts in slot_masks:
        if any(not mask&z for z in alts):opened[key[0]]+=1
    if sum(opened.values())<22:
        bound_reject+=1;continue
    impossible=False
    for j in js:
        chosen=[idx[x] for x in N[j] if mask>>idx[x]&1]
        need=max(0,6-len(chosen)-opened[j])
        available=[idx[x] for x in N[j] if not(mask>>idx[x]&1) and
                   not(anchorbad>>idx[x]&1) and not(adj[idx[x]]&mask)]
        if len(available)<need:impossible=True;break
    if impossible:quota_reject+=1
    else:residual+=1
assert (total,compatible,bound_reject,quota_reject,residual)==(91125,1143,1089,54,0)
print(json.dumps({'P_matching_pairs':len(match),'Q1_slots':len(slots),'seed_sets':total,
 'compatible_seeds':compatible,'slot_rejections':bound_reject,'quota_rejections':quota_reject,
 'residual':residual,'scope':'necessary 1320 gcd/prime balance; no full code assertion'},indent=2))
