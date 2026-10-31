#!/usr/bin/env python3
"""Independent actual cyclic product audit with even projection runs."""
import argparse
import copy
import hashlib
import json


def product(w,indices,p):
    x,e=0,0
    for i in indices:
        y,b=w[i];x=(x+(-y if e else y))%p;e^=b
    return x,e


def check(case):
    p,w=case['p'],case['word'];N=len(w)
    refs=[i for i,(_,e) in enumerate(w) if e];rot=[i for i,(_,e) in enumerate(w) if not e]
    if N!=4*p-1 or len(refs)!=3*p-2 or len(rot)!=p+1:raise ValueError('COUNTS')
    vals=[w[i][0] for i in refs];F=len(vals)
    start=next((i for i in range(F) if vals[i]!=vals[(i-1)%F]),None)
    if start is None:raise ValueError('SINGLE_RUN')
    runs=[]
    for k in range(F):
        i=refs[(start+k)%F]
        if not runs or w[runs[-1][0]][0]!=w[i][0]:runs.append([i])
        else:runs[-1].append(i)
    if sum(len(r)%2 for r in runs)!=p or sum(len(r)%2==0 for r in runs)!=case['even_projected_runs']:
        raise ValueError('PROJECTION_PROFILE')
    block=case['identity_block_cyclic_indices']
    if len(block)!=4 or any(block[k+1]!=(block[k]+1)%N for k in range(3)):
        raise ValueError('BLOCK_INDICES')
    if [w[i][1] for i in block]!=[1,0,1,0] or w[block[0]][0]!=w[block[2]][0] or w[block[1]][0]!=w[block[3]][0]:
        raise ValueError('IDENTITY_BLOCK')
    if not any(block[0] in r and block[2] in r and len(r)%2 for r in runs):
        raise ValueError('BLOCK_NOT_ODD_PROJECTION')
    sel=case['selector']
    if len(sel)!=2*p or sel!=sorted(set(sel)) or not set(block).issubset(sel):raise ValueError('SELECTOR')
    order=[(block[-1]+1+k)%N for k in range(N)]
    rest=[i for i in order if i in sel and i not in block]
    if len(rest)!=2*p-4 or any(not w[i][1] for i in rest) or any(w[rest[k]][0]!=w[rest[k+1]][0] for k in range(0,len(rest),2)):
        raise ValueError('REMAINING_PAIRS')
    if product(w,sel,p)!=(0,0):raise ValueError('ORIGINAL_PRODUCT')
    return case['even_projected_runs']


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
    with open(args.input,'rb') as src:raw=src.read()
    data=json.loads(raw);counts={}
    for c in data['cases']:
        e=check(c);counts[str(e)]=counts.get(str(e),0)+1
    ex=data['cases'][0]
    controls=[mutate(ex,lambda c:c['selector'].__setitem__(1,c['selector'][0]),'SELECTOR'),
              mutate(ex,lambda c:c['word'][c['identity_block_cyclic_indices'][3]].__setitem__(0,
                     (c['word'][c['identity_block_cyclic_indices'][3]][0]+1)%c['p']),'IDENTITY_BLOCK')]
    result={'result':'PASS_INDEPENDENT_PROJECTION_IDENTITY4_EVEN','input_sha256':hashlib.sha256(raw).hexdigest(),
            'actual_words_and_selectors':len(data['cases']),'even_projection_run_counts':counts,
            'mutation_controls':controls,'scope':'finite projected even-run fixtures; no actual-block or residual theorem'}
    with open(args.output,'x',encoding='utf-8') as out:
        json.dump(result,out,sort_keys=True,indent=2);out.write('\n')
    print(json.dumps(result,sort_keys=True))


if __name__=='__main__':
    main()
