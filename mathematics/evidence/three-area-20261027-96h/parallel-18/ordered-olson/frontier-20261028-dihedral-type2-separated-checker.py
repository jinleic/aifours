#!/usr/bin/env python3
"""Independent actual-word audit for type-II low-edge selectors."""
import argparse
from collections import Counter
import copy
import hashlib
import itertools
import json


def multiply(word,idx,p):
    x,b=0,0
    for i in idx:
        y,c=word[i]
        x=(x+((-1 if b else 1)*y))%p
        b^=c
    return x,b


def check(case):
    p,word=case['p'],case['word']
    if len(word)!=4*p-1 or any(a<0 or a>=p or b not in (0,1) for a,b in word):
        raise ValueError('invalid original word')
    refs=[i for i,(_,b) in enumerate(word) if b]
    rotations=[i for i,(_,b) in enumerate(word) if not b]
    counts=Counter(word[i][0] for i in rotations)
    if len(refs)!=p+3 or counts!={1:2*p-2,p-1:p-2}:
        raise ValueError('wrong type-II counts')
    prefix=0
    Q={}
    for i,(x,b) in enumerate(word):
        if b:
            Q[i]=prefix
        else:
            prefix+=1 if x==1 else -1
    if case['label']['generation']=='gauge' and any(word[i][0]!=(-2*Q[i])%p for i in refs):
        raise ValueError('gauge fixture mismatch')
    pairs=case['low_pairs']
    if len(pairs)!=2 or any(len(edge)!=2 for edge in pairs):
        raise ValueError('wrong low-pair count')
    (i,j),(k,l)=pairs
    if not (i<j<k<l and all(t in Q for t in (i,j,k,l))):
        raise ValueError('pairs not chronologically separated')
    for u,v in pairs:
        if not 0<=Q[v]-Q[u]<=p:
            raise ValueError('pair not low')
        signed=[(-word[t][0] if u<t<v else word[t][0])%p for t in rotations]
        if max(Counter(signed).values())>2*p-2:
            raise ValueError('signed count not low')
    selector=case['selector']
    if len(selector)!=2*p or selector!=sorted(set(selector)) or any(t<0 or t>=len(word) for t in selector):
        raise ValueError('bad actual selector indices')
    chosen_refs=[t for t in selector if word[t][1]]
    if case['mode']=='two_reflections':
        x,y=case['selected_pair']
        if chosen_refs!=[x,y] or not (x<y and x in Q and y in Q and 0<=Q[y]-Q[x]<=p):
            raise ValueError('bad two-reflection pair')
    elif case['mode']=='four_reflections':
        if chosen_refs!=[i,j,k,l]:
            raise ValueError('wrong four reflection positions')
        if any((word[v][0]-word[u][0]+2*(Q[v]-Q[u]))%p!=0 for u,v in pairs):
            raise ValueError('low-edge gauge equality fails')
        signs={t:((-word[t][0] if sum(r<t for r in chosen_refs)%2 else word[t][0])%p) for t in rotations}
        if (sum(signs.values())+word[i][0]-word[j][0]+word[k][0]-word[l][0])%p!=0:
            raise ValueError('four-edge cancellation fails')
        omitted=case['omitted_indices']
        if len(omitted)!=p or len(set(omitted))!=p or any(t not in signs for t in omitted) or len({signs[t] for t in omitted})!=1:
            raise ValueError('bad same-sign omissions')
        if set(selector)!=(set(rotations)-set(omitted))|set(chosen_refs):
            raise ValueError('wrong rotation complement')
    else:
        raise ValueError('unknown selector mode')
    if multiply(word,selector,p)!=(0,0):
        raise ValueError('actual original product nonidentity')
    return case['label']['generation']+'/'+case['mode']


def mutation(case,edit,expected):
    c=copy.deepcopy(case)
    edit(c)
    try:
        check(c)
    except ValueError as exc:
        if str(exc)==expected:
            return expected
        raise ValueError('mutation wrong failure: '+str(exc)) from exc
    raise ValueError('mutation survived')


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input')
    parser.add_argument('--output',required=True)
    args=parser.parse_args()
    with open(args.input,'rb') as source:
        raw=source.read()
    data=json.loads(raw)
    branches=Counter(check(c) for c in data['cases'])
    example=next(c for c in data['cases'] if c['mode']=='four_reflections')
    controls=[
        mutation(example,lambda c:c['selector'].__setitem__(1,c['selector'][0]),'bad actual selector indices'),
        mutation(example,lambda c:c['low_pairs'].__setitem__(1,c['low_pairs'][0]),'pairs not chronologically separated'),
        mutation(example,lambda c:c['omitted_indices'].__setitem__(1,c['omitted_indices'][0]),'bad same-sign omissions'),
    ]
    result={'result':'PASS_INDEPENDENT_TYPE2_SEPARATED_CHECK','input_sha256':hashlib.sha256(raw).hexdigest(),
            'actual_original_words_and_selectors':len(data['cases']),'branches':dict(branches),
            'mutation_controls_rejected_for_intended_reasons':controls,
            'scope':'bounded actual words; not an all-prime prefix-interval proof'}
    with open(args.output,'x',encoding='utf-8') as out:
        json.dump(result,out,sort_keys=True,indent=2)
        out.write('\n')
    print(json.dumps(result,sort_keys=True))


if __name__=='__main__':
    main()
