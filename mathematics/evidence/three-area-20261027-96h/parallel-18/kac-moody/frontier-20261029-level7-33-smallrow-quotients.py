#!/usr/bin/env python3
"""Complete fixed-seed projections, first/two-row pencils and all small corners.

The entire normalized270-source and compact Gram are pinned inputs. ALL
root-matching fixed-seed descendants are included, not chosen kernel vectors.
Nonvanishing tests may be inconclusive; zero certificates are not D3 kernels.
"""
import argparse
import hashlib
import io
import itertools
import json
import math
import sys
from collections import Counter
from fractions import Fraction as Q
from pathlib import Path

import numpy as np

ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'frontier-20261028-fastalgebra'))
import flint

COMPACT='frontier-20261029-level7-33-compact-source-v1.json'
PENCIL='frontier-20261029-level7-33-canonical-contraction-pencil-v1.json'
PENCIL_SHA='5ea001c72af7b557ba8dfb89902c14828e9f9f49614b6d522833f40626bc254c'
WEIGHTS=((0,0),(1,0),(0,1),(1,1),(1,1),(2,1),(1,2),(2,2))


def pin(name,expected):
    raw=(ROOT/name).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==expected
    return json.loads(raw)


def array(p):
    raw=(ROOT/p['file']).read_bytes();assert hashlib.sha256(raw).hexdigest()==p['sha256']
    stream=io.BytesIO(raw);a=np.load(stream,allow_pickle=False)
    assert stream.tell()==len(raw)
    return a


def mat(rows):return flint.fmpq_mat([[flint.fmpq(str(x)) for x in row] for row in rows])
def strings(M):return [[str(M[i,j]) for j in range(M.ncols())] for i in range(M.nrows())]
def select(M,rows,cols):
    rows=tuple(rows);cols=tuple(cols)
    return flint.fmpq_mat(len(rows),len(cols),[M[i,j] for i in rows for j in cols])


def ideal_basis(H,cross):
    rr,rank=flint.fmpq_mat(cross.tolist()).rref()
    columns=[next(j for j in range(cross.shape[1]) if rr[i,j]) for i in range(rank)]
    coordinates=H.solve(flint.fmpq_mat(cross[:,columns].tolist()))
    reduced,r=coordinates.transpose().rref();assert r==rank
    I=mat([[reduced[j,i] for j in range(rank)] for i in range(270)])
    pivots=[next(i for i in range(270) if reduced[j,i]) for j in range(rank)]
    free=[i for i in range(270) if i not in pivots]
    return I,pivots,free


def induced(A,I,pivots,free):
    AI=A*I
    T=select(AI,pivots,range(I.ncols()))
    assert AI==I*T,'whole ideal not contraction-stable'
    return select(A,free,free)-select(I,free,range(I.ncols()))*select(A,pivots,free)


def seed_family(node,parameter,codes,metric):
    generators=[];cross=[];depth=6-parameter
    peak=max(abs(int(metric.min())),abs(int(metric.max())))
    for outer in itertools.product(range(8),repeat=depth):
        if (sum(WEIGHTS[a][0] for a in outer)+WEIGHTS[node][0],
            sum(WEIGHTS[a][1] for a in outer)+WEIGHTS[node][1])!=(3,3):continue
        poly={node<<(3*i):(-1)**(i+1)*math.comb(parameter,i) for i in range(parameter+1)}
        length=parameter+1
        for a in reversed(outer):
            out=Counter()
            for w,c in poly.items():out[(a<<(3*length))|w]+=c;out[(w<<3)|a]-=c
            poly={w:c for w,c in out.items() if c};length+=1
        assert length==7
        ix=np.searchsorted(codes,np.array(list(poly),dtype=np.uint32))
        assert all(int(codes[i])==w for i,w in zip(ix,poly))
        coefs=np.array(list(poly.values()),dtype=np.int64)
        assert peak*sum(abs(int(c)) for c in coefs)<2**63
        cross.append(metric[:,ix]@coefs)
        generators.append({'node':node,'parameter':parameter,'outer_letters':list(outer),
                           'whole_word_terms':[[int(w),int(c)] for w,c in sorted(poly.items())]})
    return generators,np.array(cross,dtype=np.int64).T


