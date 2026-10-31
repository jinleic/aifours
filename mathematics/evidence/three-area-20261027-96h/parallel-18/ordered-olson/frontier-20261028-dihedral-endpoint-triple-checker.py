#!/usr/bin/env python3
"""Independently inspect full words and endpoint/triple selectors."""
import argparse
from collections import Counter
import copy
import hashlib
import json


def direct(word,indices,p):
    state=(0,0)
    for i in indices:
        a,b=state
        c,d=word[i]
        state=((a+((-c)%p if b else c))%p, b^d)
    return state


def verify(case):
    p,word,a=case['p'],case['word'],case['a']
    if len(word)!=4*p-1 or not 1<=a<p or any(x<0 or x>=p or b not in (0,1) for x,b in word):
        raise ValueError('invalid original word')
    rotations=[i for i,(_,b) in enumerate(word) if not b]
    refs=[i for i,(_,b) in enumerate(word) if b]
    if len(rotations)!=3*p-3 or len(refs)!=p+2:
        raise ValueError('wrong original type counts')
    triple=case['triple_ordinal']
    if not 0<=triple<=len(refs)-3:
        raise ValueError('wrong triple ordinal')
    tri=refs[triple:triple+3]
    if tri!=list(range(tri[0],tri[0]+3)) or len({word[i][0] for i in tri})!=1:
        raise ValueError('triple not contiguous and equal')
    first,last=refs[0],refs[-1]
    if case['endpoint_values']!=[word[first][0],word[last][0]]:
        raise ValueError('endpoint value mismatch')
    values=Counter(word[k][0] for k in rotations)
    if values[a]!=2*p-1 or values[(-a)%p]!=p-2 or len(values)!=2:
        raise ValueError('not the two-exponent core')
    if any(word[k][0]!=a for k in rotations if k<first or k>last):
        raise ValueError('noncore rotation outside endpoints')
    if sum(k<first or k>last for k in rotations)!=case['outer_core']:
        raise ValueError('outer-core count mismatch')
    bigs=[]
    for j,(u,v) in enumerate(zip(refs,refs[1:])):
        gap=word[u+1:v]
        if j in (triple,triple+1):
            if gap:
                raise ValueError('nonempty triple gap')
        elif len(gap)>=p+1:
            if any(entry!=[a,0] for entry in gap):
                raise ValueError('large gap contains noncore occurrence')
            bigs.append((j,len(gap)))
        elif len(gap)==1:
            if gap[0]!=[(-a)%p,0]:
                raise ValueError('wrong singleton extra')
        elif len(gap)==2:
            if sorted(x for x,_ in gap)!=sorted([a,(-a)%p]):
                raise ValueError('wrong balanced gap')
        else:
            raise ValueError('gap outside written normal form')
    if bigs!=[(case['big_ordinal'],case['big_count'])]:
        raise ValueError('large-gap mismatch')
    plus=[]
    minus=[]
    for k in rotations:
        v=(-word[k][0] if first<k<last else word[k][0])%p
        (plus if v==a else minus).append(k)
    n=p-2
    if len(plus)<n or len(minus)<n or len(plus)+len(minus)!=len(rotations):
        raise ValueError('endpoint signed-count premise fails')
    qlo=max(0,2*p-2-len(minus))
    qhi=min(len(plus),2*p-2)
    support={(2*q-(2*p-2))*a%p for q in range(qlo,qhi+1)}
    if min(len(plus),len(minus))>=p-1 and len(support)!=p:
        raise ValueError('two-reflection full-support implication failed')
    if min(len(plus),len(minus))==p-2 and (len(support)!=p-1 or 0 in support):
        raise ValueError('two-reflection nonzero-support implication failed')
    selected=case['selected_indices']
    if len(selected)!=2*p or selected!=sorted(set(selected)) or any(i<0 or i>=len(word) for i in selected):
        raise ValueError('selector indices not distinct original occurrences')
    selected_refs=[i for i in selected if word[i][1]]
    if case['mode']=='two_reflections':
        if selected_refs!=[first,last]:
            raise ValueError('wrong two-reflection selection')
    elif case['mode']=='four_reflections':
        extra=[i for i in selected_refs if i not in (first,last)]
        if len(selected_refs)!=4 or first not in selected_refs or last not in selected_refs or len(extra)!=2 or any(i not in tri for i in extra):
            raise ValueError('wrong endpoint/triple reflection selection')
        if word[first][0]!=word[last][0]:
            raise ValueError('four-reflection branch requires equal endpoints')
    else:
        raise ValueError('unknown selector mode')
    if direct(word,selected,p)!=(0,0):
        raise ValueError('original product not identity')
    return ('outer' if case['outer_core'] else 'no_outer')+'/'+case['mode']


def mutation(case,edit,expected):
    item=copy.deepcopy(case)
    edit(item)
    try:
        verify(item)
    except ValueError as exc:
        if str(exc)==expected:
            return str(exc)
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
    groups=Counter(verify(case) for case in data['cases'])
    example=data['cases'][0]
    controls=[
        mutation(example,lambda c:c['selected_indices'].__setitem__(1,c['selected_indices'][0]),
                 'selector indices not distinct original occurrences'),
        mutation(example,lambda c:c.__setitem__('big_count',c['big_count']+1),
                 'large-gap mismatch'),
        mutation(example,lambda c:c['endpoint_values'].__setitem__(0,(c['endpoint_values'][0]+1)%c['p']),
                 'endpoint value mismatch'),
    ]
    result={'result':'PASS_INDEPENDENT_ENDPOINT_TRIPLE_CHECK',
            'input_sha256':hashlib.sha256(raw).hexdigest(),
            'actual_words_checked':len(data['cases']),'verified_selector_branches':dict(groups),
            'mutation_controls_rejected_for_intended_reasons':controls,
            'scope':'actual bounded normal-form words only; not the all-word reduction proof'}
    with open(args.output,'x',encoding='utf-8') as output:
        json.dump(result,output,sort_keys=True,indent=2)
        output.write('\n')
    print(json.dumps(result,sort_keys=True))


if __name__=='__main__':
    main()
