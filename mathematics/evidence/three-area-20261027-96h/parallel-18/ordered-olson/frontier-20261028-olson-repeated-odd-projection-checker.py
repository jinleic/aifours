#!/usr/bin/env python3
"""Audit reflection-only selectors and occupied-gap pigeonhole."""
import argparse
from collections import Counter
import copy
import hashlib
import json


def product(w,idx,p):
    x,e=0,0
    for i in idx:
        y,b=w[i];x=(x+(-y if e else y))%p;e^=b
    return x,e


def check(case):
    p,w=case['p'],case['word'];N=len(w);refs=[i for i,(_,e) in enumerate(w) if e];F=len(refs)
    if N!=4*p-1 or F!=3*p-2 or sum(e==0 for _,e in w)!=p+1:raise ValueError('COUNTS')
    cut=next((i for i in range(F) if w[refs[i]][0]!=w[refs[(i-1)%F]][0]),None)
    if cut is None:raise ValueError('ONE_RUN')
    runs=[]
    for k in range(F):
        i=refs[(cut+k)%F]
        if not runs or w[runs[-1][0]][0]!=w[i][0]:runs.append([i])
        else:runs[-1].append(i)
    if len(runs)!=p or any(len(r)%2==0 for r in runs) or len({w[r[0]][0] for r in runs})==p:
        raise ValueError('ODD_DUPLICATE_PROFILE')
    occ=[]
    for k,i in enumerate(refs):
        following=refs[(k+1)%F];distance=(following-i)%N
        if distance not in (1,2):raise ValueError('SINGLETON_GAP')
        if distance==2:occ.append(i)
    perrun=[sum(i in r for i in occ) for r in runs]
    if len(occ)!=p+1 or max(perrun)<2:raise ValueError('PIGEONHOLE')
    sel=case['selector']
    if len(sel)!=2*p or sel!=sorted(set(sel)) or any(not w[i][1] for i in sel):raise ValueError('SELECTOR')
    if product(w,sel,p)!=(0,0):raise ValueError('PRODUCT')
    return str(p)


def mutate(case,edit,expected):
    c=copy.deepcopy(case);edit(c)
    try:check(c)
    except ValueError as exc:
        if str(exc)==expected:return expected
        raise ValueError('CONTROL_WRONG: '+str(exc)) from exc
    raise ValueError('CONTROL_SURVIVED')


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('input');parser.add_argument('--output',required=True);args=parser.parse_args()
    with open(args.input,'rb') as src:raw=src.read()
    data=json.loads(raw);counts=Counter(check(c) for c in data['cases']);ex=data['cases'][0]
    controls=[mutate(ex,lambda c:c['selector'].__setitem__(1,c['selector'][0]),'SELECTOR'),
              mutate(ex,lambda c:c['word'].append([1,0]),'COUNTS')]
    result={'result':'PASS_INDEPENDENT_REPEATED_ODD_PROJECTION','input_sha256':hashlib.sha256(raw).hexdigest(),
            'actual_words_and_selectors':len(data['cases']),'primes':dict(counts),'controls':controls,
            'scope':'repeated odd-projection values, actual singleton gaps, reflection-only selectors'}
    with open(args.output,'x',encoding='utf-8') as out:
        json.dump(result,out,sort_keys=True,indent=2);out.write('\n')
    print(json.dumps(result,sort_keys=True))


if __name__=='__main__':
    main()
