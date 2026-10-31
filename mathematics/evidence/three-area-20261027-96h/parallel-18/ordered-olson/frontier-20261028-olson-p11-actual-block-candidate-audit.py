#!/usr/bin/env python3
"""Verify actual block, REF, matching, deletion, and mixed witness data."""
import argparse
from collections import Counter
import hashlib
import json


def product(w,idx,p):
    x,b=0,0
    for i in idx:
        y,c=w[i]
        x=(x+(-y if b else y))%p
        b^=c
    return x,b


def reflection_support(w,p):
    values=[x for x,e in w if e]
    dp=[set() for _ in range(2*p+1)];dp[0].add(0)
    for i,y in enumerate(values):
        for k in range(min(i,2*p-1),-1,-1):
            dp[k+1] |= {(z+(y if k%2==0 else -y))%p for z in dp[k]}
    return dp[2*p]


def actual_data(w):
    refs=[i for i,(_,e) in enumerate(w) if e]
    F=len(refs)
    bounds=[]
    gaps=[]
    for q,i in enumerate(refs):
        j=refs[(q+1)%F]
        gap=w[i+1:j] if q+1<F else w[i+1:]+w[:j]
        gaps.append(gap)
        bounds.append(bool(gap) or w[i][0]!=w[j][0])
    if not any(bounds):
        return {'blocks':[[w[refs[0]][0],F]],'matching':F//2,'gaps':gaps,'refs':refs}
    start=(next(i for i,v in enumerate(bounds) if v)+1)%F
    blocks=[]
    for t in range(F):
        q=(start+t)%F
        if t==0 or bounds[(q-1)%F]:blocks.append([w[refs[q]][0],1])
        else:blocks[-1][1]+=1
    G=[set() for _ in refs]
    for q,edge in enumerate(bounds):
        if edge:G[q].add((q+1)%F);G[(q+1)%F].add(q)
    seen=set();sizes=[]
    for q in range(F):
        if q in seen:continue
        stack=[q];comp=set()
        while stack:
            x=stack.pop()
            if x in comp:continue
            comp.add(x);stack.extend(G[x]-comp)
        seen|=comp
        if len(comp)>1 and sum(len(G[x])==1 for x in comp)!=2:
            raise ValueError('RAW_NOT_PATHS')
        sizes.append(len(comp))
    return {'blocks':blocks,'matching':sum(n//2 for n in sizes),'components':sorted(sizes),
            'gaps':gaps,'refs':refs}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input')
    parser.add_argument('--output',required=True)
    args=parser.parse_args()
    with open(args.input,'rb') as src:raw=src.read()
    data=json.loads(raw);p=data['p'];w=data['word']
    if p!=11 or len(w)!=4*p-1 or any(x<0 or x>=p or e not in (0,1) for x,e in w):raise ValueError('INPUT')
    refs=[i for i,(_,e) in enumerate(w) if e];rot=[i for i,(_,e) in enumerate(w) if not e]
    if len(refs)!=3*p-2 or len(rot)!=p+1 or any(w[i][0]!=5 for i in rot):raise ValueError('TYPE_COUNTS')
    actual=actual_data(w)
    if any(len(gap)>1 for gap in actual['gaps']):raise ValueError('SINGLETON_GAPS')
    blocks=actual['blocks']
    o=sum(n%2 for _,n in blocks);e=sum(n%2==0 for _,n in blocks)
    if (o,e)!=(p+2,0):raise ValueError('ACTUAL_BLOCK_COUNTS')
    if actual['matching']!=7 or actual['matching']>p-4:raise ValueError('RAW_MATCHING')
    multiplicities=Counter(w[i][0] for i in refs)
    if max(multiplicities.values())>=2*p-1:raise ValueError('SEL_NOT_EXCLUDED')
    support=reflection_support(w,p)
    if 0 in support:raise ValueError('REF_NOT_EXCLUDED')
    deletion=[]
    for i in refs:
        post=actual_data(w[:i]+w[i+1:])
        deletion.append(sum(n%2 for _,n in post['blocks']))
    if any(n<=p for n in deletion):raise ValueError('DEL3_ELIGIBLE')
    unequal_empty=[(refs[q],refs[(q+1)%len(refs)]) for q,g in enumerate(actual['gaps'])
                   if not g and w[refs[q]][0]!=w[refs[(q+1)%len(refs)]][0]]
    if not unequal_empty:raise ValueError('RGR_RUN_CONDITION_NOT_EXCLUDED')
    selector=[0,1,2,3,4,5,6,7,8,9,10,11,13,14,15,16,19,20,22,23,25,26]
    if len(selector)!=2*p or selector!=sorted(set(selector)) or product(w,selector,p)!=(0,0):raise ValueError('MIXED_SELECTOR')
    bad=[v[:] for v in w];bad[selector[0]][0]=(bad[selector[0]][0]+1)%p
    if product(bad,selector,p)==(0,0):raise ValueError('MUTATION_SURVIVED')
    result={'result':'PASS_P11_ACTUAL_BLOCK_BASE_AUDIT','input_sha256':hashlib.sha256(raw).hexdigest(),
            'p':p,'actual_blocks':blocks,'actual_odd':o,'actual_even':e,
            'raw_matching':actual['matching'],'raw_components':actual['components'],
            'max_reflection_multiplicity':max(multiplicities.values()),
            'REF_support':sorted(support),'all_single_deletion_odd_counts':dict(Counter(deletion)),
            'empty_unequal_reflection_gaps':unequal_empty,'mixed_selector':selector,
            'source_status':'P/D0, WORD-P, literal RGR-LONG, SEL and DEL3 hypotheses not met; DS3 impossible by raw matching; full OLD/IPGEN unreviewed',
            'mutation_control':'single-selected-reflection exponent change detected',
            'scope':'one actual p11 word; no full L_RES membership or global theorem'}
    with open(args.output,'x',encoding='utf-8') as out:
        json.dump(result,out,sort_keys=True,indent=2);out.write('\n')
    print(json.dumps(result,sort_keys=True))


if __name__=='__main__':
    main()
