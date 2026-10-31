#!/usr/bin/env python3
"""Independently audit reflection-turn matchings on full original words."""
import argparse
from collections import Counter
import copy
import hashlib
import json


def product(word,idx,p):
    x,b=0,0
    for i in idx:
        y,c=word[i]
        x=(x+((-1 if b else 1)*y))%p
        b^=c
    return x,b


def matching_data(values,matching,p):
    pairs=[tuple(pair) for pair in matching]
    if any(j!=i+1 or i<0 or j>=len(values) or values[i]==values[j] for i,j in pairs):
        raise ValueError('bad nonzero adjacent reflection matching')
    flat=[k for pair in pairs for k in pair]
    if len(set(flat))!=len(flat):
        raise ValueError('overlapping reflection matching')
    starts={i:j for i,j in pairs}
    blocks=[]
    i=0
    while i<len(values):
        if i in starts:
            blocks.append((i,starts[i]))
            i=starts[i]+1
        else:
            blocks.append((i,))
            i+=1
    if len(blocks)!=2*p:
        raise ValueError('wrong reflection block count')
    C=0
    sums={0}
    for k,block in enumerate(blocks):
        sign=1 if k%2==0 else -1
        if len(block)==1:
            C+=2*sign*values[block[0]]
            sums={(v+sign*values[block[0]])%p for v in sums}
        else:
            C+=sign*(values[block[0]]+values[block[1]])
            sums={(v+sign*values[t])%p for v in sums for t in block}
    if len(sums)<p-1:
        raise ValueError('reflection swap support too small')
    if 0 not in sums and (len(sums)!=p-1 or C%p!=0):
        raise ValueError('missing-zero midpoint implication failed')
    return C%p,sums,blocks


def check(case):
    p,word=case['p'],case['word']
    if len(word)!=4*p-1 or any(x<0 or x>=p or b not in (0,1) for x,b in word):
        raise ValueError('invalid original word')
    refs=[i for i,(_,b) in enumerate(word) if b]
    rot=[i for i,(_,b) in enumerate(word) if not b]
    if len(refs)!=3*p-2 or len(rot)!=p+1 or any(word[i][0]==0 for i in rot):
        raise ValueError('wrong zero-free original counts')
    if refs[0]!=0 or any(j-i-1>1 for i,j in zip(refs,refs[1:])) or len(word)-1-refs[-1]>1:
        raise ValueError('cyclic reflection gaps not singleton')
    values=[word[i][0] for i in refs]
    steps=[(y-x)%p for x,y in zip(values,values[1:])]
    if sum(d==0 for d in steps)>(p-1)//2:
        raise ValueError('too many equal consecutive reflections')
    sel=case['selector']
    if len(sel)!=2*p or sel!=sorted(set(sel)) or any(i not in refs for i in sel):
        raise ValueError('bad reflection-only selector indices')
    details=case['details']
    if details['mode']=='constant-step':
        if not steps or steps[0]==0 or any(d!=steps[0] for d in steps) or details['step']!=steps[0]:
            raise ValueError('constant-step mismatch')
        if sel!=refs[:2*p]:
            raise ValueError('wrong constant-step selector')
    elif details['mode']=='turn-flip':
        t=details['turn_ordinal']
        if not 0<=t<len(steps)-1 or not steps[t] or not steps[t+1] or steps[t]==steps[t+1]:
            raise ValueError('not a nonzero turn')
        common=[tuple(pair) for pair in details['common_pairs']]
        if len(common)!=p-3 or any(any(v in (t,t+1,t+2) for v in pair) for pair in common):
            raise ValueError('bad external matching')
        M1=sorted(common+[(t,t+1)])
        M2=sorted(common+[(t+1,t+2)])
        if details['matchings']!=[[list(pair) for pair in M1],[list(pair) for pair in M2]]:
            raise ValueError('matching flip metadata mismatch')
        c1,S1,B1=matching_data(values,M1,p)
        c2,S2,B2=matching_data(values,M2,p)
        if details['double_midpoints']!=[c1,c2] or details['support_sizes']!=[len(S1),len(S2)]:
            raise ValueError('midpoint or support metadata mismatch')
        before=t-sum(j<t for _,j in common)
        expected=((-1 if before%2 else 1)*(steps[t]-steps[t+1]))%p
        if (c1-c2)%p!=expected or expected==0 or not (0 in S1 or 0 in S2):
            raise ValueError('actual midpoint flip implication failed')
        chosen=details['chosen_matching']
        if chosen not in (0,1):
            raise ValueError('bad chosen matching')
        blocks=(B1,B2)[chosen]
        sel_ord={refs.index(i) for i in sel}
        if any(len(sel_ord.intersection(block))!=1 for block in blocks):
            raise ValueError('selector not one per reflection block')
    else:
        raise ValueError('unknown proof branch')
    if product(word,sel,p)!=(0,0):
        raise ValueError('actual original reflection product nonidentity')
    return details['mode']


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
    sample=next(c for c in data['cases'] if c['details']['mode']=='turn-flip')
    controls=[
        mutation(sample,lambda c:c['selector'].__setitem__(1,c['selector'][0]),'bad reflection-only selector indices'),
        mutation(sample,lambda c:c['details']['double_midpoints'].__setitem__(0,(c['details']['double_midpoints'][0]+1)%c['p']),'midpoint or support metadata mismatch'),
        mutation(sample,lambda c:c['details'].__setitem__('turn_ordinal',-1),'not a nonzero turn'),
    ]
    result={'result':'PASS_INDEPENDENT_REFLECTION_TURN_CHECK','input_sha256':hashlib.sha256(raw).hexdigest(),
            'actual_full_words_and_reflection_selectors':len(data['cases']),'branches':dict(branches),
            'skipped_patterns_not_decided':data['skipped'],'mutation_controls_rejected_for_intended_reasons':controls,
            'scope':'bounded actual words, not an all-prime proof or residual realization'}
    with open(args.output,'x',encoding='utf-8') as out:
        json.dump(result,out,sort_keys=True,indent=2)
        out.write('\n')
    print(json.dumps(result,sort_keys=True))


if __name__=='__main__':
    main()
