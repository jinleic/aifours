#!/usr/bin/env python3
"""Targeted words where both selected rotations split even runs oddly."""
import argparse
import itertools
import json
import random

SEED=2026102837


def product(w,idx,p):
    x,e=0,0
    for i in idx:
        y,b=w[i];x=(x+(-y if e else y))%p;e^=b
    return x,e


def paired(seg):
    return [(seg[i],seg[i+1]) for i in range(0,len(seg)-1,2)],(seg[-1] if len(seg)%2 else None)


def make(rng,p,branch):
    odd=list(range(p));rng.shuffle(odd);j0=rng.randrange(p)
    left,right=odd[j0],odd[(j0+1)%p]
    if branch=='L2/II/s=0':
        alpha=rng.choice([x for x in range(p) if x!=left and x!=right]);beta=alpha
        gamma=rng.choice([x for x in range(p) if x!=alpha]);block=[alpha,gamma,beta]
    else:
        alpha=rng.choice([x for x in range(p) if x!=left])
        beta=rng.choice([x for x in range(p) if x!=alpha and x!=right]);block=[alpha,beta]
    labels=odd[:j0+1]+block+odd[j0+1:];iseven=[False]*(j0+1)+[True]*len(block)+[False]*(p-j0-1)
    A=j0+1;B=j0+len(block)
    units=[int(b) for b in iseven];extra=p-1-sum(units)
    if extra<0:return None
    for _ in range(extra):units[rng.randrange(len(units))]+=1
    vals=[];runs=[]
    for y,n,b in zip(labels,units,iseven):
        start=len(vals);vals.extend([y]*(2*n+(not b)));runs.append(list(range(start,len(vals))))
    if len(vals)!=3*p-2:raise ValueError('F')
    others=[j for j in range(len(runs)) if j not in (A,B)]
    active=[A,B]+rng.sample(others,p-1);gap={}
    for j in active:
        L=len(runs[j])
        k=rng.choice([x for x in range(1,L+1) if x%2==1]) if j in (A,B) else rng.randrange(1,L+1)
        gap[j]=runs[j][k-1]
    if branch=='L2/I':
        while True:
            u,v=rng.randrange(p),rng.randrange(p)
            if (beta-alpha+u+v)%p:break
    elif branch=='L2/II/s!=0':
        u=rng.randrange(p);v=(alpha-beta-u)%p
    else:
        u=rng.randrange(p);v=(-u)%p
    word=[];refs=[];rot={}
    for i,y in enumerate(vals):
        refs.append(len(word));word.append([y,1])
        if i in gap.values():
            value=u if i==gap[A] else v if i==gap[B] else rng.randrange(p)
            rot[i]=len(word);word.append([value,0])
    N=len(word);r1,r2=rot[gap[A]],rot[gap[B]]
    pairs=[];spare={}
    for j,run in enumerate(runs):
        if j in gap and (j in (A,B) or not iseven[j]):
            k=run.index(gap[j])+1;pa,a=paired(run[:k]);pb,b=paired(run[k:]);pairs+=pa+pb
            if not iseven[j]:spare[j]=a if a is not None else b
            elif j==A:a1,a2=a,b
            else:b1,b2=a,b
        else:
            pa,a=paired(run);pairs+=pa
            if not iseven[j]:spare[j]=a
    if len(pairs)!=p-3:raise ValueError('capacity')
    pos=lambda i:(refs[i]-r1)%N;D=(r2-r1)%N
    reps=sorted(spare.values(),key=pos)
    if any(pos(i)<D for i in reps) or not (pos(a2)<D and pos(b1)<D and pos(b2)>D and pos(a1)>D):
        raise ValueError('sector or sides')
    s=(u+v)%p
    def diff(t):
        return next([i,j] for i,j in itertools.combinations(reps,2) if (vals[i]-vals[j])%p==t%p)
    if branch=='L2/I':chosen=[b2]+diff(beta-alpha+s)+[a1]
    elif branch=='L2/II/s!=0':
        if not s:return None
        chosen=[a2,b1]+diff(-2*s)
    else:chosen=[a2,b1,b2,a1]
    selected=[refs[i] for pr in pairs for i in pr]+[refs[i] for i in chosen]+[r1,r2]
    if len(selected)!=2*p or len(set(selected))!=2*p:raise ValueError('size')
    cut=rng.randrange(N);original=word[cut:]+word[:cut]
    selector=sorted((i-cut)%N for i in selected)
    if product(original,selector,p)!=(0,0):raise ValueError('product '+branch)
    return {'p':p,'word':original,'selector':selector,'rotations':[(r1-cut)%N,(r2-cut)%N],
            'branch':branch,'loss':2}


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--output',required=True);args=parser.parse_args()
    rng=random.Random(SEED);cases=[];skipped=0
    for p in (3,5,7,11,13):
        for branch in ('L2/I','L2/II/s!=0','L2/II/s=0'):
            if branch=='L2/II/s=0' and p==3:continue
            got=0
            while got<60:
                c=make(rng,p,branch)
                if c is None:skipped+=1;continue
                cases.append(c);got+=1
    with open(args.output,'x',encoding='utf-8') as out:
        json.dump({'seed':SEED,'skipped_generation_draws':skipped,'cases':cases},out,sort_keys=True,separators=(',',':'));out.write('\n')
    counts={}
    for c in cases:counts[c['branch']]=counts.get(c['branch'],0)+1
    print(json.dumps({'result':'PASS_SPARE_SECTOR_LOSS2','actual_words':len(cases),'branches':counts,
                      'skipped_generation_draws':skipped},sort_keys=True))


if __name__=='__main__':
    main()
