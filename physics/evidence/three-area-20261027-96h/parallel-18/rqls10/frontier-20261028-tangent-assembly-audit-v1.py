#!/usr/bin/env python3
"""Independently audit every linearized equation and gauge row against vectors."""
import json
from itertools import combinations
from pathlib import Path

ROOT=Path(__file__).resolve().parent
v=json.loads((ROOT/'frontier-20261028-parker-13ray-result-v1.json').read_text())['partial_witness']
arr=v['array']; labels=v['labels']; n=10
cols=[arr[r][c] for r in range(n) for c in range(n)]
block_groups=[]
for r in range(n): block_groups.append([10*r+c for c in range(n)])
for c in range(n): block_groups.append([10*r+c for r in range(n)])
for t in range(n): block_groups.append([10*r+c for r in range(n) for c in range(n) if labels[r][c]==t])
assert len(block_groups)==30 and all(len(group)==10 for group in block_groups)
edges=[pair for group in block_groups for pair in combinations(group,2)]
assert len(edges)==1350


def row_dict(terms):
    result={}
    for index,value in terms:
        result[index]=result.get(index,0)+value
    return {i:x for i,x in result.items() if x}


def expected(kind):
    rows=[]
    if kind=='real':
        for x in range(100):
            rows.append(row_dict((10*x+k,cols[x][k]) for k in range(10)))
    for x,y in edges:
        terms=[]
        for k in range(10):
            terms.append((10*x+k,cols[y][k] if kind=='real' else -cols[y][k]))
            terms.append((10*y+k,cols[x][k]))
        rows.append(row_dict(terms))
    for i in range(100): rows.append({i:1})
    if kind=='imag':
        for x in range(10,100):
            rows.append(row_dict((10*x+k,cols[x][k]) for k in range(10)))
        assert cols[77][7:] == [1,-2,-2]
        rows += [{10*77+7:1},{10*77+8:1}]
    return rows


for kind in ('real','imag'):
    path=ROOT/f'frontier-20261028-parker13-tangent-{kind}-gauge-v1.txt'
    lines=path.read_text().splitlines()
    count,width=map(int,lines[0].split())
    observed=[]
    for line in lines[1:]:
        x=list(map(int,line.split()))
        assert len(x)==1+2*x[0]
        observed.append(row_dict(zip(x[1::2],x[2::2])))
    wanted=expected(kind)
    assert width==1000 and count==len(observed)==len(wanted)
    assert observed==wanted
    print(kind,'independent assembly audit: PASS',count,'rows x',width,'columns')
print('PASS every original norm/30-block orthogonality derivative and stated gauge row')
