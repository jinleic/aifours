#!/usr/bin/env python3
"""Directly verify opposite rotations and all p−1 reflection pairs."""
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


def projection(w):
    refs=[i for i,(_,e) in enumerate(w) if e];F=len(refs)
    k=next((i for i in range(F) if w[refs[i]][0]!=w[refs[(i-1)%F]][0]),None)
    if k is None:raise ValueError('ONE_RUN')
    runs=[]
    for j in range(F):
        i=refs[(k+j)%F]
        if not runs or w[runs[-1][0]][0]!=w[i][0]:runs.append([i])
        else:runs[-1].append(i)
    return refs,runs


def check(case):
    p,w=case['p'],case['word'];N=len(w);refs,runs=projection(w)
    rots=[i for i,(_,e) in enumerate(w) if not e]
    if N!=4*p-1 or len(refs)!=3*p-2 or len(rots)!=p+1:raise ValueError('COUNTS')
    odd=[r for r in runs if len(r)%2];even=[r for r in runs if len(r)%2==0]
    if len(odd)!=p or len(even)!=case['even_projection_runs']:raise ValueError('PROJECTION_PROFILE')
    a,ru,rv=case['marker'];c=case['c'];u=case['u']
    if w[a]!=[c,1] or ru!=(a+1)%N or w[ru]!=[u,0] or w[rv]!=[(-u)%p,0]:
        raise ValueError('OPPOSITE_ROTATION')
    pos=(ru+1)%N;middle=[]
    while pos!=rv and len(middle)<=N:
        if w[pos]!=[c,1]:raise ValueError('CENTRAL_RUN')
        middle.append(pos);pos=(pos+1)%N
    if pos!=rv or not middle or len(middle)%2:raise ValueError('CENTRAL_PARITY')
    if not any(run==[a]+middle for run in odd):raise ValueError('ACTUAL_PROJECTION_RUN')
    if any(i!=ru and w[i][0]!=(-u)%p for i in rots):raise ValueError('OTHER_ROTATIONS')
    selected=case['selector']
    if len(selected)!=2*p or selected!=sorted(set(selected)) or a in selected or not {ru,rv}.issubset(selected):
        raise ValueError('SELECTOR')
    if not set(middle).issubset(selected):raise ValueError('MIDDLE_NOT_SELECTED')
    order=[(ru+1+k)%N for k in range(N)]
    chosen=[i for i in order if i in selected and w[i][1]]
    if len(chosen)!=2*p-2 or any(w[chosen[i]][0]!=w[chosen[i+1]][0] for i in range(0,len(chosen),2)):
        raise ValueError('REFLECTION_PAIRS')
    if product(w,selected,p)!=(0,0):raise ValueError('ORIGINAL_PRODUCT')
    return str(len(even))


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
    controls=[mutate(ex,lambda c:c['selector'].__setitem__(0,c['marker'][0]),'SELECTOR'),
              mutate(ex,lambda c:c['word'][c['marker'][2]].__setitem__(0,c['u']),'OPPOSITE_ROTATION')]
    result={'result':'PASS_INDEPENDENT_OPPOSITE_ROTATION_SELECTOR','input_sha256':hashlib.sha256(raw).hexdigest(),
            'actual_words_and_selectors':len(data['cases']),'even_projection_run_counts':dict(counts),
            'controls':controls,'scope':'full AP-aligned exception fixtures; all other rotations negative u'}
    with open(args.output,'x',encoding='utf-8') as out:
        json.dump(result,out,sort_keys=True,indent=2);out.write('\n')
    print(json.dumps(result,sort_keys=True))


if __name__=='__main__':
    main()
