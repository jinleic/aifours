#!/usr/bin/env python3
"""Complete canonical contraction pencil for any level7 lowest root(a,b,7).

Generalizes the pinned invariant word-level generator from root(n,n) to an
arbitrary root. Source: complete integer tensor-word lowest vectors. Every
source/output is checked f1/f2-lowest, every right degree-zero tail must
cancel, and all three affine output matrices are reconstructed in EVERY word
coordinate by arbitrary-integer identities. Signed-int64 bounds are asserted.
"""
import argparse
import hashlib
import importlib.util
import io
import json
import math
from fractions import Fraction as Q
from pathlib import Path

import numpy as np

ROOT=Path(__file__).resolve().parent
BASE='frontier-20261029-trace-invariant-canonical.py'
BASE_SHA='80ed94050a08dd39cc3878da2c4d2ee837aa3e1777f852a139db477702efd1fb'
N=7


def load_base():
    raw=(ROOT/BASE).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==BASE_SHA,'pinned invariant generator mismatch'
    spec=importlib.util.spec_from_file_location('pinned_word_level_tools',ROOT/BASE)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    return module


T=load_base()
local=T.local;flint=T.flint;Transfer=T.Transfer;Words=T.Words;maximum=T.maximum;difference=T.difference
LIMIT=T.LIMIT


def affine_f3(source,target,a,b):
    n=N
    codes,_=source.root(a,b)
    out_codes,out_index=target.root(a,b)
    letters=[((codes>>np.uint32(3*(n-1-i)))&np.uint32(7)) for i in range(n)]
    maps=[[],[],[]]
    tails={g:[[],[],[]] for g in ('h3','e1','e2','e12')}
    tail_roots={'h3':(a,b),'e1':(a-1,b),'e2':(a,b-1),'e12':(a-1,b-1)}
    local_brackets=[('h3',(-1,0,0)),('e1',(-n,-1,0)),('e2',(-n,0,-1)),('e12',(-2*n,-1,-1)),('e12',(-n,0,-1))]
    for k in range(n):
        shift=3*(n-1-k)
        shortened=((codes>>(shift+3))<<shift)|(codes&np.uint32((1<<shift)-1))
        for j,(g,co) in enumerate(local_brackets):
            inputs=np.flatnonzero(letters[k]==j).astype(np.int32)
            _,tail_index=target.root(*tail_roots[g])
            outputs=tail_index[shortened[inputs]]
            for piece,c in enumerate(co):
                tails[g][piece].append((inputs,outputs,c))
            for ell in range(k+1,n):
                action_shift=3*(n-1-ell)
                for old in range(8):
                    selected=np.flatnonzero((letters[k]==j)&(letters[ell]==old)).astype(np.int32)
                    if not len(selected):
                        continue
                    if g=='h3':
                        x,y=local.levi.WEIGHTS[old]
                        choices={old:(-4+2*n*(x+y),2*x,2*y)}
                    else:
                        choices={new:tuple(c*act for c in co) for new,act in local.ACTION[g][old].items()}
                    for new,values in choices.items():
                        changed=shortened[selected].astype(np.int64)+(new-old)*(1<<action_shift)
                        assert np.all(changed>=0) and np.all(changed<len(target.all))
                        outputs=out_index[changed]
                        for piece,c in enumerate(values):
                            maps[piece].append((selected,outputs,int(c)))
    f3=[Transfer(len(codes),len(out_codes),part) for part in maps]
    tail_checks=[]
    for g,parts in tails.items():
        tail_codes,_=target.root(*tail_roots[g])
        tail_checks.extend(Transfer(len(codes),len(tail_codes),part) for part in parts)
    return f3,tail_checks


def canonical_96(d,word_space,source_space,a,b,outer_cache):
    n=N;root=(a,b)
    r1,F1=word_space.action(root,'f1')
    r2,F2=word_space.action(root,'f2')
    f1=F1.apply(d);f2=F2.apply(d)
    rr,F2_after1=word_space.action(r1,'f2')
    rr2,F1_after2=word_space.action(r2,'f1')
    assert rr==rr2
    f21=F2_after1.apply(f1);f12=F1_after2.apply(f2)
    h=difference(f21,f12)
    r5,H1=word_space.action(rr,'f1')
    r6,H2=word_space.action(rr,'f2')
    h1=H1.apply(h);h2=H2.apply(h)
    r7,H12=word_space.action(r6,'f1')
    h12=H12.apply(h2)
    negative=[(root,d,1,1),(r1,f1,2,-1),(r2,f2,2,-1),(rr,h,4,-1),
              (rr,f12,4,1),(r5,h1,8,1),(r6,h2,8,1),(r7,h12,8,-1)]
    source_codes,source_index=source_space.root(a,b)
    terms=[];bound=0
    for j,(degree,v,den,sign) in enumerate(negative):
        for i in range(8):
            factor=96*local.GINV[i][j]*sign/den
            assert factor.denominator==1
            factor=int(factor)
            if not factor:
                continue
            key=(i,degree)
            if key not in outer_cache:
                codes,_=word_space.root(*degree)
                left=source_index[(np.uint32(i)<<np.uint32(3*(n-1)))|codes]
                right=source_index[(codes<<np.uint32(3))|np.uint32(i)]
                assert np.all(left>=0) and np.all(right>=0)
                assert len(np.unique(left))==len(left) and len(np.unique(right))==len(right)
                outer_cache[key]=(left,right)
            terms.append((v,*outer_cache[key],factor))
            bound+=2*abs(factor)*maximum(v)
    assert bound<LIMIT,'int64 complete outer-bracket bound not established'
    out=np.zeros(len(source_codes),dtype=np.int64)
    for v,left,right,factor in terms:
        out[left]+=factor*v
        out[right]-=factor*v
    return out


