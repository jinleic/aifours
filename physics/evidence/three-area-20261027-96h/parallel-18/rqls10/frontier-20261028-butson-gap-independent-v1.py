#!/usr/bin/env python3
"""Verify exact strict bottleneck threshold without surd optimization.

For each 5-row subset, construct a graph of column pairs with
2|E|² < 5-sqrt(5). Its missing perfect matching proves the lower bound.
"""
from itertools import combinations
from functools import lru_cache
from collections import Counter

R=('0000000000','0123424130','0241332104','0314234012','0432120314',
   '0322301441','0204411323','0131043422','0013142243','0440213231')
base=tuple(tuple(map(int,row)) for row in R)


def weight(freq):
    square=sum(x*x for x in freq); p1=p2=0
    for i,j in combinations(range(5),2):
        if (j-i)%5 in (1,4):p1+=freq[i]*freq[j]
        else:p2+=freq[i]*freq[j]
    return (2*square-p1-p2,p1-p2)


allowed={(0,0),(10,-4)}
spectrum={(0,0),(5,-1),(5,1),(10,-4),(10,0),(10,4)}
for label,A in (('source',base),('transpose',tuple(tuple(base[j][i] for j in range(10)) for i in range(10)))):
    hist=Counter(); thresholdmax=Counter()
    for half in combinations(range(10),5):
        adj=[0]*10
        for i,j in combinations(range(10),2):
            freq=[0]*5
            for r in half:freq[(A[r][i]-A[r][j])%5]+=1
            w=weight(freq);hist[w]+=1
            assert w in spectrum
            if w in allowed:adj[i]|=1<<j;adj[j]|=1<<i
        @lru_cache(None)
        def match(mask):
            if not mask:return 0
            bit=mask&-mask;i=bit.bit_length()-1;remaining=mask^bit
            out=match(remaining);poss=adj[i]&remaining
            while poss:
                nxt=poss&-poss;poss-=nxt
                out=max(out,1+match(remaining^nxt))
            return out
        maximum=match((1<<10)-1)
        thresholdmax[maximum]+=1
        assert maximum<5
    assert hist=={(0,0):1440,(5,-1):3600,(5,1):3600,
                  (10,-4):900,(10,0):900,(10,4):900}
    print(label,'all11340 exact half-sum weights',dict(sorted(hist.items())))
    print(label,'strict-below-threshold matching maxima',dict(sorted(thresholdmax.items())),
          'no perfect matching PASS')
print('threshold proof uses 5-3sqrt(5)<0 and all other comparisons exact')
