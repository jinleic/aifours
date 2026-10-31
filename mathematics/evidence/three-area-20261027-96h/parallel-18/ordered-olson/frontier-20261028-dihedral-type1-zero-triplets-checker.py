#!/usr/bin/env python3
"""Independent actual-word checker for three zero-net reflection intervals."""
import argparse
from collections import Counter
import copy
import hashlib
import json


def product(word,idx,p):
    x,b=0,0
    for i in idx:
        y,c=word[i]
        x=(x+((-1 if b else 1)*y))%p
        b^=c
    return x,b


def check(case):
    p,word=case['p'],case['word']
    if len(word)!=4*p-1 or any(x<0 or x>=p or b not in (0,1) for x,b in word):
        raise ValueError('invalid full word')
    refs=[i for i,(_,b) in enumerate(word) if b]
    rot=[i for i,(_,b) in enumerate(word) if not b]
    counts=Counter(word[i][0] for i in rot)
    if len(refs)!=p+3 or counts[1]!=2*p-1 or counts[p-1]!=p-3 or len(rot)!=3*p-4:
        raise ValueError('wrong type-I counts')
    Q={}
    z=0
    for i,(x,b) in enumerate(word):
        if b:
            Q[i]=z
        else:
            z+=1 if x==1 else -1
    pairs=case['zero_pairs']
    if len(pairs)!=3 or any(len(pair)!=2 for pair in pairs):
        raise ValueError('wrong zero-pair structure')
    flat=[i for pair in pairs for i in pair]
    if flat!=sorted(set(flat)) or any(i not in Q for i in flat):
        raise ValueError('zero pairs not separated')
    if any(Q[i]!=Q[j] for i,j in pairs):
        raise ValueError('pair net prefix is not zero')
    chosen=case['chosen_pairs']
    if any(pair not in pairs for pair in chosen):
        raise ValueError('chosen pair outside three')
    selector=case['selector']
    if len(selector)!=2*p or selector!=sorted(set(selector)) or any(i<0 or i>=len(word) for i in selector):
        raise ValueError('bad actual selector indices')
    chosen_refs=sorted(i for pair in chosen for i in pair)
    if [i for i in selector if word[i][1]]!=chosen_refs:
        raise ValueError('selected reflections do not match pairs')
    mode=case['mode']
    if mode=='two':
        if len(chosen)!=1 or (word[chosen[0][1]][0]-word[chosen[0][0]][0])%p in (0,2%p):
            raise ValueError('invalid two-reflection branch')
    else:
        if mode not in ('four-mixed','four-all-two','six'):
            raise ValueError('unknown branch')
        signed={t:(-word[t][0] if sum(r<t for r in chosen_refs)%2 else word[t][0])%p for t in rot}
        omitted=case['omitted']
        if len(set(omitted))!=len(omitted) or any(t not in signed for t in omitted):
            raise ValueError('invalid omitted indices')
        if set(selector)!=(set(rot)-set(omitted))|set(chosen_refs):
            raise ValueError('wrong rotation complement')
        if mode.startswith('four') and len(chosen)!=2:
            raise ValueError('wrong four branch pair count')
        if mode=='six' and len(chosen)!=3:
            raise ValueError('wrong six branch pair count')
        reflsum=sum((word[i][0]-word[j][0]) for i,j in chosen)%p
        if (sum(signed.values())+reflsum-sum(signed[t] for t in omitted))%p!=0:
            raise ValueError('signed omission arithmetic failed')
    if product(word,selector,p)!=(0,0):
        raise ValueError('actual original product nonidentity')
    return case['label']['generation']+'/'+mode


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
    example=next(c for c in data['cases'] if c['mode'].startswith('four'))
    controls=[
        mutation(example,lambda c:c['selector'].__setitem__(1,c['selector'][0]),'bad actual selector indices'),
        mutation(example,lambda c:c['zero_pairs'].__setitem__(1,c['zero_pairs'][0]),'zero pairs not separated'),
        mutation(example,lambda c:c['omitted'].__setitem__(1,c['omitted'][0]),'invalid omitted indices'),
    ]
    result={'result':'PASS_INDEPENDENT_ZERO_TRIPLETS_CHECK','input_sha256':hashlib.sha256(raw).hexdigest(),
            'actual_words_and_original_selectors':len(data['cases']),'branches':dict(branches),
            'skipped_layouts_not_decided':data['skipped'],'mutation_controls_rejected_for_intended_reasons':controls,
            'scope':'bounded qualifying original words; not a proof for unqualified layouts'}
    with open(args.output,'x',encoding='utf-8') as out:
        json.dump(result,out,sort_keys=True,indent=2)
        out.write('\n')
    print(json.dumps(result,sort_keys=True))


if __name__=='__main__':
    main()
