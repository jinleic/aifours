#!/usr/bin/env python3
"""Selectors when two chosen gaps belong to an even projected run."""
import argparse
import itertools
import json
import random

SEED=2026102833


def product(w,idx,p):
    x,e=0,0
    for i in idx:
        y,b=w[i];x=(x+(-y if e else y))%p;e^=b
    return x,e


def split(seg):
    return [(seg[i],seg[i+1]) for i in range(0,len(seg)-1,2)],(seg[-1] if len(seg)%2 else None)


def make(rng,p):
    odd=list(range(p));rng.shuffle(odd);k=rng.randrange(1,p)
    c=rng.choice([x for x in range(p) if x!=odd[k-1] and x!=odd[k]])
    labels=odd[:k]+[c]+odd[k:];even_index=k
    units=[0]*len(labels);units[k]=rng.randrange(1,p)
    for _ in range(p-1-units[k]):units[rng.choice([i for i in range(len(labels)) if i!=k])]+=1
    vals=[];runs=[]
    for j,(y,n) in enumerate(zip(labels,units)):
        start=len(vals);vals.extend([y]*(2*n+(j!=k)));runs.append(list(range(start,len(vals))))
    L=len(runs[k]);h=rng.randrange(L-1);q=rng.randrange(L-1-h);r=L-2-h-q
    first=runs[k][q];second=first+1;last=second+h
    mid=runs[k][q+2:q+2+h];suffix=runs[k][q+2+h:];prefix=runs[k][:q]
    mp,_=split(mid);sp,srep=split(suffix);qp,qrep=split(prefix)
    ordered_odd=runs[k+1:]+runs[:k];otherpairs=[];otherreps=[]
    for run in ordered_odd:
        a,b=split(run);otherpairs.extend(a);otherreps.append(b)
    pairs=mp+sp+otherpairs+qp
    u,v=rng.randrange(p),rng.randrange(p);t=(u-v)%p;chosen_reps=[]
    if len(pairs) not in (p-2,p-3):raise ValueError('pair count')
    if t:
        chosen_reps=next(([i,j] for i,j in itertools.combinations(otherreps,2)
                          if (vals[i]-vals[j])%p==t),None)
        if chosen_reps is None:raise ValueError('difference support')
        if len(pairs)==p-2:pairs=pairs[:-1]
    elif len(pairs)==p-3:
        c_extra=srep if srep is not None else qrep
        if c_extra is None:raise ValueError('missing extra c')
        chosen_reps=[c_extra,next(i for i in otherreps if vals[i]==c)]
    chosen=[first,second]+[i for pair in pairs for i in pair]+chosen_reps
    if len(chosen)!=2*p-2 or len(set(chosen))!=len(chosen):raise ValueError('selector size')
    gaps={first,last};forbid=set(range(second,last))
    options=[i for i in range(len(vals)) if i not in gaps and i not in forbid]
    gaps.update(rng.sample(options,p-1));word=[];refs=[];rot={}
    for i,y in enumerate(vals):
        refs.append(len(word));word.append([y,1])
        if i in gaps:
            rot[i]=len(word);word.append([u if i==first else v if i==last else rng.randrange(1,p),0])
    selected=[refs[i] for i in chosen]+[rot[first],rot[last]]
    cut=rng.choice(refs);N=len(word);actual=word[cut:]+word[:cut]
    selector=sorted((i-cut)%N for i in selected)
    segment=[(refs[first]-cut)%N,(rot[first]-cut)%N,(refs[second]-cut)%N,(rot[last]-cut)%N]
    if N!=4*p-1 or len(selector)!=2*p or product(actual,selector,p)!=(0,0):raise ValueError('product')
    return {'p':p,'word':actual,'selector':selector,'actual_segment':segment,'h':h,'q':q,'r':r,
            'u':u,'v':v,'target':t,'pairs_after_two':len(pairs)}


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--output',required=True);args=parser.parse_args()
    rng=random.Random(SEED);cases=[make(rng,p) for p in (3,5,7,11,13) for _ in range(200)]
    with open(args.output,'x',encoding='utf-8') as out:
        json.dump({'seed':SEED,'cases':cases},out,sort_keys=True,separators=(',',':'));out.write('\n')
    print(json.dumps({'result':'PASS_EVENRUN_STRETCHED','actual_words':len(cases),
                      'nonzero_target':sum(c['target']!=0 for c in cases)},sort_keys=True))


if __name__=='__main__':
    main()
