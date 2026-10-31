#!/usr/bin/env python3
"""Use a third boundary rotation to resolve the AP-aligned exception."""
import argparse
import json
import random

SEED=2026102830


def product(w,idx,p):
    x,e=0,0
    for i in idx:
        y,b=w[i];x=(x+(-y if e else y))%p;e^=b
    return x,e


def make(rng,p):
    c=rng.randrange(p);u=rng.randrange(1,p);t=(2*u)%p
    labels=[(c+j*t)%p for j in range(p)]
    units=[0]*p;units[0]=rng.randrange(1,p)
    for _ in range(p-1-units[0]):units[rng.randrange(1,p)]+=1
    vals=[];runs=[]
    for y,n in zip(labels,units):
        start=len(vals);vals.extend([y]*(2*n+1));runs.append(list(range(start,len(vals))))
    k=rng.randrange(1,p-1);wval=rng.choice([x for x in range(1,p) if x!=(-u)%p])
    gap0=0;gap1=runs[0][-1];gap2=runs[k][-1]
    forbidden=set(range(1,gap1));gaps={gap0,gap1,gap2}
    available=[i for i in range(len(vals)) if i not in gaps and i not in forbidden]
    gaps.update(rng.sample(available,p-2))
    pairs=[]
    for j,run in enumerate(runs):
        run=run[2:] if j==0 else run
        pairs.extend((run[i],run[i+1]) for i in range(0,len(run)-1,2))
    if len(pairs)!=p-2:raise ValueError('pair count')
    reps=[]
    if wval!=u:
        d=(-(u+wval)*pow(t,-1,p))%p
        if not 1<=d<=p-2:raise ValueError('distance')
        i=max(1,k+1-d);j=i+d
        if not 1<=i<=k<j<=p-1:raise ValueError('cross reps')
        reps=[runs[i][-1],runs[j][-1]];pairs=pairs[:-1]
    refl=[0,1]+[z for pair in pairs for z in pair]+reps
    if len(refl)!=2*p-2:raise ValueError('selection size')
    word=[];refs=[];rot={}
    for i,y in enumerate(vals):
        refs.append(len(word));word.append([y,1])
        if i in gaps:
            val=u if i==gap0 else (-u)%p if i==gap1 else wval if i==gap2 else rng.randrange(1,p)
            rot[i]=len(word);word.append([val,0])
    selected=[refs[i] for i in refl]+[rot[gap0],rot[gap2]]
    cut=rng.choice(refs);N=len(word);actual=word[cut:]+word[:cut]
    selector=sorted((i-cut)%N for i in selected)
    marker=[(refs[0]-cut)%N,(rot[gap0]-cut)%N,(refs[1]-cut)%N,
            (rot[gap1]-cut)%N,(rot[gap2]-cut)%N]
    if N!=4*p-1 or len(selector)!=2*p or product(actual,selector,p)!=(0,0):raise ValueError('product')
    return {'p':p,'word':actual,'selector':selector,'marker':marker,'c':c,'u':u,'t':t,
            'k':k,'third_rotation':wval,'selected_pair_branch':wval!=u}


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--output',required=True);args=parser.parse_args()
    rng=random.Random(SEED);cases=[make(rng,p) for p in (3,5,7,11,13) for _ in range(100)]
    with open(args.output,'x',encoding='utf-8') as out:
        json.dump({'seed':SEED,'cases':cases},out,sort_keys=True,separators=(',',':'));out.write('\n')
    print(json.dumps({'result':'PASS_EXCEPTION_THIRD_ROTATION','actual_words':len(cases),
                      'cross_representative_branch':sum(c['selected_pair_branch'] for c in cases)},sort_keys=True))


if __name__=='__main__':
    main()
