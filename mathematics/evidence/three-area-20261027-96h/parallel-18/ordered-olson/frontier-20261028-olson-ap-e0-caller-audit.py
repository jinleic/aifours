#!/usr/bin/env python3
"""Audit exact structural and named finite callers on frozen AP/e0 words."""
import argparse
from collections import Counter
import hashlib
import json


def product(w,idx,p):
    x,e=0,0
    for i in idx:
        y,f=w[i]
        x=(x+(-y if e else y))%p
        e ^= f
    return x,e


def reflection_support(w,p):
    vals=[x for x,e in w if e]
    dp=[set() for _ in range(2*p+1)];dp[0].add(0)
    for i,y in enumerate(vals):
        for k in range(min(i,2*p-1),-1,-1):
            dp[k+1] |= {(v+(y if k%2==0 else -y))%p for v in dp[k]}
    return dp[2*p]


def cyclic_data(w):
    refs=[i for i,(_,e) in enumerate(w) if e]
    F=len(refs);gaps=[];bounds=[]
    for t,i in enumerate(refs):
        j=refs[(t+1)%F]
        gap=w[i+1:j] if t+1<F else w[i+1:]+w[:j]
        gaps.append(gap)
        bounds.append(bool(gap) or w[i][0]!=w[j][0])
    if not any(bounds):raise ValueError('RAW_FULL_ABSENCE')
    start=(next(i for i,v in enumerate(bounds) if v)+1)%F
    blocks=[]
    for q in range(F):
        t=(start+q)%F
        if q==0 or bounds[(t-1)%F]:blocks.append([w[refs[t]][0],1])
        else:blocks[-1][1]+=1
    G=[set() for _ in refs]
    for t,e in enumerate(bounds):
        if e:G[t].add((t+1)%F);G[(t+1)%F].add(t)
    seen=set();sizes=[]
    for i in range(F):
        if i in seen:continue
        stack=[i];comp=set()
        while stack:
            j=stack.pop()
            if j in comp:continue
            comp.add(j);stack.extend(G[j]-comp)
        seen |= comp
        if len(comp)>1 and sum(len(G[j])==1 for j in comp)!=2:raise ValueError('RAW_NOT_PATH')
        sizes.append(len(comp))
    return refs,gaps,blocks,sorted(sizes)


