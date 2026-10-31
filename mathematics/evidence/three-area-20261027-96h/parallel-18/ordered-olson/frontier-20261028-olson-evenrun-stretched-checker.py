#!/usr/bin/env python3
"""Reconstruct even projection run and actual 2p selector without producer."""
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
    odd=[r for r in runs if len(r)%2];even=[r for r in runs if len(r)%2==0]
    if len(odd)!=p or not even or len({w[r[0]][0] for r in odd})!=p:raise ValueError('PROJECTION_PROFILE')
    a,ru,b,rv=case['actual_segment'];c=w[a][0]
    if ru!=(a+1)%N or b!=(ru+1)%N or [w[i][1] for i in (a,ru,b,rv)]!=[1,0,1,0] or w[b][0]!=c:
        raise ValueError('SEGMENT')
    mid=[];i=(b+1)%N
    while i!=rv and len(mid)<=N:
        if w[i]!=[c,1]:raise ValueError('INTERIOR')
        mid.append(i);i=(i+1)%N
    if i!=rv or len(mid)!=case['h']:raise ValueError('INTERIOR_LENGTH')
    run=next((r for r in even if a in r and b in r),None)
    if run is None:raise ValueError('NOT_EVEN_RUN')
    q=run.index(a);r=len(run)-q-2-len(mid)
    if (q,r)!=(case['q'],case['r']):raise ValueError('SPLIT')
    u,v=w[ru][0],w[rv][0];t=(u-v)%p
    if (u,v,t)!=(case['u'],case['v'],case['target']):raise ValueError('ROTATION_VALUES')
    selected=case['selector']
    if len(selected)!=2*p or selected!=sorted(set(selected)) or not {a,ru,b,rv}.issubset(selected):raise ValueError('SELECTOR')
    if product(w,selected,p)!=(0,0):raise ValueError('PRODUCT')
    oddparts=sum(x%2 for x in (len(mid),q,r))
    return ('target0' if not t else 'target_nonzero')+'/oddparts'+str(oddparts)


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
    data=json.loads(raw);counts=Counter(check(c) for c in data['cases']);ex=data['cases'][0]
    controls=[mutate(ex,lambda c:c['selector'].__setitem__(1,c['selector'][0]),'SELECTOR'),
              mutate(ex,lambda c:c.__setitem__('h',c['h']+1),'INTERIOR_LENGTH')]
    result={'result':'PASS_INDEPENDENT_EVENRUN_STRETCHED','input_sha256':hashlib.sha256(raw).hexdigest(),
            'actual_words_and_selectors':len(data['cases']),'branches':dict(counts),'controls':controls,
            'scope':'actual segment in an even projection run; no historical actual-block transfer'}
    with open(args.output,'x',encoding='utf-8') as out:
        json.dump(result,out,sort_keys=True,indent=2);out.write('\n')
    print(json.dumps(result,sort_keys=True))


if __name__=='__main__':
    main()
