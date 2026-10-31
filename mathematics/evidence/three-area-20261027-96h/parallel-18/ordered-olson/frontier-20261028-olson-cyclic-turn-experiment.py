#!/usr/bin/env python3
"""Construct cyclic-cut reflection-turn witnesses and restore original order."""
import argparse
import importlib.util
import json
import random

spec=importlib.util.spec_from_file_location('turn','frontier-20261028-olson-reflection-turn-experiment.py')
turn=importlib.util.module_from_spec(spec)
spec.loader.exec_module(turn)
SEED=2026102819


def product(word,idx,p):
    x,b=0,0
    for i in idx:
        y,c=word[i]
        x=(x+(-y if b else y))%p
        b^=c
    return x,b


def make_case(rng,p,trial):
    F=3*p-2
    for _ in range(10000):
        ys=[rng.randrange(p) for _ in range(F)]
        d=[(ys[(i+1)%F]-ys[i])%p for i in range(F)]
        zeros=[i for i,x in enumerate(d) if x==0]
        turns=[i for i in range(F) if d[i] and d[(i+1)%F] and d[i]!=d[(i+1)%F]]
        if 1<=len(zeros)<=(p+1)//2 and turns:
            break
    else:
        raise ValueError('failed to sample eligible cyclic word')
    cut=zeros[0]
    start=(cut+1)%F
    ords=list(range(start,F))+list(range(start))
    vals=[ys[i] for i in ords]
    steps=[(y-x)%p for x,y in zip(vals,vals[1:])]
    t=next((i for i in range(F-2) if steps[i] and steps[i+1] and steps[i]!=steps[i+1]),None)
    if t is None or sum(x==0 for x in steps)>(p-1)//2:
        raise ValueError('zero-cut failed to expose linear turn')
    common=turn.match_outside(vals,p,t)
    M1=sorted(common+[(t,t+1)])
    M2=sorted(common+[(t+1,t+2)])
    A=turn.analyze_matching(vals,p,M1)
    B=turn.analyze_matching(vals,p,M2)
    selected=A['selected_ordinals'] if A['selected_ordinals'] is not None else B['selected_ordinals']
    if selected is None:
        raise ValueError('both rotated matchings missed identity')
    gaps=set(rng.sample(range(F),p+1))
    word=[]
    refs=[]
    for q,y in enumerate(ys):
        refs.append(len(word))
        word.append([y,1])
        if q in gaps:
            word.append([rng.randrange(1,p),0])
    rotated_selector=[refs[ords[q]] for q in selected]
    original_selector=sorted(rotated_selector)
    if len(original_selector)!=2*p or product(word,rotated_selector,p)!=(0,0) or product(word,original_selector,p)!=(0,0):
        raise ValueError('cyclic or original ordered product failed')
    return {'p':p,'trial':trial,'word':word,'cut_zero_edge':cut,'cyclic_zero_edges':len(zeros),
            'cyclic_turn_edges':turns,'rotated_selector':rotated_selector,'original_selector':original_selector}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',required=True)
    args=parser.parse_args()
    rng=random.Random(SEED)
    cases=[make_case(rng,p,trial) for p in (3,5,7,11,13) for trial in range(60)]
    with open(args.output,'x',encoding='utf-8') as out:
        json.dump({'seed':SEED,'cases':cases},out,sort_keys=True,separators=(',',':'))
        out.write('\n')
    print(json.dumps({'result':'PASS_CYCLIC_TURN_ORIGINAL_ORDER','actual_full_words':len(cases)},sort_keys=True))


if __name__=='__main__':
    main()
