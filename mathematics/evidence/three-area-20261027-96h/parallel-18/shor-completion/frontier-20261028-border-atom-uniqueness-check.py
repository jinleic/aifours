#!/usr/bin/env python3
"""Finite synthetic controls for actual a^* b^+ atom-residue uniqueness."""
from itertools import combinations
from pathlib import Path
import json,runpy

ud=runpy.run_path(str(Path(__file__).with_name('frontier-20261028-zero-column-tradeoff-check.py')))['UD']
rows=[]
for n in range(2,7):
    atoms=[(i,k,b'a'*i+b'b'*k) for i in range(2*n) for k in range(1,4) if (i,k)!=(0,1)]
    total=valid=colliding=0
    for (i,k,u),(j,l,v) in combinations(atoms,2):
        total+=1;code={b'a'*n,b'b',u,v};answer=ud(code)
        heads=[0,i%n,j%n]
        if len(set(heads))<3:
            colliding+=1
            if answer:raise AssertionError(('UD with repeated border head',n,i,k,j,l))
        if answer:valid+=1
    rows.append({'n':n,'codes':total,'UD':valid,'repeated-head-rejections':colliding})
print(json.dumps({'domains':rows,'scope':'synthetic codes; no Shor completion existence claimed'},indent=2))
