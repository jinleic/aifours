#!/usr/bin/env python3
"""Two rotations in one spare gap, at most one even-run pair loss."""
import argparse
import itertools
import json
import random

SEED=2026102834


def product(w,idx,p):
    x,e=0,0
    for i in idx:
        y,b=w[i];x=(x+(-y if e else y))%p;e^=b
    return x,e


def paired(seg):
    return [(seg[i],seg[i+1]) for i in range(0,len(seg)-1,2)],(seg[-1] if len(seg)%2 else None)


def make(rng,p):
    odd=list(range(p));rng.shuffle(odd);k=rng.randrange(1,p)
    c=rng.choice([x for x in range(p) if x!=odd[k-1] and x!=odd[k]])
    labels=odd[:k]+[c]+odd[k:];units=[0]*(p+1);units[k]=rng.randrange(1,p)
    for _ in range(p-1-units[k]):units[rng.choice([i for i in range(p+1) if i!=k])]+=1
    vals=[];runs=[]
    for j,(y,n) in enumerate(zip(labels,units)):
        start=len(vals);vals.extend([y]*(2*n+(j!=k)));runs.append(list(range(start,len(vals))))
    gap_for_run=[rng.choice(run) for run in runs];word=[];refs=[];rotation_by_gap={}
    for i,y in enumerate(vals):
        refs.append(len(word));word.append([y,1])
        if i in gap_for_run:
            rotation_by_gap[i]=len(word);word.append([rng.randrange(1,p),0])
    N=len(word);odd_pairs=[];odd_spares=[]
    for j,run in enumerate(runs):
        if j==k:continue
        split_index=run.index(gap_for_run[j])+1
        pa,a=paired(run[:split_index]);pb,b=paired(run[split_index:])
        odd_pairs+=pa+pb
        spare=a if a is not None else b
        if spare is None or (a is not None and b is not None):raise ValueError('odd spare')
        odd_spares.append(spare)
    cyclic=sorted(refs[i] for i in odd_spares);rotations=sorted(rotation_by_gap.values())
    chosen_rot=None
    for index,a in enumerate(cyclic):
        end=cyclic[(index+1)%len(cyclic)];distance=(end-a)%N
        sector=sorted((x for x in rotations if 0<(x-a)%N<distance),key=lambda x:(x-a)%N)
        if len(sector)>=2:chosen_rot=sector[:2];break
    if chosen_rot is None:raise ValueError('spare pigeonhole')
    r1,r2=chosen_rot;evgap=gap_for_run[k];evrot=rotation_by_gap[evgap]
    selected_even=evrot in chosen_rot;evrun=runs[k]
    epos=evrun.index(evgap)+1
    ep,ea=paired(evrun[:epos]);eq,eb=paired(evrun[epos:])
    lost=int(selected_even and ea is not None and eb is not None)
    if lost:
        pairs=odd_pairs+ep+eq
    else:
        evpairs,_=paired(evrun);pairs=odd_pairs+evpairs
    if len(pairs)!=p-1-lost:raise ValueError('pair capacity')
    order=lambda idx:(idx-r2)%N
    reps=sorted(odd_spares,key=lambda i:order(refs[i]))
    if not all(0<order(refs[i])<(r1-r2)%N for i in reps):raise ValueError('odd spares not after second')
    s=(word[r1][0]+word[r2][0])%p;active=[]
    if s:
        active=next(([i,j] for i,j in itertools.combinations(reps,2) if (vals[i]-vals[j])%p==(-s)%p),None)
        if active is None:raise ValueError('difference')
        if not lost:pairs=pairs[:-1]
    elif lost:
        outside=[x for x in (ea,eb) if 0<order(refs[x])<(r1-r2)%N]
        if not outside:raise ValueError('outside c spare')
        active=[outside[0],next(i for i in odd_spares if vals[i]==c)]
    chosen=[refs[i] for pair in pairs for i in pair]+[refs[i] for i in active]+chosen_rot
    cut=rng.choice(refs);original=word[cut:]+word[:cut]
    selector=sorted((i-cut)%N for i in chosen)
    markers={'rotations':[(i-cut)%N for i in chosen_rot],
             'odd_spares':[(refs[i]-cut)%N for i in odd_spares],
             'even_rotation':(evrot-cut)%N,'pair_loss':lost,'rotation_sum':s}
    if len(selector)!=2*p or product(original,selector,p)!=(0,0):raise ValueError('actual selector')
    return {'p':p,'word':original,'selector':selector,'markers':markers}


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--output',required=True);args=parser.parse_args()
    rng=random.Random(SEED);cases=[make(rng,p) for p in (3,5,7,11,13) for _ in range(200)]
    with open(args.output,'x',encoding='utf-8') as out:
        json.dump({'seed':SEED,'cases':cases},out,sort_keys=True,separators=(',',':'));out.write('\n')
    print(json.dumps({'result':'PASS_ONE_EVEN_ONE_GAP','actual_words':len(cases),
                      'selected_even_pair_loss':sum(c['markers']['pair_loss'] for c in cases)},sort_keys=True))


if __name__=='__main__':
    main()
