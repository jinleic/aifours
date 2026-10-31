#!/usr/bin/env python3
"""Targeted branch coverage for the o_pi=p+2 constructions.

Reuses construct() from frontier-20261028-olson-p2-band-experiment.py (same
producer family; the independent checker is separate) and generates
triple-multiset words with one occupied gap per projected run (sector Case
A/B with loss 0,1,2) plus stretched odd-run words with u=v (H-iva-gamma).
"""
import argparse
import importlib.util
import json
import os
import random

SEED=2026102840
HERE=os.path.dirname(os.path.abspath(__file__))
spec=importlib.util.spec_from_file_location('p2band',os.path.join(HERE,'frontier-20261028-olson-p2-band-experiment.py'))
P2=importlib.util.module_from_spec(spec);spec.loader.exec_module(P2)


def odd_labels(rng,p):
    if rng.random()<0.5:
        c=rng.randrange(p);d=rng.randrange(1,p);return [c,c,c]+[(c+k*d)%p for k in range(1,p)]
    while True:
        c=rng.randrange(p);odd=[c,c,c]+[x for x in range(p) if x!=c];rng.shuffle(odd)
        if P2.zero_quadruple(odd,p) is None:return odd


def layout(rng,p,odd,min_even=0):
    m=len(odd);mand=[i for i in range(m) if odd[i]==odd[(i+1)%m]];units=p-2
    lo=max(len(mand),min_even)
    if lo>units:return None
    e=rng.randrange(lo,units+1);slots=mand+[rng.randrange(m) for _ in range(e-len(mand))]
    runs=[]
    for i,l in enumerate(odd):
        runs.append([l,1,True])
        for _ in range(slots.count(i)):runs.append([None,2,False])
    n=len(runs)
    for i in range(n):
        if runs[i][0] is None:runs[i][0]=rng.choice([x for x in range(p) if x!=runs[i-1][0]])
    if any(runs[i][0]==runs[(i+1)%n][0] for i in range(n)):return None
    for _ in range((3*p-2-sum(r[1] for r in runs))//2):runs[rng.randrange(n)][1]+=2
    return runs


def sector_word(rng,p):
    runs=layout(rng,p,odd_labels(rng,p),min_even=2)
    if runs is None or len(runs)<p+1:return None
    active=rng.sample(range(len(runs)),p+1);gapidx=set();pos=0
    for t,(l,L,isodd) in enumerate(runs):
        if t in active:
            if not isodd and rng.random()<0.8:k=rng.choice([j for j in range(1,L+1) if j%2])
            else:k=rng.randrange(1,L+1)
            gapidx.add(pos+k-1)
        pos+=L
    vals=[l for l,L,_ in runs for _ in range(L)];w=[]
    for i,y in enumerate(vals):
        w.append([y,1])
        if i in gapidx:w.append([rng.randrange(1,p),0])
    cut=rng.randrange(len(w));return w[cut:]+w[:cut]


def gamma_word(rng,p):
    c=rng.randrange(p);d=rng.randrange(1,p);odd=[c,c,c]+[(c+k*d)%p for k in range(1,p)]
    runs=layout(rng,p,odd)
    if runs is None:return None
    cand=[t for t,(l,L,isodd) in enumerate(runs) if isodd and l!=c]
    t=rng.choice(cand)
    need=5-runs[t][1]
    if need>0:
        donors=[j for j,(l,L,isodd) in enumerate(runs) if j!=t and L>=(3 if isodd else 4)]
        while need>0:
            if not donors:return None
            j=rng.choice(donors);runs[j][1]-=2;runs[t][1]+=2;need-=2
            donors=[j for j,(l,L,isodd) in enumerate(runs) if j!=t and L>=(3 if isodd else 4)]
    L=runs[t][1];a=2*rng.randrange(1,(L-1)//2+1)
    while True:
        x=2*rng.randrange(0,(L-a-1)//2+1)+1
        if a+x<=L and (L-a-x)%2==0:break
    start=sum(r[1] for r in runs[:t]);g1=start+a-1;g2=start+a+x-1
    vals=[l for l,L2,_ in runs for _ in range(L2)];F=len(vals)
    others=[j for j in range(len(runs)) if j!=t]
    if len(others)<p-1:return None
    chosen=rng.sample(others,p-1);rest=[]
    for j in chosen:
        s0=sum(r[1] for r in runs[:j]);rest.append(s0+rng.randrange(runs[j][1]))
    gaps={g1,g2}|set(rest);u=rng.randrange(1,p);w=[]
    for i,y in enumerate(vals):
        w.append([y,1])
        if i in gaps:w.append([u if i in (g1,g2) else rng.randrange(1,p),0])
    cut=rng.randrange(len(w));return w[cut:]+w[:cut]


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--output',required=True);args=parser.parse_args()
    rng=random.Random(SEED);cases=[];branches={};draws=0
    quota={'A/L0':40,'A/L1':40,'A/L2':40,'B/L0':40,'B/L1':40,'B/L2':40}
    for p in (5,7,11,13):
        got={k:0 for k in quota};tries=0
        while any(got[k]<quota[k]//4 for k in quota) and tries<60000:
            tries+=1;w=sector_word(rng,p)
            if w is None:continue
            sel,case=P2.construct(w,p)
            if case in got and got[case]<quota[case]//4:
                got[case]+=1;cases.append({'p':p,'word':w,'selector':sel,'case':case,'mode':'sector'})
                branches[case]=branches.get(case,0)+1
        draws+=tries
        g=0
        while g<25:
            w=gamma_word(rng,p)
            if w is None:continue
            sel,case=P2.construct(w,p)
            if case!='H-iva-gamma':raise ValueError('gamma generator produced '+case)
            cases.append({'p':p,'word':w,'selector':sel,'case':case,'mode':'gamma'});g+=1
            branches[case]=branches.get(case,0)+1
    with open(args.output,'x',encoding='utf-8') as out:
        json.dump({'seed':SEED,'sector_draws':draws,'cases':cases},out,sort_keys=True,separators=(',',':'));out.write('\n')
    print(json.dumps({'result':'PASS_P2_BAND_TARGETED','actual_words':len(cases),'branches':dict(sorted(branches.items())),
                      'sector_draws':draws},sort_keys=True))


if __name__=='__main__':
    main()
