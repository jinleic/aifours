#!/usr/bin/env python3
"""Case B with loss 0: all p+1 rotations at boundary gaps of distinct odd runs.

Reuses base()/assemble() of frontier-20261028-olson-p2-band-design-experiment.py
and construct() of frontier-20261028-olson-p2-band-experiment.py (same
producer family; the separate checker imports nothing).
"""
import argparse
import importlib.util
import json
import os
import random

SEED=2026102842
HERE=os.path.dirname(os.path.abspath(__file__))


def load(name,file):
    spec=importlib.util.spec_from_file_location(name,os.path.join(HERE,file))
    mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod);return mod


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--output',required=True);args=parser.parse_args()
    P2=load('p2band','frontier-20261028-olson-p2-band-experiment.py')
    DS=load('p2design','frontier-20261028-olson-p2-band-design-experiment.py')
    rng=random.Random(SEED);cases=[];branches={}
    for p in (5,7,11,13):
        got=0
        while got<40:
            b=DS.base(rng,p,[])
            if b is None:continue
            runs,kinds=b
            odd=[t for t,(l,L) in enumerate(runs) if L%2]
            gap={t:runs[t][1] for t in rng.sample(odd,p+1)}
            w=DS.assemble(rng,p,runs,gap)
            sel,case=P2.construct(w,p)
            cases.append({'p':p,'word':w,'selector':sel,'case':case,'mode':'design-B0'});got+=1
            branches[case]=branches.get(case,0)+1
    with open(args.output,'x',encoding='utf-8') as out:
        json.dump({'seed':SEED,'cases':cases},out,sort_keys=True,separators=(',',':'));out.write('\n')
    print(json.dumps({'result':'PASS_P2_BAND_DESIGN_B0','actual_words':len(cases),'branches':dict(sorted(branches.items()))},sort_keys=True))


if __name__=='__main__':
    main()
