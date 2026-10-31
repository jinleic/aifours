#!/usr/bin/env python3
"""Exact GF(9) complex conference matrix and 19-ray two-ONB fragment.

Entries are (a,b)/8 representing (a+b*i*sqrt(7))/8. Formula is reconstructed
from Et-Taoui, arXiv:1409.4282v1, Theorem 2, and checked from scratch in
integer arithmetic; it is NOT a 100-ray QLS construction.
"""
from itertools import product
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent
F9=tuple(product(range(3), repeat=2))

def mul(x,y):
    a,b=x; c,d=y
    return ((a*c-b*d)%3,(a*d+b*c)%3)

def sub(x,y): return tuple((a-b)%3 for a,b in zip(x,y))

def mul_complex(x,y):
    a,b=x; c,d=y
    return (a*c-7*b*d,a*d+b*c)

def conj(x): return (x[0],-x[1])

def dot(u,v):
    terms=[mul_complex(conj(x),y) for x,y in zip(u,v)]
    return (sum(x[0] for x in terms),sum(x[1] for x in terms))

squares={mul(x,x) for x in F9 if x!=(0,0)}
assert len(squares)==4 and (0,0) not in squares
C=[]
for x in F9:
    row=[]
    for y in F9:
        d=sub(x,y)
        row.append((0,0) if d==(0,0) else (1,1 if d in squares else -1))
    C.append(row)
for i in range(9):
    for j in range(9):
        assert dot(C[i],C[j])==((64,0) if i==j else (0,0))
for i in range(9):
    for j in range(9):
        a,b=C[i][j]
        assert (a*a+7*b*b)==(0 if i==j else 8)

# Basis1 is e_0,...,e_9. Basis2 shares e_0, with the 9 conference columns
# embedded in coordinates1,...,9. Store scaled exact numerators.
e=[]
for j in range(10):
    v=[(0,0)]*10; v[j]=(8,0); e.append(v)
f=[]
for j in range(9): f.append([(0,0)]+[C[i][j] for i in range(9)])
assert all(dot(x,y)==((64,0) if i==j else (0,0))
           for i,x in enumerate([e[0]]+f) for j,y in enumerate([e[0]]+f))
assert all(dot(x,x)==(64,0) for x in e+f)
assert all(sum(a*a+7*b*b for a,b in v)>0 for v in e+f)
for m in (7,):
    magnitudes=[]; zeros=[]
    for n0 in range(m+1):
        for nplus in range(m-n0+1):
            nminus=m-n0-nplus
            k=nplus+nminus; delta=nplus-nminus
            numerator=(4*n0-3*k)**2+7*delta**2
            if numerator==128: magnitudes.append((n0,nplus,nminus))
            if numerator==0: zeros.append((n0,nplus,nminus))
    assert not magnitudes and zeros==[(3,2,2)]
    print('7-overlap two-phase count: target squared magnitude 8 impossible; zero patterns',zeros)
record={'field':'F3[t]/(t^2+1)','field_order':F9,'square_elements':sorted(squares),
        'representation':'(a+b*i*sqrt(7))/8','basis1':e,'basis2':[e[0]]+f,
        'distinct_ray_count_claim':19,
        'caveat':'two ONBs only, not a resolvable 10x10 array or full uniform lift'}
p=ROOT/'frontier-20261028-gf9-conference-result-v1.json'
p.write_text(json.dumps(record,indent=2,sort_keys=True)+'\n')
print('GF9 squares:',len(squares),'of8 nonzero elements')
print('exact scaled 9x9 Gram=64I and offdiagonal norm squared=8: PASS')
print('exact 10x10 two-basis fragment: both ONBs, one common ray, 19 distinct rays')
print('wrote',p.name)


if __name__=='__main__':
    pass
