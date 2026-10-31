#!/usr/bin/env python3
"""Independent exact exhaustive BH(10,5) half-frame obstruction checker.

Builds dephased candidate rows by deduplicating all 9! permutations, uses
Python integer bitsets and a matching DP, independently of the C++ search.
At timeout, reports partial counts and never claims exhaustive completion.
"""
import argparse
from collections import Counter
from functools import lru_cache
from itertools import permutations
from pathlib import Path
import json
import time

ROOT=Path(__file__).resolve().parent
SECOND=(0,0,1,1,2,2,3,3,4,4)
ZERO=(0,)*10

def balanced(a,b):
    counts=[0]*5
    for x,y in zip(a,b):counts[(x-y)%5]+=1
    return counts==[2]*5


def perfect(E):
    adj=[0]*10
    for i in range(10):
        for j in range(i+1,10):
            if len({(row[i]-row[j])%5 for row in E})==5:
                adj[i]|=1<<j;adj[j]|=1<<i
    @lru_cache(None)
    def solve(mask):
        if not mask:return True
        bit=mask&-mask;i=bit.bit_length()-1;rest=mask^bit
        options=adj[i]&rest
        while options:
            b=options&-options;options-=b
            if solve(rest^b):return True
        return False
    return solve((1<<10)-1),sum(x==0 for x in adj)


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--seconds',type=float,default=50);args=parser.parse_args()
    start=time.monotonic()
    tails=sorted(set(permutations((0,1,1,2,2,3,3,4,4))))
    assert len(tails)==22680
    rows=[(0,)+tail for tail in tails if balanced((0,)+tail,SECOND)]
    assert len(rows)==1075
    adj=[0]*len(rows); edges=0
    for i in range(len(rows)):
        for j in range(i+1,len(rows)):
            if balanced(rows[i],rows[j]):
                adj[i]|=1<<j;adj[j]|=1<<i;edges+=1
    print('independent row candidates',len(rows),'compatibility edges',edges,flush=True)
    triples=common5=matched=0;isolated=Counter();first=None;timedout=False
    for i in range(len(rows)):
        js=adj[i] & ~((1<<(i+1))-1)
        while js:
            bit=js&-js;js-=bit;j=bit.bit_length()-1
            ks=adj[i]&adj[j]&~((1<<(j+1))-1)
            while ks:
                b=ks&-ks;ks-=b;k=b.bit_length()-1
                triples+=1
                if triples%1024==0 and time.monotonic()-start>=args.seconds:
                    timedout=True;break
                common=adj[i]&adj[j]&adj[k]
                if common.bit_count()<5:continue
                common5+=1
                ok,isolates=perfect((ZERO,SECOND,rows[i],rows[j],rows[k]))
                isolated[isolates]+=1
                if ok:
                    matched+=1
                    if first is None:first=[rows[i],rows[j],rows[k]]
            if timedout:break
        if timedout:break
    elapsed=time.monotonic()-start
    result={'rows':len(rows),'edges':edges,'triples_examined':triples,
            'triples_with_at_least5_common_neighbors':common5,
            'half_frames_with_perfect_matching':matched,'first_matching_triple':first,
            'isolated_vertex_histogram':dict(isolated),'timed_out':timedout,
            'elapsed_seconds':elapsed,
            'scope':'dephased BH10,5 necessary 5-row half-frame; not general QLS'}
    out=ROOT/'frontier-20261028-bh10-half-independent-result-v1.json'
    out.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print('triples',triples,'common5',common5,'halfmatch',matched,
          'isolates',dict(sorted(isolated.items())),'timed_out',timedout,'elapsed',round(elapsed,3),flush=True)
    print('wrote',out.name,flush=True)


if __name__=='__main__':main()
