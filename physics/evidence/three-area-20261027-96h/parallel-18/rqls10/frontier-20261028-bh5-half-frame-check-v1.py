#!/usr/bin/env python3
"""Independently check the SAT half-frame and duplicated columns exactly."""
from collections import Counter
from itertools import combinations
import json
from pathlib import Path

root=Path(__file__).resolve().parent
D=json.loads((root/'frontier-20261028-bh5-half-frame-smt-result-v1.json').read_text())
assert D['verdict']=='sat'
A=D['exponents']
assert len(A)==5 and all(len(row)==10 for row in A)
for i,j in combinations(range(5),2):
    assert Counter((A[i][c]-A[j][c])%5 for c in range(10))==Counter({k:2 for k in range(5)})
for c in range(0,10,2):
    assert {(A[i][c]-A[i][c+1])%5 for i in range(5)}==set(range(5))
classes=Counter(tuple(A[i][c] for i in range(5)) for c in range(10))
assert len(classes)==5 and set(classes.values())=={2}
print('exact 5x10 half-frame: all 10 row-pair sums0 and 5 designated column-pair sums0 PASS')
print('distinct column signatures',len(classes),'multiplicities',sorted(classes.values()))
print('not a full BH(10,5); duplicate-half obstruction requires written proof')
