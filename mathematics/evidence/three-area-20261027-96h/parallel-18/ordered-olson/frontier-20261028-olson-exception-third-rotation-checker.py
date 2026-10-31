#!/usr/bin/env python3
"""Reconstruct AP-aligned exception and actual original-index selectors."""
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
    start=next((i for i in range(F) if w[refs[i]][0]!=w[refs[(i-1)%F]][0]),None)
    if start is None:raise ValueError('ONE_RUN')
    runs=[]
    for k in range(F):
        j=refs[(start+k)%F]
        if not runs or w[runs[-1][0]][0]!=w[j][0]:runs.append([j])
        else:runs[-1].append(j)
    return refs,runs


def check(case):
    p,w=case['p'],case['word'];N=len(w);refs,runs=projection(w)
    if N!=4*p-1 or len(refs)!=3*p-2 or sum(e==0 for _,e in w)!=p+1:raise ValueError('COUNTS')
    odd=[run for run in runs if len(run)%2]
    if len(odd)!=p:raise ValueError('ODD_COUNT')
    a,ru,a2,rv,rw=case['marker'];c=case['c'];u=case['u'];t=(2*u)%p
    if w[a]!=[c,1] or ru!=(a+1)%N or a2!=(ru+1)%N or w[ru]!=[u,0] or w[a2]!=[c,1] or w[rv]!=[(-u)%p,0]:
        raise ValueError('DISTINGUISHED_SEGMENT')
    pos=(a2+1)%N;middle=[]
    while pos!=rv and len(middle)<=N:
        if w[pos]!=[c,1]:raise ValueError('MIDDLE_RUN')
        middle.append(pos);pos=(pos+1)%N
    if pos!=rv or not len(middle)%2:raise ValueError('ODD_MIDDLE')
    crun=next((run for run in odd if run[0]==a and run[1]==a2),None)
    if crun is None or crun[-1]!=(rv-1)%N:raise ValueError('C_RUN_BOUNDARY')
    cycle=odd[odd.index(crun):]+odd[:odd.index(crun)]
    if [w[run[0]][0] for run in cycle]!=[(c+j*t)%p for j in range(p)]:raise ValueError('ODD_AP')
    if w[rw][1] or w[rw][0]==(-u)%p:raise ValueError('THIRD_ROTATION')
    if w[(rw-1)%N][1]!=1 or w[(rw+1)%N][1]!=1 or w[(rw-1)%N][0]==w[(rw+1)%N][0]:
        raise ValueError('THIRD_NOT_RUN_BOUNDARY')
    distance=lambda x:(x-rv)%N
    k=sum(distance(run[-1])<distance(rw) for run in cycle[1:])
    if k!=case['k'] or not 1<=k<=p-2:raise ValueError('THIRD_NOT_INTERIOR')
    if w[rw][0]!=case['third_rotation'] or t!=case['t']:raise ValueError('MARKER_METADATA')
    selected=case['selector']
    if len(selected)!=2*p or selected!=sorted(set(selected)) or not {a,ru,a2,rw}.issubset(selected) or rv in selected:
        raise ValueError('SELECTOR')
    if product(w,selected,p)!=(0,0):raise ValueError('ORIGINAL_PRODUCT')
    return 'w_equal_u' if w[rw][0]==u else 'w_neither_sign'


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
              mutate(ex,lambda c:c['word'][c['marker'][4]].__setitem__(0,(-c['u'])%c['p']),'THIRD_ROTATION')]
    result={'result':'PASS_INDEPENDENT_EXCEPTION_THIRD_ROTATION','input_sha256':hashlib.sha256(raw).hexdigest(),
            'actual_words_and_selectors':len(data['cases']),'branches':dict(counts),'controls':controls,
            'scope':'AP-aligned exception with boundary third rotation; no general residual theorem'}
    with open(args.output,'x',encoding='utf-8') as out:
        json.dump(result,out,sort_keys=True,indent=2);out.write('\n')
    print(json.dumps(result,sort_keys=True))


if __name__=='__main__':
    main()
