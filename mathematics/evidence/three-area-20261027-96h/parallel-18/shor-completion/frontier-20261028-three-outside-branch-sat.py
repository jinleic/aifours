#!/usr/bin/env python3
"""Bounded n=16m double-saturated Shor branch with exactly three new atoms.

Requires actual-count consequences already proved in the companion note.
Each head-multiplicity case uses only linear seam-conservation constraints.
Solver UNSAT is not a formal certificate; UNKNOWN is not evidence of UNSAT.
"""
from collections import Counter
from itertools import combinations_with_replacement
import json
import sys
import z3

OLD_ROWS={0:(0,1,7,13,14),3:(0,2,4,6),8:(0,2,4,6),11:(0,1,2)}


def solve_case(n,even,odd,timeout_ms):
    m=n//16;q=4*m
    degrees={0:q-2,3:q,8:q,11:q-1,odd:1}
    for i in even:degrees[i]=degrees.get(i,0)+1
    heads=sorted(degrees)
    x={i:[z3.Bool(f'x_{n}_{even}_{odd}_{i}_{j}') for j in range(n)] for i in heads}
    s=z3.Solver();s.set(timeout=timeout_ms)
    for i,tails in OLD_ROWS.items():s.add(*[x[i][j] for j in tails])
    standard={16*k+j for k in range(m) for j in (0,2,4,6)}
    for i in (3,8):
        s.add(*[x[i][j] if j in standard else z3.Not(x[i][j]) for j in range(n)])
    for i in heads:s.add(z3.PbEq([(v,1) for v in x[i]],degrees[i]))
    # Each new head forces one optional old-row0 tail absent.
    for r in set(even):
        k=r//16-1;s.add(z3.Not(x[0][14+16*k]))
    h=(odd-11)//16;k=m-1-h;s.add(z3.Not(x[0][14+16*k]))
    for d in range(1,n//2+1):
        row=z3.Bool(f'r_{n}_{even[0]}_{even[1]}_{odd}_{d}')
        col=z3.Bool(f'c_{n}_{even[0]}_{even[1]}_{odd}_{d}')
        s.add(z3.Not(z3.And(row,col)))
        for i in heads:
            for j in range(n):s.add(z3.Implies(z3.And(x[i][j],x[i][(j+d)%n]),row))
        for h1 in heads:
            for h2 in heads:
                if (h2-h1)%n!=d:continue
                for j in range(n):s.add(z3.Implies(z3.And(x[h1][j],x[h2][j]),col))
    column=[z3.Sum([z3.If(x[i][j],1,0) for i in heads]) for j in range(n)]
    for g in range(n):s.add(z3.Sum([degrees[i]*column[(g-i)%n] for i in heads])==n)
    result=s.check();out={'even_heads':even,'odd_head':odd,'result':str(result)}
    if result==z3.unknown:out['reason']=s.reason_unknown()
    if result==z3.sat:
        model=s.model();pairs=[(i,j) for i in heads for j in range(n) if z3.is_true(model.eval(x[i][j]))]
        if len(pairs)!=n:raise AssertionError('bad layer count')
        keys=set();seams=Counter()
        for i,j in pairs:
            for k,l in pairs:
                key=(i,(j+k)%n,l)
                if key in keys:raise AssertionError('pair collision')
                keys.add(key);seams[key[1]]+=1
        if any(seams[g]!=n for g in range(n)):raise AssertionError('seam conservation failed')
        out['pairs']=pairs;out['directly_checked_paths']=len(keys)
    return out


def main(n,timeout_ms):
    if n not in (48,64,80) or not 1<=timeout_ms<=30000:
        raise ValueError('n in {48,64,80}; timeout 1..30000ms')
    m=n//16
    even=[16*h for h in range(2,m)]
    odd=[11+16*h for h in range(1,m-1)]
    cases=[solve_case(n,pair,o,timeout_ms) for pair in combinations_with_replacement(even,2) for o in odd]
    return {'n':n,'case_count':len(cases),'cases':cases,
            'scope':'conditional both-saturated N_out=3, 2-path constraints only; solver result not a formal proof'}


if __name__=='__main__':
    if len(sys.argv)!=3:raise SystemExit('usage: three-outside-branch-sat.py N TIMEOUT_MS')
    print(json.dumps(main(int(sys.argv[1]),int(sys.argv[2])),indent=2))
