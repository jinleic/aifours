#!/usr/bin/env python3
"""Exact finite search: 7 q-th roots with squared sum magnitude 8.

Tests one overlap equation only, NOT a full QLS or a general nonexistence proof.
Cyclotomic polynomials and remainders use integer arithmetic.
"""
from itertools import combinations_with_replacement
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent


def trim(p):
    while len(p)>1 and p[-1]==0: p.pop()
    return p


def div_monic(a,b):
    a=a[:]; q=[0]*max(1,len(a)-len(b)+1)
    while len(a)>=len(b) and a!=[0]:
        k=len(a)-len(b); value=a[-1]; q[k]=value
        for j,x in enumerate(b): a[j+k]-=value*x
        trim(a)
    return trim(q),trim(a)


def cyclotomic(n):
    known={}
    for d in range(1,n+1):
        if n%d: continue
        q=[-1]+[0]*(d-1)+[1]
        for e in sorted(known):
            if d%e==0:
                q,rem=div_monic(q,known[e]); assert rem==[0]
        known[d]=q
    return known[n]


def is_solution(terms,q,phi):
    counts=[0]*q
    for a in terms:
        for b in terms:
            counts[(a-b)%q]+=1
    counts[0]-=8
    _,rem=div_monic(trim(counts),phi)
    return rem==[0]


def main():
    results=[]
    for q in (2,3,4,5,6,7,8,9,10,12,15):
        phi=cyclotomic(q)
        checked=solutions=0
        first=None
        for terms in combinations_with_replacement(range(q),7):
            checked+=1
            if is_solution(terms,q,phi):
                solutions+=1
                if first is None: first=list(terms)
        result={'q':q,'phi_coefficients_low_to_high':phi,
                'multisets_checked':checked,'solutions':solutions,'first':first}
        results.append(result)
        print('q',q,'multisets',checked,'solutions',solutions,'first',first,flush=True)
    assert is_solution((0,0,0,3,3,4,8),12,cyclotomic(12))
    print('explicit q=12 S=1+1+i+i+(1+zeta3+zeta3²)=2+2i: PASS',flush=True)
    out=ROOT/'frontier-20261028-cyclotomic-seven-sums-result-v1.json'
    out.write_text(json.dumps({'results':results,
        'caveat':'one-pair phase equation only, not a 100-ray construction'},indent=2,sort_keys=True)+'\n')
    print('wrote',out.name,flush=True)


if __name__=='__main__': main()
