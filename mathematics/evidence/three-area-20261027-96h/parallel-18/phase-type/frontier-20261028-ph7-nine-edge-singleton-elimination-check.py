#!/usr/bin/env python3
"""All-variable symbolic check of the 9-edge singleton-elimination construction.

For every one of 9 connector shapes and every omitted triangle vertex (18
choices), build actual 7-state/6-state row generators symbolically and verify
row ties and the full determinant factor after setting singleton rate equal
to that omitted rate. No numerical states or PH witnesses are used.
"""
from itertools import permutations, product
from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT/'frontier-20261028-localdeps'))
import sympy as s

rates = s.symbols('a0 a1 a2 b0 b1 b2', positive=True)
ta,tb = s.symbols('theta_A theta_B', positive=True)
y = s.symbols('y')


def segment(entry, exit):
    result = [entry]
    while result[-1] != exit:
        result.append((result[-1]+1) % 3)
    return result


def matrix(k, ell, singleton=None, selected=None):
    ae,af,be,bf = (-ell)%3,0,0,k
    av,bv = segment(ae,af),segment(be,bf)
    if selected is not None:
        group,idx=selected
        en,ex=(ae,af) if group=='A' else (be,bf)
        old=segment(en,ex)
        if (en-1)%3==idx:
            en=idx
        elif (ex+1)%3==idx:
            ex=idx
        else:
            raise AssertionError((k,ell,selected,old))
        assert set(segment(en,ex)) == set(old)|{idx}
        if group=='A': ae,af=en,ex
        else: be,bf=en,ex
    n=6 if selected is not None else 7
    u=list(rates)+([] if selected is not None else [singleton])
    M=[[s.S.Zero for _ in range(n)] for _ in range(n)]
    for i in range(n): M[i][i]=y+u[i]
    for i in range(3): M[i][(i+1)%3]=-u[i]*(ta if i==af else 1)
    for i in range(3): M[i+3][(i+1)%3+3]=-u[i+3]*(tb if i==bf else 1)
    M[af][be+3]=-u[af]*(1-ta)
    if selected is not None:
        M[bf+3][ae]=-u[bf+3]*(1-tb)
    else:
        M[bf+3][6]=-u[bf+3]*(1-tb)
        M[6][ae]=-singleton
    assert all(s.expand(sum(row)-y)==0 for row in M)
    return M,av,bv


def determinant(M):
    n=len(M);answer=s.S.Zero
    for p in permutations(range(n)):
        entries=[M[i][j] for i,j in enumerate(p)]
        if any(q==0 for q in entries): continue
        inv=sum(p[i]>p[j] for i in range(n) for j in range(i+1,n))
        answer+=(-1 if inv%2 else 1)*s.prod(entries)
    return s.expand(answer)


count=0
for k,ell in product(range(3),repeat=2):
    _,av,bv=matrix(k,ell,singleton=s.Symbol('x'))
    omitted=[('A',i) for i in range(3) if i not in av]+[('B',i) for i in range(3) if i not in bv]
    for group,idx in omitted:
        rate=rates[idx+(3 if group=='B' else 0)]
        M7,_,_=matrix(k,ell,singleton=rate)
        M6,_,_=matrix(k,ell,selected=(group,idx))
        assert s.expand(determinant(M7)-(y+rate)*determinant(M6))==0
        count+=1
assert count==18
print('SymPy',s.__version__,'PASS: 9 connector shapes / 18 omissions; 7- and 6-state row ties and full symbolic determinant factor')
print('Requires independently justified 0<theta_A,theta_B<1 for Metzler positivity; not a formal proof or PH witness.')
