#!/usr/bin/env python3
"""Verify unique run gaps, spare-gap choice and actual products."""
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
    if cut is None:raise ValueError('ONE_RUN')
    runs=[]
    for k in range(F):
        i=refs[(cut+k)%F]
        if not runs or w[runs[-1][0]][0]!=w[i][0]:runs.append([i])
        else:runs[-1].append(i)
    odd=[r for r in runs if len(r)%2];even=[r for r in runs if len(r)%2==0]
    if len(odd)!=p or len(even)!=1 or len({w[r[0]][0] for r in odd})!=p:
        raise ValueError('PROJECTION_PROFILE')
    runrotation={}
    for run in runs:
        rr=[]
        for i in run:
            if w[(i+1)%N][1]==0:
                if w[(i+2)%N][1]!=1:raise ValueError('SINGLETON_GAPS')
                rr.append((i+1)%N)
        if len(rr)!=1:raise ValueError('ONE_GAP_PER_RUN')
        runrotation[run[0]]=rr[0]
    mark=case['markers'];spares=mark['odd_spares']
    if len(spares)!=p or len(set(spares))!=p or any(sum(i in run for i in spares)!=1 for run in odd):
        raise ValueError('ODD_SPARES')
    for run in odd:
        rotation=runrotation[run[0]];preceding=(rotation-1)%N;k=run.index(preceding)+1
        before,after=run[:k],run[k:];spare=next(i for i in spares if i in run)
        if not ((spare in before and len(before)%2 and len(after)%2==0) or
                (spare in after and len(after)%2 and len(before)%2==0)):
            raise ValueError('SPARE_SIDE')
    r1,r2=mark['rotations']
    if r1==r2 or w[r1][1] or w[r2][1] or any(0<(s-r1)%N<(r2-r1)%N for s in spares):
        raise ValueError('SPARE_GAP_ROTATIONS')
    erun=even[0];erot=runrotation[erun[0]];idx=erun.index((erot-1)%N)+1
    loss=int(erot in (r1,r2) and idx%2==1 and (len(erun)-idx)%2==1)
    if erot!=mark['even_rotation'] or loss!=mark['pair_loss'] or (w[r1][0]+w[r2][0])%p!=mark['rotation_sum']:
        raise ValueError('LOSS_OR_SUM')
    sel=case['selector']
    if len(sel)!=2*p or sel!=sorted(set(sel)) or not {r1,r2}.issubset(sel):raise ValueError('SELECTOR')
    if product(w,sel,p)!=(0,0):raise ValueError('ORIGINAL_PRODUCT')
    return ('zero' if mark['rotation_sum']==0 else 'nonzero')+'/loss'+str(loss)


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
    data=json.loads(raw);branches=Counter(check(c) for c in data['cases']);ex=data['cases'][0]
    controls=[mutate(ex,lambda c:c['selector'].__setitem__(1,c['selector'][0]),'SELECTOR'),
              mutate(ex,lambda c:c['markers']['odd_spares'].__setitem__(1,c['markers']['odd_spares'][0]),'ODD_SPARES')]
    result={'result':'PASS_INDEPENDENT_ONE_EVEN_ONE_GAP','input_sha256':hashlib.sha256(raw).hexdigest(),
            'actual_words_and_selectors':len(data['cases']),'branches':dict(branches),'controls':controls,
            'scope':'one even projected run, one occupied gap per projected run, actual original products'}
    with open(args.output,'x',encoding='utf-8') as out:
        json.dump(result,out,sort_keys=True,indent=2);out.write('\n')
    print(json.dumps(result,sort_keys=True))


if __name__=='__main__':
    main()
