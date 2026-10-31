#!/usr/bin/env python3
"""Memoized finite search for p+2 distinct-adjacent labels avoiding ordered zero quadruples."""
import argparse
import functools
import json


def rotate(mask,shift,p):
    shift%=p
    full=(1<<p)-1
    return ((mask<<shift)|(mask>>(p-shift)))&full if shift else mask


def search(p):
    target=p+2
    visits=0
    @functools.lru_cache(None)
    def rec(length,last,seen,pairs,triples):
        nonlocal visits
        visits+=1
        if length==target:
            return ()
        for y in range(p):
            if y==last or triples>>y&1:
                continue
            addpairs=0
            for x in range(p):
                if seen>>x&1:
                    addpairs |= 1<<((x-y)%p)
            result=rec(length+1,y,seen|(1<<y),pairs|addpairs,triples|rotate(pairs,y,p))
            if result is not None:
                return (y,)+result
        return None
    result=rec(1,0,1,0,0)
    return {'p':p,'normalized_first_label':0,'target_length':target,
            'visited_states':visits,'no_witness_found':result is None,
            'first_avoiding_label_sequence':None if result is None else [0]+list(result)}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--p',type=int,required=True)
    parser.add_argument('--output',required=True)
    args=parser.parse_args()
    result=search(args.p)
    result['scope']='finite source-unreviewed label-avoidance search, NOT a universal theorem'
    with open(args.output,'x',encoding='utf-8') as out:
        json.dump(result,out,sort_keys=True,indent=2)
        out.write('\n')
    print(json.dumps(result,sort_keys=True))


if __name__=='__main__':
    main()
