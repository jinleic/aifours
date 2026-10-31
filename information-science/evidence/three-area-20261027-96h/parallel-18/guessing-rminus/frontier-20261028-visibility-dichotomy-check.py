#!/usr/bin/env python3
"""Exact dichotomy of all 1,024 visibility sets and binary-plane census."""
from collections import Counter
from hashlib import sha256
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
GOOD=('frontier-20261028-visibility-minimal-dual-check-result.json','59c9c593957b2343cc10920d744186493f4bb576514db20f8519e50dc5129667')
BAD=('frontier-20261028-visibility-bad-polymatroid-check-result.json','67dbfe681f285ac4b63ee0306927a80f51eb0790679a2682b8c4de0cb835adb2')
OUT=ROOT/'frontier-20261028-visibility-dichotomy-check-result.json'
N={1:(2,3,4,5,6,7),2:(1,3,7,9,10),3:(1,2,4,8,9),4:(1,3,5,8,10),5:(1,4,6,9,10),6:(1,5,7,8,9),7:(1,2,6,8,10),8:(3,4,6,7,9,10),9:(2,3,5,6,8),10:(2,4,5,7,8)}
TRI=((1,2,3),(1,4,5),(1,6,7),(2,3,9),(2,7,10),(3,8,9),(4,5,10),(4,8,10),(5,6,9),(6,7,8))
P=((1,2,3,4,5,6,7,8,9,10),(1,5,4,3,2,7,6,8,10,9),(8,9,3,4,10,7,6,1,2,5),(8,10,4,3,9,6,7,1,5,2))

def pin(item):
    raw=(ROOT/item[0]).read_bytes()
    if sha256(raw).hexdigest()!=item[1]:raise ValueError('HASH')
    return json.loads(raw)

def main():
    good=pin(GOOD);bad=pin(BAD)
    if not good['all_checked'] or not bad['all_checked']:raise ValueError('INPUT')
    E={tuple(sorted((u,v))) for u in N for v in N[u]};T={tuple(sorted(t)) for t in TRI}
    for p in P:
        if {tuple(sorted((p[a-1],p[b-1]))) for a,b in E}!=E or {tuple(sorted(p[v-1] for v in t)) for t in TRI}!=T:raise ValueError('AUTOMORPHISM')
    gen={frozenset(p[v-1] for v in c['visibility_required']) for c in good['cases'] for p in P}
    badmax={frozenset(p[v-1] for v in c['W']) for c in bad['cases'] for p in P}
    counts=Counter()
    for W in range(1024):
        Ws=frozenset(v+1 for v in range(10) if W>>v&1);g=any(x<=Ws for x in gen);b=any(Ws<=x for x in badmax)
        if g and b:raise ValueError(('CONFLICT',sorted(Ws)))
        if not g and not b:raise ValueError(('UNCLASSIFIED',sorted(Ws)))
        counts['good' if g else 'bad']+=1
    inc=[sum(1<<t for t,tri in enumerate(TRI) if v in tri) for v in range(1,11)];planes=Counter()
    for a in range(1,1024):
        for b in range(a+1,1024):
            c=a^b
            if b>=c:continue
            J=a|b|c
            if set().union(*(set(TRI[t]) for t in range(10) if J>>t&1))!=set(N):planes['noncover']+=1;continue
            Ws=frozenset(v+1 for v in range(10) if a&inc[v] and b&inc[v] and c&inc[v])
            planes['cover_good' if any(x<=Ws for x in gen) else 'cover_bad']+=1
    if sum(planes.values())!=174251:raise ValueError('PLANE_COUNT')
    out={'good_receipt':GOOD[1],'bad_receipt':BAD[1],'all_checked':True,'good_generators':sorted(sorted(x) for x in gen),
         'maximal_bad_sets':sorted(sorted(x) for x in badmax),'visibility_sets':dict(counts),'direction_planes':dict(planes),
         'limits':'Exact finite set dichotomy and plane census, using exactly checked certificates/polymatroids; scientific review of row validity pending.'}
    with OUT.open('x',encoding='utf-8') as f:json.dump(out,f,indent=2);f.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
