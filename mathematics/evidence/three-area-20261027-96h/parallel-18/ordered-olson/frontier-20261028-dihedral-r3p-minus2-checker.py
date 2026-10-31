#!/usr/bin/env python3
"""Independently check R=3p-2 pair selectors and separated-gap words."""
import argparse
from collections import Counter
import copy
import hashlib
import itertools
import json


def product(word,indices,p):
    x,b=0,0
    for k in indices:
        t,e=word[k]
        x=(x+((-t)%p if b else t))%p
        b^=e
    return x,b


def check_pair(word,p,record):
    i,j=record['reflections']
    if not (0<=i<j<len(word) and word[i][1] and word[j][1]):
        raise ValueError('invalid reflection positions')
    signed={k:(-x if i<k<j else x)%p for k,(x,b) in enumerate(word) if not b}
    M=max(Counter(signed.values()).values())
    if record['max_signed_multiplicity']!=M or record['eligible']!=(M<=2*p-1):
        raise ValueError('wrong signed eligibility')
    if not record['eligible']:
        return False
    pairs=record['pairs']
    fixed=record['fixed_omission']
    omitted=record['omitted']
    selected=record['selector']
    flat=[k for pair in pairs for k in pair]
    if len(pairs)!=p-1 or len(set(flat))!=2*(p-1) or any(k not in signed for k in flat):
        raise ValueError('invalid unequal pair positions')
    if any(signed[u]==signed[v] for u,v in pairs):
        raise ValueError('pair signed values equal')
    if fixed not in signed or fixed in flat:
        raise ValueError('fixed omission not outside pairs')
    if len(set(omitted))!=p or fixed not in omitted or any(len(set(pair).intersection(omitted))!=1 for pair in pairs):
        raise ValueError('incorrect actual omissions')
    if len(selected)!=2*p or selected!=sorted(set(selected)) or any(k<0 or k>=len(word) for k in selected):
        raise ValueError('bad selector indices')
    if set(selected)!=(set(signed)-set(omitted)) | {i,j}:
        raise ValueError('selected complement mismatch')
    sums={signed[fixed]}
    for u,v in pairs:
        sums={(z+signed[k])%p for z in sums for k in (u,v)}
    if len(sums)!=p:
        raise ValueError('omission support not full')
    if product(word,selected,p)!=(0,0):
        raise ValueError('actual original product not identity')
    return True


def check_case(case):
    p,word=case['p'],case['word']
    if len(word)!=4*p-1 or sum(b==0 for _,b in word)!=3*p-2 or any(a<0 or a>=p or b not in (0,1) for a,b in word):
        raise ValueError('wrong full original word')
    refs=[k for k,(_,b) in enumerate(word) if b]
    expected=[list(pair) for pair in itertools.combinations(refs,2)]
    if [r['reflections'] for r in case['pairs']]!=expected:
        raise ValueError('incomplete pair coverage')
    return sum(check_pair(word,p,r) for r in case['pairs'])


def check_family(case):
    p,word=case['p'],case['word']
    refs=[i for i,(_,b) in enumerate(word) if b]
    ys=[word[i][0] for i in refs]
    expected=[[1,0]]*(p-2)+[[ys[0],1]]+[[1,0]]*(p+1)+[[ys[1],1]]
    expected += [v for y in ys[2:] for v in ([p-1,0],[y,1])]
    if word!=expected:
        raise ValueError('separated-gap family mismatch')
    by_pair={tuple(r['reflections']):r for r in case['pairs']}
    if any(by_pair[(i,j)]['eligible'] for i,j in zip(refs,refs[1:])):
        raise ValueError('consecutive-pair threshold unexpectedly succeeds')
    if not by_pair[(refs[0],refs[-1])]['eligible']:
        raise ValueError('endpoint pair threshold fails')
    return True


def mutation(case,edit,expected):
    altered=copy.deepcopy(case)
    row=next(r for r in altered['pairs'] if r['eligible'])
    edit(row)
    try:
        check_pair(altered['word'],altered['p'],row)
    except ValueError as exc:
        if str(exc)==expected:
            return expected
        raise ValueError('mutation rejected for unintended reason: '+str(exc)) from exc
    raise ValueError('mutation survived')


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input')
    parser.add_argument('--output',required=True)
    args=parser.parse_args()
    with open(args.input,'rb') as source:
        raw=source.read()
    data=json.loads(raw)
    random=[check_case(c) for c in data['cases']]
    structured=[check_case(c) for c in data['structured']]
    for case in data['structured']:
        check_family(case)
    sample=data['structured'][0]
    controls=[
        mutation(sample,lambda r:r['selector'].__setitem__(1,r['selector'][0]),'bad selector indices'),
        mutation(sample,lambda r:r['pairs'][0].__setitem__(1,r['pairs'][0][0]),'invalid unequal pair positions'),
        mutation(sample,lambda r:r.__setitem__('fixed_omission',r['pairs'][0][0]),'fixed omission not outside pairs'),
    ]
    total=sum(len(c['pairs']) for c in data['cases'])
    result={'result':'PASS_INDEPENDENT_R3P_MINUS2_CHECK','input_sha256':hashlib.sha256(raw).hexdigest(),
            'random_words_checked':len(random),'random_reflection_pairs_checked':total,
            'random_original_selectors_verified':sum(random),'ineligible_pairs_not_decided':total-sum(random),
            'structured_words_checked':len(structured),'structured_selectors_verified':sum(structured),
            'all_structured_consecutive_pairs_ineligible_endpoint_eligible':True,
            'mutation_controls_rejected_for_intended_reasons':controls,
            'scope':'bounded actual words; does not itself establish all-word contradiction proof'}
    with open(args.output,'x',encoding='utf-8') as out:
        json.dump(result,out,sort_keys=True,indent=2)
        out.write('\n')
    print(json.dumps(result,sort_keys=True))


if __name__=='__main__':
    main()
