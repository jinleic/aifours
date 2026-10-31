#!/usr/bin/env python3
"""Find avoidance prefixes with repeated consecutive triple targets."""
import argparse
import itertools
import json


def search(p):
    for length in range(4,p+2):
        for ds in itertools.product(range(1,p),repeat=length-1):
            v=[0]
            for d in ds:
                v.append((v[-1]+d)%p)
            if any((v[i]-v[j]+v[k]-v[l])%p==0 for i,j,k,l in itertools.combinations(range(length),4)):
                continue
            targets=[(v[i]-v[i+1]+v[i+2])%p for i in range(length-2)]
            if len(set(targets))<len(targets):
                return {'p':p,'length':length,'labels':v,'triple_targets':targets}
    return None


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',required=True)
    args=parser.parse_args()
    results=[search(p) for p in (3,5,7)]
    result={'result':'BOUNDED_TURN_TARGET_COUNTERSEARCH','first_counterexamples':results,
            'scope':'finite search of a proof route; not an Olson verdict'}
    with open(args.output,'x',encoding='utf-8') as out:
        json.dump(result,out,sort_keys=True,indent=2)
        out.write('\n')
    print(json.dumps(result,sort_keys=True))


if __name__=='__main__':
    main()
