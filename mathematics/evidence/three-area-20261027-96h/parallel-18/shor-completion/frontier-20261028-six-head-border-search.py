#!/usr/bin/env python3
"""Exact-cover search for |P|=6 Shor border factorizations at one order.

Complete coverage of 6-head candidates is proved only under the checked
v2(n) in {2,3}, v3(n)=1 conditions. A time cap yields INCOMPLETE, not UNSAT.
"""
from itertools import combinations
import json
import sys
import time

A={0,3,8,11}
Y={0,1,7,13,14}


def val(n,p):
    k=0
    while n%p==0:k+=1;n//=p
    return k


def search(n,seconds,node_cap):
    if not (26<=n<=3000 and val(n,2) in (2,3) and val(n,3)==1):
        raise ValueError('need n>=26, v2(n) in {2,3}, v3(n)=1')
    if not (0<seconds<=120 and 1<=node_cap<=100000):
        raise ValueError('invalid resource caps')
    stop=time.monotonic()+seconds
    full=(1<<n)-1
    vals=[i for i in range(n) if i%3==1 and i not in A]
    result={'n':n,'seconds_cap':seconds,'node_cap_per_candidate':node_cap,
            'tested_pairs':0,'anchor_collisions':0,'exhausted':0,'node_capped':0,
            'total_dfs_nodes':0,'status':'INCOMPLETE','factorization':None}
    for u,v in combinations(vals,2):
        if (u-v)%2==0:continue
        if time.monotonic()>=stop:return result
        result['tested_pairs']+=1
        P=A|{u,v}
        base=sum(1<<p for p in P)
        def tile(j):return ((base<<j)|(base>>(n-j)))&full
        initial=0;bad=False
        for y in Y:
            mask=tile(y)
            if initial&mask:bad=True;break
            initial|=mask
        if bad:
            result['anchor_collisions']+=1
            continue
        nodes=[0]
        def visit(mask,chosen):
            nodes[0]+=1
            if nodes[0]>node_cap or time.monotonic()>=stop:return None
            if mask==full:return chosen
            best=None
            missing=full^mask
            while missing:
                low=missing&-missing;missing-=low;target=low.bit_length()-1
                options=[(target-a)%n for a in P if not (mask&tile((target-a)%n))]
                if not options:return False
                if best is None or len(options)<len(best):best=options
                if len(best)==1:break
            for j in best:
                answer=visit(mask|tile(j),chosen+(j,))
                if answer is None:return None
                if answer is not False:return answer
            return False
        answer=visit(initial,tuple(sorted(Y)))
        result['total_dfs_nodes']+=nodes[0]
        if answer is None:
            result['node_capped']+=1
            if time.monotonic()>=stop:return result
        elif answer is False:
            result['exhausted']+=1
        else:
            Q=set(answer);sums=[(p+q)%n for p in P for q in Q]
            if len(P)!=6 or len(Q)!=n//6 or not A<=P or not Y<=Q or len(set(sums))!=n:
                raise AssertionError('invalid independently rechecked factorization')
            result['status']='SAT';result['factorization']={'P':sorted(P),'Q':sorted(Q)}
            return result
    result['status']='EXHAUSTED' if result['node_capped']==0 else 'INCOMPLETE'
    result['scope']='exact finite border-factorization search only; not general completion proof'
    return result


if __name__=='__main__':
    if len(sys.argv)!=4:raise SystemExit('usage: six-head-border-search.py N SECONDS NODE_CAP')
    print(json.dumps(search(int(sys.argv[1]),float(sys.argv[2]),int(sys.argv[3])),indent=2))
