#!/usr/bin/env python3
"""Exact binary Gaussian ranks of every selected-factor vertex projection."""
from pathlib import Path
import json

OUT=Path(__file__).resolve().parent/'frontier-20261028-binary-projection-rank-check-result.json'
TRI=((1,2,3),(1,4,5),(1,6,7),(2,3,9),(2,7,10),(3,8,9),(4,5,10),(4,8,10),(5,6,9),(6,7,8))
CASES=((1,2,5,6,8,9),(1,3,4,6,7,10),(2,3,4,6,7,10),(2,3,5,6,9,10))

def rank(rows):
    basis={}
    for x in rows:
        while x:
            k=x.bit_length()-1
            if k in basis:x^=basis[k]
            else:basis[k]=x;break
    return len(basis)

def check(case,mutation=False):
    bits={v:[] for v in range(1,11)}
    for j,t in enumerate(case):
        T=TRI[t-1]
        for v,row in zip(T,(1<<(2*j),1<<(2*j+1),(1<<(2*j))|(1<<(2*j+1)))):bits[v].append(row)
    if mutation:bits[TRI[case[0]-1][2]][0]=0
    ranks=[]
    for A in range(1024):
        rows=[x for v in range(1,11) if A>>(v-1)&1 for x in bits[v]]
        actual=rank(rows);formula=sum(min(sum(bool(A>>(v-1)&1) for v in TRI[t-1]),2) for t in case)
        if actual!=formula:raise ValueError('PROJECTION_RANK')
        ranks.append(actual)
    return {'factors':case,'projections':1024,'all_rank_increments':5120,'full_rank':ranks[-1]}


def main():
    cases=[check(c) for c in CASES]
    try:check(CASES[0],True)
    except ValueError as e:control=str(e)
    else:raise ValueError('MUTATION_ACCEPTED')
    out={'all_checked':True,'cases':cases,'negative_control':control,
         'limits':'Exact binary matrix projection ranks. Conditional entropy fiber bound follows from the separately written affine-linear argument, not from numerical LP status.'}
    with OUT.open('x',encoding='utf-8') as f:json.dump(out,f,indent=2);f.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
