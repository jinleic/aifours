#!/usr/bin/env python3
"""Check exact threshold-gap matching for K, K^T and all fifth-root Galois powers."""
from itertools import combinations
from functools import lru_cache
from collections import Counter

ROWS=('0000000000','0123424130','0241332104','0314234012','0432120314',
      '0322301441','0204411323','0131043422','0013142243','0440213231')
BASE=tuple(tuple(map(int,row)) for row in ROWS)


def weight(freq):
    squares=sum(x*x for x in freq);p1=p2=0
    for i,j in combinations(range(5),2):
        if (j-i)%5 in (1,4):p1+=freq[i]*freq[j]
        else:p2+=freq[i]*freq[j]
    return (2*squares-p1-p2,p1-p2)


for orient,orig in (('source',BASE),('transpose',tuple(tuple(BASE[j][i] for j in range(10)) for i in range(10)))):
    for power in (1,2,3,4):
        A=tuple(tuple(power*x%5 for x in row) for row in orig)
        maxima=Counter()
        for half in combinations(range(10),5):
            adj=[0]*10
            for i,j in combinations(range(10),2):
                freq=[0]*5
                for t in half:freq[(A[t][i]-A[t][j])%5]+=1
                w=weight(freq)
                assert w in {(0,0),(5,-1),(5,1),(10,-4),(10,0),(10,4)}
                if w in {(0,0),(10,-4)}:
                    adj[i]|=1<<j;adj[j]|=1<<i
            @lru_cache(None)
            def match(mask):
                if not mask:return 0
                bit=mask&-mask;i=bit.bit_length()-1;rest=mask^bit
                best=match(rest);options=adj[i]&rest
                while options:
                    nxt=options&-options;options-=nxt
                    best=max(best,1+match(rest^nxt))
                return best
            maximum=match((1<<10)-1);maxima[maximum]+=1
        assert maxima=={4:252},(orient,power,maxima)
        print(orient,'Galois exponent',power,'all252 half threshold graph max matching4: PASS')
print('threshold (5-sqrt5)/50 follows only after the written original-vector caller')
