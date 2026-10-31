#!/usr/bin/env python3
"""Select two same-spare-gap rotations with at most one even split loss."""
import argparse
import itertools
import json
import random

SEED=2026102835


def product(w,idx,p):
    x,e=0,0
    for i in idx:
        y,b=w[i];x=(x+(-y if e else y))%p;e^=b
    return x,e


def paired(seg):
    return [(seg[i],seg[i+1]) for i in range(0,len(seg)-1,2)],(seg[-1] if len(seg)%2 else None)


def make(rng,p):
    e=rng.randrange(1,min(3,p-2)+1);odd=list(range(p));rng.shuffle(odd)
    insertion=set(rng.sample(range(p),e));labels=[];iseven=[]
    for j in range(p):
        labels.append(odd[j]);iseven.append(False)
        if j in insertion:
            labels.append(rng.choice([x for x in range(p) if x!=odd[j] and x!=odd[(j+1)%p]]));iseven.append(True)
    units=[int(b) for b in iseven]
    for _ in range(p-1-e):units[rng.randrange(len(units))]+=1
    vals=[];runs=[]
    for y,n,b in zip(labels,units,iseven):
        start=len(vals);vals.extend([y]*(2*n+(not b)));runs.append(list(range(start,len(vals))))
    active=set(rng.sample(range(len(runs)),p+1));gap={j:rng.choice(runs[j]) for j in active}
    lossy=[j for j in active if iseven[j] and (runs[j].index(gap[j])+1)%2==1]
    if len(lossy)>1:return None
    word=[];refs=[];rot={}
    for i,y in enumerate(vals):
        refs.append(len(word));word.append([y,1])
        if i in gap.values():rot[i]=len(word);word.append([rng.randrange(1,p),0])
    N=len(word);oddpairs=[];spares=[]
    for j,run in enumerate(runs):
        if iseven[j]:continue
        k=run.index(gap[j])+1 if j in gap else len(run)
        pa,a=paired(run[:k]);pb,b=paired(run[k:]);oddpairs+=pa+pb
        spare=a if a is not None else b
        if spare is None or (a is not None and b is not None):raise ValueError('odd spare')
        spares.append(spare)
    cyc=sorted(refs[i] for i in spares);rotations=sorted(rot.values());chosen_rot=None
    for index,a in enumerate(cyc):
        end=cyc[(index+1)%len(cyc)];distance=(end-a)%N
        sector=sorted((x for x in rotations if 0<(x-a)%N<distance),key=lambda x:(x-a)%N)
        if len(sector)>=2:chosen_rot=sector[:2];break
    if chosen_rot is None:raise ValueError('spare gap')
    r1,r2=chosen_rot;pairs=oddpairs[:];extra=[];loss=0
    for j,run in enumerate(runs):
        if not iseven[j]:continue
        if j in lossy and rot[gap[j]] in chosen_rot:
            k=run.index(gap[j])+1;pa,a=paired(run[:k]);pb,b=paired(run[k:]);pairs+=pa+pb
            extra=[a,b];loss+=1
        else:
            a,_=paired(run);pairs+=a
    if loss>1 or len(pairs)!=p-1-loss:raise ValueError('pair capacity')
    order=lambda i:(i-r2)%N
    reps=sorted(spares,key=lambda i:order(refs[i]))
    if not all(0<order(refs[i])<(r1-r2)%N for i in reps):raise ValueError('spares after')
    s=(word[r1][0]+word[r2][0])%p;chosen=[]
    if s:
        chosen=next(([i,j] for i,j in itertools.combinations(reps,2) if (vals[i]-vals[j])%p==(-s)%p),None)
        if chosen is None:raise ValueError('directed difference')
        if not loss:pairs=pairs[:-1]
    elif loss:
        outside=[i for i in extra if 0<order(refs[i])<(r1-r2)%N]
        if not outside:raise ValueError('outside spare')
        chosen=[outside[0],next(i for i in reps if vals[i]==vals[outside[0]])]
    selected=[refs[i] for pair in pairs for i in pair]+[refs[i] for i in chosen]+chosen_rot
    cut=rng.choice(refs);original=word[cut:]+word[:cut]
    selector=sorted((i-cut)%N for i in selected)
    marks={'rotations':[(i-cut)%N for i in chosen_rot],'odd_spares':[(refs[i]-cut)%N for i in spares],
           'global_lossy':len(lossy),'selected_pair_loss':loss,'rotation_sum':s,'even_runs':e}
    if len(selector)!=2*p or product(original,selector,p)!=(0,0):raise ValueError('actual product')
    return {'p':p,'word':original,'selector':selector,'markers':marks}


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--output',required=True);args=parser.parse_args()
    rng=random.Random(SEED);cases=[];rejected=0
    for p in (3,5,7,11,13):
        while sum(c['p']==p for c in cases)<200:
            c=make(rng,p)
            if c is None:rejected+=1
            else:cases.append(c)
    with open(args.output,'x',encoding='utf-8') as out:
        json.dump({'seed':SEED,'excluded_more_than_one_lossy':rejected,'cases':cases},out,sort_keys=True,separators=(',',':'));out.write('\n')
    print(json.dumps({'result':'PASS_LOW_LOSS_SPARE_GAP','actual_words':len(cases),
                      'excluded_more_than_one_lossy':rejected},sort_keys=True))


if __name__=='__main__':
    main()
