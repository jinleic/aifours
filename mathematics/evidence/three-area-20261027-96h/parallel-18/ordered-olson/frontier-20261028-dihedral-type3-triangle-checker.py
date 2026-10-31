#!/usr/bin/env python3
"""Independently check saved type-III words, triangles, and selectors."""
import argparse
from collections import Counter
import copy
import hashlib
import itertools
import json


def multiply(word,idx,p):
    state=(0,0)
    for i in idx:
        x,b=state
        y,c=word[i]
        state=((x+(-y if b else y))%p,b^c)
    return state


def check(case):
    p,word=case['p'],case['word']
    if len(word)!=4*p-1 or any(x<0 or x>=p or b not in (0,1) for x,b in word):
        raise ValueError('wrong original word')
    refs=[i for i,(_,b) in enumerate(word) if b]
    rotations=[i for i,(_,b) in enumerate(word) if not b]
    counts=Counter(word[i][0] for i in rotations)
    if len(refs)!=p+3 or counts!={1:2*p-3,p-1:p-1}:
        raise ValueError('wrong raw type-III counts')
    prefix=0
    actual={}
    for i,(x,b) in enumerate(word):
        if b:
            actual[i]=prefix
        else:
            prefix+=1 if x==1 else -1
    tri=case['triangle_indices']
    if len(tri)!=3 or tri!=sorted(set(tri)) or any(i not in actual for i in tri):
        raise ValueError('invalid triangle indices')
    if case['prefix_triangle']!=[actual[i] for i in tri]:
        raise ValueError('prefix metadata mismatch')
    totals=[]
    for i,j in itertools.combinations(tri,2):
        u=actual[j]-actual[i]
        signed=[(-word[k][0] if i<k<j else word[k][0])%p for k in rotations]
        c=Counter(signed)
        if not (-1<=u<=p-1) or max(c.values())>2*p-2:
            raise ValueError('triangle pair not low-majority')
        if len(c)!=2 or min(c.values())<p-2:
            raise ValueError('triangle pair not two-support')
        totals.append(sum(signed)%p)
    raw=sum(word[k][0] for k in rotations)%p
    if raw!=(-2)%p or (totals[0]+totals[2]-totals[1])%p!=raw:
        raise ValueError('triangle cocycle mismatch')
    pair=case['selected_pair']
    if pair not in [list(x) for x in itertools.combinations(tri,2)]:
        raise ValueError('selected pair outside triangle')
    selector=case['selector']
    if len(selector)!=2*p or selector!=sorted(set(selector)) or any(i<0 or i>=len(word) for i in selector):
        raise ValueError('bad actual selector indices')
    if [i for i in selector if word[i][1]]!=pair:
        raise ValueError('selector reflections mismatch')
    if multiply(word,selector,p)!=(0,0):
        raise ValueError('actual original product nonidentity')
    return True


def check_saturated(case):
    p,word=case['p'],case['word']
    refs=[word[i] for i,(_,b) in enumerate(word) if b]
    h=(p-1)//2
    left=case['label']['left_blocks']
    cursor=0
    def two():
        nonlocal cursor
        out=refs[cursor:cursor+2]
        cursor+=2
        return out
    expected=two()
    for _ in range(left):
        expected += [[p-1,0]]*2+two()
    expected += [[1,0]]*p+two()
    for _ in range(h-left):
        expected += [[p-1,0]]*2+two()
    expected += [[1,0]]*(p-3)
    if expected!=word or cursor!=p+3:
        raise ValueError('saturated-window fixture mismatch')


def negative(case,edit,expected):
    altered=copy.deepcopy(case)
    edit(altered)
    try:
        check(altered)
    except ValueError as exc:
        if str(exc)==expected:
            return expected
        raise ValueError('mutation rejected for wrong reason: '+str(exc)) from exc
    raise ValueError('mutation survived')


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input')
    parser.add_argument('--output',required=True)
    args=parser.parse_args()
    with open(args.input,'rb') as source:
        raw=source.read()
    data=json.loads(raw)
    for case in data['random_cases']+data['saturated_cases']:
        check(case)
    for case in data['saturated_cases']:
        check_saturated(case)
    example=data['random_cases'][0]
    controls=[
        negative(example,lambda c:c['selector'].__setitem__(1,c['selector'][0]),'bad actual selector indices'),
        negative(example,lambda c:c['prefix_triangle'].__setitem__(0,c['prefix_triangle'][0]+1),'prefix metadata mismatch'),
        negative(example,lambda c:c['triangle_indices'].__setitem__(1,c['triangle_indices'][0]),'invalid triangle indices'),
    ]
    result={'result':'PASS_INDEPENDENT_TYPE3_TRIANGLE_CHECK','input_sha256':hashlib.sha256(raw).hexdigest(),
            'random_original_words_and_selectors':len(data['random_cases']),
            'saturated_window_original_words_and_selectors':len(data['saturated_cases']),
            'mutation_controls_rejected_for_intended_reasons':controls,
            'scope':'bounded actual words; not a proof of the universal prefix triangle lemma'}
    with open(args.output,'x',encoding='utf-8') as out:
        json.dump(result,out,sort_keys=True,indent=2)
        out.write('\n')
    print(json.dumps(result,sort_keys=True))


if __name__=='__main__':
    main()
