#!/usr/bin/env python3
"""Independently reconstruct cyclic odd runs and actual selector products."""
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
    refs=[i for i,(_,b) in enumerate(word) if b]
    rot=[i for i,(_,b) in enumerate(word) if not b]
    if len(word)!=4*p-1 or len(refs)!=3*p-2 or len(rot)!=p+1 or any(word[i][0]==0 for i in rot):
        raise ValueError('wrong zero-free original counts')
    if refs[0]!=0 or any(j-i-1>1 for i,j in zip(refs,refs[1:])) or len(word)-1-refs[-1]>1:
        raise ValueError('cyclic singleton-gap failure')
    values=[word[i][0] for i in refs]
    F=len(refs)
    start=next((i for i in range(F) if values[i]!=values[(i-1)%F]),None)
    if start is None:
        raise ValueError('single cyclic reflection run')
    ordered=[refs[(start+t)%F] for t in range(F)]
    runs=[]
    for i in ordered:
        if not runs or word[runs[-1][0]][0]!=word[i][0]:
            runs.append([i])
        else:
            runs[-1].append(i)
    if len(runs)!=p+2 or any(len(run)%2==0 for run in runs):
        raise ValueError('wrong cyclic odd-run structure')
    labels=[word[run[0]][0] for run in runs]
    if set(labels)!=set(range(p)) or any(labels[i]==labels[(i+1)%len(labels)] for i in range(len(labels))):
        raise ValueError('odd-run labels not full and adjacent-distinct')
    selector=case['selector']
    if len(selector)!=2*p or selector!=sorted(set(selector)) or any(i not in refs for i in selector):
        raise ValueError('bad original reflection selector')
    selected=set(selector)
    odd_labels=[word[run[0]][0] for run in runs if sum(i in selected for i in run)%2]
    if len(odd_labels)!=4 or (odd_labels[0]-odd_labels[1]+odd_labels[2]-odd_labels[3])%p!=0:
        raise ValueError('wrong selected odd-run quadruple')
    if product(word,selector,p)!=(0,0):
        raise ValueError('actual original product nonidentity')
    return case['construction_cut']!=0


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
        mutation(sample,lambda c:c['selector'].__setitem__(1,c['selector'][0]),'bad original reflection selector'),
        mutation(sample,lambda c:c['word'][0].__setitem__(1,0),'wrong zero-free original counts'),
    ]
    result={'result':'PASS_INDEPENDENT_ODD_RUN_SUPPORT_CHECK','input_sha256':hashlib.sha256(raw).hexdigest(),
            'actual_words_and_original_selectors':len(data['cases']),'nonzero_construction_cuts':wraps,
            'mutation_controls_rejected_for_intended_reasons':controls,
            'scope':'bounded full-support odd-run fixtures, not whole L_RES'}
    with open(args.output,'x',encoding='utf-8') as out:
        json.dump(result,out,sort_keys=True,indent=2)
        out.write('\n')
    print(json.dumps(result,sort_keys=True))


if __name__=='__main__':
    main()
