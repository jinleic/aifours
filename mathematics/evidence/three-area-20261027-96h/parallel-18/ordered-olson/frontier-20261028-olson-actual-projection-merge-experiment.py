#!/usr/bin/env python3
"""Check actual-block/projection collapse states and REF selectors."""
import argparse
import importlib.util
import json
import random

spec=importlib.util.spec_from_file_location('walk','frontier-20261028-olson-reflection-walk-experiment.py')
walk=importlib.util.module_from_spec(spec)
spec.loader.exec_module(walk)
SEED=2026102824


def product(word,idx,p):
    x,b=0,0
    for i in idx:
        y,c=word[i]
        x=(x+(-y if b else y))%p
        b^=c
    return x,b


def build(rng,p,kind,trial):
    if kind=='no-merge':labels=[j%p for j in range(p+2)];even=None
    elif kind=='one-collapse':labels=[0,0,0]+list(range(1,p));even=None
    elif kind=='two-collapse':labels=[0,0,1,1]+list(range(2,p));even=None
    else:labels=[j%p for j in range(p+3)];even=0
    r=len(labels)
    equal={i for i in range(r) if labels[i]==labels[(i+1)%r]}
    if len(equal)>p+1:raise ValueError('too many mandatory occupied boundaries')
    selected=set(equal)
    selected.update(rng.sample([i for i in range(r) if i not in selected],p+1-len(selected)))
    units=[0]*r
    if even is not None:units[even]=1
    for _ in range(p-2-(1 if even is not None else 0)):
        units[rng.randrange(r)]+=1
    w=[]
    for j,y in enumerate(labels):
        length=2*units[j]+(0 if j==even else 1)
        w += [[y,1]]*length
        if j in selected:w.append([rng.randrange(1,p),0])
    refs=[i for i,(_,b) in enumerate(w) if b]
    cut=rng.choice(refs)
    w=w[cut:]+w[:cut]
    refs=[i for i,(_,b) in enumerate(w) if b]
    vals=[w[i][0] for i in refs]
    start=next(i for i in range(len(vals)) if vals[i]!=vals[(i-1)%len(vals)])
    vv=vals[start:]+vals[:start]
    rr=[]
    for y in vv:
        if not rr or rr[-1][0]!=y:rr.append([y,1])
        else:rr[-1][1]+=1
    odd=[y for y,n in rr if n%2]
    ep=sum(n%2==0 for _,n in rr)
    ords=walk.selector(vals,p)
    selector=None if ords is None else [refs[i] for i in ords]
    if selector is not None and product(w,selector,p)!=(0,0):raise ValueError('REF product invalid')
    if len(odd)==p+2 and (ep>1 or selector is None):raise ValueError('uncollapsed projection branch failed')
    if len(odd)<=p-2 and selector is None:raise ValueError('multiple-collapse projection branch failed')
    if selector is None and (len(odd)!=p or len(set(odd))!=p):raise ValueError('REF failure outside p-distinct projection branch')
    return {'p':p,'trial':trial,'kind':kind,'word':w,'actual_even':int(even is not None),
            'projected_odd':len(odd),'projected_even':ep,'projected_odd_labels':odd,
            'selector':selector}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',required=True)
    args=parser.parse_args()
    rng=random.Random(SEED)
    cases=[build(rng,p,kind,t) for p in (3,5,7,11,13)
           for kind in ('no-merge','one-collapse','two-collapse','one-even') for t in range(30)]
    with open(args.output,'x',encoding='utf-8') as out:
        json.dump({'seed':SEED,'cases':cases},out,sort_keys=True,separators=(',',':'));out.write('\n')
    counts={}
    for c in cases:
        key=f"{c['kind']}/o{c['projected_odd']}/"+('REF' if c['selector'] is not None else 'REFfail')
        counts[key]=counts.get(key,0)+1
    print(json.dumps({'result':'PASS_ACTUAL_PROJECTION_MERGE_EXPERIMENT','cases':len(cases),'branches':counts},sort_keys=True))


if __name__=='__main__':
    main()
