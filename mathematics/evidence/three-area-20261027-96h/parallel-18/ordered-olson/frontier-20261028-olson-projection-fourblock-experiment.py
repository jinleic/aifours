#!/usr/bin/env python3
"""Construct selectors for arbitrary two rotation values and distinct odd runs."""
import argparse
import itertools
import json
import random

SEED=2026102828


def product(w,idx,p):
    x,e=0,0
    for i in idx:
        y,b=w[i];x=(x+(-y if e else y))%p;e^=b
    return x,e


def make(rng,p,even,trial):
    odd=list(range(p));rng.shuffle(odd)
    labels=odd[:]
    for _ in range(even):
        options=[x for x in range(p) if x!=labels[-1] and x!=labels[0]]
        labels.append(rng.choice(options))
    if any(labels[i]==labels[(i+1)%len(labels)] for i in range(len(labels))):
        raise ValueError('cyclic label collision')
    units=[0]*len(labels);units[0]=1
    for j in range(p,len(labels)):units[j]=1
    for _ in range(p-2-even):units[rng.randrange(len(labels))]+=1
    vals=[];runs=[]
    for j,(y,h) in enumerate(zip(labels,units)):
        start=len(vals);length=2*h+(0 if j>=p else 1)
        vals += [y]*length;runs.append(list(range(start,start+length)))
    if len(vals)!=3*p-2:raise ValueError('projection length')
    # Actual first block has arbitrary nonzero rotations u,v.
    u=rng.randrange(1,p);v=rng.randrange(1,p)
    if trial%2==0 and u==v:v=(v%(p-1))+1
    target=(u-v)%p
    residual=[run[2:] if j==0 else run[:] for j,run in enumerate(runs)]
    pairs=[];reps=[]
    for j,run in enumerate(residual):
        for k in range(0,len(run)-1,2):pairs.append((run[k],run[k+1]))
        if j<p:reps.append(run[-1])
    if len(pairs)!=p-2 or len(reps)!=p:raise ValueError('residual pairing')
    active=[]
    if target:
        active=next(([reps[i],reps[j]] for i,j in itertools.combinations(range(p),2)
                     if (vals[reps[i]]-vals[reps[j]])%p==target),None)
        if active is None:raise ValueError('directed support missing target')
        pairs=pairs[:-1]
    refl_ord=[0,1]+[q for pair in pairs for q in pair]+active
    if len(refl_ord)!=2*p-2:raise ValueError('wrong reflection selection')
    gaps={0,1};gaps.update(rng.sample(range(2,len(vals)),p-1))
    word=[];refs=[];rots=[]
    for i,y in enumerate(vals):
        refs.append(len(word));word.append([y,1])
        if i in gaps:
            rotval=u if i==0 else v if i==1 else rng.randrange(1,p)
            rots.append(len(word));word.append([rotval,0])
    chosen=[refs[i] for i in refl_ord]+rots[:2]
    cut=rng.choice(refs);original=word[cut:]+word[:cut]
    selector=sorted((i-cut)%len(word) for i in chosen)
    block=[(i-cut)%len(word) for i in (refs[0],rots[0],refs[1],rots[1])]
    if len(word)!=4*p-1 or len(selector)!=2*p or product(original,selector,p)!=(0,0):
        raise ValueError('original selector failed')
    return {'p':p,'trial':trial,'even_projected_runs':even,'word':original,'selector':selector,
            'fourblock_cyclic_indices':block,'target':target,'construction_cut':cut}


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--output',required=True);args=parser.parse_args()
    rng=random.Random(SEED)
    cases=[make(rng,p,e,t) for p in (3,5,7,11,13) for e in range(0,min(1,p-2)+1) for t in range(50)]
    with open(args.output,'x',encoding='utf-8') as out:
        json.dump({'seed':SEED,'cases':cases},out,sort_keys=True,separators=(',',':'));out.write('\n')
    print(json.dumps({'result':'PASS_ARBITRARY_FOURBLOCK_ROTATIONS','actual_words':len(cases),
                      'nonzero_targets':sum(c['target']!=0 for c in cases)},sort_keys=True))


if __name__=='__main__':
    main()
