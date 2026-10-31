#!/usr/bin/env python3
"""Exact diagnostic of a REF-failing high-surplus affine-core expansion.

This is NOT a full L_RES witness/counterexample: old GEN/IPGEN/OLD caller
membership is deliberately not asserted. The two contiguous identity-four
head blocks make such historical coverage plausible and require a separate
source correspondence before any residual claim.
"""
import argparse
from collections import Counter
from fractions import Fraction
from itertools import combinations
import json


def product(word,indices,p):
    x,e=0,0
    for i in indices:
        y,b=word[i];x=(x+(-y if e else y))%p;e^=b
    return x,e


def family(p):
    word=[[0,1],[-1%p,1],[-1%p,1],[0,1],[1,1],[2,1],[2,1],[1,1]]
    L=2*p-9;z=[];r=[]
    z.append(len(word));word.append([0,1]);r.append(len(word));word.append([1,0])
    for _ in range(L-1):z.append(len(word));word.append([0,1])
    r.append(len(word));word.append([1,0])
    for k in range(1,p):word.extend([[(-k)%p,1],[1,0]])
    sel=list(range(8))+z[:2*p-10]+r
    return word,sorted(sel)


def matching(edges):
    def path(es):
        a,b=0,0
        for e in es:a,b=max(a,b),a+1 if e else -999999
        return max(a,b)
    n=len(edges);a=path(edges[:-1])
    return max(a,1+path(edges[1:n-2])) if edges[-1] else a


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--output',required=True);args=parser.parse_args()
    head=[0,-1,-1,0,1,2,2,1];bounds={}
    for k in range(9):
        values=[sum(head[i]*(1 if j%2==0 else -1) for j,i in enumerate(q)) for q in combinations(range(8),k)]
        lo,hi=min(values),max(values);t=9-k
        if not (lo+(t+1)//2>=1 and hi<=t//2):raise ValueError('HEAD_BOUND')
        bounds[str(k)]=[lo,hi]
    results=[]
    for p in (7,11,13,17,19,23,29):
        word,sel=family(p);N=len(word);refs=[i for i,(_,e) in enumerate(word) if e]
        if N!=4*p-1 or len(refs)!=3*p-2 or sum(e==0 for _,e in word)!=p+1:raise ValueError('COUNTS')
        if any(not word[(i+1)%N][1] for i,(_,e) in enumerate(word) if not e):raise ValueError('SINGLETON')
        if len(sel)!=2*p or len(set(sel))!=2*p or product(word,sel,p)!=(0,0):raise ValueError('SELECTOR')
        # independent element-count DP for the complete reflection-only 2p product support
        dp=[set() for _ in range(2*p+1)];dp[0].add(0)
        for i in refs:
            y=word[i][0]
            for k in range(2*p-1,-1,-1):
                if dp[k]:dp[k+1].update((x+(y if k%2==0 else -y))%p for x in tuple(dp[k]))
        if 0 in dp[2*p]:raise ValueError('REF_EXISTS')
        # maximal cyclic reflection-only runs
        vals=[word[i][0] for i in refs];F=len(vals)
        cut=next(k for k in range(F) if vals[k]!=vals[k-1]);runs=[]
        for k in range(F):
            v=vals[(cut+k)%F]
            if not runs or runs[-1][0]!=v:runs.append([v,1])
            else:runs[-1][1]+=1
        o=sum(L%2 for _,L in runs);e=len(runs)-o
        if (o,e)!=(p+4,2):raise ValueError('PROJECTION_PROFILE')
        edges=[vals[k]!=vals[(k+1)%F] or (refs[(k+1)%F]-refs[k])%N!=1 for k in range(F)]
        nu=matching(edges)
        if nu!=(p+9)//2 or sum(edges)!=p+7:raise ValueError('RAW_GRAPH')
        if p>=17 and nu>p-3:raise ValueError('LOW_RAW')
        if max(Counter(vals).values())!=2*p-7:raise ValueError('MULTIPLICITY')
        results.append({'p':p,'F':F,'R':p+1,'o_projection':o,'e_projection':e,'raw_edges':sum(edges),
                        'raw_matching':nu,'low_matching':nu<=p-3,'reflection_2p_support':sorted(dp[2*p]),
                        'word':word,'selector':sel,'selector_product':[0,0]})
    out={'result':'PASS_HIGH_SURPLUS_AFFINE_CORE_FAMILY','head_bounds':bounds,'cases':results,
         'scope':'REF-failing base family and exact mixed selector, not full L_RES membership'}
    with open(args.output,'x',encoding='utf-8') as dst:json.dump(out,dst,sort_keys=True,indent=2);dst.write('\n')
    print(json.dumps({'result':out['result'],'primes':[r['p'] for r in results],
                      'low_matching_primes':[r['p'] for r in results if r['low_matching']]},sort_keys=True))


if __name__=='__main__':main()
