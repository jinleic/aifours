#!/usr/bin/env python3
"""Independently check cyclic actual identity-four and projected pair witnesses."""
import argparse
import copy
import hashlib
import json


def product(word,idx,p):
    x,e=0,0
    for i in idx:
        y,b=word[i]
        x=(x+((-1 if e else 1)*y))%p
        e ^= b
    return x,e


def projection_runs(word):
    refs=[i for i,(_,e) in enumerate(word) if e]
    vals=[word[i][0] for i in refs];F=len(refs)
    start=next((i for i in range(F) if vals[i]!=vals[(i-1)%F]),None)
    if start is None:return [refs]
    runs=[]
    for k in range(F):
        i=refs[(start+k)%F]
        if not runs or word[runs[-1][0]][0]!=word[i][0]:runs.append([i])
        else:runs[-1].append(i)
    return runs


def check(case):
    p,word=case['p'],case['word'];N=len(word)
    refs=[i for i,(_,e) in enumerate(word) if e]
    rot=[i for i,(_,e) in enumerate(word) if not e]
    if N!=4*p-1 or len(refs)!=3*p-2 or len(rot)!=p+1:
        raise ValueError('FULL_WORD_COUNTS')
    runs=projection_runs(word)
    if len(runs)!=p or any(len(r)%2==0 for r in runs):
        raise ValueError('PROJECTED_ODD_RUNS')
    block=case['identity_block_cyclic_indices']
    if len(block)!=4 or any(i<0 or i>=N for i in block) or any(block[k+1]!=(block[k]+1)%N for k in range(3)):
        raise ValueError('ACTUAL_BLOCK_POSITIONS')
    if [word[i][1] for i in block]!=[1,0,1,0] or word[block[0]][0]!=word[block[2]][0] or word[block[1]][0]!=word[block[3]][0]:
        raise ValueError('ACTUAL_IDENTITY_FOUR')
    containing=[run for run in runs if block[0] in run and block[2] in run]
    if len(containing)!=1 or len(containing[0])%2==0:
        raise ValueError('BLOCK_NOT_IN_ODD_PROJECTED_RUN')
    selector=case['selector']
    if len(selector)!=2*p or selector!=sorted(set(selector)) or not set(block).issubset(selector):
        raise ValueError('SELECTOR_INDICES')
    start=(block[-1]+1)%N
    order=[(start+k)%N for k in range(N)]
    rest=[i for i in order if i in selector and i not in block]
    if len(rest)!=2*p-4 or any(not word[i][1] for i in rest):
        raise ValueError('NONREFLECTION_REMAINDER')
    if any(word[rest[k]][0]!=word[rest[k+1]][0] for k in range(0,len(rest),2)):
        raise ValueError('REMAINDER_NOT_EQUAL_PAIRS')
    if product(word,block,p)!=(0,0) or product(word,selector,p)!=(0,0):
        raise ValueError('ACTUAL_PRODUCT')
    return block!=sorted(block)


def mutation(case,edit,expected):
    c=copy.deepcopy(case);edit(c)
    try:check(c)
    except ValueError as exc:
        if str(exc)==expected:return expected
        raise ValueError('MUTATION_WRONG: '+str(exc)) from exc
    raise ValueError('MUTATION_SURVIVED')


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input');parser.add_argument('--output',required=True);args=parser.parse_args()
    with open(args.input,'rb') as src:raw=src.read()
    data=json.loads(raw);cross=sum(check(c) for c in data['cases'])
    ex=data['cases'][0]
    controls=[
        mutation(ex,lambda c:c['selector'].__setitem__(1,c['selector'][0]),'SELECTOR_INDICES'),
        mutation(ex,lambda c:c['word'][c['identity_block_cyclic_indices'][3]].__setitem__(0,
                 (c['word'][c['identity_block_cyclic_indices'][3]][0]+1)%c['p']),'ACTUAL_IDENTITY_FOUR'),
    ]
    result={'result':'PASS_INDEPENDENT_PROJECTION_IDENTITY4','input_sha256':hashlib.sha256(raw).hexdigest(),
            'actual_words_and_selectors':len(data['cases']),'identity_blocks_crossing_original_start':cross,
            'intentional_controls_rejected':controls,
            'scope':'bounded projection-only premise and actual identity selectors; not L_RES closure'}
    with open(args.output,'x',encoding='utf-8') as out:
        json.dump(result,out,sort_keys=True,indent=2);out.write('\n')
    print(json.dumps(result,sort_keys=True))


if __name__=='__main__':
    main()
