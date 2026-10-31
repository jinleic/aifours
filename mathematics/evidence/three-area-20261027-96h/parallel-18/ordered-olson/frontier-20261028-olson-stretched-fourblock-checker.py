#!/usr/bin/env python3
"""Independently audit actual stretched selectors and their cyclic splits."""
import argparse
from collections import Counter
import copy
import hashlib
import itertools
import json


def product(w,idx,p):
    x,e=0,0
    for i in idx:
        y,b=w[i];x=(x+(-y if e else y))%p;e^=b
    return x,e


def projection(w):
    refs=[i for i,(_,e) in enumerate(w) if e];n=len(refs)
    cut=next((k for k in range(n) if w[refs[k]][0]!=w[refs[(k-1)%n]][0]),None)
    if cut is None:raise ValueError('SINGLE_RUN')
    runs=[]
    for k in range(n):
        i=refs[(cut+k)%n]
        if not runs or w[runs[-1][0]][0]!=w[i][0]:runs.append([i])
        else:runs[-1].append(i)
    return refs,runs


def check(case):
    p,w=case['p'],case['word'];N=len(w);refs,rr=projection(w)
    if N!=4*p-1 or len(refs)!=3*p-2 or sum(e==0 for _,e in w)!=p+1:raise ValueError('COUNTS')
    odd=[run for run in rr if len(run)%2]
    if len(odd)!=p or len({w[run[0]][0] for run in odd})!=p:raise ValueError('ODD_RUNS')
    b=case['actual_segment'];a,ru,b2,rv=b
    if ru!=(a+1)%N or b2!=(ru+1)%N or [w[i][1] for i in b]!=[1,0,1,0] or w[a][0]!=w[b2][0]:
        raise ValueError('SEGMENT_FORM')
    c=w[a][0];mid=[];pos=(b2+1)%N
    while pos!=rv and len(mid)<=N:
        if w[pos]!=( [c,1] ):raise ValueError('MID_NOT_SAME_REFLECTION')
        mid.append(pos);pos=(pos+1)%N
    if pos!=rv or len(mid)!=case['h']:raise ValueError('MID_LENGTH')
    run=next((run for run in odd if a in run and b2 in run),None)
    if run is None:raise ValueError('BLOCK_NOT_ODD_RUN')
    index=run.index(a);q=index;r=len(run)-index-2-len(mid)
    if q!=case['q'] or r!=case['r'] or r<0:raise ValueError('CYCLIC_SPLIT')
    u,v=w[ru][0],w[rv][0]
    if (u,v,(u-v)%p)!=(case['u'],case['v'],case['target']):raise ValueError('ROTATION_METADATA')
    if r+q==0 and (u+v)%p==0 and (u-v)%p:
        order=[(rv+1+k)%N for k in range(N)]
        labels=[];seen=set()
        for i in order:
            if w[i][1] and w[i][0]!=c and w[i][0] not in seen:
                # Other odd runs have distinct labels. Even runs are absent in these fixtures.
                seen.add(w[i][0]);labels.append(w[i][0])
        if not any((x-y)%p==(u-v)%p for x,y in itertools.combinations(labels,2)):
            raise ValueError('EXCEPTION_NOT_EXCLUDED')
    sel=case['selector']
    if len(sel)!=2*p or sel!=sorted(set(sel)) or not set(b).issubset(sel):raise ValueError('SELECTOR_INDICES')
    if product(w,sel,p)!=(0,0):raise ValueError('ORIGINAL_PRODUCT')
    return case['branch']


def mutate(case,edit,expected):
    c=copy.deepcopy(case);edit(c)
    try:check(c)
    except ValueError as exc:
        if str(exc)==expected:return expected
        raise ValueError('CONTROL_WRONG: '+str(exc)) from exc
    raise ValueError('CONTROL_SURVIVED')


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('input');parser.add_argument('--output',required=True);args=parser.parse_args()
    with open(args.input,'rb') as source:raw=source.read()
    data=json.loads(raw);branches=Counter(check(c) for c in data['cases']);ex=data['cases'][0]
    controls=[mutate(ex,lambda c:c['selector'].__setitem__(1,c['selector'][0]),'SELECTOR_INDICES'),
              mutate(ex,lambda c:c.__setitem__('h',c['h']+1),'MID_LENGTH')]
    output={'result':'PASS_INDEPENDENT_STRETCHED_FOURBLOCK','input_sha256':hashlib.sha256(raw).hexdigest(),
            'actual_words_and_selectors':len(data['cases']),'branches':dict(branches),
            'controls':controls,'excluded_exceptional_draws':data['excluded_exceptional_draws'],
            'scope':'bounded distinct-odd-projection fixtures; exception intentionally excluded'}
    with open(args.output,'x',encoding='utf-8') as out:
        json.dump(output,out,sort_keys=True,indent=2);out.write('\n')
    print(json.dumps(output,sort_keys=True))


if __name__=='__main__':
    main()
