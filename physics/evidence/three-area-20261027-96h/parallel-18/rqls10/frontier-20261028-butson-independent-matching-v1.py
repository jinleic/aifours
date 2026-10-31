#!/usr/bin/env python3
"""Independent exact max-matching audit of all half-rows of explicit BH(10,5)."""
from collections import Counter
from functools import lru_cache
from itertools import combinations

# Independently transcribed from the same cited Appendix D phase table.
rows=('0000000000','0123424130','0241332104','0314234012','0432120314',
      '0322301441','0204411323','0131043422','0013142243','0440213231')
A=tuple(tuple(map(int,row)) for row in rows)
assert len(A)==10 and all(len(row)==10 for row in A)
for i,j in combinations(range(10),2):
    assert Counter((A[i][k]-A[j][k])%5 for k in range(10))==Counter({k:2 for k in range(5)})
    assert Counter((A[k][i]-A[k][j])%5 for k in range(10))==Counter({k:2 for k in range(5)})

hist=Counter()
for half in combinations(range(10),5):
    neighbors=[0]*10
    for i,j in combinations(range(10),2):
        if len({(A[t][i]-A[t][j])%5 for t in half})==5:
            neighbors[i]|=1<<j; neighbors[j]|=1<<i
    @lru_cache(None)
    def maxmatch(mask):
        if not mask:return 0
        bit=mask&-mask;i=bit.bit_length()-1
        remaining=mask^bit
        best=maxmatch(remaining)
        options=neighbors[i]&remaining
        while options:
            e=options&-options;options-=e
            best=max(best,1+maxmatch(remaining^e))
        return best
    edgecount=sum(mask.bit_count() for mask in neighbors)//2
    isolated=sum(mask==0 for mask in neighbors)
    maximum=maxmatch((1<<10)-1)
    hist[(edgecount,isolated,maximum)]+=1
    assert maximum<5
print('exact BH row/column exponent balance: PASS')
print('all252 half-row graphs independently audited by bitmask DP')
print('histogram (edges,isolated,max_matching) -> count:',dict(sorted(hist.items())))
print('perfect matchings:',sum(count for (edges,iso,maximum),count in hist.items() if maximum==5))
print('scope: this explicit K under all row permutations, not all BH(10,5) matrices')
