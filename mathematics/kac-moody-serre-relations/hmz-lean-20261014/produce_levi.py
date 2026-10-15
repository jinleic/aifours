#!/usr/bin/env python3
"""Exact sl3 free-Lie primitives: certificate producer, standard library only."""
import argparse
from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
from itertools import product
import json
from math import gcd, lcm
from pathlib import Path

NAMES = ['E12', 'E23', 'E13', 'E21', 'E32', 'E31', 'H1', 'H2']
WEIGHTS = [(2,-1), (-1,2), (1,1), (-2,1), (1,-2), (-1,-1), (0,0), (0,0)]

def unit(i,j):
    return tuple(int((a,b)==(i,j)) for a in range(3) for b in range(3))

def subtract(a,b):
    return tuple(x-y for x,y in zip(a,b))

def matrix_bracket(a,b):
    return tuple(sum(a[3*i+k]*b[3*k+j]-b[3*i+k]*a[3*k+j] for k in range(3))
                 for i in range(3) for j in range(3))

BASIS = [unit(0,1), unit(1,2), unit(0,2), unit(1,0), unit(2,1), unit(2,0),
         subtract(unit(0,0),unit(1,1)), subtract(unit(1,1),unit(2,2))]

def matrix_coordinates(a):
    assert a[0]+a[4]+a[8]==0
    return [a[1],a[5],a[2],a[3],a[7],a[6],a[0],-a[8]]

ACTIONS = [{j:{i:c for i,c in enumerate(matrix_coordinates(matrix_bracket(f,v))) if c}
            for j,v in enumerate(BASIS)} for f in (BASIS[3],BASIS[4])]

def plus(a,b,scale=1):
    out=dict(a)
    for w,c in b.items():
        out[w]=out.get(w,0)+scale*c
        if not out[w]: del out[w]
    return out

def times(a,b):
    out=defaultdict(int)
    for u,c in a.items():
        for v,d in b.items(): out[u+v]+=c*d
    return {w:c for w,c in out.items() if c}

def bracket(a,b):
    return plus(times(a,b),times(b,a),-1)

def lyndon(w):
    return all(w<w[k:] for k in range(1,len(w)))

@lru_cache(None)
def expansion(w):
    if len(w)==1: return {w:1}
    k=next(k for k in range(1,len(w)) if lyndon(w[k:]))
    return bracket(expansion(w[:k]),expansion(w[k:]))

def tree(w):
    if len(w)==1: return w[0]
    k=next(k for k in range(1,len(w)) if lyndon(w[k:]))
    return [tree(w[:k]),tree(w[k:])]

def weight(w):
    return tuple(sum(WEIGHTS[i][j] for i in w) for j in (0,1))

def act(action,p):
    out={}
    for w,c in p.items():
        for pos,j in enumerate(w):
            for i,d in action[j].items():
                out=plus(out,{w[:pos]+(i,)+w[pos+1:]:c*d})
    return out

def coordinates(p,words):
    out={};rem=dict(p)
    for j,w in enumerate(words):
        if w in rem:
            c=rem[w];out[j]=c;rem=plus(rem,expansion(w),-c)
    assert not rem
    return out

def data(degree):
    words=[w for w in product(range(8),repeat=degree) if lyndon(w)]
    zero=[w for w in words if weight(w)==(0,0)]
    targets=[[w for w in words if weight(w)==a] for a in [(-2,1),(1,-2)]]
    matrix=[]
    for action,basis in zip(ACTIONS,targets):
        columns=[coordinates(act(action,expansion(w)),basis) for w in zero]
        matrix.extend([[c.get(row,0) for c in columns] for row in range(len(basis))])
    return words,zero,targets,matrix

def independent_rows(rows):
    pivots={};selected=[]
    for number,row in enumerate(rows):
        w=[Fraction(x) for x in row]
        for p,b in sorted(pivots.items()):
            c=w[p]
            if c: w=[x-c*y for x,y in zip(w,b)]
        p=next((j for j,x in enumerate(w) if x),None)
        if p is not None:
            c=w[p];pivots[p]=[x/c for x in w];selected.append(number)
    return selected

def bareiss(a):
    b=[row[:] for row in a];sign=1;previous=1
    for k in range(len(b)-1):
        p=next((r for r in range(k,len(b)) if b[r][k]),None)
        if p is None: return 0
        if p!=k: b[k],b[p]=b[p],b[k];sign=-sign
        pivot=b[k][k]
        for i in range(k+1,len(b)):
            for j in range(k+1,len(b)):
                numerator=b[i][j]*pivot-b[i][k]*b[k][j]
                assert numerator%previous==0
                b[i][j]=numerator//previous
            b[i][k]=0
        previous=pivot
    return sign*b[-1][-1]

def first_nullvector(a):
    b=[[Fraction(x) for x in row] for row in a];pivots=[];r=0;n=len(b[0])
    for j in range(n):
        p=next((k for k in range(r,len(b)) if b[k][j]),None)
        if p is None: continue
        b[r],b[p]=b[p],b[r];c=b[r][j];b[r]=[x/c for x in b[r]]
        for k in range(len(b)):
            if k!=r and b[k][j]:
                c=b[k][j];b[k]=[x-c*y for x,y in zip(b[k],b[r])]
        pivots.append(j);r+=1
    free=next(j for j in range(n) if j not in pivots)
    out=[Fraction(int(j==free)) for j in range(n)]
    for row,j in enumerate(pivots): out[j]=-b[row][free]
    den=lcm(*(x.denominator for x in out));out=[int(x*den) for x in out]
    divisor=gcd(*out)
    return [x//divisor for x in out]

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    if args.output.exists(): raise SystemExit('Refusing to overwrite a certificate')
    all3,zero3,targets3,matrix3=data(3)
    rows=independent_rows(matrix3)
    determinant=bareiss([matrix3[r] for r in rows])
    assert len(all3)==168 and len(zero3)==18 and len(rows)==18 and determinant==288
    _,zero4,_,matrix4=data(4)
    vector4=first_nullvector(matrix4)
    witness=[{'word':list(w),'coefficient':c,'tree':tree(w)}
             for w,c in zip(zero4,vector4) if c]
    poly={}
    for w,c in zip(zero4,vector4):
        if c: poly=plus(poly,expansion(w),c)
    assert poly and all(not act(action,poly) for action in ACTIONS)
    certificate={'schema':'sl3-free-lie-level3/1','field':'Q','basis':NAMES,
        'source_words':zero3,'target_words':targets3,'matrix':matrix3,
        'selected_rows':rows,'minor_determinant':determinant,
        'degree4_primitive':witness,
        'scope':'No weight-zero Levi primitive in L3(ad sl3); degree4 witness is NOT a Serre counterexample.'}
    args.output.write_text(json.dumps(certificate,indent=2)+'\n')
    print(json.dumps({'certificate':str(args.output),'source_dimension':18,'target_dimension':26,
                      'minor_determinant':determinant,'degree4_bracket_terms':len(witness)},indent=2))

if __name__=='__main__': main()