def doubling_witnesses(w,p):
    refs=[i for i,(_,e) in enumerate(w) if e]
    F=len(refs);gaprots=[];beta=[]
    for t,i in enumerate(refs):
        prev=refs[(t-1)%F]
        gap=w[prev+1:i] if t else w[prev+1:]+w[:i]
        gaprots.append([x for x,e in gap if not e])
        beta.append((w[prev][0]-w[i][0]-sum(gaprots[-1]))%p)
    hits=[];eligible=0
    for start in range(F):
        for j in range((p-1)//2+1):
            P=[(start+2*k)%F for k in range(j+1)]
            M=[(start+2*k+1)%F for k in range(j)]
            need=p-2*j-sum(len(gaprots[t]) for t in M)
            vals=[x for t in P for x in gaprots[t]]
            if not 0<=need<=len(vals):continue
            eligible+=1
            sums=[set() for _ in range(need+1)];sums[0].add(0)
            for i,x in enumerate(vals):
                for k in range(min(i,need-1),-1,-1):
                    sums[k+1] |= {(v+x)%p for v in sums[k]}
            target=(-sum(beta[t] for t in M))%p
            if target in sums[need]:hits.append({'start_gap':start,'j':j,'need':need})
    return hits,eligible


def check(case):
    p=case['p'];w=case['word'];b=case['rotation']
    expected=[[0,1],[b,0],[0,1],[b,0],[0,1],[b,0]]+[[1,1]]*(2*p-5)+[[2,1]]*3+[[b,0]]
    for j in range(3,p):expected += [[j,1],[b,0]]
    if w!=expected or len(w)!=4*p-1 or b!=(p-1)//2:raise ValueError('FROZEN_WORD_SHAPE')
    refs,gaps,blocks,components=cyclic_data(w)
    if len(refs)!=3*p-2 or sum(not e for _,e in w)!=p+1 or any(len(g)>1 for g in gaps):raise ValueError('ORIGINAL_COUNTS_GAPS')
    odd=sum(n%2 for _,n in blocks);even=sum(n%2==0 for _,n in blocks)
    if (odd,even)!=(p+2,0):raise ValueError('ACTUAL_BLOCK_PROFILE')
    nu=sum(n//2 for n in components)
    if components!=sorted([p+2,2]+[1]*(2*p-6)) or nu!=(p+3)//2 or nu>p-4:
        raise ValueError('RAW_GRAPH')
    if 0 in reflection_support(w,p):raise ValueError('REF_FAILURE')
    multiplicities=Counter(w[i][0] for i in refs)
    if max(multiplicities.values())>=2*p-1:raise ValueError('SEL_PREDICATE')
    deleted=[]
    for i in refs:
        _,_,after,_=cyclic_data(w[:i]+w[i+1:])
        oddafter=sum(n%2 for _,n in after)
        evenafter=sum(n%2==0 for _,n in after)
        H=sum(n//2 for _,n in after)
        deleted.append((oddafter,evenafter,p-1-H))
    if any(o<=p or k>=2 for o,e,k in deleted):raise ValueError('EVDEL_OR_D1')
    empty_unequal=[q for q,g in enumerate(gaps) if not g and w[refs[q]][0]!=w[refs[(q+1)%len(refs)]][0]]
    if not empty_unequal:raise ValueError('RGR_TYPE_RUN')
    hits,eligible=doubling_witnesses(w,p)
    if hits:raise ValueError('OLD_DOUBLING_HIT')
    pair_upper=(3*p-3)//2+(p+1)
    if pair_upper>=3*p-1:raise ValueError('DAVENPORT_BOUND')
    one=[i for i,(v,e) in enumerate(w) if e and v==1]
    two=[i for i,(v,e) in enumerate(w) if e and v==2]
    selector=sorted([0,1,2,3]+one[:2*p-6]+two[:2])
    if len(selector)!=2*p or product(w,selector,p)!=(0,0):raise ValueError('MIXED_WITNESS')
    return {'p':p,'actual_odd':odd,'actual_even':even,'raw_matching':nu,
            'raw_components':dict(Counter(components)),'REF_support':sorted(reflection_support(w,p)),
            'max_reflection_multiplicity':max(multiplicities.values()),
            'single_deletion_profiles':{str(k):v for k,v in Counter(deleted).items()},
            'empty_unequal_reflection_gaps':empty_unequal,'OLD_doubling_eligible_stretches_checked':eligible,
            'OLD_doubling_witnesses':len(hits),'davenport_max_items':pair_upper,'selector':selector}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input')
    parser.add_argument('--output',required=True)
    args=parser.parse_args()
    with open(args.input,'rb') as source:raw=source.read()
    data=json.loads(raw)
    if data['kind']!='UNPROMOTED_AP_ODD_RUN_E0_CANDIDATES':raise ValueError('INPUT_KIND')
    cases=[check(c) for c in data['cases']]
    # A separate explicit positive control: one actual gap with p copies of b.
    p=11;b=5;F=3*p-2
    positive=[[0,1]]+[[b,0]]*p+[[1,1],[b,0]]+[[2,1]]*(F-2)
    hits,_=doubling_witnesses(positive,p)
    if not hits:raise ValueError('POSITIVE_DOUBLING_CONTROL')
    result={'result':'PASS_AP_E0_LITERAL_CALLER_AUDIT','input_sha256':hashlib.sha256(raw).hexdigest(),
            'cases':cases,'positive_doubling_control_first_witness':hits[0],
            'scope':'literal tested callers and exact original witnesses; no complete OLD/IPGEN or residual-membership verdict'}
    with open(args.output,'x',encoding='utf-8') as out:
        json.dump(result,out,sort_keys=True,indent=2);out.write('\n')
    print(json.dumps(result,sort_keys=True))


if __name__=='__main__':
    main()
