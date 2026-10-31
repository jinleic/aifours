#!/usr/bin/env python3
"""Independent direct verification of all exceptional q8 syndrome triples."""
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
SOURCE=('frontier-20261028-syndrome-triple-cliques-result.json','a567094dd9a4f7fb9484c8a11a8c7bb2dc0476cb5e7f56499d3c1a6bb15b2004')
OUT=ROOT/'frontier-20261028-syndrome-triple-independent-result.json'
N={1:(2,3,4,5,6,7),2:(1,3,7,9,10),3:(1,2,4,8,9),4:(1,3,5,8,10),
   5:(1,4,6,9,10),6:(1,5,7,8,9),7:(1,2,6,8,10),8:(3,4,6,7,9,10),
   9:(2,3,5,6,8),10:(2,4,5,7,8)}
TRI=((1,2,3),(1,4,5),(1,6,7),(2,3,9),(2,7,10),(3,8,9),(4,5,10),(4,8,10),(5,6,9),(6,7,8))


def verify(source):
    if source['triangles']!=[list(x) for x in TRI]:raise ValueError('TRIANGLES')
    inc={v:[i for i,T in enumerate(TRI) if v in T] for v in N}
    if any(len(x)!=3 for x in inc.values()) or any(set(T)<=set(N[v]) for v in N for T in TRI):raise ValueError('LOCAL_COMPLETION')
    def syndrome(word):
        ans=0
        for t,T in enumerate(TRI):
            parity=0
            for v in T:parity^=(word>>(3*(v-1)+inc[v].index(t)))&1
            ans|=parity<<t
        return ans
    def conflict(word):
        if not 0<=word<2**30:return False
        return any((word>>(3*(v-1)))&7 and all(not ((word>>(3*(u-1)))&7) for u in N[v]) for v in N)
    masks=[sum(1<<t for t in inc[v]) for v in N]
    if masks!=source['local_incident_syndrome_masks']:raise ValueError('LOCAL_MASKS')
    records=source['exceptional_witnesses'];table={}
    for r in records:
        s,t,u,v=r['s'],r['t'],r['u'],r['v'];key=(s,t)
        if key in table or not 1<=s<t<1024:raise ValueError('DUPLICATE_OR_RANGE')
        if syndrome(u)!=s or syndrome(v)!=t:raise ValueError('SYNDROME')
        if not(conflict(u) and conflict(v) and conflict(u^v)):raise ValueError('CONFLICT')
        table[key]=(u,v)
    local=0;exceptions=0
    for s,t in combinations(range(1,1024),2):
        simple=any((s&A) and (t&A) and (s&A)!=(t&A) for A in masks)
        if simple:
            local+=1
            if (s,t) in table:raise ValueError('UNNEEDED_RECORD')
        else:
            exceptions+=1
            if (s,t) not in table:raise ValueError('MISSING_RECORD')
    if (local,exceptions)!=(522231,522) or len(table)!=522:raise ValueError('COUNTS')
    return {'nonzero_syndrome_pairs':local+exceptions,'local_constructible_pairs':local,
            'exceptional_direct_conflict_triangles':exceptions,'factor_neighborhood_checks':100}


def main():
    raw=(ROOT/SOURCE[0]).read_bytes()
    if sha256(raw).hexdigest()!=SOURCE[1]:raise ValueError('HASH')
    src=json.loads(raw);checks=verify(src);controls={}
    for name,mut,reason in (
        ('removed_exception',lambda x:x['exceptional_witnesses'].pop(),'MISSING_RECORD'),
        ('changed_word_syndrome',lambda x:x['exceptional_witnesses'][0].__setitem__('u',0),'SYNDROME'),
        ('invalid_local_mask',lambda x:x['local_incident_syndrome_masks'].__setitem__(0,0),'LOCAL_MASKS')):
        bad=json.loads(json.dumps(src));mut(bad)
        try:verify(bad)
        except ValueError as exc:
            if str(exc)!=reason:raise ValueError(('WRONG_REASON',name,str(exc)))
            controls[name]=reason
        else:raise ValueError(('MUTATION_ACCEPTED',name))
    out={'source_receipt_sha256':SOURCE[1],'exact_checks':checks,'all_checked':True,'mutation_controls':controls,
         'limits':'Exact exhaustive syndrome classification and direct exceptional conflict triangles; local representative and clique-factor proof is written separately.'}
    with OUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
