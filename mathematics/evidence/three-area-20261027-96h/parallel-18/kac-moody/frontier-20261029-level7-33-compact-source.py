#!/usr/bin/env python3
"""Faithful whole270-source tensor expansion and compact-Levi Gram.

Consumes the already independently replayed full rational Lyndon kernel.
Clears EACH basis-row denominator, recording the diagonal change of basis.
Integer NumPy operations have explicit pre-bounds; Gram products use FLINT
arbitrary integers rather than an overflowing int64 matrix product.
"""
import hashlib
import io
import json
import math
import sys
from collections import Counter
from fractions import Fraction as Q
from functools import lru_cache
from pathlib import Path

import numpy as np

ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'frontier-20261028-fastalgebra'))
import flint

SOURCE='frontier-20261029-level7-33-complete-primitive-source-v1.json'
SOURCE_SHA='26ae433281226f8fa2138dc0c4a63967b2037b798fa818cd3eb522743853533d'
REPLAY='frontier-20261029-level7-33-canonical-independent-replay-v1.json'
REPLAY_SHA='d352ee9226252abed29e92f4b45f15438d1e9d69218416dd0b9ce577acbf897e'
WEIGHTS=((0,0),(1,0),(0,1),(1,1),(1,1),(2,1),(1,2),(2,2))
PREFIX='frontier-20261029-level7-33-compact-source'


def pinned(name,expected):
    raw=(ROOT/name).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==expected
    return json.loads(raw)


def code(word):
    value=0
    for a in word:value=8*value+int(a)
    return value


def bracket(a,b):
    out=Counter()
    for u,x in a.items():
        for v,y in b.items():out[u+v]+=x*y;out[v+u]-=x*y
    return {w:c for w,c in out.items() if c}


def lyndon(word):
    return all(word<word[i:] for i in range(1,len(word)))


@lru_cache(None)
def expansion(word):
    assert lyndon(word)
    if len(word)==1:return {word:1}
    cut=next(i for i in range(1,len(word)) if lyndon(word[i:]))
    assert lyndon(word[:cut])
    out=bracket(expansion(word[:cut]),expansion(word[cut:]))
    assert min(out)==word and out[word]==1
    return out


def words():
    out=[]
    def visit(prefix,left,a,b):
        if min(a,b)<0 or max(a,b)>2*left:return
        if left==0:
            if a==b==0:out.append(code(prefix))
            return
        for j,(da,db) in enumerate(WEIGHTS):visit(prefix+(j,),left-1,a-da,b-db)
    visit((),7,3,3)
    assert len(out)==5376 and out==sorted(set(out))
    return np.array(out,dtype=np.uint32)


