#!/usr/bin/env python3
"""Force nontrivial constant-transport and bit-completion controls.

Producer family: imports construct/free_core from the candidate producer.
The independent audit imports neither. No theorem is inferred from checks.
"""
import argparse
from collections import Counter
import importlib.util
import json
from pathlib import Path
import random

SEED=2026102845
HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('band',HERE/'frontier-20261028-olson-universal-rotation-band-experiment-v1.py')
B=importlib.util.module_from_spec(spec);spec.loader.exec_module(B)


def make(rng,p,mode,trial):
    a=rng.randrange(p);d=rng.randrange(1,p);c=rng.randrange(1,p)
    refl=[a]*(2*p-1)+[(a+k*d)%p for k in range(1,p)]
    _,pairs=B.free_core([[x,1] for x in refl]);S={i for pr in pairs for i in pr}
    if mode=='same':gaps=[2]*(p+1)
    elif mode=='different':gaps=[0,2]+list(range(2*p-2,3*p-3))
    else:gaps=[rng.randrange(3*p-2) for _ in range(p+1)]
    if len(gaps)!=p+1:raise ValueError('COUNT')
    amounts=Counter(gaps);w=[];parity=0;nrot=0
    for i,x in enumerate(refl):
        w.append([x,1]);parity^=i in S
        for _ in range(amounts[i]):
            desired=(-c if nrot%2 else c)%p if mode=='inverse' else c
            w.append([(-desired if parity else desired)%p,0]);nrot+=1
    cut=0 if trial%2==0 else rng.randrange(len(w))
    return w[cut:]+w[:cut]


def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--output',required=True);args=ap.parse_args()
    rng=random.Random(SEED);cases=[];routes=Counter()
    for p in (3,5,7,11,13,17,23,31):
        for mode in ('same','different','inverse'):
            for trial in range(40):
                w=make(rng,p,mode,trial);sel,meta=B.construct(w,p)
                routes[meta['route']]+=1
                cases.append({'p':p,'word':w,'selector':sel,'proof_metadata':meta,'kind':'adversarial-'+mode})
    with open(args.output,'x',encoding='utf-8') as out:
        json.dump({'seed':SEED,'result':'PASS_ADVERSARIAL_UNIVERSAL_ROTATION_BAND','cases':cases,'routes':dict(routes)},out,sort_keys=True,separators=(',',':'));out.write('\n')
    print(json.dumps({'result':'PASS_ADVERSARIAL_UNIVERSAL_ROTATION_BAND','actual_words':len(cases),'routes':dict(routes)},sort_keys=True))


if __name__=='__main__':main()
