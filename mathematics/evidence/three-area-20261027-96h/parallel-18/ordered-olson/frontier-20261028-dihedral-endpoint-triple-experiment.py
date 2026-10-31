#!/usr/bin/env python3
"""Construct endpoint/triple selectors for bounded normal-form words."""
import argparse
import json
import random

SEED=2026102808


def multiply(word,indices,p):
    x,parity=0,0
    for k in sorted(indices):
        a,b=word[k]
        x=(x+(-a if parity else a))%p
        parity ^= b
    return x,parity


def make_case(rng,p,trial):
    F=p+2
    L=2*p-1
    n=p-2
    a=rng.randrange(1,p)
    triple=rng.randrange(F-2)
    triple_gaps={triple,triple+1}
    gaps=[i for i in range(F-1) if i not in triple_gaps]
    big=rng.choice(gaps)
    little=[i for i in gaps if i!=big]
    balanced=set(rng.sample(little,rng.randrange(n+1)))
    big_count=rng.randrange(p+1,L-len(balanced)+1)
    outer=L-big_count-len(balanced)
    before=rng.randrange(outer+1)
    after=outer-before
    ys=[rng.randrange(p) for _ in range(F)]
    y=ys[triple]
    ys[triple:triple+3]=[y]*3
    if trial%3==0:
        if triple==0:
            ys[-1]=ys[0]
        elif triple+2==F-1:
            ys[0]=ys[-1]
        else:
            ys[-1]=ys[0]
    word=[[a,0] for _ in range(before)]
    refs=[]
    for i in range(F):
        refs.append(len(word))
        word.append([ys[i],1])
        if i==F-1 or i in triple_gaps:
            continue
        if i==big:
            word.extend([[a,0] for _ in range(big_count)])
        elif i in balanced:
            gap=[[a,0],[(-a)%p,0]]
            if rng.randrange(2):
                gap.reverse()
            word.extend(gap)
        else:
            word.append([(-a)%p,0])
    word.extend([[a,0] for _ in range(after)])
    rotations=[k for k,(_,b) in enumerate(word) if not b]
    first,last=refs[0],refs[-1]
    plus=[k for k in rotations if ((-word[k][0] if first<k<last else word[k][0])%p)==a]
    minus=[k for k in rotations if ((-word[k][0] if first<k<last else word[k][0])%p)==(-a)%p]
    assert len(word)==4*p-1 and len(rotations)==3*p-3 and len(plus)>=n and len(minus)>=p+1
    target=(ys[-1]-ys[0])%p
    selector=None
    for q in range(2*p-1):
        other=2*p-2-q
        if q<=len(plus) and other<=len(minus) and (q-other)*a%p==target:
            selector=sorted(plus[:q]+minus[:other]+[first,last])
            break
    if selector is not None:
        mode='two_reflections'
    else:
        assert target==0
        triple_indices=[refs[i] for i in range(triple,triple+3) if refs[i] not in (first,last)]
        assert len(triple_indices)>=2
        selector=sorted(plus[:n]+minus[:n]+[first,last]+triple_indices[:2])
        mode='four_reflections'
    assert len(selector)==2*p and len(set(selector))==2*p and multiply(word,selector,p)==(0,0)
    return {'p':p,'trial':trial,'a':a,'word':word,'triple_ordinal':triple,'big_ordinal':big,
            'big_count':big_count,'outer_core':outer,'balanced_gaps':sorted(balanced),
            'selected_indices':selector,'mode':mode,'endpoint_values':[ys[0],ys[-1]]}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',required=True)
    args=parser.parse_args()
    rng=random.Random(SEED)
    cases=[make_case(rng,p,trial) for p in (3,5,7,11) for trial in range(120)]
    result={'seed':SEED,'cases':cases}
    with open(args.output,'x',encoding='utf-8') as out:
        json.dump(result,out,sort_keys=True,separators=(',',':'))
        out.write('\n')
    groups={}
    for c in cases:
        key=('outer' if c['outer_core'] else 'no_outer')+'/'+c['mode']
        groups[key]=groups.get(key,0)+1
    print(json.dumps({'result':'PASS_ENDPOINT_TRIPLE_CONSTRUCTION','cases':len(cases),'branches':groups},sort_keys=True))


if __name__=='__main__':
    main()
