#!/usr/bin/env python3
"""Alternate whole invariant map: literal LEFT transport and full shifted grid.

The framing/block bookkeeping is adapted from the right-transport program;
the mathematical reconstruction is different: NO producer module is imported,
matrix units/actions/weights/Gram are independently derived, localF3 is derived
from the cyclic words, mixed Cartan terms move LEFT, and theta negatives use
those cyclic words directly (last term F12^2, not -2F1F2F12). Bind the ALREADY
completed literal source/byte-seed replay; do not count it as a new rerun. Shared
NumPy/FLINT libraries are explicit. No configured-family/formal acceptance.
"""
import argparse
import hashlib
import importlib.util
import json
import math
from fractions import Fraction as Q
from multiprocessing import Pool
from pathlib import Path

import numpy as np

ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('literal_source_checker',ROOT/'frontier-20261029-trace-invariant-source-replay.py')
source_checker=importlib.util.module_from_spec(spec)
spec.loader.exec_module(source_checker)
core=source_checker.core
flint=core.flint
DATA=None


def pin(name,expected):
    assert Path(name).name==name
    raw=(ROOT/name).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==expected
    return json.loads(raw)


def qmatrix(rows):
    return core.qmatrix(rows)


def parse_terms(rows,first,second,k):
    result={}
    for term in rows:
        a,b=term[first],term[second]
        assert type(a) is int and type(b) is int and min(a,b)>=0 and a+b<=k
        assert (a,b) not in result
        c=Q(term['coefficient'])
        assert c
        result[a,b]=c
    assert result
    denominator=math.lcm(*(c.denominator for c in result.values()))
    return result,{mon:int(c*denominator) for mon,c in result.items()},denominator


def fixed_columns(terms,x,k):
    powers=[1]*(k+1)
    for j in range(1,k+1):
        powers[j]=powers[j-1]*x
    out=[0]*(k+1)
    for (a,b),c in terms.items():
        out[b]+=c*powers[a]
    return out


def horner(values,x):
    out=0
    for c in reversed(values):
        out=out*x+c
    return out


def init(data):
    global DATA
    DATA=data


def grid_check(task):
    x,y,numerator,denominator,scale=task
    value=int(flint.fmpz_mat([[a+x*b+y*c for a,b,c in row] for row in DATA]).det())
    assert value*denominator==numerator*scale, ('literal-left full polynomial grid mismatch',x,y)
    return x,y


