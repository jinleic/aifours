#!/usr/bin/env python3
"""Construct identity-four selectors with nonzero even projection runs."""
import argparse
import json
import random

SEED=2026102827


def product(word,idx,p):
    x,e=0,0
    for i in idx:
        y,b=word[i];x=(x+(-y if e else y))%p;e^=b
    return x,e


def make(rng,p,even,trial):
    r=p+even
    for _ in range(10000):
        labels=[rng.randrange(p) for _ in range(r)]
        if all(labels[i]!=labels[(i+1)%r] for i in range(r)):break
    else:raise ValueError('could not sample cyclic run labels')
    units=[0]*r;units[0]=1
    for j in range(p,r):units[j]=1
    for _ in range(p-2-even):units[rng.randrange(r)]+=1
    vals=[];chosen_ord=[0,1]
    for j,(y,u) in enumerate(zip(labels,units)):
        start=len(vals);length=2*u+(0 if j>=p else 1)
        vals += [y]*length
        if j==0:chosen_ord += list(range(start+2,start+2+2*(u-1)))
        else:chosen_ord += list(range(start,start+2*u))
    if len(vals)!=3*p-2 or len(chosen_ord)!=2*p-2:raise ValueError('wrong projected counts')
    F=len(vals);gaps={0,1};gaps.update(rng.sample(range(2,F),p-1));b=rng.randrange(1,p)
    word=[];refs=[];rot=[]
    for i,y in enumerate(vals):
        refs.append(len(word));word.append([y,1])
        if i in gaps:
            rot.append(len(word));word.append([b if i in (0,1) else rng.randrange(1,p),0])
    chosen=[refs[i] for i in chosen_ord]+rot[:2]
    cut=rng.choice(refs)
    original=word[cut:]+word[:cut]
    selector=sorted((i-cut)%len(word) for i in chosen)
    block=[(i-cut)%len(word) for i in (refs[0],rot[0],refs[1],rot[1])]
    if len(word)!=4*p-1 or len(selector)!=2*p or product(original,selector,p)!=(0,0):
        raise ValueError('actual original selector failed')
    return {'p':p,'trial':trial,'even_projected_runs':even,'word':original,'selector':selector,
            'identity_block_cyclic_indices':block,'construction_cut':cut}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',required=True);args=parser.parse_args()
    rng=random.Random(SEED)
    cases=[make(rng,p,e,t) for p in (3,5,7,11,13) for e in range(1,min(2,p-2)+1) for t in range(20)]
    with open(args.output,'x',encoding='utf-8') as out:
        json.dump({'seed':SEED,'cases':cases},out,sort_keys=True,separators=(',',':'));out.write('\n')
    print(json.dumps({'result':'PASS_PROJECTION_IDENTITY4_EVEN','actual_words':len(cases)},sort_keys=True))


if __name__=='__main__':
    main()
