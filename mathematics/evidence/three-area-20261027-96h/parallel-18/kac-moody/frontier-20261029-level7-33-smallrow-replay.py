#!/usr/bin/env python3
"""Alternate whole root33 seed-ideal, quotient-pencil and corner replay.

NO producer is imported. Tuple bracket trees/repeated seed adjoints replace
packed-word/binomial seeds; sparse G-on-descendants replaces G-on-source.
Transpose evaluation-space RREF replaces selected-column extraction; explicit
annihilator/source-lift maps replace the producer's quotient block formula.
"""
import argparse
import hashlib
import importlib.util
import itertools
import json
import math
from collections import Counter
from fractions import Fraction as Q
from pathlib import Path

import numpy as np

ROOT=Path(__file__).resolve().parent
LITERAL='frontier-20261029-invariant-actual22-corner-replay.py'
LITERAL_SHA='a1cf8aa7d4b085384bdc48e01978bd56f20beff5c4b8faf9b61eea3621b6d8d6'
COMPACT_REPLAY='frontier-20261029-level7-33-compact-source-replay-v1.json'
COMPACT_REPLAY_SHA='0a4cebf078d7770a61c65c72f42da1971eaec574dd2f3812e6fa13a5fa6f824c'


def load_literal():
    raw=(ROOT/LITERAL).read_bytes();assert hashlib.sha256(raw).hexdigest()==LITERAL_SHA
    spec=importlib.util.spec_from_file_location('literal_matrices_and_tuple_brackets',ROOT/LITERAL)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    return module


def regenerate(L,node,parameter,V,G,degrees,lookup):
    q={(node,):1}
    for _ in range(parameter):q=L.bracket({(0,):1},q)
    q={w:-c for w,c in q.items()}
    generators=[];columns=[];depth=6-parameter
    maximum=max(abs(int(V.min())),abs(int(V.max())))
    for outer in itertools.product(range(8),repeat=depth):
        if (sum(degrees[a][0] for a in outer)+degrees[node][0],
            sum(degrees[a][1] for a in outer)+degrees[node][1])!=(3,3):continue
        y=q
        for a in reversed(outer):y=L.bracket({(a,):1},y)
        generators.append({'node':node,'parameter':parameter,'outer_letters':list(outer),
                           'whole_word_terms':[[L.code(w),int(c)] for w,c in sorted(y.items(),key=lambda z:L.code(z[0]))]})
        gy=Counter()
        for word,c in y.items():
            expansion={():c}
            for letter in word:
                expansion={prefix+(j,):value*G[j][letter]
                           for prefix,value in expansion.items() for j in range(8) if G[j][letter]}
            for w,value in expansion.items():gy[L.code(w)]+=value
        gy={w:c for w,c in gy.items() if c}
        indices=np.array([lookup[w] for w in gy],dtype=np.int64)
        coefficients=np.array(list(gy.values()),dtype=np.int64)
        assert maximum*sum(abs(int(c)) for c in coefficients)<2**63
        columns.append(V[:,indices]@coefficients)
    assert len(generators)=={1:400,2:144,3:39,4:6}[parameter]
    return generators,np.array(columns,dtype=np.int64).T


def canonical_ideal(F,H,cross):
    # Every evaluation vector is included; extract a basis of its entire
    # transpose row space BEFORE solving the source Gram system.
    rr,rank=F.fmpq_mat(cross.T.tolist()).rref()
    evaluation_basis=F.fmpq_mat(270,rank,[rr[j,i] for i in range(270) for j in range(rank)])
    projected=H.solve(evaluation_basis)
    basis,r=projected.transpose().rref();assert r==rank
    I=F.fmpq_mat(270,rank,[basis[j,i] for i in range(270) for j in range(rank)])
    pivots=[next(i for i in range(270) if basis[j,i]) for j in range(rank)]
    free=[i for i in range(270) if i not in pivots]
    return I,pivots,free


