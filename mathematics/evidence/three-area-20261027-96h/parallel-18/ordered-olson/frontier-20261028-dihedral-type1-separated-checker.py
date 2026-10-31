#!/usr/bin/env python3
"""Independently audit type-I separated low-pair selectors."""
import argparse
from collections import Counter
import copy
import hashlib
import json


def product(word,indices,p):
    state=(0,0)
    for i in indices:
        x,b=state
        y,c=word[i]
        state=((x+(-y if b else y))%p,b^c)
    return state


def check(case):
    p,word=case['p'],case['word']
    if len(word)!=4*p-1 or any(x<0 or x>=p or b not in (0,1) for x,b in word):
        raise ValueError('invalid original word')
    refs=[i for i,(_,b) in enumerate(word) if b]
    rot=[i for i,(_,b) in enumerate(word) if not b]
    c=Counter(word[i][0] for i in rot)
    if len(refs)!=p+3 or c[1]!=2*p-1 or c[p-1]!=p-3 or sum(c.values())!=3*p-4:
        raise ValueError('wrong type-I counts')
    Q={}
    z=0
    for i,(x,b) in enumerate(word):
        if b:
            Q[i]=z
        else:
            z+=1 if x==1 else -1
    pairs=case['low_pairs']
    if len(pairs)!=2 or any(len(edge)!=3 for edge in pairs):
        raise ValueError('wrong low-pair structure')
    (i,j,u),(k,l,v)=pairs
    if not (i<j<k<l and all(t in Q for t in (i,j,k,l))):
        raise ValueError('low pairs not separated')
    if u!=Q[j]-Q[i] or v!=Q[l]-Q[k] or not (1<=u<=p+1 and 1<=v<=p+1 and u+v<=p):
        raise ValueError('wrong low increments')
    selector=case['selector']
    if len(selector)!=2*p or selector!=sorted(set(selector)) or any(t<0 or t>=len(word) for t in selector):
        raise ValueError('bad original selector indices')
    selected_refs=[t for t in selector if word[t][1]]
    if case['mode']=='two':
        if case['selected_pair'] not in ([i,j],[k,l]) or selected_refs!=case['selected_pair']:
            raise ValueError('wrong two-reflection pair')
    elif case['mode']=='four':
        if selected_refs!=[i,j,k,l]:
            raise ValueError('wrong four-reflection positions')
        if any((word[vv][0]-word[uu][0]-2*(1-du))%p!=0 for uu,vv,du in pairs):
            raise ValueError('pair missing-target equalities fail')
        signed={t:(-word[t][0] if sum(r<t for r in selected_refs)%2 else word[t][0])%p for t in rot}
        if (sum(signed.values())+word[i][0]-word[j][0]+word[k][0]-word[l][0])%p != (-2)%p:
            raise ValueError('four-reflection signed total mismatch')
        omitted=case['omitted']
        if len(omitted)!=p or len(set(omitted))!=p or any(t not in signed for t in omitted):
            raise ValueError('invalid omitted indices')
        signs=Counter(signed[t] for t in omitted)
        if signs[1]!=p-1 or signs[p-1]!=1:
            raise ValueError('wrong signed omission counts')
        if set(selector)!=(set(rot)-set(omitted)) | set(selected_refs):
            raise ValueError('wrong selected complement')
    else:
        raise ValueError('unknown selector mode')
    if product(word,selector,p)!=(0,0):
        raise ValueError('actual ordered product nonidentity')
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
    cases=data['random_cases']+data['forced_cases']
    branches=Counter(check(c) for c in cases)
    example=data['forced_cases'][0]
    controls=[
        mutation(example,lambda c:c['selector'].__setitem__(1,c['selector'][0]),'bad original selector indices'),
        mutation(example,lambda c:c['low_pairs'].__setitem__(1,c['low_pairs'][0]),'low pairs not separated'),
        mutation(example,lambda c:c['omitted'].__setitem__(1,c['omitted'][0]),'invalid omitted indices'),
    ]
    result={'result':'PASS_INDEPENDENT_TYPE1_SEPARATED_CHECK','input_sha256':hashlib.sha256(raw).hexdigest(),
            'actual_original_words_and_selectors':len(cases),'branches':dict(branches),
            'skipped_random_patterns_not_decided':data['skipped'],
            'mutation_controls_rejected_for_intended_reasons':controls,
            'scope':'bounded actual words satisfying the sufficient condition; not complete type-I proof'}
    with open(args.output,'x',encoding='utf-8') as out:
        json.dump(result,out,sort_keys=True,indent=2)
        out.write('\n')
    print(json.dumps(result,sort_keys=True))


if __name__=='__main__':
    main()
