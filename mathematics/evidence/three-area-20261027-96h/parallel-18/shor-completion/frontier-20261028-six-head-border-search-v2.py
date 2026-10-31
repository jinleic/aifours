#!/usr/bin/env python3
"""Indexed, resource-bounded exact-cover search for Shor P6 border tilings.

Only orders with v2 in {2,3} and v3=1 are in scope. A chunk result is not a
global verdict, and capped candidates remain explicit UNKNOWNs.
"""
from itertools import combinations
import json
import sys
import time

A={0,3,8,11}
Y={0,1,7,13,14}


def valuation(n,p):
    k=0
    while n%p==0:k+=1;n//=p
    return k


def search(n,start,end,seconds,node_cap):
    if not (26<=n<=3000 and valuation(n,2) in (2,3) and valuation(n,3)==1):
        raise ValueError('unsupported order valuations')
    if not (0<seconds<=120 and 1<=node_cap<=1000000):raise ValueError('invalid limits')
    values=[i for i in range(n) if i%3==1 and i not in A]
    pairs=[(u,v) for u,v in combinations(values,2) if (u-v)%2]
    if not (0<=start<=end<=len(pairs)):raise ValueError('bad chunk')
    stop=time.monotonic()+seconds;full=(1<<n)-1
    out={'n':n,'all_pairs':len(pairs),'start':start,'end':end,'next_index':start,
         'seconds_cap':seconds,'node_cap':node_cap,'anchor_collisions':0,
         'exhausted':0,'unknown_cases':[],'dfs_nodes':0,'status':'INCOMPLETE'}
    for index in range(start,end):
        if time.monotonic()>=stop:return out
        u,v=pairs[index];P=A|{u,v};base=sum(1<<p for p in P)
        def tile(j):return ((base<<j)|(base>>(n-j)))&full
        mask=0;collision=False
        for y in Y:
            z=tile(y)
            if mask&z:collision=True;break
            mask|=z
        if collision:
            out['anchor_collisions']+=1;out['next_index']=index+1;continue
        nodes=[0]
        def visit(covered,chosen):
            nodes[0]+=1
            if nodes[0]>node_cap or time.monotonic()>=stop:return None
            if covered==full:return chosen
            best=None;missing=full^covered
            while missing:
                low=missing&-missing;missing-=low;target=low.bit_length()-1
                opts=[(target-a)%n for a in P if not covered&tile((target-a)%n)]
                if not opts:return False
                if best is None or len(opts)<len(best):best=opts
                if len(best)==1:break
            for j in best:
                answer=visit(covered|tile(j),chosen+(j,))
                if answer is None:return None
                if answer is not False:return answer
            return False
        answer=visit(mask,tuple(sorted(Y)));out['dfs_nodes']+=nodes[0]
        if answer is None:
            out['unknown_cases'].append({'index':index,'P':sorted(P),'nodes':nodes[0]})
            out['next_index']=index+1
            if time.monotonic()>=stop:return out
        elif answer is False:
            out['exhausted']+=1;out['next_index']=index+1
        else:
            Q=set(answer);sums={(p+q)%n for p in P for q in Q}
            if len(P)!=6 or len(Q)!=n//6 or not A<=P or not Y<=Q or len(sums)!=n:
                raise AssertionError('invalid SAT witness')
            out['status']='SAT';out['factorization']={'P':sorted(P),'Q':sorted(Q)}
            out['next_index']=index+1;return out
    out['status']='CHUNK_EXHAUSTED' if not out['unknown_cases'] else 'CHUNK_WITH_UNKNOWNS'
    return out


if __name__=='__main__':
    if len(sys.argv)!=6:raise SystemExit('usage: search-v2.py N START END SECONDS NODE_CAP')
    print(json.dumps(search(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]),
                            float(sys.argv[4]),int(sys.argv[5])),indent=2))
