#!/usr/bin/env python3
"""Whole first-row invariant ideals and shifted22x22 determinant replay.

Pinned helper is the separately completed literal corner REPLAYER, not a
producer. Reuses its completed whole Gram proof without double-counting it.
Reconstructs every new seed descendant/cross pairing and complete quotient.
"""
import argparse
import hashlib
import importlib.util
import itertools
import json
from collections import Counter
from fractions import Fraction as Q
from pathlib import Path

import numpy as np

ROOT=Path(__file__).resolve().parent
HELPER='frontier-20261029-invariant-actual22-corner-replay.py'
HELPER_SHA='a1cf8aa7d4b085384bdc48e01978bd56f20beff5c4b8faf9b61eea3621b6d8d6'


def literal_helper():
    path=ROOT/HELPER
    assert hashlib.sha256(path.read_bytes()).hexdigest()==HELPER_SHA
    spec=importlib.util.spec_from_file_location('pinned_entire_corner_replayer',path)
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
    return m


def regenerate(L,seed,V,G,degrees,lookup):
    generators=[];columns=[];maximum=max(abs(int(V.min())),abs(int(V.max())))
    for outer in itertools.product(range(8),repeat=5):
        if (sum(degrees[a][0] for a in outer)+degrees[seed][0],
            sum(degrees[a][1] for a in outer)+degrees[seed][1])!=(7,7):continue
        q=L.bracket({(0,):1},{(seed,):1})
        y={w:-c for w,c in q.items()}
        for a in reversed(outer):y=L.bracket({(a,):1},y)
        generators.append({'seed_letter':seed,'outer_letters':list(outer),
                           'whole_word_terms':[[L.code(w),int(c)] for w,c in sorted(y.items(),key=lambda z:L.code(z[0]))]})
        gy=Counter()
        for word,c in y.items():
            expansion={():c}
            for letter in word:
                expansion={u+(j,):value*G[j][letter]
                           for u,value in expansion.items() for j in range(8) if G[j][letter]}
            for u,value in expansion.items():gy[L.code(u)]+=value
        gy={w:c for w,c in gy.items() if c}
        ix=np.array([lookup[w] for w in gy],dtype=np.int64)
        coefs=np.array(list(gy.values()),dtype=np.int64)
        assert maximum*sum(abs(int(c)) for c in coefs)<2**63
        columns.append(V[:,ix]@coefs)
    assert len(generators)==1100
    return generators,np.array(columns,dtype=np.int64).T