def determinant_polynomial(A,B):
    k=A.nrows();row_scales=[];integers=[]
    for i in range(k):
        scale=math.lcm(*(int(M[i,j].denominator) for M in (A,B) for j in range(k)))
        row_scales.append(scale)
        integers.append([[int(A[i,j]*scale),int(B[i,j]*scale)] for j in range(k)])
    values=[int(flint.fmpz_mat([[a+t*b for a,b in row] for row in integers]).det()) for t in range(k+1)]
    work=values[:];differences=[]
    while work:differences.append(work[0]);work=[b-a for a,b in zip(work,work[1:])]
    factorial=math.factorial(k);out=[0]*(k+1);falling=[1]
    for order,d in enumerate(differences):
        multiplier=d*(factorial//math.factorial(order))
        for i,c in enumerate(falling):out[i]+=multiplier*c
        following=[0]*(len(falling)+1)
        for i,c in enumerate(falling):following[i]-=order*c;following[i+1]+=c
        falling=following
    row_scale_product=math.prod(row_scales)
    denominator=factorial*row_scale_product
    coefficients=[Q(c,denominator) for c in out]
    for t,v in enumerate(values):
        z=Q(0)
        for c in reversed(coefficients):z=z*t+c
        assert z*row_scale_product==v
    return coefficients


def translate(coefficients,delta):
    return [sum((c*math.comb(j,i)*delta**(j-i) for j,c in enumerate(coefficients) if j>=i),Q(0)) for i in range(len(coefficients))]


def main():
    if not __debug__:raise RuntimeError('assertions disabled')
    ap=argparse.ArgumentParser();ap.add_argument('--compact-sha256',required=True)
    args=ap.parse_args()
    output=ROOT/'frontier-20261029-level7-33-smallrow-quotients-v1.json'
    if output.exists():raise FileExistsError(output)
    C=pin(COMPACT,args.compact_sha256);P=pin(PENCIL,PENCIL_SHA)
    assert C['degree']==P['degree']==[3,3,7]
    codes,V=[array(p) for p in C['files']]
    assert codes.dtype==np.dtype('uint32') and V.dtype==np.dtype('int64') and V.shape==(270,5376)
    metric=V.copy();lookup={int(w):i for i,w in enumerate(codes)}
    maximum=max(abs(int(V.min())),abs(int(V.max())))
    for pos in range(7):
        assert maximum*4**(pos+1)<2**63
        shift=3*(6-pos);letters=(codes>>shift)&7
        c3=np.flatnonzero(letters==3);c4=np.array([lookup[int(codes[i])^(7<<shift)] for i in c3],dtype=np.int64)
        a=metric[:,c3].copy();b=metric[:,c4].copy()
        metric[:,c3]=2*a+b;metric[:,c4]=a+2*b;metric[:,np.flatnonzero(letters==7)]*=4
    H=mat(C['source_gram']);den=C['row_denominators']
    fields=[]
    for part in range(3):
        fields.append(mat([[flint.fmpq(P['matrix'][i][j][part])*den[j]/den[i] for j in range(270)] for i in range(270)]))
    ideals={};families=[];expected_counts={1:400,2:144,3:39,4:6}
    for node in (1,2):
        for parameter in (1,2,3,4):
            generators,cross=seed_family(node,parameter,codes,metric)
            assert len(generators)==expected_counts[parameter]
            I,pivots,free=ideal_basis(H,cross)
            entry={'node':node,'parameter':parameter,'all_generators':generators,'all_cross_inner_products':cross.tolist(),
                   'whole_projected_ideal_rank':I.ncols(),'ideal_basis':strings(I),'ideal_pivot_coordinates':pivots,'complement_coordinates':free}
            ideals[node,parameter]=(I,pivots,free,cross)
            if parameter<=2:
                A=fields[0]+(parameter-7)*fields[1]+(3-7)*fields[2] if node==1 else fields[0]+(3-7)*fields[1]+(parameter-7)*fields[2]
                B=fields[2] if node==1 else fields[1]
                QA=induced(A,I,pivots,free);QB=induced(B,I,pivots,free)
                coefficients=determinant_polynomial(QA,QB)
                translations=[]
                for other_bound in (3,4,5):
                    shifted=translate(coefficients,other_bound-3)
                    positive=sum(c>0 for c in shifted);negative=sum(c<0 for c in shifted)
                    sign=1 if positive and not negative else -1 if negative and not positive else 0
                    translations.append({'other_bound':other_bound,'coefficient_sign':sign,'nonzero_constant':bool(shifted[0]),'coefficients':[str(c) for c in shifted]})
                entry.update({'quotient_affine_variable':'t=other_parameter-3','quotient_affine_matrix':[[[str(QA[i,j]),str(QB[i,j])] for j in range(len(free))] for i in range(len(free))],
                              'determinant_coefficients_at_other3':[str(c) for c in coefficients],'positive_translation_tests':translations})
                print('WHOLE smallrow quotient',node,parameter,'dimension',len(free),'positive-translations',[(x['other_bound'],x['coefficient_sign'],x['nonzero_constant']) for x in translations],flush=True)
            else:print('WHOLE smallrow ideal',node,parameter,'rank',I.ncols(),flush=True)
            families.append(entry)
    corners=[]
    for r in range(1,5):
        for s in range(1,5):
            cross=np.concatenate((ideals[1,r][3],ideals[2,s][3]),axis=1)
            I,pivots,free=ideal_basis(H,cross)
            A=fields[0]+(r-7)*fields[1]+(s-7)*fields[2]
            Qbar=induced(A,I,pivots,free)
            determinant=Qbar.det()
            corners.append({'parameters':[r,s],'whole_ideal_rank':I.ncols(),'actual_primitive_dimension':len(free),
                            'entire_quotient_contraction_matrix':strings(Qbar),'determinant':str(determinant),'nonzero':bool(determinant)})
            print('ENTIRE small corner',r,s,'source',len(free),'contraction nonzero',bool(determinant),flush=True)
    result={'owner':'MathKacMoody-2','degree':[3,3,7],'compact_source':{'file':COMPACT,'sha256':args.compact_sha256},
            'canonical_pencil':{'file':PENCIL,'sha256':PENCIL_SHA},'normalized_basis_change':C['canonical_matrix_change'],
            'families':families,'complete_small_corners':corners,'program_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'numpy_version':np.__version__,'flint_version':flint.__version__,
            'status':'COMPLETE_ENTIRE_SMALLROW_IDEALS_AND_CONTRACTION_TESTS_CANDIDATE',
            'ordinary_recovery':'The initial run stopped before publishing any artifact at a zero-dimensional corner because the nested-list matrix constructor lost its0xN shape. The general indexed constructor now preserves both dimensions, including zero; no mathematical exception or failed corner was suppressed.',
            'limits':'Same-owner producer; alternate complete source/Gram/seed/quotient/polynomial reconstruction and scientific review required. Zero free or quotient contraction is not an actual D3 kernel. Actual-source, whole-lowest-ideal projection and descent mathematics remain substantive inputs. No parent, formal/kernel, configured-family/human, native-library, B7/all-level or novelty acceptance.'}
    with output.open('x') as stream:json.dump(result,stream,indent=2);stream.write('\n')
    print('WROTE complete entire root33 smallrow assay',output.name,flush=True)


if __name__=='__main__':main()
