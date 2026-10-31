#!/usr/bin/env python3
"""Entire L6 lowest-source contraction by ALL eight negative local directions.

Omega(x)=sum_ij (G^-1)_ij [u_i,[w_j,x]], w_j=-theta(u_j).
For f1x=f2x=0 every [w_j,x] is a stated f1/f2 word on [f3,x].
Consequently D3x=0 IMPLIES Omega(x)=0. Invertible Omega is sufficient,
not necessary, for full original primitive injectivity. It is NOT a selected
positive-root row left test. No self-adjointness or scalar-Casimir is assumed.
All word arithmetic below is integral after EXPLICIT uniform denominator
clearing. Matrix membership is checked in the ENTIRE free primitive basis.
"""
import argparse
import hashlib
import importlib.util
import json
import math
from fractions import Fraction as Q
from functools import lru_cache
from pathlib import Path

ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('original_coordinate_tools',ROOT/'frontier-20261028-level6-coordinate-row-quotient.py')
original=importlib.util.module_from_spec(spec)
spec.loader.exec_module(original)
levi=original.levi
lift=original.lift
flint=original.flint
ACTION={g:[{int(j):int(2*c) for j,c in row.items()} for row in levi.ACTIONS[g]] for g in ('f1','f2','e1','e2','e12')}
assert all(Q(c).denominator<=2 and 2*Q(c)==int(2*Q(c)) for rows in levi.ACTIONS.values() for row in rows for c in row.values())
GINV=[[Q(int(i==j)) for j in range(8)] for i in range(8)]
GINV[3][3]=GINV[4][4]=Q(2,3)
GINV[3][4]=GINV[4][3]=Q(-1,3)
GINV[7][7]=Q(1,4)


def plus(out,vector,scale=1):
    assert isinstance(scale,int)
    for w,c in vector.items():
        out[w]=out.get(w,0)+scale*c
        if not out[w]:
            del out[w]
    return out


@lru_cache(None)
def standard(word):
    v=lift.lyndon_bracket(word)
    assert v and min(v)==word and v[word]==1 and all(Q(c).denominator==1 for c in v.values())
    return {w:int(c) for w,c in v.items()}


def decompose_integer(vector):
    rem=dict(vector)
    coords={}
    while rem:
        word=min(rem)
        assert lift.is_lyndon(word), 'canonical output escaped free Lie algebra'
        c=rem[word]
        coords[word]=coords.get(word,0)+c
        plus(rem,standard(word),-c)
    return coords


def action2(v,g):
    out={}
    for word,c in v.items():
        for position,j in enumerate(word):
            for new,b in ACTION[g][j].items():
                w=word[:position]+(new,)+word[position+1:]
                out[w]=out.get(w,0)+c*b
                if not out[w]:
                    del out[w]
    return out


def f12_4(v):
    # f12=[f2,f1]; each f_i is represented here by TWICE its action.
    return plus(action2(action2(v,'f1'),'f2'),action2(action2(v,'f2'),'f1'),-1)


def suffix_d3_2(v,r,s):
    out={}
    tails={}
    local=({'h3':-1},{'e1':-r},{'e2':-s},{'e12':-(r+s)},{'e12':-s},{},{},{})
    for word,c in v.items():
        for k,j in enumerate(word):
            shorter=word[:k]+word[k+1:]
            for g,b in local[j].items():
                key=(shorter,g)
                tails[key]=tails.get(key,0)+c*b
                for ell in range(k+1,len(word)):
                    position=ell-1
                    if g=='h3':
                        a0,b0=levi.WEIGHTS[word[ell]]
                        choices={word[ell]:2*(2-r*a0-s*b0)}
                    else:
                        choices=ACTION[g][word[ell]]
                    for new,co in choices.items():
                        w=shorter[:position]+(new,)+shorter[position+1:]
                        out[w]=out.get(w,0)+c*b*co
                        if not out[w]:
                            del out[w]
    assert not any(tails.values()), 'uncancelled right Cartan tail'
    return out


def canonical_96(d):
    h=f12_4(d)
    # Pairs are integer numerator / denominator. Every numerator is linear
    # in the original d; NO primitive normalization is allowed here.
    negative=[(d,1),({w:-c for w,c in action2(d,'f1').items()},2),
              ({w:-c for w,c in action2(d,'f2').items()},2),({w:-c for w,c in h.items()},4),
              (action2(action2(d,'f2'),'f1'),4),(action2(h,'f1'),8),(action2(h,'f2'),8),
              ({w:-c for w,c in action2(action2(h,'f2'),'f1').items()},8)]
    out={}
    for i in range(8):
        for j in range(8):
            factor=96*GINV[i][j]/negative[j][1]
            assert factor.denominator==1
            factor=int(factor)
            if not factor:
                continue
            for word,c in negative[j][0].items():
                left=(i,)+word
                right=word+(i,)
                out[left]=out.get(left,0)+factor*c
                out[right]=out.get(right,0)-factor*c
    return {w:c for w,c in out.items() if c}


