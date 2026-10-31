#!/usr/bin/env python3
"""Set-based independent replay of the relaxed 264-class slot obstruction."""
from collections import defaultdict
from itertools import combinations,product
from math import gcd
import json
N=1320;heads=(0,3,8,11);tails=(0,1,7,13,14)
forbidden_head={gcd(x-y,N) for x,y in combinations(heads,2)}
tail_candidates=[q for q in range(N) if all(q==y or gcd(q-y,N) not in forbidden_head for y in tails)]
bad=forbidden_head|{264}
def conflict(a,b):return a!=b and gcd(a-b,N) in bad
extras={j:[q for q in tail_candidates if q%11==j and q%3!=1] for j in (1,2,7)}
assert [len(extras[j]) for j in (1,2,7)]==[10,10,10]
pool=set(sum((extras[j] for j in (1,2,7)),[]))
slots=defaultdict(list)
for q in tail_candidates:
    if q%3==1:slots[(q%11,q%8)].append(q)
assert len(slots)==44 and all(q%2 for key in slots for q in slots[key])
blocked={q:{a for a in pool if conflict(q,a)} for group in slots.values() for q in group}
seed_count=admitted=small_slots=quota_failure=unsettled=0
for triple in product(*(list(combinations(extras[j],2)) for j in (1,2,7))):
    seed=set(sum((list(pair) for pair in triple),[]));seed_count+=1
    if any(conflict(a,b) for a,b in combinations(seed,2)) or any(conflict(a,t) for a in seed for t in tails):continue
    admitted+=1;open_by_11=defaultdict(int)
    for (j,mod8),group in slots.items():
        if any(not(seed&blocked[q]) for q in group):open_by_11[j]+=1
    if sum(open_by_11.values())<22:small_slots+=1;continue
    for j in (1,2,7):
        required=max(0,6-2-open_by_11[j])
        remaining=[q for q in extras[j] if q not in seed and not any(conflict(q,s) for s in seed)
                   and not any(conflict(q,t) for t in tails)]
        if len(remaining)<required:quota_failure+=1;break
    else:unsettled+=1
assert (seed_count,admitted,small_slots,quota_failure,unsettled)==(91125,1143,1089,54,0)
print(json.dumps({'seeds':seed_count,'compatible':admitted,'slot_rejections':small_slots,
                  'quota_rejections':quota_failure,'residual':unsettled},indent=2))
