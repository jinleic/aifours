#!/usr/bin/env python3
"""Direct reflection-only witnesses for repeated odd projected labels."""
import argparse
import json
import random

SEED=2026102832


def product(w,idx,p):
    x,e=0,0
    for i in idx:
        y,b=w[i];x=(x+(-y if e else y))%p;e^=b
    return x,e


def make(rng,p):
    while True:
        labels=[rng.randrange(p) for _ in range(p)]
        if all(labels[i]!=labels[(i+1)%p] for i in range(p)) and len(set(labels))<p:break
    units=[0]*p
    for _ in range(p-1):units[rng.randrange(p)]+=1
    vals=[];runs=[]
    for label,n in zip(labels,units):
        start=len(vals);vals.extend([label]*(2*n+1));runs.append(list(range(start,len(vals))))
    i,j=next((i,j) for i in range(p) for j in range(i+1,p) if labels[i]==labels[j])
    chosen=[]
    for run in runs:
        chosen.extend(z for n in range(0,len(run)-1,2) for z in (run[n],run[n+1]))
    chosen.extend((runs[i][-1],runs[j][-1]))
    gaps=set(rng.sample(range(len(vals)),p+1));word=[];refs=[]
    for q,y in enumerate(vals):
        refs.append(len(word));word.append([y,1])
        if q in gaps:word.append([rng.randrange(1,p),0])
    cut=rng.choice(refs);N=len(word);actual=word[cut:]+word[:cut]
    selector=sorted((refs[q]-cut)%N for q in chosen)
    if len(selector)!=2*p or product(actual,selector,p)!=(0,0):raise ValueError('product')
    return {'p':p,'word':actual,'selector':selector}


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--output',required=True);args=parser.parse_args()
    rng=random.Random(SEED);cases=[make(rng,p) for p in (5,7,11,13) for _ in range(100)]
    with open(args.output,'x',encoding='utf-8') as out:
        json.dump({'seed':SEED,'cases':cases},out,sort_keys=True,separators=(',',':'));out.write('\n')
    print(json.dumps({'result':'PASS_REPEATED_ODD_PROJECTION','actual_words':len(cases)},sort_keys=True))


if __name__=='__main__':
    main()
