#!/usr/bin/env python3
"""Independent direct FD/color replay for all four-cover one-outsider supports."""
from hashlib import sha256
from itertools import combinations,product
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
SOURCE=('frontier-20261028-mincover-outsider-color-census-result.json','7c25535f2c52ffdc667f3c7b231c201fef4b1279e1da826299283230dbbb44c2')
COVERS=('frontier-20261028-syndrome-cover-check-result.json','e1bf3ece1f9204a8f0f779bf98a236d689946df2bef5d2a50408b30bc9f3418d')
OUT=ROOT/'frontier-20261028-mincover-outsider-color-independent-result.json'
N={1:(2,3,4,5,6,7),2:(1,3,7,9,10),3:(1,2,4,8,9),4:(1,3,5,8,10),
   5:(1,4,6,9,10),6:(1,5,7,8,9),7:(1,2,6,8,10),8:(3,4,6,7,9,10),
   9:(2,3,5,6,8),10:(2,4,5,7,8)}
TRI=((1,2,3),(1,4,5),(1,6,7),(2,3,9),(2,7,10),(3,8,9),(4,5,10),(4,8,10),(5,6,9),(6,7,8))


def pin(item):
    raw=(ROOT/item[0]).read_bytes()
    if sha256(raw).hexdigest()!=item[1]:raise ValueError(('HASH',item[0]))
    return json.loads(raw)


def geometry(cover):
    Ts=[TRI[t-1] for t in cover];positions={};cursor=0
    for v in range(1,11):
        positions[v]=[cursor+j for j in range(sum(v in T for T in Ts))];cursor+=len(positions[v])
    if cursor!=12 or any(not positions[v] for v in positions):raise ValueError('GEOMETRY')
    seed=set()
    for choices in product(range(4),repeat=4):
        word=0
        for t,T in enumerate(Ts):
            a=choices[t]&1;b=(choices[t]>>1)&1
            for v,x in zip(T,(a,b,a^b)):
                slot=positions[v][[j for j,U in enumerate(Ts) if v in U].index(t)]
                word|=x<<slot
        seed.add(word)
    if len(seed)!=256:raise ValueError('SEED')
    vmask=[];bad=[]
    for d in range(4096):
        m=sum(1<<(v-1) for v in positions if any(d>>j&1 for j in positions[v]));vmask.append(m)
        bad.append(any(not (m&sum(1<<(u-1) for u in N[v])) for v in N if m>>(v-1)&1))
    return Ts,positions,seed,vmask,bad


def verify(record,geo,add_conflicting=False,override_colors=None):
    Ts,pos,seed,vmask,bad=geo;sy=record['syndrome'];outside=record['outside_word']
    if not 1<=sy<16 or not 0<=outside<4096 or outside in seed:raise ValueError('OUTSIDER')
    bits=[]
    for t,T in enumerate(Ts):
        bits.append(sum((outside>>pos[v][[j for j,U in enumerate(Ts) if v in U].index(t)])&1 for v in T)%2)
    if sum(x<<t for t,x in enumerate(bits))!=sy:raise ValueError('SYNDROME')
    removed={x for x in seed if bad[x^outside]};W=sorted((seed-removed)|{outside})
    if len(removed)!=record['removed_conflicts'] or len(W)!=record['support_size']:raise ValueError('COUNTS')
    if add_conflicting:W.append(next(iter(removed)))
    colors=override_colors if override_colors is not None else record['vertex_colors']
    if len(colors)!=10 or any(c not in (0,1,2) for c in colors):raise ValueError('COLORS')
    masks=[sum(1<<i for i,c in enumerate(colors) if c==k) for k in range(3)];pairs=0
    for a,b in combinations(W,2):
        if bad[a^b]:raise ValueError('FD')
    for a,b in combinations(W,2):
        mask=vmask[a^b]
        if any(mask&~C==0 for C in masks):raise ValueError('COLOR')
        pairs+=1
    return {'factors':record['factors'],'syndrome':sy,'support_size':len(W),'pair_checks':pairs}


def main():
    src=pin(SOURCE);cov=pin(COVERS);covers={tuple(x) for x in cov['exact_checks']['minimum_covers']}
    if len(covers)!=19 or len(src['cases'])!=285:raise ValueError('CASE_COUNT')
    cases={};geos={};pairchecks=0
    for r in src['cases']:
        key=(tuple(r['factors']),r['syndrome'])
        if key in cases or key[0] not in covers:raise ValueError('CASE')
        cases[key]=r
        if key[0] not in geos:geos[key[0]]=geometry(key[0])
        pairchecks+=verify(r,geos[key[0]])['pair_checks']
    if set(cases)!={(J,s) for J in covers for s in range(1,16)}:raise ValueError('COVERAGE')
    first=src['cases'][0];geo=geos[tuple(first['factors'])];controls={}
    for name,kw,reason in (('monochrome',{'override_colors':[0]*10},'COLOR'),('added_conflict',{'add_conflicting':True},'FD')):
        try:verify(first,geo,**kw)
        except ValueError as exc:
            if str(exc)!=reason:raise ValueError(('WRONG_REASON',name,str(exc)))
            controls[name]=reason
        else:raise ValueError(('MUTATION_ACCEPTED',name))
    out={'source_receipt_sha256':SOURCE[1],'cover_receipt_sha256':COVERS[1],
         'cover_count':len(covers),'syndromes_per_cover':15,'cases_checked':len(cases),'FD_and_color_pair_checks':pairchecks,
         'all_checked':True,'mutation_controls':controls,
         'limits':'Finite canonical support/FD/color replay only; coset translation and entropy implications are written separately.'}
    with OUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
