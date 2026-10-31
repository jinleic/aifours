#!/usr/bin/env python3
"""All-prime exception selector without any third-rotation condition."""
import argparse
import json
import random

SEED=2026102831


def product(w,idx,p):
    x,e=0,0
    for i in idx:
        y,b=w[i];x=(x+(-y if e else y))%p;e^=b
    return x,e


def make(rng,p,even):
    c=rng.randrange(p);u=rng.randrange(1,p);t=2*u%p
    labels=[(c+j*t)%p for j in range(p)]
    if even:
        k=rng.randrange(1,p)
        ev=rng.choice([x for x in range(p) if x!=labels[k-1] and x!=labels[k]])
        labels.insert(k,ev)
    units=[0]*len(labels);units[0]=rng.randrange(1,p-even)
    if even:units[k]=1
    for _ in range(p-1-sum(units)):
        units[rng.randrange(1,len(labels))]+=1
    vals=[];runs=[]
    for j,(y,n) in enumerate(zip(labels,units)):
        start=len(vals);length=2*n+(0 if even and j==k else 1)
        vals.extend([y]*length);runs.append(list(range(start,start+length)))
    gap0=0;gap1=runs[0][-1];gaps={gap0,gap1}
    forbid=set(range(1,gap1))
    possible=[i for i in range(len(vals)) if i not in gaps and i not in forbid]
    gaps.update(rng.sample(possible,p-1))
    chosen=[]
    for j,run in enumerate(runs):
        available=run[1:] if j==0 else run
        chosen.extend(available[i] for i in range(0,len(available)-1,2))
        chosen.extend(available[i+1] for i in range(0,len(available)-1,2))
    if len(chosen)!=2*p-2:raise ValueError('reflection selection')
    word=[];refs=[];rot={}
    for i,y in enumerate(vals):
        refs.append(len(word));word.append([y,1])
        if i in gaps:
            rot[i]=len(word);word.append([u if i==gap0 else (-u)%p,0])
    selected=[refs[i] for i in chosen]+[rot[gap0],rot[gap1]]
    cut=rng.choice(refs);N=len(word);actual=word[cut:]+word[:cut]
    selector=sorted((i-cut)%N for i in selected)
    marker=[(refs[0]-cut)%N,(rot[gap0]-cut)%N,(rot[gap1]-cut)%N]
    if N!=4*p-1 or len(selector)!=2*p or product(actual,selector,p)!=(0,0):raise ValueError('actual product')
    return {'p':p,'word':actual,'selector':selector,'marker':marker,'c':c,'u':u,
            'even_projection_runs':even}


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--output',required=True);args=parser.parse_args()
    rng=random.Random(SEED);cases=[make(rng,p,e) for p in (3,5,7,11,13) for e in (0,1) for _ in range(50)]
    with open(args.output,'x',encoding='utf-8') as out:
        json.dump({'seed':SEED,'cases':cases},out,sort_keys=True,separators=(',',':'));out.write('\n')
    print(json.dumps({'result':'PASS_OPPOSITE_ROTATION_EXCEPTION','actual_words':len(cases)},sort_keys=True))


if __name__=='__main__':
    main()
