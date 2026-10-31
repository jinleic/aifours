#!/usr/bin/env python3
"""Spare-sector selectors for o_pi=p, distinct odd labels, one gap per run.

Covers selected even-run pair loss 0, 1 and 2.  Every selector is mapped
back to an arbitrary linear cut of the actual word and multiplied directly.
"""
import argparse
import itertools
import json
import random

SEED=2026102836


def product(w,idx,p):
    x,e=0,0
    for i in idx:
        y,b=w[i];x=(x+(-y if e else y))%p;e^=b
    return x,e


def paired(seg):
    return [(seg[i],seg[i+1]) for i in range(0,len(seg)-1,2)],(seg[-1] if len(seg)%2 else None)


def make(rng,p,want_loss):
    e=rng.randrange(max(1,want_loss),max(1,want_loss)+3)
    odd=list(range(p));rng.shuffle(odd)
    slots=sorted(rng.choices(range(p),k=e));labels=[];iseven=[]
    for j in range(p):
        labels.append(odd[j]);iseven.append(False)
        for _ in range(slots.count(j)):
            labels.append(None);iseven.append(True)
    R=len(labels)
    for j in range(R):
        if iseven[j]:
            left=labels[j-1];right=next(labels[(j+k)%R] for k in range(1,R) if not iseven[(j+k)%R])
            labels[j]=rng.choice([x for x in range(p) if x!=left and x!=right])
    units=[int(b) for b in iseven];spare_units=p-1-sum(units)
    if spare_units<0:return None
    for _ in range(spare_units):units[rng.randrange(R)]+=1
    vals=[];runs=[]
    for y,n,b in zip(labels,units,iseven):
        start=len(vals);vals.extend([y]*(2*n+(not b)));runs.append(list(range(start,len(vals))))
    F=len(vals)
    if F!=3*p-2 or any(vals[i]==vals[(i+1)%F] and next(j for j,r in enumerate(runs) if i in r)!=next(j for j,r in enumerate(runs) if (i+1)%F in r) for i in range(F)):
        return None
    if R<p+1:return None
    active=rng.sample(range(R),p+1);gap={}
    evens=[j for j in active if iseven[j]]
    for j in active:
        L=len(runs[j])
        if iseven[j] and want_loss and j in evens[:want_loss]:
            k=rng.choice([x for x in range(1,L+1) if x%2==1])
        else:
            k=rng.randrange(1,L+1)
        gap[j]=runs[j][k-1]
    word=[];refs=[];rot={}
    for i,y in enumerate(vals):
        refs.append(len(word));word.append([y,1])
        if i in gap.values():
            rot[i]=len(word);word.append([rng.randrange(p),0])
    N=len(word)
    pairs_base={};spare={}
    for j,run in enumerate(runs):
        if iseven[j]:continue
        k=run.index(gap[j])+1 if j in gap else len(run)
        pa,a=paired(run[:k]);pb,b=paired(run[k:]);pairs_base[j]=pa+pb
        spare[j]=a if a is not None else b
    spares=sorted(refs[i] for i in spare.values())
    rotations=sorted(rot.values());options=[]
    for index,a in enumerate(spares):
        end=spares[(index+1)%p];dist=(end-a)%N or N
        sector=sorted((x for x in rotations if 0<(x-a)%N<dist),key=lambda x:(x-a)%N)
        if len(sector)>=2:options.append(sector[:2])
    if not options:raise ValueError('pigeonhole failed')
    gap_run={rot[g]:j for j,g in gap.items()}
    def loss_of(pair):
        return sum(iseven[gap_run[r]] and (runs[gap_run[r]].index(gap[gap_run[r]])+1)%2==1 for r in pair)
    preferred=[o for o in options if loss_of(o)==want_loss]
    r1,r2=rng.choice(preferred) if preferred else rng.choice(options)
    G1,G2=gap_run[r1],gap_run[r2]
    if G1==G2:raise ValueError('same run')
    pairs=[];extra={}
    for j,run in enumerate(runs):
        if not iseven[j]:pairs+=pairs_base[j];continue
        if j in (G1,G2) and (run.index(gap[j])+1)%2==1:
            k=run.index(gap[j])+1;pa,a=paired(run[:k]);pb,b=paired(run[k:])
            pairs+=pa+pb;extra[j]=(a,b)
        else:
            pa,_=paired(run);pairs+=pa
    lam=len(extra)
    if len(pairs)!=p-1-lam:raise ValueError('capacity')
    pos=lambda i:(refs[i]-r1)%N
    D=(r2-r1)%N
    oddreps=sorted(spare.values(),key=pos)
    if any(pos(i)<D for i in oddreps):raise ValueError('spare between')
    u,v=word[r1][0],word[r2][0];s=(u+v)%p;chosen=[];branch=None
    def diff(target):
        return next([i,j] for i,j in itertools.combinations(oddreps,2) if (vals[i]-vals[j])%p==target%p)
    if lam==0:
        if s:chosen=diff(-s);pairs=pairs[:-1];branch='L0/s!=0'
        else:branch='L0/s=0'
    elif lam==1:
        j=next(iter(extra));a,b=extra[j]
        out=[x for x in (a,b) if pos(x)>D]
        if len(out)!=1:raise ValueError('outside extra')
        if s:chosen=diff(-s);branch='L1/s!=0'
        else:chosen=[out[0],next(i for i in oddreps if vals[i]==vals[out[0]])];branch='L1/s=0'
    else:
        a1,a2=extra[G1];b1,b2=extra[G2]
        alpha,beta=vals[a1],vals[b1]
        if not (pos(a2)<D and pos(b1)<D and pos(b2)>D and pos(a1)>D):raise ValueError('extra sides')
        if (beta-alpha+s)%p:
            o=diff(beta-alpha+s);chosen=[b2]+o+[a1];branch='L2/I'
        elif s:
            o=diff(-2*s);chosen=[a2,b1]+o;branch='L2/II/s!=0'
        else:
            chosen=[a2,b1,b2,a1];branch='L2/II/s=0'
    selected=[refs[i] for pr in pairs for i in pr]+[refs[i] for i in chosen]+[r1,r2]
    if len(selected)!=2*p or len(set(selected))!=2*p:raise ValueError('size')
    cut=rng.randrange(N);original=word[cut:]+word[:cut]
    selector=sorted((i-cut)%N for i in selected)
    if product(original,selector,p)!=(0,0):raise ValueError('product failure '+branch)
    return {'p':p,'word':original,'selector':selector,'rotations':[(r1-cut)%N,(r2-cut)%N],
            'branch':branch,'loss':lam,'even_runs':e}


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--output',required=True);args=parser.parse_args()
    rng=random.Random(SEED);cases=[];skipped=0
    for p in (3,5,7,11,13):
        for want in (0,1,2):
            got=0
            while got<100:
                c=make(rng,p,want)
                if c is None:skipped+=1;continue
                cases.append(c);got+=1
    branches={}
    for c in cases:branches[c['branch']]=branches.get(c['branch'],0)+1
    with open(args.output,'x',encoding='utf-8') as out:
        json.dump({'seed':SEED,'skipped_generation_draws':skipped,'cases':cases},out,sort_keys=True,separators=(',',':'));out.write('\n')
    print(json.dumps({'result':'PASS_SPARE_SECTOR_FULL','actual_words':len(cases),'branches':branches,
                      'skipped_generation_draws':skipped},sort_keys=True))


if __name__=='__main__':
    main()
