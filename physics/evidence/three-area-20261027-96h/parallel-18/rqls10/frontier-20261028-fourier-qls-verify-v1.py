#!/usr/bin/env python3
"""Independently verify any Fourier-graph result against original QLS(10).

Exact root sums are reduced modulo the independently constructed Phi_10.
No author/search-side table of root coefficients is imported.
"""
import importlib.util
import json
from itertools import combinations
from pathlib import Path

ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('cy',ROOT/'frontier-20261028-cyclotomic-seven-sums-v1.py')
cy=importlib.util.module_from_spec(spec); spec.loader.exec_module(cy)
D=json.loads((ROOT/'frontier-20261028-fourier-graph-result-v1.json').read_text())
if not D['found']:
    print('no candidate recorded; no QLS witness to verify')
    raise SystemExit(0)
n=10; mu=D['mu']; pi=D['pi']
assert len(mu)==len(pi)==n and set(mu)==set(pi)==set(range(n))
L=[[(c-pi[r])%n for c in range(n)] for r in range(n)]
assert all(set(row)==set(range(n)) for row in L)
assert all({L[r][c] for r in range(n)}==set(range(n)) for c in range(n))
phi=cy.cyclotomic(n)
assert phi==[1,-1,1,-1,1]


def exponent(r,c,t): return (r*t+c*mu[t])%n


def zero_inner(x,y):
    r,c=x; s,d=y
    counts=[0]*n
    for t in range(n):counts[(exponent(s,d,t)-exponent(r,c,t))%n]+=1
    return cy.div_monic(cy.trim(counts),phi)[1]==[0]


def parallel(x,y):
    r,c=x;s,d=y
    diffs={(exponent(s,d,t)-exponent(r,c,t))%n for t in range(n)}
    return len(diffs)==1

blocks=[[(r,c) for c in range(n)] for r in range(n)]
blocks += [[(r,c) for r in range(n)] for c in range(n)]
blocks += [[(r,c) for r in range(n) for c in range(n) if L[r][c]==t] for t in range(n)]
assert len(blocks)==30 and all(len(block)==n for block in blocks)
for block in blocks:
    for x,y in combinations(block,2):
        assert zero_inner(x,y),(x,y)
cells=[(r,c) for r in range(n) for c in range(n)]
for x,y in combinations(cells,2):
    assert not parallel(x,y),(x,y)
# Every entry has norm 1/sqrt(10), so each 10-vector has exact norm one.
print('PASS 100 exact unit vectors, all30 original ONBs, 10 Latin transversals')
print('PASS all4950 distinct-cell pairs have different projective rays')
print('CERTIFIED within exact tenth-root polynomial arithmetic; independent review required')
