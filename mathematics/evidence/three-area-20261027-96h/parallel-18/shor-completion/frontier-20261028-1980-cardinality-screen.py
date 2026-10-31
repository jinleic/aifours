#!/usr/bin/env python3
"""Exact scalar screen for the n1980 direct-border cardinalities."""
from itertools import combinations
from math import gcd
import json
n=1980;A={0,3,8,11};Y={0,1,7,13,14}
GY={gcd(a-b,n) for a,b in combinations(Y,2)}
C={x for x in range(n) if all(x==a or gcd(x-a,n) not in GY for a in A)}
assert len(C)==158 and sum(x%5==2 for x in C)==8 and sum(x%11==1 for x in C)==8
D=[d for d in range(7,len(C)+1) if n%d==0]
filtered=[d for d in D if not(d%5==0 and d//5>8) and not(d%11==0 and (d//11>8 or d==11))]
assert filtered==[9,10,12,15,18,20,22,30,33,36,44,66]
remaining=[d for d in filtered if d not in {9,10,12,15,20,36,44}]
assert remaining==[18,22,30,33,66]
print(json.dumps({'P_candidate_count':len(C),'initial_divisors':D,'prime_filtered':filtered,
 'remaining_after_named_separate_exclusions':remaining,'scope':'numeric sieve, not exclusion proofs'},indent=2))
