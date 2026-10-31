#!/usr/bin/env python3
"""Construct cyclic odd-run boundary selectors with zero or one even run."""
import argparse
import itertools
import json
import random

SEED=2026102822


def product(word,idx,p):
    x,b=0,0
    for i in idx:
        y,c=word[i]
        x=(x+(-y if b else y))%p
        b^=c
    return x,b


def make(rng,p,even,force_equal,trial):
    o=p+2
    r=o+even
    for _ in range(10000):
        labels=[rng.randrange(p) for _ in range(r)]
        if force_equal:
            labels[-1]=labels[1]
        if all(labels[i]!=labels[(i+1)%r] for i in range(r)):
            break
    else:
        raise ValueError('failed to sample maximal cyclic run labels')
    even_idx=0 if even else None
    odd_indices=[i for i in range(r) if i!=even_idx]
    odd_labels=[labels[i] for i in odd_indices]
    quad=next((I for I in itertools.combinations(range(o),4)
              if (odd_labels[I[0]]-odd_labels[I[1]]+odd_labels[I[2]]-odd_labels[I[3]])%p==0),None)
    if quad is None:
        raise ValueError('odd-run zero quadruple not found')
    units=[0]*r
    if even:
        units[0]=1
    for _ in range(p-2-even):
        units[rng.randrange(r)]+=1
    values=[]
    selected_ord=[]
    odd_ord=0
    for j,y in enumerate(labels):
        start=len(values)
        length=2*units[j]+(0 if j==even_idx else 1)
        values += [y]*length
        add=0
        if j!=even_idx:
            add=int(odd_ord in quad)
            odd_ord+=1
        selected_ord += list(range(start,start+2*units[j]+add))
    if len(values)!=3*p-2 or len(selected_ord)!=2*p:
        raise ValueError('wrong odd-run allocation')
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
    original=word[cut:]+word[:cut]
    selector=sorted((i-cut)%len(word) for i in chosen)
    if product(original,selector,p)!=(0,0):
        raise ValueError('original cyclic restoration failed')
    return {'p':p,'trial':trial,'even_runs':even,'forced_equal_across_even':force_equal,
            'word':original,'selector':selector,'construction_cut':cut}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',required=True)
    args=parser.parse_args()
    rng=random.Random(SEED)
    cases=[]
    for p in (3,5,7,11,13):
        for even,forced in ((0,False),(1,False),(1,True)):
            for trial in range(40):
                cases.append(make(rng,p,even,forced,trial))
    with open(args.output,'x',encoding='utf-8') as out:
        json.dump({'seed':SEED,'cases':cases},out,sort_keys=True,separators=(',',':'))
        out.write('\n')
    print(json.dumps({'result':'PASS_ODD_RUN_BOUNDARY','actual_words':len(cases)},sort_keys=True))


if __name__=='__main__':
    main()
