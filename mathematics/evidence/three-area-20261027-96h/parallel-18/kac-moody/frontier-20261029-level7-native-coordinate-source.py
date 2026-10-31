#!/usr/bin/env python3
"""Generate a COMPLETE level7 source via native faithful Lyndon-coordinate nullspace.

This is a bounded scientific slice, not a whole-level7 claim. Exact sparse
joint f1/f2 nullspace is solved in the entire specified free weight space.
All primitive combinations, full canonical images and coordinate membership
are checked before either new artifact is written. Existing files are refused.
The actual source is free for r,s>=7 at the named free-Levi/PBW interfaces.
"""
import argparse
import hashlib
import importlib.util
import json
import math
from collections import Counter
from fractions import Fraction as Q
from pathlib import Path

ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('full_integer_canonical',ROOT/'frontier-20261029-level6-canonical-contraction.py')
canonical=importlib.util.module_from_spec(spec)
spec.loader.exec_module(canonical)
levi=canonical.levi
lift=canonical.lift


def dimensions(a,b):
    ch=Counter({(0,0):1})
    for _ in range(7):
        following=Counter()
        for (u,v),c in ch.items():
            for i,j in levi.WEIGHTS:
                following[u+i,v+j]+=c
        ch=following
    for i,j in levi.WEIGHTS:
        ch[7*i,7*j]-=1
    assert all(c>=0 and c%7==0 for c in ch.values())
    ch=Counter({degree:c//7 for degree,c in ch.items() if c})
    assert sum(ch.values())==(8**7-8)//7==299592
    lowest=ch[a,b]-ch[a-1,b]-ch[a,b-1]+ch[a-2,b-1]+ch[a-1,b-2]-ch[a-2,b-2]
    return ch[a,b],lowest


def publish(path,record):
    with path.open('x') as stream:
        json.dump(record,stream,indent=2)
        stream.write('\n')
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--a',type=int,required=True)
    ap.add_argument('--b',type=int,required=True)
    ap.add_argument('--max-weight',type=int,default=1500)
    ap.add_argument('--max-primitive',type=int,default=400)
    args=ap.parse_args()
    degree=(args.a,args.b,7)
    size,k=dimensions(args.a,args.b)
    assert 0<k<=args.max_primitive and 0<size<=args.max_weight, 'explicit complete-type scientific size bound exceeded'
    source_name=f'frontier-20261029-level7-{args.a}{args.b}-complete-primitive-source-v1.json'
    source_path=ROOT/source_name
    pencil_path=ROOT/f'frontier-20261029-level7-{args.a}{args.b}-canonical-contraction-pencil-v1.json'
    if source_path.exists() or pencil_path.exists():
        raise FileExistsError('refusing to replace either existing source/pencil artifact')
    basis=levi.lie_basis(degree)
    assert len(basis)==size
    columns=[]
    for word,v in basis:
        integer={w:int(c) for w,c in v.items()}
        assert all(Q(c).denominator==1 for c in v.values())
        column={}
        for index,g in enumerate(('f1','f2')):
            # TWICE each actual finite-Levi action; independent monic-Lyndon
            # decomposition is faithful and never discards word coefficients.
            image=canonical.action2(integer,g)
            coordinates=canonical.decompose_integer(image)
            column.update({(index,w):c for w,c in coordinates.items()})
        columns.append(column)
    labels=sorted({w for column in columns for w in column})
    action=canonical.flint.fmpz_mat([[column.get(w,0) for column in columns] for w in labels])
    nullspace,nullity=action.nullspace()
    assert nullity==k
    # Reverse word-coordinate order BEFORE canonical RREF, retaining the
    # same maximal-free-coordinate identity used by the existing certificates.
    rows=canonical.flint.fmpq_mat([[canonical.flint.fmpq(nullspace[size-1-j,i]) for j in range(size)] for i in range(k)])
    reduced,rank=rows.rref(inplace=True)
    assert rank==k
    coefficients=[]
    for i in range(k):
        co={size-1-j:Q(int(reduced[i,j].numerator),int(reduced[i,j].denominator)) for j in range(size) if reduced[i,j]}
        coefficients.append(co)
    assert len(coefficients)==k
    print('NATIVE COMPLETE source',degree,'weight',size,'target coordinates',len(labels),'nullity',nullity,flush=True)
    free=[max(co) for co in coefficients]
    assert len(set(free))==k
    assert all(co.get(j,0)==int(i==q) for i,co in enumerate(coefficients) for q,j in enumerate(free))
    primitive_matrix=canonical.qmatrix([[co.get(j,0) for co in coefficients] for j in range(size)])
    matrices=[]
    for r,s in ((7,7),(8,7),(7,8)):
        image_columns=[]
        full_columns=[]
        for co in coefficients:
            den=math.lcm(*(Q(c).denominator for c in co.values()))
            vector={}
            for j,c in co.items():
                canonical.plus(vector,canonical.standard(basis[j][0]),int(c*den))
            assert vector and not canonical.action2(vector,'f1') and not canonical.action2(vector,'f2')
            output=canonical.canonical_96(canonical.suffix_d3_2(vector,r,s))
            assert not canonical.action2(output,'f1') and not canonical.action2(output,'f2')
            coords=canonical.decompose_integer(output)
            normalization=den*192
            full_columns.append({w:Q(c,normalization) for w,c in coords.items()})
            image_columns.append([Q(coords.get(basis[j][0],0),normalization) for j in free])
        M=[list(row) for row in zip(*image_columns)]
        full=[[col.get(w,Q(0)) for col in full_columns] for w,v in basis]
        assert primitive_matrix*canonical.qmatrix(M)==canonical.qmatrix(full)
        matrices.append(M)
        print('COMPLETE grade7 canonical',degree,r,s,'weight',size,'primitive',k,flush=True)
    source={'owner':'MathKacMoody-2','degree':list(degree),'variables':'x=r-7,y=s-7','source_words':[''.join(map(str,w)) for w,v in basis],
            'horizontal_kernel_coefficients':[{str(j):str(c) for j,c in sorted(co.items())} for co in coefficients],
            'joint_horizontal_kernel_dim':k,'complete_character_free_weight_dimension':size,'complete_character_lowest_multiplicity':k,
            'level7_total_free_dimension':299592,'source_generation':'complete exact native Lyndon-coordinate f1/f2 nullspace, then EVERY primitive independently checked in full word coordinates; exact coordinate independence plus Witt/Weyl completeness',
            'native_horizontal_target_coordinate_count':len(labels),
            'scope':'ENTIRE specified root primitive source; actual free source on r,s>=7 under named actual free-Levi/PBW transport. NOT whole level7 or B7.'}
    source_sha=publish(source_path,source)
    triples=[[[matrices[0][i][j],matrices[1][i][j]-matrices[0][i][j],matrices[2][i][j]-matrices[0][i][j]] for j in range(k)] for i in range(k)]
    pencil={'owner':'MathKacMoody-2','degree':list(degree),'variable_meaning':'x=r-7,y=s-7','source_pencil':source_name,'source_pencil_sha256':source_sha,
            'entire_primitive_dimension':k,'source_primitive_free_coordinate_indices':free,'matrix':[[[str(c) for c in e] for e in row] for row in triples],
            'Gram_inverse':[[str(c) for c in row] for row in canonical.GINV],
            'negative_words':['f3','-f1 f3','-f2 f3','-f12 f3','f1 f2 f3','f1 f12 f3','f2 f12 f3','-2 f1 f2 f12 f3'],
            'all_three_complete_primitive_coordinate_products_matched':True,'status':'EXACT_NEXT_GRADE_CANONICAL_PENCIL_ONLY',
            'canonical_integer_helper_sha256':hashlib.sha256((ROOT/'frontier-20261029-level6-canonical-contraction.py').read_bytes()).hexdigest(),
            'limits':'D3-kernel containment, actual source transport, whole-quadrant polynomial, independent implementation and scientific review remain separate obligations. No global level7/B7, parent, formal/kernel or novelty acceptance.'}
    publish(pencil_path,pencil)
    print('WROTE',source_name,pencil_path.name,flush=True)


if __name__=='__main__':
    main()
