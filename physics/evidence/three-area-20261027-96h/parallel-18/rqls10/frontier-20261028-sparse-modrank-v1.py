#!/usr/bin/env python3
"""Independent dictionary-based exact rank of sparse integer rows modulo p."""
import argparse
from math import isqrt
from pathlib import Path

p=argparse.ArgumentParser()
p.add_argument('matrix')
p.add_argument('--prime',type=int,default=65521)
args=p.parse_args()
prime=args.prime
assert prime>1 and all(prime%d for d in range(2,isqrt(prime)+1)), 'modulus not prime'
lines=Path(args.matrix).read_text().splitlines()
rows,cols=map(int,lines[0].split())
assert len(lines)==rows+1
pivots={}
for line in lines[1:]:
    parts=list(map(int,line.split()))
    count=parts[0]
    assert len(parts)==1+2*count
    row={}
    for col,value in zip(parts[1::2],parts[2::2]):
        assert 0<=col<cols
        row[col]=(row.get(col,0)+value)%prime
    row={c:v for c,v in row.items() if v}
    while row:
        lead=min(row)
        factor=row[lead]
        if lead not in pivots:
            inv=pow(factor,-1,prime)
            pivots[lead]={c:v*inv%prime for c,v in row.items()}
            break
        for c,v in pivots[lead].items():
            value=(row.get(c,0)-factor*v)%prime
            if value: row[c]=value
            else: row.pop(c,None)
print('file',args.matrix,'rows',rows,'columns',cols,'prime',prime,
      'rank',len(pivots),'nullity',cols-len(pivots))
