#!/usr/bin/env python3
"""Exact reflection-only 2p witnesses for unit-step exponent walks."""
import argparse
import itertools
import json
import random

SEED=2026102817


def selector(values,p):
    states=[{} for _ in range(2*p+1)]
    states[0][0]=()
    for i,y in enumerate(values):
        for k in range(min(i,2*p-1),-1,-1):
            for value,indices in states[k].items():
                new=(value+(y if k%2==0 else -y))%p
                if new not in states[k+1]:
                    states[k+1][new]=indices+(i,)
    result=states[2*p].get(0)
    if result is not None:
        if len(result)!=2*p or len(set(result))!=2*p:
            raise ValueError('invalid reflection-only indices')
        if sum((1 if q%2==0 else -1)*values[i] for q,i in enumerate(result))%p:
            raise ValueError('reflection-only product not identity')
    return result


def word_from_steps(steps,p):
    values=[0]
    for d in steps:
        values.append((values[-1]+d)%p)
    return values


def run(p,steps_iter):
    tested=solved=0
    first_failure=None
    first_witness=None
    for steps in steps_iter:
        tested+=1
        values=word_from_steps(steps,p)
        indices=selector(values,p)
        if indices is None:
            if first_failure is None:
                first_failure={'steps':steps,'values':values}
        else:
            solved+=1
            if first_witness is None:
                first_witness={'steps':steps,'values':values,'indices':indices}
    return {'p':p,'tested':tested,'reflection_only_witnesses':solved,
            'reflection_only_failures':tested-solved,'first_failure':first_failure,'first_witness':first_witness}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',required=True)
    args=parser.parse_args()
    rng=random.Random(SEED)
    cases=[]
    for p in (3,5):
        cases.append(run(p,itertools.product((-1,1),repeat=3*p-3)))
    for p in (7,11):
        cases.append(run(p,([rng.choice((-1,1)) for _ in range(3*p-3)] for _ in range(600))))
    result={'result':'BOUNDED_REFLECTION_WALKS','seed':SEED,'cases':cases,
            'scope':'reflection-only exponent walks; no original-residual or all-prime theorem'}
    with open(args.output,'x',encoding='utf-8') as out:
        json.dump(result,out,sort_keys=True,indent=2)
        out.write('\n')
    print(json.dumps(result,sort_keys=True))


if __name__=='__main__':
    main()
