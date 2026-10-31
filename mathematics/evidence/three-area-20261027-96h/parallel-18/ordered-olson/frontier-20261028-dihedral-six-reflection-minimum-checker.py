#!/usr/bin/env python3
"""Check exact reflection-count minimum for one all-prime family."""
import argparse
import json


def product(word,indices,p):
    x,parity=0,0
    for i in sorted(indices):
        t,b=word[i]
        x=(x+(-t if parity else t))%p
        parity ^= b
    return x,parity


def check(p):
    refs=list(range(p+3))
    plus=list(range(p+3,p+3+2*p-1))
    minus=list(range(p+3+2*p-1,4*p-1))
    word=[[0,1]]*(p+3)+[[1,0]]*(2*p-1)+[[p-1,0]]*(p-3)
    if len(word)!=4*p-1 or len(refs)!=p+3 or len(plus)+len(minus)!=3*p-4:
        raise ValueError('wrong original counts')
    nonzero={}
    for refl_count in (0,2,4):
        nrot=2*p-refl_count
        low=max(0,nrot-len(plus))
        high=min(len(minus),nrot)
        checked=[]
        for q in range(low,high+1):
            idx=refs[:refl_count]+plus[:nrot-q]+minus[:q]
            value=product(word,idx,p)
            expected=((nrot-2*q)%p,0)
            if len(idx)!=2*p or value!=expected or value==(0,0):
                raise ValueError('smaller-reflection selection succeeds')
            checked.append(q)
        nonzero[str(refl_count)]=checked
    selector=sorted(refs[:6]+plus[:p-3]+minus[:p-3])
    if len(selector)!=2*p or len(set(selector))!=2*p or product(word,selector,p)!=(0,0):
        raise ValueError('six-reflection selector failed')
    mutated=sorted(selector[:-1])
    if len(mutated)==2*p:
        raise ValueError('selector-length mutation not detected')
    return {'p':p,'smaller_even_reflection_counts_checked':nonzero,
            'six_reflection_selector':selector,'all_reflection_pairs_signed_majority':2*p-1}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',required=True)
    args=parser.parse_args()
    result={'result':'PASS_MINIMUM_SIX_REFLECTIONS','instances':[check(p) for p in (5,7,11,13,17)],
            'scope':'all possible reflection-count / sign-count classes for five explicit words only'}
    with open(args.output,'x',encoding='utf-8') as out:
        json.dump(result,out,sort_keys=True,indent=2)
        out.write('\n')
    print(json.dumps(result,sort_keys=True))


if __name__=='__main__':
    main()
