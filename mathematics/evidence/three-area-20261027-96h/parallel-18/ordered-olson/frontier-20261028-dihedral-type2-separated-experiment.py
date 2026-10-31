#!/usr/bin/env python3
"""Construct type-II two- or four-reflection original selectors."""
import argparse
import itertools
import json
import random

SEED=2026102814


def product(word,indices,p):
    x,b=0,0
    for i in sorted(indices):
        y,c=word[i]
        x=(x+(-y if b else y))%p
        b^=c
    return x,b


def evaluate(word,p,label):
    refs=[i for i,(_,b) in enumerate(word) if b]
    rotations=[i for i,(_,b) in enumerate(word) if not b]
    if len(word)!=4*p-1 or len(refs)!=p+3 or len(rotations)!=3*p-4:
        raise ValueError('bad original word size')
    Q={}
    q=0
    for i,(x,b) in enumerate(word):
        if b:
            Q[i]=q
        else:
            q+=1 if x==1 else -1
    low=[(i,j) for i,j in itertools.combinations(refs,2) if 0<=Q[j]-Q[i]<=p]
    first=min(low,key=lambda pair:pair[1]) if low else None
    second=next((edge for edge in low if first and edge[0]>first[1]),None)
    if first is None or second is None:
        raise ValueError('two separated low edges not found')
    for i,j in low:
        signed={k:(-word[k][0] if i<k<j else word[k][0])%p for k in rotations}
        plus=[k for k,v in signed.items() if v==1]
        minus=[k for k,v in signed.items() if v==p-1]
        target=(word[j][0]-word[i][0])%p
        for z in range(2*p-1):
            other=2*p-2-z
            if z<=len(plus) and other<=len(minus) and (z-other)%p==target:
                selector=sorted(plus[:z]+minus[:other]+[i,j])
                if product(word,selector,p)!=(0,0):
                    raise ValueError('bad two-reflection selector')
                return {'p':p,'label':label,'word':word,'low_pairs':[first,second],
                        'mode':'two_reflections','selected_pair':[i,j],'selector':selector}
    i,j=first
    k,l=second
    selected_refs=[i,j,k,l]
    values={t:((-word[t][0] if sum(r<t for r in selected_refs)%2 else word[t][0])%p) for t in rotations}
    total=(sum(values.values())+word[i][0]-word[j][0]+word[k][0]-word[l][0])%p
    if total!=0:
        raise ValueError('separated-edge gauge cancellation failed')
    sign=1 if sum(v==1 for v in values.values())>=p else p-1
    omitted=[t for t,v in values.items() if v==sign][:p]
    if len(omitted)!=p:
        raise ValueError('p equal signed omissions unavailable')
    selector=sorted((set(rotations)-set(omitted)) | set(selected_refs))
    if len(selector)!=2*p or product(word,selector,p)!=(0,0):
        raise ValueError('bad four-reflection selector')
    return {'p':p,'label':label,'word':word,'low_pairs':[first,second],
            'mode':'four_reflections','omitted_indices':omitted,'selector':selector}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',required=True)
    args=parser.parse_args()
    rng=random.Random(SEED)
    cases=[]
    for p in (3,5,7,11,13):
        for mode in ('random','gauge'):
            for trial in range(80):
                kinds=[0]*(2*p-2)+[1]*(p-2)+[2]*(p+3)
                rng.shuffle(kinds)
                Q=0
                word=[]
                for t in kinds:
                    if t==0:
                        word.append([1,0])
                        Q+=1
                    elif t==1:
                        word.append([p-1,0])
                        Q-=1
                    else:
                        word.append([rng.randrange(p) if mode=='random' else (-2*Q)%p,1])
                cases.append(evaluate(word,p,{'trial':trial,'generation':mode}))
    with open(args.output,'x',encoding='utf-8') as out:
        json.dump({'seed':SEED,'cases':cases},out,separators=(',',':'),sort_keys=True)
        out.write('\n')
    branches={}
    for c in cases:
        key=c['label']['generation']+'/'+c['mode']
        branches[key]=branches.get(key,0)+1
    print(json.dumps({'result':'PASS_TYPE2_SEPARATED_LOW_EDGES','actual_words':len(cases),'branches':branches},sort_keys=True))


if __name__=='__main__':
    main()
