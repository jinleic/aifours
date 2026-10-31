#!/usr/bin/env python3
"""Literal source/seed replay from matrix definitions, importing NO producer.

Rebuild recursive full word universes, integer matrix-unit actions and duals,
ALL proper unshuffle coproducts, full f1/f2 lowerings, exact modular independence,
and EVERY trace/Dynkin seed directly. Canonical NPY bytes are regenerated and
hashed. Shared NumPy integer arithmetic is explicitly not independent-library,
configured-model-family, formal/kernel or human scientific verification.
"""
import argparse
import hashlib
import importlib.util
import io
import itertools
import json
import math
from collections import Counter
from fractions import Fraction as Q
from pathlib import Path

import numpy as np

ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('literal_left_core',ROOT/'frontier-20261029-trace-invariant-left-core.py')
core=importlib.util.module_from_spec(spec)
spec.loader.exec_module(core)


class VerificationError(ArithmeticError):
    pass


def require(condition,reason):
    if not condition:
        raise VerificationError(reason)


def dimensions(n):
    tensor=Counter({(0,0):1})
    for _ in range(n):
        following=Counter()
        for (a,b),c in tensor.items():
            for u,v in core.WEIGHTS:
                following[a+u,b+v]+=c
        tensor=following
    char=Counter(tensor)
    for a,b in core.WEIGHTS:
        char[n*a,n*b]-=1
    require(all(c>=0 and c%n==0 for c in char.values()),'CHARACTER_INTEGRALITY')
    char=Counter({ab:c//n for ab,c in char.items() if c})
    count=char[n,n]-char[n-1,n]-char[n,n-1]+char[n-2,n-1]+char[n-1,n-2]-char[n-2,n-2]
    return tensor,char,count


def permute_codes(codes,permutation,n):
    require(len(permutation)==n and set(permutation)==set(range(n)),'PERMUTATION')
    output=np.zeros(len(codes),dtype=np.uint32)
    for old in permutation:
        output=(output<<np.uint32(3))|((codes>>np.uint32(3*(n-1-old)))&np.uint32(7))
    return output


def modular_determinant(matrix,prime):
    rows=[[int(c)%prime for c in row] for row in matrix]
    result=1
    for j in range(len(rows)):
        pivot=next((i for i in range(j,len(rows)) if rows[i][j]),None)
        if pivot is None:
            return 0
        if pivot!=j:
            rows[pivot],rows[j]=rows[j],rows[pivot]
            result=-result
        value=rows[j][j]
        result=result*value%prime
        inverse=pow(value,-1,prime)
        for i in range(j+1,len(rows)):
            multiplier=rows[i][j]*inverse%prime
            if multiplier:
                rows[i][j:]=[(a-multiplier*b)%prime for a,b in zip(rows[i][j:],rows[j][j:])]
    return result%prime


def literal_duals():
    D=np.zeros((8,3,3),dtype=np.int64)
    for i in range(8):
        for a in range(3):
            for b in range(3):
                c=6*sum(core.GINV[i][j]*int(core.BASIS[j][b,a]) for j in range(8))
                require(c.denominator==1,'DUAL_DENOMINATOR')
                D[i,a,b]=int(c)
    require(core.maximum(D.ravel())<=6,'DUAL_BOUND')
    for i in range(8):
        for j in range(8):
            require(int(np.trace(core.BASIS[i]@D[j]))==6*int(i==j),'DUAL_PAIRING')
    return D


def read_inputs(n,expected_sha):
    name=f'frontier-20261029-level{n}-trace-dynkin-invariants-v1.json'
    raw=(ROOT/name).read_bytes()
    require(hashlib.sha256(raw).hexdigest()==expected_sha,'SOURCE_BYTE_HASH')
    C=json.loads(raw)
    require(C['grade']==n and C['root_degree']==[n,n,n],'SOURCE_GRADE')
    expected_names=[f'frontier-20261029-level{n}-trace-dynkin-invariants-{kind}-v1.npy' for kind in ('words','source')]
    require(len(C['files'])==2 and [p['file'] for p in C['files']]==expected_names,'SOURCE_FILE_SET')
    words,vectors=[core.load_array(pin) for pin in C['files']]
    return C,words,vectors


def check_source(C,words,vectors,n):
    tensor,char,expected=dimensions(n)
    require(expected==({5:6,7:100}[n]),'SOURCE_DIMENSION')
    require(words.dtype==np.dtype('uint32') and words.ndim==1,'WORD_FORMAT')
    require(vectors.dtype==np.dtype('int64') and vectors.shape==(expected,len(words)),'SOURCE_SHAPE')
    source=core.Words(n)
    exhaustive,index=source.root(n,n)
    require(np.array_equal(words,exhaustive) and len(words)==tensor[n,n],'WORD_UNIVERSE')
    bound=2**(n-1)*18**n
    require(bound<2**63,'SOURCE_BOUND_PREMISE')
    require(core.maximum(vectors.ravel())<=bound,'SOURCE_VALUE_BOUND')
    prime=32749
    require(all(prime%d for d in range(2,math.isqrt(prime)+1)),'PRIME')
    detectors=C['coefficient_detector_indices']
    require(len(detectors)==expected==len(set(detectors)) and all(0<=i<len(words) for i in detectors),'DETECTOR_UNIVERSE')
    coproduct=[]
    for cut in range(1,n):
        group=[]
        for subset in itertools.combinations(range(n),cut):
            permutation=subset+tuple(i for i in range(n) if i not in subset)
            mapping=index[permute_codes(words,permutation,n)]
            require(np.all(mapping>=0) and len(np.unique(mapping))==len(words),'COPRODUCT_MAP')
            group.append(mapping)
        coproduct.append(group)
    _,F1=source.action((n,n),'f1')
    _,F2=source.action((n,n),'f2')
    for vector in vectors:
        for group in coproduct:
            require(len(group)*core.maximum(vector)<2**63,'COPRODUCT_BOUND')
            out=np.zeros(len(words),dtype=np.int64)
            for mapping in group:
                # PUSHFORWARD unshuffle, not producer inverse-index pullback.
                out[mapping]+=vector
            require(not np.any(out),'SOURCE_PRIMITIVITY')
        require(not np.any(F1.apply(vector)) and not np.any(F2.apply(vector)),'SOURCE_LEVI_INVARIANCE')
    minor=vectors[:,detectors].tolist()
    determinant=modular_determinant(minor,prime)
    require(determinant!=0,'SOURCE_INDEPENDENCE')
    require(determinant==C['coefficient_minor_determinant_mod_prime'],'SOURCE_MINOR_VALUE')
    require(minor==C['coefficient_minor'],'SOURCE_MINOR_CONTENT')
    D=literal_duals()
    require(D.tolist()==C['scaled_trace_duals'],'SOURCE_DUAL_TABLE')
    # Expand right brackets RECURSIVELY, instead of the producer bitmask rule.
    terms=[((n-1,),1)]
    for j in range(n-2,-1,-1):
        terms=[entry for order,c in terms for entry in (((j,)+order,c),(order+(j,),-c))]
    require(len(terms)==2**(n-1),'DYNKIN_EXPANSION')
    dynkin=[]
    for order,c in terms:
        mapping=index[permute_codes(words,order,n)]
        require(np.all(mapping>=0) and len(np.unique(mapping))==len(words),'DYNKIN_MAP')
        dynkin.append((mapping,c))
    allowed={(5,),(3,2)} if n==5 else {(7,),(5,2),(4,3),(3,2,2)}
    require(len(C['source_provenance'])==expected,'SOURCE_PROVENANCE_COUNT')
    regenerated=np.empty_like(vectors)
    for row,seed in enumerate(C['source_provenance']):
        partition=tuple(seed['partition'])
        permutation=tuple(seed['permutation'])
        require(partition in allowed and sum(partition)==n,'TRACE_PARTITION')
        require(len(permutation)==n and set(permutation)==set(range(n)),'TRACE_PERMUTATION')
        values=np.ones(len(words),dtype=np.int64)
        start=0
        for length in partition:
            product=np.broadcast_to(np.eye(3,dtype=np.int64),(len(words),3,3)).copy()
            for old in permutation[start:start+length]:
                letters=(words>>np.uint32(3*(n-1-old)))&np.uint32(7)
                product=product@D[letters]
            values*=np.trace(product,axis1=1,axis2=2)
            start+=length
        require(core.maximum(values)<=18**n,'TRACE_INTEGER_BOUND')
        vector=np.zeros(len(words),dtype=np.int64)
        for mapping,c in dynkin:
            vector[mapping]+=c*values
        divisor=int(np.gcd.reduce(np.abs(vector)))
        require(divisor>0 and divisor==seed['integer_gcd_divisor'],'SOURCE_SEED_DIVISOR')
        vector//=divisor
        require(np.array_equal(vector,vectors[row]),'SOURCE_SEED_REPLAY')
        regenerated[row]=vector
        if (row+1)%10==0 or row+1==expected:
            print('PASS literal invariant source/seed',n,row+1,'of',expected,flush=True)
    rebuilt=[]
    for array,pin in zip((exhaustive,regenerated),C['files']):
        stream=io.BytesIO()
        np.save(stream,array,allow_pickle=False)
        digest=hashlib.sha256(stream.getvalue()).hexdigest()
        require(digest==pin['sha256'],'SOURCE_BYTE_REPLAY')
        rebuilt.append(digest)
    return {'grade':n,'whole_tensor_weight_word_count':len(words),'whole_free_Lie_weight_dimension':char[n,n],
            'entire_invariant_dimension':expected,'all_proper_unshuffle_cuts':n-1,'all_actual_f1_f2_checks':True,
            'literal_trace_seed_replays':expected,'exact_modular_independence_prime':prime,'nonzero_coefficient_minor':determinant,
            'regenerated_NPY_byte_hashes':rebuilt,'source_mathematical_reconstruction':'literal matrix units/derived weights/duals; recursive exhaustive words; pushforward coproduct; recursively expanded Dynkin brackets; direct per-seed trace contractions',
            'limits':'shared NumPy integer backend; finite-Witt/Weyl/classical-source interfaces are named mathematical inputs, not formal/kernel or scientific adoption.'}


def main():
    if not __debug__:
        raise VerificationError('ASSERTIONS_DISABLED')
    ap=argparse.ArgumentParser()
    ap.add_argument('--grade',type=int,choices=[5,7],required=True)
    ap.add_argument('--source-sha256',required=True)
    args=ap.parse_args()
    C,words,vectors=read_inputs(args.grade,args.source_sha256)
    result=check_source(C,words,vectors,args.grade)
    result.update({'owner':'MathKacMoody-2','input_sha256':args.source_sha256,'program_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                   'literal_core_sha256':hashlib.sha256((ROOT/'frontier-20261029-trace-invariant-left-core.py').read_bytes()).hexdigest(),
                   'numpy_version':np.__version__,'status':'PASS_LITERAL_ENTIRE_INVARIANT_SOURCE_AND_BYTE_SEED_REPLAY',
                   'not_claimed':'D3 rank/injectivity, independent arithmetic library, configured-family/human/formal/kernel, parent/scientific review or novelty acceptance'})
    path=ROOT/f'frontier-20261029-level{args.grade}-trace-invariant-source-replay-v1.json'
    with path.open('x') as stream:
        json.dump(result,stream,indent=2)
        stream.write('\n')
    print('WROTE',path.name,flush=True)


if __name__=='__main__':
    main()
