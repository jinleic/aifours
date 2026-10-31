#!/usr/bin/env python3
"""Independently audit cyclic-cut reflection witnesses and original ordering."""
import argparse
from collections import Counter
import copy
import hashlib
import json


def product(word,idx,p):
    a,b=0,0
    for i in idx:
        x,y=word[i]
        a=(a+(-x if b else x))%p
        b^=y
    return a,b


def check(case):
    p,word=case['p'],case['word']
    refs=[i for i,(_,b) in enumerate(word) if b]
    rot=[i for i,(_,b) in enumerate(word) if not b]
    if len(word)!=4*p-1 or len(refs)!=3*p-2 or len(rot)!=p+1 or any(word[i][0]==0 for i in rot):
        raise ValueError('wrong zero-free original counts')
    if refs[0]!=0 or any(j-i-1>1 for i,j in zip(refs,refs[1:])) or len(word)-1-refs[-1]>1:
        raise ValueError('cyclic reflection gaps not singleton')
    F=len(refs)
    vals=[word[i][0] for i in refs]
    d=[(vals[(i+1)%F]-vals[i])%p for i in range(F)]
    zeros=[i for i,x in enumerate(d) if x==0]
    turns=[i for i in range(F) if d[i] and d[(i+1)%F] and d[i]!=d[(i+1)%F]]
    if not 1<=len(zeros)<=(p+1)//2 or case['cyclic_zero_edges']!=len(zeros) or case['cyclic_turn_edges']!=turns:
        raise ValueError('cyclic turn or zero count mismatch')
    cut=case['cut_zero_edge']
    if cut not in zeros:
        raise ValueError('cut is not an equal-exponent edge')
    ords=list(range(cut+1,F))+list(range(cut+1))
    order=[refs[i] for i in ords]
    rotated=case['rotated_selector']
    original=case['original_selector']
    if len(rotated)!=2*p or len(set(rotated))!=2*p or any(i not in refs for i in rotated):
        raise ValueError('bad rotated selector')
    positions=[order.index(i) for i in rotated]
    if positions!=sorted(positions):
        raise ValueError('rotated selector not cyclic-order increasing')
    if original!=sorted(rotated):
        raise ValueError('original selector not restored')
    if product(word,rotated,p)!=(0,0) or product(word,original,p)!=(0,0):
        raise ValueError('cyclic or original product nonidentity')
    return rotated!=original


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
    wraps=sum(check(c) for c in data['cases'])
    sample=data['cases'][0]
    controls=[
        mutation(sample,lambda c:c['rotated_selector'].__setitem__(1,c['rotated_selector'][0]),'bad rotated selector'),
        mutation(sample,lambda c:c.__setitem__('cut_zero_edge',c['cyclic_turn_edges'][0]),'cut is not an equal-exponent edge'),
        mutation(sample,lambda c:c['original_selector'].__setitem__(0,c['original_selector'][1]),'original selector not restored'),
    ]
    result={'result':'PASS_INDEPENDENT_CYCLIC_TURN_CHECK','input_sha256':hashlib.sha256(raw).hexdigest(),
            'actual_full_words_and_selectors':len(data['cases']),'selectors_crossing_original_start':wraps,
            'mutation_controls_rejected_for_intended_reasons':controls,
            'scope':'bounded cyclic-cut witnesses, not an all-prime theorem or L_RES closure'}
    with open(args.output,'x',encoding='utf-8') as out:
        json.dump(result,out,sort_keys=True,indent=2)
        out.write('\n')
    print(json.dumps(result,sort_keys=True))


if __name__=='__main__':
    main()
