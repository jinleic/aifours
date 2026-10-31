#!/usr/bin/env python3
"""Bounded actual-word producer for the R=3p-4 diverse-swap lemma."""
import argparse
from collections import Counter,defaultdict
import itertools
import json
import random

SEED=2026102809


def product(word,idx,p):
    x,parity=0,0
    for k in sorted(idx):
        y,b=word[k]
        x=(x+(-y if parity else y))%p
        parity ^= b
    return x,parity


def make_selector(word,p,i,j):
    signed={k:(-x if i<k<j else x)%p for k,(x,b) in enumerate(word) if not b}
    buckets=defaultdict(list)
    for k,v in signed.items():
        buckets[v].append(k)
    M=max(map(len,buckets.values()))
    x=max(buckets,key=lambda v:(len(buckets[v]),v))
    others=[v for v in buckets if v!=x]
    diffclasses={min((v-x)%p,(x-v)%p) for v in others}
    eligible=len(buckets)>=3 and (M<=2*p-3 or (M==2*p-2 and len(diffclasses)>=2))
    record={'reflections':[i,j],'signed_max':M,'signed_support':len(buckets),
            'nonmajor_difference_classes':len(diffclasses),'eligible':eligible}
    if not eligible:
        return record
    crossing=next(((y,z) for y,z in itertools.combinations(others,2)
                   if (y-x)%p != (x-z)%p),None)
    if crossing:
        y,z=crossing
        seed=[[buckets[x].pop(),buckets[y].pop()], [buckets[x].pop(),buckets[z].pop()]]
    else:
        y=next(v for v in others if len(buckets[v])>=2)
        z=next(v for v in others if v!=y)
        seed=[[buckets[x].pop(),buckets[y].pop()], [buckets[y].pop(),buckets[z].pop()]]
    pairs=seed[:]
    while len(pairs)<p-2:
        live=sorted((len(indices),v) for v,indices in buckets.items() if indices)
        if len(live)<2:
            raise ValueError('unequal pair extension failed')
        _,u=live[-1]
        _,v=live[-2]
        pairs.append([buckets[u].pop(),buckets[v].pop()])
    choices={0:[]}
    for u,v in pairs:
        new={}
        for total,indices in choices.items():
            for k in (u,v):
                new.setdefault((total+signed[k])%p,indices+[k])
        choices=new
    if len(choices)!=p:
        raise ValueError('diverse swap support not full')
    target=(sum(signed.values())+word[i][0]-word[j][0])%p
    omitted=choices[target]
    selected=sorted((set(signed)-set(omitted)) | {i,j})
    if len(selected)!=2*p or product(word,selected,p)!=(0,0):
        raise ValueError('actual original selector failed')
    record.update({'unequal_signed_pairs':pairs,'omitted_rotations':omitted,'selected_indices':selected})
    return record


def evaluate(word,p,label):
    refs=[i for i,(_,b) in enumerate(word) if b]
    assert len(word)==4*p-1 and len(refs)==p+3
    return {'p':p,'label':label,'word':word,
            'pairs':[make_selector(word,p,i,j) for i,j in itertools.combinations(refs,2)]}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',required=True)
    args=parser.parse_args()
    rng=random.Random(SEED)
    cases=[]
    for p in (5,7,11):
        R=3*p-4
        for trial in range(30):
            sites=set(rng.sample(range(4*p-1),R))
            mode=trial%3
            word=[]
            for k in range(4*p-1):
                if k not in sites:
                    word.append([rng.randrange(p),1])
                elif mode==0:
                    word.append([rng.randrange(p),0])
                elif mode==1:
                    word.append([rng.choice((0,0,0,1,p-1)),0])
                else:
                    word.append([rng.choice((0,0,0,1,2)),0])
            cases.append(evaluate(word,p,{'trial':trial,'mode':mode}))
    special=[]
    for p in (5,7,11,13):
        # Pair at positions 0,1; signed 0 has 2p-2 copies, with 1 and 2
        # as nonopposite difference classes among p-2 other values.
        word=[[0,1],[1,1]]+[[0,0]]*(2*p-2)+[[1,0]]*(p-3)+[[2,0]]+[[0,1]]*(p+1)
        case=evaluate(word,p,{'family':'boundary-majority'})
        assert case['pairs'][0]['eligible'] and case['pairs'][0]['signed_max']==2*p-2
        special.append(case)
    with open(args.output,'x',encoding='utf-8') as out:
        json.dump({'seed':SEED,'cases':cases,'special':special},out,separators=(',',':'),sort_keys=True)
        out.write('\n')
    eligible=sum(r['eligible'] for case in cases for r in case['pairs'])
    allpairs=sum(len(case['pairs']) for case in cases)
    print(json.dumps({'result':'PASS_DIVERSE_SIGNED_SWAP','words':len(cases),'all_reflection_pairs':allpairs,
                      'eligible_actual_selectors':eligible,'ineligible_pairs_not_decided':allpairs-eligible,
                      'special_boundary_words':len(special)},sort_keys=True))


if __name__=='__main__':
    main()