def main():
    if not __debug__:raise RuntimeError('assertions disabled')
    destinations=[ROOT/f'{PREFIX}-{kind}-v1.npy' for kind in ('words','vectors')]+[ROOT/f'{PREFIX}-v1.json']
    if any(p.exists() for p in destinations):raise FileExistsError('immutable compact-source destination exists')
    C=pinned(SOURCE,SOURCE_SHA);R=pinned(REPLAY,REPLAY_SHA)
    assert R['source_pencil_sha256']==SOURCE_SHA and R['all_free_source_membership_and_Witt_completeness_checked']
    assert C['degree']==[3,3,7] and C['joint_horizontal_kernel_dim']==270
    basis=C['source_words'];assert len(basis)==768 and basis==sorted(set(basis))
    codes=words();lookup={int(w):i for i,w in enumerate(codes)}
    B=np.zeros((768,5376),dtype=np.int64)
    for i,w in enumerate(basis):
        for v,c in expansion(w).items():B[i,lookup[code(v)]]=c
    rows=[];denominators=[]
    for row in C['horizontal_kernel_coefficients']:
        parsed={int(j):Q(c) for j,c in row.items()}
        denominator=math.lcm(*(c.denominator for c in parsed.values()))
        denominators.append(denominator)
        rows.append({j:int(c*denominator) for j,c in parsed.items()})
    assert len(rows)==270
    pivot_indices=[max(row) for row in rows]
    assert len(set(pivot_indices))==270
    assert all(row.get(j,0)==(denominators[i] if i==k else 0) for i,row in enumerate(rows) for k,j in enumerate(pivot_indices))
    row_norm=max(sum(abs(c) for c in row.values()) for row in rows)
    basis_peak=max(abs(int(B.min())),abs(int(B.max())))
    embedding_bound=row_norm*basis_peak
    assert embedding_bound<2**63
    coefficients=np.zeros((270,768),dtype=np.int64)
    for i,row in enumerate(rows):
        for j,c in row.items():coefficients[i,j]=c
    V=coefficients@B
    maximum=max(abs(int(V.min())),abs(int(V.max())))
    assert maximum<=embedding_bound
    metric=V.copy();bounds=[]
    for pos in range(7):
        assert maximum*4**(pos+1)<2**63
        shift=3*(6-pos);letters=(codes>>shift)&7
        c3=np.flatnonzero(letters==3)
        c4=np.array([lookup[int(codes[i])^(7<<shift)] for i in c3],dtype=np.int64)
        a=metric[:,c3].copy();b=metric[:,c4].copy()
        metric[:,c3]=2*a+b;metric[:,c4]=a+2*b
        metric[:,np.flatnonzero(letters==7)]*=4
        bounds.append(maximum*4**(pos+1))
    # This arbitrary-integer product is intentional: the int64 dot-product
    # bound need not hold even though each individual tensor entry fits.
    FV=flint.fmpz_mat(V.tolist());FM=flint.fmpz_mat(metric.tolist())
    gram=FM*FV.transpose()
    assert gram==gram.transpose() and gram.det()
    files=[]
    for path,data in zip(destinations,(codes,V)):
        with path.open('xb') as stream:np.save(stream,data,allow_pickle=False)
        raw=path.read_bytes();files.append({'file':path.name,'sha256':hashlib.sha256(raw).hexdigest(),'bytes':len(raw)})
    result={'owner':'MathKacMoody-2','degree':[3,3,7],'source':{'file':SOURCE,'sha256':SOURCE_SHA},
            'completed_input_source_replay':{'file':REPLAY,'sha256':REPLAY_SHA},
            'whole_tensor_word_count':5376,'free_Lie_weight_dimension':768,
            'entire_lowest_dimension':270,'normalized_source_basis':'v_new_i=d_i*v_original_i',
            'row_denominators':denominators,'canonical_matrix_change':'A_new[i,j]=A_original[i,j]*d_j/d_i',
            'word_encoding':'first letter is most significant3-bit digit; C-order signed-int64 source rows',
            'source_embedding_int64_upper_bound':embedding_bound,'source_max_abs_coefficient':maximum,
            'metric_entry_int64_upper_bounds':bounds,
            'gram_arithmetic':'FLINT arbitrary-integer full270x5376 times5376x270 matrix product',
            'source_gram':[[str(gram[i,j]) for j in range(270)] for i in range(270)],
            'files':files,'program_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'numpy_version':np.__version__,'flint_version':flint.__version__,
            'status':'COMPLETE_FAITHFUL_INTEGER270_SOURCE_AND_COMPACT_GRAM_CANDIDATE',
            'limits':'Earlier full source membership/completeness replay reused and bound, not rerun. New tensor embedding and Gram require alternate reconstruction/scientific review; no actual small-row ideal, D3 rank, parent, formal/kernel, configured-family/human, native-library or novelty acceptance.'}
    with destinations[-1].open('x') as stream:json.dump(result,stream,indent=2);stream.write('\n')
    print('PASS faithful entire270 tensor source and compact Gram',destinations[-1].name,'maximum',maximum,flush=True)


if __name__=='__main__':main()
