#!/usr/bin/env python3
"""Independent exact checks of the order-10 Fourier parity obstruction.

No numerical trigonometry or search-code coefficient table is used. The
written proof generalizes to n=2p, p odd prime.
"""
from itertools import combinations, permutations
from collections import Counter
import importlib.util
from pathlib import Path

ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('cy',ROOT/'frontier-20261028-cyclotomic-seven-sums-v1.py')
cy=importlib.util.module_from_spec(spec);spec.loader.exec_module(cy)
phi=cy.cyclotomic(10)
assert phi==[1,-1,1,-1,1]
counts=Counter()
for positive in combinations(range(10),5):
    s=set(positive)
    h=[1 if j in s else -1 for j in range(10)]
    _,rem=cy.div_monic(cy.trim(h[:]),phi)
    v=[h[r]-h[r+5] for r in range(5)]
    criterion=(v[0]==-v[1]==v[2]==-v[3]==v[4])
    parity=all(h[j]==h[0]*((-1)**j) for j in range(10))
    assert (rem==[0])==criterion==parity
    counts['patterns']+=1
    counts['zero_F_5_1']+=int(criterion)
print('5+ / 5- sign patterns',counts['patterns'],'exact Fourier zeros',counts['zero_F_5_1'],
      'both parity-homogeneous: PASS')
mu_counts=Counter(); f55=Counter()
for tail in permutations(range(1,10)):
    mu=(0,)+tail
    homogeneous=all((mu[t]-t)%2==0 for t in range(10))
    v=sum((-1)**(t+mu[t]) for t in range(10))
    assert v!=0 and v%4==2
    f55[v]+=1
    mu_counts['permutations']+=1;mu_counts['homogeneous']+=int(homogeneous)
print('mu(0)=0 permutations',mu_counts['permutations'],'parity-homogeneous',mu_counts['homogeneous'])
print('F(5,5) exact nonzero histogram',dict(sorted(f55.items())))
valid=0
for tail in permutations(range(1,10)):
    pi=(0,)+tail
    valid+=int(all((pi[r]-pi[r+5])%2==0 for r in range(5)))
print('pi(0)=0 permutations admitting five monochromatic opposite-row pairs',valid)
assert valid==0
print('PASS finite corroboration; ALL-p theorem rests on independent written proof')
