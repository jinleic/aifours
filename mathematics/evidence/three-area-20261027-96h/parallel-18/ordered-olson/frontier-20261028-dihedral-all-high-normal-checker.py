#!/usr/bin/env python3
"""Exact selectors in two structural layouts of the all-high pair class."""
import argparse
from collections import Counter
import itertools
import json
import random

SEED=2026102811


def product(word,indices,p):
    a,b=0,0
    for k in indices:
        x,y=word[k]
        a=(a+(-x if b else x))%p
        b ^= y
    return a,b


def runs(word):
    out=[]
    i=0
    while i<len(word):
        if not word[i][1]:
            i+=1
            continue
        j=i
        while j<len(word) and word[j][1]:
            j+=1
        out.append(list(range(i,j)))
        i=j
    return out


def family(rng,p,kind,trial):
    n=p-3
    L=2*p-1
    A=rng.randrange(p)
    if kind=='one-five':
        word=[[A,1]]*5
        for _ in range(n):
            word += [[p-1,0],[rng.randrange(p),1]]
        word += [[1,0]]*L+[[rng.randrange(p),1]]
    else:
        u=trial%(n+1)
        B=rng.randrange(p)
        word=[[A,1]]*3
        for _ in range(u):
            word += [[p-1,0],[rng.randrange(p),1]]
        word += [[1,0]]*L+[[B,1]]*3
        for _ in range(n-u):
            word += [[p-1,0],[rng.randrange(p),1]]
    return word


def check(word,p,kind):
    refs=[i for i,(_,b) in enumerate(word) if b]
    rot=[i for i,(_,b) in enumerate(word) if not b]
    if len(word)!=4*p-1 or len(refs)!=p+3 or len(rot)!=3*p-4:
        raise ValueError('wrong original type counts')
    first,last=refs[0],refs[-1]
    if any(not first<i<last for i in rot):
        raise ValueError('rotation outside endpoints')
    for i,j in itertools.combinations(refs,2):
        c=Counter((-word[k][0] if i<k<j else word[k][0])%p for k in rot)
        if max(c.values())<2*p-1:
            raise ValueError('a reflection pair is not high-majority')
    nontrivial=[run for run in runs(word) if len(run)>1]
    wanted=[5] if kind=='one-five' else [3,3]
    if sorted(map(len,nontrivial))!=wanted:
        raise ValueError('wrong reflection-run pattern')
    if any(len({word[i][0] for i in run})!=1 for run in nontrivial):
        raise ValueError('nonconstant forced run')
    extra_pairs=[]
    for run in nontrivial:
        available=[i for i in run if i not in (first,last)]
        while len(available)>=2 and len(extra_pairs)<2:
            x,y=available[:2]
            if y!=x+1:
                raise ValueError('extra reflection pair not adjacent')
            extra_pairs.append((x,y))
            available=available[2:]
    if len(extra_pairs)!=2:
        raise ValueError('two pairs excluding endpoints unavailable')
    core=[i for i in rot if word[i][0]==1]
    extras=[i for i in rot if word[i][0]==p-1]
    if len(core)!=2*p-1 or len(extras)!=p-3:
        raise ValueError('wrong signed-core fixture')
    delta=(word[last][0]-word[first][0])%p
    for k in range(3):
        target=(2*(k+1)-delta)%p
        for q in range(p-2):
            if (-2*q)%p!=target:
                continue
            nrot=2*p-2-2*k
            reflections=[first,last]+[i for pair in extra_pairs[:k] for i in pair]
            selector=sorted(reflections+extras[:q]+core[:nrot-q])
            if len(selector)!=2*p or len(set(selector))!=2*p or product(word,selector,p)!=(0,0):
                raise ValueError('actual endpoint-plus-pairs selector failed')
            return k
    raise ValueError('all three distinct targets missed')


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',required=True)
    args=parser.parse_args()
    rng=random.Random(SEED)
    stats=Counter()
    for p in (5,7,11,13):
        for kind in ('one-five','two-threes'):
            for trial in range(30):
                word=family(rng,p,kind,trial)
                k=check(word,p,kind)
                stats[f'{kind}/k{k}']+=1
    result={'result':'PASS_ALL_HIGH_NORMAL_LAYOUTS','seed':SEED,'actual_words_and_selectors':sum(stats.values()),
            'branches':dict(stats),
            'scope':'bounded two structural-layout families; not an all-word proof'}
    with open(args.output,'x',encoding='utf-8') as out:
        json.dump(result,out,sort_keys=True,indent=2)
        out.write('\n')
    print(json.dumps(result,sort_keys=True))


if __name__=='__main__':
    main()