def quotient_maps(F,I,pivots,free):
    q=len(free);d=I.ncols()
    covectors=F.fmpq_mat(q,270)
    lifts=F.fmpq_mat(270,q)
    for j,f in enumerate(free):
        covectors[j,f]=1;lifts[f,j]=1
        for k,p in enumerate(pivots):covectors[j,p]=-I[f,k]
    assert covectors*I==F.fmpq_mat(q,d)
    identity=F.fmpq_mat(q,q,[int(i==j) for i in range(q) for j in range(q)])
    assert covectors*lifts==identity
    return covectors,lifts


def induced(F,A,I,covectors,lifts):
    assert covectors*A*I==F.fmpq_mat(covectors.nrows(),I.ncols())
    return covectors*A*lifts


def translate_integers(coefficients,delta):
    denominator=math.lcm(*(c.denominator for c in coefficients))
    nums=[int(c*denominator) for c in coefficients]
    return [Q(sum(nums[j]*math.comb(j,i)*delta**(j-i) for j in range(i,len(nums))),denominator)
            for i in range(len(nums))]


def main():
    if not __debug__:raise RuntimeError('assertions disabled')
    ap=argparse.ArgumentParser();ap.add_argument('--sha256',required=True);args=ap.parse_args()
    L=load_literal();F=L.flint
    name='frontier-20261029-level7-33-smallrow-quotients-v1.json'
    C=json.loads(L.pinned({'file':name,'sha256':args.sha256}))
    compact=json.loads(L.pinned(C['compact_source']))
    completed=json.loads(L.pinned({'file':COMPACT_REPLAY,'sha256':COMPACT_REPLAY_SHA}))
    assert completed['status']=='PASS_ENTIRE_NORMALIZED270_SOURCE_BYTES_AND_HADAMARD_GRAM'
    assert completed['input_sha256']==C['compact_source']['sha256']
    assert C['degree']==compact['degree']==[3,3,7]
    P=json.loads(L.pinned(C['canonical_pencil']))
    assert P['degree']==[3,3,7] and P['source_pencil_sha256']==compact['source']['sha256']
    codes,V=[L.array(pin) for pin in compact['files']]
    assert codes.dtype==np.dtype('uint32') and V.dtype==np.dtype('int64') and V.shape==(270,5376)
    lookup={int(w):i for i,w in enumerate(codes)}
    G,degrees=L.literal_module();H=L.matrix(compact['source_gram']);den=compact['row_denominators']
    fields=[L.matrix([[F.fmpq(P['matrix'][i][j][part])*den[j]/den[i] for j in range(270)] for i in range(270)]) for part in range(3)]
    assert len(C['families'])==8
    crosses={};ranks={};matrix_grid_count=0;positive_terms=0;ideal_vector_count=0
    oriented_polynomials={}
    for expected,family in zip(itertools.product((1,2),(1,2,3,4)),C['families']):
        node,parameter=expected
        assert (family['node'],family['parameter'])==expected
        generators,cross=regenerate(L,node,parameter,V,G,degrees,lookup)
        assert generators==family['all_generators'] and cross.tolist()==family['all_cross_inner_products']
        I,pivots,free=canonical_ideal(F,H,cross)
        assert I.ncols()==family['whole_projected_ideal_rank']
        assert L.strings(I)==family['ideal_basis']
        assert pivots==family['ideal_pivot_coordinates'] and free==family['complement_coordinates']
        crosses[expected]=cross;ranks[expected]=I.ncols();ideal_vector_count+=len(generators)
        if parameter<=2:
            A=fields[0]+(parameter-7)*fields[1]-4*fields[2] if node==1 else fields[0]-4*fields[1]+(parameter-7)*fields[2]
            B=fields[2] if node==1 else fields[1]
            covectors,lifts=quotient_maps(F,I,pivots,free)
            QA=induced(F,A,I,covectors,lifts);QB=induced(F,B,I,covectors,lifts)
            q=len(free)
            assert [[[str(QA[i,j]),str(QB[i,j])] for j in range(q)] for i in range(q)]==family['quotient_affine_matrix']
            coefficients=[Q(c) for c in family['determinant_coefficients_at_other3']]
            assert len(coefficients)==q+1 and coefficients[0]>0 and all(c>=0 for c in coefficients)
            assert family['quotient_affine_variable']=='t=other_parameter-3'
            for i in range(q+1):
                t=i-2;value=Q(0)
                for c in reversed(coefficients):value=value*t+c
                assert value==Q(str((QA+t*QB).det()))
                matrix_grid_count+=1
            assert len(family['positive_translation_tests'])==3
            for bound,entry in zip((3,4,5),family['positive_translation_tests']):
                assert entry['other_bound']==bound and entry['coefficient_sign']==1 and entry['nonzero_constant'] is True
                assert translate_integers(coefficients,bound-3)==[Q(c) for c in entry['coefficients']]
            oriented_polynomials[expected]=coefficients;positive_terms+=sum(c>0 for c in coefficients)
        print('PASS ENTIRE root33 seed family',node,parameter,'descendants',len(generators),'rank',I.ncols(),'quotient',len(free),flush=True)
    assert ideal_vector_count==1178
    for parameter in (1,2):assert oriented_polynomials[1,parameter]==oriented_polynomials[2,parameter]
    assert len(C['complete_small_corners'])==16
    corner_dimensions=[]
    for (r,s),corner in zip(itertools.product(range(1,5),repeat=2),C['complete_small_corners']):
        assert corner['parameters']==[r,s]
        cross=np.concatenate((crosses[1,r],crosses[2,s]),axis=1)
        I,pivots,free=canonical_ideal(F,H,cross)
        assert I.ncols()==corner['whole_ideal_rank'] and len(free)==corner['actual_primitive_dimension']
        covectors,lifts=quotient_maps(F,I,pivots,free)
        Qbar=induced(F,fields[0]+(r-7)*fields[1]+(s-7)*fields[2],I,covectors,lifts)
        assert L.strings(Qbar)==corner['entire_quotient_contraction_matrix']
        determinant=Qbar.det()
        assert determinant and str(determinant)==corner['determinant'] and corner['nonzero'] is True
        corner_dimensions.append(len(free))
        print('PASS ENTIRE root33 ACTUAL corner',r,s,'source',len(free),'nonzero quotient contraction',flush=True)
    result={'owner':'MathKacMoody-2','input_file':name,'input_sha256':args.sha256,
            'compact_source':C['compact_source'],'compact_source_completed_replay':{'file':COMPACT_REPLAY,'sha256':COMPACT_REPLAY_SHA},
            'canonical_pencil':C['canonical_pencil'],'literal_matrix_helper':{'file':LITERAL,'sha256':LITERAL_SHA},
            'all_fixed_seed_descendants_reconstructed':ideal_vector_count,'all8_entire_ideal_ranks':[[n,p,ranks[n,p]] for n,p in sorted(ranks)],
            'all4_entire_affine_quotient_pencils_reconstructed':True,
            'firstrow_dimensions':[51,51],'secondrow_dimensions':[148,148],
            'positive_coefficients_in_base_polynomials':positive_terms,
            'shifted_complete_matrix_determinant_comparisons':matrix_grid_count,
            'base_polynomial_domain':'other_parameter>=3',
            'all_redundant_other4_other5_translations_verified':True,
            'mirror_polynomials_identical':True,'entire_actual_small_corner_determinants_recomputed':16,
            'actual4x4_source_dimensions':[corner_dimensions[i:i+4] for i in range(0,16,4)],
            'program_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'numpy_version':np.__version__,'flint_version':F.__version__,
            'status':'PASS_ALL_ENTIRE_ROOT33_SMALLROW_IDEALS_PENCILS_AND16_ACTUAL_CORNERS',
            'limits':'Entire normalized source/Gram and earlier whole free canonical pencil replays are reused and bound, not rerun. Alternate complete tuple/sparse-metric/transpose-RREF/annihilator quotient algorithms; same owner and NumPy/FLINT libraries. Actual source, projection and contraction-descent WRITTEN proofs require disjoint scientific review. No B7/all-level, parent, formal/kernel, configured-family/human, native-library, status/novelty/priority acceptance.'}
    output=ROOT/'frontier-20261029-level7-33-smallrow-replay-v1.json'
    with output.open('x') as stream:json.dump(result,stream,indent=2);stream.write('\n')
    print('PASS all complete root33 smallrows and16 actual corners',output.name,flush=True)


if __name__=='__main__':main()