def pinned_array(pin):
    raw=(ROOT/pin['file']).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==pin['sha256']
    stream=io.BytesIO(raw);array=np.load(stream,allow_pickle=False)
    assert stream.tell()==len(raw)
    return array


def main():
    if not __debug__:raise RuntimeError('assertions disabled')
    ap=argparse.ArgumentParser()
    ap.add_argument('--source',required=True);ap.add_argument('--source-sha256',required=True)
    ap.add_argument('--block-size',type=int,default=512)
    args=ap.parse_args()
    assert Path(args.source).name==args.source and 1<=args.block_size<=4096
    raw=(ROOT/args.source).read_bytes();assert hashlib.sha256(raw).hexdigest()==args.source_sha256
    C=json.loads(raw);a,b,n=C['degree'];assert n==N
    words=pinned_array(C['files'][0]);vectors=pinned_array(C['files'][1])
    k=C['entire_lowest_dimension']
    assert vectors.shape==(k,len(words)) and vectors.dtype==np.dtype('int64') and words.dtype==np.dtype('uint32')
    source=Words(N);target=Words(N-1)
    expected,_=source.root(a,b)
    assert np.array_equal(words,expected),'word universe mismatch or omitted words'
    detectors=C['coefficient_detector_indices']
    assert len(detectors)==k==len(set(detectors)) and all(0<=j<len(words) for j in detectors)
    minor=flint.fmpz_mat(vectors[:,detectors].T.tolist())
    assert minor.det()
    inverse=flint.fmpq_mat(minor).inv()
    path=ROOT/f'frontier-20261029-level7-{a}{b}-general-canonical-pencil-v1.json'
    if path.exists():raise FileExistsError(path)
    F3,tails=affine_f3(source,target,a,b)
    _,source_f1=source.action((a,b),'f1')
    _,source_f2=source.action((a,b),'f2')
    images=[np.empty_like(vectors) for _ in range(3)]
    outer_cache={}
    for i,v in enumerate(vectors):
        assert not np.any(source_f1.apply(v)) and not np.any(source_f2.apply(v))
        for tail in tails:
            assert not np.any(tail.apply(v)),'right degree-zero tail did not cancel'
        for piece,operator in enumerate(F3):
            d=operator.apply(v)
            out=canonical_96(d,target,source,a,b,outer_cache)
            assert not np.any(source_f1.apply(out)) and not np.any(source_f2.apply(out))
            images[piece][i]=out
        if (i+1)%50==0 or i+1==k:print('ENTIRE WORD canonical',(a,b,7),i+1,'of',k,flush=True)
    matrices=[];blocks_done=[]
    for piece,image in enumerate(images):
        M=inverse*flint.fmpq_mat(image[:,detectors].T.tolist())
        denominator=math.lcm(*(int(M[i,j].denominator) for i in range(k) for j in range(k)))
        integer=flint.fmpz_mat(k,k,[int(M[i,j]*denominator) for i in range(k) for j in range(k)])
        blocks=0
        for start in range(0,len(words),args.block_size):
            end=min(start+args.block_size,len(words))
            A=flint.fmpz_mat(vectors[:,start:end].T.tolist())
            B=flint.fmpz_mat((image[:,start:end].T.astype(object)*denominator).tolist())
            assert A*integer==B,'full canonical word-coordinate reconstruction failed'
            blocks+=1
        matrices.append([[Q(int(M[i,j].numerator),int(M[i,j].denominator))/192 for j in range(k)] for i in range(k)])
        blocks_done.append(blocks)
        print('PASS EVERY word coordinate',(a,b,7),'piece',piece,'blocks',blocks,flush=True)
    entries=[[[matrices[p][i][j] for p in range(3)] for j in range(k)] for i in range(k)]
    record={'owner':'MathKacMoody-2','degree':[a,b,7],'variable_meaning':'x=r-7,y=s-7',
            'source_pencil':args.source,'source_pencil_sha256':args.source_sha256,'source_files':C['files'],
            'entire_primitive_dimension':k,'whole_tensor_weight_word_count':len(words),
            'matrix':[[[str(c) for c in e] for e in row] for row in entries],
            'coefficient_detector_indices':detectors,'all_source_and_output_full_f1_f2_checks':True,
            'all_affine_right_degree_zero_tails_cancelled':True,'all3_entire_word_coordinate_reconstructions':True,
            'word_coordinate_block_size':args.block_size,'blocks_per_affine_piece':blocks_done,
            'canonical_normalization':'F3 operators produce2*F3; canonical outer sum produces96*Omega, hence divide192',
            'f3_affine_integer_operator_norms':[op.norm for op in F3],
            'program_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'base_word_tools':{'file':BASE,'sha256':BASE_SHA},
            'numpy_version':np.__version__,'flint_version':flint.__version__,
            'status':'COMPLETE_EXACT_WORD_LEVEL_GENERAL_CANONICAL_PENCIL_CANDIDATE',
            'limits':'Entire source/target word arithmetic with explicit int64 bounds and arbitrary-integer full reconstructions. Source completeness and D3-kernel containment are separate obligations. No determinant/injectivity, parent, formal/kernel or novelty acceptance.'}
    with path.open('x') as stream:json.dump(record,stream,indent=2);stream.write('\n')
    print('WROTE',path.name,'dimension',k,'words',len(words),flush=True)


if __name__=='__main__':main()
