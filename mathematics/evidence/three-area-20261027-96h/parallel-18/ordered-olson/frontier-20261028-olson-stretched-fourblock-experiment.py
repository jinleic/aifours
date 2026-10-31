#!/usr/bin/env python3
"""Original-word selectors with two rotations in one odd projected run."""
import argparse
import itertools
import json
import random

SEED=2026102829


def product(w,indices,p):
    x,e=0,0
    for i in indices:
        y,b=w[i];x=(x+(-y if e else y))%p;e^=b
    return x,e


def split(seg):
    return [(seg[i],seg[i+1]) for i in range(0,len(seg)-1,2)],(seg[-1] if len(seg)%2 else None)


def make(rng,p):
    labels=list(range(p));rng.shuffle(labels)
    units=[0]*p;units[0]=rng.randrange(1,p)
    for _ in range(p-1-units[0]):units[rng.randrange(1,p)]+=1
    vals=[];runs=[]
    for y,n in zip(labels,units):
        start=len(vals);vals.extend([y]*(2*n+1));runs.append(list(range(start,len(vals))))
    L=len(runs[0]);h=rng.randrange(L-1);q=rng.randrange(L-1-h);r=L-2-h-q
    first=q;second=q+1;last=second+h
    mid=runs[0][second+1:last+1];suffix=runs[0][last+1:];prefix=runs[0][:first]
    if (len(mid),len(suffix),len(prefix))!=(h,r,q):raise ValueError('segment lengths')
    u=rng.randrange(p);v=rng.randrange(p);t=(u-v)%p;c=labels[0]
    mp,mrep=split(mid);sp,srep=split(suffix);qp,qrep=split(prefix)
    otherpairs=[];otherreps=[]
    for run in runs[1:]:
        a,b=split(run);otherpairs.extend(a);otherreps.append(b)
    pairs=mp+sp+otherpairs+qp;chosen_reps=[]
    if h%2==0:
        odd_reps=([srep] if srep is not None else [])+otherreps+([qrep] if qrep is not None else [])
        if len(pairs)!=p-2 or len(odd_reps)!=p:raise ValueError('even-mid profile')
        branch='h-even'
        if t:
            chosen_reps=next(([i,j] for i,j in itertools.combinations(odd_reps,2)
                              if (vals[i]-vals[j])%p==t),None)
            if chosen_reps is None:raise ValueError('full directed difference')
            pairs=pairs[:-1]
    elif r%2==1 and q%2==1:
        if len(pairs)!=p-3:raise ValueError('three-odd profile')
        branch='h-odd-two-outside-odd'
        if t:
            y=(c-t)%p
            chosen_reps=[srep,next(x for x in otherreps if vals[x]==y)]
        else:chosen_reps=[srep,qrep]
    elif r+q:
        if len(pairs)!=p-2 or r%2 or q%2:raise ValueError('even-outside profile')
        branch='h-odd-outside-even-nonempty'
        if t:
            if r:
                lost=sp[0];c_rep=lost[0];y=(c-t)%p
                chosen_reps=[c_rep,next(x for x in otherreps if vals[x]==y)]
            else:
                lost=qp[-1];c_rep=lost[-1];y=(c+t)%p
                chosen_reps=[next(x for x in otherreps if vals[x]==y),c_rep]
            pairs.remove(lost)
    else:
        if len(pairs)!=p-2 or mrep is None:raise ValueError('inside-only profile')
        branch='h-odd-no-outside'
        if t and (u+v)%p:
            y=(c-u-v)%p
            chosen_reps=[mrep,next(x for x in otherreps if vals[x]==y)]
            pairs=pairs[:-1]
        elif t:
            chosen_reps=next(([i,j] for i,j in itertools.combinations(otherreps,2)
                              if (vals[i]-vals[j])%p==t),None)
            if chosen_reps is None:return None
            pairs=pairs[:-1]
    chosen=[first,second]+[i for pair in pairs for i in pair]+chosen_reps
    if len(chosen)!=2*p-2 or len(set(chosen))!=len(chosen):raise ValueError('chosen size')
    forbidden=set(range(second,last));gaps={first,last}
    allowed=[i for i in range(len(vals)) if i not in gaps and i not in forbidden]
    gaps.update(rng.sample(allowed,p-1))
    word=[];refs=[];rot_by_gap={}
    for i,y in enumerate(vals):
        refs.append(len(word));word.append([y,1])
        if i in gaps:
            rot_by_gap[i]=len(word);value=u if i==first else v if i==last else rng.randrange(1,p)
            word.append([value,0])
    selected=[refs[i] for i in chosen]+[rot_by_gap[first],rot_by_gap[last]]
    cut=rng.choice(refs);N=len(word);actual=word[cut:]+word[:cut]
    selector=sorted((i-cut)%N for i in selected)
    segment=[(refs[first]-cut)%N,(rot_by_gap[first]-cut)%N,(refs[second]-cut)%N,(rot_by_gap[last]-cut)%N]
    if N!=4*p-1 or len(selector)!=2*p or product(actual,selector,p)!=(0,0):raise ValueError('product')
    return {'p':p,'word':actual,'selector':selector,'actual_segment':segment,'h':h,'r':r,'q':q,
            'u':u,'v':v,'target':t,'branch':branch}


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--output',required=True);args=parser.parse_args()
    rng=random.Random(SEED);cases=[];excluded=0
    for p in (3,5,7,11,13):
        while sum(c['p']==p for c in cases)<200:
            c=make(rng,p)
            if c is None:excluded+=1
            else:cases.append(c)
    with open(args.output,'x',encoding='utf-8') as out:
        json.dump({'seed':SEED,'excluded_exceptional_draws':excluded,'cases':cases},out,sort_keys=True,separators=(',',':'));out.write('\n')
    print(json.dumps({'result':'PASS_STRETCHED_FOURBLOCK','actual_words':len(cases),
                      'exceptional_draws_excluded':excluded},sort_keys=True))


if __name__=='__main__':
    main()
