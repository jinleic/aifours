#!/usr/bin/env python3
"""Direct designs exercising the rare o_pi=p+2 branches (no rejection loops).

Reuses construct() from frontier-20261028-olson-p2-band-experiment.py (same
producer family; the separate checker imports nothing).  Odd labels are
c,c,c,c+d,...,c+(p-1)d.  Designs:
  B: rotations at odd splits inside the two c-separators, none at the C1/C2
     boundaries, the rest at boundary gaps of distinct other odd runs;
  A2: two even runs between consecutive AP runs, each split oddly, the rest at
     boundary gaps of other odd runs;
  A1: one even run between AP runs split oddly after a boundary rotation;
  G: stretched odd AP run with a,b even, x odd and u=v (gamma sub-branch).
Random linear cuts; every selector multiplied directly by construct().
"""
import argparse
import importlib.util
import json
import os
import random

SEED=2026102841
HERE=os.path.dirname(os.path.abspath(__file__))
spec=importlib.util.spec_from_file_location('p2band',os.path.join(HERE,'frontier-20261028-olson-p2-band-experiment.py'))
P2=importlib.util.module_from_spec(spec);spec.loader.exec_module(P2)


def assemble(rng,p,runs,gap_after):
    """runs: list of [label,length]; gap_after: dict run_index -> k (gap after k-th reflection)."""
    vals=[];gaps=set();pos=0
    for t,(l,L) in enumerate(runs):
        vals+= [l]*L
        if t in gap_after:gaps.add(pos+gap_after[t]-1)
        pos+=L
    if len(vals)!=3*p-2:raise ValueError('F')
    w=[]
    for i,y in enumerate(vals):
        w.append([y,1])
        if i in gaps:w.append([rng.randrange(1,p),0])
    if sum(1 for _,e in w if not e)!=p+1:raise ValueError('R')
    cut=rng.randrange(len(w));return w[cut:]+w[:cut]


def base(rng,p,extra_even):
    c=rng.randrange(p);d=rng.randrange(1,p)
    A=[(c+k*d)%p for k in range(1,p)]
    runs=[[c,1],[None,2],[c,1],[None,2],[c,1]]+[[a,1] for a in A]
    kinds=['C1','B1','C2','B2','C3']+['A%d'%k for k in range(1,p)]
    for pos in extra_even:  # insert even runs after given A index (1-based) -> before A_{k+1}
        idx=kinds.index('A%d'%pos)+1
        runs.insert(idx,[None,2]);kinds.insert(idx,'E%d'%pos)
    n=len(runs)
    for i in range(n):
        if runs[i][0] is None:
            nxt=next(runs[(i+k)%n][0] for k in range(1,n) if runs[(i+k)%n][0] is not None)
            runs[i][0]=rng.choice([x for x in range(p) if x!=runs[i-1][0] and x!=nxt])
    rem=3*p-2-sum(L for _,L in runs)
    if rem<0:return None
    for _ in range(rem//2):runs[rng.randrange(n)][1]+=2
    if any(runs[i][0]==runs[(i+1)%n][0] for i in range(n)):return None
    return runs,kinds


def design(rng,p,kind):
    if kind=='B':
        b=base(rng,p,[]);
        if b is None:return None
        runs,kinds=b;gap={}
        for name in ('B1','B2'):
            t=kinds.index(name);L=runs[t][1];gap[t]=rng.choice([k for k in range(1,L+1) if k%2])
        pool=[kinds.index(x) for x in ['C3']+['A%d'%k for k in range(1,p)]]
        for t in rng.sample(pool,p-1):gap[t]=runs[t][1]
        return assemble(rng,p,runs,gap)
    if kind in ('A2','A1'):
        k0=rng.randrange(1,p-1)
        b=base(rng,p,[k0,k0] if kind=='A2' else [k0])
        if b is None:return None
        runs,kinds=b;gap={}
        ev=[t for t,nm in enumerate(kinds) if nm=='E%d'%k0]
        for t in ev:gap[t]=rng.choice([k for k in range(1,runs[t][1]+1) if k%2])
        ak=kinds.index('A%d'%k0)
        others=[t for t,nm in enumerate(kinds) if (nm.startswith('A') or nm.startswith('C')) and t!=ak]
        need=p+1-len(gap)
        if kind=='A1':gap[ak]=runs[ak][1];need-=1
        if need>len(others):return None
        for t in rng.sample(others,need):gap[t]=runs[t][1]
        return assemble(rng,p,runs,gap)
    raise ValueError(kind)


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--output',required=True);args=parser.parse_args()
    tgt=importlib.util.spec_from_file_location('p2tgt',os.path.join(HERE,'frontier-20261028-olson-p2-band-targeted-experiment.py'))
    TG=importlib.util.module_from_spec(tgt);tgt.loader.exec_module(TG)
    rng=random.Random(SEED);cases=[];branches={};none=0
    for p in (5,7,11,13):
        for kind in ('B','A2','A1','G'):
            got=0;tries=0
            while got<40 and tries<4000:
                tries+=1
                w=TG.gamma_word(rng,p) if kind=='G' else design(rng,p,kind)
                if w is None:none+=1;continue
                sel,case=P2.construct(w,p)
                cases.append({'p':p,'word':w,'selector':sel,'case':case,'mode':'design-'+kind});got+=1
                branches[case]=branches.get(case,0)+1
    with open(args.output,'x',encoding='utf-8') as out:
        json.dump({'seed':SEED,'unbuildable_draws':none,'cases':cases},out,sort_keys=True,separators=(',',':'));out.write('\n')
    print(json.dumps({'result':'PASS_P2_BAND_DESIGNS','actual_words':len(cases),'branches':dict(sorted(branches.items())),
                      'unbuildable_draws':none},sort_keys=True))


if __name__=='__main__':
    main()
