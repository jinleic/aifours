#!/usr/bin/env python3
"""Independent phase-table transcription, half graph and matching check.

Checks both source BH(10,5) and its transpose without importing producer code.
"""
from collections import Counter
from functools import lru_cache
from itertools import combinations

ROWS=('0000000000','0123424130','0241332104','0314234012','0432120314',
      '0322301441','0204411323','0131043422','0013142243','0440213231')
M=tuple(tuple(int(c) for c in row) for row in ROWS)
for label,A in (('source',M),('transpose',tuple(tuple(M[j][i] for j in range(10)) for i in range(10)))):
    for i,j in combinations(range(10),2):
        assert sorted((A[i][t]-A[j][t])%5 for t in range(10))==[0,0,1,1,2,2,3,3,4,4]
        assert sorted((A[t][i]-A[t][j])%5 for t in range(10))==[0,0,1,1,2,2,3,3,4,4]
    hist=Counter()
    for E in combinations(range(10),5):
        adjacency=[0]*10
        for c,d in combinations(range(10),2):
            freq=[0]*5
            for t in E:freq[(A[t][c]-A[t][d])%5]+=1
            if freq==[1]*5:
                adjacency[c]|=1<<d;adjacency[d]|=1<<c
        @lru_cache(None)
        def matching(mask):
            if mask==0:return 0
            u=mask&-mask; c=u.bit_length()-1; rest=mask^u
            best=matching(rest); opts=adjacency[c]&rest
            while opts:
                v=opts&-opts;opts-=v
                best=max(best,1+matching(rest^v))
            return best
        edges=sum(x.bit_count() for x in adjacency)//2
        isolated=sum(x==0 for x in adjacency)
        mx=matching((1<<10)-1)
        hist[(edges,isolated,mx)]+=1
    assert hist=={(4,2,4):50,(6,1,4):200,(20,0,4):2}
    print(label,'BH exact PASS; 252 half graphs (edges,isolated,maxmatch):',dict(sorted(hist.items())))
    print(label,'perfect matchings 0; all physical implications still require written caller')
