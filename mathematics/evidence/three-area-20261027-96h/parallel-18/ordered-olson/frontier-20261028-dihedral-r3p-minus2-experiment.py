#!/usr/bin/env python3
"""Construct fixed-pair selectors for R=3p-2 actual words."""
import argparse
from collections import Counter,defaultdict
import itertools
import json
import random

SEED=2026102810


def product(word,indices,p):
    x,b=0,0
    for k in sorted(indices):
        t,e=word[k]
        x=(x+(-t if b else t))%p
        b^=e
    return x,b


def pair_record(word,p,i,j):
    signed={k:(-x if i<k<j else x)%p for k,(x,b) in enumerate(word) if not b}
    counts=Counter(signed.values())
    M=max(counts.values())
    record={'reflections':[i,j],'max_signed_multiplicity':M,'eligible':M<=2*p-1}
    if not record['eligible']:
        return record
    buckets=defaultdict(list)
    for k,value in signed.items():
        buckets[value].append(k)
    pairs=[]
    for _ in range(p-1):
        live=sorted((len(items),v) for v,items in buckets.items() if items)
        if len(live)<2:
            raise ValueError('p-1 unequal pairs unavailable')
        _,a=live[-1]
        _,b=live[-2]
        pairs.append([buckets[a].pop(),buckets[b].pop()])
    paired={k for pair in pairs for k in pair}
    fixed=next(k for k in signed if k not in paired)
    choices={signed[fixed]:[]}
    for u,v in pairs:
        new={}
        for value,chosen in choices.items():
            for k in (u,v):
                new.setdefault((value+signed[k])%p,chosen+[k])
        choices=new
    if len(choices)!=p:
        raise ValueError('omission sums not full')
    target=(sum(signed.values())+word[i][0]-word[j][0])%p
    omitted=choices[target]+[fixed]
    selector=sorted((set(signed)-set(omitted))|{i,j})
    if len(selector)!=2*p or product(word,selector,p)!=(0,0):
        raise ValueError('actual selector failure')
    record.update({'pairs':pairs,'fixed_omission':fixed,'omitted':omitted,'selector':selector})
    return record


def evaluate(word,p,label):
    refs=[k for k,(_,b) in enumerate(word) if b]
    assert len(word)==4*p-1 and len(refs)==p+1
    return {'p':p,'label':label,'word':word,
            'pairs':[pair_record(word,p,i,j) for i,j in itertools.combinations(refs,2)]}


def family(p,ys):
    word=[[1,0]]*(p-2)+[[ys[0],1]]+[[1,0]]*(p+1)+[[ys[1],1]]
    word += [item for y in ys[2:] for item in ([p-1,0],[y,1])]
    return word


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',required=True)
    args=parser.parse_args()
    rng=random.Random(SEED)
    cases=[]
    for p in (3,5,7,11):
        R=3*p-2
        for trial in range(120):
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
                    word.append([1,0])
            cases.append(evaluate(word,p,{'trial':trial,'mode':mode}))
    structured=[]
    for p in (3,5,7,11,13):
        for trial in range(20):
            ys=[rng.randrange(p) for _ in range(p+1)]
            case=evaluate(family(p,ys),p,{'family':'every-consecutive-pair-fails','trial':trial})
            refs=[i for i,(_,b) in enumerate(case['word']) if b]
            by_pair={tuple(r['reflections']):r for r in case['pairs']}
            assert all(not by_pair[(i,j)]['eligible'] for i,j in zip(refs,refs[1:]))
            assert by_pair[(refs[0],refs[-1])]['eligible']
            structured.append(case)
    with open(args.output,'x',encoding='utf-8') as out:
        json.dump({'seed':SEED,'cases':cases,'structured':structured},out,separators=(',',':'),sort_keys=True)
        out.write('\n')
    pairs=sum(len(c['pairs']) for c in cases)
    eligible=sum(r['eligible'] for c in cases for r in c['pairs'])
    print(json.dumps({'result':'PASS_R3P_MINUS2_FIXED_PAIRS','random_words':len(cases),
                      'random_reflection_pairs':pairs,'random_eligible_selectors':eligible,
                      'ineligible_not_decided':pairs-eligible,'structured_words':len(structured)},sort_keys=True))


if __name__=='__main__':
    main()
