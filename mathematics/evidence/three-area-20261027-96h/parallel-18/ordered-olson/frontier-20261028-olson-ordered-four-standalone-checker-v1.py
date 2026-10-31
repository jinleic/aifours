#!/usr/bin/env python3
"""Fresh finite direct-pair witness checker for the standalone ordered-four lemma."""
import argparse
import itertools
import json
import random

SEED=2026102823


def find(values,p):
    if len(values)!=p+2:
        raise ValueError('BAD_LENGTH')
    if any(x<0 or x>=p for x in values):
        raise ValueError('VALUE_RANGE')
    if any(a==b for a,b in zip(values,values[1:])):
        raise ValueError('ADJACENT_EQUAL')
    differences={}
    for k in range(2,len(values)-1):
        j=k-1
        for i in range(j):
            differences.setdefault((values[i]-values[j])%p,(i,j))
        for l in range(k+1,len(values)):
            target=(values[l]-values[k])%p
            if target in differences:
                i,j=differences[target]
                if not (i<j<k<l) or (values[i]-values[j]+values[k]-values[l])%p:
                    raise ValueError('INVALID_ORIGINAL_INDICES')
                return i,j,k,l
    return None


def exact(p):
    total=0
    for steps in itertools.product(range(1,p),repeat=p+1):
        values=[0]
        for d in steps:values.append((values[-1]+d)%p)
        if find(values,p) is None:raise ValueError('FINITE_COUNTEREXAMPLE')
        total+=1
    return total


def crossing(p):
    total=0
    for a in range(p):
        for b in range(p):
            if a==b:continue
            x=(2*a-b)%p
            for pattern in ([a,b,a,b],[b,a,b,a]):
                for gap in range(5):
                    vals=pattern[:gap]+[x]+pattern[gap:]
                    if not any((vals[i]-vals[j]+vals[k]-vals[l])%p==0 for i,j,k,l in itertools.combinations(range(5),4)):
                        raise ValueError('CROSSING_INSERTION_FAILURE')
                    total+=1
    return total


def expect_error(values,p,expected):
    try:find(values,p)
    except ValueError as exc:
        if str(exc)==expected:return expected
        raise ValueError('CONTROL_WRONG: '+str(exc)) from exc
    raise ValueError('CONTROL_SURVIVED')


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',required=True)
    args=parser.parse_args()
    rng=random.Random(SEED)
    samples={}
    for p in (7,11,13):
        count=0
        for _ in range(2000):
            vals=[0]
            for _ in range(p+1):vals.append((vals[-1]+rng.randrange(1,p))%p)
            if find(vals,p) is None:raise ValueError('SAMPLED_COUNTEREXAMPLE')
            count+=1
        samples[str(p)]=count
    controls=[expect_error([0,1,2,3,4,0],5,'BAD_LENGTH'),
              expect_error([0,0,1,2,3,4,1],5,'ADJACENT_EQUAL'),
              expect_error([0,1,2,3,4,0,5],5,'VALUE_RANGE')]
    result={'result':'PASS_STANDALONE_ORDERED_FOUR_FINITE_CHECK','seed':SEED,
            'normalized_complete_sequences':{str(p):exact(p) for p in (3,5)},
            'sampled_sequences':samples,'crossing_extension_cases':{str(p):crossing(p) for p in (3,5,7)},
            'intentional_control_rejections':controls,
            'scope':'standalone field-sequence lemma only; no actual-block, L_RES, f111 or old-review assertion'}
    with open(args.output,'x',encoding='utf-8') as out:
        json.dump(result,out,sort_keys=True,indent=2);out.write('\n')
    print(json.dumps(result,sort_keys=True))


if __name__=='__main__':
    main()
