#!/usr/bin/env python3
"""Bounded search for alternating-zero quadruples of distinct-adjacent labels."""
import argparse
import itertools
import json
import random

SEED=2026102820


def witness(values,p):
    for i,j,k,l in itertools.combinations(range(len(values)),4):
        if (values[i]-values[j]+values[k]-values[l])%p==0:
            return [i,j,k,l]
    return None


def cyclic_labels(p):
    # Translation invariance permits the first label 0; avoid only consecutive equals.
    for suffix in itertools.product(range(1,p),repeat=p+1):
        vals=[0]
        for d in suffix:
            vals.append((vals[-1]+d)%p)
        yield vals


def run(p,values):
    tested=found=0
    first_failure=None
    first_witness=None
    for vals in values:
        tested+=1
        idx=witness(vals,p)
        if idx is None:
            if first_failure is None:
                first_failure=vals
        else:
            found+=1
            if first_witness is None:
                first_witness={'labels':vals,'indices':idx}
    return {'p':p,'tested':tested,'with_four_reflection_witness':found,
            'without_four_reflection_witness':tested-found,
            'first_failure':first_failure,'first_witness':first_witness}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',required=True)
    args=parser.parse_args()
    rng=random.Random(SEED)
    results=[run(p,cyclic_labels(p)) for p in (3,5)]
    for p in (7,11):
        def samples():
            for _ in range(10000):
                vals=[0]
                for _ in range(p+1):
                    vals.append((vals[-1]+rng.randrange(1,p))%p)
                yield vals
        results.append(run(p,samples()))
    result={'result':'BOUNDED_ODD_RUN_FOUR_SEARCH','seed':SEED,'cases':results,
            'scope':'four-reflection witnesses on odd-run-label lists; NOT a full original-word verdict'}
    with open(args.output,'x',encoding='utf-8') as out:
        json.dump(result,out,sort_keys=True,indent=2)
        out.write('\n')
    print(json.dumps(result,sort_keys=True))


if __name__=='__main__':
    main()