def main():
    if not __debug__:raise RuntimeError('assertions disabled')
    ap=argparse.ArgumentParser();ap.add_argument('--certificate',required=True);ap.add_argument('--sha256',required=True)
    args=ap.parse_args();L=literal_helper();F=L.flint
    C=json.loads(L.pinned({'file':args.certificate,'sha256':args.sha256}))
    assert C['degree']==[7,7,7]
    prior=json.loads(L.pinned(C['prior_entire_gram_and_second_seed_corner']))
    receipt=json.loads(L.pinned(C['prior_entire_gram_and_corner_replay']))
    assert receipt['status']=='PASS_ENTIRE_ACTUAL74_INVARIANT_TWO_SEED_CORNER'
    assert receipt['input_sha256']==C['prior_entire_gram_and_second_seed_corner']['sha256']
    assert receipt['program_sha256']==HELPER_SHA
    assert prior['source']==C['source'] and prior['canonical_pencil']==C['canonical_pencil']
    source=json.loads(L.pinned(C['source']))
    source_receipt=json.loads(L.pinned(C['source_replay']))
    assert source_receipt['status']=='PASS_LITERAL_ENTIRE_INVARIANT_SOURCE_AND_BYTE_SEED_REPLAY'
    assert source_receipt['input_sha256']==C['source']['sha256']
    P=json.loads(L.pinned(C['canonical_pencil']))
    assert P['source_pencil_sha256']==C['source']['sha256']
    words,V=[L.array(pin) for pin in source['files']]
    assert words.dtype==np.dtype('uint32') and V.dtype==np.dtype('int64')
    assert words.shape==(104960,) and V.shape==(100,104960)
    lookup={int(w):i for i,w in enumerate(words)}
    G,degrees=L.literal_module();H=F.fmpq_mat(prior['source_gram'])
    assert len(C['families'])==2
    all_cross={};coefficient_tables=[];grid_checks=0
    for expected_seed,family in enumerate(C['families'],1):
        assert family['seed_letter']==expected_seed
        generators,cross=regenerate(L,expected_seed,V,G,degrees,lookup)
        assert generators==family['all_generators']
        assert cross.tolist()==family['all_cross_inner_products']
        assert F.fmpz_mat(cross.tolist()).rank()==family['whole_ideal_rank']==78
        indices=family['independent_witness_indices']
        assert len(indices)==len(set(indices))==78 and all(type(i) is int and 0<=i<1100 for i in indices)
        coordinates=H.solve(F.fmpq_mat(cross[:,indices].tolist()))
        rr,rank=coordinates.transpose().rref();assert rank==78
        I=L.matrix([[rr[j,i] for j in range(rank)] for i in range(100)])
        assert L.strings(I)==family['ideal_basis']
        pivots=[next(i for i in range(100) if rr[j,i]) for j in range(rank)]
        free=[i for i in range(100) if i not in pivots]
        assert pivots==family['ideal_pivot_coordinates'] and free==family['complement_coordinates']
        assert len(free)==22
        fields=[]
        for kind in (0,1):
            if expected_seed==1:
                A=L.matrix([[F.fmpq(e[0])-6*F.fmpq(e[1])-4*F.fmpq(e[2]) if kind==0 else F.fmpq(e[2]) for e in row] for row in P['matrix']])
            else:
                A=L.matrix([[F.fmpq(e[0])-4*F.fmpq(e[1])-6*F.fmpq(e[2]) if kind==0 else F.fmpq(e[1]) for e in row] for row in P['matrix']])
            AI=A*I;T=L.matrix([[AI[p,j] for j in range(rank)] for p in pivots])
            assert AI==I*T
            fields.append(L.matrix([[A[i,j]-sum(I[i,k]*A[p,j] for k,p in enumerate(pivots)) for j in free] for i in free]))
        assert [[[str(fields[0][i,j]),str(fields[1][i,j])] for j in range(22)] for i in range(22)]==family['quotient_affine_matrix']
        coefs=[Q(c) for c in family['complete_determinant_coefficients']]
        assert len(coefs)==23 and all(c>0 for c in coefs)
        assert family['polynomial_variable']=='u=other_parameter-2'
        assert family['variable']=='t=other_parameter-3'
        for i in range(23):
            u=i-2;value=Q(0)
            for c in reversed(coefs):value=value*u+c
            assert value==Q(str((fields[0]+(u-1)*fields[1]).det()))
            grid_checks+=1
        assert (fields[0]-fields[1]).det()
        all_cross[expected_seed]=cross;coefficient_tables.append(coefs)
        print('PASS ENTIRE firstrow',expected_seed,'1100 descendants,rank78,full22 quotient,23 shifted determinant points',flush=True)
    assert coefficient_tables[0]==coefficient_tables[1]
    r11=F.fmpz_mat(np.concatenate((all_cross[1],all_cross[2]),axis=1).tolist()).rank()
    second=np.array(prior['cross_inner_products'],dtype=np.int64)
    r12=F.fmpz_mat(np.concatenate((all_cross[1],second[:,40:80]),axis=1).tolist()).rank()
    r21=F.fmpz_mat(np.concatenate((second[:,:40],all_cross[2]),axis=1).tolist()).rank()
    assert (r11,r12,r21)==(100,82,82)
    result={'owner':'MathKacMoody-2','input_file':args.certificate,'input_sha256':args.sha256,
            'source':C['source'],'canonical_pencil':C['canonical_pencil'],
            'prior_entire_gram_and_corner_replay':C['prior_entire_gram_and_corner_replay'],
            'all_new_seed_descendants_and_cross_pairings_reconstructed':2200,
            'single_first_seed_invariant_ideal_ranks':[78,78],
            'entire_one_seed_quotient_dimensions':[22,22],
            'all4_affine_source_ideal_stability_and_quotient_matrices_checked':True,
            'shifted_exact_matrix_determinants':grid_checks,
            'positive_coefficients_per_determinant':23,
            'universal_other_parameter_lower_bound':2,
            'two_oriented_determinant_polynomials_identical':True,
            'actual_source_dimensions':{'1,1':0,'1,2':18,'2,1':18,'1,other>=3':22,'other>=3,1':22},
            'scalar_grid':'u=i-2,i=0..22; actual other=2+u,formal outside-domain evaluations only prove polynomial identity',
            'program_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'literal_helper':{'file':HELPER,'sha256':HELPER_SHA},
            'numpy_version':np.__version__,'flint_version':F.__version__,
            'status':'PASS_ENTIRE_FIRSTROWS_AND_ALL_SMALL_INVARIANT_SOURCE_COUNTS',
            'limits':'Whole previously replayed source and compact Gram reused and bound, not credited as new reruns. Same-owner alternate tuple/sparse-metric reconstruction with shared NumPy/FLINT; source, ideal-projection, half-level and contraction-descent WRITTEN inputs require independent scientific review. No target dimension at parameter1or2, parent, formal/kernel, configured-family/human, library or novelty acceptance.'}
    output=args.certificate.removesuffix('-v1.json')+'-replay-v1.json'
    with (ROOT/output).open('x') as stream:json.dump(result,stream,indent=2);stream.write('\n')
    print('PASS entire firstrows and full small invariant sources',output,flush=True)


if __name__=='__main__':main()
