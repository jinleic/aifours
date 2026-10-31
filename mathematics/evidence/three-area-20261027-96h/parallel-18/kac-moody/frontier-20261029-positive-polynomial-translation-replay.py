#!/usr/bin/env python3
"""Standard-library-only exact identity replay of a pinned positive translation.

Reads BOTH complete rational coefficient tables. An entire shifted unisolvent
triangle proves T(u,v)=P(u-shift,v-shift) under the stated total-degree bound.
Checks positive coefficients/nonzero constant. This does NOT reconstruct any
source or matrix, rerun a determinant, prove source transport or promote a
scientific claim. No FLINT/SymPy/NumPy or producer code is imported.
"""
import argparse
import hashlib
import json
import math
from fractions import Fraction as Q
from pathlib import Path

ROOT=Path(__file__).resolve().parent


def bound_path(name):
    if not isinstance(name,str) or Path(name).name!=name:
        raise ValueError('non-basename input reference')
    return ROOT/name


def pinned(pin):
    raw=bound_path(pin['file']).read_bytes()
    if hashlib.sha256(raw).hexdigest()!=pin['sha256']:
        raise ArithmeticError('input byte-hash mismatch')
    return json.loads(raw)


def parse_terms(rows,first,second,degree):
    terms={}
    for row in rows:
        i,j=row[first],row[second]
        if type(i) is not int or type(j) is not int or min(i,j)<0 or i+j>degree:
            raise ArithmeticError('invalid monomial or total degree')
        if (i,j) in terms:
            raise ArithmeticError('duplicate monomial')
        c=Q(row['coefficient'])
        if not c:
            raise ArithmeticError('serialized zero coefficient')
        terms[i,j]=c
    if not terms:
        raise ArithmeticError('empty polynomial')
    denominator=math.lcm(*(c.denominator for c in terms.values()))
    return terms,{mon:int(c*denominator) for mon,c in terms.items()},denominator


def columns_at(terms,x,degree):
    powers=[1]*(degree+1)
    for i in range(1,degree+1):
        powers[i]=powers[i-1]*x
    output=[0]*(degree+1)
    for (i,j),c in terms.items():
        output[j]+=c*powers[i]
    return output


def horner(values,x):
    out=0
    for c in reversed(values):
        out=out*x+c
    return out


def main():
    if not __debug__:
        raise RuntimeError('assertions disabled')
    ap=argparse.ArgumentParser()
    ap.add_argument('--certificate',required=True)
    ap.add_argument('--sha256',required=True)
    args=ap.parse_args()
    raw=bound_path(args.certificate).read_bytes()
    if hashlib.sha256(raw).hexdigest()!=args.sha256:
        raise ArithmeticError('certificate byte-hash mismatch')
    C=json.loads(raw)
    original=pinned(C['original_polynomial'])
    matrix=pinned(C['canonical_pencil'])
    k=C['entire_primitive_dimension']
    assert type(k) is int and 1<=k<=1000
    assert original['size']==matrix['entire_primitive_dimension']==k
    assert matrix['degree']==original['degree']==C['degree']
    assert len(matrix['matrix'])==k and all(len(row)==k and all(len(e)==3 for e in row) for row in matrix['matrix'])
    assert original['pencil_sha256']==C['canonical_pencil']['sha256']
    grade=C['grade']
    lower=C['lower_parameter_bound']
    assert type(grade) is int and type(lower) is int and 1<=lower<=grade
    shift=grade-lower
    if 'translation_shift' in C:
        assert C['translation_shift']==shift
    T,tints,tden=parse_terms(C['coefficients'],'u_power','v_power',k)
    P,pints,pden=parse_terms(original['coefficients'],'x_power','y_power',k)
    assert T.get((0,0),Q(0))>0 and all(c>0 for c in T.values())
    assert T[0,0]==Q(C['constant_coefficient'])
    checks=0
    for i in range(k+1):
        u=i-1
        ti=columns_at(tints,u,k)
        pi=columns_at(pints,u-shift,k)
        for j in range(k+1-i):
            v=j+2
            assert horner(ti,v)*pden==horner(pi,v-shift)*tden, ('translation mismatch',u,v)
            checks+=1
    assert checks==(k+1)*(k+2)//2
    result={'owner':'MathKacMoody-2','input_file':args.certificate,'input_sha256':args.sha256,
            'original_polynomial':C['original_polynomial'],'canonical_pencil':C['canonical_pencil'],
            'degree':C['degree'],'entire_primitive_dimension':k,'lower_parameter_bound':lower,
            'positive_nonzero_coefficients':len(T),'nonzero_constant':str(T[0,0]),
            'exact_complete_unisolvent_evaluations':checks,'grid':'u=i-1,v=j+2,i,j>=0,i+j<=matrix_dimension',
            'identity':f'T(u,v)=P(u-{shift},v-{shift})','arithmetic':'stdlib Python integers and Fraction only',
            'program_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'status':'PASS_EXACT_POSITIVE_TRANSLATION_OF_PINNED_POLYNOMIAL',
            'limits':'Scalar polynomial identity only. Source/matrix/degree-bound/actual-sector transport and scientific review remain explicit substantive inputs; no determinant or source was independently reconstructed by THIS checker. No parent/formal/kernel/configured-family/human or novelty acceptance.'}
    output=args.certificate.removesuffix('-v1.json')+'-identity-replay-v1.json'
    with bound_path(output).open('x') as stream:
        json.dump(result,stream,indent=2)
        stream.write('\n')
    print('PASS exact complete positive translation',C['degree'],'coefficients',len(T),'grid',checks,output,flush=True)


if __name__=='__main__':
    main()
