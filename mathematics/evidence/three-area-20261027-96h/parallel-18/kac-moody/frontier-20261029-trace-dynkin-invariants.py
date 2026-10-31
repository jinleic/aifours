#!/usr/bin/env python3
"""Construct ENTIRE free-Lie invariant sources by explicit trace/Dynkin tensors.

No FFT spanning theorem is assumed: every selected integer vector is physically
checked primitive under the FULL unshuffle coproduct and killed by BOTH actual
finite-Levi lowerings. A nonzero exact modular coefficient minor proves their
Q-independence; the independent Witt/Weyl count proves ENTIRE-source coverage.
All NumPy arithmetic is signed int64 with WRITTEN integer bounds checked BEFORE
it is used. No floats, numerical rank, solver or source omission is involved.
Allowed grades5,7 are prime. The grade5 complete source is a positive control.
"""
import argparse
import hashlib
import importlib.util
import itertools
import json
import math
import random
from collections import Counter
from fractions import Fraction as Q
from pathlib import Path

import numpy as np

ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('literal_positive_local_module',ROOT/'frontier-20261029-level6-canonical-contraction.py')
local=importlib.util.module_from_spec(spec)
spec.loader.exec_module(local)


def prime_character(n):
    ch=Counter({(0,0):1})
    for _ in range(n):
        following=Counter()
        for (a,b),c in ch.items():
            for u,v in local.levi.WEIGHTS:
                following[a+u,b+v]+=c
        ch=following
    tensor=Counter(ch)
    for a,b in local.levi.WEIGHTS:
        ch[n*a,n*b]-=1
    assert all(c>=0 and c%n==0 for c in ch.values())
    ch=Counter({ab:c//n for ab,c in ch.items() if c})
    invariant=ch[n,n]-ch[n-1,n]-ch[n,n-1]+ch[n-2,n-1]+ch[n-1,n-2]-ch[n-2,n-2]
    return tensor,ch,invariant


def scaled_duals():
    B=np.zeros((8,3,3),dtype=np.int64)
    for i,matrix in enumerate(local.levi.BASIS):
        for (a,b),c in matrix.items():
            assert Q(c).denominator==1
            B[i,a-1,b-1]=int(c)
    D=np.zeros((8,3,3),dtype=np.int64)
    for i in range(8):
        for a in range(3):
            for b in range(3):
                c=6*sum(local.GINV[i][j]*int(B[j,b,a]) for j in range(8))
                assert c.denominator==1
                D[i,a,b]=int(c)
    assert np.max(np.abs(D))<=6
    for i in range(8):
        for j in range(8):
            assert int(np.trace(B[i]@D[j]))==6*int(i==j)
    return D


def permuted(codes,permutation,n):
    assert len(permutation)==n and set(permutation)==set(range(n))
    out=np.zeros(len(codes),dtype=np.uint32)
    for new,old in enumerate(permutation):
        out|=((codes>>np.uint32(3*(n-1-old)))&np.uint32(7))<<np.uint32(3*(n-1-new))
    return out


def root_words(n,tensor):
    codes=np.arange(8**n,dtype=np.uint32)
    a=np.zeros(8**n,dtype=np.int16)
    b=np.zeros(8**n,dtype=np.int16)
    weights=np.array(local.levi.WEIGHTS,dtype=np.int16)
    for i in range(n):
        letters=(codes>>np.uint32(3*(n-1-i)))&np.uint32(7)
        a+=weights[letters,0]
        b+=weights[letters,1]
    roots={degree:codes[(a==degree[0])&(b==degree[1])] for degree in ((n,n),(n-1,n),(n,n-1))}
    for degree,words in roots.items():
        assert len(words)==tensor[degree]
    return roots


def position_map(codes,index,permutation,n):
    mapping=index[permuted(codes,permutation,n)]
    assert np.all(mapping>=0) and len(np.unique(mapping))==len(codes)
    inverse=np.empty(len(codes),dtype=np.int32)
    inverse[mapping]=np.arange(len(codes),dtype=np.int32)
    return mapping,inverse


def base_tensor(codes,partition,n,D):
    # General trace bound: at most3^n paths, each product <=6^n.
    assert 18**n<2**63
    result=np.ones(len(codes),dtype=np.int64)
    position=0
    for length in partition:
        product=np.broadcast_to(np.eye(3,dtype=np.int64),(len(codes),3,3)).copy()
        for i in range(position,position+length):
            letters=(codes>>np.uint32(3*(n-1-i)))&np.uint32(7)
            product=product@D[letters]
        result*=np.trace(product,axis1=1,axis2=2)
        position+=length
    assert position==n and int(np.max(np.abs(result)))<=18**n
    return result


def trace_patterns(n):
    partitions=[(5,),(3,2)] if n==5 else [(7,),(5,2),(4,3),(3,2,2)]
    patterns=[]
    for partition in partitions:
        seen=set()
        for permutation in itertools.permutations(range(n)):
            cycles=[]
            start=0
            for length in partition:
                cycle=permutation[start:start+length]
                rotations=[cycle[i:]+cycle[:i] for i in range(length)]
                cycles.append(min(rotations))
                start+=length
            key=tuple(sorted(cycles))
            if key not in seen:
                seen.add(key)
                patterns.append((partition,permutation))
    assert len(patterns)==(44 if n==5 else 1854)
    return partitions,patterns


def integer_modular_determinant(matrix,p):
    A=[[int(c)%p for c in row] for row in matrix]
    det=1
    for j in range(len(A)):
        pivot=next((i for i in range(j,len(A)) if A[i][j]),None)
        if pivot is None:
            return 0
        if pivot!=j:
            A[pivot],A[j]=A[j],A[pivot]
            det=-det
        value=A[j][j]
        det=det*value%p
        inverse=pow(value,-1,p)
        for i in range(j+1,len(A)):
            multiplier=A[i][j]*inverse%p
            if multiplier:
                for k in range(j+1,len(A)):
                    A[i][k]=(A[i][k]-multiplier*A[j][k])%p
            A[i][j]=0
    return det%p


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--grade',type=int,choices=[5,7],required=True)
    ap.add_argument('--seed',type=int,default=20261029)
    args=ap.parse_args()
    n=args.grade
    prefix=f'frontier-20261029-level{n}-trace-dynkin-invariants'
    paths=[ROOT/f'{prefix}-words-v1.npy',ROOT/f'{prefix}-source-v1.npy',ROOT/f'{prefix}-v1.json']
    if any(path.exists() for path in paths):
        raise FileExistsError('refusing to replace an existing trace/Dynkin artifact')
    tensor,character,expected=prime_character(n)
    assert expected==({5:6,7:100}[n])
    roots=root_words(n,tensor)
    codes=roots[n,n]
    count=len(codes)
    index=np.full(8**n,-1,dtype=np.int32)
    index[codes]=np.arange(count,dtype=np.int32)
    D=scaled_duals()
    dynkin=[]
    for mask in range(2**(n-1)):
        left=tuple(i for i in range(n-1) if not (mask>>i)&1)
        right=tuple(i for i in range(n-2,-1,-1) if (mask>>i)&1)
        permutation=left+(n-1,)+right
        _,inverse=position_map(codes,index,permutation,n)
        dynkin.append(((-1)**mask.bit_count(),inverse))
    coproduct=[]
    for cut in range(1,n):
        group=[]
        for subset in itertools.combinations(range(n),cut):
            permutation=subset+tuple(i for i in range(n) if i not in subset)
            _,inverse=position_map(codes,index,permutation,n)
            group.append(inverse)
        coproduct.append(group)
    levi_maps={}
    for g,degree in (('f1',(n-1,n)),('f2',(n,n-1))):
        target=roots[degree]
        target_index=np.full(8**n,-1,dtype=np.int32)
        target_index[target]=np.arange(len(target),dtype=np.int32)
        maps=[]
        for position in range(n):
            shift=3*(n-1-position)
            letters=(codes>>np.uint32(shift))&np.uint32(7)
            for old,row in enumerate(local.ACTION[g]):
                inputs=np.flatnonzero(letters==old).astype(np.int32)
                for new,coefficient in row.items():
                    # Signed intermediate avoids unsigned wrap for a lowering.
                    changed=codes[inputs].astype(np.int64)+(new-old)*(1<<shift)
                    assert np.all(changed>=0) and np.all(changed<8**n)
                    outputs=target_index[changed]
                    assert np.all(outputs>=0) and len(np.unique(outputs))==len(outputs)
                    maps.append((inputs,outputs,int(coefficient)))
        levi_maps[g]=(len(target),maps)
    partitions,patterns=trace_patterns(n)
    random.Random(args.seed).shuffle(patterns)
    bases={part:base_tensor(codes,part,n,D) for part in partitions}
    assert 2**(n-1)*18**n<2**63
    p=32749
    assert all(p%d for d in range(2,math.isqrt(p)+1)) and p*p<2**63
    echelon={}
    accepted=[]
    provenance=[]
    scratch=np.empty(count,dtype=np.int64)
    attempts=0
    for partition,permutation in patterns:
        attempts+=1
        mapping=index[permuted(codes,permutation,n)]
        assert np.all(mapping>=0)
        coefficients=bases[partition][mapping]
        vector=np.zeros(count,dtype=np.int64)
        for sign,inverse in dynkin:
            if sign==1:
                vector+=coefficients[inverse]
            else:
                vector-=coefficients[inverse]
        divisor=int(np.gcd.reduce(np.abs(vector)))
        if not divisor:
            continue
        vector//=divisor
        residual=vector%p
        for pivot,row in sorted(echelon.items()):
            factor=int(residual[pivot])
            if factor:
                np.multiply(row,factor,out=scratch)
                residual-=scratch
                residual%=p
        nonzero=np.flatnonzero(residual)
        if not len(nonzero):
            continue
        pivot=int(nonzero[0])
        np.multiply(residual,pow(int(residual[pivot]),-1,p),out=residual)
        residual%=p
        echelon[pivot]=residual.copy()
        maximum=int(np.max(np.abs(vector)))
        assert 2**(n-1)*maximum<2**63
        for group in coproduct:
            out=np.zeros(count,dtype=np.int64)
            for inverse in group:
                out+=vector[inverse]
            assert not np.any(out), 'FULL unshuffle primitive identity failed'
        for g,(length,maps) in levi_maps.items():
            bound=8*n*max(abs(c) for row in local.ACTION[g] for c in row.values())*maximum
            assert bound<2**63
            out=np.zeros(length,dtype=np.int64)
            for inputs,outputs,c in maps:
                out[outputs]+=c*vector[inputs]
            assert not np.any(out), 'FULL actual finite-Levi lowering failed'
        accepted.append(vector)
        provenance.append({'partition':list(partition),'permutation':list(permutation),'integer_gcd_divisor':divisor,'coefficient_pivot_index':pivot,'maximum_absolute_coefficient':maximum})
        print('EXACT trace/Dynkin invariant source',n,'rank',len(accepted),'of',expected,'attempts',attempts,flush=True)
        if len(accepted)==expected:
            break
    assert len(accepted)==expected, 'trace/Dynkin representation did not supply the entire invariant source'
    detectors=[e['coefficient_pivot_index'] for e in provenance]
    minor=[[int(vector[j]) for j in detectors] for vector in accepted]
    determinant=integer_modular_determinant(minor,p)
    assert determinant, 'exact modular coefficient independence minor vanished'
    source=np.stack(accepted)
    np.save(paths[0],codes,allow_pickle=False)
    np.save(paths[1],source,allow_pickle=False)
    record={'owner':'MathKacMoody-2','grade':n,'root_degree':[n,n,n],
            'entire_tensor_weight_word_count':count,'entire_free_Lie_weight_dimension':character[n,n],
            'entire_primitive_invariant_dimension':expected,'actual_source_scope':f'free source only; actual on r,s>={n} at the named actual free-Levi/PBW interface',
            'source_encoding':'C-order npy signed-int64 array: rows are whole integer Lie polynomials, columns indexed by words.npy uint32 codes; word first letter occupies most significant3-bit group',
            'dual_basis_integer_scale':6,'scaled_trace_duals':D.tolist(),'trace_pattern_universe':len(patterns),
            'candidate_order_seed':args.seed,'candidate_attempts':attempts,'source_provenance':provenance,
            'all_proper_unshuffle_coproduct_cuts_checked':n-1,'all_full_actual_f1_f2_lowerings_checked':True,
            'integer_bounds':{'unscaled_trace_tensor':18**n,'Dynkin_sum':2**(n-1)*18**n,'int64_limit':2**63},
            'coefficient_independence_prime':p,'coefficient_detector_indices':detectors,'coefficient_minor':minor,'coefficient_minor_determinant_mod_prime':determinant,
            'files':[{'file':path.name,'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'bytes':path.stat().st_size} for path in paths[:2]],
            'program_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'status':'COMPLETE_EXACT_TRACE_DYNKIN_INVARIANT_SOURCE_CANDIDATE',
            'limits':'Constructive full invariant source only, NOT D3 injectivity, Serre equality, parent/scientific review, independent arithmetic implementation, formal/kernel, configured-family/human or novelty acceptance. FFT spanning theorem is NOT assumed.'}
    with paths[2].open('x') as stream:
        json.dump(record,stream,indent=2)
        stream.write('\n')
    print('WROTE',paths[2].name,'ENTIRE invariant source',expected,'words',count,'minor mod prime',determinant,flush=True)


if __name__=='__main__':
    main()
