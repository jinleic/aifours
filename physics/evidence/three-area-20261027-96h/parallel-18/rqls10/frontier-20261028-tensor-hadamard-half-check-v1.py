#!/usr/bin/env python3
"""Exact half-frame graphs of F2 tensor F5 under every row permutation."""
from itertools import combinations
from collections import Counter
from functools import lru_cache

p=5
rows=[(a,t) for a in range(2) for t in range(p)]
columns=[(h,b) for h in range(2) for b in range(p)]
hist=Counter()
for E in combinations(rows,p):
    adj=[0]*(2*p)
    for i,j in combinations(range(2*p),2):
        h,b=columns[i];hh,bb=columns[j];d=(bb-b)%p
        coeff=[sum(((-1)**(a*(hh-h))) for a,u in E if u==t) for t in range(p)]
        iszero=(sum(coeff)==0) if d==0 else len(set(coeff))==1
        if iszero:adj[i]|=1<<j;adj[j]|=1<<i
    @lru_cache(None)
    def match(mask):
        if not mask:return 0
        bit=mask&-mask;i=bit.bit_length()-1;rest=mask^bit
        best=match(rest);options=adj[i]&rest
        while options:
            b=options&-options;options-=b;best=max(best,1+match(rest^b))
        return best
    pure=len({a for a,t in E})==1
    oneper=len({t for a,t in E})==p
    kind='pure' if pure else ('mixed-one-per' if oneper else 'other')
    edges=sum(v.bit_count() for v in adj)//2
    maximum=match((1<<(2*p))-1)
    hist[(kind,edges,maximum)]+=1
assert hist=={('pure',40,5):2,('mixed-one-per',20,4):30,('other',0,0):220}
for key,value in sorted(hist.items()):print(key,'count',value)
print('all252 half choices; exact fifth-root balance; no quantum witness claimed')
