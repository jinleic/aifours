#!/usr/bin/env python3
"""Finite checks for the o_pi=p+2 REF-failure structure.

Part 1 (exhaustive, p=3,5): cyclic sequences of length p+2 over F_p (first
entry normalised to 0) with NO cyclic zero alternating quadruple; record them
and test membership in the class c,c,c,c+d,...,c+(p-1)d up to rotation.
Part 2 (sampled, p=5,7,11): reflection-only projections with odd-run labels
c,c,c,AP and random even runs; keep REF-failing ones (exact DP) and record
the even-run labels between the three c-runs.
"""
import argparse
import itertools
import json
import random

SEED=2026102838


def zero_quadruple(seq,p):
    m=len(seq)
    for a,b,c,d in itertools.combinations(range(m),4):
        if (seq[a]-seq[b]+seq[c]-seq[d])%p==0:return True
    return False


def in_class(seq,p):
    m=len(seq)
    for s in range(m):
        lin=seq[s:]+seq[:s]
        c=lin[0];d=(lin[3]-c)%p
        if d and lin[:3]==[c,c,c] and all(lin[3+k]==(c+(k+1)*d)%p for k in range(p-1)):return True
    return False


def ref_exists(vals,p):
    states={(0,0)}
    for k,y in enumerate(vals):
        new=set(states)
        for c,x in states:
            if c<2*p:new.add((c+1,(x+(y if c%2==0 else -y))%p))
        states=new
    return (2*p,0) in states


def sample_projection(rng,p):
    odd=[0,0,0]+list(range(1,p));m=len(odd);units=p-2
    e=rng.randrange(2,units+1);slots=[0,1]+[rng.randrange(m) for _ in range(e-2)]
    runs=[]
    for i,l in enumerate(odd):
        runs.append([l,1])
        for _ in range(slots.count(i)):runs.append([None,2])
    n=len(runs)
    for i in range(n):
        if runs[i][0] is None:runs[i][0]=rng.choice([x for x in range(p) if x!=runs[i-1][0]])
    if any(runs[i][0]==runs[(i+1)%n][0] for i in range(n)):return None
    for _ in range((3*p-2-sum(r[1] for r in runs))//2):runs[rng.randrange(n)][1]+=2
    return [tuple(r) for r in runs]


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--output',required=True);args=parser.parse_args()
    part1={}
    for p in (3,5):
        bad=[]
        for rest in itertools.product(range(p),repeat=p+1):
            seq=[0]+list(rest)
            if not zero_quadruple(seq,p):bad.append(seq)
        part1[str(p)]={'no_zero_quadruple':len(bad),'all_in_class':all(in_class(s,p) for s in bad),'sequences':bad}
    rng=random.Random(SEED);part2={}
    for p in (5,7,11):
        found=[];draws=0
        while len(found)<(40 if p<11 else 20) and draws<400000:
            draws+=1;s=sample_projection(rng,p)
            if s is None:continue
            vals=[l for l,L in s for _ in range(L)]
            if not ref_exists(vals,p):found.append(s)
        part2[str(p)]={'draws':draws,'ref_failing':found}
    with open(args.output,'x',encoding='utf-8') as out:
        json.dump({'seed':SEED,'part1':part1,'part2':part2},out,sort_keys=True,separators=(',',':'));out.write('\n')
    print(json.dumps({'result':'DONE','part1':{k:(v['no_zero_quadruple'],v['all_in_class']) for k,v in part1.items()},
                      'part2':{k:len(v['ref_failing']) for k,v in part2.items()}},sort_keys=True))


if __name__=='__main__':
    main()
