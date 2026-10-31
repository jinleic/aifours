#!/usr/bin/env python3
"""Independent audit of spare-sector selectors (no producer imports).

Recomputes from each linear actual word: counts, singleton cyclic gaps, the
cyclic reflection-only projection, one-occupied-gap-per-run, canonical odd-run
spares, the two-rotation sector condition, the even split loss, the branch,
and the original-order product of the supplied 2p selector.
"""
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


def analyse(case):
    p,w=case['p'],case['word'];N=len(w)
    refs=[i for i,(_,e) in enumerate(w) if e];rots=[i for i,(_,e) in enumerate(w) if not e]
    if N!=4*p-1 or len(refs)!=3*p-2 or len(rots)!=p+1:raise ValueError('COUNTS')
    if any(not w[(i+1)%N][1] for i in rots):raise ValueError('SINGLETON')
    F=len(refs);lab=[w[i][0] for i in refs]
    start=next((k for k in range(F) if lab[k]!=lab[k-1]),None)
    if start is None:raise ValueError('PROJECTION')
    runs=[]
    for k in range(F):
        i=refs[(start+k)%F]
        if not runs or w[runs[-1][-1]][0]!=w[i][0]:runs.append([i])
        else:runs[-1].append(i)
    runof={i:t for t,run in enumerate(runs) for i in run}
    odd=[t for t,run in enumerate(runs) if len(run)%2]
    if len(odd)!=p or len({w[runs[t][0]][0] for t in odd})!=p:raise ValueError('PROJECTION')
    before={r:(r-1)%N for r in rots}
    gaps={}
    for r in rots:
        t=runof[before[r]]
        if t in gaps:raise ValueError('ONE_GAP_PER_RUN')
        gaps[t]=r
    spares=set()
    for t in odd:
        run=runs[t]
        if t in gaps:
            k=run.index(before[gaps[t]])+1;piece=run[:k] if k%2 else run[k:]
        else:piece=run
        spares.add(piece[-1])
    return p,w,N,runs,runof,rots,before,spares


def check(case):
    p,w,N,runs,runof,rots,before,spares=analyse(case)
    r1,r2=case['rotations']
    if r1==r2 or r1 not in rots or r2 not in rots:raise ValueError('ROTATIONS')
    D=(r2-r1)%N
    if any(0<(s-r1)%N<D for s in spares):raise ValueError('SECTOR')
    loss=0;labels=[]
    for r in (r1,r2):
        run=runs[runof[before[r]]];labels.append(w[run[0]][0])
        loss+=len(run)%2==0 and (run.index(before[r])+1)%2==1
    sel=case['selector']
    if len(sel)!=2*p or sel!=sorted(set(sel)) or not all(0<=i<N for i in sel):raise ValueError('SELECTOR')
    if {i for i in sel if not w[i][1]}!={r1,r2}:raise ValueError('SELECTED_ROTATIONS')
    if product(w,sel,p)!=(0,0):raise ValueError('PRODUCT')
    s=(w[r1][0]+w[r2][0])%p;alpha,beta=labels
    if loss<2:branch='L%d/%s'%(loss,'s!=0' if s else 's=0')
    elif (beta-alpha+s)%p:branch='L2/I'
    else:branch='L2/II/s!=0' if s else 'L2/II/s=0'
    if loss!=case['loss'] or branch!=case['branch']:raise ValueError('BRANCH_LABEL')
    return branch


def mutate(case,edit,expected):
    c=copy.deepcopy(case);edit(c)
    try:check(c)
    except ValueError as exc:
        if str(exc)==expected:return expected
        raise ValueError('CONTROL_WRONG: '+str(exc)) from exc
    raise ValueError('CONTROL_SURVIVED')


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('inputs',nargs='+');parser.add_argument('--output',required=True);args=parser.parse_args()
    pins={};branches=Counter();primes=Counter();sample=None
    for path in args.inputs:
        with open(path,'rb') as src:raw=src.read()
        pins[path]=hashlib.sha256(raw).hexdigest()
        for case in json.loads(raw)['cases']:
            branches[check(case)]+=1;primes[case['p']]+=1
            if sample is None:sample=case
    def tamper_v(c):
        r=c['rotations'][1];c['word'][r][0]=(c['word'][r][0]+1)%c['p']
    controls=[mutate(sample,lambda c:c['selector'].__setitem__(1,c['selector'][0]),'SELECTOR'),
              mutate(sample,tamper_v,'PRODUCT'),
              mutate(sample,lambda c:c.__setitem__('branch','L9'),'BRANCH_LABEL')]
    result={'result':'PASS_INDEPENDENT_SPARE_SECTOR','input_sha256':pins,
            'actual_words_and_selectors':sum(branches.values()),'branches':dict(sorted(branches.items())),
            'primes':{str(k):v for k,v in sorted(primes.items())},'controls':controls,
            'scope':'o_pi=p, distinct odd labels, one occupied gap per projected run, singleton gaps, R=p+1'}
    with open(args.output,'x',encoding='utf-8') as out:
        json.dump(result,out,sort_keys=True,indent=2);out.write('\n')
    print(json.dumps(result,sort_keys=True))


if __name__=='__main__':
    main()
