#!/usr/bin/env python3
"""Check REF failure for p odd projected AP runs and non-AP mutations."""
import argparse
import itertools
import json
import random

SEED=2026102825


def support(values,p):
    dp=[set() for _ in range(2*p+1)];dp[0].add(0)
    for i,y in enumerate(values):
        for k in range(min(i,2*p-1),-1,-1):
            dp[k+1] |= {(v+(y if k%2==0 else -y))%p for v in dp[k]}
    return dp[2*p]


def check(p,rng,trial):
    d=rng.randrange(1,p);start=rng.randrange(p)
    labels=[(start+j*d)%p for j in range(p)]
    units=[0]*p
    for _ in range(p-1):units[rng.randrange(p)]+=1
    values=[y for y,u in zip(labels,units) for _ in range(2*u+1)]
    S=support(values,p)
    if S!=set(range(1,p)):
        raise ValueError('odd projected AP support not exactly nonzero')
    # A swap that is genuinely non-AP is impossible only for p=3.
    mutated=None
    if p>=5:
        for i,j in itertools.combinations(range(p),2):
            candidate=labels[:];candidate[i],candidate[j]=candidate[j],candidate[i]
            steps=[(candidate[k+1]-candidate[k])%p for k in range(p-1)]
            if len(set(steps))>1:
                vals=[y for y,u in zip(candidate,units) for _ in range(2*u+1)]
                if 0 not in support(vals,p):raise ValueError('non-AP mutation did not create REF selector')
                mutated=[i,j]
                break
        if mutated is None:raise ValueError('non-AP mutation unavailable')
    return {'p':p,'trial':trial,'labels':labels,'units':units,'nonAP_swap':mutated}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',required=True)
    args=parser.parse_args()
    rng=random.Random(SEED)
    cases=[check(p,rng,t) for p in (3,5,7,11,13) for t in range(50)]
    with open(args.output,'x',encoding='utf-8') as out:
        json.dump({'result':'PASS_PROJECTED_ODD_AP','seed':SEED,'cases':cases,
                   'scope':'projection-only odd-run fixtures; no actual-block or L_RES claim'},out,sort_keys=True,indent=2)
        out.write('\n')
    print(json.dumps({'result':'PASS_PROJECTED_ODD_AP','cases':len(cases),
                      'nonAP_mutations':sum(c['nonAP_swap'] is not None for c in cases)},sort_keys=True))


if __name__=='__main__':
    main()
