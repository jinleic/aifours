#!/usr/bin/env python3
"""Audit arbitrary-u/v four-block selectors without producer imports."""
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


def runs(w):
    refs=[i for i,(_,e) in enumerate(w) if e];F=len(refs)
    vals=[w[i][0] for i in refs]
    cut=next((i for i in range(F) if vals[i]!=vals[(i-1)%F]),None)
    if cut is None:raise ValueError('SINGLE_PROJECTION_RUN')
    out=[]
    for k in range(F):
        i=refs[(cut+k)%F]
        if not out or w[out[-1][0]][0]!=w[i][0]:out.append([i])
        else:out[-1].append(i)
    return out


def check(case):
    p,w=case['p'],case['word'];N=len(w)
    refs=[i for i,(_,e) in enumerate(w) if e];rot=[i for i,(_,e) in enumerate(w) if not e]
    if N!=4*p-1 or len(refs)!=3*p-2 or len(rot)!=p+1:raise ValueError('COUNTS')
    rr=runs(w);odd=[r for r in rr if len(r)%2];even=[r for r in rr if len(r)%2==0]
    if len(odd)!=p or len(even)!=case['even_projected_runs'] or len({w[r[0]][0] for r in odd})!=p:
        raise ValueError('PROJECTION_PREMISE')
    block=case['fourblock_cyclic_indices']
    if len(block)!=4 or any(block[k+1]!=(block[k]+1)%N for k in range(3)):
        raise ValueError('BLOCK_POSITIONS')
    if [w[i][1] for i in block]!=[1,0,1,0] or w[block[0]][0]!=w[block[2]][0]:
        raise ValueError('FOURBLOCK_FORM')
    if not any(block[0] in r and block[2] in r for r in odd):
        raise ValueError('BLOCK_NOT_ODD_RUN')
    target=(w[block[1]][0]-w[block[3]][0])%p
    if target!=case['target']:raise ValueError('TARGET_METADATA')
    selector=case['selector']
    if len(selector)!=2*p or selector!=sorted(set(selector)) or not set(block).issubset(selector):
        raise ValueError('SELECTOR_INDICES')
    order=[(block[-1]+1+k)%N for k in range(N)]
    rest=[i for i in order if i in selector and i not in block]
    if len(rest)!=2*p-4 or any(not w[i][1] for i in rest):raise ValueError('REMAINDER_REFLECTIONS')
    if product(w,block,p)!=((-target)%p,0) or product(w,rest,p)!=(target,0):
        raise ValueError('ACTUAL_BLOCK_REMAINDER_PRODUCT')
    active=[r for r in rr if sum(i in selector and i not in block for i in r)%2]
    if (target==0 and active) or (target!=0 and (len(active)!=2 or any(r not in odd for r in active))):
        raise ValueError('ACTIVE_RUN_PATTERN')
    if product(w,selector,p)!=(0,0):raise ValueError('ORIGINAL_PRODUCT')
    return ('nonzero' if target else 'zero')+f"/e{len(even)}"


def mutate(case,edit,expected):
    c=copy.deepcopy(case);edit(c)
    try:check(c)
    except ValueError as exc:
        if str(exc)==expected:return expected
        raise ValueError('CONTROL_WRONG: '+str(exc)) from exc
    raise ValueError('CONTROL_SURVIVED')


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input');parser.add_argument('--output',required=True);args=parser.parse_args()
    with open(args.input,'rb') as source:raw=source.read()
    data=json.loads(raw);branches=Counter(check(c) for c in data['cases'])
    sample=data['cases'][0]
    controls=[mutate(sample,lambda c:c['selector'].__setitem__(1,c['selector'][0]),'SELECTOR_INDICES'),
              mutate(sample,lambda c:c.__setitem__('target',(c['target']+1)%c['p']),'TARGET_METADATA')]
    result={'result':'PASS_INDEPENDENT_ARBITRARY_FOURBLOCK','input_sha256':hashlib.sha256(raw).hexdigest(),
            'actual_words_and_selectors':len(data['cases']),'branches':dict(branches),'controls':controls,
            'scope':'bounded projected data plus actual block/products; no residual/actual-block transfer'}
    with open(args.output,'x',encoding='utf-8') as out:
        json.dump(result,out,sort_keys=True,indent=2);out.write('\n')
    print(json.dumps(result,sort_keys=True))


if __name__=='__main__':
    main()
