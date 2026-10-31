#!/usr/bin/env python3
"""Construct odd-run full-support reflection selectors in cyclic full words."""
import argparse
import itertools
import json
import random

SEED=2026102821


def product(word,idx,p):
    x,b=0,0
    for i in idx:
        y,c=word[i]
        x=(x+(-y if b else y))%p
        b^=c
    return x,b


def make(rng,p,trial):
    o=p+2
    for _ in range(10000):
        labels=list(range(p))+[rng.randrange(p),rng.randrange(p)]
        rng.shuffle(labels)
        if all(labels[i]!=labels[(i+1)%o] for i in range(o)):
            break
    else:
        raise ValueError('failed to sample cyclic full-support run labels')
    quad=next((t for t in itertools.combinations(range(o),4)
              if (labels[t[0]]-labels[t[1]]+labels[t[2]]-labels[t[3]])%p==0),None)
    if quad is None:
        raise ValueError('full-support run labels have no zero quadruple')
    units=[0]*o
    for _ in range(p-2):
        units[rng.randrange(o)]+=1
    values=[]
    selected_ord=[]
    for j,y in enumerate(labels):
        start=len(values)
        values += [y]*(2*units[j]+1)
        selected_ord += list(range(start,start+2*units[j]+(1 if j in quad else 0)))
    if len(values)!=3*p-2 or len(selected_ord)!=2*p:
        raise ValueError('wrong run allocation')
    gaps=set(rng.sample(range(len(values)),p+1))
    word=[]
    refs=[]
    for i,y in enumerate(values):
        refs.append(len(word))
        word.append([y,1])
        if i in gaps:
            word.append([rng.randrange(1,p),0])
    chosen=[refs[i] for i in selected_ord]
    cut=rng.choice(refs)
    rotated=word[cut:]+word[:cut]
    selector=sorted((i-cut)%len(word) for i in chosen)
    if len(rotated)!=4*p-1 or len(selector)!=2*p or product(rotated,selector,p)!=(0,0):
        raise ValueError('original-order cyclic restoration failed')
    return {'p':p,'trial':trial,'word':rotated,'selector':selector,'construction_cut':cut,
            'odd_run_labels':labels,'chosen_odd_run_ordinals':quad}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',required=True)
    args=parser.parse_args()
    rng=random.Random(SEED)
    cases=[make(rng,p,trial) for p in (3,5,7,11,13) for trial in range(50)]
    with open(args.output,'x',encoding='utf-8') as out:
        json.dump({'seed':SEED,'cases':cases},out,sort_keys=True,separators=(',',':'))
        out.write('\n')
    print(json.dumps({'result':'PASS_ODD_RUN_FULL_SUPPORT','actual_words_and_selectors':len(cases)},sort_keys=True))


if __name__=='__main__':
    main()
