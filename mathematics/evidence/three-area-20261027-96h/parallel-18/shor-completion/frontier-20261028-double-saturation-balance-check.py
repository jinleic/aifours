#!/usr/bin/env python3
"""Bounded integer checks for the Shor double-saturation Fourier dichotomy."""
from collections import Counter
import json
import sys

OLD={(0,j) for j in (0,1,7,13,14)}
OLD|={(i,j) for i in (3,8) for j in (0,2,4,6)}
OLD|={(11,j) for j in (0,1,2)}


def check(n):
    if n<32 or n%16:raise ValueError('n must be multiple16 and at least32')
    m=n//16; standard={16*k+j for k in range(m) for j in (0,2,4,6)}
    pairs=OLD|{(i,j) for i in (3,8) for j in standard}
    if sum(i in (3,8) for i,j in pairs)!=8*m:
        raise AssertionError('saturated rows wrong size')
    C=Counter(j%16 for i,j in pairs)
    lower=sum(C[r] for r in (0,2,4,6))
    outside=n-8*m
    if lower!=8*m+3 or lower<=outside:
        raise AssertionError('opposite-tail contradiction not strict')
    # Φ_16 tail-balance would force this many atoms in 8,10,12,14,
    # all outside the two standard rows; actual completions remain unknown.
    possible=[]
    for even_new in range(4):
        odd_new=3-even_new
        row0=4*m-even_new; row11=4*m-odd_new
        if row0<=4*m-2 and row11<=4*m-1 and row0>=5 and row11>=3:
            possible.append((even_new,odd_new,row0,row11))
    if possible!=[(2,1,4*m-2,4*m-1)]:
        raise AssertionError(('unexpected N_out=3 distribution',n,possible))
    return {'n':n,'two_saturated_row_atoms':8*m,
            'tail_balance_required_outside_at_least':lower,
            'available_outside_two_rows':outside,
            'N_out_3_even_odd':possible[0][:2]}


if __name__=='__main__':
    if len(sys.argv)!=2:raise SystemExit('usage: double-saturation-balance-check.py MAX_N')
    limit=int(sys.argv[1])
    if not 32<=limit<=10000:raise SystemExit('require32<=MAX_N<=10000')
    samples=[32,48,64,128,2640]
    if limit<2640:samples=[n for n in samples if n<=limit]
    for n in range(32,limit+1,16):check(n)
    print(json.dumps({'checked_orders':len(range(32,limit+1,16)),
                      'samples':[check(n) for n in samples],
                      'scope':'integer lower-bound checks; no physical completion'},indent=2))