def main():
    if not __debug__:
        raise RuntimeError('ASSERTIONS_DISABLED')
    ap=argparse.ArgumentParser()
    ap.add_argument('--grade',type=int,choices=[5,7],required=True)
    ap.add_argument('--source-sha256',required=True)
    ap.add_argument('--pencil-sha256',required=True)
    ap.add_argument('--half-polynomial-sha256',required=True)
    ap.add_argument('--workers',type=int,default=2)
    ap.add_argument('--block-size',type=int,default=512)
    args=ap.parse_args()
    n=args.grade
    assert 1<=args.workers<=8 and 1<=args.block_size<=4096
    out=ROOT/f'frontier-20261029-level{n}-trace-invariant-left-replay-v1.json'
    if out.exists():
        raise FileExistsError(out)
    C,words,vectors=source_checker.read_inputs(n,args.source_sha256)
    core_sha=hashlib.sha256((ROOT/'frontier-20261029-trace-invariant-left-core.py').read_bytes()).hexdigest()
    source_replay_name=f'frontier-20261029-level{n}-trace-invariant-source-replay-v1.json'
    source_replay_raw=(ROOT/source_replay_name).read_bytes()
    source_replay=json.loads(source_replay_raw)
    assert source_replay['status']=='PASS_LITERAL_ENTIRE_INVARIANT_SOURCE_AND_BYTE_SEED_REPLAY'
    assert source_replay['input_sha256']==args.source_sha256 and source_replay['literal_core_sha256']==core_sha
    assert source_replay['regenerated_NPY_byte_hashes']==[p['sha256'] for p in C['files']]
    k=C['entire_primitive_invariant_dimension']
    tensor,character,expected=source_checker.dimensions(n)
    assert k==expected==({5:6,7:100}[n]) and source_replay['entire_invariant_dimension']==k
    assert words.dtype==np.dtype('uint32') and vectors.dtype==np.dtype('int64') and vectors.shape==(k,len(words))
    assert core.maximum(vectors.ravel())<=2**(n-1)*18**n<2**63
    source=core.Words(n)
    target=core.Words(n-1)
    exhaustive,_=source.root(n,n)
    assert np.array_equal(exhaustive,words) and len(words)==tensor[n,n]
    pname=f'frontier-20261029-level{n}-trace-dynkin-canonical-pencil-v1.json'
    P=pin(pname,args.pencil_sha256)
    hname=f'frontier-20261029-level{n}-trace-invariant-half-level-polynomial-v1.json'
    H=pin(hname,args.half_polynomial_sha256)
    assert P['source_pencil_sha256']==args.source_sha256
    assert P['degree']==H['degree']==[n,n,n] and P['entire_primitive_dimension']==H['entire_primitive_dimension']==k
    assert H['canonical_pencil']=={'file':pname,'sha256':args.pencil_sha256}
    original=pin(H['original_polynomial']['file'],H['original_polynomial']['sha256'])
    assert original['pencil_sha256']==args.pencil_sha256 and original['size']==k and original['degree']==[n,n,n]
    detectors=C['coefficient_detector_indices']
    assert detectors==P['coefficient_detector_indices'] and len(set(detectors))==len(detectors)==k
    coefficient_minor=qmatrix(vectors[:,detectors].T.tolist())
    assert coefficient_minor.det()
    inverse=coefficient_minor.inv()
    F3,tails=core.affine_f3(source,target,n)
    _,F1=source.action((n,n),'f1')
    _,F2=source.action((n,n),'f2')
    images=[np.empty_like(vectors) for _ in range(3)]
    outer_cache={}
    normalization=None
    for j,v in enumerate(vectors):
        assert not np.any(F1.apply(v)) and not np.any(F2.apply(v))
        for tail in tails:
            assert not np.any(tail.apply(v)), 'left degree-zero Cartan/Levi tail did not cancel'
        for piece,operator in enumerate(F3):
            d=operator.apply(v)
            image,common=core.canonical_96(d,target,source,n,outer_cache)
            if normalization is None:
                normalization=2*common
            assert normalization==2*common
            assert not np.any(F1.apply(image)) and not np.any(F2.apply(image))
            images[piece][j]=image
        if (j+1)%10==0 or j+1==k:
            print('PASS literal LEFT whole invariant images',n,j+1,'of',k,flush=True)
    matrices=[]
    blocks=[]
    for piece,image in enumerate(images):
        M=inverse*qmatrix(image[:,detectors].T.tolist())
        denominator=math.lcm(*(int(M[i,j].denominator) for i in range(k) for j in range(k)))
        integer_coefficients=flint.fmpz_mat([[int(M[i,j]*denominator) for j in range(k)] for i in range(k)])
        checked=0
        for start in range(0,len(words),args.block_size):
            end=min(start+args.block_size,len(words))
            A=flint.fmpz_mat(vectors[:,start:end].T.tolist())
            B=flint.fmpz_mat([[int(image[j,w])*denominator for j in range(k)] for w in range(start,end)])
            assert A*integer_coefficients==B, 'literal LEFT full word reconstruction mismatch'
            checked+=1
        matrix=[[Q(int(M[i,j].numerator),int(M[i,j].denominator))/normalization for j in range(k)] for i in range(k)]
        for i in range(k):
            for j in range(k):
                assert matrix[i][j]==Q(P['matrix'][i][j][piece]), ('LEFT/RIGHT canonical matrix mismatch',piece,i,j)
        matrices.append(matrix)
        blocks.append(checked)
        print('PASS literal LEFT EVERY word coordinate',n,'piece',piece,'blocks',checked,flush=True)
    entries=[[[matrices[piece][i][j] for piece in range(3)] for j in range(k)] for i in range(k)]
    half_terms,half_ints,half_den=parse_terms(H['coefficients'],'u_power','v_power',k)
    original_terms,original_ints,original_den=parse_terms(original['coefficients'],'x_power','y_power',k)
    assert half_terms.get((0,0),Q(0))>0 and all(c>0 for c in half_terms.values())
    assert H['lower_parameter_bound']==n//2
    shift=n-n//2
    scales=[math.lcm(*(c.denominator for e in row for c in e)) for row in entries]
    data=[[[int(c*scale) for c in e] for e in row] for row,scale in zip(entries,scales)]
    scale=math.prod(scales)
    tasks=[]
    for i in range(k+1):
        u=i-2
        half_column=fixed_columns(half_ints,u,k)
        original_column=fixed_columns(original_ints,u-shift,k)
        for j in range(k+1-i):
            v=j+1
            numerator=horner(half_column,v)
            assert numerator*original_den==horner(original_column,v-shift)*half_den
            tasks.append((u-shift,v-shift,numerator,half_den,scale))
    with Pool(args.workers,initializer=init,initargs=(data,)) as pool:
        checked=list(pool.imap_unordered(grid_check,tasks,chunksize=16))
    assert len(checked)==(k+1)*(k+2)//2
    result={'owner':'MathKacMoody-2','grade':n,'degree':[n,n,n],'source_input_sha256':args.source_sha256,
            'source_replay':{'file':source_replay_name,'sha256':hashlib.sha256(source_replay_raw).hexdigest()},
            'canonical_pencil_sha256':args.pencil_sha256,'half_level_polynomial_sha256':args.half_polynomial_sha256,
            'entire_invariant_dimension':k,'whole_tensor_weight_word_count':len(words),
            'literal_local_F3_derived_from_cyclic_words':True,'left_degree_zero_tail_checks':True,
            'cyclic_theta_negatives_used_directly_including_F12_squared':True,'computed_integer_normalization':normalization,
            'all3_entire_word_reconstructions':True,'blocks_per_affine_piece':blocks,
            'all_affine_coefficients_match_right_transport_pencil':True,'strictly_positive_half_level_coefficients':len(half_terms),
            'half_level_lower_parameter_bound':n//2,'exact_complete_shifted_matrix_determinants':len(checked),
            'grid':'u=i-2,v=j+1,i,j>=0,i+j<=dimension; x=u-(grade-bound),y=v-(grade-bound)',
            'polynomial_identity_and_matrix_truth_checked_on_same_full_unisolvent_grid':True,
            'program_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'literal_core_sha256':core_sha,
            'numpy_version':np.__version__,'flint_version':flint.__version__,
            'status':'PASS_ALTERNATE_ENTIRE_INVARIANT_MATRIX_AND_HALF_LEVEL_POLYNOMIAL',
            'limits':'Literal source/byte seed replay was separately completed and bound, not credited as a new rerun. Shared word-index/block framing and NumPy/FLINT exact libraries; mathematically different LEFT mixed-Cartan transport, freshly derived literal normalizations and cyclic theta negatives. Actual source/adjoint transport and D3-kernel containment remain explicit WRITTEN imports pending scientific review. No configured-family/human/formal/kernel, native-library, parent or novelty acceptance.'}
    with out.open('x') as stream:
        json.dump(result,stream,indent=2)
        stream.write('\n')
    print('PASS alternate COMPLETE invariant map',n,'dimension',k,'matrix grid',len(checked),'lower bound',n//2,out.name,flush=True)


if __name__=='__main__':
    main()
