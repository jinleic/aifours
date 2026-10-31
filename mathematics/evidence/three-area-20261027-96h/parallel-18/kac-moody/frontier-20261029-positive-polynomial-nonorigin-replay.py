#!/usr/bin/env python3
"""Exact scalar identity and positivity off the nonnegative origin.

Reuses the pinned standard-library parser/Horner helpers, not a producer.
Does not reconstruct a source, a matrix or a determinant. An absent constant
and a positive pure-power term on EACH axis prove positivity off the origin.
"""
import argparse
import hashlib
import importlib.util
import json
from fractions import Fraction as Q
from pathlib import Path

ROOT=Path(__file__).resolve().parent
HELPER='frontier-20261029-positive-polynomial-translation-replay.py'
HELPER_SHA='7dffe489557a7782d283fd2894f9f8f12eecce7e898f27ae8e7c0400dbe60de3'


def load_helper():
    path=ROOT/HELPER
    if hashlib.sha256(path.read_bytes()).hexdigest()!=HELPER_SHA:
        raise ArithmeticError('pinned scalar helper mismatch')
    spec=importlib.util.spec_from_file_location('pinned_scalar_translation_helper',path)
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main():
    if not __debug__:
        raise RuntimeError('assertions disabled')
    ap=argparse.ArgumentParser()
    ap.add_argument('--certificate',required=True)
    ap.add_argument('--sha256',required=True)
    args=ap.parse_args()
    S=load_helper()
    raw=S.bound_path(args.certificate).read_bytes()
    if hashlib.sha256(raw).hexdigest()!=args.sha256:
        raise ArithmeticError('certificate byte-hash mismatch')
    C=json.loads(raw)
    original=S.pinned(C['original_polynomial'])
    matrix=S.pinned(C['canonical_pencil'])
    replay=S.pinned(C['completed_original_full_replay'])
    k=C['entire_primitive_dimension']
    assert type(k) is int and 1<=k<=1000
    assert original['size']==matrix['entire_primitive_dimension']==k
    assert matrix['degree']==original['degree']==C['degree']
    assert len(matrix['matrix'])==k
    assert all(len(row)==k and all(len(e)==3 for e in row) for row in matrix['matrix'])
    assert original['pencil_sha256']==C['canonical_pencil']['sha256']
    assert replay['canonical_pencil_sha256']==C['canonical_pencil']['sha256']
    assert replay['all3_entire_word_reconstructions'] is True
    assert replay['status']=='PASS_ALTERNATE_ENTIRE_INVARIANT_MATRIX_AND_HALF_LEVEL_POLYNOMIAL'
    grade=C['grade'];lower=C['lower_parameter_bound']
    assert type(grade) is int and type(lower) is int and 1<=lower<=grade
    shift=grade-lower
    assert C['translation_shift']==shift
    assert C['positivity_mode']=='NONNEGATIVE_ORTHANT_EXCEPT_ORIGIN'
    assert C['exceptional_nonnegative_points']==[[0,0]]
    T,tints,tden=S.parse_terms(C['coefficients'],'u_power','v_power',k)
    P,pints,pden=S.parse_terms(original['coefficients'],'x_power','y_power',k)
    assert T.get((0,0),Q(0))==Q(C['constant_coefficient'])==0
    assert all(c>0 for c in T.values())
    witnesses=C['nonzero_axis_witnesses']
    assert len(witnesses)==2
    assert any(i>0 and j==0 and (i,j) in T for i,j in witnesses)
    assert any(i==0 and j>0 and (i,j) in T for i,j in witnesses)
    checks=0
    for i in range(k+1):
        u=i-1
        ti=S.columns_at(tints,u,k)
        pi=S.columns_at(pints,u-shift,k)
        for j in range(k+1-i):
            v=j+2
            assert S.horner(ti,v)*pden==S.horner(pi,v-shift)*tden,('identity mismatch',u,v)
            checks+=1
    assert checks==(k+1)*(k+2)//2
    result={'owner':'MathKacMoody-2','input_file':args.certificate,'input_sha256':args.sha256,
            'original_polynomial':C['original_polynomial'],'canonical_pencil':C['canonical_pencil'],
            'completed_original_full_replay':C['completed_original_full_replay'],
            'degree':C['degree'],'entire_free_primitive_dimension':k,'lower_parameter_bound':lower,
            'positive_nonzero_coefficients':len(T),'constant_coefficient':'0',
            'positivity_domain':'u,v>=0 except (0,0)',
            'nonzero_axis_witnesses':witnesses,'exact_complete_unisolvent_evaluations':checks,
            'grid':'u=i-1,v=j+2,i,j>=0,i+j<=matrix_dimension',
            'identity':f'T(u,v)=P(u-{shift},v-{shift})',
            'arithmetic':'stdlib Python integers and Fraction only',
            'program_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'scalar_helper':{'file':HELPER,'sha256':HELPER_SHA},
            'status':'PASS_EXACT_POSITIVE_TRANSLATION_EXCEPT_NONNEGATIVE_ORIGIN',
            'limits':'Scalar identity and positivity only. Source, matrix and determinant reconstruction are separately bound prior evidence, not rerun here. Actual quotient descent and source dimensions require written mathematics and independent scientific review. No (lower,lower) verdict, parent, formal/kernel, configured-family/human or novelty acceptance.'}
    output=args.certificate.removesuffix('-v1.json')+'-identity-replay-v1.json'
    with S.bound_path(output).open('x') as stream:
        json.dump(result,stream,indent=2)
        stream.write('\n')
    print('PASS complete scalar translation except origin',C['degree'],'coefficients',len(T),'grid',checks,output,flush=True)


if __name__=='__main__':
    main()
