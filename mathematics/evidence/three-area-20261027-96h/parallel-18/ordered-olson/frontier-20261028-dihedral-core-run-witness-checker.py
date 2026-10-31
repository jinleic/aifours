#!/usr/bin/env python3
"""Exercise exceptional-core four-reflection branch on actual words."""
import argparse
import itertools
import json


def product(word,indices,p):
    exponent,parity=0,0
    for i in sorted(indices):
        x,b=word[i]
        exponent=(exponent+(-x if parity else x))%p
        parity ^= b
    return exponent,parity


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',required=True)
    args=parser.parse_args()
    checked=[]
    for p in (3,5,7,11,13):
        a=1
        word=[[a,0]]*(2*p-1)+[[0,1]]*(p+2)+[[p-1,0]]*(p-2)
        core=list(range(2*p-1))
        refs=list(range(2*p-1,3*p+1))
        extras=list(range(3*p+1,4*p-1))
        if len(word)!=4*p-1 or len(refs)!=p+2 or len(extras)!=p-2:
            raise ValueError('wrong family length')
        # Any two-reflection selector has k extras and 2p-2-k core
        # rotations; all chosen rotations are outside the reflection block.
        distinct=set()
        for k in range(p-1):
            indices=core[:2*p-2-k]+refs[:2]+extras[:k]
            value=product(word,indices,p)
            expected=((-2*(k+1))%p,0)
            if len(indices)!=2*p or value!=expected or value==(0,0):
                raise ValueError('two-reflection support mismatch')
            distinct.add(value[0])
        if len(distinct)!=p-1:
            raise ValueError('missing-value count incorrect')
        # With four equal reflections choose p-2 of each rotation value.
        four=core[:p-2]+refs[:4]+extras
        if len(four)!=2*p or len(set(four))!=2*p or product(word,four,p)!=(0,0):
            raise ValueError('four-reflection original selector fails')
        if any((sum((-2)%p for k in range(p-2) if mask>>k&1))%p==0 for mask in range(1,1<<(p-2))):
            raise ValueError('extra difference sequence not zero-sum-free')
        checked.append({'p':p,'reflection_pairs':len(list(itertools.combinations(refs,2))),
                        'two_reflection_distinct_nonzero_products':len(distinct),
                        'four_reflection_selector':sorted(four)})
    result={'result':'PASS_EXCEPTIONAL_FOUR_REFLECTION_FAMILY',
            'actual_words':checked,'scope':'five exact instances of one written all-prime family'}
    with open(args.output,'x',encoding='utf-8') as out:
        json.dump(result,out,indent=2,sort_keys=True)
        out.write('\n')
    print(json.dumps(result,sort_keys=True))


if __name__=='__main__':
    main()
