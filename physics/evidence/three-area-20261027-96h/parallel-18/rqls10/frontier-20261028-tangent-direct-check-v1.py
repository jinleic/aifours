#!/usr/bin/env python3
"""Directly verify rational tangent vectors against actual QLS definitions.

Does not read generated tangent matrices or modular elimination outputs.
"""
from fractions import Fraction as F
from itertools import combinations
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent
cert=json.loads((ROOT/'frontier-20261028-parker-13ray-result-v1.json').read_text())['partial_witness']
A=cert['array']; L=cert['labels']; den=cert['denominator']; n=10
vec=[A[r][c] for r in range(n) for c in range(n)]
bs=[[n*r+c for c in range(n)] for r in range(n)]
bs += [[n*r+c for r in range(n)] for c in range(n)]
bs += [[n*r+c for r in range(n) for c in range(n) if L[r][c]==k] for k in range(n)]
assert len(bs)==30 and all(len(b)==n for b in bs)


def load(kind):
    p=ROOT/f'frontier-20261028-parker13-null-{kind}-rational-v1.json'
    data=json.loads(p.read_text())
    result=[]
    for item in data['vectors']:
        v=[F(0) for _ in range(n*n*n)]
        for i,num,dd in item['entries']:
            v[i]=F(num,dd)
        result.append((item['free_column'],v))
    return result


def inner(a,b): return sum(x*y for x,y in zip(a,b))


def check(kind,free,v):
    delta=[v[n*x:n*x+n] for x in range(n*n)]
    assert all(z==0 for x in range(n) for z in delta[x])
    if kind=='real':
        assert all(inner(vec[x],delta[x])==0 for x in range(n*n))
    else:
        assert all(inner(vec[x],delta[x])==0 for x in range(n,n*n))
        assert delta[77][7]==0 and delta[77][8]==0
    for block in bs:
        for x,y in combinations(block,2):
            if kind=='real':
                val=inner(delta[x],vec[y])+inner(vec[x],delta[y])
            else:
                val=inner(vec[x],delta[y])-inner(delta[x],vec[y])
            assert val==0, (kind,free,x,y,val)
    touched=[x for x in range(n*n) if any(delta[x])]
    print(kind,'free_column',free,'exact_30block_constraints PASS',
          'first_row_gauge PASS','touched_cells',len(touched))


real=load('real'); imag=load('imag')
assert len(real)==3 and len(imag)==1
for i,(free,v) in enumerate(real):
    assert all(v[other_free]==int(i==j) for j,(other_free,_) in enumerate(real))
    check('real',free,v)
for free,v in imag:
    assert v[free]==1
    check('imag',free,v)
print('independence: three real free coordinates form identity; imaginary vector nonzero')
print('PASS exact direct rational tangent/gauge checks; no nonlinear integration inferred')
