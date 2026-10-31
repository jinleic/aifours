#!/usr/bin/env python3
"""Audit actual cyclic run selectors and finite ordered-four lemmas."""
import argparse
from collections import Counter
import copy
import hashlib
import itertools
import json


def product(word,idx,p):
    x,b=0,0
    for i in idx:
        y,c=word[i]
        x=(x+(-y if b else y))%p
        b^=c
    return x,b


def four(values,p):
    return next((t for t in itertools.combinations(range(len(values)),4)
                 if (values[t[0]]-values[t[1]]+values[t[2]]-values[t[3]])%p==0),None)


def check(case):
    p,word=case['p'],case['word']
    refs=[i for i,(_,b) in enumerate(word) if b]
    rotations=[i for i,(_,b) in enumerate(word) if not b]
    if len(word)!=4*p-1 or len(refs)!=3*p-2 or len(rotations)!=p+1 or any(word[i][0]==0 for i in rotations):
        raise ValueError('wrong original counts')
    if refs[0]!=0 or any(j-i-1>1 for i,j in zip(refs,refs[1:])) or len(word)-1-refs[-1]>1:
        raise ValueError('cyclic singleton-gap failure')
    vals=[word[i][0] for i in refs]
    F=len(refs)
    start=next((i for i in range(F) if vals[i]!=vals[(i-1)%F]),None)
    if start is None:
        raise ValueError('single constant reflection run')
    ordered=[refs[(start+i)%F] for i in range(F)]
    runs=[]
    for index in ordered:
        if not runs or word[runs[-1][0]][0]!=word[index][0]:
            runs.append([index])
        else:
            runs[-1].append(index)
    odd=[r for r in runs if len(r)%2]
    even=[r for r in runs if len(r)%2==0]
    if len(odd)!=p+2 or len(even)!=case['even_runs'] or len(even)>1:
        raise ValueError('wrong odd/even cyclic run counts')
    labels=[word[r[0]][0] for r in odd]
    eq=sum(labels[i]==labels[(i+1)%len(labels)] for i in range(len(labels)))
    if eq>1 or (case['forced_equal_across_even'] and eq!=1):
        raise ValueError('wrong cyclic odd-label equality count')
    selector=case['selector']
    if len(selector)!=2*p or selector!=sorted(set(selector)) or any(i not in refs for i in selector):
        raise ValueError('bad original reflection selector')
    chosen=set(selector)
    chosen_odd=[word[r[0]][0] for r in runs if sum(i in chosen for i in r)%2]
    if len(chosen_odd)!=4 or (chosen_odd[0]-chosen_odd[1]+chosen_odd[2]-chosen_odd[3])%p!=0:
        raise ValueError('wrong selected odd-run quadruple')
    if product(word,selector,p)!=(0,0):
        raise ValueError('actual original product nonidentity')
    return f'e{len(even)}/odd-equalities{eq}'


def audit_four_lemma(p):
    total=0
    for ds in itertools.product(range(1,p),repeat=p+1):
        values=[0]
        for d in ds:
            values.append((values[-1]+d)%p)
        if four(values,p) is None:
            raise ValueError('finite adjacent-distinct ordered-four lemma false')
        total+=1
    return total


def audit_crossing_extension(p):
    total=0
    for a in range(p):
        for b in range(p):
            if a==b:
                continue
            x=(2*a-b)%p
            for pattern in ([a,b,a,b],[b,a,b,a]):
                for position in range(5):
                    values=pattern[:position]+[x]+pattern[position:]
                    if four(values,p) is None:
                        raise ValueError('crossing-pair extension witness false')
                    total+=1
    for positions in itertools.combinations(range(5),3):
        values=[0 if i in positions else 1 for i in range(5)]
        if four(values,p) is None:
            raise ValueError('triple plus double lemma false')
    return total


def mutation(case,edit,expected):
    c=copy.deepcopy(case)
    edit(c)
    try:
        check(c)
    except ValueError as exc:
        if str(exc)==expected:
            return expected
        raise ValueError('mutation wrong failure: '+str(exc)) from exc
    raise ValueError('mutation survived')


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input')
    parser.add_argument('--output',required=True)
    args=parser.parse_args()
    with open(args.input,'rb') as source:
        raw=source.read()
    data=json.loads(raw)
    branches=Counter(check(c) for c in data['cases'])
    sample=data['cases'][0]
    controls=[
        mutation(sample,lambda c:c['selector'].__setitem__(1,c['selector'][0]),'bad original reflection selector'),
        mutation(sample,lambda c:c.__setitem__('even_runs',1-c['even_runs']),'wrong odd/even cyclic run counts'),
    ]
    result={'result':'PASS_INDEPENDENT_ODD_RUN_BOUNDARY_CHECK','input_sha256':hashlib.sha256(raw).hexdigest(),
            'actual_original_words_and_selectors':len(data['cases']),'branches':dict(branches),
            'exhaustive_normalized_adjacent_distinct_label_lists':{str(p):audit_four_lemma(p) for p in (3,5)},
            'crossing_extension_insertion_cases':{str(p):audit_crossing_extension(p) for p in (3,5,7)},
            'mutation_controls_rejected_for_intended_reasons':controls,
            'scope':'bounded actual words and finite ordered-four instances; not complete L_RES'}
    with open(args.output,'x',encoding='utf-8') as out:
        json.dump(result,out,sort_keys=True,indent=2)
        out.write('\n')
    print(json.dumps(result,sort_keys=True))


if __name__=='__main__':
    main()
