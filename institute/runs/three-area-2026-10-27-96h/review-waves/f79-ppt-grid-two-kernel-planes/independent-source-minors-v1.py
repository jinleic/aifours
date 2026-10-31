#!/usr/bin/env python3
"""Sparse Z-polynomial verification of the source range/SN3 minor identity."""
from itertools import combinations, permutations
import json
names='abcdefgih'; n=len(names)
zero=(0,)*n

def C(x): return {zero:x} if x else {}
def var(i):
    e=list(zero); e[i]=1; return {tuple(e):1}
def add(*args):
    out={}
    for p in args:
        for mon,c in p.items(): out[mon]=out.get(mon,0)+c
    return {mon:c for mon,c in out.items() if c}
def neg(p): return {m:-v for m,v in p.items()}
def sub(a,b): return add(a,neg(b))
def mul(*args):
    out=C(1)
    for p in args:
        prod={}
        for u,x in out.items():
            for v,y in p.items():
                key=tuple(i+j for i,j in zip(u,v))
                prod[key]=prod.get(key,0)+x*y
        out={m:c for m,c in prod.items() if c}
    return out
def determinant3(mat):
    terms=[]
    for p in permutations(range(3)):
        inv=sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))
        term=mul(*(mat[i][p[i]] for i in range(3)))
        terms.append(neg(term) if inv%2 else term)
    return add(*terms)

a,b,c,d,e,f,g,i,h=(var(j) for j in range(n))
M=[[a,b,c,{},h],[d,a,b,{},{}],[e,neg(d),a,f,{}],[g,{},i,e,c]]
g1=mul(e,sub(mul(a,a),mul(b,d)))
g2=mul(c,add(mul(a,a),mul(b,d)))
g3=mul(e,sub(mul(b,b),mul(a,c)))
g4=neg(mul(c,add(mul(d,d),mul(a,e))))
g5=sub(add(mul(a,a,a),mul(b,b,e)),add(mul(d,d,c),mul(a,c,e)))
claimed=[g1,g2,g3,g4,g5]
match=[[] for _ in claimed]
for rr in combinations(range(4),3):
    for cc in combinations(range(5),3):
        value=determinant3([[M[r][s] for s in cc] for r in rr])
        for j,expected in enumerate(claimed):
            if value==expected: match[j].append({'rows':rr,'columns':cc,'sign':1})
            if value==neg(expected): match[j].append({'rows':rr,'columns':cc,'sign':-1})
assert all(match)
left=sub(sub(mul(C(2),a,sub(sub(g5,g3),g4)),mul(c,g1)),mul(e,g2))
assert left==mul(C(2),a,a,a,a)
print(json.dumps({'coefficient_domain':'Z','range_matrix_shape':[4,5],
                  'minors_scanned':40,'five_required_minor_matches':match,
                  'corrected_identity_residual':'zero polynomial'},indent=2))