def qmatrix(rows):
    return flint.fmpq_mat([[flint.fmpq(Q(c).numerator,Q(c).denominator) for c in row] for row in rows])


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--a',type=int,required=True)
    ap.add_argument('--b',type=int,required=True)
    args=ap.parse_args()
    name=f'frontier-20261028-level6-free-{args.a}{args.b}-pencil-v1.json'
    raw=(ROOT/name).read_bytes()
    P=json.loads(raw)
    a,b,n=P['degree']
    assert (a,b,n)==(args.a,args.b,6)
    path=ROOT/f'frontier-20261029-level6-{a}{b}-canonical-contraction-pencil-v1.json'
    if path.exists():
        raise FileExistsError(path)
    words=[tuple(map(int,w)) for w in P['source_words']]
    assert len(words)==original.weight_dimension(a,b) and words==sorted(set(words))
    assert all(lift.is_lyndon(w) and levi.degree(w)==(a,b,6) for w in words)
    coefs=[{int(j):Q(c) for j,c in co.items() if Q(c)} for co in P['horizontal_kernel_coefficients']]
    k=len(coefs)
    assert k==original.lowest_multiplicity(a,b)
    free_indices=[max(co) for co in coefs]
    assert len(set(free_indices))==k
    assert all(co.get(j,0)==int(i==q) for i,co in enumerate(coefs) for q,j in enumerate(free_indices))
    primitive_matrix=qmatrix([[co.get(j,0) for co in coefs] for j in range(len(words))])
    matrix_columns=[[],[],[]]
    all_coordinate_columns=[[],[],[]]
    for col,co in enumerate(coefs):
        den=math.lcm(*(c.denominator for c in co.values()))
        source={}
        for j,c in co.items():
            plus(source,standard(words[j]),int(c*den))
        assert source and not action2(source,'f1') and not action2(source,'f2')
        for index,(r,s) in enumerate(((6,6),(7,6),(6,7))):
            d=suffix_d3_2(source,r,s)
            output=canonical_96(d)
            assert not action2(output,'f1') and not action2(output,'f2'), 'full contraction not horizontal'
            coords=decompose_integer(output)
            assert set(coords)<=set(words)
            normalization=den*192
            all_coordinate_columns[index].append({word:Q(c,normalization) for word,c in coords.items()})
            matrix_columns[index].append([Q(coords.get(words[j],0),normalization) for j in free_indices])
        if (col+1)%20==0 or col+1==k:
            print('canonical full negative source',a,b,col+1,'of',k,flush=True)
    matrices=[]
    for columns,images in zip(matrix_columns,all_coordinate_columns):
        matrix=[list(row) for row in zip(*columns)]
        full=[[images[j].get(w,Q(0)) for j in range(k)] for w in words]
        assert primitive_matrix*qmatrix(matrix)==qmatrix(full), 'canonical output not exactly in entire primitive basis'
        matrices.append(matrix)
    triples=[[[matrices[0][i][j],matrices[1][i][j]-matrices[0][i][j],matrices[2][i][j]-matrices[0][i][j]] for j in range(k)] for i in range(k)]
    with path.open('x') as stream:
        json.dump({'owner':'MathKacMoody-2','degree':[a,b,6],'variable_meaning':'x=r-6,y=s-6','source_pencil':name,
                   'source_pencil_sha256':hashlib.sha256(raw).hexdigest(),'entire_primitive_dimension':k,
                   'source_primitive_free_coordinate_indices':free_indices,'matrix':[[[str(c) for c in e] for e in row] for row in triples],
                   'Gram_inverse':[[str(c) for c in row] for row in GINV],
                   'negative_words':['f3','-f1 f3','-f2 f3','-f12 f3','f1 f2 f3','f1 f12 f3','f2 f12 f3','-2 f1 f2 f12 f3'],
                   'exact_checks':{'all_free_primitive_membership_and_Witt_Weyl_dimensions':True,'all_right_Cartan_tails_cancel':True,
                                   'all_contracted_images_horizontal':True,'all_three_full_coordinate_matrix_products_match':True},
                   'status':'EXACT_COMPLETE_CANONICAL_CONTRACTION_PENCIL_ONLY',
                   'limits':'D3 kernel implies canonical kernel, not conversely. No self-adjointness, scalar-Casimir, polynomial sign, original-map theorem, formal/kernel or parent acceptance inferred.'},stream,indent=2)
        stream.write('\n')
    print('WROTE',path.name,'dimension',k,flush=True)


if __name__=='__main__':
    main()
