#!/usr/bin/env python3
"""Exact two-support missing-value checks and original triple witnesses."""
import argparse
from collections import Counter
import itertools
import json


def product(word,indices,p):
    x,parity=0,0
    for i in sorted(indices):
        a,b=word[i]
        x=(x+(-a if parity else a))%p
        parity^=b
    return x,parity


def all_count_formulas(p):
    R=3*p-4
    checked=0
    for m in range(p-2,2*p-1):
        n=R-m
        for x in range(p):
            for y in range(p):
                if x==y:
                    continue
                qlo=max(0,2*p-2-m)
                qhi=min(n,2*p-2)
                actual={((2*p-2-q)*x+q*y)%p for q in range(qlo,qhi+1)}
                missing=((m+1)*x+(n+1)*y)%p
                if actual!=set(range(p))-{missing}:
                    raise ValueError('two-support formula failed')
                if (missing+1)%p not in actual:
                    raise ValueError('mutated missing-value control failed')
                checked+=1
    return checked


def actual_family(p):
    checked=0
    branches=Counter()
    for y1,y2,y3 in itertools.product(range(p),repeat=3):
        word=[[1,0]]*(2*p-5)+[[p-1,0]]*(p-3)+[[y1,1], [1,0],[p-1,0],
                [y2,1],[1,0],[p-1,0],[y3,1]]+[[0,1]]*p
        rotations=[i for i,(_,b) in enumerate(word) if not b]
        refs=[i for i,(_,b) in enumerate(word) if b]
        if len(word)!=4*p-1 or len(rotations)!=3*p-4 or len(refs)!=p+3:
            raise ValueError('family counts incorrect')
        T=sum(word[k][0] for k in rotations)%p
        missing=[]
        for u,v in itertools.combinations(refs[:3],2):
            signed={k:(-word[k][0] if u<k<v else word[k][0])%p for k in rotations}
            count=Counter(signed.values())
            if set(count)!={1,p-1} or count[1]!=2*p-3 or count[p-1]!=p-1:
                raise ValueError('balanced gap signed counts incorrect')
            missing.append(((u,v),(sum(signed.values())+1+(p-1))%p,signed))
        if (missing[0][1]+missing[2][1]-missing[1][1])%p!=T or T==0:
            raise ValueError('nonzero cocycle identity failed')
        chosen=next(((u,v,mu,signed) for (u,v),mu,signed in missing
                     if (word[v][0]-word[u][0])%p != mu),None)
        if chosen is None:
            raise ValueError('nonzero cocycle failed to force pair')
        u,v,mu,signed=chosen
        plus=[k for k,x in signed.items() if x==1]
        minus=[k for k,x in signed.items() if x==p-1]
        target=(word[v][0]-word[u][0])%p
        selected=None
        for q in range(2*p-1):
            other=2*p-2-q
            if q<=len(plus) and other<=len(minus) and (q-other)%p==target:
                selected=sorted(plus[:q]+minus[:other]+[u,v])
                break
        if selected is None or len(selected)!=2*p or len(set(selected))!=2*p or product(word,selected,p)!=(0,0):
            raise ValueError('actual increasing-index witness failed')
        checked+=1
        branches[f'{refs.index(u)}-{refs.index(v)}']+=1
    return checked,dict(branches)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',required=True)
    args=parser.parse_args()
    instances={}
    for p in (5,7,11,13):
        count=all_count_formulas(p)
        actual,branches=actual_family(p)
        instances[str(p)]={'distinct_value_count_formulas':count,'actual_full_words_and_selectors':actual,
                           'selected_reflection_pair_ordinal_counts':branches}
    result={'result':'PASS_TWO_SUPPORT_COCYCLE_EXACT','instances':instances,
            'scope':'finite arithmetic and one explicit full-word family, not a proof of all words'}
    with open(args.output,'x',encoding='utf-8') as out:
        json.dump(result,out,sort_keys=True,indent=2)
        out.write('\n')
    print(json.dumps(result,sort_keys=True))


if __name__=='__main__':
    main()
