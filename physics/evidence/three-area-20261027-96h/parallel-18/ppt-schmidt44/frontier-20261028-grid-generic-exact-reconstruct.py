#!/usr/bin/env python3
"""Reconstruct an EXACT positive rational Gram certificate from exact atoms.

Numeric QR-like selection chooses a basis only. Integer Bareiss elimination,
positivity and all 81 reconstructed Hermitian coordinates are checked exactly.
An independent verifier must still check the resulting 4x4 rank/PPT certificate.
"""
from fractions import Fraction as F
from math import gcd, lcm
from pathlib import Path
import json
import sys
import numpy as np


sys.set_int_max_str_digits(0)
HERE=Path(__file__).parent
INPUT=HERE/'frontier-20261028-grid-rationalized-atoms-run-v1.json'
OUTPUT=HERE/'frontier-20261028-grid-generic-exact-certificate-v1.json'


def int_atom(entry):
    q=[(F(x),F(y)) for x,y in entry['atom']]
    L=1
    for x,y in q:L=lcm(L,x.denominator,y.denominator)
    z=[(int(x*L),int(y*L)) for x,y in q]
    g=0
    for x,y in z:g=gcd(g,abs(x));g=gcd(g,abs(y))
    if not g:raise ValueError('zero atom')
    return [(x//g,y//g) for x,y in z]


def integer_feature(z):
    out=[x*x+y*y for x,y in z]
    for i in range(9):
        for j in range(i+1,9):
            a,b=z[i];c,d=z[j]
            out.extend((a*c+b*d,b*c-a*d))
    return out


def solve_bareiss(matrix,rhs):
    n=len(rhs); a=[list(matrix[i])+[rhs[i]] for i in range(n)];prev=1
    for k in range(n-1):
        candidates=[j for j in range(k,n) if a[j][k]]
        if not candidates:raise ValueError('singular selected basis')
        pivotrow=min(candidates,key=lambda j:abs(a[j][k]))
        if pivotrow!=k:a[k],a[pivotrow]=a[pivotrow],a[k]
        pivot=a[k][k]
        for i in range(k+1,n):
            left=a[i][k]
            for j in range(k+1,n+1):
                value=a[i][j]*pivot-left*a[k][j]
                quotient,rem=divmod(value,prev)
                if rem:raise ArithmeticError('nonexact Bareiss division')
                a[i][j]=quotient
            a[i][k]=0
        prev=pivot
    if not a[-1][-2]:raise ValueError('singular final pivot')
    x=[F(0)]*n
    for i in range(n-1,-1,-1):
        x[i]=(F(a[i][n])-sum(F(a[i][j])*x[j] for j in range(i+1,n)))/a[i][i]
    return x


def main():
    data=json.loads(INPUT.read_text()); rows=data['active_atoms']
    zs=[int_atom(row) for row in rows]
    feats=[integer_feature(z) for z in zs]
    norms=[sum(x*x+y*y for x,y in z) for z in zs]
    weights=np.array([row['normalized_weight_float'] for row in rows])
    floats=np.column_stack([np.array(v,dtype=float)/float(s) for v,s in zip(feats,norms)])
    candidates=np.array([j for j in range(len(zs)) if norms[j].bit_length()<=175 and weights[j]>=.001])
    residual=floats[:,candidates].copy(); chosen=[]
    for _ in range(81):
        sq=np.sum(residual*residual,axis=0);j=int(np.argmax(sq))
        if sq[j]<1e-20:raise ValueError('numeric basis not full rank')
        v=residual[:,j]/np.sqrt(sq[j]);chosen.append(int(candidates[j]))
        residual-=np.outer(v,v@residual)
    if len(set(chosen))!=81:raise AssertionError('duplicate basis')
    denominator=max(norms)*10**15
    # round(w*D/norm) exactly from the decimal rendering of each observed float
    numerators=[]
    for w,s in zip(weights,norms):
        v=F(str(w))*denominator/s
        numerators.append(round(v))
    if min(numerators)<=0:raise ValueError('base coefficient rounded to zero')
    target=[1,1,3,1,3,3,3,3,3]+[0]*72
    rhs=[denominator*target[i]-sum(numerators[j]*feats[j][i] for j in range(len(zs)))
         for i in range(81)]
    mat=[[feats[j][i] for j in chosen] for i in range(81)]
    correction=solve_bareiss(mat,rhs)
    common=1
    for x in correction:common=lcm(common,x.denominator)
    total_denominator=denominator*common
    final=[k*common for k in numerators]
    for j,x in zip(chosen,correction):final[j]+=int(x*common)
    if min(final)<=0:raise AssertionError('nonpositive exact coefficient')
    bad=[i for i in range(81) if sum(final[j]*feats[j][i] for j in range(len(zs)))
         !=total_denominator*target[i]]
    if bad:raise AssertionError({'Gram_mismatches':bad})
    result={'schema_version':1,'kind':'EXACT_POSITIVE_GAUSSIAN_INTEGER_COEFFICIENT_GRAM_CERTIFICATE',
            'kernel_vector':[-1,-1,-1,4,-1],
            'map':'K|0,1,2>=|0,1,2>; K|3>=(|0>+|1>+|2>+|3>)/4; K|4>=|3>',
            'target_diagonal':target[:9], 'common_denominator':str(total_denominator),
            'atoms':[{'weight_numerator':str(n),'coefficients':[[str(a),str(b)] for a,b in z]}
                     for n,z in zip(final,zs)],
            'construction':{'basis_count':81,'atom_count':len(zs),'fraction_free_solver':'Bareiss',
                            'all_weights_strictly_positive':True,'exact_gram_coordinates_checked':81},
            'limits':'Gram equality verified in this construction; independent physical rank, PPT and entanglement verification required'}
    with open(OUTPUT,'x',encoding='utf-8') as f:json.dump(result,f,separators=(',',':'))
    print(json.dumps({'atoms':len(zs),'basis':len(chosen),'exact_gram_mismatches':len(bad),
                      'all_weights_strictly_positive':True,
                      'common_denominator_bits':total_denominator.bit_length(),
                      'max_atom_integer_bits':max(max(abs(x).bit_length() for pair in z for x in pair) for z in zs),
                      'certificate':str(OUTPUT)},indent=2))


if __name__=='__main__':main()
