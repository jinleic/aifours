#!/usr/bin/env python3
"""Directly span every homogeneous right-normed free-Lie word."""
import hashlib,itertools,json,subprocess
from collections import defaultdict
from fractions import Fraction as Q
from functools import lru_cache
from pathlib import Path
R=Path(__file__).resolve().parent
p=Path('/Users/jinleic/repos/aifours/mathematics/evidence/three-area-20261027-96h/parallel-18/kac-moody/frontier-20261028-level6-free-22-pencil-v1.json')
b=p.read_bytes();assert hashlib.sha256(b).hexdigest()=='b3779b89c8a5e67bb0478ac31dae9c96cd2c32f912f8f8c63baa4e8227c6e5bc'
source=json.loads(b)['source_words']
wt=((0,0),(1,0),(0,1),(1,1),(1,1),(2,1),(1,2),(2,2))
words=[w for w in itertools.product(range(8),repeat=6) if sum(wt[x][0] for x in w)==2 and sum(wt[x][1] for x in w)==2]
@lru_cache(None)
def nested(w):
    if len(w)==1:return {w:Q(1)}
    out=defaultdict(Q)
    for v,c in nested(w[1:]).items():out[(w[0],)+v]+=c;out[v+(w[0],)]-=c
    return {u:c for u,c in out.items() if c}
pivots={};nonzero=0
for w in words:
    v=dict(nested(w));nonzero+=bool(v)
    while v:
        pivot=min(v)
        if pivot not in pivots:
            q=v[pivot];pivots[pivot]={u:c/q for u,c in v.items()};break
        q=v[pivot]
        for u,c in pivots[pivot].items():v[u]=v.get(u,Q(0))-q*c
        v={u:c for u,c in v.items() if c}
assert len(words)==456 and len(pivots)==74 and len(source)==74
print('PASS:',len(words),'homogeneous right-normed words,',nonzero,'nonzero, exact span rank',len(pivots),flush=True)
r={'clock_before_receipt_creation':subprocess.check_output(['/bin/date','+%Y-%m-%dT%H:%M:%S%z %Z'],text=True).strip(),
   'source_pencil_sha256':hashlib.sha256(b).hexdigest(),
   'right_normed_words':len(words),'nonzero_right_normed_words':nonzero,'exact_span_rank':len(pivots),
   'argument':'Jacobi reduces every bracket tree to right-normed trees; the preceding 74 distinct-leading-word Lyndon brackets are independent and in this Lie space.'}
with (R/'independent-226-span-receipt-v1.json').open('x') as f:json.dump(r,f,indent=2);f.write('\n')
