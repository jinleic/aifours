#!/usr/bin/env python3
"""Construct original selectors from a cyclic identity-four and projected pairs."""
import argparse
import json
import random

SEED=2026102826


def product(word,idx,p):
    x,e=0,0
    for i in idx:
        y,b=word[i]
        x=(x+(-y if e else y))%p
        e^=b
    return x,e


def make(rng,p,trial):
    labels=[j for j in range(p)]
    rng.shuffle(labels)
    units=[0]*p
    units[0]=1
    for _ in range(p-2):units[rng.randrange(p)]+=1
    vals=[];selected_ord=[0,1]
    for j,(y,u) in enumerate(zip(labels,units)):
        start=len(vals);length=2*u+1
        vals += [y]*length
        if j==0:selected_ord += list(range(start+2,start+2+2*(u-1)))
        else:selected_ord += list(range(start,start+2*u))
    if len(vals)!=3*p-2 or len(selected_ord)!=2*p-2:
        raise ValueError('projection counts')
    F=len(vals);gaps={0,1}
    gaps.update(rng.sample(range(2,F),p-1))
    b=rng.randrange(1,p)
    word=[];refs=[];rot=[]
    for i,y in enumerate(vals):
        refs.append(len(word));word.append([y,1])
        if i in gaps:
            rot.append(len(word));word.append([b if i in (0,1) else rng.randrange(1,p),0])
    if len(word)!=4*p-1 or len(rot)!=p+1:
        raise ValueError('full word counts')
    chosen=[refs[i] for i in selected_ord]+rot[:2]
    # The first two occupied gaps are exactly the two identity-block rotations.
    if rot[:2]!=[refs[0]+1,refs[1]+1]:raise ValueError('identity block not consecutive')
    cut=rng.choice(refs)
    original=word[cut:]+word[:cut]
    selector=sorted((i-cut)%len(word) for i in chosen)
    block=[(x-cut)%len(word) for x in (refs[0],rot[0],refs[1],rot[1])]
    if len(selector)!=2*p or product(original,selector,p)!=(0,0):
        raise ValueError('original product failed')
    return {'p':p,'trial':trial,'word':original,'selector':selector,'identity_block_cyclic_indices':block,
            'construction_cut':cut,'projection_run_units':units}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',required=True);args=parser.parse_args()
    rng=random.Random(SEED)
    cases=[make(rng,p,t) for p in (3,5,7,11,13) for t in range(50)]
    with open(args.output,'x',encoding='utf-8') as out:
        json.dump({'seed':SEED,'cases':cases},out,sort_keys=True,separators=(',',':'));out.write('\n')
    print(json.dumps({'result':'PASS_PROJECTION_IDENTITY4','actual_words':len(cases)},sort_keys=True))


if __name__=='__main__':
    main()
