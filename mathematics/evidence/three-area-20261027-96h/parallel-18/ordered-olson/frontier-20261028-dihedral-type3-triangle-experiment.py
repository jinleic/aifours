#!/usr/bin/env python3
"""Construct actual type-III selectors via a low-M reflection triangle."""
import argparse
import itertools
import json
import random

SEED=2026102813


def product(word,indices,p):
    x,b=0,0
    for k in sorted(indices):
        t,e=word[k]
        x=(x+(-t if b else t))%p
        b^=e
    return x,b


def evaluate(word,p,label):
    refs=[i for i,(_,b) in enumerate(word) if b]
    rot=[i for i,(_,b) in enumerate(word) if not b]
    if len(word)!=4*p-1 or len(refs)!=p+3 or len(rot)!=3*p-4:
        raise ValueError('wrong actual word length/count')
    prefix=0
    Q={}
    for i,(x,b) in enumerate(word):
        if b:
            Q[i]=prefix
        else:
            prefix += 1 if x==1 else -1
    tri=next((t for t in itertools.combinations(refs,3)
              if all(-1<=Q[v]-Q[u]<=p-1 for u,v in itertools.combinations(t,2))),None)
    if tri is None:
        raise ValueError('type-III low triangle not found')
    for i,j in itertools.combinations(tri,2):
        signed={k:(-word[k][0] if i<k<j else word[k][0])%p for k in rot}
        plus=[k for k,v in signed.items() if v==1]
        minus=[k for k,v in signed.items() if v==p-1]
        target=(word[j][0]-word[i][0])%p
        for q in range(2*p-1):
            other=2*p-2-q
            if q<=len(plus) and other<=len(minus) and (q-other)%p==target:
                selector=sorted(plus[:q]+minus[:other]+[i,j])
                if len(selector)!=2*p or product(word,selector,p)!=(0,0):
                    raise ValueError('incorrect original selector')
                return {'p':p,'label':label,'word':word,'prefix_triangle':[Q[x] for x in tri],
                        'triangle_indices':tri,'selected_pair':[i,j],'selector':selector}
    raise ValueError('nonzero triangle cocycle did not force selector')


def saturated_family(rng,p,hleft):
    h=(p-1)//2
    ys=[rng.randrange(p) for _ in range(p+3)]
    at=0
    def doublet():
        nonlocal at
        ans=[[ys[at],1],[ys[at+1],1]]
        at+=2
        return ans
    word=doublet()
    for _ in range(hleft):
        word += [[p-1,0]]*2+doublet()
    word += [[1,0]]*p+doublet()
    for _ in range(h-hleft):
        word += [[p-1,0]]*2+doublet()
    word += [[1,0]]*(p-3)
    return word


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',required=True)
    args=parser.parse_args()
    rng=random.Random(SEED)
    cases=[]
    for p in (3,5,7,11,13):
        for trial in range(80):
            kinds=[0]*(2*p-3)+[1]*(p-1)+[2]*(p+3)
            rng.shuffle(kinds)
            word=[[1,0] if t==0 else [p-1,0] if t==1 else [rng.randrange(p),1] for t in kinds]
            cases.append(evaluate(word,p,{'trial':trial,'kind':'random'}))
    structured=[]
    for p in (3,5,7,11,13):
        for hleft in range((p-1)//2+1):
            for trial in range(10):
                structured.append(evaluate(saturated_family(rng,p,hleft),p,
                                {'kind':'saturated-window','left_blocks':hleft,'trial':trial}))
    with open(args.output,'x',encoding='utf-8') as out:
        json.dump({'seed':SEED,'random_cases':cases,'saturated_cases':structured},out,separators=(',',':'),sort_keys=True)
        out.write('\n')
    print(json.dumps({'result':'PASS_TYPE3_TRIANGLE_SELECTOR','random_words':len(cases),
                      'saturated_words':len(structured)},sort_keys=True))


if __name__=='__main__':
    main()
