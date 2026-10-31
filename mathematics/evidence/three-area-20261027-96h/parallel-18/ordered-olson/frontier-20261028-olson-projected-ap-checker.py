#!/usr/bin/env python3
"""Audit projected odd-run AP parity classes independently of word DP."""
import argparse
import copy
import hashlib
import itertools
import json


def check(case):
    p,labels,units=case['p'],case['labels'],case['units']
    if len(labels)!=p or len(units)!=p or sum(units)!=p-1 or any(u<0 for u in units):
        raise ValueError('PROJECTION_COUNTS')
    if set(labels)!=set(range(p)):
        raise ValueError('LABELS_NOT_PERMUTATION')
    d=(labels[1]-labels[0])%p
    if not d or any((labels[i+1]-labels[i])%p!=d for i in range(p-1)):
        raise ValueError('LABELS_NOT_AP')
    checked=0
    for t in range(2,p,2):
        for I in itertools.combinations(range(p),t):
            alt=sum((1 if k%2==0 else -1)*labels[j] for k,j in enumerate(I))%p
            if alt==0:raise ValueError('EVEN_ACTIVE_IDENTITY')
            checked+=1
    possible={(labels[i]-labels[j])%p for i,j in itertools.combinations(range(p),2)}
    if possible!=set(range(1,p)):
        raise ValueError('NONZERO_SUPPORT')
    mutation=case['nonAP_swap']
    if p>=5:
        if not mutation or len(mutation)!=2:raise ValueError('MUTATION_METADATA')
        a,b=mutation
        changed=labels[:];changed[a],changed[b]=changed[b],changed[a]
        four=next((I for I in itertools.combinations(range(p),4)
                  if (changed[I[0]]-changed[I[1]]+changed[I[2]]-changed[I[3]])%p==0),None)
        if four is None:raise ValueError('NONAP_NO_ZERO_FOUR')
    return checked


def mutation(case,edit,expected):
    c=copy.deepcopy(case)
    edit(c)
    try:check(c)
    except ValueError as exc:
        if str(exc)==expected:return expected
        raise ValueError('MUTATION_WRONG: '+str(exc)) from exc
    raise ValueError('MUTATION_SURVIVED')


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input');parser.add_argument('--output',required=True);args=parser.parse_args()
    with open(args.input,'rb') as src:raw=src.read()
    data=json.loads(raw)
    per=[check(c) for c in data['cases']]
    sample=next(c for c in data['cases'] if c['p']>=5)
    controls=[
        mutation(sample,lambda c:c['labels'].__setitem__(1,c['labels'][0]),'LABELS_NOT_PERMUTATION'),
        mutation(sample,lambda c:c['units'].__setitem__(0,c['units'][0]+1),'PROJECTION_COUNTS'),
    ]
    result={'result':'PASS_INDEPENDENT_PROJECTED_AP_PARITY_AUDIT','input_sha256':hashlib.sha256(raw).hexdigest(),
            'projection_cases':len(per),'even_active_run_subsets_checked':sum(per),
            'nonAP_mutations_with_zero_four':sum(c['nonAP_swap'] is not None for c in data['cases']),
            'intentional_controls_rejected':controls,
            'scope':'bounded projection-only cases; no actual-block or residual claim'}
    with open(args.output,'x',encoding='utf-8') as out:
        json.dump(result,out,sort_keys=True,indent=2);out.write('\n')
    print(json.dumps(result,sort_keys=True))


if __name__=='__main__':
    main()
