#!/usr/bin/env python3
"""Exact FD / atom-count check for a negative original-graph J1 example."""
from collections import Counter
from itertools import combinations
from pathlib import Path
import json

OUT=Path(__file__).with_name('frontier-20261028-diamond-ingleton-witness-result.json')
N={1:(2,3,4,5,6,7),2:(1,3,7,9,10),3:(1,2,4,8,9),4:(1,3,5,8,10),
   5:(1,4,6,9,10),6:(1,5,7,8,9),7:(1,2,6,8,10),8:(3,4,6,7,9,10),
   9:(2,3,5,6,8),10:(2,4,5,7,8)}
WORDS=(0,6,3,15);WEIGHTS=(2,1,1,2)


def main():
    for x,y in combinations(WORDS,2):
        d=x^y
        if any((d>>(v-1))&1 and all(not ((d>>(u-1))&1) for u in N[v]) for v in range(1,11)):
            raise ValueError(('FD',x,y))
    def bits(w,*vs):return tuple((w>>(v-1))&1 for v in vs)
    cd=Counter();ab=Counter();single={v:Counter() for v in range(1,11)}
    for w,n in zip(WORDS,WEIGHTS):
        cd[bits(w,1,3)]+=n;ab[bits(w,2,4)]+=n
        for v in range(1,11):single[v][bits(w,v)[0]]+=n
    if cd!={(0,0):2,(0,1):1,(1,0):1,(1,1):2}:raise ValueError('CD_DISTRIBUTION')
    if ab!={(0,0):2,(1,0):2,(1,1):2}:raise ValueError('AB_DISTRIBUTION')
    if single[1]!={0:3,1:3} or single[3]!={0:3,1:3}:raise ValueError('MAX_ENTROPY')
    if any(single[v].get(1,0) for v in range(5,11)):raise ValueError('CONDITIONING_NOT_CONSTANT')
    if not 9**8>2**25 or not 69>56:raise ValueError('EXACT_INEQUALITY')
    out={'words':WORDS,'probability_numerators':WEIGHTS,'denominator':6,
         'FD_pair_vertex_checks':60,'CD_counts':{''.join(map(str,k)):v for k,v in cd.items()},
         'AB_counts':{''.join(map(str,k)):v for k,v in ab.items()},
         'conditioning_vertices_5_to_10_constant':True,
         'J1_exact':'3 - 2 log2(3) = log2(8/9)',
         'max_singleton_entropy_bits':1,'strict_J1_less_than_minus_one_eighth':True,
         'comparison_9_pow_8':9**8,'comparison_2_pow_25':2**25,
         'limits':'A local J1 counterexample only: the graph-automorphism average can have a different sign; no guessing-number gain is claimed.'}
    with OUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
