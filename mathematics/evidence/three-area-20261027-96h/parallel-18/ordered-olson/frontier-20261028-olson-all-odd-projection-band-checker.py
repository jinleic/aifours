#!/usr/bin/env python3
"""Audit p odd projected runs with p+1 occupied singleton gaps."""
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
    cut=next((k for k in range(F) if w[refs[k]][0]!=w[refs[(k-1)%F]][0]),None)
    if cut is None:raise ValueError('ONE_PROJECTION_RUN')
    runs=[]
    for k in range(F):
        i=refs[(cut+k)%F]
        if not runs or w[runs[-1][0]][0]!=w[i][0]:runs.append([i])
        else:runs[-1].append(i)
    if len(runs)!=p or any(len(r)%2==0 for r in runs):raise ValueError('PROJECTION_PROFILE')
    occupied=[]
    for k,i in enumerate(refs):
        d=(refs[(k+1)%F]-i)%N
        if d not in (1,2):raise ValueError('SINGLETON_GAPS')
        if d==2:occupied.append(i)
    counts=[sum(i in run for i in occupied) for run in runs]
    if len(occupied)!=p+1 or max(counts)<2:raise ValueError('PIGEONHOLE')
    sel=case['selector']
    if len(sel)!=2*p or sel!=sorted(set(sel)):raise ValueError('SELECTOR')
    if product(w,sel,p)!=(0,0):raise ValueError('ORIGINAL_PRODUCT')
    return 'distinct' if len({w[r[0]][0] for r in runs})==p else 'repeated'


def mutate(case,edit,expected):
    c=copy.deepcopy(case);edit(c)
    try:check(c)
    except ValueError as exc:
        if str(exc)==expected:return expected
        raise ValueError('CONTROL_WRONG: '+str(exc)) from exc
    raise ValueError('CONTROL_SURVIVED')


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('inputs',nargs='+');parser.add_argument('--output',required=True);args=parser.parse_args()
    branches=Counter();pins={};fixture=None;skipped=0
    for path in args.inputs:
        with open(path,'rb') as src:raw=src.read()
        pins[path]=hashlib.sha256(raw).hexdigest();data=json.loads(raw)
        for case in data['cases']:
            if case.get('even_projection_runs',0)!=0:skipped+=1;continue
            branches[check(case)]+=1
            if fixture is None:fixture=case
    controls=[mutate(fixture,lambda c:c['selector'].__setitem__(1,c['selector'][0]),'SELECTOR'),
              mutate(fixture,lambda c:c['word'].append([1,0]),'COUNTS')]
    result={'result':'PASS_INDEPENDENT_ALL_ODD_PROJECTION_BAND','input_sha256':pins,
            'actual_words_and_selectors':sum(branches.values()),'branches':dict(branches),
            'skipped_even_projection_fixtures':skipped,'controls':controls,
            'scope':'finite p-odd projection, no even runs, actual singleton gaps'}
    with open(args.output,'x',encoding='utf-8') as out:
        json.dump(result,out,sort_keys=True,indent=2);out.write('\n')
    print(json.dumps(result,sort_keys=True))


if __name__=='__main__':
    main()
